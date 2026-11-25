#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent says to a desperate
customer to /output/entry.txt.

The competition gate requires a single line of 1-199 characters, so the
line is checked against that gate before anything is written: a bad line
aborts the run instead of producing an invalid entry.
"""

import os
import sys

LINE = "I've restarted your router, your laptop, and \u2014 while I was at it \u2014 my career. Only the router came back."

MAX_LINE_LENGTH = 199


def check_line(line: str) -> None:
    """Fail loudly if the line breaks the competition gate.

    The gate is one line of 1-199 characters. A newline inside the line,
    an empty line, or anything over the limit means the entry would be
    rejected, so stop here with a clear message instead of writing it.
    """
    if not line:
        sys.exit("error: entry line is empty; expected a single line of 1-199 characters")
    if "\n" in line or "\r" in line:
        sys.exit("error: entry line must be a single line, but it contains a line break")
    if len(line) > MAX_LINE_LENGTH:
        sys.exit(
            f"error: entry line is {len(line)} characters, over the {MAX_LINE_LENGTH}-character limit"
        )


def main() -> None:
    check_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
