"""Summarize a dated series of closing prices from a CSV file."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path


@dataclass(frozen=True)
class PricePoint:
    day: date
    close: Decimal


@dataclass(frozen=True)
class PriceSummary:
    first: PricePoint
    last: PricePoint
    highest: PricePoint
    lowest: PricePoint
    best_day: date
    best_return: Decimal
    worst_day: date
    worst_return: Decimal

    @property
    def total_return(self) -> Decimal:
        return self.last.close / self.first.close - 1


def load_prices(path: str | Path) -> list[PricePoint]:
    """Read date and close columns from a CSV file."""
    try:
        with Path(path).open(newline="", encoding="utf-8-sig") as price_file:
            reader = csv.DictReader(price_file)
            if reader.fieldnames is None or not {"date", "close"}.issubset(
                reader.fieldnames
            ):
                raise ValueError("CSV must contain date and close columns.")
            points = [
                _parse_row(row, line_number)
                for line_number, row in enumerate(reader, start=2)
            ]
    except OSError as error:
        raise ValueError(f"Could not read CSV file: {error}") from error

    if len(points) < 2:
        raise ValueError("CSV must contain at least two price rows.")
    if any(
        current.day <= previous.day
        for previous, current in zip(points, points[1:])
    ):
        raise ValueError("Dates must be unique and ordered from oldest to newest.")
    return points


def _parse_row(row: dict[str, str | None], line_number: int) -> PricePoint:
    raw_date = (row.get("date") or "").strip()
    raw_close = (row.get("close") or "").strip()
    try:
        parsed_date = date.fromisoformat(raw_date)
    except ValueError as error:
        raise ValueError(f"Line {line_number} has an invalid date.") from error
    try:
        close = Decimal(raw_close)
    except InvalidOperation as error:
        raise ValueError(f"Line {line_number} has an invalid close price.") from error
    if not close.is_finite() or close <= 0:
        raise ValueError(f"Line {line_number} close price must be positive and finite.")
    return PricePoint(parsed_date, close)


def summarize_prices(points: list[PricePoint]) -> PriceSummary:
    """Calculate range and daily-return statistics for ordered prices."""
    if len(points) < 2:
        raise ValueError("At least two price points are required.")

    daily_returns = [
        (current.day, current.close / previous.close - 1)
        for previous, current in zip(points, points[1:])
    ]
    best_day, best_return = max(daily_returns, key=lambda item: item[1])
    worst_day, worst_return = min(daily_returns, key=lambda item: item[1])
    return PriceSummary(
        first=points[0],
        last=points[-1],
        highest=max(points, key=lambda point: point.close),
        lowest=min(points, key=lambda point: point.close),
        best_day=best_day,
        best_return=best_return,
        worst_day=worst_day,
        worst_return=worst_return,
    )


def format_summary(summary: PriceSummary) -> str:
    """Format a price summary for terminal output."""
    return "\n".join(
        [
            f"Period: {summary.first.day} to {summary.last.day}",
            f"Start close: {summary.first.close}",
            f"End close: {summary.last.close}",
            f"Total return: {summary.total_return:.2%}",
            f"Highest close: {summary.highest.close} on {summary.highest.day}",
            f"Lowest close: {summary.lowest.close} on {summary.lowest.day}",
            f"Best day: {summary.best_return:.2%} on {summary.best_day}",
            f"Worst day: {summary.worst_return:.2%} on {summary.worst_day}",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize closing prices from CSV.")
    parser.add_argument(
        "csv_file",
        type=Path,
        help="CSV file with date and close columns",
    )
    args = parser.parse_args()
    try:
        print(format_summary(summarize_prices(load_prices(args.csv_file))))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
