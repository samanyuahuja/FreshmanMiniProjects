"""Compare package prices using price per unit."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True)
class Item:
    name: str
    price: Decimal
    quantity: Decimal

    @property
    def price_per_unit(self) -> Decimal:
        return self.price / self.quantity


def parse_item(value: str) -> Item:
    """Parse one name,price,quantity command-line value."""
    fields = next(csv.reader([value], skipinitialspace=True))
    if len(fields) != 3:
        raise ValueError("Each item must contain name, price, and quantity.")

    name = fields[0].strip()
    if not name:
        raise ValueError("Item name cannot be empty.")

    try:
        price = Decimal(fields[1].strip())
        quantity = Decimal(fields[2].strip())
    except InvalidOperation as error:
        raise ValueError("Price and quantity must be numbers.") from error

    if not price.is_finite() or price <= 0:
        raise ValueError("Price must be a positive finite number.")
    if not quantity.is_finite() or quantity <= 0:
        raise ValueError("Quantity must be a positive finite number.")
    return Item(name=name, price=price, quantity=quantity)


def rank_items(items: list[Item]) -> list[Item]:
    """Return items from lowest to highest price per unit."""
    if len(items) < 2:
        raise ValueError("Enter at least two items to compare.")
    return sorted(items, key=lambda item: (item.price_per_unit, item.name.lower()))


def format_results(items: list[Item]) -> str:
    """Format ranked items as a small text table."""
    ranked = rank_items(items)
    lines = ["Item | Price | Quantity | Per unit", "-" * 42]
    for item in ranked:
        lines.append(
            f"{item.name} | ${item.price:.2f} | {item.quantity:g} | "
            f"${item.price_per_unit:.4f}"
        )
    lines.append(f"Best value: {ranked[0].name}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare packages by price per unit."
    )
    parser.add_argument(
        "items",
        nargs="+",
        metavar="NAME,PRICE,QUANTITY",
        help='package details, for example "Small,3.99,12"',
    )
    args = parser.parse_args()

    try:
        print(format_results([parse_item(value) for value in args.items]))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
