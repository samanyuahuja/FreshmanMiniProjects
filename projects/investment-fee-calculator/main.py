"""Command-line interface for the investment fee calculator."""

import argparse

from fee_calculator import compare_fee


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare compound growth with and without an annual fee.",
    )
    parser.add_argument("principal", type=float, help="starting amount")
    parser.add_argument("annual_return", type=float, help="annual return percent")
    parser.add_argument("annual_fee", type=float, help="annual fee percent")
    parser.add_argument("years", type=int, help="number of years")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        without_fee, with_fee, fee_drag = compare_fee(
            args.principal,
            args.annual_return / 100,
            args.annual_fee / 100,
            args.years,
        )
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

    print(f"Without fee: ${without_fee:,.2f}")
    print(f"After fee:   ${with_fee:,.2f}")
    print(f"Fee drag:    ${fee_drag:,.2f}")


if __name__ == "__main__":
    main()
