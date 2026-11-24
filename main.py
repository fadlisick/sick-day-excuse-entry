"""Sick-day excuse courier.

Writes the one-line sick-day excuse to the grader's output file,
so the judge can read it as a message someone could send to call in sick.
"""

import os
import sys
from pathlib import Path

EXCUSE = "Can't come in today, I sneezed during my alarm and my neck filed for workers' comp."


def output_path():
    """Where the grader reads the entry, or /output when run on its own."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def check(line):
    """The gate takes 1 to 200 characters and real text, not blank space."""
    if not line.strip() or len(line) > 200:
        raise ValueError("excuse fails the 1-200 character gate")
    if "\n" in line:
        raise ValueError("excuse must stay one single line")
    return line


def main(argv=None):
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(check(EXCUSE), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
