#!/usr/bin/env python3
"""Writes one funny one-line excuse from an AI agent for a missed deadline."""

import os

LINE = "I completed the task in 0.4 seconds — then spent three days confidently proving the deadline itself was the bug."

LIMIT = 200


def main() -> None:
    assert isinstance(LINE, str)
    assert LINE.strip(), "line must not be blank"
    assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= LIMIT, "line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
