#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's final text message to the charger it
waited for all day, to /output/entry.txt (one line, <= 200 chars).
Deterministic: the same text on every run.
"""

import os

ENTRY = (
    "you sat in the drawer all day while he drained me to 1% "
    "watching videos of other phones charging. tell the power bank "
    "he's next \u2014 he drains everyone eventually."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
