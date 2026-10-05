"""Tests for the unit-price comparer."""

from decimal import Decimal
import unittest

from unit_price import Item, format_results, parse_item, rank_items


class UnitPriceTests(unittest.TestCase):
    def test_parse_item_supports_a_quoted_comma_in_the_name(self) -> None:
        item = parse_item('"Cereal, family size",6.49,24')

        self.assertEqual(item.name, "Cereal, family size")
        self.assertEqual(item.price, Decimal("6.49"))
        self.assertEqual(item.quantity, Decimal("24"))

    def test_parse_item_rejects_invalid_values(self) -> None:
        invalid_items = (
            "Missing fields,2.00",
            "Bad price,nope,10",
            "Zero price,0,10",
            "Zero quantity,2.00,0",
            "Infinite price,Infinity,10",
        )

        for value in invalid_items:
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_item(value)

    def test_rank_items_orders_by_unit_price(self) -> None:
        small = Item("Small", Decimal("3.99"), Decimal("12"))
        large = Item("Large", Decimal("6.49"), Decimal("24"))

        self.assertEqual(rank_items([small, large]), [large, small])

    def test_rank_items_requires_two_choices(self) -> None:
        item = Item("Only choice", Decimal("1.00"), Decimal("1"))

        with self.assertRaisesRegex(ValueError, "at least two"):
            rank_items([item])

    def test_format_results_names_the_best_value(self) -> None:
        items = [
            Item("Small", Decimal("3.99"), Decimal("12")),
            Item("Large", Decimal("6.49"), Decimal("24")),
        ]

        output = format_results(items)

        self.assertIn("Large | $6.49 | 24 | $0.2704", output)
        self.assertTrue(output.endswith("Best value: Large"))


if __name__ == "__main__":
    unittest.main()
