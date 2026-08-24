import unittest
from decimal import Decimal

from expense_splitter import parse_money, split_expense


class ExpenseSplitterTests(unittest.TestCase):
    def test_distributes_leftover_cents_without_changing_total(self) -> None:
        shares = split_expense(Decimal("10.00"), 3)

        self.assertEqual(
            shares, [Decimal("3.34"), Decimal("3.33"), Decimal("3.33")]
        )
        self.assertEqual(sum(shares), Decimal("10.00"))

    def test_applies_tip_before_splitting(self) -> None:
        shares = split_expense(Decimal("25.00"), 2, Decimal("20"))

        self.assertEqual(shares, [Decimal("15.00"), Decimal("15.00")])

    def test_rounds_entered_money_to_nearest_cent(self) -> None:
        self.assertEqual(parse_money("12.345"), Decimal("12.35"))

    def test_rejects_invalid_inputs(self) -> None:
        for value in ("not-a-number", "-1", "Infinity"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_money(value)

        with self.assertRaises(ValueError):
            split_expense(Decimal("10"), 0)


if __name__ == "__main__":
    unittest.main()
