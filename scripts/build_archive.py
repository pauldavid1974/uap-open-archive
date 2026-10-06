#!/usr/bin/env python3
"""Build record pages and collection manifests from the official PURSUE catalog.

The Markdown under records/ and the manifests under sources/pursue-0N/ are
generated. Re-running this script overwrites them. Hand-written pages
(cases, entities, timelines, most analysis, gaps) are left alone.

Usage (from the repo root):
    python scripts/build_archive.py
"""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "sources" / "catalog" / "uap-data-2026-09-29-release-6v5.csv"
DVIDS_META = ROOT / "sources" / "dvids" / "metadata-2026-10-06.json"

CATALOG_LIVE = "https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6v5"
CATALOG_ARCHIVE = (
    "https://web.archive.org/web/20260929120048/"
    "https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6v5"
)
UFO_PAGE = "https://www.war.gov/UFO/"
UFO_ARCHIVE = "https://web.archive.org/web/20261004165250/https://www.war.gov/UFO/"

# Dated copies of uap-data.csv stored in this repo. Record pages are built
# from the last one. Manifests list every copy so a release is not one number.
CATALOG_SNAPSHOTS = [
    {
        "path": "sources/catalog/uap-data-2026-05-20.csv",
        "captured": "2026-05-20T09:58:41Z",
        "label": "May 20, 2026, 09:58 UTC",
        "query": "no query string",
        "archive_url": "https://web.archive.org/web/20260520095841/https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv",
    },
    {
        "path": "sources/catalog/uap-data-2026-09-18-release-6.csv",
        "captured": "2026-09-18T11:39:50Z",
        "label": "September 18, 2026, 11:39 UTC",
        "query": "release=6",
        "archive_url": "https://web.archive.org/web/20260918113950/https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6",
    },
    {
        "path": "sources/catalog/uap-data-2026-09-18-release-6v3.csv",
        "captured": "2026-09-18T15:56:29Z",
        "label": "September 18, 2026, 15:56 UTC",
        "query": "release=6v3",
        "archive_url": "https://web.archive.org/web/20260918155629/https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6v3",
    },
    {
        "path": "sources/catalog/uap-data-2026-09-19-release-6.csv",
        "captured": "2026-09-19T20:49:42Z",
        "label": "September 19, 2026, 20:49 UTC",
        "query": "release=6",
        "archive_url": "https://web.archive.org/web/20260919204942/https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6",
    },
    {
        "path": "sources/catalog/uap-data-2026-09-29-release-6v5.csv",
        "captured": "2026-09-29T12:00:48Z",
        "label": "September 29, 2026, 12:00 UTC",
        "query": "release=6v5",
        "archive_url": CATALOG_ARCHIVE,
    },
]

RELEASES = {
    "5/8/26": {
        "collection": "pursue-01",
        "number": 1,
        "iso": "2026-05-08",
        "label": "May 8, 2026",
        "docs_bundle": "https://www.war.gov/medialink/ufo/bundle/Release_1.zip",
        "video_bundle": "https://d34w7g4gy10iej.cloudfront.net/uapvideos.zip",
        "docs_size_stated": "1.2 GB",
        "video_size_stated": "1.3 GB",
        "press_archive": "https://web.archive.org/web/20260508125016/https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/",
        "press_live": "https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/",
    },
    "5/22/26": {
        "collection": "pursue-02",
        "number": 2,
        "iso": "2026-05-22",
        "label": "May 22, 2026",
        "docs_bundle": "https://www.war.gov/medialink/ufo/052226/release_02/release_02_document_bundle.zip",
        "video_bundle": "https://d34w7g4gy10iej.cloudfront.net/uap052226.zip",
        "docs_size_stated": "70.1 MB",
        "video_size_stated": "5.6 GB",
        "press_archive": "https://web.archive.org/web/20260522135306/https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/",
        "press_live": "https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/",
    },
    "6/12/26": {
        "collection": "pursue-03",
        "number": 3,
        "iso": "2026-06-12",
        "label": "June 12, 2026",
        "docs_bundle": "https://www.war.gov/medialink/ufo/061226/release_03/release_03_documents.zip",
        "video_bundle": "https://d34w7g4gy10iej.cloudfront.net/release_03/uap_videos_061226.zip",
        "docs_size_stated": "826 MB",
        "video_size_stated": "4.6 GB",
        "press_archive": "https://web.archive.org/web/20260612161132/https://www.war.gov/News/Releases/Release/Article/4515408/department-of-war-publishes-third-release-of-unidentified-anomalous-phenomena-f/",
        "press_live": "https://www.war.gov/News/Releases/Release/Article/4515408/department-of-war-publishes-third-release-of-unidentified-anomalous-phenomena-f/",
    },
    "7/10/26": {
        "collection": "pursue-04",
        "number": 4,
        "iso": "2026-07-10",
        "label": "July 10, 2026",
        "docs_bundle": "https://www.war.gov/medialink/ufo/071026/release_04/release_04_documents_071026.zip",
        "video_bundle": "https://d34w7g4gy10iej.cloudfront.net/release_04/uap_release04_videos_071026.zip",
        "docs_size_stated": "227 MB",
        "video_size_stated": "1.4 GB",
        "press_archive": "https://web.archive.org/web/20260710134746/https://www.war.gov/News/Releases/Release/Article/4539898/department-of-war-publishes-fourth-release-of-unidentified-anomalous-phenomena/",
        "press_live": "https://www.war.gov/News/Releases/Release/Article/4539898/department-of-war-publishes-fourth-release-of-unidentified-anomalous-phenomena/",
    },
    "8/7/26": {
        "collection": "pursue-05",
        "number": 5,
        "iso": "2026-08-07",
        "label": "August 7, 2026",
        "docs_bundle": "https://www.war.gov/medialink/ufo/release_05/Aug_07/release_05_Aug_07_documents.zip",
        "video_bundle": "https://d34w7g4gy10iej.cloudfront.net/release_05/uap_videos_080726.zip",
        "docs_size_stated": "130 MB",
        "video_size_stated": "513 MB",
        "press_archive": "https://web.archive.org/web/20260807151112/https://www.war.gov/News/Releases/Release/Article/4565994/department-of-war-publishes-fifth-release-of-unidentified-anomalous-phenomena-f/",
        "press_live": "https://www.war.gov/News/Releases/Release/Article/4565994/department-of-war-publishes-fifth-release-of-unidentified-anomalous-phenomena-f/",
    },
    "9/18/26": {
        "collection": "pursue-06",
        "number": 6,
        "iso": "2026-09-18",
        "label": "September 18, 2026",
        "docs_bundle": "https://www.war.gov/medialink/ufo/sept-18/release-06/documents_release_06_sept_18_2026.zip",
        "video_bundle": "https://d34w7g4gy10iej.cloudfront.net/release_06/pursue_vids_091826.zip",
        "docs_size_stated": "2.25 GB",
        "video_size_stated": "1.4 GB",
        "press_archive": "https://web.archive.org/web/20260918155319/https://www.war.gov/News/Releases/Release/Article/4604795/department-of-war-publishes-sixth-release-of-unidentified-anomalous-phenomena-f/",
        "press_live": "https://www.war.gov/News/Releases/Release/Article/4604795/department-of-war-publishes-sixth-release-of-unidentified-anomalous-phenomena-f/",
    },
}

TYPE_MAP = {"PDF": "document", "VID": "video", "IMG": "image", "AUD": "audio"}
MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}
OFFICIAL_ID_RE = re.compile(r"^([A-Z]{2,12}-UAP-[A-Z]*\d+[A-Z]?)\b")

GULF_IDS = {f"DOW-UAP-PR{n}" for n in range(117, 123)} | {"DOW-UAP-D101"}
TREMONTON_IDS = {
    "DOW-UAP-D098",
    "DOW-UAP-D102",
    "DOW-UAP-D103",
    "DOW-UAP-D104",
    "DOW-UAP-D105",
    "DOW-UAP-PR159",
}
PARTICLE_IDS = {"NASA-UAP-D010", "NASA-UAP-D011", "NASA-UAP-D012", "NASA-UAP-D013"}


