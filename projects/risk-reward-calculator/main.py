"""Command-line interface for the risk-reward calculator."""

from __future__ import annotations

import argparse

from risk_reward import analyze_trade


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare the possible loss and gain for a planned trade."
    )
    parser.add_argument("entry", type=float, help="planned entry price")
    parser.add_argument("stop", type=float, help="stop-loss price")
    parser.add_argument("target", type=float, help="profit target price")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        result = analyze_trade(args.entry, args.stop, args.target)
    except ValueError as error:
        print(f"Error: {error}")
        return 2

    print(f"Direction: {result.direction}")
    print(f"Risk per unit: {result.risk_per_unit:.2f}")
    print(f"Reward per unit: {result.reward_per_unit:.2f}")
    print(f"Reward-to-risk ratio: {result.reward_risk_ratio:.2f}:1")
    print(f"Break-even win rate: {result.break_even_win_rate_percent:.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
