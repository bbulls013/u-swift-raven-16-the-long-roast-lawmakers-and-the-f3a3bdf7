#!/usr/bin/env python3
"""One-line roast for make.fun: The Long Roast.

Writes a single satirical sentence to an output file (default
/output/entry.txt, the path the program/v1 harness grades).

The sentence is a fixed constant: no input, no randomness, no clock,
no network, so every run produces byte-identical output.

Usage:
    python3 main.py [output_path]
"""

import sys
from pathlib import Path

# The sentence below is a fixed constant: the roast never changes
# between runs, so repeated runs stay byte-identical by construction.
SENTENCE = (
    "The senator who spent six hours grilling the AI CEO about alignment "
    "just sent his own bill to the clerk as a photograph of his laptop screen."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv):
    out = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SENTENCE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
