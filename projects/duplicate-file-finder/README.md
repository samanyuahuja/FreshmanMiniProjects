# Duplicate File Finder

This command-line tool scans a folder and lists files with identical contents. It only reports matches and never deletes or changes a file.

## Run it

Python 3.9 or newer is required. From this project folder, pass the directory you want to check:

```bash
python3 main.py ~/Downloads
```

The scan includes nested folders. A result looks like this:

```text
Group 1:
  /Users/name/Downloads/notes.txt
  /Users/name/Downloads/archive/notes-copy.txt
```

Files are compared in two steps. The program first groups them by size, then calculates a SHA-256 digest for files that could match. This avoids hashing files with unique sizes.

## Run the tests

```bash
python3 -m unittest discover -s . -p "test_*.py" -v
```

## Limits

- Symbolic links are skipped.
- Unreadable files stop the scan and produce an error.
- The program reports duplicates but does not decide which copy should be removed.
- A large folder may take time because matching files must be read to calculate their digests.
