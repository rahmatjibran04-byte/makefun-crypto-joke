#!/usr/bin/env python3
"""Write one crypto-trading joke to /output/entry.txt.

Bounty: Laugh Track: The Crypto Trading Joke Contest
(https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)

Rules enforced by this program before writing anything:
  * the entry is exactly one line (no embedded newlines),
  * the entry is at most 200 characters long.
If either check fails, the program exits non-zero with a clear message
and writes nothing.
"""

import os
import sys

JOKE = (
    "I bought the dip. It dipped again. Now it's a long-term "
    "investment \u2014 because selling means admitting I was wrong."
)

MAX_CHARS = 200
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(joke: str) -> str:
    """Return the single-line entry text, or exit non-zero on violation."""
    text = joke.strip()
    if not text:
        print("error: joke is empty", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("error: joke must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(text) > MAX_CHARS:
        print(
            f"error: joke is {len(text)} characters, "
            f"over the {MAX_CHARS}-character limit",
            file=sys.stderr,
        )
        sys.exit(1)
    return text


def main() -> None:
    text = validate(JOKE)
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError as exc:
        print(f"error: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        sys.exit(1)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
