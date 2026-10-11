#!/usr/bin/env python3
"""Fetch DVIDS page text, download rows, and optional SHA-256 hashes.

Writes sources/dvids/enrichment-2026-10-06.json. Does not save media files.

    python scripts/fetch_dvids_enrichment.py
    python scripts/fetch_dvids_enrichment.py --skip-hash
    python scripts/fetch_dvids_enrichment.py --hash-only

The catalog's DVIDS ids come from sources/dvids/metadata-2026-10-06.json,
which is left unchanged.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import ssl
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIOR = ROOT / "sources" / "dvids" / "metadata-2026-10-06.json"
OUT = ROOT / "sources" / "dvids" / "enrichment-2026-10-06.json"
FETCH_DATE = "2026-10-06"
UA = "uap-open-archive/1.1 (research; +https://github.com/pauldavid1974/uap-open-archive)"
WORKERS = 8

FIELD_MAP = {
    "Date Taken": "date_taken",
    "Date Posted": "date_posted",
    "Length": "duration",
    "Location": "location",
    "VIRIN": "virin",
    "Filename": "filename",
    "Category": "category",
    "Video ID": "video_id_field",
}


def fetch(url: str, method: str = "GET", timeout: int = 45, max_bytes: int | None = None) -> tuple[int, str, dict, bytes]:
    request = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = response.status
            final = response.geturl()
            headers = {key.lower(): value for key, value in response.headers.items()}
            if method == "HEAD":
                return status, final, headers, b""
            if max_bytes is None:
                body = response.read()
            else:
                body = response.read(max_bytes)
            return status, final, headers, body
    except urllib.error.HTTPError as exc:
        headers = {key.lower(): value for key, value in exc.headers.items()} if exc.headers else {}
        body = exc.read(max_bytes or 2000) if method != "HEAD" else b""
        return exc.code, url, headers, body


def fetch_retry(url: str, method: str = "GET", timeout: int = 45, attempts: int = 3) -> tuple[int, str, dict, bytes]:
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            return fetch(url, method=method, timeout=timeout)
        except (urllib.error.URLError, TimeoutError, ssl.SSLError, ConnectionError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"{method} {url} failed: {last}")


def html_to_text(fragment: str) -> str:
    fragment = re.sub(r"(?i)<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"(?i)</p>", "\n\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    text = html.unescape(fragment).replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.strip() for line in text.split("\n")]
    cleaned: list[str] = []
    blank = 0
    for line in lines:
        if line == "":
            blank += 1
            if blank <= 1:
                cleaned.append("")
        else:
            blank = 0
            cleaned.append(line)
    return "\n".join(cleaned).strip()


def blank_to_none(value: str | None) -> str | None:
    if value is None:
        return None
    text = html.unescape(re.sub(r"\s+", " ", value)).strip()
    return text or None


def parse_page(page_html: str) -> dict:
    title_match = re.search(r'<h1 class="asset-title">(.*?)</h1>', page_html, re.S)
    title = html_to_text(title_match.group(1)) if title_match else None
    title_source = "h1.asset-title" if title else None
    if not title:
        og = re.search(r'property="og:title" content="(.*?)"', page_html, re.S)
        if og:
            title = blank_to_none(og.group(1))
            title_source = "og:title"

    fields: dict[str, str] = {}
    for label, value in re.findall(r"<tr>\s*<td>([^<:]+):</td>\s*<td>(.*?)</td>\s*</tr>", page_html, re.S):
        key = html_to_text(label)
        val = html_to_text(value)
        if key and key not in fields:
            fields[key] = val

    paragraph = None
    paragraph_match = re.search(
        r'<div class="uk-width-1-1" style="clear: both;"></div>\s*<p>(.*?)</p>',
        page_html,
        re.S,
    )
    if paragraph_match:
        paragraph = html_to_text(paragraph_match.group(1)) or None
    og_desc = None
    og_match = re.search(r'property="og:description" content="(.*?)"\s*/?>', page_html, re.S)
    if og_match:
        og_desc = html_to_text(html.unescape(og_match.group(1))) or None

    description = paragraph or og_desc
    if paragraph:
        description_source = "page_paragraph"
    elif og_desc:
        description_source = "og:description"
    else:
        description_source = None

    media = re.findall(r"https://d34w7g4gy10iej\.cloudfront\.net/video/[^\"'\s]+\.mp4", page_html)
    m3u8 = re.search(r'src="(/video/\d+\.m3u8)"', page_html)
    tracks = re.findall(r"<track\b[^>]*>", page_html, re.I)
    caption_links = re.findall(r'href="([^"]+\.(?:vtt|srt))"', page_html, re.I)
    transcript_heading = bool(
        re.search(r"<h[1-4][^>]*>\s*(transcript|closed captions?|subtitles)\s*</h[1-4]>", page_html, re.I)
    )
    return {
        "title": title or None,
        "title_source": title_source,
        "fields": fields,
        "description": description,
        "description_source": description_source,
        "media_urls": list(dict.fromkeys(media)),
        "m3u8_path": m3u8.group(1) if m3u8 else None,
        "track_elements": len(tracks),
        "caption_links": caption_links,
        "transcript_heading": transcript_heading,
    }


def parse_popup(popup_html: str) -> list[dict]:
    rows = []
    pattern = re.compile(
        r'<td>\s*<a href="(/download/videofile/\d+)"[^>]*>.*?</a>\s*</td>\s*'
        r"<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>",
        re.S | re.I,
    )
    for href, resolution, bitrate, size in pattern.findall(popup_html):
        resolution_text = blank_to_none(html_to_text(resolution))
        bitrate_text = blank_to_none(html_to_text(bitrate))
        if bitrate_text and re.fullmatch(r"kbps", bitrate_text, re.I):
            bitrate_text = None
        rows.append(
            {
                "resolution": resolution_text,
                "size_stated": blank_to_none(html_to_text(size)),
                "size_bytes": None,
                "bitrate_stated": bitrate_text,
                "url": "https://www.dvidshub.net" + href,
                "http_status": None,
            }
        )
    return rows


def parse_m3u8(text: str) -> tuple[list[dict], int]:
    variants = []
    subtitle_renditions = 0
    lines = text.splitlines()
    pending_bandwidth = None
    pending_resolution = None
    for line in lines:
        if "TYPE=SUBTITLES" in line or "TYPE=CLOSED-CAPTIONS" in line:
            subtitle_renditions += 1
        bandwidth = re.search(r"BANDWIDTH=(\d+)", line)
        resolution = re.search(r"RESOLUTION=(\d+x\d+)", line)
        if line.startswith("#EXT-X-STREAM-INF"):
            pending_bandwidth = int(bandwidth.group(1)) if bandwidth else None
            pending_resolution = resolution.group(1) if resolution else None
            continue
        if pending_bandwidth is not None and line and not line.startswith("#"):
            filename_resolution = re.search(r"(\d+x\d+)", line)
            variants.append(
                {
                    "bandwidth": pending_bandwidth,
                    "resolution": pending_resolution
                    or (filename_resolution.group(1) if filename_resolution else None),
                    "url": line.strip(),
                }
            )
            pending_bandwidth = None
            pending_resolution = None
    return variants, subtitle_renditions


def head_download(row: dict) -> dict:
    try:
        status, _final, headers, _body = fetch_retry(row["url"], method="HEAD", timeout=25)
    except RuntimeError as exc:
        row = dict(row)
        row["http_status"] = None
        row["head_error"] = str(exc)
        return row
    row = dict(row)
    row["http_status"] = status
    length = headers.get("content-length")
    if status == 200 and length and length.isdigit():
        row["size_bytes"] = int(length)
    return row


def one_id(dvids_id: str) -> dict:
    page_url = f"https://www.dvidshub.net/video/{dvids_id}"
    popup_url = f"https://www.dvidshub.net/download/popup/{dvids_id}"
    record: dict = {
        "dvids_id": dvids_id,
        "fetch_date": FETCH_DATE,
        "fetch_status": "failed",
        "fetch_error": None,
        "page_url_requested": page_url,
        "page_url": None,
        "popup_url": popup_url,
        "popup_status": None,
        "title": None,
        "title_source": None,
        "date_taken": None,
        "date_posted": None,
        "duration": None,
        "location": None,
        "virin": None,
        "filename": None,
        "category": None,
        "video_id_field": None,
        "other_fields": {},
        "description": None,
        "description_source": None,
        "fields_unknown": [],
        "downloads": [],
        "downloads_note": None,
        "player_media": {
            "url": None,
            "content_length": None,
            "etag": None,
            "content_type": None,
            "head_status": None,
            "sha256": None,
            "sha256_bytes": None,
            "sha256_note": "SHA-256 was not computed yet.",
        },
        "hls_variants": [],
        "captions": {
            "status": "unknown",
            "kind": None,
            "source_url": None,
            "text": None,
            "checks": {
                "track_elements": 0,
                "vtt_or_srt_links": 0,
                "transcript_heading": False,
                "hls_subtitle_renditions": 0,
            },
            "note": "The page was not fetched.",
        },
    }
    try:
        status, final, _headers, body = fetch_retry(page_url)
    except RuntimeError as exc:
        record["fetch_error"] = str(exc)
        record["captions"]["note"] = "The DVIDS page request failed, so title, date, duration, description, downloads, and captions are unknown."
        return record
    if status != 200:
        record["fetch_error"] = f"HTTP {status} for {page_url}"
        record["captions"]["note"] = f"The DVIDS page returned HTTP {status}. Title, date, duration, description, and captions are unknown."
        return record
    parsed = parse_page(body.decode("utf-8", "replace"))
    record["fetch_status"] = "ok"
    record["page_url"] = final
    record["title"] = parsed["title"]
    record["title_source"] = parsed["title_source"]
    record["description"] = parsed["description"]
    record["description_source"] = parsed["description_source"]
    mapped = {}
    for label, key in FIELD_MAP.items():
        value = blank_to_none(parsed["fields"].get(label))
        record[key] = value
        mapped[label] = True
        if value is None:
            record["fields_unknown"].append(key)
    for label, value in parsed["fields"].items():
        if label not in FIELD_MAP:
            record["other_fields"][label] = value
    if parsed["media_urls"]:
        media_url = parsed["media_urls"][0]
        record["player_media"]["url"] = media_url
        try:
            head_status, _final, headers, _body = fetch_retry(media_url, method="HEAD", timeout=30)
            record["player_media"]["head_status"] = head_status
            length = headers.get("content-length")
            if length and length.isdigit():
                record["player_media"]["content_length"] = int(length)
            etag = headers.get("etag")
            if etag and etag.startswith('"') and etag.endswith('"') and len(etag) >= 2:
                etag = etag[1:-1]
            record["player_media"]["etag"] = etag
            record["player_media"]["content_type"] = headers.get("content-type")
        except RuntimeError as exc:
            record["player_media"]["sha256_note"] = f"HTTP HEAD of the public media file failed: {exc}"
    else:
        record["player_media"]["sha256_note"] = "The DVIDS page did not include a public MP4 URL. SHA-256 was not computed."

    hls_subtitles = 0
    if parsed["m3u8_path"]:
        m3u8_url = "https://www.dvidshub.net" + parsed["m3u8_path"]
        try:
            m3u8_status, _final, _headers, m3u8_body = fetch_retry(m3u8_url)
            if m3u8_status == 200:
                variants, hls_subtitles = parse_m3u8(m3u8_body.decode("utf-8", "replace"))
                record["hls_variants"] = variants
        except RuntimeError:
            pass

    caption_text = None
    caption_kind = None
    caption_url = None
    if parsed["caption_links"]:
        caption_url = parsed["caption_links"][0]
        if caption_url.startswith("/"):
            caption_url = "https://www.dvidshub.net" + caption_url
        try:
            cap_status, _final, _headers, cap_body = fetch_retry(caption_url)
            if cap_status == 200:
                caption_text = cap_body.decode("utf-8", "replace").strip() or None
                caption_kind = "srt" if caption_url.lower().endswith(".srt") else "vtt"
        except RuntimeError as exc:
            record["captions"]["note"] = f"A caption link was on the page but the fetch failed: {exc}"
    checks = {
        "track_elements": parsed["track_elements"],
        "vtt_or_srt_links": len(parsed["caption_links"]),
        "transcript_heading": parsed["transcript_heading"],
        "hls_subtitle_renditions": hls_subtitles,
    }
    if caption_text:
        status_label = "present"
        note = "Caption text fetched from the URL on the DVIDS page."
    elif parsed["caption_links"]:
        status_label = "unknown"
        note = record["captions"].get("note") or "A caption link was on the page, but the caption text was not retrieved."
    elif parsed["transcript_heading"]:
        status_label = "unknown"
        note = "The page has a transcript or caption heading, but no caption file text was extracted. The transcript text is unknown."
    else:
        status_label = "absent"
        note = (
            "No caption track, WebVTT or SRT link, transcript heading, or HLS subtitle rendition "
            f"was on the DVIDS page fetched {FETCH_DATE}."
        )
    record["captions"] = {
        "status": status_label,
        "kind": caption_kind,
        "source_url": caption_url,
        "text": caption_text,
        "checks": checks,
        "note": note,
    }

    try:
        popup_status, _final, _headers, popup_body = fetch_retry(popup_url)
        record["popup_status"] = popup_status
        if popup_status == 200:
            downloads = parse_popup(popup_body.decode("utf-8", "replace"))
            if downloads:
                with ThreadPoolExecutor(max_workers=4) as pool:
                    record["downloads"] = list(pool.map(head_download, downloads))
                statuses = sorted({row["http_status"] for row in record["downloads"]})
                record["downloads_note"] = (
                    "Resolutions and size text come from the DVIDS download popup. "
                    f"HEAD requests to those download URLs returned HTTP {statuses}. "
                    "size_bytes is set only when that HEAD returned Content-Length with HTTP 200."
                )
            else:
                record["downloads_note"] = "The download popup returned HTTP 200 and no download rows. Offered resolutions are unknown."
        else:
            record["downloads_note"] = f"The download popup returned HTTP {popup_status}. Offered resolutions and sizes are unknown."
    except RuntimeError as exc:
        record["downloads_note"] = f"The download popup request failed ({exc}). Offered resolutions and sizes are unknown."
    return record


def hash_player_stream(item: dict) -> dict:
    media = dict(item.get("player_media") or {})
    url = media.get("url")
    if not url:
        media["sha256"] = None
        if not media.get("sha256_note") or media.get("sha256_note") == "SHA-256 was not computed yet.":
            media["sha256_note"] = "No public media URL was on the DVIDS page. SHA-256 was not computed."
        item["player_media"] = media
        return item
    expected = media.get("content_length")
    digest = hashlib.sha256()
    total = 0
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            status = response.status
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                digest.update(chunk)
                total += len(chunk)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ssl.SSLError, ConnectionError) as exc:
        media["sha256"] = None
        media["sha256_bytes"] = None
        media["sha256_note"] = f"SHA-256 was not computed. Downloading the public media file failed: {exc}"
        item["player_media"] = media
        return item
    if status != 200:
        media["sha256"] = None
        media["sha256_bytes"] = total or None
        media["sha256_note"] = f"SHA-256 was not computed. The public media file returned HTTP {status}."
        item["player_media"] = media
        return item
    if expected is not None and total != expected:
        media["sha256"] = None
        media["sha256_bytes"] = total
        media["sha256_note"] = (
            f"SHA-256 was not computed. The download was {total} bytes and the HTTP Content-Length was {expected}. "
            "The two did not match, so the hash was discarded."
        )
        item["player_media"] = media
        return item
    media["sha256"] = digest.hexdigest()
    media["sha256_bytes"] = total
    media["sha256_note"] = (
        f"SHA-256 of the public DVIDS media file {url}, downloaded {FETCH_DATE}. "
        f"{total} bytes were read"
        + (f", matching Content-Length {expected}." if expected is not None else ", and Content-Length was absent.")
        + " The file was not committed to the repository."
    )
    item["player_media"] = media
    return item


def scan_sitemaps() -> dict:
    """Record what the public sitemaps and the AARO unit page actually contain."""
    note: dict = {
        "fetch_date": FETCH_DATE,
        "sitemap_index": "https://www.dvidshub.net/sitemap.xml",
        "aaro_unit_page": "https://www.dvidshub.net/unit/AARO",
        "war_gov_ufo": None,
        "video_sitemap_count": None,
        "urls_containing_057b": [],
        "urls_containing_057": [],
        "image_sitemap_count": None,
        "image_sitemap_urls_containing_virin_260508-O-D0360-1021": 0,
        "image_sitemap_urls_containing_photo_a001": 0,
        "errors": [],
    }
    try:
        status, _final, _headers, body = fetch_retry("https://www.war.gov/UFO/", timeout=20)
        note["war_gov_ufo"] = {"url": "https://www.war.gov/UFO/", "http_status": status}
    except RuntimeError as exc:
        note["war_gov_ufo"] = {"url": "https://www.war.gov/UFO/", "error": str(exc)}

    try:
        status, _final, _headers, body = fetch_retry("https://www.dvidshub.net/unit/AARO")
        page = body.decode("utf-8", "replace")
        def count_for(label: str) -> int | None:
            match = re.search(rf"{label}</a>:&nbsp;\s*</div>\s*(\d+)", page)
            return int(match.group(1)) if match else None
        note["aaro_counts"] = {
            "http_status": status,
            "videos": count_for("Video"),
            "images": count_for("Images"),
            "audio": count_for("Audio"),
        }
    except RuntimeError as exc:
        note["errors"].append(f"AARO unit page: {exc}")

    try:
        _status, _final, _headers, body = fetch_retry("https://www.dvidshub.net/sitemap.xml")
        index = body.decode("utf-8", "replace")
    except RuntimeError as exc:
        note["errors"].append(f"sitemap index: {exc}")
        return note
    video_locs = re.findall(r"https://www\.dvidshub\.net/sitemap-videos-\d+\.xml", index)
    image_locs = re.findall(r"https://www\.dvidshub\.net/sitemap-images-\d+\.xml", index)
    note["video_sitemap_count"] = len(video_locs)
    note["image_sitemap_count"] = len(image_locs)

    def scan_video(url: str) -> list[str]:
        try:
            _status, _final, _headers, payload = fetch_retry(url, timeout=90)
        except RuntimeError:
            return []
        return re.findall(r"https://www\.dvidshub\.net/video/\d+/[^<\s]*", payload.decode("utf-8", "replace"))

    uap_urls: list[str] = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        for urls in pool.map(scan_video, video_locs):
            for url in urls:
                if "uap" in url.lower():
                    uap_urls.append(url)
    uap_urls = sorted(set(uap_urls))
    note["uap_video_url_count"] = len(uap_urls)
    note["urls_containing_057"] = [url for url in uap_urls if "057" in url.lower()]
    note["urls_containing_057b"] = [url for url in uap_urls if "057b" in url.lower()]
    # Keep the full UAP slug list out of the enrichment file; it is a search aid, not a catalog.
    note["uap_video_urls_sample_note"] = (
        f"{len(uap_urls)} video-sitemap URLs contained 'uap' in the path. "
        "The full list is not stored. urls_containing_057 and urls_containing_057b are the matches used "
        "when looking for a DVIDS id for DOW-UAP-PR057b."
    )

    virin = b"260508-O-D0360-1021"
    photo = b"photo-a001"

    def scan_image(url: str) -> tuple[int, int]:
        try:
            _status, _final, _headers, payload = fetch_retry(url, timeout=90)
        except RuntimeError:
            return (0, 0)
        return (payload.count(virin), payload.lower().count(photo))

    virin_hits = 0
    photo_hits = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        for virin_count, photo_count in pool.map(scan_image, image_locs):
            virin_hits += virin_count
            photo_hits += photo_count
    note["image_sitemap_urls_containing_virin_260508-O-D0360-1021"] = virin_hits
    note["image_sitemap_urls_containing_photo_a001"] = photo_hits
    return note


def load_ids() -> list[str]:
    prior = json.loads(PRIOR.read_text(encoding="utf-8"))
    return sorted(prior, key=lambda item: int(item))


def write_out(payload: dict) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-hash", action="store_true")
    parser.add_argument("--hash-only", action="store_true")
    parser.add_argument("--skip-sitemap", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    if args.hash_only:
        payload = json.loads(OUT.read_text(encoding="utf-8"))
        items = payload["items"]
    else:
        ids = load_ids()
        if args.limit:
            ids = ids[: args.limit]
        print(f"fetching {len(ids)} DVIDS ids", flush=True)
        items = {}
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = {pool.submit(one_id, dvids_id): dvids_id for dvids_id in ids}
            done = 0
            for future in as_completed(futures):
                dvids_id = futures[future]
                items[dvids_id] = future.result()
                done += 1
                status = items[dvids_id]["fetch_status"]
                print(f"  {done}/{len(ids)} {dvids_id} {status} downloads={len(items[dvids_id]['downloads'])}", flush=True)
        payload = {
            "fetch_date": FETCH_DATE,
            "source": "https://www.dvidshub.net/video/{id} and https://www.dvidshub.net/download/popup/{id}",
            "prior_metadata": "sources/dvids/metadata-2026-10-06.json",
            "items": items,
        }
        if not args.skip_sitemap and not args.limit:
            print("scanning sitemaps and the AARO unit page", flush=True)
            payload["lookup"] = scan_sitemaps()
        write_out(payload)
        print(f"wrote {OUT}", flush=True)

    if args.skip_hash:
        return

    print(f"hashing {len(payload['items'])} public media files", flush=True)
    hashed = 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(hash_player_stream, item): dvids_id for dvids_id, item in payload["items"].items()}
        done = 0
        for future in as_completed(futures):
            dvids_id = futures[future]
            payload["items"][dvids_id] = future.result()
            done += 1
            media = payload["items"][dvids_id]["player_media"]
            if media.get("sha256"):
                hashed += 1
            print(f"  hash {done}/{len(futures)} {dvids_id} {'ok' if media.get('sha256') else 'skipped'}", flush=True)
    payload["sha256_computed"] = hashed
    write_out(payload)
    print(f"sha256 computed for {hashed} files", flush=True)


if __name__ == "__main__":
    main()
