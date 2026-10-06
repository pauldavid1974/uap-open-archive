#!/usr/bin/env python3
"""Search record titles and official catalog descriptions.

Usage (from the repo root):
    python scripts/search.py "tremonton"
    python scripts/search.py "gulf of oman" --agency "Department of War"
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the UAP open archive index")
    parser.add_argument("query", help="Text to find in the title or official description")
    parser.add_argument("--agency", default="", help="Optional agency filter, case-insensitive substring")
    parser.add_argument("--collection", default="", help="Optional collection id, for example pursue-01")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    records = json.loads((ROOT / "data" / "records.json").read_text(encoding="utf-8"))
    needle = args.query.lower()
    hits = []
    for record in records:
        if args.collection and record.get("collection") != args.collection:
            continue
        if args.agency and args.agency.lower() not in (record.get("agency") or "").lower():
            continue
        blob = f"{record.get('title','')}\n{record.get('official_description','')}".lower()
        if needle in blob:
            hits.append(record)
    print(f"{len(hits)} match(es) for {args.query!r}")
    for record in hits[: args.limit]:
        print(
            f"- {record['id']} | {record.get('official_id') or '-'} | {record.get('release_date')} | "
            f"{record.get('agency')} | {record.get('title')}"
        )
    if len(hits) > args.limit:
        print(f"... {len(hits) - args.limit} more. Raise --limit to see them.")


if __name__ == "__main__":
    main()
