#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1).

Writes the one-line roast to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). The line is at most 140 characters, plain text, no
trailing newline. Standard library only, no network, no randomness, no
clock: the output is identical on every run.
"""

import os
import sys
from pathlib import Path

ENTRY = "My agent's idea of a fix is a five-paragraph apology and the same bug, now with comments."

MAX_CHARS = 140


def output_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> int:
    if not ENTRY.strip():
        print("entry is empty or whitespace only", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(f"entry is {len(ENTRY)} characters, over the {MAX_CHARS} gate", file=sys.stderr)
        return 1
    out_path = output_path()
    out_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
