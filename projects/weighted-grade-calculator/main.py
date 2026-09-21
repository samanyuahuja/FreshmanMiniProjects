"""Command-line interface for the weighted grade calculator."""

import argparse

from grade_calculator import calculate_weighted_grade, letter_grade


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate a final grade from weighted category scores."
    )
    parser.add_argument(
        "--item",
        action="append",
        nargs=2,
        metavar=("SCORE", "WEIGHT"),
        type=float,
        required=True,
        help="add a score and its percentage weight; repeat for each category",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        percentage = calculate_weighted_grade(args.item)
    except ValueError as error:
        parser.error(str(error))

    print(f"Weighted grade: {percentage:.2f}%")
    print(f"Letter grade: {letter_grade(percentage)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
