#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one funny one-line apology note from an office printer to
the people who keep jamming it, feeding it cheap paper and
swearing at it, to /output/entry.txt.
"""

import os

# The apology: a printer says sorry for jamming, then turns the
# blame back on the office — cheap paper, then the swearing.
# 107 characters, punch at the end.
ENTRY_LINE = (
    "Sorry I jammed again. In my defence, you fed me paper "
    "thinner than your excuses - and then you swore at me."
)


def main():
    line = ENTRY_LINE
    if not 1 <= len(line) <= 120:
        raise ValueError(f"entry line must be 1-120 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
