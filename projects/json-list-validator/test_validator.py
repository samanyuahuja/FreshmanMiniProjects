"""Tests for JSON record validation."""

import unittest

from validator import validate_records


class ValidateRecordsTests(unittest.TestCase):
    def test_accepts_records_with_required_fields(self) -> None:
        records = [{"name": "Ava", "score": 91}, {"name": "Noah", "score": 84}]

        self.assertEqual(validate_records(records, ["name", "score"]), [])

    def test_rejects_non_list_root(self) -> None:
        self.assertEqual(
            validate_records({"name": "Ava"}, ["name"]),
            ["Root value must be a list."],
        )

    def test_reports_non_object_items(self) -> None:
        self.assertEqual(
            validate_records([{"name": "Ava"}, "Noah"], ["name"]),
            ["Item 1 must be an object."],
        )

    def test_reports_missing_fields_in_requested_order(self) -> None:
        self.assertEqual(
            validate_records([{"name": "Ava"}], ["score", "section"]),
            ["Item 0 is missing: score, section."],
        )

    def test_rejects_empty_required_field_names(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            validate_records([], ["name", " "])


if __name__ == "__main__":
    unittest.main()
