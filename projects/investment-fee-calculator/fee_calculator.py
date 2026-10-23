"""Compare investment growth with and without an annual fee."""


def future_value(principal: float, annual_return: float, years: int) -> float:
    """Return the compounded value of an investment."""
    if principal < 0:
        raise ValueError("principal cannot be negative")
    if annual_return <= -1:
        raise ValueError("annual return must be greater than -100%")
    if years < 0 or not isinstance(years, int):
        raise ValueError("years must be a non-negative integer")
    return principal * (1 + annual_return) ** years


def compare_fee(
    principal: float,
    annual_return: float,
    annual_fee: float,
    years: int,
) -> tuple[float, float, float]:
    """Return values without fees, after fees, and the difference."""
    if annual_fee < 0:
        raise ValueError("annual fee cannot be negative")
    if annual_return - annual_fee <= -1:
        raise ValueError("return after fees must be greater than -100%")

    without_fee = future_value(principal, annual_return, years)
    with_fee = future_value(principal, annual_return - annual_fee, years)
    return without_fee, with_fee, without_fee - with_fee
