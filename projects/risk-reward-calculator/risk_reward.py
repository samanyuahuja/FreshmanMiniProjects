"""Risk and reward calculations for one planned trade."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class RiskRewardResult:
    direction: str
    risk_per_unit: float
    reward_per_unit: float
    reward_risk_ratio: float
    break_even_win_rate_percent: float


def analyze_trade(entry: float, stop: float, target: float) -> RiskRewardResult:
    """Calculate the payoff ratio and break-even win rate for one setup."""
    prices = {"entry": entry, "stop": stop, "target": target}
    for label, value in prices.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{label} price must be a number")
        if not isfinite(value) or value <= 0:
            raise ValueError(f"{label} price must be finite and greater than zero")

    if stop < entry < target:
        direction = "long"
    elif target < entry < stop:
        direction = "short"
    else:
        raise ValueError(
            "prices must describe a long trade (stop < entry < target) "
            "or a short trade (target < entry < stop)"
        )

    risk = abs(entry - stop)
    reward = abs(target - entry)
    ratio = reward / risk
    break_even_rate = risk / (risk + reward) * 100

    return RiskRewardResult(
        direction=direction,
        risk_per_unit=risk,
        reward_per_unit=reward,
        reward_risk_ratio=ratio,
        break_even_win_rate_percent=break_even_rate,
    )
