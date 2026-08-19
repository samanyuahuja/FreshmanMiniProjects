# Log Level Counter

This command-line tool counts `DEBUG`, `INFO`, `WARNING`, `ERROR`, and
`CRITICAL` entries in a plain-text log. It also reports lines that do not
contain one of those labels.

## Usage

Pass a log file from the repository root:

```bash
python3 projects/log-level-counter/main.py path/to/app.log
```

Use `-` to read from standard input:

```bash
printf 'INFO Server started\nERROR Connection failed\n' | \
  python3 projects/log-level-counter/main.py -
```

Example output:

```text
DEBUG: 0
INFO: 1
WARNING: 0
ERROR: 1
CRITICAL: 0
UNMATCHED: 0
TOTAL: 2
```

## Tests

```bash
python3 -m unittest discover -s projects/log-level-counter -p 'test_*.py' -v
```

## Limitations

The tool reads UTF-8 text and counts the first recognized level on each line.
It does not parse structured JSON logs or group multiline stack traces.
