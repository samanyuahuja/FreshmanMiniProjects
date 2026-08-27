import unittest

from signal_explainer import explain_signal


class SignalExplainerTests(unittest.TestCase):
    def test_detects_bullish_crossover(self) -> None:
        summary = explain_signal([5, 4, 3, 6], 2, 3)

        self.assertEqual(summary.signal, "bullish crossover")
        self.assertEqual(summary.relationship, "above")

    def test_detects_bearish_crossover(self) -> None:
        summary = explain_signal([3, 4, 5, 2], 2, 3)

        self.assertEqual(summary.signal, "bearish crossover")
        self.assertEqual(summary.relationship, "below")

    def test_reports_when_short_average_stays_above(self) -> None:
        summary = explain_signal([1, 2, 3, 4, 5], 2, 3)

        self.assertEqual(summary.signal, "short average remains above long average")
        self.assertAlmostEqual(summary.short_average, 4.5)
        self.assertAlmostEqual(summary.long_average, 4.0)

    def test_rejects_invalid_windows_prices_and_history(self) -> None:
        invalid_cases = (
            ([1, 2, 3], 3, 2),
            ([1, 2, 3], 1, 3),
            ([1, float("inf"), 3, 4], 2, 3),
            ([1, -2, 3, 4], 2, 3),
        )
        for prices, short_window, long_window in invalid_cases:
            with self.subTest(
                prices=prices, short=short_window, long=long_window
            ):
                with self.assertRaises(ValueError):
                    explain_signal(prices, short_window, long_window)


if __name__ == "__main__":
    unittest.main()
