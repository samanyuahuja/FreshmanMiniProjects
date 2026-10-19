"""Command-line entry point for the reading-time estimator."""

from __future__ import annotations

import argparse
from pathlib import Path

from reading_time import estimate_reading_time, format_estimate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Estimate reading time for a UTF-8 text file.",
    )
    parser.add_argument("file", type=Path, help="path to the text file")
    parser.add_argument(
        "--wpm",
        type=int,
        default=200,
        help="reading speed in words per minute (default: 200)",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        text = args.file.read_text(encoding="utf-8")
        estimate = estimate_reading_time(text, args.wpm)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    print(format_estimate(estimate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
