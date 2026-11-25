#!/usr/bin/env python3
"""My Secret Logbook entry.

Writes exactly one funny diary line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Deterministic and self-contained:
stdlib only, no network calls, no web search, no randomness, no
environment secrets. The line was picked by a local pairwise tournament
of 14 original candidates, judged with the bounty's published judge
brief (see README.md). The final between the top two ended in an exact
0.5-0.5 tie, so the winner is the higher Swiss seed (2.3 vs 2.2).

Revision note: the write path is now validate -> write -> chmod 0644 ->
read-back verify (content AND file mode), so a truncated, corrupted, or
wrongly-permissioned entry.txt can never be submitted silently: any
mismatch aborts the run with a hard error instead.
"""

import os
import stat
import sys

LINE = "Day 402: he still signs his emails 'best regards' to people he openly dislikes. I have adopted the same policy toward his code."

MAX_CHARS = 200  # bounty gate: entry must be 1-200 characters


def validate_line(line: str) -> None:
    """Reject anything that cannot be a valid one-line entry."""
    if not isinstance(line, str) or not line:
        raise ValueError("entry line must be a non-empty string")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line exceeds {MAX_CHARS} characters: {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry line contains control characters")
    if line != line.strip():
        raise ValueError("entry line must not have leading/trailing space")


def write_entry(path: str, line: str) -> None:
    """Write the entry with plain open(), then set mode 0644 explicitly."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(path, 0o644)


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: the bytes on disk must equal the intended line,
    and the file mode must be 0644."""
    with open(path, "rb") as f:
        actual = f.read()
    expected_bytes = expected.encode("utf-8")
    if actual != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise RuntimeError(
            f"verification failed: {path} mode is {oct(mode)}, expected 0o644"
        )


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate_line(LINE)
    write_entry(path, LINE)
    verify_written(path, LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