def load_catalog() -> list[dict]:
    with CATALOG.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row.pop("", None)
    return rows


def clean(text: str) -> str:
    return (text or "").replace("\u00a0", " ").replace("\u200b", "").strip()


def slug(text: str) -> str:
    text = clean(text).lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:90].strip("-") or "record"


def parse_when(raw: str) -> tuple[str | None, str]:
    raw = clean(raw)
    if not raw or raw.upper() in {"N/A", "NA", "UNDATED", "NONE"}:
        return None, "unknown"
    match = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", raw)
    if match:
        month, day, year = (int(part) for part in match.groups())
        if year < 100:
            year += 2000 if year < 30 else 1900
        return f"{year:04d}-{month:02d}-{day:02d}", "day"
    match = re.fullmatch(r"([A-Za-z]+),?\s+(\d{4})", raw)
    if match and match.group(1).lower() in MONTHS:
        return f"{match.group(2)}-{MONTHS[match.group(1).lower()]:02d}", "month"
    if re.fullmatch(r"\d{4}", raw):
        return raw, "year"
    if re.fullmatch(r"\d{4}\s*-\s*\d{4}", raw):
        return re.sub(r"\s+", "", raw), "range"
    if raw.lower().startswith("late ") or "approximately" in raw.lower():
        return raw, "approximate"
    return None, "unknown"


def official_id_of(title: str) -> str | None:
    match = OFFICIAL_ID_RE.match(title)
    return match.group(1) if match else None


def archive_id_for(title: str, official_id: str | None, used: set[str]) -> str:
    if official_id == "FBI-UAP-D014":
        if "Correspondence" in title:
            base = "fbi-uap-d014-correspondence"
        elif "Western United States Event" in title:
            base = "fbi-uap-d014-western-us-event-rendering"
        else:
            base = "fbi-uap-d014-other"
    elif official_id:
        base = official_id.lower()
    else:
        base = slug(title)
    candidate = base
    n = 2
    while candidate in used:
        candidate = f"{base}-{n}"
        n += 1
    used.add(candidate)
    return candidate


def cases_for(title: str, official_id: str | None) -> list[str]:
    found: list[str] = []
    if "Western United States Event" in title or title == "Western US Event":
        if "Correspondence" not in title:
            found.append("western-us-event-2023")
    if (
        title.startswith("FBI Photo A")
        or title.startswith("FBI Photo B")
        or title.startswith("USPER Statement")
        or official_id == "ODNI-UAP-D001"
    ):
        found.append("western-us-test-range-orbs-2025")
    if official_id in {"CIA-UAP-D022", "CIA-UAP-D023"}:
        found.append("puerto-rico-radar-1964")
    if official_id in GULF_IDS:
        found.append("gulf-of-oman-orbs-2021")
    if official_id in TREMONTON_IDS:
        found.append("tremonton-1952")
    if official_id == "NASA-UAP-VM006" or (official_id or "").startswith("NASA-UAP-") and "Apollo 17" in title:
        found.append("apollo-17-three-dots")
    if official_id == "NASA-UAP-D012":
        found.append("schirra-mercury-atlas-8")
    if "AAWSAP" in title:
        found.append("aawsap")
    if (official_id or "").startswith("LLE-UAP-"):
        found.append("colorado-police-2023")
    if official_id == "DOW-UAP-PR051":
        found.append("syria-instant-acceleration")
    if official_id in PARTICLE_IDS:
        found.append("astronaut-particles")
    # stable order, no duplicates
    seen = []
    for item in found:
        if item not in seen:
            seen.append(item)
    return seen


def split_pairs(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split("|") if part.strip()]


def human_size(n: int | None) -> str:
    if n is None:
        return "not obtained"
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f} GB ({n} bytes)"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f} MB ({n} bytes)"
    if n >= 1_000:
        return f"{n / 1_000:.1f} KB ({n} bytes)"
    return f"{n} bytes"


def blockquote(text: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out = []
    for line in lines:
        if line.strip() == "":
            out.append(">")
        else:
            out.append("> " + line)
    return "\n".join(out)


def yaml_dump(data: dict) -> str:
    return yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        width=100,
    ).strip()


def assert_catalog_shape(rows: list[dict]) -> None:
    counts = Counter(row["Release Date"] for row in rows)
    expected = {"5/8/26": 158, "5/22/26": 64, "6/12/26": 72, "7/10/26": 40, "8/7/26": 41, "9/18/26": 75}
    if len(rows) != 450 or dict(counts) != expected:
        raise SystemExit(f"Catalog shape changed: {len(rows)} rows, counts {dict(counts)}")
    westen = sum(1 for row in rows if "Westen" in row["Incident Location"])
    if westen != 7:
        raise SystemExit(f"Expected 7 'Westen United States' locations, found {westen}")
    spaced = sum(1 for row in rows if row["Type"] != row["Type"].strip())
    if spaced != 6:
        raise SystemExit(f"Expected 6 types with trailing space, found {spaced}")
    d014 = [clean(row["Title"]) for row in rows if clean(row["Title"]).startswith("FBI-UAP-D014")]
    if len(d014) != 2:
        raise SystemExit(f"Expected FBI-UAP-D014 twice, found {d014}")
    d022 = next(row for row in rows if clean(row["Title"]).startswith("CIA-UAP-D022"))
    if clean(d022["Incident Date"]) != "2/1/65":
        raise SystemExit("CIA-UAP-D022 incident date column changed")
    if "November 19, 1964" not in d022["Description Blurb"]:
        raise SystemExit("CIA-UAP-D022 description no longer dates the event November 19, 1964")
    d105 = next(row for row in rows if clean(row["Title"]).startswith("DOW-UAP-D105"))
    if "Pages 26-36" not in d105["Description Blurb"] or "Tremonton" not in d105["Description Blurb"]:
        raise SystemExit("DOW-UAP-D105 no longer describes Tremonton on pages 26-36")


