"""Calculate simple statistics for a block of text."""

from dataclasses import dataclass
import re


WORD_PATTERN = re.compile(r"\b[\w']+\b", re.UNICODE)
SENTENCE_END_PATTERN = re.compile(r"[.!?]+")


@dataclass(frozen=True)
class TextStats:
    characters: int
    characters_without_spaces: int
    words: int
    sentences: int
    nonempty_lines: int


def analyze_text(text: str) -> TextStats:
    """Return counts for characters, words, sentences, and nonempty lines."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return TextStats(
        characters=len(text),
        characters_without_spaces=sum(
            not character.isspace() for character in text
        ),
        words=len(WORD_PATTERN.findall(text)),
        sentences=len(SENTENCE_END_PATTERN.findall(text)),
        nonempty_lines=sum(bool(line.strip()) for line in text.splitlines()),
    )
