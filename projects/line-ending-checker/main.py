"""Command-line interface for checking line endings."""

import argparse
from pathlib import Path

from line_endings import inspect_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Report the line-ending style used by a file."
    )
    parser.add_argument("path", type=Path, help="file to inspect")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        summary = inspect_file(args.path)
    except OSError as error:
        raise SystemExit(f"error: {error}") from error

    print(f"Style: {summary.style}")
    print(f"CRLF endings: {summary.crlf}")
    print(f"LF endings: {summary.lf}")
    print(f"CR endings: {summary.cr}")


if __name__ == "__main__":
    main()
