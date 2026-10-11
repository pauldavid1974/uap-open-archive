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
- `sha256`, when set, is the SHA-256 of the public DVIDS MP4 linked from the page, downloaded October 6, 2026. The file is not in the repository. It is null when that file was not hashed for this row, including when the DVIDS id points at a different catalog entry. `sha256_note` says which. `file_size_bytes` is the Content-Length from an HTTP HEAD of that same public MP4. `http_etag` is the server's tag, not a checksum. `dvids_downloads` is the download popup: resolution, the size text DVIDS printed, and the HTTP status of the menu URL. Exact byte length there is null when the menu URL did not return it.

A case has `status`: `explained`, `disputed`, or `unexplained`. Read the first paragraph before trusting the word. `in_pursue_catalog` is false for the 2019–2020 Colorado and Nebraska drone page, which is here so it is not confused with a file that does exist.
