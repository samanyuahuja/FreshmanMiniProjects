"""Count common severity labels in plain-text log lines."""

from collections.abc import Iterable
from dataclasses import dataclass
import re


LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
LEVEL_PATTERN = re.compile(
    rf"(?:^|[\s\[])({'|'.join(LOG_LEVELS)})(?=$|[\s\]])",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class LogCounts:
    levels: dict[str, int]
    unmatched: int

    @property
    def total(self) -> int:
        return sum(self.levels.values()) + self.unmatched


def count_log_levels(lines: Iterable[str]) -> LogCounts:
    """Count the first recognized level in each line."""
    counts = {level: 0 for level in LOG_LEVELS}
    unmatched = 0

    for line in lines:
        match = LEVEL_PATTERN.search(line)
        if match is None:
            unmatched += 1
            continue
        counts[match.group(1).upper()] += 1

    return LogCounts(levels=counts, unmatched=unmatched)
