#!/usr/bin/env python3
"""Find relevant source headlines in the bundled 6,835-row winner-only sample."""

import argparse
import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Optional


DATASET = Path(__file__).resolve().parent.parent / "references" / "articles-over-100k.csv"
LEVELS = ("L0", "L1", "L2", "L3", "L4")


def load_rows(path: Path = DATASET) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {
            "posted_utc", "handle", "title", "views", "topic", "level", "moves",
            "failure_marks", "followers_at_scan", "english", "article_url", "preview",
        }
        missing = required - set(reader.fieldnames or ())
        if missing:
            raise ValueError("Dataset columns missing: " + ", ".join(sorted(missing)))
        rows = list(reader)
    for row in rows:
        int(row["views"])
        int(row["followers_at_scan"])
    return rows


def select_examples(
    rows: list[dict[str, str]],
    *,
    topic: Optional[str] = None,
    levels: tuple[str, ...] = ("L3", "L4"),
    small_accounts: bool = False,
    query: str = "",
    since: Optional[date] = None,
    sort: str = "views",
    limit: int = 6,
) -> list[dict[str, str]]:
    matches = [
        row for row in rows
        if row["english"].lower() == "yes"
        and (topic is None or row["topic"].casefold() == topic.casefold())
        and row["level"] in levels
        and (not small_accounts or int(row["followers_at_scan"]) < 10_000)
        and query.casefold() in (row["title"] + " " + row["preview"]).casefold()
        and (since is None or date.fromisoformat(row["posted_utc"][:10]) >= since)
    ]
    if sort == "recent":
        matches.sort(key=lambda row: (row["posted_utc"], int(row["views"])), reverse=True)
    else:
        matches.sort(key=lambda row: (int(row["views"]), row["posted_utc"]), reverse=True)
    selected = []
    authors = set()
    for row in matches:
        if row["handle"].casefold() in authors:
            continue
        selected.append(row)
        authors.add(row["handle"].casefold())
        if len(selected) >= limit:
            break
    return selected


def positive_integer(value: str) -> int:
    try:
        result = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("Expected a positive integer.") from error
    if result < 1:
        raise argparse.ArgumentTypeError("Expected a positive integer.")
    return result


def iso_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("Expected a date in YYYY-MM-DD form.") from error


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", help="Exact topic, ignoring case; see --list-topics")
    parser.add_argument("--levels", nargs="+", choices=LEVELS, default=["L3", "L4"])
    parser.add_argument("--small-accounts", action="store_true", help="Under 10k followers at scan")
    parser.add_argument("--query", default="", help="Literal substring in the title or preview")
    parser.add_argument("--since", type=iso_date, help="Earliest posting date, YYYY-MM-DD")
    parser.add_argument("--sort", choices=("views", "recent"), default="views")
    parser.add_argument("--limit", type=positive_integer, default=6, help="Maximum rows; one per author")
    parser.add_argument("--list-topics", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        rows = load_rows()
    except (OSError, UnicodeError, ValueError, csv.Error) as error:
        parser.error(f"Cannot read the bundled dataset: {error}")
    topics = Counter(row["topic"] for row in rows)
    if args.list_topics:
        if args.json:
            print(json.dumps(dict(sorted(topics.items())), ensure_ascii=False, indent=2))
        else:
            for topic, count in sorted(topics.items()):
                print(f"{topic}: {count:,}")
        return
    if args.topic and args.topic.casefold() not in {topic.casefold() for topic in topics}:
        parser.error("Unknown topic. Available: " + ", ".join(sorted(topics)))
    try:
        examples = select_examples(
            rows, topic=args.topic, levels=tuple(args.levels),
            small_accounts=args.small_accounts, query=args.query, since=args.since,
            sort=args.sort, limit=args.limit,
        )
    except ValueError as error:
        parser.error(f"Invalid dataset value: {error}")
    note = (
        "Winner-only X sample, Jan 1-Sep 26, 2026. Counts and followers are at scan; "
        "levels are source tags, not quality scores. One example per author."
    )
    if args.json:
        print(json.dumps({"dataset_note": note, "examples": examples}, ensure_ascii=False, indent=2))
        return
    print(note)
    if not examples:
        print("No rows matched. Try more levels, remove a filter, or use a related topic.")
    for row in examples:
        print(f'\n{row["title"]}')
        print(f'  {int(row["views"]):,} views; {row["topic"]}; {row["level"]}; '
              f'{int(row["followers_at_scan"]):,} followers at scan; {row["posted_utc"]} UTC')
        print("  Moves: " + (row["moves"] or "none"))
        print("  Failure marks: " + (row["failure_marks"] or "none"))
        print("  Preview: " + row["preview"])
        print("  " + row["article_url"])


if __name__ == "__main__":
    main()
