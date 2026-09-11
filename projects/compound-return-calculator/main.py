"""Command-line interface for the compound-return calculator."""

from __future__ import annotations

import argparse

from calculator import calculate_compound_return


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate repeated growth at a fixed percentage rate."
    )
    parser.add_argument("initial", type=float, help="starting value")
    parser.add_argument("rate", type=float, help="percentage change per period")
    parser.add_argument("periods", type=int, help="number of compounding periods")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        result = calculate_compound_return(args.initial, args.rate, args.periods)
    except ValueError as error:
        print(error)
        return 2

    print(f"Starting value: {args.initial:,.2f}")
    print(f"Ending value: {result.ending_value:,.2f}")
    print(f"Growth: {result.growth_amount:,.2f}")
    print(f"Total return: {result.total_return_percent:.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
