"""Command-line interface for the position size calculator."""

import argparse
from decimal import Decimal, InvalidOperation

from position_size import calculate_position_size


def decimal_value(raw_value: str) -> Decimal:
    try:
        return Decimal(raw_value)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError(f"invalid number: {raw_value}") from error


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate whole shares from a fixed percentage risk limit."
    )
    parser.add_argument("balance", type=decimal_value, help="account balance")
    parser.add_argument("risk", type=decimal_value, help="risk percentage")
    parser.add_argument("entry", type=decimal_value, help="entry price")
    parser.add_argument("stop", type=decimal_value, help="stop price")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        result = calculate_position_size(
            args.balance, args.risk, args.entry, args.stop
        )
    except ValueError as error:
        print(f"Error: {error}")
        return 2

    print(f"Risk budget: ${result.risk_budget:.2f}")
    print(f"Risk per share: ${result.risk_per_share:.2f}")
    print(f"Maximum shares: {result.shares}")
    print(f"Position value: ${result.position_value:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
