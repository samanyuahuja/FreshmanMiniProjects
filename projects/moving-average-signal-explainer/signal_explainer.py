"""Explain the relationship between two simple moving averages."""

from dataclasses import dataclass
from math import isfinite
from numbers import Integral, Real


@dataclass(frozen=True)
class SignalSummary:
    short_average: float
    long_average: float
    relationship: str
    signal: str


def explain_signal(
    prices: list[float], short_window: int, long_window: int
) -> SignalSummary:
    """Compare current and previous moving averages for one price series."""
    if (
        isinstance(short_window, bool)
        or not isinstance(short_window, Integral)
        or isinstance(long_window, bool)
        or not isinstance(long_window, Integral)
        or short_window < 1
        or long_window <= short_window
    ):
        raise ValueError("windows must be positive integers with short below long")
    if len(prices) < long_window + 1:
        raise ValueError(f"at least {long_window + 1} prices are required")
    if any(
        isinstance(price, bool)
        or not isinstance(price, Real)
        or not isfinite(price)
        or price <= 0
        for price in prices
    ):
        raise ValueError("prices must be positive finite numbers")

    current_short = sum(prices[-short_window:]) / short_window
    current_long = sum(prices[-long_window:]) / long_window
    previous_short = sum(prices[-short_window - 1 : -1]) / short_window
    previous_long = sum(prices[-long_window - 1 : -1]) / long_window

    if previous_short <= previous_long and current_short > current_long:
        signal = "bullish crossover"
    elif previous_short >= previous_long and current_short < current_long:
        signal = "bearish crossover"
    elif current_short > current_long:
        signal = "short average remains above long average"
    elif current_short < current_long:
        signal = "short average remains below long average"
    else:
        signal = "moving averages are equal"

    relationship = "above" if current_short > current_long else "below"
    if current_short == current_long:
        relationship = "equal to"

    return SignalSummary(current_short, current_long, relationship, signal)
