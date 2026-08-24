"""Command-line interface for the expense splitter."""

import argparse
from decimal import Decimal

from expense_splitter import parse_money, split_expense


def non_negative_decimal(value: str) -> Decimal:
    """Parse a non-negative decimal value for an argument."""
    try:
        return parse_money(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def positive_integer(value: str) -> int:
    """Parse a whole number greater than zero."""
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("people must be a whole number") from exc
    if number < 1:
        raise argparse.ArgumentTypeError("people must be at least 1")
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Split an expense evenly while keeping the total exact."
    )
    parser.add_argument("subtotal", type=non_negative_decimal)
    parser.add_argument("people", type=positive_integer)
    parser.add_argument("--tip", type=non_negative_decimal, default=Decimal("0"))
    return parser


def main() -> None:
    args = build_parser().parse_args()
    shares = split_expense(args.subtotal, args.people, args.tip)

    for number, share in enumerate(shares, start=1):
        print(f"Person {number}: ${share:.2f}")
    print(f"Total: ${sum(shares):.2f}")


if __name__ == "__main__":
    main()
