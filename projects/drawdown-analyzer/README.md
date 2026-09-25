# Drawdown Analyzer

This command-line tool finds the largest drop from a previous peak in a list of portfolio values. It reports the size of that drawdown and the indexes where the peak, trough, and recovery occurred.

## Run it

Use Python 3.8 or newer. Enter the values in chronological order:

```bash
python3 main.py 100 120 90 105 125
```

Output:

```text
Maximum drawdown: 25.00%
Peak index: 1
Trough index: 2
Recovery index: 4
```

Indexes start at zero, so index `1` is the second value. If the values never return to the previous peak, the recovery line says `not recovered`.

## Run the tests

From this project folder, run:

```bash
python3 -m unittest -v
```

## Limits

The tool accepts positive, finite numbers only. It works with a short list entered on the command line and does not read dates or CSV files. It measures drawdown from the raw values without adjusting for deposits, withdrawals, fees, or inflation.
