"""Check the header and row shape of a CSV file."""

from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ColumnCheck:
    columns: tuple[str, ...]
    missing: tuple[str, ...]
    duplicates: tuple[str, ...]
    row_count: int

    @property
    def is_valid(self) -> bool:
        return not self.missing and not self.duplicates


def check_csv(path: str | Path, required_columns: Iterable[str]) -> ColumnCheck:
    """Return a summary of one CSV file without changing it."""
    required = tuple(dict.fromkeys(column.strip() for column in required_columns))
    if not required or any(not column for column in required):
        raise ValueError("At least one non-empty required column is needed.")

    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        try:
            columns = tuple(column.strip() for column in next(reader))
        except StopIteration as error:
            raise ValueError("CSV file is empty.") from error

        if not columns or any(not column for column in columns):
            raise ValueError("CSV header cannot contain blank column names.")

        row_count = 0
        for line_number, row in enumerate(reader, start=2):
            if len(row) != len(columns):
                raise ValueError(
                    f"Row {line_number} has {len(row)} values; expected {len(columns)}."
                )
            row_count += 1

    counts = Counter(columns)
    duplicates = tuple(column for column in columns if counts[column] > 1)
    return ColumnCheck(
        columns=columns,
        missing=tuple(column for column in required if column not in counts),
        duplicates=tuple(dict.fromkeys(duplicates)),
        row_count=row_count,
    )
