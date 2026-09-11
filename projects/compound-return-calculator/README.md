# Compound Return Calculator

This command-line tool calculates how a starting value changes when the same percentage return is applied for several periods. It reports the ending value, the amount gained or lost, and the total percentage return. It uses only Python's standard library.

## Usage

Run the command from the repository root. The arguments are the starting value, percentage return per period, and number of periods:

```bash
python3 projects/compound-return-calculator/main.py 1000 5 3
```

The result is:

```text
Starting value: 1,000.00
Ending value: 1,157.63
Growth: 157.63
Total return: 15.76%
```

The rate may be negative, but it must be greater than `-100`. Periods must be a whole number of zero or more.

## Tests

```bash
python3 -m unittest discover -s projects/compound-return-calculator -p 'test_*.py'
```

## Limitations

The calculator applies one fixed return for every period. It does not handle deposits, withdrawals, fees, taxes, changing rates, or investment risk. Its output is a mathematical estimate, not an investment forecast.
