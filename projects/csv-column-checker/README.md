# CSV Column Checker

This command checks a CSV file before another script tries to use it. It lists the headers and row count, then reports required columns that are missing, duplicate headers, or rows with the wrong number of values. The input file is never changed.

## Run it

From the repository root, pass the CSV path and repeat `--require` for each column you need:

```bash
python3 projects/csv-column-checker/main.py students.csv \
  --require name \
  --require score
```

For a valid file, the output looks like this:

```text
Columns: name, score
Data rows: 24
Result: valid
```

Missing or duplicate columns produce `Result: invalid`. The command exits with status `0` for a valid file, `1` for a failed column check, and `2` when the file cannot be read or its rows are malformed.

## Tests

```bash
python3 -m unittest discover -s projects/csv-column-checker -p 'test_*.py' -v
```

## Limits

- Column matching is case-sensitive.
- Files must use UTF-8 text and comma-separated fields.
- The checker does not validate cell types or values.
- Quoted fields are supported through Python's `csv` module.
