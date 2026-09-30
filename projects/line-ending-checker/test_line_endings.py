"""Tests for line-ending inspection."""

import tempfile
import unittest
from pathlib import Path

from line_endings import LineEndingSummary, inspect_bytes, inspect_file


class LineEndingTests(unittest.TestCase):
    def test_counts_lf_endings(self) -> None:
        self.assertEqual(
            inspect_bytes(b"first\nsecond\n"),
            LineEndingSummary(crlf=0, lf=2, cr=0),
        )

    def test_does_not_double_count_crlf(self) -> None:
        self.assertEqual(
            inspect_bytes(b"first\r\nsecond\r\n"),
            LineEndingSummary(crlf=2, lf=0, cr=0),
        )

    def test_reports_mixed_endings(self) -> None:
        summary = inspect_bytes(b"first\r\nsecond\nthird\r")

        self.assertEqual(summary, LineEndingSummary(crlf=1, lf=1, cr=1))
        self.assertEqual(summary.style, "mixed")

    def test_reports_no_endings_for_one_line(self) -> None:
        self.assertEqual(inspect_bytes(b"one line").style, "none")

    def test_reads_binary_data_from_a_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_bytes(b"first\r\nsecond\r\n")

            self.assertEqual(inspect_file(path).style, "CRLF")


if __name__ == "__main__":
    unittest.main()
