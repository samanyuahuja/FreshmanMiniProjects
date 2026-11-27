"""Tests for the average share-cost calculator."""

import math
import unittest

from average_cost import calculate_average_cost


class AverageCostTests(unittest.TestCase):
    def test_calculates_weighted_average_cost(self) -> None:
        result = calculate_average_cost([(20, 2), (30, 3)])

        self.assertEqual(result.total_shares, 5)
        self.assertEqual(result.total_cost, 130)
        self.assertEqual(result.average_cost, 26)

    def test_supports_fractional_shares(self) -> None:
        result = calculate_average_cost([(10, 0.5), (20, 0.5)])

        self.assertEqual(result.average_cost, 15)

    def test_requires_at_least_one_purchase(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one"):
            calculate_average_cost([])

    def test_rejects_invalid_purchase_values(self) -> None:
        invalid_purchases = [
            [(0, 1)],
            [(10, -1)],
            [(math.inf, 1)],
            [(10, True)],
        ]

        for purchases in invalid_purchases:
            with self.subTest(purchases=purchases):
                with self.assertRaises(ValueError):
                    calculate_average_cost(purchases)

    def test_rejects_overflowed_total_cost(self) -> None:
        with self.assertRaisesRegex(ValueError, "too large"):
            calculate_average_cost([(1e308, 10)])


if __name__ == "__main__":
    unittest.main()
