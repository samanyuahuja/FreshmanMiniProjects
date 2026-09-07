# Study Session Summarizer

This command-line tool adds up study time by subject. Give it one or more sessions in `SUBJECT=MINUTES` format, and it reports the total time, each subject's time, and the most-studied subject. It uses only Python's standard library.

## Usage

Run the command from the repository root:

```bash
python3 projects/study-session-summarizer/main.py "Calculus=40" "CS 124=25" "Calculus=20"
```

The result is:

```text
Total: 85 minutes
Calculus: 60 minutes
CS 124: 25 minutes
Most studied: Calculus
```

Subjects can contain spaces. Minutes must be positive whole numbers.

## Tests

```bash
python3 -m unittest discover -s projects/study-session-summarizer -p 'test_*.py'
```

## Limitations

The tool reads sessions from command-line arguments only. It does not save history, read calendar data, or separate sessions by date. If two subjects have the same total, it reports the one entered first.
