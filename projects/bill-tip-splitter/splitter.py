"""Calculate a restaurant bill split with a percentage tip."""

from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def split_bill(
    subtotal: Decimal,
    tip_percent: Decimal,
    people: int,
) -> dict[str, Decimal]:
    """Return the tip, total, and per-person amount."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    if tip_percent < 0:
        raise ValueError("Tip percentage cannot be negative.")
    if people < 1:
        raise ValueError("People must be at least 1.")

    tip = (subtotal * tip_percent / 100).quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )
    total = (subtotal + tip).quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )
    per_person = (total / people).quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )

    return {
        "tip": tip,
        "total": total,
        "per_person": per_person,
    }
