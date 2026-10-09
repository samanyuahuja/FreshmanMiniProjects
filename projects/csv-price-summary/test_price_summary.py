"""Tests for the CSV price-summary tool."""

from decimal import Decimal
from pathlib import Path
import tempfile
import unittest

from price_summary import format_summary, load_prices, summarize_prices


class PriceSummaryTests(unittest.TestCase):
    def write_csv(self, content: str) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "prices.csv"
        path.write_text(content, encoding="utf-8")
        return path

    def test_summarizes_price_range_and_daily_returns(self) -> None:
        path = self.write_csv(
            "date,close\n"
            "2026-01-02,100\n"
            "2026-01-05,110\n"
            "2026-01-06,99\n"
        )

        summary = summarize_prices(load_prices(path))

        self.assertEqual(summary.total_return, Decimal("-0.01"))
        self.assertEqual(summary.highest.close, Decimal("110"))
        self.assertEqual(summary.lowest.close, Decimal("99"))
        self.assertEqual(summary.best_return, Decimal("0.1"))
        self.assertEqual(summary.worst_return, Decimal("-0.1"))
        self.assertIn("Total return: -1.00%", format_summary(summary))

    def test_accepts_extra_csv_columns(self) -> None:
        path = self.write_csv(
            "date,symbol,close\n"
            "2026-01-02,TEST,10.50\n"
            "2026-01-05,TEST,10.75\n"
        )

        points = load_prices(path)

        self.assertEqual(
            [point.close for point in points],
            [Decimal("10.50"), Decimal("10.75")],
        )

    def test_rejects_missing_required_columns(self) -> None:
        path = self.write_csv("day,price\n2026-01-02,100\n")

        with self.assertRaisesRegex(ValueError, "date and close columns"):
            load_prices(path)

    def test_rejects_unordered_or_duplicate_dates(self) -> None:
        path = self.write_csv(
            "date,close\n"
            "2026-01-05,100\n"
            "2026-01-05,101\n"
        )

        with self.assertRaisesRegex(ValueError, "unique and ordered"):
            load_prices(path)

    def test_rejects_nonpositive_and_nonfinite_prices(self) -> None:
        for invalid_price in ("0", "-2", "Infinity", "not-a-number"):
            with self.subTest(invalid_price=invalid_price):
                path = self.write_csv(
                    "date,close\n"
                    f"2026-01-02,{invalid_price}\n"
                    "2026-01-05,101\n"
                )
                with self.assertRaisesRegex(ValueError, "close price"):
                    load_prices(path)


if __name__ == "__main__":
    unittest.main()
