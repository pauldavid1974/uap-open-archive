#!/usr/bin/env python3
"""Validate records, cases, entities, manifests, and internal links.

Usage (from the repo root):
    python scripts/validate.py
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[1]
FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def load_schema(name: str) -> Draft202012Validator:
    schema = json.loads((ROOT / "schema" / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


def front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_RE.match(text)
    if not match:
        raise ValueError(f"{path} has no YAML front matter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{path} front matter is not a mapping")
    return data, text


def check_links(path: Path, text: str, errors: list[str]) -> None:
    for match in LINK_RE.finditer(text):
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes the repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path}: broken link {target}")


def main() -> int:
    errors: list[str] = []
    record_validator = load_schema("record.schema.json")
    case_validator = load_schema("case.schema.json")
    entity_validator = load_schema("entity.schema.json")
    manifest_validator = load_schema("manifest.schema.json")

    def content_pages(folder: str):
        for path in sorted((ROOT / folder).glob("*.md")):
            if path.name != "README.md":
                yield path

    records: dict[str, dict] = {}
    for path in content_pages("records"):
        try:
            data, text = front_matter(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if data.get("id") != path.stem:
            errors.append(f"{path}: id {data.get('id')!r} does not match filename")
        for err in record_validator.iter_errors(data):
            errors.append(f"{path}: {err.message} ({'.'.join(str(p) for p in err.path)})")
        if data.get("underlying_file_opened") is not False:
            errors.append(f"{path}: underlying_file_opened must stay false until a file is actually opened")
        check_links(path, text, errors)
        records[path.stem] = data

    if len(records) != 450:
        errors.append(f"expected 450 record files, found {len(records)}")

    orders = [data["catalog_order"] for data in records.values() if "catalog_order" in data]
    if sorted(orders) != list(range(1, 451)):
        errors.append("catalog_order is not a unique 1..450 sequence")

    cases: dict[str, dict] = {}
    case_dir = ROOT / "cases"
    if not case_dir.exists():
        errors.append("cases/ is missing")
    else:
        for path in content_pages("cases"):
            try:
                data, text = front_matter(path)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if data.get("id") != path.stem:
                errors.append(f"{path}: id does not match filename")
            for err in case_validator.iter_errors(data):
                errors.append(f"{path}: {err.message}")
            check_links(path, text, errors)
            for record_id in data.get("records") or []:
                if record_id not in records:
                    errors.append(f"{path}: unknown record {record_id}")
            for entity_id in data.get("entities") or []:
                entity_path = ROOT / "entities" / f"{entity_id}.md"
                if not entity_path.exists():
                    errors.append(f"{path}: unknown entity {entity_id}")
            cases[path.stem] = data

    entities: dict[str, dict] = {}
    for path in content_pages("entities"):
        try:
            data, text = front_matter(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if data.get("id") != path.stem:
            errors.append(f"{path}: id does not match filename")
        for err in entity_validator.iter_errors(data):
            errors.append(f"{path}: {err.message}")
        check_links(path, text, errors)
        for case_id in data.get("cases") or []:
            if case_id not in cases:
                errors.append(f"{path}: unknown case {case_id}")
        entities[path.stem] = data

    membership_path = ROOT / "sources" / "case-membership.json"
    if membership_path.exists() and cases:
        membership = json.loads(membership_path.read_text(encoding="utf-8"))
        for case_id, record_ids in membership.items():
            if case_id not in cases:
                errors.append(f"case-membership.json lists {case_id}, but cases/{case_id}.md does not exist")
                continue
            listed = cases[case_id].get("records") or []
            if listed != record_ids:
                errors.append(
                    f"{case_id}: case front matter records do not match sources/case-membership.json"
                )
        for case_id, data in cases.items():
            if data.get("in_pursue_catalog") and case_id not in membership and data.get("records"):
                errors.append(f"{case_id}: in the catalog but missing from case-membership.json")
            if not data.get("in_pursue_catalog") and data.get("records"):
                errors.append(f"{case_id}: marked not in the PURSUE catalog but lists records")

    for record_id, data in records.items():
        for case_id in data.get("related_cases") or []:
            if case_id not in cases:
                errors.append(f"records/{record_id}.md related case missing: {case_id}")
            elif record_id not in (cases[case_id].get("records") or []):
                errors.append(f"{record_id} points at {case_id}, but that case does not list it")

    catalog = ROOT / "sources" / "catalog" / "uap-data-2026-09-29-release-6v5.csv"
    with catalog.open(newline="", encoding="utf-8-sig") as handle:
        catalog_rows = list(csv.DictReader(handle))
    if len(catalog_rows) != len(records):
        errors.append(f"catalog has {len(catalog_rows)} rows and records/ has {len(records)} files")

    for manifest_path in sorted((ROOT / "sources").glob("pursue-*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for err in manifest_validator.iter_errors(manifest):
            errors.append(f"{manifest_path}: {err.message}")
        ids = [item["id"] for item in manifest["records"]]
        if len(ids) != manifest["record_count"]:
            errors.append(f"{manifest_path}: record_count does not match the list")
        for record_id in ids:
            if record_id not in records:
                errors.append(f"{manifest_path}: unknown record {record_id}")
            elif records[record_id]["collection"] != manifest["collection"]:
                errors.append(f"{manifest_path}: {record_id} belongs to a different collection")
        expected = sorted(rid for rid, data in records.items() if data["collection"] == manifest["collection"])
        if sorted(ids) != expected:
            errors.append(f"{manifest_path}: manifest ids do not match records in {manifest['collection']}")
        text = (manifest_path.parent / "manifest.md").read_text(encoding="utf-8")
        check_links(manifest_path.parent / "manifest.md", text, errors)

    # Other markdown internal links (README, guides, analysis, gaps, timelines, entities already done)
    extra_roots = [
        ROOT / "README.md",
        ROOT / "AI_GUIDE.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "CHANGELOG.md",
        ROOT / "llms.txt",
        ROOT / "cases" / "README.md",
        ROOT / "entities" / "README.md",
        ROOT / "schema" / "README.md",
        ROOT / "LICENSE",
    ]
    for folder in ("analysis", "gaps", "timelines", "sources"):
        extra_roots.extend((ROOT / folder).rglob("*.md"))
    seen = set()
    for path in extra_roots:
        if not path.exists() or path in seen:
            continue
        if "records" in path.parts:
            continue
        seen.add(path)
        check_links(path, path.read_text(encoding="utf-8"), errors)

    required = [
        ROOT / "data" / "records.json",
        ROOT / "data" / "records.csv",
        ROOT / "data" / "cases.json",
        ROOT / "data" / "cases.csv",
        ROOT / "data" / "entities.json",
        ROOT / "data" / "entities.csv",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing export {path.relative_to(ROOT)}")
    if (ROOT / "data" / "records.json").exists():
        exported = json.loads((ROOT / "data" / "records.json").read_text(encoding="utf-8"))
        if len(exported) != len(records):
            errors.append(f"data/records.json has {len(exported)} rows; records/ has {len(records)}")
        else:
            exported_ids = [item["id"] for item in exported]
            if exported_ids != sorted(records):
                errors.append("data/records.json is not sorted in the same order as records/*.md; re-run scripts/export_indexes.py")
        if (ROOT / "data" / "cases.json").exists():
            exported_cases = json.loads((ROOT / "data" / "cases.json").read_text(encoding="utf-8"))
            if len(exported_cases) != len(cases):
                errors.append("data/cases.json is out of date; re-run scripts/export_indexes.py")
        if (ROOT / "data" / "entities.json").exists():
            exported_entities = json.loads((ROOT / "data" / "entities.json").read_text(encoding="utf-8"))
            if len(exported_entities) != len(entities):
                errors.append("data/entities.json is out of date; re-run scripts/export_indexes.py")

    if errors:
        print(f"{len(errors)} validation error(s):", file=sys.stderr)
        for err in errors[:80]:
            print(f"- {err}", file=sys.stderr)
        if len(errors) > 80:
            print(f"... {len(errors) - 80} more", file=sys.stderr)
        return 1
    print(
        f"ok: {len(records)} records, {len(cases)} cases, {len(entities)} entities, links and schemas passed"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
