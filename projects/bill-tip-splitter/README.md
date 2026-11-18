# Bill and Tip Splitter

This command-line tool adds a percentage tip to a restaurant bill and splits the total between a chosen number of people. It uses decimal arithmetic so currency values round to cents in a predictable way.

## Run it

Pass the bill subtotal, tip percentage, and number of people:

```bash
python3 main.py 48.50 18 3
```

Output:

```text
Tip: $8.73
Total: $57.23
Each person pays: $19.08
```

The tool rejects negative subtotals, negative tip percentages, and groups smaller than one person.

## Tests

From this project directory, run:

```bash
python3 -m unittest test_splitter.py
```

## Limitations

The result does not include taxes or separate items. Each person's share is rounded independently to the nearest cent, so the displayed shares can differ from the total by a few cents when multiplied by the group size.
