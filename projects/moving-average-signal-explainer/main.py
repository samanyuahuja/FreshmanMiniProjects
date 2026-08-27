"""Command-line interface for the moving-average signal explainer."""

import argparse

from signal_explainer import explain_signal


def parse_prices(value: str) -> list[float]:
    """Parse a comma-separated price list."""
    try:
        prices = [float(item.strip()) for item in value.split(",")]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("prices must be comma-separated numbers") from exc
    if not prices:
        raise argparse.ArgumentTypeError("enter at least one price")
    return prices


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare short and long simple moving averages."
    )
    parser.add_argument("prices", type=parse_prices, help="comma-separated prices")
    parser.add_argument("--short", type=int, default=3, dest="short_window")
    parser.add_argument("--long", type=int, default=5, dest="long_window")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        summary = explain_signal(
            args.prices, args.short_window, args.long_window
        )
    except ValueError as exc:
        build_parser().error(str(exc))

    print(f"Short average: {summary.short_average:.2f}")
    print(f"Long average: {summary.long_average:.2f}")
    print(f"Relationship: short is {summary.relationship} long")
    print(f"Description: {summary.signal}")


if __name__ == "__main__":
    main()
