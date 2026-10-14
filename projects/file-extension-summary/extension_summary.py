"""Count files by their final filename extension."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

NO_EXTENSION = "[no extension]"


def summarize_extensions(
    directory: str | Path,
    *,
    recursive: bool = False,
) -> dict[str, int]:
    """Return extension counts for files inside a directory."""
    root = Path(directory)
    if not root.exists():
        raise FileNotFoundError(f"Directory does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {root}")

    entries = root.rglob("*") if recursive else root.iterdir()
    counts = Counter(
        _extension_label(path)
        for path in entries
        if path.is_file()
    )
    return dict(sorted(counts.items()))


def _extension_label(path: Path) -> str:
    return path.suffix.lower() or NO_EXTENSION
