"""Tests for the retry helper."""

from __future__ import annotations

import unittest

from retry_helper import retry


class RetryTests(unittest.TestCase):
    def test_returns_first_successful_result(self) -> None:
        calls = 0

        def action() -> str:
            nonlocal calls
            calls += 1
            return "ready"

        self.assertEqual(retry(action), "ready")
        self.assertEqual(calls, 1)

    def test_retries_until_action_succeeds(self) -> None:
        calls = 0

        def action() -> int:
            nonlocal calls
            calls += 1
            if calls < 3:
                raise ValueError("not yet")
            return calls

        self.assertEqual(retry(action, attempts=3, retry_on=(ValueError,)), 3)
        self.assertEqual(calls, 3)

    def test_reraises_last_expected_failure(self) -> None:
        calls = 0

        def action() -> None:
            nonlocal calls
            calls += 1
            raise RuntimeError("still failing")

        with self.assertRaisesRegex(RuntimeError, "still failing"):
            retry(action, attempts=2)
        self.assertEqual(calls, 2)

    def test_does_not_retry_unlisted_exception(self) -> None:
        calls = 0

        def action() -> None:
            nonlocal calls
            calls += 1
            raise KeyError("wrong failure")

        with self.assertRaises(KeyError):
            retry(action, attempts=4, retry_on=(ValueError,))
        self.assertEqual(calls, 1)

    def test_rejects_invalid_settings(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive integer"):
            retry(lambda: None, attempts=0)
        with self.assertRaisesRegex(ValueError, "finite nonnegative"):
            retry(lambda: None, delay_seconds=float("inf"))
        with self.assertRaisesRegex(TypeError, "exception types"):
            retry(lambda: None, retry_on=())


if __name__ == "__main__":
    unittest.main()
