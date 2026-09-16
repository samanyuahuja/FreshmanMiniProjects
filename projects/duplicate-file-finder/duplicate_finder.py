"""Find files that have identical contents."""

from collections import defaultdict
from hashlib import sha256
from pathlib import Path


def file_digest(path: Path, chunk_size: int = 65_536) -> str:
    """Return a SHA-256 digest without loading the whole file at once."""
    digest = sha256()
    with path.open("rb") as file:
        while chunk := file.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def find_duplicates(directory: Path) -> list[list[Path]]:
    """Group regular files that have the same size and contents."""
    if not directory.is_dir():
        raise ValueError(f"Not a directory: {directory}")

    files_by_size: dict[int, list[Path]] = defaultdict(list)
    for path in sorted(directory.rglob("*")):
        if path.is_file() and not path.is_symlink():
            files_by_size[path.stat().st_size].append(path)

    duplicate_groups: list[list[Path]] = []
    for same_size_files in files_by_size.values():
        if len(same_size_files) < 2:
            continue

        files_by_digest: dict[str, list[Path]] = defaultdict(list)
        for path in same_size_files:
            files_by_digest[file_digest(path)].append(path)

        for group in files_by_digest.values():
            if len(group) > 1:
                duplicate_groups.append(group)

    return sorted(duplicate_groups, key=lambda group: str(group[0]))
