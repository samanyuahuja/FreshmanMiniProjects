"""Summarize study time recorded as subject and minute pairs."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class StudySummary:
    minutes_by_subject: dict[str, int]

    @property
    def total_minutes(self) -> int:
        return sum(self.minutes_by_subject.values())

    @property
    def top_subject(self) -> str | None:
        if not self.minutes_by_subject:
            return None
        return max(self.minutes_by_subject, key=self.minutes_by_subject.get)


def summarize_sessions(rows: Iterable[tuple[str, int]]) -> StudySummary:
    """Combine valid study sessions by normalized subject name."""
    totals: dict[str, int] = {}
    for subject, minutes in rows:
        normalized_subject = " ".join(subject.split())
        if not normalized_subject:
            raise ValueError("Subject cannot be empty.")
        if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes <= 0:
            raise ValueError("Minutes must be a positive integer.")
        totals[normalized_subject] = totals.get(normalized_subject, 0) + minutes
    return StudySummary(totals)
