"""Tests for the risk-reward calculator."""

import math
import unittest

from risk_reward import analyze_trade


class RiskRewardTests(unittest.TestCase):
    def test_long_trade_calculation(self) -> None:
        result = analyze_trade(entry=100, stop=95, target=110)

        self.assertEqual(result.direction, "long")
        self.assertEqual(result.risk_per_unit, 5)
        self.assertEqual(result.reward_per_unit, 10)
        self.assertEqual(result.reward_risk_ratio, 2)
        self.assertAlmostEqual(result.break_even_win_rate_percent, 33.3333, places=3)

    def test_short_trade_calculation(self) -> None:
        result = analyze_trade(entry=50, stop=54, target=42)

        self.assertEqual(result.direction, "short")
        self.assertEqual(result.reward_risk_ratio, 2)

    def test_rejects_prices_in_the_wrong_order(self) -> None:
        with self.assertRaisesRegex(ValueError, "prices must describe"):
            analyze_trade(entry=100, stop=90, target=95)

    def test_rejects_non_finite_prices(self) -> None:
        with self.assertRaisesRegex(ValueError, "finite"):
            analyze_trade(entry=100, stop=95, target=math.inf)

    def test_rejects_non_positive_prices(self) -> None:
        with self.assertRaisesRegex(ValueError, "greater than zero"):
            analyze_trade(entry=0, stop=95, target=110)


if __name__ == "__main__":
    unittest.main()
