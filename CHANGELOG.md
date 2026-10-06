# Changelog

## 1.0.0 — 2026-10-06

First version of the archive.

- All 450 rows of the Department of War PURSUE catalog, from the Internet Archive snapshot of September 29, 2026 (`uap-data.csv?release=6v5`).
- One Markdown record per row. The official description is quoted. The underlying PDFs, videos, and audio were not opened. war.gov returned HTTP 403, and sample media URLs had no Wayback copy.
- Manifests for Releases 01 through 06. The record pages use the September 29 counts (158, 64, 72, 40, 41, and 75). Each manifest also lists earlier snapshots, because those counts moved.
- Catalog snapshots kept for that history: May 20; September 18 at 11:39 UTC (`release=6`, 71 rows in Release 06); September 18 at 15:56 UTC (`release=6v3`, 72 rows); September 19 (still 72); September 29 (`release=6v5`, 75).
- An October 5, 2026 fact-check of the research memo is folded in. Launch-week press counted 162 Release 01 rows; the stored CSVs have 158. The zip-bundle explanation is dropped. NASA-UAP-D003A changed from video to audio after May 20. Luna's March 31 letter is stored and kept separate from the March 6 request. Apollo frame AS17-147-22470 is identified from NASA's own image pages. The Denver Gazette's Colorado details are cited as press. The AAWSAP contract trail is not called new. Thirteen unverified claims are listed and left unverified.
- DVIDS page metadata and HTTP file sizes for every catalog DVIDS id, retrieved October 6, 2026. Media files are linked, not stored.
- Case files for the episodes a general reader is most likely to ask about, plus entity pages, two timelines, redaction and catalog-quality notes, and a keyword search for famous cases that are not named in the spreadsheet.
- JSON and CSV indexes, JSON Schema, and a GitHub Actions check that validates schemas and internal links.

Counts and limits are stated in the [README](README.md). Disagreements with a prior research memo are listed there under "Honest limits."
