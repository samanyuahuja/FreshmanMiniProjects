import unittest

from fee_calculator import compare_fee, future_value


class FeeCalculatorTests(unittest.TestCase):
    def test_future_value_compounds_return(self) -> None:
        self.assertAlmostEqual(future_value(1_000, 0.10, 2), 1_210)

    def test_compare_fee_reports_growth_difference(self) -> None:
        without_fee, with_fee, fee_drag = compare_fee(10_000, 0.07, 0.01, 10)

        self.assertAlmostEqual(without_fee, 19_671.51, places=2)
        self.assertAlmostEqual(with_fee, 17_908.48, places=2)
        self.assertAlmostEqual(fee_drag, 1_763.04, places=2)

    def test_zero_years_has_no_fee_drag(self) -> None:
        self.assertEqual(compare_fee(500, 0.08, 0.02, 0), (500, 500, 0))

    def test_invalid_inputs_are_rejected(self) -> None:
        invalid_inputs = [
            (-1, 0.05, 0.01, 5),
            (1_000, -1.0, 0.01, 5),
            (1_000, 0.05, -0.01, 5),
            (1_000, 0.05, 0.01, -1),
        ]
        for values in invalid_inputs:
            with self.subTest(values=values), self.assertRaises(ValueError):
                compare_fee(*values)


if __name__ == "__main__":
    unittest.main()
