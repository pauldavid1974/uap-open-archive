# Changelog

## 1.1.0 — 2026-10-06

DVIDS page metadata for every catalog DVIDS id, fetched again the same day and kept beside the first scrape.

- For each id: page URL, title, date taken, date posted, duration, the description paragraph verbatim, each download-popup resolution with the size text DVIDS printed, and the HLS renditions. The fetch date and source are on the record.
- Download-menu URLs returned HTTP 403. Exact byte lengths of those renditions were not measured and were not guessed.
- SHA-256 of the public MP4 linked from each DVIDS page, 149 files. The bytes were not committed. The hash is stored on the catalog row the page matches.
- DVIDS 1006111 and 1007720 are flagged. 1006111 is the Army video DOW-UAP-PR049, and the same id on FBI Photo A001 points at that video. 1007720 is DOW-UAP-PR057a, and the same id on DOW-UAP-PR057b points at that video. No corrected id is proposed. The sitemap search is in [gaps/dvids-coverage.md](gaps/dvids-coverage.md).
- No DVIDS caption file or transcript heading was on these pages. None were added.
- war.gov/UFO still returned HTTP 403. The underlying files were still not opened.

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
