"""Command-line interface for the text statistics tool."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

from text_stats import analyze_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Count words, sentences, characters, and nonempty lines."
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=Path,
        help="UTF-8 text file. If omitted, text is read from standard input.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the counts as JSON.",
    )
    return parser


def read_text(path: Path | None) -> str:
    if path is None:
        return sys.stdin.read()
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        stats = analyze_text(read_text(args.file))
    except (OSError, UnicodeError) as error:
        parser.error(str(error))

    values = asdict(stats)
    if args.json:
        print(json.dumps(values, indent=2))
    else:
        for label, value in values.items():
            print(f"{label.replace('_', ' ').title()}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
