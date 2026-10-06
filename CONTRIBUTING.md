# Contributing

This archive is for a general reader and for any AI pointed at the repository. The rule that beats every other rule: do not invent. If you cannot open the source, say so.

## Labels

Every claim is one of:

| Label | Meaning |
| --- | --- |
| official | A government document or a government website, quoted or closely paraphrased, with a URL |
| press | A news organization. Summarize and link. Do not paste the article |
| advocate | A UFO or disclosure site, or an interested witness's public claim. A lead, not a fact |
| skeptic | A skeptical analysis. Same standard: label it, link it, do not treat it as the file |
| analysis | Our arithmetic, our reading, our uncertainty |

Do not blend a skeptic's theory into an official paragraph.

## What is generated

These paths are rewritten by `python scripts/build_archive.py`. Do not hand-edit them. Change the script, then rebuild.

- `records/*.md`
- `sources/pursue-01/` through `sources/pursue-06/`
- `sources/case-membership.json`
- `analysis/redaction.md`
- `analysis/catalog-quality.md`
- `gaps/keyword-search.md`
- the READMEs under `sources/` that the script writes

Case pages, entity pages, timelines, and the other analysis and gap notes are written by hand. If a rebuild changes `sources/case-membership.json`, update the matching case's `records:` list to the new order. The validator checks that the two lists match.

After a rebuild:

```bash
python scripts/export_indexes.py
python scripts/validate.py
```

## How to check the count against the official catalog

The live spreadsheet is:

`https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv?release=6v5`

war.gov often refuses automated downloads. The Internet Archive captures it. Save a new capture under `sources/catalog/` with the date in the filename, and record its SHA-256 in `sources/catalog/SHA256SUMS`.

From a checkout:

```bash
python -c "
import csv
from collections import Counter
p='sources/catalog/uap-data-2026-09-29-release-6v5.csv'
rows=list(csv.DictReader(open(p, newline='', encoding='utf-8-sig')))
print('rows', len(rows))
print(Counter(r['Release Date'] for r in rows))
print('redacted', sum(1 for r in rows if (r['Redaction'] or '').strip().upper()=='TRUE'))
"
```

This version's record pages are built from the September 29, 2026 snapshot: 450 rows, and release counts 158, 64, 72, 40, 41, 75. Those are not the counts on every earlier date. Release 01 launch-week press said 162. Release 06 was 71, then 72, then 75. If a newer snapshot differs, that difference is the news. Write the new snapshot's date into the manifest's version table. Do not silently "fix" an old snapshot, and do not replace the history with one number.

## Adding a new release

1. Capture the new `uap-data.csv` and the Department of War press release (live and, if possible, an archive.org URL).
2. Point `CATALOG` in `scripts/build_archive.py` at the new snapshot, and add the new release date to the `RELEASES` table (collection id `pursue-07`, and so on). Add the id to `schema/record.schema.json`.
3. Fetch DVIDS metadata for any new DVIDS ids. Extend `sources/dvids/` rather than throwing away the October 6, 2026 file. Record sizes with HTTP HEAD. Do not commit video or audio binaries. Do not commit PDFs over about 10 MB. If you do commit a small public-domain file, store its SHA-256 and leave the original bytes unmodified.
4. Rebuild, export, and validate.
5. Add or extend case files only for rows you have actually read in the catalog. Quote the description. Say if you still have not opened the PDF.
6. Recount. If a news story's file count differs from the spreadsheet, record both numbers and say which one you counted.

## Adding any other collection

AARO reports, FOIA batches, and National Archives scans belong in a new folder under `sources/`, not inside a PURSUE release. Give the collection its own manifest. Government records can be stored in full when they are small enough. News and advocacy sites are summarized and linked, never copied wholesale.

## Reporting an error

Open an issue or a pull request. Name the record id, the sentence you think is wrong, and the source URL that shows the correction. A wrong official quote is an urgent fix. A disagreement with an `analysis` paragraph is a normal edit, as long as the new paragraph stays labeled.
