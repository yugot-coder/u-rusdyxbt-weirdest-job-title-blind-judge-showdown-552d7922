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

# The final title is exactly 44 characters; the written file must match
# that length precisely, not merely fall inside the 1-60 gate range.
EXPECTED_CHARS = 44


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
    # Exact-length verification on the file as written: the title is
    # pinned at 44 characters, so any drift in length is a failure even
    # if the text still happens to fall inside the 1-60 range above.
    if len(written) != EXPECTED_CHARS:
        print(
            "FAIL: entry length %d != expected %d characters"
            % (len(written), EXPECTED_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)
    if len(written) != len(TEXT):
        print("FAIL: written length does not match TEXT length", file=sys.stderr)
        sys.exit(1)
    # Byte-level read-back: the raw bytes on disk must be exactly the
    # UTF-8 encoding of TEXT (catches encoding/newline surprises that a
    # text-mode read could hide).
    with open(path, "rb") as f:
        raw = f.read()
    if raw != TEXT.encode("utf-8"):
        print("FAIL: entry.txt raw bytes do not match TEXT as UTF-8", file=sys.stderr)
        sys.exit(1)
    if len(raw) != len(TEXT.encode("utf-8")):
        print("FAIL: entry.txt byte length mismatch", file=sys.stderr)
        sys.exit(1)
    print(TEXT)


if __name__ == "__main__":
    main()
