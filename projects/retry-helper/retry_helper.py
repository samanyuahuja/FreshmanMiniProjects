"""Run a callable again when it raises an expected exception."""

from __future__ import annotations

from collections.abc import Callable
from math import isfinite
import time
from typing import TypeVar


T = TypeVar("T")


def retry(
    action: Callable[[], T],
    *,
    attempts: int = 3,
    delay_seconds: float = 0.0,
    retry_on: tuple[type[BaseException], ...] = (Exception,),
) -> T:
    """Return the action result, retrying expected failures when possible."""
    if not callable(action):
        raise TypeError("action must be callable")
    if isinstance(attempts, bool) or not isinstance(attempts, int) or attempts < 1:
        raise ValueError("attempts must be a positive integer")
    if (
        isinstance(delay_seconds, bool)
        or not isinstance(delay_seconds, (int, float))
        or not isfinite(delay_seconds)
        or delay_seconds < 0
    ):
        raise ValueError("delay_seconds must be a finite nonnegative number")
    if not retry_on or not all(
        isinstance(error_type, type) and issubclass(error_type, BaseException)
        for error_type in retry_on
    ):
        raise TypeError("retry_on must contain exception types")

    for attempt_number in range(1, attempts + 1):
        try:
            return action()
        except retry_on:
            if attempt_number == attempts:
                raise
            if delay_seconds:
                time.sleep(delay_seconds)

    raise RuntimeError("retry loop ended unexpectedly")
