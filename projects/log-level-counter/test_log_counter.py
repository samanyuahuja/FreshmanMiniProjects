import unittest

from log_counter import count_log_levels
from main import format_counts


class LogCounterTests(unittest.TestCase):
    def test_counts_bracketed_and_plain_levels(self) -> None:
        result = count_log_levels(
            ["INFO server started", "[error] request failed", "DEBUG cache hit"]
        )

        self.assertEqual(result.levels["INFO"], 1)
        self.assertEqual(result.levels["ERROR"], 1)
        self.assertEqual(result.levels["DEBUG"], 1)
        self.assertEqual(result.total, 3)

    def test_counts_only_first_level_in_each_line(self) -> None:
        result = count_log_levels(["WARNING retry after ERROR response"])

        self.assertEqual(result.levels["WARNING"], 1)
        self.assertEqual(result.levels["ERROR"], 0)

    def test_tracks_lines_without_a_level(self) -> None:
        result = count_log_levels(["plain message", "", "CRITICAL outage"])

        self.assertEqual(result.unmatched, 2)
        self.assertEqual(result.total, 3)

    def test_formats_counts_in_a_stable_order(self) -> None:
        result = count_log_levels(["INFO ready", "unknown"])

        self.assertEqual(
            format_counts(result),
            "DEBUG: 0\n"
            "INFO: 1\n"
            "WARNING: 0\n"
            "ERROR: 0\n"
            "CRITICAL: 0\n"
            "UNMATCHED: 1\n"
            "TOTAL: 2",
        )


if __name__ == "__main__":
    unittest.main()
