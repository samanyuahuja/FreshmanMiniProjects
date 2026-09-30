# Line Ending Checker

This command-line tool reports whether a file uses LF, CRLF, CR, mixed, or no line endings. It reads the file as bytes, so it does not need to know the text encoding. The file is never changed.

## Run it

Pass the path of one file:

```bash
python3 main.py sample.txt
```

Example output for a file that mixes Windows and Unix line endings:

```text
Style: mixed
CRLF endings: 2
LF endings: 1
CR endings: 0
```

## Run the tests

From this project folder, run:

```bash
python3 -m unittest -v
```

## Limits

The tool checks one file at a time. It does not convert line endings, scan folders, identify character encodings, or enforce a project policy. A final line without an ending is not included in the counts.
