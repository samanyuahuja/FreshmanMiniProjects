# File Extension Summary

This command-line tool counts files by extension in a directory. It can help you quickly see what kinds of files a folder contains without opening each subfolder.

The project uses only Python's standard library.

## Run it

From this project directory, pass the folder you want to inspect:

```bash
python3 main.py /path/to/folder
```

Add `--recursive` to include files inside nested directories:

```bash
python3 main.py /path/to/folder --recursive
```

Example output:

```text
.csv: 2
.py: 4
.txt: 3
[no extension]: 1
```

Extensions are converted to lowercase, so `.TXT` and `.txt` share one count. Files such as `LICENSE` are grouped under `[no extension]`.

## Run the tests

```bash
python3 -m unittest discover -p "test_*.py" -v
```

## Limitations

- The default scan only checks the selected directory. Use `--recursive` for nested folders.
- Only the final suffix is counted. For example, `backup.tar.gz` is counted as `.gz`.
- The tool reports file counts, not file sizes.
