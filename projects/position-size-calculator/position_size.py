"""Position sizing calculations for a single trade."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PositionSize:
    shares: int
    risk_budget: Decimal
    risk_per_share: Decimal
    position_value: Decimal


def calculate_position_size(
    account_balance: Decimal,
    risk_percent: Decimal,
    entry_price: Decimal,
    stop_price: Decimal,
) -> PositionSize:
    """Return the largest whole-share position within the risk budget."""
    if account_balance <= 0:
        raise ValueError("account balance must be positive")
    if risk_percent <= 0 or risk_percent >= 100:
        raise ValueError("risk percent must be between 0 and 100")
    if entry_price <= 0 or stop_price <= 0:
        raise ValueError("entry and stop prices must be positive")

    risk_per_share = abs(entry_price - stop_price)
    if risk_per_share == 0:
        raise ValueError("entry and stop prices must be different")

    risk_budget = account_balance * risk_percent / Decimal("100")
    shares = int(risk_budget // risk_per_share)
    return PositionSize(
        shares=shares,
        risk_budget=risk_budget,
        risk_per_share=risk_per_share,
        position_value=entry_price * shares,
    )
