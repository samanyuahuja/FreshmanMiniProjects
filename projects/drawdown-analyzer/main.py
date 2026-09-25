"""Command-line interface for the drawdown analyzer."""

import argparse

from drawdown_analyzer import analyze_drawdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find the largest drawdown in a list of portfolio values."
    )
    parser.add_argument(
        "values",
        nargs="+",
        type=float,
        help="positive portfolio values in chronological order",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        result = analyze_drawdown(args.values)
    except (TypeError, ValueError) as error:
        raise SystemExit(f"error: {error}") from error

    print(f"Maximum drawdown: {result.max_drawdown:.2%}")
    print(f"Peak index: {result.peak_index}")
    print(f"Trough index: {result.trough_index}")
    recovery = (
        str(result.recovery_index)
        if result.recovery_index is not None
        else "not recovered"
    )
    print(f"Recovery index: {recovery}")


if __name__ == "__main__":
    main()
