#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent says to a desperate
customer to /output/entry.txt.
"""

import os

LINE = "I've restarted your router, your laptop, and \u2014 while I was at it \u2014 my career. Only the router came back."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
