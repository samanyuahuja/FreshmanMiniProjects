# Text Statistics

This command-line tool counts words, sentence endings, characters, and nonempty lines in plain text. It uses only the Python standard library.

## Run it

Pass a UTF-8 text file:

```bash
python3 projects/text-statistics/main.py notes.txt
```

You can also pipe text into the command:

```bash
printf 'One sentence.\nAnother one!' | python3 projects/text-statistics/main.py --json
```

The JSON output for that example is:

```json
{
  "characters": 26,
  "characters_without_spaces": 23,
  "words": 4,
  "sentences": 2,
  "nonempty_lines": 2
}
```

## Tests

Run the tests from the repository root:

```bash
python3 -m unittest discover -s projects/text-statistics -v
```

## Limits

Words are whitespace-separated pieces that contain at least one letter or number. Sentence counting uses groups of `.`, `!`, or `?`, so text without those marks reports zero sentences. The tool reads plain UTF-8 files and does not parse formats such as PDF or Word documents.
