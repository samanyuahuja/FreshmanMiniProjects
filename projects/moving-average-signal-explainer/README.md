# Moving Average Signal Explainer

This command-line tool compares a short simple moving average with a longer
one. It reports their current relationship and whether they crossed on the
latest price.

## Usage

Pass comma-separated prices and choose the two window lengths:

```bash
python3 projects/moving-average-signal-explainer/main.py \
  "5,4,3,6" --short 2 --long 3
```

The command prints:

```text
Short average: 4.50
Long average: 4.33
Relationship: short is above long
Description: bullish crossover
```

The price list needs at least one more value than the long window. That extra
value lets the program compare the latest averages with the previous ones.

## Tests

```bash
python3 -m unittest discover \
  -s projects/moving-average-signal-explainer -p 'test_*.py' -v
```

## Limitations

The program accepts one manually entered price series and calculates simple
moving averages only. Its descriptions explain the arithmetic. They are not
trading recommendations and do not account for fees, risk, or market context.
