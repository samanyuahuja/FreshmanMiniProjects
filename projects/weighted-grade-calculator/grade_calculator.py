"""Calculate a course grade from weighted category scores."""

from collections.abc import Iterable


GradeItem = tuple[float, float]


def calculate_weighted_grade(items: Iterable[GradeItem]) -> float:
    """Return the weighted percentage for ``(score, weight)`` pairs."""
    grade_items = list(items)
    if not grade_items:
        raise ValueError("at least one grade item is required")

    total_weight = 0.0
    weighted_total = 0.0

    for score, weight in grade_items:
        if not 0 <= score <= 100:
            raise ValueError("scores must be between 0 and 100")
        if weight <= 0:
            raise ValueError("weights must be greater than zero")

        total_weight += weight
        weighted_total += score * weight

    if abs(total_weight - 100) > 0.01:
        raise ValueError("weights must add up to 100")

    return weighted_total / total_weight


def letter_grade(percentage: float) -> str:
    """Convert a percentage into a basic A-F letter grade."""
    if not 0 <= percentage <= 100:
        raise ValueError("percentage must be between 0 and 100")

    for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if percentage >= cutoff:
            return letter
    return "F"
