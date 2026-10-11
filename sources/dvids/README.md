# DVIDS metadata

Two files, both fetched on October 6, 2026. Neither file is a media binary.

`metadata-2026-10-06.json` is the first scrape of the DVIDS pages named in the catalog's "DVIDS Video ID" column, from `https://www.dvidshub.net/video/{id}`. It records the final page URL, the open-graph title, the on-page fields, the media URL, and the `Content-Length` and `ETag` from an HTTP HEAD request. It is kept so that scrape is not thrown away.

`enrichment-2026-10-06.json` is a second fetch the same day, written by `scripts/fetch_dvids_enrichment.py`. For each id it records the page URL, the on-page title, date taken, date posted, duration, and the description paragraph verbatim. It also records each row of the download popup (`/download/popup/{id}`): resolution, the size text DVIDS printed, bitrate when the cell was not blank, the download URL, and the HTTP status of a HEAD request. Exact byte length is set only when that HEAD returned HTTP 200 with Content-Length. The HLS playlist renditions (resolution and bandwidth) are included. Caption and transcript checks are included. Where the public MP4 linked from the page downloaded in full, the file's SHA-256 is recorded. The bytes were not committed.

DVIDS is a Department of Defense public distribution site. Page text, popup rows, and playlist fields are **official**. HTTP sizes, ETags, and SHA-256 hashes are measurements made by this project (**analysis**).

Which catalog videos have no DVIDS copy of that video is in [gaps/dvids-coverage.md](../../gaps/dvids-coverage.md).
