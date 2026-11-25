#!/usr/bin/env python3
"""The One-Liner Groan-Off — write one original dad joke to /output/entry.txt.

The joke: a dad "fixes" the Wi-Fi with duct tape and total confidence.
The pun is the turn and lands in the last words: "stick around".
"""

import os

JOKE = "Dad fixed the Wi-Fi with duct tape \u2014 he said the signal just needed to stick around."

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the competition rules: entry.txt must be UTF-8 text of
# 1 to 140 characters, a single line, not only whitespace.
MAX_CHARS = 140
MAX_BYTES = 140


def validate(line):
    """Check the entry against the gate: one line, 1-140 chars, not blank."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry exceeds {MAX_CHARS} characters")
    if len(line.encode("utf-8")) > MAX_BYTES:
        raise ValueError(f"entry exceeds {MAX_BYTES} bytes")
    return line


def main():
    line = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
