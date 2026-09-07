"""Tests for study session summaries and command input."""

import argparse
import unittest

from main import parse_session
from summarizer import summarize_sessions


class StudySummaryTests(unittest.TestCase):
    def test_combines_repeated_subjects(self) -> None:
        summary = summarize_sessions(
            [("Calculus", 40), ("CS 124", 25), ("Calculus", 20)]
        )

        self.assertEqual(summary.total_minutes, 85)
        self.assertEqual(summary.minutes_by_subject["Calculus"], 60)
        self.assertEqual(summary.top_subject, "Calculus")

    def test_normalizes_subject_spacing(self) -> None:
        summary = summarize_sessions([("  Linear   Algebra ", 30)])

        self.assertEqual(summary.minutes_by_subject, {"Linear Algebra": 30})

    def test_empty_summary_has_no_top_subject(self) -> None:
        summary = summarize_sessions([])

        self.assertEqual(summary.total_minutes, 0)
        self.assertIsNone(summary.top_subject)

    def test_rejects_invalid_session_values(self) -> None:
        for row in [("", 20), ("Math", 0), ("Math", True)]:
            with self.subTest(row=row):
                with self.assertRaises(ValueError):
                    summarize_sessions([row])

    def test_parses_subject_with_equals_sign(self) -> None:
        self.assertEqual(parse_session("Math = review=15"), ("Math = review", 15))

    def test_rejects_non_integer_command_minutes(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_session("Calculus=half-hour")


if __name__ == "__main__":
    unittest.main()
