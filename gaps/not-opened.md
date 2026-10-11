# What was not opened

**Label: analysis.** A limit of this version, stated so it is not mistaken for a conclusion.

## The underlying files

On October 6, 2026, requests to war.gov from this project returned HTTP 403. The Internet Archive's availability API returned no snapshot for sample media URLs (one Release 01 image and one Release 06 PDF). Those two checks were not repeated for all 450 files.

So:

- No PDF in this archive was opened.
- No video was watched.
- No audio was played.
- SHA-256 was computed for the public MP4 linked from each DVIDS page (149 files, October 6, 2026). The bytes were not committed. Download-menu renditions returned HTTP 403 and were not hashed. Rows whose DVIDS id points at a different file do not carry that other file's hash. See [DVIDS coverage](dvids-coverage.md).

Record pages quote the catalog description and, where a DVIDS page loaded, the DVIDS description. Where a DVIDS id exists, the page URL, the media URL, and the size from an HTTP HEAD request are recorded. The largest object hashed that way was over 3 gigabytes. The official download bundles, as sized on the October 4, 2026 archived homepage, run from tens of megabytes to 5.6 gigabytes. They were not downloaded. Sizes by release are on each collection's manifest, for example [Release 01](../sources/pursue-01/manifest.md).

## What *was* opened

- The official spreadsheet, from Internet Archive snapshots, including the September 29, 2026 `release=6v5` file used to build every record. Checksums are in [sources/catalog/SHA256SUMS](../sources/catalog/SHA256SUMS).
- The PURSUE homepage archived October 4, 2026.
- The six Department of War press releases, from Wayback captures. Extracts are in [sources/press](../sources/press/).
- DVIDS pages for every catalog DVIDS id (149 unique ids), retrieved live on October 6, 2026, plus the download popup, the HLS playlist, a HEAD request for each public media file, and a full download of that public MP4 used only to compute SHA-256. Metadata is in [sources/dvids](../sources/dvids/). Which videos have no DVIDS copy of themselves is in [DVIDS coverage](dvids-coverage.md).

## How to go further

A later version can store a file when three things are true: the bytes are actually retrieved, the file is small enough to keep the repository easy to clone (this version's cutoff is about 10 MB, and even under that line the videos were left as links), and a SHA-256 is recorded. The public DVIDS MP4s were downloaded only to compute that hash, then discarded. "The file says" on a record page means the catalog description, or the DVIDS page description when that section is labeled official. It does not mean the media was watched.
