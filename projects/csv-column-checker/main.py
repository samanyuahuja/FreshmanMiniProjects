"""Command-line entry point for the CSV column checker."""

from __future__ import annotations

import argparse
from pathlib import Path

from column_checker import check_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check whether a CSV file contains required columns."
    )
    parser.add_argument("csv_file", type=Path, help="CSV file to inspect")
    parser.add_argument(
        "--require",
        action="append",
        required=True,
        dest="required_columns",
        metavar="COLUMN",
        help="required column name; repeat for multiple columns",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        result = check_csv(args.csv_file, args.required_columns)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}")
        return 2

    print(f"Columns: {', '.join(result.columns)}")
    print(f"Data rows: {result.row_count}")
    if result.missing:
        print(f"Missing: {', '.join(result.missing)}")
    if result.duplicates:
        print(f"Duplicate headers: {', '.join(result.duplicates)}")
    if result.is_valid:
        print("Result: valid")
        return 0

    print("Result: invalid")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
