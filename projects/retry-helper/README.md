# Retry Helper

This project repeats a Python function when it raises an expected exception.
It stops as soon as the function succeeds or the allowed attempts run out.

## Run the example

```bash
python3 main.py --attempts 3 --failures 2
```

The example prints each call. With these settings, the first two calls fail and
the third succeeds:

```text
Attempt 1
Attempt 2
Attempt 3
Task completed
```

Set `--delay` to add a pause between calls:

```bash
python3 main.py --attempts 4 --failures 2 --delay 0.5
```

## Use it in Python

```python
from retry_helper import retry

result = retry(read_data, attempts=3, retry_on=(OSError,))
```

## Run the tests

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

## Limits

The helper runs calls one at a time and uses a fixed delay. It does not add
exponential backoff, random jitter, timeouts, or asynchronous support. Retrying
an operation that changes data can repeat part of that operation, so the caller
must decide whether another attempt is safe.
