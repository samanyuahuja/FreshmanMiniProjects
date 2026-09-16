"""Tests for duplicate file detection."""

from pathlib import Path
import tempfile
import unittest

from duplicate_finder import file_digest, find_duplicates


class DuplicateFinderTests(unittest.TestCase):
    def test_groups_files_with_matching_contents(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            root = Path(temp_directory)
            (root / "copy-a.txt").write_text("same", encoding="utf-8")
            (root / "copy-b.txt").write_text("same", encoding="utf-8")
            (root / "other.txt").write_text("different", encoding="utf-8")

            groups = find_duplicates(root)

            self.assertEqual(groups, [[root / "copy-a.txt", root / "copy-b.txt"]])

    def test_checks_nested_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            root = Path(temp_directory)
            nested = root / "nested"
            nested.mkdir()
            (root / "first.csv").write_text("a,b\n1,2\n", encoding="utf-8")
            (nested / "second.csv").write_text("a,b\n1,2\n", encoding="utf-8")

            groups = find_duplicates(root)

            self.assertEqual(groups, [[root / "first.csv", nested / "second.csv"]])

    def test_same_size_different_files_are_not_grouped(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            root = Path(temp_directory)
            (root / "one.txt").write_text("abc", encoding="utf-8")
            (root / "two.txt").write_text("xyz", encoding="utf-8")

            self.assertEqual(find_duplicates(root), [])

    def test_rejects_missing_directory(self) -> None:
        with self.assertRaisesRegex(ValueError, "Not a directory"):
            find_duplicates(Path("missing-folder"))

    def test_digest_changes_with_file_contents(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            path = Path(temp_directory) / "sample.txt"
            path.write_text("first", encoding="utf-8")
            first_digest = file_digest(path)
            path.write_text("second", encoding="utf-8")

            self.assertNotEqual(file_digest(path), first_digest)


if __name__ == "__main__":
    unittest.main()
