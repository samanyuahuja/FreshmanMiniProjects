# CSV Price Summary

This command-line tool reads dated closing prices from a CSV file and prints a
short summary. It reports the start and end close, total return, highest and
lowest close, and the best and worst one-day returns.

The calculations use Python's `Decimal` type. This keeps values such as `10.75`
as decimal numbers instead of binary floating-point approximations.

## CSV format

The file needs `date` and `close` columns. Dates use the `YYYY-MM-DD` format and
must be ordered from oldest to newest.

```csv
date,close
2026-01-02,100
2026-01-05,110
2026-01-06,99
```

Extra columns are allowed.

## Run it

Python 3.9 or newer is enough. The project has no third-party dependencies.

From this project folder, pass the path to a CSV file:

```bash
python3 price_summary.py prices.csv
```

For the example above, the result is:

```text
Period: 2026-01-02 to 2026-01-06
Start close: 100
End close: 99
Total return: -1.00%
Highest close: 110 on 2026-01-05
Lowest close: 99 on 2026-01-06
Best day: 10.00% on 2026-01-05
Worst day: -10.00% on 2026-01-06
```

## Run the tests

From the repository root:

```bash
python3 -m unittest discover -s projects/csv-price-summary -p 'test_*.py' -v
```

## Limits

- The tool expects one price series per file.
- It does not download market data or check whether dates are trading days.
- Returns are based on consecutive rows, even when calendar days are missing.
- Closing prices are not adjusted for splits or dividends unless the CSV
  already contains adjusted values.
- The output describes past prices and is not an investment recommendation.
