"""Command-line interface for the average share-cost calculator."""

from __future__ import annotations

import argparse

from average_cost import calculate_average_cost


def purchase(value: str) -> tuple[float, float]:
    """Parse one purchase written as PRICE:SHARES."""
    parts = value.split(":")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("use PRICE:SHARES, such as 25.50:4")

    try:
        return float(parts[0]), float(parts[1])
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "price and shares must be numbers"
        ) from error


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find the weighted average price paid for shares."
    )
    parser.add_argument(
        "purchases",
        metavar="PRICE:SHARES",
        nargs="+",
        type=purchase,
        help="one purchase price and share count",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        result = calculate_average_cost(args.purchases)
    except ValueError as error:
        print(f"Error: {error}")
        return 2

    print(f"Total shares: {result.total_shares:.4f}")
    print(f"Total cost: ${result.total_cost:.2f}")
    print(f"Average cost per share: ${result.average_cost:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
