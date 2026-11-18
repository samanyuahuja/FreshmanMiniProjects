"""Command-line interface for the bill and tip splitter."""

import argparse
from decimal import Decimal, InvalidOperation

from splitter import split_bill


def decimal_value(value: str) -> Decimal:
    try:
        number = Decimal(value)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError(
            f"{value!r} is not a valid number"
        ) from error

    if not number.is_finite():
        raise argparse.ArgumentTypeError(
            "numbers must be finite"
        )
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Split a bill after adding a percentage tip.",
    )
    parser.add_argument("subtotal", type=decimal_value)
    parser.add_argument("tip_percent", type=decimal_value)
    parser.add_argument("people", type=int)
    return parser


def main() -> None:
    args = build_parser().parse_args()

    try:
        result = split_bill(
            args.subtotal,
            args.tip_percent,
            args.people,
        )
    except ValueError as error:
        raise SystemExit(f"error: {error}") from error

    print(f"Tip: ${result['tip']:.2f}")
    print(f"Total: ${result['total']:.2f}")
    print(f"Each person pays: ${result['per_person']:.2f}")


if __name__ == "__main__":
    main()
