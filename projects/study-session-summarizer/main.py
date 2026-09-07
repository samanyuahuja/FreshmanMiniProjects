"""Command-line interface for the study session summarizer."""

from __future__ import annotations

import argparse

from summarizer import summarize_sessions


def parse_session(value: str) -> tuple[str, int]:
    """Parse a SUBJECT=MINUTES argument."""
    subject, separator, minutes_text = value.rpartition("=")
    if not separator or not subject.strip():
        raise argparse.ArgumentTypeError("use SUBJECT=MINUTES")
    try:
        minutes = int(minutes_text)
    except ValueError as error:
        raise argparse.ArgumentTypeError("minutes must be an integer") from error
    if minutes <= 0:
        raise argparse.ArgumentTypeError("minutes must be positive")
    return subject, minutes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Add up study time by subject."
    )
    parser.add_argument(
        "sessions",
        nargs="+",
        type=parse_session,
        metavar="SUBJECT=MINUTES",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    summary = summarize_sessions(args.sessions)
    print(f"Total: {summary.total_minutes} minutes")
    for subject, minutes in summary.minutes_by_subject.items():
        print(f"{subject}: {minutes} minutes")
    print(f"Most studied: {summary.top_subject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
