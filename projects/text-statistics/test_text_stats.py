"""Tests for text statistics calculations."""

import unittest

from text_stats import TextStats, analyze_text


class AnalyzeTextTests(unittest.TestCase):
    def test_counts_multiline_text(self):
        self.assertEqual(
            analyze_text("Hello world.\nSecond line!"),
            TextStats(
                characters=25,
                characters_without_spaces=22,
                words=4,
                sentences=2,
                nonempty_lines=2,
            ),
        )

    def test_empty_text_has_zero_counts(self):
        self.assertEqual(
            analyze_text(""),
            TextStats(0, 0, 0, 0, 0),
        )

    def test_groups_repeated_sentence_punctuation(self):
        stats = analyze_text("Really?! Yes...")

        self.assertEqual(stats.words, 2)
        self.assertEqual(stats.sentences, 2)

    def test_counts_unicode_words_and_ignores_blank_lines(self):
        stats = analyze_text("Café isn't closed.\n  \nफिर मिलेंगे।")

        self.assertEqual(stats.words, 5)
        self.assertEqual(stats.nonempty_lines, 2)

    def test_rejects_non_string_input(self):
        with self.assertRaises(TypeError):
            analyze_text(123)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
