"""Inspect the line-ending bytes used by a file."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LineEndingSummary:
    crlf: int
    lf: int
    cr: int

    @property
    def style(self) -> str:
        present = [
            name
            for name, count in (("CRLF", self.crlf), ("LF", self.lf), ("CR", self.cr))
            if count
        ]
        if not present:
            return "none"
        if len(present) > 1:
            return "mixed"
        return present[0]


def inspect_bytes(data: bytes) -> LineEndingSummary:
    """Count CRLF, lone LF, and lone CR endings without decoding the file."""
    crlf = data.count(b"\r\n")
    return LineEndingSummary(
        crlf=crlf,
        lf=data.count(b"\n") - crlf,
        cr=data.count(b"\r") - crlf,
    )


def inspect_file(path: str | Path) -> LineEndingSummary:
    """Read a file as bytes and summarize its line endings."""
    return inspect_bytes(Path(path).read_bytes())
