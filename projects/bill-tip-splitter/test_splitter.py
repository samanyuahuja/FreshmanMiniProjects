"""Tests for bill and tip calculations."""

import unittest
from decimal import Decimal

from splitter import split_bill


class SplitBillTests(unittest.TestCase):
    def test_splits_a_tipped_bill(self):
        result = split_bill(
            Decimal("48.50"),
            Decimal("18"),
            3,
        )

        self.assertEqual(result["tip"], Decimal("8.73"))
        self.assertEqual(result["total"], Decimal("57.23"))
        self.assertEqual(
            result["per_person"],
            Decimal("19.08"),
        )

    def test_rounds_half_up_to_cents(self):
        result = split_bill(
            Decimal("10.05"),
            Decimal("10"),
            2,
        )

        self.assertEqual(result["tip"], Decimal("1.01"))
        self.assertEqual(result["total"], Decimal("11.06"))
        self.assertEqual(
            result["per_person"],
            Decimal("5.53"),
        )

    def test_rejects_invalid_inputs(self):
        invalid_inputs = [
            (Decimal("-1"), Decimal("15"), 2),
            (Decimal("20"), Decimal("-1"), 2),
            (Decimal("20"), Decimal("15"), 0),
        ]

        for inputs in invalid_inputs:
            with self.subTest(inputs=inputs):
                with self.assertRaises(ValueError):
                    split_bill(*inputs)


if __name__ == "__main__":
    unittest.main()
