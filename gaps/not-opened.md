# What was not opened

**Label: analysis.** A limit of this version, stated so it is not mistaken for a conclusion.

## The underlying files

On October 6, 2026, requests to war.gov from this project returned HTTP 403. The Internet Archive's availability API returned no snapshot for sample media URLs (one Release 01 image and one Release 06 PDF). Those two checks were not repeated for all 450 files.

So:

- No PDF in this archive was opened.
- No video was watched.
- No audio was played.
- No SHA-256 of a media file was computed.

Record pages quote the catalog description and say so in the first paragraph. Where a DVIDS id exists, the page URL, the media URL, and the size from an HTTP HEAD request are recorded. The largest object reported that way was over 3 gigabytes. The official download bundles, as sized on the October 4, 2026 archived homepage, run from tens of megabytes to 5.6 gigabytes. They were not downloaded. Sizes by release are on each collection's manifest, for example [Release 01](../sources/pursue-01/manifest.md).

## What *was* opened

- The official spreadsheet, from Internet Archive snapshots, including the September 29, 2026 `release=6v5` file used to build every record. Checksums are in [sources/catalog/SHA256SUMS](../sources/catalog/SHA256SUMS).
- The PURSUE homepage archived October 4, 2026.
- The six Department of War press releases, from Wayback captures. Extracts are in [sources/press](../sources/press/).
- DVIDS pages for every catalog DVIDS id (149 unique ids), retrieved live on October 6, 2026, plus a HEAD request for each media file's size. Metadata is in [sources/dvids](../sources/dvids/).

## How to go further

A later version can store a file when three things are true: the bytes are actually retrieved, the file is small enough to keep the repository easy to clone (this version's cutoff is about 10 MB, and even under that line the videos were left as links), and a SHA-256 is recorded. Until then, "the file says" on a record page means "the catalog description says."