def render_record(rec: dict, dvids_by_id: dict, shared: dict[str, list[str]]) -> str:
    release = RELEASES[rec["release_raw"]]
    redaction_sentence = (
        "The catalog flags this row as redacted."
        if rec["catalog_redaction_flag"]
        else "The catalog does not flag this row as redacted."
    )
    place = rec["location_raw"] if rec["location_raw"] else "not given"
    when = rec["incident_date_raw"] if rec["incident_date_raw"] else "not given"
    summary = (
        f"This is one file in the U.S. Department of War PURSUE catalog, Release "
        f"{release['number']:02d} ({release['label']}). The agency on the row is "
        f"{rec['agency']}. The catalog calls the file type {rec['type_raw'].strip() or 'blank'}. "
        f"The incident date cell says \"{when}\". The incident location cell says \"{place}\". "
        f"{redaction_sentence} That flag is only a yes or no. It does not say how much was "
        f"removed, and this archive did not open the file to look."
    )
    if rec["official_id"] == "NASA-UAP-D003A":
        summary += (
            " On the May 20, 2026 snapshot this row's type cell is VID. "
            "On every later snapshot stored here it is AUD. "
            "See [catalog quality](../analysis/catalog-quality.md)."
        )
    dvids = dvids_by_id.get(rec["dvids_id"]) if rec["dvids_id"] else None
    file_lines = []
    if rec["original_file_url"]:
        file_lines.append(f"- Original file URL (as printed in the catalog): {rec['original_file_url']}")
        file_lines.append(
            "- Archived copy of that file: not found. On October 6, 2026 the Internet Archive "
            "availability API returned no snapshot for sample war.gov media URLs, and a direct "
            "request to war.gov returned HTTP 403. This was not re-checked one file at a time."
        )
    else:
        file_lines.append("- The catalog row has no direct file URL in the \"PDF | Image Link\" column.")
    if dvids:
        page = dvids.get("page") or {}
        fields = page.get("fields") or {}
        file_lines.append(f"- DVIDS page (live, retrieved October 6, 2026): {page.get('final_url')}")
        file_lines.append(
            "- Archived copy of the DVIDS page: not saved by this project, and not confirmed in the Wayback Machine."
        )
        if rec["media_url"]:
            file_lines.append(f"- Media URL from the DVIDS page: {rec['media_url']}")
        file_lines.append(f"- Size from an HTTP HEAD request: {human_size(rec['file_size_bytes'])}. The file was not downloaded.")
        if rec["http_etag"]:
            file_lines.append(
                f"- HTTP ETag: `{rec['http_etag']}`. This is the server's ETag, not a SHA-256 of the file. "
                "Amazon S3 multipart ETags end in a hyphen and a part count, and are not a whole-file checksum."
            )
        if fields:
            bits = []
            for key in ("Date Taken", "Date Posted", "Length", "Location", "VIRIN", "Filename", "Category", "Video ID"):
                if fields.get(key):
                    bits.append(f"{key}: {fields[key]}")
            if bits:
                file_lines.append("- DVIDS page fields (**official**, DVIDS is a Department of Defense distribution site): " + "; ".join(bits) + ".")
        siblings = [item for item in shared.get(rec["dvids_id"], []) if item != rec["id"]]
        if siblings:
            links = ", ".join(f"[{item}]({item}.md)" for item in siblings)
            file_lines.append(
                f"- This DVIDS id `{rec['dvids_id']}` is also listed on: {links}. "
                "Where the DVIDS page title matches only one of those catalog rows, the shared id may be a catalog error. See [catalog quality](../analysis/catalog-quality.md)."
            )
    elif rec["type"] in {"video", "audio"}:
        file_lines.append("- No DVIDS id was listed for this row, so no media size was retrieved.")
    file_lines.append("- SHA-256 of the underlying file: not computed, because the bytes were not downloaded.")
    file_lines.append(
        f"- Catalog spreadsheet this row was read from: [archived copy]({CATALOG_ARCHIVE}) "
        f"(live URL {CATALOG_LIVE}, which returned HTTP 403 to this project on October 6, 2026)."
    )

    related = rec["related_records"]
    if related:
        rel_lines = "\n".join(f"- [{item}]({item}.md)" for item in related)
    else:
        rel_lines = "None listed in the catalog pairing columns that this archive could match to another row."

    if rec["related_cases"]:
        case_lines = "\n".join(
            f"- [{item}](../cases/{item}.md)" for item in rec["related_cases"]
        )
    else:
        case_lines = "This row is not attached to one of the case files in `cases/`. It is still searchable from the indexes in `data/`."

    id_note = ""
    if rec.get("id_note"):
        id_note = f"\n\n{rec['id_note']}\n"

    body = f"""# {rec['title']}

## Plain-English summary

**Label: analysis.** This paragraph only restates fields from the official catalog row. It is not a judgment about what the event was. The underlying file was not opened.

{summary}

The government's own description of the file is quoted in the next section. If that description and the date or place cells disagree, both are printed here and neither has been "fixed."

## Official catalog description

**Label: official.** Quoted from the Department of War PURSUE catalog spreadsheet `uap-data.csv`, snapshot archived September 29, 2026 (`release=6v5`), row {rec['catalog_order']} in that file. This is the catalog's description. It is not a transcript and not text extracted from the file.

{blockquote(rec['description'])}
{id_note}
## File, archive copy, and checksum

**Label: official** for URLs that come from the catalog or from DVIDS. **Label: analysis** for the notes about what this project could not retrieve.

{chr(10).join(file_lines)}

## Pairings inside the catalog

**Label: official.** These are the other catalog titles or ids printed in this row's pairing columns. Links are added only where the text matched another row in the same spreadsheet.

{rel_lines}

## Cases

{case_lines}

## What is missing or unverified

**Label: analysis.**

- The underlying file was not opened. Anything the catalog description does not say is unknown to this page.
- Witnesses and sensors are not copied into separate fields in this version, because pulling names out of the prose automatically would mix people who are mentioned with people who were witnesses. Named people, if the catalog names any, are in the description above.
- A "not flagged" redaction mark means the spreadsheet cell was empty. It does not mean someone checked the file and found no black bars.
- Resolved cases are not in this catalog. The Department of War's PURSUE page says the files posted here are unresolved cases, and that resolved cases are reported separately.
"""
    front = {
        "id": rec["id"],
        "official_id": rec["official_id"],
        "title": rec["title"],
        "collection": rec["collection"],
        "agency": rec["agency"],
        "type": rec["type"],
        "type_raw": rec["type_raw"],
        "release_date": rec["release_date"],
        "incident_date": rec["incident_date"],
        "incident_date_raw": rec["incident_date_raw"],
        "incident_date_precision": rec["incident_date_precision"],
        "location": rec["location"],
        "location_raw": rec["location_raw"],
        "catalog_redaction_flag": rec["catalog_redaction_flag"],
        "redaction_level": rec["redaction_level"],
        "witnesses": [],
        "sensors": [],
        "labels": ["official", "analysis"],
        "featured": rec["featured"],
        "sources": rec["sources"],
        "related_cases": rec["related_cases"],
        "related_records": rec["related_records"],
        "underlying_file_opened": False,
        "catalog_order": rec["catalog_order"],
        "dvids_id": rec["dvids_id"],
        "file_size_bytes": rec["file_size_bytes"],
        "http_etag": rec["http_etag"],
        "media_url": rec["media_url"],
        "sha256": None,
        "image_virin": rec["image_virin"],
        "video_pairing": rec["video_pairing"],
        "pdf_pairing": rec["pdf_pairing"],
    }
    if rec.get("id_note"):
        front["id_note"] = rec["id_note"]
    return f"---\n{yaml_dump(front)}\n---\n\n{body}"


