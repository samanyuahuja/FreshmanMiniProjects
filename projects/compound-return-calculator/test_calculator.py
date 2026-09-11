"""Tests for compound-return calculations."""

import unittest

from calculator import calculate_compound_return


class CompoundReturnTests(unittest.TestCase):
    def test_compounds_positive_return(self) -> None:
        result = calculate_compound_return(1_000, 5, 3)

        self.assertAlmostEqual(result.ending_value, 1_157.625)
        self.assertAlmostEqual(result.growth_amount, 157.625)
        self.assertAlmostEqual(result.total_return_percent, 15.7625)

    def test_zero_periods_preserve_starting_value(self) -> None:
        result = calculate_compound_return(750, 8, 0)

        self.assertEqual(result.ending_value, 750)
        self.assertEqual(result.total_return_percent, 0)

    def test_supports_negative_return_above_total_loss(self) -> None:
        result = calculate_compound_return(1_000, -10, 2)

        self.assertAlmostEqual(result.ending_value, 810)
        self.assertAlmostEqual(result.total_return_percent, -19)

    def test_rejects_invalid_initial_value_and_rate(self) -> None:
        for inputs in ((0, 5, 2), (1_000, -100, 2), (1_000, float("nan"), 2)):
            with self.subTest(inputs=inputs):
                with self.assertRaises(ValueError):
                    calculate_compound_return(*inputs)

    def test_rejects_invalid_period_counts(self) -> None:
        for periods in (-1, 1.5, True):
            with self.subTest(periods=periods):
                with self.assertRaisesRegex(ValueError, "non-negative integer"):
                    calculate_compound_return(1_000, 5, periods)


if __name__ == "__main__":
    unittest.main()
