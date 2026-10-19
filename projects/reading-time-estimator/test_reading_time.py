"""Tests for the reading-time estimator."""

from __future__ import annotations

import unittest

from reading_time import ReadingEstimate, estimate_reading_time, format_estimate


class ReadingTimeTests(unittest.TestCase):
    def test_estimates_one_minute_at_selected_speed(self) -> None:
        estimate = estimate_reading_time("word " * 200, words_per_minute=200)

        self.assertEqual(estimate, ReadingEstimate(word_count=200, total_seconds=60))

    def test_rounds_partial_seconds_up(self) -> None:
        estimate = estimate_reading_time("one two three", words_per_minute=200)

        self.assertEqual(estimate.total_seconds, 1)

    def test_counts_words_across_whitespace(self) -> None:
        estimate = estimate_reading_time("first\nsecond\tthird", words_per_minute=60)

        self.assertEqual(estimate.word_count, 3)
        self.assertEqual((estimate.minutes, estimate.seconds), (0, 3))

    def test_formats_terminal_summary(self) -> None:
        summary = format_estimate(ReadingEstimate(word_count=350, total_seconds=105))

        self.assertEqual(summary, "Words: 350\nEstimated reading time: 1m 45s")

    def test_rejects_empty_text_and_invalid_speeds(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one word"):
            estimate_reading_time("   ")

        for speed in (True, 49, 1_001, 200.5):
            with self.subTest(speed=speed):
                with self.assertRaisesRegex(ValueError, "integer from 50 to 1000"):
                    estimate_reading_time("hello", speed)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
