"""Command-line interface for counting log severity labels."""

import argparse
from pathlib import Path
import sys
from typing import TextIO

from log_counter import LOG_LEVELS, LogCounts, count_log_levels


def read_lines(path: str) -> TextIO:
    if path == "-":
        return sys.stdin
    return Path(path).open(encoding="utf-8")


def format_counts(counts: LogCounts) -> str:
    rows = [f"{level}: {counts.levels[level]}" for level in LOG_LEVELS]
    rows.extend((f"UNMATCHED: {counts.unmatched}", f"TOTAL: {counts.total}"))
    return "\n".join(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Count common severity labels in a text log."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="-",
        help="log file path, or - to read from standard input",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        lines = read_lines(args.path)
        print(format_counts(count_log_levels(lines)))
    except (OSError, UnicodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    finally:
        if "lines" in locals() and lines is not sys.stdin:
            lines.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
