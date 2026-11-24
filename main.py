#!/usr/bin/env python3
"""Entry program for 'Monday, Reviewed in One Line'.

The whole submission is a one-star review of Monday: it arrived
uninvited, ate the entire weekend, billed the reviewer for the
privilege, and left a 7 a.m. meeting invite on the table as a tip —
so the reviewer has filed a complaint with Tuesday.

The program writes that line to entry.txt inside the directory named
by MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is
where the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

TEXT = (
    "Monday gets one star: it arrived uninvited, ate my entire weekend, "
    "billed me for the privilege, and left a 7 a.m. meeting invite on "
    "the table as a tip. I have filed a formal complaint with Tuesday."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200

def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("review must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
