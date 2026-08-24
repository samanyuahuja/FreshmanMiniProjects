# Expense Splitter

Expense Splitter divides a bill evenly and keeps the final total exact to the
cent. An optional tip percentage can be added before the split.

## Usage

Run the program from the repository root with a subtotal and number of people:

```bash
python3 projects/expense-splitter/main.py 10 3
```

Add a tip with `--tip`:

```bash
python3 projects/expense-splitter/main.py 25 2 --tip 20
```

The second command prints:

```text
Person 1: $15.00
Person 2: $15.00
Total: $30.00
```

If a total cannot be divided evenly, the first people receive one extra cent.
For example, splitting $10 among three people produces shares of $3.34, $3.33,
and $3.33.

## Tests

```bash
python3 -m unittest discover -s projects/expense-splitter -p 'test_*.py' -v
```

## Limitations

The program splits one subtotal evenly. It does not assign individual items,
handle tax separately, or track payments between people.
