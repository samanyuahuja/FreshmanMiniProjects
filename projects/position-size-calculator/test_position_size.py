import unittest
from decimal import Decimal

from position_size import calculate_position_size


class PositionSizeTests(unittest.TestCase):
    def test_calculates_whole_share_limit(self) -> None:
        result = calculate_position_size(
            Decimal("10000"),
            Decimal("1"),
            Decimal("50"),
            Decimal("48"),
        )

        self.assertEqual(result.shares, 50)
        self.assertEqual(result.risk_budget, Decimal("100"))
        self.assertEqual(result.position_value, Decimal("2500"))

    def test_supports_stop_above_entry(self) -> None:
        result = calculate_position_size(
            Decimal("5000"),
            Decimal("2"),
            Decimal("25"),
            Decimal("27.5"),
        )

        self.assertEqual(result.shares, 40)
        self.assertEqual(result.risk_per_share, Decimal("2.5"))

    def test_rejects_equal_entry_and_stop(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be different"):
            calculate_position_size(
                Decimal("1000"),
                Decimal("1"),
                Decimal("10"),
                Decimal("10"),
            )

    def test_rejects_out_of_range_risk(self) -> None:
        with self.assertRaisesRegex(ValueError, "between 0 and 100"):
            calculate_position_size(
                Decimal("1000"),
                Decimal("100"),
                Decimal("10"),
                Decimal("9"),
            )


if __name__ == "__main__":
    unittest.main()
