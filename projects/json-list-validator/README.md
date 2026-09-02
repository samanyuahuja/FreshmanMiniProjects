# JSON List Validator

This command-line tool checks that a JSON file contains a list of objects and that every object includes the fields you name. It uses only Python's standard library.

## Usage

Run the command from the repository root:

```bash
python3 projects/json-list-validator/main.py records.json --required name score
```

For this file:

```json
[
  {"name": "Ava", "score": 91},
  {"name": "Noah"}
]
```

the command reports:

```text
Item 1 is missing: score.
```

A valid file exits with status 0. A structural validation failure exits with status 1. File, JSON syntax, and command configuration errors exit with status 2.

## Tests

```bash
python3 -m unittest discover -s projects/json-list-validator -p 'test_*.py'
```

## Limitations

The validator checks the root list, object items, and required field names. It does not validate value types, nested data, or a JSON Schema.
