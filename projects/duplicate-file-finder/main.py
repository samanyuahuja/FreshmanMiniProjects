"""Command-line interface for the duplicate file finder."""

import argparse
from pathlib import Path

from duplicate_finder import find_duplicates


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="List groups of files that have identical contents."
    )
    parser.add_argument("directory", type=Path, help="folder to scan")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        groups = find_duplicates(args.directory)
    except (OSError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    if not groups:
        print("No duplicate files found.")
        return 0

    for number, group in enumerate(groups, start=1):
        print(f"Group {number}:")
        for path in group:
            print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
