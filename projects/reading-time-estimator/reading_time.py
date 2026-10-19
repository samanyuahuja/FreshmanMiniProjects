"""Estimate how long a block of text will take to read."""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil


@dataclass(frozen=True)
class ReadingEstimate:
    """Word count and estimated reading duration."""

    word_count: int
    total_seconds: int

    @property
    def minutes(self) -> int:
        return self.total_seconds // 60

    @property
    def seconds(self) -> int:
        return self.total_seconds % 60


def estimate_reading_time(text: str, words_per_minute: int = 200) -> ReadingEstimate:
    """Return a reading estimate for non-empty text."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Text must contain at least one word.")
    if (
        isinstance(words_per_minute, bool)
        or not isinstance(words_per_minute, int)
        or not 50 <= words_per_minute <= 1_000
    ):
        raise ValueError("Reading speed must be an integer from 50 to 1000.")

    word_count = len(text.split())
    total_seconds = ceil(word_count * 60 / words_per_minute)
    return ReadingEstimate(word_count=word_count, total_seconds=total_seconds)


def format_estimate(estimate: ReadingEstimate) -> str:
    """Format an estimate as a short terminal summary."""
    duration = f"{estimate.minutes}m {estimate.seconds}s"
    return f"Words: {estimate.word_count}\nEstimated reading time: {duration}"