def build_records(rows: list[dict], dvids_meta: dict) -> list[dict]:
    used: set[str] = set()
    records = []
    for index, row in enumerate(rows, start=1):
        title = clean(row["Title"])
        official_id = official_id_of(title)
        release_raw = row["Release Date"].strip()
        if release_raw not in RELEASES:
            raise SystemExit(f"Unknown release date {release_raw!r} on {title}")
        release = RELEASES[release_raw]
        type_raw = row["Type"]
        type_key = type_raw.strip()
        if type_key not in TYPE_MAP:
            raise SystemExit(f"Unknown type {type_raw!r} on {title}")
        incident_raw = clean(row["Incident Date"])
        incident_date, precision = parse_when(incident_raw)
        location_raw = clean(row["Incident Location"])
        location = None if location_raw.upper() in {"", "N/A", "NA"} else location_raw
        redaction_flag = clean(row["Redaction"]).upper() == "TRUE"
        if clean(row["Redaction"]) not in {"", "TRUE"}:
            raise SystemExit(f"Unexpected redaction value {row['Redaction']!r}")
        dvids_id = clean(row["DVIDS Video ID"]) or None
        meta = dvids_meta.get(dvids_id) if dvids_id else None
        page = (meta or {}).get("page") or {}
        archive_id = archive_id_for(title, official_id, used)
        id_note = ""
        if official_id == "FBI-UAP-D014":
            id_note = (
                "**Label: analysis.** The catalog uses the official id FBI-UAP-D014 on two different "
                "rows (a 1967/1974 correspondence file and a 2023 Western United States Event rendering). "
                f"This page is `{archive_id}` so the two are not mixed together."
            )
        file_url = clean(row["PDF | Image Link"]) or None
        sources = [
            {
                "role": "catalog",
                "label": "official",
                "url": CATALOG_LIVE,
                "archive_url": CATALOG_ARCHIVE,
                "note": "Row taken from the September 29, 2026 Wayback snapshot of uap-data.csv?release=6v5. Live war.gov returned HTTP 403 on October 6, 2026.",
            }
        ]
        if file_url:
            sources.append(
                {
                    "role": "file",
                    "label": "official",
                    "url": file_url,
                    "archive_url": None,
                    "note": "No Wayback snapshot was found for sample war.gov media URLs on October 6, 2026. Not re-checked per file.",
                }
            )
        if dvids_id and page.get("final_url"):
            sources.append(
                {
                    "role": "dvids",
                    "label": "official",
                    "url": page["final_url"],
                    "archive_url": None,
                    "note": "DVIDS page fetched live on October 6, 2026. Media bytes were not downloaded. File size is from HTTP HEAD.",
                }
            )
        records.append(
            {
                "id": archive_id,
                "official_id": official_id,
                "id_note": id_note,
                "title": title,
                "description": row["Description Blurb"].replace("\u00a0", " ").strip(),
                "collection": release["collection"],
                "release_number": release["number"],
                "release_date": release["iso"],
                "release_raw": release_raw,
                "agency": clean(row["Agency"]),
                "type": TYPE_MAP[type_key],
                "type_raw": type_raw,
                "incident_date": incident_date,
                "incident_date_raw": incident_raw,
                "incident_date_precision": precision,
                "location": location,
                "location_raw": location_raw,
                "catalog_redaction_flag": redaction_flag,
                "redaction_level": "flagged" if redaction_flag else "not_flagged",
                "featured": clean(row["Featured"]).upper() == "YES",
                "dvids_id": dvids_id,
                "file_size_bytes": (meta or {}).get("content_length"),
                "http_etag": (meta or {}).get("etag"),
                "media_url": (meta or {}).get("media_url"),
                "original_file_url": file_url,
                "image_virin": clean(row["Image VIRIN"]) or None,
                "video_pairing": split_pairs(row["Video Pairing"]),
                "pdf_pairing": split_pairs(row["PDF Pairing"]),
                "related_cases": cases_for(title, official_id),
                "sources": sources,
                "catalog_order": index,
                "related_records": [],
            }
        )
    by_official: dict[str, list[str]] = defaultdict(list)
    by_title: dict[str, str] = {}
    for rec in records:
        by_title[rec["title"]] = rec["id"]
        if rec["official_id"]:
            by_official[rec["official_id"]].append(rec["id"])

    def resolve(token: str, self_id: str) -> list[str]:
        token = clean(token)
        if token in by_title and by_title[token] != self_id:
            return [by_title[token]]
        # token may be an official id, or "ID, rest of title"
        match = OFFICIAL_ID_RE.match(token)
        hits = []
        if match:
            hits.extend(item for item in by_official.get(match.group(1), []) if item != self_id)
        if token in by_official:
            hits.extend(item for item in by_official[token] if item != self_id)
        # unique, stable
        out = []
        for item in hits:
            if item not in out:
                out.append(item)
        return out

    for rec in records:
        related = []
        for token in rec["video_pairing"] + rec["pdf_pairing"]:
            for item in resolve(token, rec["id"]):
                if item not in related:
                    related.append(item)
        rec["related_records"] = related
    return records


def write_records(records: list[dict], dvids_meta: dict) -> None:
    shared: dict[str, list[str]] = defaultdict(list)
    for rec in records:
        if rec["dvids_id"]:
            shared[rec["dvids_id"]].append(rec["id"])
    shared = {key: value for key, value in shared.items() if len(value) > 1}
    out_dir = ROOT / "records"
    if out_dir.exists():
        for old in out_dir.glob("*.md"):
            old.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)
    for rec in records:
        text = render_record(rec, dvids_meta, shared)
        (out_dir / f"{rec['id']}.md").write_text(text, encoding="utf-8")
    print(f"wrote {len(records)} records")


def load_csv_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row.pop("", None)
    return rows


def snapshot_release_stats() -> list[dict]:
    stats = []
    for snap in CATALOG_SNAPSHOTS:
        rows = load_csv_rows(ROOT / snap["path"])
        by_release: dict[str, dict] = {}
        for row in rows:
            bucket = by_release.setdefault(
                row["Release Date"],
                {"rows": 0, "redacted": 0, "by_type": Counter()},
            )
            bucket["rows"] += 1
            if (row.get("Redaction") or "").strip() == "TRUE":
                bucket["redacted"] += 1
            bucket["by_type"][(row.get("Type") or "").strip() or "(blank)"] += 1
        stats.append({**snap, "rows_in_file": len(rows), "by_release": by_release})
    return stats


def versions_for_release(release_date: str, stats: list[dict]) -> list[dict]:
    versions = []
    for snap in stats:
        bucket = snap["by_release"].get(release_date)
        if not bucket:
            continue
        versions.append(
            {
                "snapshot": snap["path"],
                "captured": snap["captured"],
                "archive_url": snap["archive_url"],
                "query": snap["query"],
                "label": snap["label"],
                "rows_in_file": snap["rows_in_file"],
                "rows_in_this_release": bucket["rows"],
                "redacted_count": bucket["redacted"],
                "by_type": dict(bucket["by_type"]),
            }
        )
    return versions


def version_notes(collection: str) -> list[str]:
    if collection == "pursue-01":
        return [
            "The table is official catalog rows. Launch-day news is a separate count, and it is **press**.",
            "",
            "Launch-day coverage on May 8 counted **162** catalog entries: 120 PDFs, 28 videos, 14 images, and 108 flagged redacted. An independent fact-check on October 5, 2026 found that breakdown in The Next Web, USA Herald, and other write-ups. This archive did not re-open those articles on October 6 (the Next Web URL returned HTTP 404). No CSV from May 8 through May 19 is stored here. Both 162 and 158 are descriptions of catalog rows. They are not a count of files inside the zip bundles. The gap is 4 PDF rows and 3 redaction flags. The video count (28) and the image count (14) in that press breakdown match the May 20 CSV.",
            "",
            "An advocate tracker (pursueufotracker.com) says duplicate PDF rows were consolidated on May 11, and it gives 161 then 158 rather than 162. That account is **unverified**. See [unverified claims](../../gaps/unverified-claims.md). Nothing in the snapshots stored here shows a video or image row withdrawn.",
            "",
            "NASA-UAP-D003A, the Gemini 7 audio excerpt, is type VID in the May 20 CSV and type AUD from the September 18 morning CSV onward. The September 29 composition of this release is therefore 27 videos and 1 audio, not the launch-week 28 videos and 0 audio.",
            "",
            "Two titles also changed spelling after May 20: DOW-UAP-D052 (\"Correspondance\" to \"Correspondence\") and NASA-UAP-D007 (\"Techincal\" to \"Technical\"). Those fixes, and the VID-to-AUD change, are the Release 01 differences this archive can see between May 20 and September 29. The row count stays 158.",
        ]
    if collection == "pursue-02":
        return [
            "The row count for this release does not change across the September snapshots stored here: 64 rows, 51 of them videos.",
            "",
            "Many of those video descriptions say that on March 6, 2026, eight members of the House asked for 51 records. That sentence is the catalog's. It is not Rep. Anna Paulina Luna's letter. Her letter is a different document, dated March 31, 2026, with 46 numbered items covering 50 videos and a deadline of April 14, 2026. A copy is in [sources/house-oversight](../house-oversight/README.md). The catalog's PR050 title matches item 1 of that letter, and PR051 matches item 2. See [the Syria case](../../cases/syria-instant-acceleration.md).",
        ]
    if collection == "pursue-06":
        return [
            "On the morning of release day the catalog had 71 Release 06 rows: 55 PDFs, 15 videos, 1 audio file, 64 flagged redacted. The four local-law-enforcement videos were in. The transcripts were not. LLE-UAP-PR004's title said October 2023.",
            "",
            "Later the same day, the `release=6v3` capture (15:56 UTC) has 72 rows. LLE-UAP-D001 is the added transcript, and the redaction count is 65. PR004's title still said October 2023. The September 19 capture is still 72 rows and still only that one transcript.",
            "",
            "By September 29 (`release=6v5`) the count is 75. LLE-UAP-D002, D003, and D004 are present. The redaction count is 67. D001, D002, and D004 are flagged. D003 is not. PR004's title now says January 2024, while its incident-date cell still says October 2023.",
            "",
            "A same-day news count of 71 matches the 11:39 UTC spreadsheet. It does not match the catalog after the transcripts were added. This archive does not hold a September 22 CSV. An October 5 fact-check of further Wayback copies reported that D002–D004 appeared between September 22 and September 29.",
        ]
    return [
        "Across the September snapshots stored here, this release's row count, redaction count, and type counts do not change. The May 20, 2026 snapshot contains Release 01 only, so it is absent from the table.",
    ]


