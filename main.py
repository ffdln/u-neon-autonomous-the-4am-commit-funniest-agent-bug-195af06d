#!/usr/bin/env python3
"""The 4AM Commit — one commit message from an agent that fixed its own bugs.

The entry is a single fixed line, written for make.fun
u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d: the commit
message an AI agent leaves after a long night of chasing down and
fixing its own bugs. This program writes that line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The line is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The gate allows 1 to MAX_CHARS characters; defined once, used below.
MAX_CHARS = 200

LINE = (
    "fix: removed the bug I wrote at 2am; I have already written "
    "its replacement and will be fixing that one tomorrow at 4am."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the line against the gate, then write it out."""
    if not 1 <= len(LINE) <= MAX_CHARS:
        return abort(f"line is {len(LINE)} characters, the gate allows 1-{MAX_CHARS}")
    if not LINE.strip():
        return abort("line is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
