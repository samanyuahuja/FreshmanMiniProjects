# Average Share-Cost Calculator

This command-line program finds the weighted average price paid across several share purchases. Each purchase includes a price and a share count, so larger purchases affect the average more than smaller ones.

## Usage

Write each purchase as `PRICE:SHARES`:

```bash
python3 projects/average-share-cost/main.py 20:2 30:3
```

The example represents two shares bought at $20 and three shares bought at $30. It prints:

```text
Total shares: 5.0000
Total cost: $130.00
Average cost per share: $26.00
```

Prices and share counts must be finite numbers greater than zero. Fractional shares are supported.

## Tests

Run the project tests from the repository root:

```bash
python3 -m unittest discover -s projects/average-share-cost -p 'test_*.py'
```

## Limitations

The calculator uses the purchase values entered on the command line. It does not fetch market prices or include fees, taxes, sales, dividends, or currency conversion. Results use standard floating-point arithmetic and are rounded only when displayed. This is a cost calculation, not an estimate of future returns or investment advice.
