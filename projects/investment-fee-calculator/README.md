# Investment Fee Calculator

This command-line tool shows how an annual investment fee changes compound
growth. It reports the ending value without a fee, the ending value after the
fee, and the difference between them.

## Usage

Pass the starting amount, expected annual return percentage, annual fee
percentage, and number of years:

```bash
python3 main.py 10000 7 1 10
```

Example output:

```text
Without fee: $19,671.51
After fee:   $17,908.48
Fee drag:    $1,763.04
```

Run the tests with:

```bash
python3 -m unittest
```

## Limitations

The calculation uses one fixed annual return and subtracts the fee from that
return once per year. It does not include taxes, deposits, withdrawals,
inflation, or changing market returns. The output is an estimate, not an
investment recommendation.
