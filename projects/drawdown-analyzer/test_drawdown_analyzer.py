"""Tests for drawdown analysis."""

import math
import unittest

from drawdown_analyzer import DrawdownResult, analyze_drawdown


class DrawdownAnalyzerTests(unittest.TestCase):
    def test_finds_largest_drawdown_and_recovery(self) -> None:
        result = analyze_drawdown([100, 120, 90, 105, 125])

        self.assertEqual(
            result,
            DrawdownResult(
                max_drawdown=0.25,
                peak_index=1,
                trough_index=2,
                recovery_index=4,
            ),
        )

    def test_marks_unrecovered_drawdown(self) -> None:
        result = analyze_drawdown([100, 80, 90])

        self.assertAlmostEqual(result.max_drawdown, 0.20)
        self.assertIsNone(result.recovery_index)

    def test_reports_zero_drawdown_for_rising_values(self) -> None:
        result = analyze_drawdown([50, 60, 60, 70])

        self.assertEqual(result, DrawdownResult(0.0, 0, 0, 0))

    def test_accepts_a_generator(self) -> None:
        result = analyze_drawdown(value for value in [10, 8, 10])

        self.assertAlmostEqual(result.max_drawdown, 0.20)
        self.assertEqual(result.recovery_index, 2)

    def test_rejects_invalid_values(self) -> None:
        with self.assertRaises(ValueError):
            analyze_drawdown([])
        with self.assertRaises(ValueError):
            analyze_drawdown([100, 0])
        with self.assertRaises(ValueError):
            analyze_drawdown([100, math.inf])
        with self.assertRaises(TypeError):
            analyze_drawdown([100, True])


if __name__ == "__main__":
    unittest.main()
