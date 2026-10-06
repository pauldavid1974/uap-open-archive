# Schemas

These JSON Schema files describe the YAML at the top of each page. The validator (`scripts/validate.py`) checks every record, case, entity, and manifest against them.

| File | What it checks |
| --- | --- |
| [record.schema.json](record.schema.json) | One catalog item in `records/` |
| [case.schema.json](case.schema.json) | One episode in `cases/` |
| [entity.schema.json](entity.schema.json) | One person, place, program, agency, or platform in `entities/` |
| [manifest.schema.json](manifest.schema.json) | One release list in `sources/pursue-0N/manifest.json` |

Fields you will see on a record:

- `id` is the filename. `official_id` is the government's id, when the title has one. Some old files have no official id. FBI-UAP-D014 is used twice, so those two pages have different `id`s and the same `official_id`.
- `release_date` is the day the tranche was posted. `incident_date` is when the catalog says the event happened, normalized when the cell is a real date. `incident_date_raw` is the cell unchanged.
- `catalog_redaction_flag` is the spreadsheet's yes/no. `redaction_level` is only `flagged` or `not_flagged`. The spreadsheet does not say how much was removed.
- `labels` on a record are `official` (the quoted catalog text) and `analysis` (our framing paragraph).
- `underlying_file_opened` is false for every row in this version. See [what was not opened](../gaps/not-opened.md).
- `witnesses` and `sensors` are empty lists. Names were not pulled out of the prose by software, because that mixes a mention with a witness. The names are in the quoted description.
- `sha256` is null. The file bytes were not downloaded. `file_size_bytes` is set only when a DVIDS media URL answered an HTTP HEAD request. `http_etag` is that server's tag, not a checksum.

A case has `status`: `explained`, `disputed`, or `unexplained`. Read the first paragraph before trusting the word. `in_pursue_catalog` is false for the 2019–2020 Colorado and Nebraska drone page, which is here so it is not confused with a file that does exist.
