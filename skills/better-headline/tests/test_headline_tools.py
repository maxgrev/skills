"""Behavior checks for the deterministic helpers; run with unittest discovery."""

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
from find_examples import load_rows, select_examples
from headline_check import analyze


class HeadlineCheckTests(unittest.TestCase):
    def test_level_ladder(self):
        cases = (
            ("Content marketing: What to publish", "L0"),
            ("Your content plan for the month", "L1"),
            ("How to plan your content", "L2"),
            ("How to plan your content with Claude", "L3"),
            ("How to plan your content with Claude in 1 hour", "L4"),
        )
        for headline, level in cases:
            with self.subTest(headline=headline):
                self.assertEqual(analyze(headline)["level"], level)

    def test_families_count_once(self):
        report = analyze("How to use Claude and Cursor (full guide)")
        self.assertEqual(report["move_count"], 3)
        self.assertEqual(set(report["moves"]), {"how to / guide", "named tool", "completeness tag"})

    def test_high_level_can_carry_marks(self):
        report = analyze("How to use Claude in 1 hour: Why this works?")
        self.assertEqual(report["level"], "L4")
        self.assertEqual(set(report["failure_marks"]), {"label colon", "why anywhere", "question mark"})

    def test_substrings_do_not_create_moves(self):
        report = analyze("A claudesque guidebook (fuller account)")
        self.assertEqual(report["move_count"], 0)
        self.assertEqual(report["level"], "L1")
        self.assertEqual(analyze("How top labs use a clawdhub skill")["move_count"], 0)

    def test_completeness_tags(self):
        for suffix in ("(full guide)", "[Full walkthrough].", "(step-by-step)"):
            with self.subTest(suffix=suffix):
                self.assertIn("completeness tag", analyze("Your setup " + suffix)["moves"])
        self.assertNotIn("completeness tag", analyze("Your setup (full guide) explained")["moves"])

    def test_recorded_receipt_and_clock_forms(self):
        for headline in ("I built it in one weekend", "I set up the system in 30 minutes", "I mass-built sites in an afternoon"):
            with self.subTest(headline=headline):
                self.assertEqual(set(analyze(headline)["moves"]), {"receipt", "clock"})
        for headline in ("We built it", "I launched it", "I build it", "I analyst says"):
            with self.subTest(headline=headline):
                self.assertNotIn("receipt", analyze(headline)["moves"])

    def test_dollar_forms_keep_exact_amounts_separate(self):
        for amount in ("$5,000", "$3M", "$7 million", "$15 Billion", "$10k/mo", "$375,000", "$1.5m"):
            with self.subTest(amount=amount):
                self.assertIn("round dollar", analyze("A result of " + amount)["moves"])
        for amount in ("$11,400", "$2,382,780", "$999", "$2,000.50", "$5,000,50"):
            with self.subTest(amount=amount):
                self.assertNotIn("round dollar", analyze("A result of " + amount)["moves"])

    def test_custom_names_do_not_change_research_level(self):
        report = analyze("How to plan posts with Notion", ("Notion", "Acme"))
        self.assertEqual(report["level"], "L2")
        self.assertEqual(report["relevant_names"], ["Notion"])
        self.assertEqual(analyze("Your Notional plan", ("Notion",))["relevant_names"], [])

    def test_marks_use_whole_words_and_whitespace(self):
        self.assertEqual(analyze("Why this works")["failure_marks"], ["opens with why"])
        self.assertEqual(analyze("From notes to posts")["failure_marks"], ["opens with from"])
        self.assertEqual(analyze("A weekly recap")["failure_marks"], ["recap", "weekly"])
        self.assertEqual(analyze("Weeklyish recapping at 12:30")["failure_marks"], [])

    def test_cli_file_input_is_json_and_preserves_order(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "candidates.txt"
            file.write_text("\ufeffA plain title\n\nHow to use Claude\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "headline_check.py"), "--file", str(file), "--json"],
                capture_output=True, text=True, check=True,
            )
        reports = json.loads(result.stdout)["headlines"]
        self.assertEqual([report["level"] for report in reports], ["L1", "L3"])

    def test_cli_rejects_missing_or_empty_candidates(self):
        for args in ([], [" "], ["--file", "/nonexistent/headline-candidates.txt"]):
            with self.subTest(args=args):
                result = subprocess.run(
                    [sys.executable, str(SCRIPTS / "headline_check.py"), *args],
                    capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)


class ExampleFinderTests(unittest.TestCase):
    @staticmethod
    def row(title, views, *, handle="a", topic="Marketing", level="L3", followers="900", posted="2026-09-20 10:00", english="yes"):
        return {
            "title": title, "views": str(views), "handle": handle, "topic": topic,
            "level": level, "followers_at_scan": followers, "posted_utc": posted,
            "english": english, "preview": "A useful template", "moves": "how to / guide",
            "failure_marks": "", "article_url": "https://example.com/article",
        }

    def test_topic_level_account_date_and_language_filters(self):
        rows = [
            self.row("A marketing result", 200_000),
            self.row("Older", 900_000, handle="b", posted="2026-08-01 10:00"),
            self.row("Big account", 900_000, handle="c", followers="10000"),
            self.row("Plain", 900_000, handle="d", level="L1"),
            self.row("Another topic", 900_000, handle="e", topic="AI"),
            self.row("Non-English", 900_000, handle="f", english="no"),
        ]
        selected = select_examples(rows, topic="marketing", small_accounts=True, since=date(2026, 9, 1))
        self.assertEqual([row["title"] for row in selected], ["A marketing result"])

    def test_sort_query_and_author_diversity(self):
        rows = [
            self.row("Low result", 100_000, handle="a", posted="2026-09-26 10:00"),
            self.row("High result", 900_000, handle="a", posted="2026-09-01 10:00"),
            self.row("Other result", 200_000, handle="b"),
        ]
        self.assertEqual([row["title"] for row in select_examples(rows, limit=2)], ["High result", "Other result"])
        self.assertEqual(select_examples(rows, sort="recent", limit=1)[0]["title"], "Low result")
        self.assertEqual(len(select_examples(rows, query="TEMPLATE")), 2)
        self.assertEqual(select_examples(rows, query="absent"), [])

    def test_bundled_sample_and_url_fields(self):
        rows = load_rows()
        self.assertEqual(len(rows), 6835)
        self.assertTrue(all(int(row["views"]) >= 100_000 for row in rows))
        selected = select_examples(rows, topic="Marketing", small_accounts=True)
        self.assertTrue(selected)
        self.assertTrue(all(row["article_url"].startswith("https://x.com/") for row in selected))

    def test_cli_returns_structured_examples(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "find_examples.py"), "--topic", "marketing", "--limit", "2", "--json"],
            capture_output=True, text=True, check=True,
        )
        examples = json.loads(result.stdout)["examples"]
        self.assertEqual(len(examples), 2)
        self.assertTrue(all(row["topic"] == "Marketing" for row in examples))

    def test_cli_rejects_bad_filters(self):
        for args in (["--limit", "0"], ["--topic", "not-a-topic"], ["--since", "not-a-date"]):
            with self.subTest(args=args):
                result = subprocess.run(
                    [sys.executable, str(SCRIPTS / "find_examples.py"), *args],
                    capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
