"""Tests for weighted grade calculations."""

import unittest

from grade_calculator import calculate_weighted_grade, letter_grade


class WeightedGradeTests(unittest.TestCase):
    def test_calculates_weighted_percentage(self) -> None:
        result = calculate_weighted_grade([(92, 40), (81, 60)])
        self.assertAlmostEqual(result, 85.4)

    def test_accepts_weights_with_small_rounding_difference(self) -> None:
        result = calculate_weighted_grade([(100, 33.33), (80, 33.33), (60, 33.34)])
        self.assertAlmostEqual(result, 79.998)

    def test_rejects_score_outside_percentage_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "scores must be between 0 and 100"):
            calculate_weighted_grade([(101, 100)])

    def test_rejects_incomplete_weights(self) -> None:
        with self.assertRaisesRegex(ValueError, "weights must add up to 100"):
            calculate_weighted_grade([(90, 50), (80, 40)])

    def test_assigns_letter_grades_at_cutoffs(self) -> None:
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(80), "B")
        self.assertEqual(letter_grade(70), "C")
        self.assertEqual(letter_grade(60), "D")
        self.assertEqual(letter_grade(59.99), "F")


if __name__ == "__main__":
    unittest.main()
