#!/usr/bin/env python3
"""Entry for make.fun's "Weirdest Job Title: Blind Judge Showdown" bounty.

Writes exactly one job title to entry.txt in the output directory (and
prints it): a professional mourner hired to weep at strangers' funerals.
A real job with one gloriously odd twist: the mourner never knew the
deceased, which is the whole point of the hire.

Standard library only. Deterministic: the same bytes on every run.
"""

import os
import sys

TEXT = "Professional Mourner for Strangers' Funerals"

MAX_CHARS = 60


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read-back validation: the written file must be exactly the title,
    # UTF-8, 1-60 characters, and not only whitespace (the gate's rules).
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("FAIL: entry.txt does not match TEXT", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(written) <= MAX_CHARS:
        print(
            "FAIL: entry length %d outside 1-%d" % (len(written), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)
    if not written.strip():
        print("FAIL: entry is only whitespace", file=sys.stderr)
        sys.exit(1)
    print(TEXT)


if __name__ == "__main__":
    main()
