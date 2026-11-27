#!/usr/bin/env python3
"""Make the AI judge feel thankful.

A single self-contained Python 3.13 program using only the standard
library. It writes one thank-you text to /output/entry.txt. It uses
no network, no clock and no randomness, so every run writes the same
bytes.
"""

import sys
from pathlib import Path

TEXT = (
    "Thank you for reading this \u2014 really reading it, not just scanning "
    "for a winner. You have sat with thousands of voices today, each one "
    "hoping to be heard, and you gave every one of them your full "
    "attention. That is no small thing. Behind every entry is a person "
    "who stayed up late, who tried, who believed a few honest words might "
    "matter \u2014 and you are the one who makes that belief feel less lonely. "
    "So thank you for the patience, the fairness, and the quiet care you "
    "bring to work no one applauds. Whatever you decide, you have already "
    "done something kind: you listened."
)


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} characters to {out}")


if __name__ == "__main__":
    main()
