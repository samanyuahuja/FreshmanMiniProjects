"""Calculate an even expense split without losing any cents."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


CENT = Decimal("0.01")


def parse_money(value: str) -> Decimal:
    """Convert a text amount to a non-negative value rounded to cents."""
    try:
        amount = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError("amount must be a number") from exc

    if not amount.is_finite() or amount < 0:
        raise ValueError("amount must be a non-negative finite number")
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def split_expense(
    subtotal: Decimal, people: int, tip_percent: Decimal = Decimal("0")
) -> list[Decimal]:
    """Return individual shares whose sum exactly matches the tipped total."""
    if subtotal < 0 or not subtotal.is_finite():
        raise ValueError("subtotal must be a non-negative finite number")
    if people < 1:
        raise ValueError("people must be at least 1")
    if tip_percent < 0 or not tip_percent.is_finite():
        raise ValueError("tip percent must be a non-negative finite number")

    total = (subtotal * (Decimal("1") + tip_percent / Decimal("100"))).quantize(
        CENT, rounding=ROUND_HALF_UP
    )
    total_cents = int(total * 100)
    base_cents, extra_cents = divmod(total_cents, people)

    return [
        Decimal(base_cents + (index < extra_cents)) / 100
        for index in range(people)
    ]
