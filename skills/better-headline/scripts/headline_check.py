#!/usr/bin/env python3
"""Report X headline patterns, not quality scores or reach predictions."""

import argparse
import json
import re
from decimal import Decimal
from pathlib import Path
from typing import Optional


TOOLS = (
    "claude", "grok", "hermes", "openclaw", "clawdbot", "clawd", "kimi",
    "codex", "cursor",
)
RECEIPT_VERBS = (
    "built", "made", "spent", "tested", "analyzed", "fed", "ran", "tracked",
    "gave", "turned", "replaced", "bought", "sold", "studied", "read",
    "surveyed", "mapped", "reverse-engineered", "hacked", "installed", "asked",
    "set up", "stopped", "quit", "got", "wasted", "cut", "saved", "told",
    "let", "pointed", "benchmarked",
)
COMPLETENESS = (
    "full", "complete", "step", "exact", "ultimate", "builder", "quant",
    "roadmap", "resources", "blueprint", "playbook", "tutorial", "setup",
    "walkthrough",
)


def alternatives(words: tuple[str, ...]) -> str:
    return "|".join(re.escape(word) for word in words)


FAMILIES = (
    ("how to / guide", re.compile(r"\bhow\s+to\b|\bguide\b", re.I)),
    ("named tool", re.compile(r"\b(?:" + alternatives(TOOLS) + r")\b", re.I)),
    ("clock", re.compile(
        r"\bin\s+(?:\d+|one|a|an)\s*"
        r"(?:minute|min|hour|day|week|month|year|weekend|afternoon|evening|sitting|night)s?\b",
        re.I,
    )),
    ("receipt", re.compile(
        r"^\W*i\s+(?:" + alternatives(RECEIPT_VERBS) + r"|mass-\w+)\b",
        re.I,
    )),
    ("introducing", re.compile(r"^\W*(?:introducing|announcing|launching|meet)\b", re.I)),
    ("completeness tag", re.compile(
        r"(?:\((?:" + alternatives(COMPLETENESS) + r")\b[^()]*\)"
        r"|\[(?:" + alternatives(COMPLETENESS) + r")\b[^\[\]]*\])\s*\.?$",
        re.I,
    )),
)
AMOUNT = re.compile(
    r"\$(?P<amount>(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?)"
    r"(?:\s*(?P<scale>billion|million|thousand|bn|k|m|b))?(?!\w|[,.]\d)",
    re.I,
)


def round_dollar_match(headline: str) -> Optional[str]:
    for match in AMOUNT.finditer(headline):
        amount = Decimal(match.group("amount").replace(",", ""))
        if match.group("scale") or (amount >= 1000 and amount % 1000 == 0):
            return match.group(0)
    return None


def analyze(headline: str, names: tuple[str, ...] = ()) -> dict[str, object]:
    headline = headline.strip()
    moves = {}
    for family, pattern in FAMILIES:
        match = pattern.search(headline)
        if match:
            moves[family] = match.group(0)
    dollar = round_dollar_match(headline)
    if dollar:
        moves["round dollar"] = dollar

    marks = []
    if "?" in headline:
        marks.append("question mark")
    opener = re.match(r"^\W*(why|from)\b", headline, re.I)
    if opener:
        marks.append("opens with " + opener.group(1).lower())
    elif re.search(r"\bwhy\b", headline, re.I):
        marks.append("why anywhere")
    if re.search(r":\s", headline):
        marks.append("label colon")
    if re.search(r"\brecap\b", headline, re.I):
        marks.append("recap")
    if re.search(r"\bweekly\b", headline, re.I):
        marks.append("weekly")

    count = len(moves)
    if count == 0:
        level = "L0" if marks else "L1"
    else:
        level = "L2" if count == 1 else "L3" if count == 2 else "L4"
    relevant_names = [
        name for name in dict.fromkeys(names)
        if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", headline, re.I)
    ]
    return {
        "headline": headline,
        "level": level,
        "move_count": count,
        "moves": moves,
        "failure_marks": marks,
        "relevant_names": relevant_names,
        "words": len(headline.split()),
        "characters": len(headline),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("headlines", nargs="*", help="Headlines, each as a quoted argument")
    parser.add_argument("--file", type=Path, help="UTF-8 file with one headline per line; '-' reads stdin")
    parser.add_argument("--names", default="", help="Comma-separated relevant names; do not change L0-L4")
    parser.add_argument("--json", action="store_true", help="Return structured pattern reports")
    args = parser.parse_args()
    if args.file and args.headlines:
        parser.error("Use headline arguments or --file, not both.")
    headlines = args.headlines
    if args.file:
        try:
            if str(args.file) == "-":
                import sys

                text = sys.stdin.read().lstrip("\ufeff")
            else:
                text = args.file.read_text(encoding="utf-8-sig")
            headlines = text.splitlines()
        except (OSError, UnicodeError) as error:
            parser.error(f"Cannot read candidates: {error}")
    headlines = [headline.strip() for headline in headlines if headline.strip()]
    if not headlines:
        parser.error("Provide at least one non-empty headline.")
    names = tuple(name.strip() for name in args.names.split(",") if name.strip())
    reports = [analyze(headline, names) for headline in headlines]
    if args.json:
        print(json.dumps({
            "method": "X Article wording patterns from the Jan-Sep 2026 source sample",
            "note": "Levels count patterns. Verify truth, value, and fit separately; no reach forecast.",
            "headlines": reports,
        }, ensure_ascii=False, indent=2))
        return
    for report in reports:
        print(report["headline"])
        print(f'  {report["level"]}: {report["move_count"]} move families; '
              f'{report["words"]} words; {report["characters"]} characters')
        moves = report["moves"]
        print("  Moves: " + ("; ".join(f"{key} [{value}]" for key, value in moves.items()) or "none"))
        print("  Failure marks: " + (", ".join(report["failure_marks"]) or "none"))
        if report["relevant_names"]:
            print("  Relevant names: " + ", ".join(report["relevant_names"]))
        print()
    print("Pattern counts only. Check truth, reader value, and content fit before choosing.")


if __name__ == "__main__":
    main()
