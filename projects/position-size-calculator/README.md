# Position Size Calculator

This command-line tool calculates how many whole shares fit within a chosen
risk limit. It is meant for practicing position-sizing math, not for choosing
trades.

## Usage

Run the script with an account balance, risk percentage, entry price, and stop
price:

```bash
python3 main.py 10000 1 50 48
```

The example sets a $100 risk budget. With $2 between the entry and stop prices,
the result is 50 shares:

```text
Risk budget: $100.00
Risk per share: $2.00
Maximum shares: 50
Position value: $2500.00
```

Run the tests from the repository root:

```bash
python3 -m unittest discover -s projects/position-size-calculator -p 'test_*.py' -v
```

## Limitations

The calculator uses whole shares and does not include fees, slippage, taxes,
portfolio-wide exposure, or gap risk. It checks the distance between the entry
and stop prices but does not decide whether a trade is appropriate.
