"""Calculate the average cost of shares bought at different prices."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable


@dataclass(frozen=True)
class AverageCostResult:
    total_shares: float
    total_cost: float
    average_cost: float


def calculate_average_cost(
    purchases: Iterable[tuple[float, float]],
) -> AverageCostResult:
    """Return total shares, total cost, and weighted average share cost."""
    purchase_list = list(purchases)
    if not purchase_list:
        raise ValueError("at least one purchase is required")

    total_shares = 0.0
    total_cost = 0.0

    for price, shares in purchase_list:
        for label, value in (("price", price), ("shares", shares)):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"{label} must be a number")
            if not isfinite(value) or value <= 0:
                raise ValueError(f"{label} must be finite and greater than zero")

        total_shares += shares
        total_cost += price * shares

    if not isfinite(total_cost):
        raise ValueError("total cost is too large")

    return AverageCostResult(
        total_shares=total_shares,
        total_cost=total_cost,
        average_cost=total_cost / total_shares,
    )