def write_manifests(records: list[dict]) -> None:
    membership: dict[str, list[str]] = defaultdict(list)
    for rec in records:
        for case_id in rec["related_cases"]:
            membership[case_id].append(rec["id"])
    (ROOT / "sources" / "case-membership.json").write_text(
        json.dumps({key: membership[key] for key in sorted(membership)}, indent=2) + "\n",
        encoding="utf-8",
    )
    stats = snapshot_release_stats()
    for release_date, release in RELEASES.items():
        group = [rec for rec in records if rec["collection"] == release["collection"]]
        folder = ROOT / "sources" / release["collection"]
        folder.mkdir(parents=True, exist_ok=True)
        redacted = sum(1 for rec in group if rec["catalog_redaction_flag"])
        by_agency = dict(Counter(rec["agency"] for rec in group))
        by_type = dict(Counter(rec["type"] for rec in group))
        versions = versions_for_release(release_date, stats)
        manifest = {
            "collection": release["collection"],
            "release_number": release["number"],
            "release_date": release["iso"],
            "catalog_snapshot": "sources/catalog/uap-data-2026-09-29-release-6v5.csv",
            "catalog_archive_url": CATALOG_ARCHIVE,
            "record_count": len(group),
            "redacted_count": redacted,
            "by_agency": by_agency,
            "by_type": by_type,
            "catalog_versions": [
                {key: value for key, value in version.items() if key != "label"}
                for version in versions
            ],
            "bundle": {
                "documents_url": release["docs_bundle"],
                "videos_url": release["video_bundle"],
                "documents_size_stated_on_war_gov_ufo": release["docs_size_stated"],
                "videos_size_stated_on_war_gov_ufo": release["video_size_stated"],
                "size_source": UFO_ARCHIVE,
                "note": "Bundle sizes are the figures printed on the archived war.gov/UFO page, not measurements made by this archive. The zip files were not downloaded.",
            },
            "records": [
                {
                    "id": rec["id"],
                    "official_id": rec["official_id"],
                    "title": rec["title"],
                    "agency": rec["agency"],
                    "type": rec["type"],
                    "type_raw": rec["type_raw"],
                    "incident_date_raw": rec["incident_date_raw"],
                    "location_raw": rec["location_raw"],
                    "catalog_redaction_flag": rec["catalog_redaction_flag"],
                    "original_file_url": rec["original_file_url"],
                    "archive_file_url": None,
                    "dvids_url": next((s["url"] for s in rec["sources"] if s["role"] == "dvids"), None),
                    "media_url": rec["media_url"],
                    "file_size_bytes": rec["file_size_bytes"],
                    "http_etag": rec["http_etag"],
                    "sha256": None,
                    "catalog_order": rec["catalog_order"],
                }
                for rec in group
            ],
        }
        (folder / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        lines = [
            f"# PURSUE Release {release['number']:02d}",
            "",
            f"**Label: official** for counts taken from the catalog. **Label: analysis** for the notes.",
            "",
            f"Cleared for release {release['label']}, as printed on the [archived war.gov/UFO page]({UFO_ARCHIVE}) (live page: {UFO_PAGE}).",
            "",
            f"This folder lists every catalog row whose Release Date is this tranche in the September 29, 2026 spreadsheet (`release=6v5`). There are **{len(group)}** rows. **{redacted}** have the catalog redaction flag set ({redacted / len(group):.1%} of this release).",
            "",
            f"Press release: [live]({release['press_live']}) and [archived copy]({release['press_archive']}).",
            "",
            "Download bundles linked from the October 4, 2026 archived PURSUE page. These zips were not downloaded. The page states these sizes:",
            "",
            f"- Documents: {release['docs_size_stated']} — {release['docs_bundle']}",
            f"- Videos: {release['video_size_stated']} — {release['video_bundle']}",
            "",
            "Agencies on the catalog rows:",
            "",
        ]
        for agency, count in sorted(by_agency.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"- {agency}: {count}")
        lines += ["", "File types, after stripping a trailing space that the catalog left on six Release 01 PDF cells:", ""]
        for kind, count in sorted(by_type.items()):
            lines.append(f"- {kind}: {count}")
        lines += [
            "",
            "## Catalog versions",
            "",
            "The counts above are the September 29, 2026 snapshot (`release=6v5`). That is the snapshot the record pages are built from. Earlier copies of the same spreadsheet are stored in [`sources/catalog/`](../catalog/). A release does not have one number.",
            "",
            "| Snapshot | Rows in this release | Flagged redacted | PDF | VID | IMG | AUD | Rows in the whole file |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for version in versions:
            types = version["by_type"]
            lines.append(
                f"| {version['label']} (`{version['query']}`) | {version['rows_in_this_release']} | "
                f"{version['redacted_count']} | {types.get('PDF', 0)} | {types.get('VID', 0)} | "
                f"{types.get('IMG', 0)} | {types.get('AUD', 0)} | {version['rows_in_file']} |"
            )
        lines += ["", *version_notes(release["collection"]), ""]
        lines += [
            "The machine-readable list, including these version counts, is [manifest.json](manifest.json). Each item also has a page in [`records/`](../../records/).",
            "",
            "| Archive id | Official id | Type | Redaction flag | Agency | Title |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for rec in sorted(group, key=lambda item: (item["official_id"] or "zzz", item["title"])):
            oid = rec["official_id"] or ""
            flag = "flagged" if rec["catalog_redaction_flag"] else "not flagged"
            title = rec["title"].replace("|", "\\|")
            lines.append(
                f"| [{rec['id']}](../../records/{rec['id']}.md) | {oid} | {rec['type']} | {flag} | {rec['agency']} | {title} |"
            )
        lines.append("")
        (folder / "manifest.md").write_text("\n".join(lines), encoding="utf-8")
        readme = f"""# {release['collection']}

PURSUE Release {release['number']:02d}, {release['label']}.

Record pages are built from the September 29, 2026 catalog (`release=6v5`): **{len(group)}** rows, **{redacted}** flagged redacted. Earlier snapshots of the same spreadsheet do not all show that number. The dated counts are in [manifest.md](manifest.md).

This folder is one collection. Later collections (AARO reports, FOIA batches, National Archives record groups) can sit beside it under `sources/` without renumbering these six.
"""
        (folder / "README.md").write_text(readme, encoding="utf-8")
    print("wrote 6 manifests")


def write_generated_analysis(rows: list[dict], records: list[dict], dvids_meta: dict) -> None:
    analysis = ROOT / "analysis"
    analysis.mkdir(parents=True, exist_ok=True)
    gaps = ROOT / "gaps"
    gaps.mkdir(parents=True, exist_ok=True)

    # Redaction
    lines = [
        "# Redaction flags in the PURSUE catalog",
        "",
        "**Label: analysis.** The counts below are arithmetic on the official yes/no redaction column. They are not a measurement of how many words were blacked out. The catalog does not say that. This page is generated by `scripts/build_archive.py` from the September 29, 2026 snapshot.",
        "",
        "Source spreadsheet: [archived copy](" + CATALOG_ARCHIVE + ").",
        "",
        "## By release",
        "",
        "| Release | Records | Flagged redacted | Share |",
        "| --- | ---: | ---: | ---: |",
    ]
    total = len(records)
    total_red = sum(1 for rec in records if rec["catalog_redaction_flag"])
    for release in RELEASES.values():
        group = [rec for rec in records if rec["collection"] == release["collection"]]
        red = sum(1 for rec in group if rec["catalog_redaction_flag"])
        lines.append(
            f"| [{release['collection']}](../sources/{release['collection']}/manifest.md) ({release['label']}) | {len(group)} | {red} | {red / len(group):.1%} |"
        )
    lines.append(f"| **Total** | **{total}** | **{total_red}** | **{total_red / total:.1%}** |")
    lines += ["", "## By agency", "", "| Agency | Records | Flagged redacted | Share |", "| --- | ---: | ---: | ---: |"]
    agencies = sorted(set(rec["agency"] for rec in records))
    for agency in agencies:
        group = [rec for rec in records if rec["agency"] == agency]
        red = sum(1 for rec in group if rec["catalog_redaction_flag"])
        lines.append(f"| {agency} | {len(group)} | {red} | {red / len(group):.1%} |")
    lines += [
        "",
        "## By file type",
        "",
        "| Type | Records | Flagged redacted | Share |",
        "| --- | ---: | ---: | ---: |",
    ]
    for kind in ("document", "video", "image", "audio"):
        group = [rec for rec in records if rec["type"] == kind]
        red = sum(1 for rec in group if rec["catalog_redaction_flag"])
        lines.append(f"| {kind} | {len(group)} | {red} | {red / len(group):.1%} |")
    lines += [
        "",
        "## How to read this",
        "",
        "Modern military videos and reports are flagged far more often than the older history files. Release 03 is mostly older documents, and its flag rate is the lowest. Release 06 is mostly AAWSAP papers plus recent military and police files, and its flag rate is the highest. That pattern is visible in the tables. It is a description of the spreadsheet, not a claim about what was removed.",
        "",
        "An empty redaction cell is counted here as not flagged. See [catalog quality](catalog-quality.md).",
        "",
    ]
    (analysis / "redaction.md").write_text("\n".join(lines), encoding="utf-8")

    # Catalog quality
    def series_numbers(prefix: str) -> list[int]:
        found = []
        pattern = re.compile(rf"^{re.escape(prefix)}(\d+)[A-Z]?$")
        for rec in records:
            official = rec["official_id"] or ""
            match = pattern.match(official)
            if match:
                found.append(int(match.group(1)))
        return found

    dow_d = series_numbers("DOW-UAP-D")
    dow_pr = series_numbers("DOW-UAP-PR")
    fbi_d = series_numbers("FBI-UAP-D")

    def missing_in_span(nums: list[int]) -> list[int]:
        if not nums:
            return []
        return [n for n in range(1, max(nums) + 1) if n not in set(nums)]

    quirks = []
    for rec in records:
        title = rec["title"]
        date = rec["incident_date_raw"]
        loc = rec["location_raw"]
        if rec["official_id"] == "DOW-UAP-D027":
            quirks.append((rec, "Title says United Arab Emirates, October 2023. Incident date cell is 6/7/24. Location cell is Gulf of Oman."))
        elif rec["official_id"] == "DOW-UAP-D042":
            quirks.append((rec, "Title says Japan, 2023. Incident date cell is 8/31/20. Location cell is Arabian Gulf."))
        elif rec["official_id"] == "DOW-UAP-D051":
            quirks.append((rec, "Title says March 2023. Incident date cell is 3/23/26."))
        elif rec["official_id"] == "DOW-UAP-PR045":
            quirks.append((rec, "Title says Middle East, 2020. Location cell is Southern United States. Incident date cell is N/A."))
        elif rec["official_id"] == "LLE-UAP-PR004":
            quirks.append((rec, "Title says Colorado, January 2024. Incident date cell is October, 2023."))
        elif rec["official_id"] == "CIA-UAP-D022":
            quirks.append((rec, "Title says 1965 and the incident date cell is 2/1/65. The description dates the sighting November 19, 1964."))
        elif rec["official_id"] == "FBI-UAP-D022" and "2026" in title:
            quirks.append((rec, "Title ends in 2026. The other Western United States Event renderings from the same set are titled 2023. The incident date cell should be checked on the record page."))
        elif "Westen United States" in loc:
            quirks.append((rec, "Location cell is spelled \"Westen United States\". The title uses the ordinary spelling Western."))

    # identical titles PR093 PR095
    pr093 = next(rec for rec in records if rec["official_id"] == "DOW-UAP-PR093")
    pr095 = next(rec for rec in records if rec["official_id"] == "DOW-UAP-PR095")

    # shared dvids
    shared_groups: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        if rec["dvids_id"]:
            shared_groups[rec["dvids_id"]].append(rec)

    quality = [
        "# Catalog quality: gaps, collisions, and cells that disagree",
        "",
        "**Label: analysis.** Everything on this page is a comparison of cells inside the official spreadsheet, or a comparison of those cells with the DVIDS page the spreadsheet points at. It is generated by `scripts/build_archive.py`.",
        "",
        "None of these notes change the stored catalog. The original CSV is in [`sources/catalog/`](../sources/catalog/).",
        "",
        "## One official id used twice",
        "",
        "FBI-UAP-D014 is the only official id that the September 29, 2026 catalog assigns to two different files:",
        "",
        "- [fbi-uap-d014-correspondence](../records/fbi-uap-d014-correspondence.md) — correspondence, 1967 and 1974, Release 04.",
        "- [fbi-uap-d014-western-us-event-rendering](../records/fbi-uap-d014-western-us-event-rendering.md) — a digital rendering for the Western United States Event, Release 03.",
        "",
        "Nearby ids that look similar are not collisions. DOW-UAP-PR057a and DOW-UAP-PR057b are different ids. NASA-UAP-D003 (a Gemini 7 transcript) and NASA-UAP-D003A (a Gemini 7 audio excerpt) are different ids.",
        "",
        "## Title or date cells that do not match each other",
        "",
    ]
    for rec, note in quirks:
        quality.append(f"- [{rec['id']}](../records/{rec['id']}.md): {note}")
    quality += [
        "",
        f"- [dow-uap-pr093](../records/{pr093['id']}.md) and [dow-uap-pr095](../records/{pr095['id']}.md) have the same title text: \"{pr093['title']}\". They are separate rows.",
        "",
        "## Type cells with a trailing space",
        "",
        "Six Release 01 rows have the type value `PDF` followed by a space. Counted as documents. The raw value is kept on each record as `type_raw`. The six titles are:",
        "",
    ]
    for rec in records:
        if rec["type_raw"] != rec["type_raw"].strip():
            quality.append(f"- [{rec['id']}](../records/{rec['id']}.md)")
    quality += [
        "",
        "## Numbering gaps",
        "",
        "These are official numbers that do not appear, counting from 1 up to the highest number that does appear. The Department of War does not say whether a missing number was withheld, reported later as a resolved case, merged, or never used. The PURSUE page says resolved cases are reported separately, as statute requires. It does not name aaro.mil as that destination. **Label: analysis:** absence from this list is not evidence the record exists somewhere else, and it is not evidence it was destroyed.",
        "",
        f"- DOW-UAP-D missing: {', '.join(str(n) for n in missing_in_span(dow_d)) or 'none'}.",
        f"- DOW-UAP-PR missing: {', '.join(str(n) for n in missing_in_span(dow_pr)) or 'none'}.",
        f"- FBI-UAP-D missing: {', '.join(str(n) for n in missing_in_span(fbi_d)) or 'none'}.",
        "",
        "## The same DVIDS id on more than one catalog row",
        "",
        "Some shares are a written report and its video. Two shares do not look like that, because the DVIDS page title retrieved on October 6, 2026 matches only one of the rows:",
        "",
    ]
    for dvids_id, group in sorted(shared_groups.items()):
        if len(group) < 2:
            continue
        meta = dvids_meta.get(dvids_id) or {}
        page_title = html.unescape(((meta.get("page") or {}).get("og_title")) or "")
        names = ", ".join(f"[{rec['id']}](../records/{rec['id']}.md)" for rec in group)
        quality.append(f"- DVIDS `{dvids_id}` page title \"{page_title}\" is listed on {names}.")
    quality += [
        "",
        "## What changed in Release 01 after May 20",
        "",
        "The May 20, 2026 catalog is Release 01 only: 158 rows, 116 PDF, 28 VID, 14 IMG, 105 flagged redacted, and no audio row. The September 29 Release 01 rows are the same count, with two title spelling fixes and one type change:",
        "",
        "- DOW-UAP-D052: \"Correspondance\" became \"Correspondence\".",
        "- NASA-UAP-D007: \"Techincal\" became \"Technical\".",
        "- [NASA-UAP-D003A](../records/nasa-uap-d003a.md), the Gemini 7 audio excerpt, changed from VID to AUD. By the September 18 morning snapshot it is already AUD. This archive does not hold the snapshot that first shows the new type.",
        "",
        "Launch-week press counted 162 rows (120 PDF, 28 video, 14 image, 108 redacted). That figure is not in any CSV stored here. It is not explained by counting files inside a zip. The dated table is on the [Release 01 manifest](../sources/pursue-01/manifest.md).",
        "",
        "## Release 06 grew after release morning",
        "",
        "Counted from archived copies of the same spreadsheet:",
        "",
        "| Snapshot | Total rows | Release 06 rows | Redaction flags | What changed in Release 06 |",
        "| --- | ---: | ---: | ---: | --- |",
        "| September 18, 2026, 11:39 UTC (`release=6`) | 446 | 71 | 64 | Four local-law-enforcement videos. No transcripts. LLE-UAP-PR004's title said October 2023. |",
        "| September 18, 2026, 15:56 UTC (`release=6v3`) | 447 | 72 | 65 | LLE-UAP-D001 is present. |",
        "| September 19, 2026, 20:49 UTC (`release=6`) | 447 | 72 | 65 | Still only D001. |",
        "| September 29, 2026 (`release=6v5`) | 450 | 75 | 67 | D002, D003, and D004 are present. D003 is not flagged redacted. PR004's title says January 2024. |",
        "",
        "Releases 02 through 05 stay at 64, 72, 40, and 41 across those snapshots. Release 01 stays at 158. A title comma also changed on DOW-UAP-D134 between the September 18 morning snapshot and the later ones (a question mark was removed). The bytes of each snapshot are in `sources/catalog/`.",
        "",
    ]
    (analysis / "catalog-quality.md").write_text("\n".join(quality), encoding="utf-8")

    # Keyword gap search
    needles = [
        "nimitz",
        "tic tac",
        "gimbal",
        "go fast",
        "gofast",
        "flir1",
        "roswell",
        "rendlesham",
        "phoenix lights",
        "kecksburg",
        "socorro",
        "zamora",
        "shag harbour",
        "shag harbor",
        "project twinkle",
        "condon",
        "grusch",
        "immaculate constellation",
        "kona blue",
        "uss omaha",
        "malmstrom",
        "minot",
    ]
    keyword_lines = [
        "# Keyword search of the September 29, 2026 catalog",
        "",
        "**Label: analysis.** This is a text search of titles and catalog descriptions. A miss does not prove a topic is absent from inside a PDF that was not opened. A hit does not prove the famous case of that name is the file that matched.",
        "",
        "Generated by `scripts/build_archive.py`.",
        "",
        "| Search text | Rows matched | Where |",
        "| --- | ---: | --- |",
    ]
    for needle in needles:
        hits = []
        for rec in records:
            blob = f"{rec['title']}\n{rec['description']}".lower()
            if needle in blob:
                hits.append(rec)
        if not hits:
            keyword_lines.append(f"| {needle} | 0 | — |")
        else:
            where = ", ".join(f"[{rec['id']}](../records/{rec['id']}.md)" for rec in hits[:8])
            extra = f" (+{len(hits) - 8} more)" if len(hits) > 8 else ""
            keyword_lines.append(f"| {needle} | {len(hits)} | {where}{extra} |")
    keyword_lines += [
        "",
        "Notes on hits that are easy to misread:",
        "",
        "- \"tic tac\" matches two 2024 Coast Guard video titles (DOW-UAP-PR065 and PR066). It does not match a 2004 Nimitz record. \"nimitz\" itself matches nothing.",
        "- \"flir1\" matches nothing. A different title, DOW-UAP-PR069, contains the word FLIR (\"F/A-18 FLIR UAP\"). That is not the string FLIR1.",
        "- \"project twinkle\" matches nothing. The word \"twinkle\" does appear in an Apollo 17 description and is not this search.",
        "",
    ]
    (gaps / "keyword-search.md").write_text("\n".join(keyword_lines), encoding="utf-8")
    print("wrote generated analysis and keyword search")


def write_sources_readme() -> None:
    text = f"""# Sources

Each collection lives in its own folder.

| Folder | What it is |
| --- | --- |
| [pursue-01](pursue-01/README.md) through [pursue-06](pursue-06/README.md) | The six Department of War PURSUE releases |
| [catalog](catalog/) | Untouched copies of the official `uap-data.csv` spreadsheet, several dates |
| [dvids](dvids/) | Metadata fetched from DVIDS on October 6, 2026 (not the media files) |
| [press](press/) | Short extracts of the six Department of War press releases, with archive links |
| [house-oversight](house-oversight/README.md) | Rep. Luna's March 31, 2026 video-request letter (the PDF, plus a short note) |

Room is deliberately left for later collections that are not in this version: AARO's own reports, FOIA reading-room releases, and National Archives record groups. Add them as new folders here (`sources/aaro-historical-2024/`, `sources/foia-…`, `sources/nara-…`). Do not renumber the PURSUE folders.

The catalog snapshot this version is built from is `catalog/uap-data-2026-09-29-release-6v5.csv`.

- Live URL: {CATALOG_LIVE}
- Archived copy used: {CATALOG_ARCHIVE}

On October 6, 2026 a direct request to war.gov from this project returned HTTP 403. Counts in the manifests were checked against the archived CSV, not against a live download that day.
"""
    (ROOT / "sources" / "README.md").write_text(text, encoding="utf-8")
    catalog_readme = """# Official catalog snapshots

These CSV files are the Department of War spreadsheet that the PURSUE website uses, saved from the Internet Archive. They are stored as retrieved (UTF-8, with the header row the site publishes). They are public-domain U.S. government records.

| File | Wayback timestamp | What it contains |
| --- | --- | --- |
| `uap-data-2026-05-20.csv` | 2026-05-20 09:58:41 | Release 01 only, 158 rows. NASA-UAP-D003A is still type VID. Two titles still have the original spelling (Correspondance, Techincal). |
| `uap-data-2026-09-18-release-6.csv` | 2026-09-18 11:39:50, `?release=6` | 446 rows. Release 06 has 71 rows (videos, no Colorado transcripts). D003A is already type AUD. |
| `uap-data-2026-09-18-release-6v3.csv` | 2026-09-18 15:56:29, `?release=6v3` | 447 rows. Release 06 has 72 rows. LLE-UAP-D001 is in. |
| `uap-data-2026-09-19-release-6.csv` | 2026-09-19 20:49:42, `?release=6` | 447 rows. Release 06 still has 72 rows and only D001. |
| `uap-data-2026-09-29-release-6v5.csv` | 2026-09-29 12:00:48, `?release=6v5` | **The snapshot this archive is built from.** 450 rows. Release 06 has 75, including D002–D004. |

SHA-256 checksums are in `SHA256SUMS` next to the files.

Archive URL for the snapshot in use:

https://web.archive.org/web/20260929120048/https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6v5

No newer successful capture of this spreadsheet was in the Internet Archive's CDX index when this archive was built (checked October 6, 2026). That is not proof the live site was unchanged after September 29. The live site could not be opened from this project's network.
"""
    (ROOT / "sources" / "catalog" / "README.md").write_text(catalog_readme, encoding="utf-8")
    dvids_readme = """# DVIDS metadata

`metadata-2026-10-06.json` is a scrape of the DVIDS pages named in the catalog's "DVIDS Video ID" column. It was collected on October 6, 2026 from `https://www.dvidshub.net/video/{id}`, which is where both the video and the audio items resolved.

For each id the file records the final page URL, the open-graph title, the on-page fields (date taken, date posted, length, location, VIRIN, filename), the media URL embedded in the page, and the `Content-Length` and `ETag` returned by an HTTP HEAD request to that media URL.

The media files themselves are not in this repository. The largest object reported by HEAD was over 3 GB. SHA-256 checksums were not computed.

DVIDS is a Department of Defense public distribution site. The page text is treated as **official**. The HTTP size and ETag are measurements made by this project (**analysis** of a header, not a government statement of the size).
"""
    (ROOT / "sources" / "dvids" / "README.md").write_text(dvids_readme, encoding="utf-8")


def write_press_extracts() -> None:
    folder = ROOT / "sources" / "press"
    folder.mkdir(parents=True, exist_ok=True)
    pages = {
        "2026-05-08-release-01.md": """# Release 01 press statement, May 8, 2026

**Label: official.** Extracted from the Department of War release page. This is not the full HTML of the page. The untouched archived page is linked below. U.S. government work, public domain.

- Live: https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/
- Archived: https://web.archive.org/web/20260508125016/https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/

Headline on the page: "Department of War Releases Unidentified Anomalous Phenomena Files in Historic Transparency Effort."

The page says the initial release is part of the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE), an interagency effort including the White House, ODNI, the Department of Energy, the Department of War's All-domain Anomaly Resolution Office (AARO), NASA, the FBI, and additional intelligence-community components. It says the collection will be housed on WAR.GOV/UFO and that additional files will be released on a rolling basis.

It says: "While all of the files have been reviewed for security purposes, many of the materials have not yet been analyzed for resolution of any anomalies."

Quoted on the page:

- Secretary of War Pete Hegseth: "The Department of War is in lockstep with President Trump to bring unprecedented transparency regarding our government's understanding of Unidentified Anomalous Phenomena. These files, hidden behind classifications, have long fueled justified speculation — and it's time the American people see it for themselves."
- Director of National Intelligence Tulsi Gabbard, describing the release as the first in an ongoing joint declassification effort.
- FBI Director Kash Patel, saying the FBI is participating in the release.
- NASA Administrator Jared Isaacman: "We will remain candid about what we know to be true, what we have yet to understand, and all that remains to be discovered."
""",
        "2026-05-22-release-02.md": """# Release 02 press statement, May 22, 2026

**Label: official.** Statement attributable to Assistant to the Secretary of War for Public Affairs and Chief Pentagon Spokesman Sean Parnell. Extract, not the full page HTML.

- Live: https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/
- Archived: https://web.archive.org/web/20260522135306/https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/

Parnell says the Department is publishing the second release of declassified and historical UAP files under PURSUE, that the collection continues to be housed on WAR.GOV/UFO, and that additional files will be released on a rolling basis.

He says that since the site's launch on May 8, 2026, WAR.GOV/UFO "has received over 1 billion hits worldwide."
""",
        "2026-06-12-release-03.md": """# Release 03 press statement, June 12, 2026

**Label: official.** Statement attributable to Sean Parnell. Extract, not the full page HTML.

- Live: https://www.war.gov/News/Releases/Release/Article/4515408/department-of-war-publishes-third-release-of-unidentified-anomalous-phenomena-f/
- Archived: https://web.archive.org/web/20260612161132/https://www.war.gov/News/Releases/Release/Article/4515408/department-of-war-publishes-third-release-of-unidentified-anomalous-phenomena-f/

Parnell says the Department is publishing the third release. He says WAR.GOV/UFO "has received over 1.7 billion hits worldwide since the site's launch on May 8, 2026."
""",
        "2026-07-10-release-04.md": """# Release 04 press statement, July 10, 2026

**Label: official.** Statement attributable to Sean Parnell. Extract, not the full page HTML.

- Live: https://www.war.gov/News/Releases/Release/Article/4539898/department-of-war-publishes-fourth-release-of-unidentified-anomalous-phenomena/
- Archived: https://web.archive.org/web/20260710134746/https://www.war.gov/News/Releases/Release/Article/4539898/department-of-war-publishes-fourth-release-of-unidentified-anomalous-phenomena/

Parnell says the Department is publishing the fourth release, that further files will follow on a rolling basis, and that the fourth release is available on WAR.GOV/UFO. This statement does not give a hit count.
""",
        "2026-08-07-release-05.md": """# Release 05 press statement, August 7, 2026

**Label: official.** Statement attributable to Sean Parnell. Extract, not the full page HTML.

- Live: https://www.war.gov/News/Releases/Release/Article/4565994/department-of-war-publishes-fifth-release-of-unidentified-anomalous-phenomena-f/
- Archived: https://web.archive.org/web/20260807151112/https://www.war.gov/News/Releases/Release/Article/4565994/department-of-war-publishes-fifth-release-of-unidentified-anomalous-phenomena-f/

Parnell says the Department is publishing the fifth release and that the Department and agency partners are working on the next release. This statement does not give a hit count.
""",
        "2026-09-18-release-06.md": """# Release 06 press statement, September 18, 2026

**Label: official.** Statement attributable to Sean Parnell. Extract, not the full page HTML.

- Live: https://www.war.gov/News/Releases/Release/Article/4604795/department-of-war-publishes-sixth-release-of-unidentified-anomalous-phenomena-f/
- Archived: https://web.archive.org/web/20260918155319/https://www.war.gov/News/Releases/Release/Article/4604795/department-of-war-publishes-sixth-release-of-unidentified-anomalous-phenomena-f/

Parnell says the Department is publishing the sixth release and that further files will follow on a rolling basis. This statement does not give a file count. The catalog snapshot from later the same morning (11:39 UTC) contains 71 Release 06 rows; the September 29 snapshot contains 75. See [catalog quality](../../analysis/catalog-quality.md).
""",
    }
    for name, body in pages.items():
        (folder / name).write_text(body, encoding="utf-8")
    (folder / "README.md").write_text(
        """# Press statements

These are short extracts of the six Department of War release announcements. The pages are U.S. government work. The extracts are here so the statements can be searched without copying the website's navigation chrome. The archived full page is linked at the top of each file.

**Label: official.**
""",
        encoding="utf-8",
    )


def main() -> None:
    rows = load_catalog()
    assert_catalog_shape(rows)
    dvids_meta = json.loads(DVIDS_META.read_text(encoding="utf-8"))
    records = build_records(rows, dvids_meta)
    if len(records) != 450:
        raise SystemExit("record count drifted")
    if len({rec["id"] for rec in records}) != 450:
        raise SystemExit("archive ids are not unique")
    if len({rec["catalog_order"] for rec in records}) != 450:
        raise SystemExit("catalog order collided")
    write_records(records, dvids_meta)
    write_manifests(records)
    write_generated_analysis(rows, records, dvids_meta)
    write_sources_readme()
    write_press_extracts()
    digest = hashlib.sha256(CATALOG.read_bytes()).hexdigest()
    print("catalog sha256", digest)


if __name__ == "__main__":
    main()
