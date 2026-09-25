"""Calculate the largest drawdown in a sequence of portfolio values."""

from dataclasses import dataclass
from math import isfinite
from numbers import Real
from typing import Iterable


@dataclass(frozen=True)
class DrawdownResult:
    """The size and location of a sequence's largest drawdown."""

    max_drawdown: float
    peak_index: int
    trough_index: int
    recovery_index: int | None


def analyze_drawdown(values: Iterable[float]) -> DrawdownResult:
    """Return the largest peak-to-trough decline in positive values."""
    series = list(values)
    if not series:
        raise ValueError("at least one value is required")

    for value in series:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("values must be real numbers")
        if not isfinite(value) or value <= 0:
            raise ValueError("values must be positive and finite")

    running_peak = series[0]
    running_peak_index = 0
    max_drawdown = 0.0
    peak_index = 0
    trough_index = 0

    for index, value in enumerate(series[1:], start=1):
        if value > running_peak:
            running_peak = value
            running_peak_index = index
            continue

        drawdown = (running_peak - value) / running_peak
        if drawdown > max_drawdown:
            max_drawdown = drawdown
            peak_index = running_peak_index
            trough_index = index

    recovery_index = 0 if max_drawdown == 0 else None
    if max_drawdown > 0:
        peak_value = series[peak_index]
        recovery_index = next(
            (
                index
                for index in range(trough_index + 1, len(series))
                if series[index] >= peak_value
            ),
            None,
        )

    return DrawdownResult(
        max_drawdown=max_drawdown,
        peak_index=peak_index,
        trough_index=trough_index,
        recovery_index=recovery_index,
    )
