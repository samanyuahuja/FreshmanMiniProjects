# Reading Time Estimator

This command counts the words in a text file and estimates how long they will take to read. The default speed is 200 words per minute, and you can choose a different speed between 50 and 1,000.

## Usage

Run the command from the repository root:

```bash
python3 projects/reading-time-estimator/main.py notes.txt
```

Set a different reading speed with `--wpm`:

```bash
python3 projects/reading-time-estimator/main.py notes.txt --wpm 240
```

Example output:

```text
Words: 350
Estimated reading time: 1m 28s
```

The input file must use UTF-8 text. Invalid paths, empty files, and unsupported reading speeds return an error instead of an estimate.

## Tests

```bash
python3 -m unittest discover -s projects/reading-time-estimator -p 'test_*.py' -v
```

## Limitations

- Words are separated by whitespace, so hyphenated text counts as one word.
- The estimate does not adjust for diagrams, code samples, or difficult material.
- Reading speed varies by person and type of text.
