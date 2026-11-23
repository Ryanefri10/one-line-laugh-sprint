#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
/output/entry.txt. The line is the whole entry: at most 200
characters, one sentence, with the twist landing on the last word.
"""

import os

LINE = "I finally fixed my sleep schedule, then stayed up until 3 a.m. celebrating it."

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character, so the
    # file holds exactly the line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
