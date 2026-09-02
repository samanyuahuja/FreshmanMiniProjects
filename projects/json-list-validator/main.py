"""Command-line interface for the JSON list validator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from validator import validate_records


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check a JSON list for objects and required fields."
    )
    parser.add_argument("file", type=Path, help="path to a JSON file")
    parser.add_argument(
        "--required",
        nargs="+",
        required=True,
        metavar="FIELD",
        help="field names that every object must contain",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
        errors = validate_records(data, args.required)
    except OSError as error:
        print(f"Could not read {args.file}: {error}")
        return 2
    except json.JSONDecodeError as error:
        print(f"Invalid JSON at line {error.lineno}, column {error.colno}.")
        return 2
    except ValueError as error:
        print(error)
        return 2

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"Valid: {len(data)} records contain all required fields.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
