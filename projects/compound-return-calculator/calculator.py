"""Calculate growth from a fixed compound return."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from numbers import Integral, Real


@dataclass(frozen=True)
class CompoundResult:
    ending_value: float
    growth_amount: float
    total_return_percent: float


def calculate_compound_return(
    initial_value: float,
    rate_percent: float,
    periods: int,
) -> CompoundResult:
    """Return the ending value and growth for repeated percentage changes."""
    if isinstance(initial_value, bool) or not isinstance(initial_value, Real):
        raise ValueError("Initial value must be numeric.")
    if not isfinite(initial_value) or initial_value <= 0:
        raise ValueError("Initial value must be finite and positive.")
    if isinstance(rate_percent, bool) or not isinstance(rate_percent, Real):
        raise ValueError("Rate must be numeric.")
    if not isfinite(rate_percent) or rate_percent <= -100:
        raise ValueError("Rate must be finite and greater than -100 percent.")
    if isinstance(periods, bool) or not isinstance(periods, Integral) or periods < 0:
        raise ValueError("Periods must be a non-negative integer.")

    ending_value = float(initial_value) * (1 + float(rate_percent) / 100) ** int(periods)
    growth_amount = ending_value - float(initial_value)
    return CompoundResult(
        ending_value=ending_value,
        growth_amount=growth_amount,
        total_return_percent=growth_amount / float(initial_value) * 100,
    )
