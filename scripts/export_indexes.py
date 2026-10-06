#!/usr/bin/env python3
"""Build data/*.json and data/*.csv from Markdown front matter.

Usage (from the repo root):
    python scripts/export_indexes.py
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def load_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_RE.match(text)
    if not match:
        raise SystemExit(f"No YAML front matter: {path}")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise SystemExit(f"Front matter is not a mapping: {path}")
    return data, text[match.end():]


def section(body: str, heading: str) -> str:
    marker = f"## {heading}\n"
    start = body.find(marker)
    if start < 0:
        return ""
    start += len(marker)
    end = body.find("\n## ", start)
    chunk = body[start:] if end < 0 else body[start:end]
    return chunk.strip()


def unquote(block: str) -> str:
    lines = []
    for line in block.splitlines():
        if line.startswith("> "):
            lines.append(line[2:])
        elif line == ">":
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines).strip()


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            flat = {}
            for field in fields:
                value = row.get(field)
                if isinstance(value, list):
                    flat[field] = " | ".join(str(item) for item in value)
                elif isinstance(value, bool):
                    flat[field] = "true" if value else "false"
                elif value is None:
                    flat[field] = ""
                else:
                    flat[field] = value
            writer.writerow(flat)


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    def pages(folder: str):
        for path in sorted((ROOT / folder).glob("*.md")):
            if path.name == "README.md":
                continue
            yield path

    records = []
    for path in pages("records"):
        meta, body = load_front_matter(path)
        description = unquote(section(body, "Official catalog description"))
        summary = section(body, "Plain-English summary")
        # drop the label line from the summary used in the index
        summary_lines = [line for line in summary.splitlines() if line.strip() and not line.startswith("**Label:")]
        meta = dict(meta)
        meta["official_description"] = description
        meta["plain_summary"] = "\n".join(summary_lines).strip()
        meta["path"] = f"records/{path.name}"
        records.append(meta)

    cases = []
    for path in pages("cases"):
        meta, _body = load_front_matter(path)
        meta = dict(meta)
        meta["path"] = f"cases/{path.name}"
        cases.append(meta)

    entities = []
    for path in pages("entities"):
        meta, _body = load_front_matter(path)
        meta = dict(meta)
        meta["path"] = f"entities/{path.name}"
        entities.append(meta)

    (DATA / "records.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (DATA / "cases.json").write_text(json.dumps(cases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (DATA / "entities.json").write_text(json.dumps(entities, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    write_csv(
        DATA / "records.csv",
        records,
        [
            "id",
            "official_id",
            "title",
            "collection",
            "agency",
            "type",
            "release_date",
            "incident_date",
            "incident_date_raw",
            "incident_date_precision",
            "location",
            "location_raw",
            "catalog_redaction_flag",
            "redaction_level",
            "featured",
            "dvids_id",
            "file_size_bytes",
            "media_url",
            "related_cases",
            "underlying_file_opened",
            "catalog_order",
            "path",
            "plain_summary",
        ],
    )
    write_csv(
        DATA / "cases.csv",
        cases,
        ["id", "title", "status", "in_pursue_catalog", "incident_date", "location", "records", "entities", "labels", "path"],
    )
    write_csv(
        DATA / "entities.csv",
        entities,
        ["id", "title", "kind", "labels", "cases", "path"],
    )
    print(f"exported {len(records)} records, {len(cases)} cases, {len(entities)} entities")


if __name__ == "__main__":
    main()
