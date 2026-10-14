"""Tests for file extension summaries."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from extension_summary import NO_EXTENSION, summarize_extensions


class ExtensionSummaryTests(unittest.TestCase):
    def test_counts_extensions_case_insensitively(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "notes.TXT").touch()
            (root / "report.txt").touch()
            (root / "scores.csv").touch()

            self.assertEqual(
                summarize_extensions(root),
                {".csv": 1, ".txt": 2},
            )

    def test_counts_extensionless_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "LICENSE").touch()

            self.assertEqual(summarize_extensions(root), {NO_EXTENSION: 1})

    def test_recursive_mode_includes_nested_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            nested = root / "archive"
            nested.mkdir()
            (nested / "data.json").touch()

            self.assertEqual(summarize_extensions(root), {})
            self.assertEqual(
                summarize_extensions(root, recursive=True),
                {".json": 1},
            )

    def test_rejects_non_directory_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "notes.txt"
            file_path.touch()

            with self.assertRaises(NotADirectoryError):
                summarize_extensions(file_path)


if __name__ == "__main__":
    unittest.main()
