"""Try the retry helper with a predictable failing task."""

from __future__ import annotations

import argparse

from retry_helper import retry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a task that fails a chosen number of times.",
    )
    parser.add_argument(
        "--attempts",
        type=int,
        default=3,
        help="maximum number of calls (default: 3)",
    )
    parser.add_argument(
        "--failures",
        type=int,
        default=2,
        help="number of failures before success (default: 2)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="seconds between attempts (default: 0)",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.failures < 0:
        raise SystemExit("--failures must be nonnegative")

    calls = 0

    def sample_task() -> str:
        nonlocal calls
        calls += 1
        print(f"Attempt {calls}")
        if calls <= args.failures:
            raise RuntimeError("sample task failed")
        return "Task completed"

    try:
        print(
            retry(
                sample_task,
                attempts=args.attempts,
                delay_seconds=args.delay,
            )
        )
    except RuntimeError as error:
        print(f"Stopped: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
