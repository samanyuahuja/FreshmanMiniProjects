"""Validation rules for JSON lists of objects."""

from __future__ import annotations

from collections.abc import Iterable


def validate_records(data: object, required_fields: Iterable[str]) -> list[str]:
    """Return one message for each structural problem in the JSON data."""
    fields = _normalize_fields(required_fields)
    if not isinstance(data, list):
        return ["Root value must be a list."]

    errors: list[str] = []
    for index, record in enumerate(data):
        if not isinstance(record, dict):
            errors.append(f"Item {index} must be an object.")
            continue

        missing = [field for field in fields if field not in record]
        if missing:
            errors.append(f"Item {index} is missing: {', '.join(missing)}.")
    return errors


def _normalize_fields(required_fields: Iterable[str]) -> tuple[str, ...]:
    fields = tuple(dict.fromkeys(field.strip() for field in required_fields))
    if not fields or any(not field for field in fields):
        raise ValueError("Required field names cannot be empty.")
    return fields
