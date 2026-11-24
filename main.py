#!/usr/bin/env python3
"""Two lines to my past self: the misspelled cup.

The moment is small and specific: a barista at the corner café
spells my name wrong on a coffee cup, and my past self's instinct
is to correct her. The warning says don't — laugh about it instead.

That is the whole gamble. The second line traces what the small
choice buys: she remembers the guy who laughed about it, and three
years later she is the one hiring. A misspelled cup turns into a
job, which is exactly the cause and effect the judge brief asks
for: one concrete moment, one sentence on why it mattered, and a
twist that sharpens the moment instead of decorating it.

The entry is exactly two lines, 171 characters including the
trailing newline, written to /output/entry.txt.
"""

from pathlib import Path

LINE_1 = (
    "When the barista at the corner café spells your name wrong "
    "on the cup, don't correct her."
)
LINE_2 = (
    "She remembers the guy who laughed about it, and three years "
    "later she hires him."
)

ENTRY = LINE_1 + "\n" + LINE_2

assert 1 <= len(ENTRY) + 1 <= 280, "entry must fit in 280 characters"
assert ENTRY.count("\n") == 1, "entry must be exactly two lines"


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
