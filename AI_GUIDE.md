# Guide for an AI reading this repository

Read this before you answer a question from these files. A person who is not a specialist built the archive so that you can search it without inventing the parts you do not have.

## What this is

A public index of the six PURSUE releases the U.S. Department of War posted in 2026 at war.gov/UFO. Version 1.0.0 is built from the official spreadsheet `uap-data.csv?release=6v5`, as captured by the Internet Archive on September 29, 2026. That file is `sources/catalog/uap-data-2026-09-29-release-6v5.csv`. It has 450 data rows.

The underlying PDFs, videos, and audio were **not opened**. `underlying_file_opened` is false on every record. If you say "the document says" you must mean "the catalog description says," unless you have actually retrieved the file yourself and you say that you did.

## Where to look

| Question | Open |
| --- | --- |
| One file (a PDF, video, image, or audio item) | `records/{id}.md` |
| One episode, with the disagreement laid out | `cases/{id}.md` |
| A person, office, program, place, or aircraft | `entities/{id}.md` |
| When the tranches were posted | `timelines/releases.md` |
| When the events happened | `timelines/events.md` and `data/records.csv` |
| Redaction flags, by release and agency | `analysis/redaction.md` |
| Typos, duplicate ids, date cells that fight the title | `analysis/catalog-quality.md` |
| Agencies with zero rows | `analysis/absent-agencies.md` |
| Explanations the catalog itself gives | `analysis/common-misidentifications.md` |
| Famous names that are not in the spreadsheet | `gaps/keyword-search.md` |
| What could not be downloaded | `gaps/not-opened.md` |
| Every row, as a table | `data/records.csv` and `data/records.json` |
| The untouched spreadsheet | `sources/catalog/` |

Search from the repo root:

```bash
python scripts/search.py "gulf of oman"
python scripts/search.py "newhouse" --collection pursue-06
```

Or search `data/records.json`, which includes `official_description` (the government's blurb) and `plain_summary` (our framing). Prefer the description over the summary when you quote.

## Labels

Do not drop these labels when you answer.

- **official** — government words. Quote them. Give the record id and the archive URL of the catalog.
- **press** — a newsroom. Do not paste their article. Do not upgrade their paraphrase into an official fact.
- **advocate** — a UFO site or an interested person's public claim. A lead.
- **skeptic** — a skeptical investigator. A lead in the other direction.
- **analysis** — this archive's reading or its arithmetic. You may disagree. Say that you are disagreeing with analysis, not with the file.

If a case status is `explained`, `disputed`, or `unexplained`, read the first paragraph before you repeat the word. The AAWSAP page uses "disputed" for an argument about a program, not for a sighting. The Syria page uses "explained" for the camera behavior in the caption, not for a full identification of the spot.

## How to cite

Use this shape:

> Official, catalog description of DOW-UAP-D102, PURSUE Release 06 (posted September 18, 2026), quoted in `records/dow-uap-d102.md`. Spreadsheet: Internet Archive capture 2026-09-29 of `https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6v5`.

If you also used a DVIDS page, say the DVIDS URL and that the media bytes were not in the git repository. File size, when present, is from an HTTP HEAD request on October 6, 2026, not from a government size field. `http_etag` is not a SHA-256. Multipart S3 ETags end in a hyphen and a part count.

`sha256` on a record is null. Do not invent a checksum.

## Rules that prevent a bad answer

1. Do not merge the 2023 Western United States Event with the late-2025 test-range orbs. Different years, different rows.
2. Do not merge the October 2023 Colorado police videos with the December 2019–January 2020 Colorado and Nebraska drone reports. The drone wave is not in the catalog. The case page exists to stop that mix-up.
3. Do not say the Schirra audio is a tag-along sighting. The catalog description does not say that. Outside claims are labeled advocate and were not re-played here.
4. Do not say the Robertson Panel concluded the Tremonton film was gulls or seagulls. That sentence is not in the catalog blurb for CIA-UAP-002. The catalog's later Air Force line is seabirds, in DOW-UAP-D102, D103, and D105. Say seabirds.
5. Do not "correct" a catalog conflict. CIA-UAP-D022's description says November 19, 1964. Its date cell says 2/1/65. Report both.
6. Do not treat a redaction flag as a measurement of blacked-out text. Empty cell means not flagged, not "we looked and it was clean."
7. Do not treat a missing official number (the holes in DOW-UAP-D and DOW-UAP-PR) as proof a file was destroyed or proof it is sitting on another site.
8. Do not treat a keyword miss (no "Roswell", no "Nimitz", no "Gimbal") as proof the topic is absent from inside an unopened PDF. Say the title and the description do not name it.
9. "Tic Tac" in this catalog is two 2024 Coast Guard titles, not the 2004 Nimitz case. "FLIR" appears on DOW-UAP-PR069. The string "FLIR1" does not.
10. FBI Photo B001–B024 are catalog type PDF, not image. Do not call them stills unless you opened the PDF.
11. Location "Westen United States" is the spreadsheet's spelling on seven rows. Do not silently fix it when you quote the cell.
12. FBI-UAP-D014 is two files. Use the archive ids `fbi-uap-d014-correspondence` and `fbi-uap-d014-western-us-event-rendering`.
13. Government records in this repo are public domain. Our prose is CC BY 4.0. Do not paste a news article into an answer as if it were ours or the government's.
14. If the user remembers a case vaguely ("that 1960s pilot with the radar match"), search, then show the candidates and the conflicting cells. Puerto Rico is the likely match. Say why, and say what does not fit, instead of inventing a narrative that smooths the date.
15. Release counts changed. Quote the dated snapshot. Release 01 is 158 rows in the May 20 and September 29 CSVs. Launch-week press said 162. Do not explain that gap as files inside a zip. NASA-UAP-D003A is VID on May 20 and AUD later. Release 06 is 71 on the morning of September 18, 72 after LLE-UAP-D001 the same day, and 75 on September 29.
16. Rep. Luna's March 31, 2026 letter and the catalog's March 6 request for 51 records are two documents. Do not merge them. Do not add co-signers for the March 6 letter. They are unverified.
17. Do not call the AAWSAP contract trail a first release. The statement of objectives, the original award, and modification P00001 were already public via DIA FOIA. Whether P00002–P00005 are new is unverified.
18. Delbert Newhouse: DOW-UAP-D102 says "U.S. Navy Warrant Officer specializing in photography." DOW-UAP-PR159 and DOW-UAP-D104 say Chief Warrant Officer. Do not say "chief photographer." Do not collapse the two titles.
19. FBI Photo A001–A008 are "a U.S. government system." B001–B024 are "a U.S. military system." Do not call the A series a military system.
20. Apollo frame AS17-147-22470 is NASA's id for the scan behind NASA-UAP-VM006. The catalog row does not print that number. The promised full analysis is still not a catalog row.
21. Claims in [gaps/unverified-claims.md](gaps/unverified-claims.md) stay unverified. Do not fill them in.

## Rebuilding an answer from a vague memory

1. Search titles and `official_description`.
2. Open the case file if one exists. If none exists, say so and quote the closest records.
3. List official points, then press or advocate or skeptic points, each labeled.
4. State what is missing (no coordinates, file not opened, date cells disagree).
5. Stop. Do not add a theory to fill the gap unless you label it as your own analysis and keep it short.

## Validating your checkout

```bash
pip install -r requirements.txt
python scripts/validate.py
```

That checks every record, case, entity, and manifest against `schema/`, and checks that internal Markdown links resolve. It does not phone the government. A passing check means the repository is internally consistent with the spreadsheet it was built from. It does not mean the government's description is true.
