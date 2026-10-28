"""Tests for CSV column checks."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from column_checker import check_csv


class ColumnCheckerTests(unittest.TestCase):
    def check_text(self, text: str, required: list[str]):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text(text, encoding="utf-8")
            return check_csv(path, required)

    def test_valid_file_reports_columns_and_rows(self) -> None:
        result = self.check_text(
            "name,score\nAsha,91\nNoah,87\n",
            ["name", "score", "score"],
        )

        self.assertTrue(result.is_valid)
        self.assertEqual(result.columns, ("name", "score"))
        self.assertEqual(result.row_count, 2)

    def test_missing_and_duplicate_headers_are_reported(self) -> None:
        result = self.check_text(
            "name,name\nAsha,A. Shah\n",
            ["name", "score"],
        )

        self.assertFalse(result.is_valid)
        self.assertEqual(result.missing, ("score",))
        self.assertEqual(result.duplicates, ("name",))

    def test_malformed_row_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Row 2 has 1 values; expected 2"):
            self.check_text("name,score\nAsha\n", ["name"])

    def test_blank_required_column_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-empty required column"):
            self.check_text("name\nAsha\n", [" "])


if __name__ == "__main__":
    unittest.main()
