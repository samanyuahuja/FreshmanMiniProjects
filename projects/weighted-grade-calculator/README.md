# Weighted Grade Calculator

This command-line tool calculates a course percentage from category scores and weights. It also reports a letter grade using a basic A-F scale.

## Run it

Use one `--item` argument for each category. The first number is the score and the second is its percentage weight.

```bash
python3 main.py --item 92 40 --item 81 60
```

Output:

```text
Weighted grade: 85.40%
Letter grade: B
```

The weights must add up to 100. Scores must be between 0 and 100.

## Run the tests

From this project directory:

```bash
python3 -m unittest -v
```

## Limits

- The letter scale is A at 90, B at 80, C at 70, D at 60, and F below 60.
- It does not support plus or minus grades.
- It does not calculate the score needed on a future assignment.
- It uses category percentages, not points earned and points possible.
