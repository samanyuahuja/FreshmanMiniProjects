# Unit Price Comparer

This command-line tool compares package prices using cost per unit. It is useful
when two products have different prices and quantities.

The script uses Python's `Decimal` type so values such as `3.99` are handled as
decimal numbers instead of binary floating-point approximations.

## Run it

Python 3.9 or newer is enough. The project has no third-party dependencies.

Pass each choice as `name,price,quantity`:

```bash
python3 unit_price.py "Small,3.99,12" "Large,6.49,24"
```

The result is sorted from the lowest unit price to the highest:

```text
Item | Price | Quantity | Per unit
------------------------------------------
Large | $6.49 | 24 | $0.2704
Small | $3.99 | 12 | $0.3325
Best value: Large
```

Names containing commas need CSV-style quotes inside the argument:

```bash
python3 unit_price.py '"Cereal, family size",6.49,24' "Regular box,4.25,12"
```

## Run the tests

From the repository root:

```bash
python3 -m unittest discover -s projects/unit-price-comparer -p 'test_*.py' -v
```

## Limits

- Quantities must use the same unit for a fair comparison.
- The tool does not convert currencies or units.
- Taxes, coupons, and multi-buy discounts are not included.
- Unit prices are displayed to four decimal places.
