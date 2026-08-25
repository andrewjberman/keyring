#!/usr/bin/env python3
"""safe_commit_msg_verify -- the -F message self-verify safe-commit runs on ITS OWN new hash.

Andrew-direct 2026-08-24 ~23:5xZ (COO record @91011a1a1d): "seems to me like the 'checker'
should have that built in." safe-commit is the only actor holding both the message file and
its own commit hash at the moment of the act; every after-the-fact form broke on a
reconstruction step -- flag spelling (%B vs pretty=format:%B disagree by exactly one byte),
a peer's HEAD in a 15-seat shared worktree (two false hash claims in one night), or newline
normalisation (four control variants falsified in an hour, LD-0449).

BOTH sides get git's own `-F` cleanup transform (cleanup=whitespace, MEASURED 2026-08-25 in a
probe repo): per-line trailing-whitespace strip, blank RUNS collapsed to one, leading/trailing
blank lines stripped, `#` lines KEPT. Anything weaker false-alarms on a trailing space -- the
fifth-checker fate this file exists to end.

Usage: safe_commit_msg_verify.py <msgfile> <commit-hash>
Exit 0 = MATCH (prints length). Exit 1 = MISMATCH (prints first differing index + both
contexts). Exit 2 = usage/read error. Never edits anything.
"""
from __future__ import annotations

import subprocess
import sys


def clean(bts: bytes) -> bytes:
    lines = [ln.rstrip() for ln in bts.replace(b"\r\n", b"\n").split(b"\n")]
    out: list[bytes] = []
    prev_blank = False
    for ln in lines:
        blank = ln == b""
        if blank and prev_blank:
            continue
        out.append(ln)
        prev_blank = blank
    while out and out[0] == b"":
        out.pop(0)
    while out and out[-1] == b"":
        out.pop()
    return b"\n".join(out)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: safe_commit_msg_verify.py <msgfile> <commit-hash>")
        return 2
    f, h = sys.argv[1], sys.argv[2]
    try:
        disk = clean(open(f, "rb").read())
    except OSError as exc:
        print("READ-ERROR on msgfile: %s" % exc)
        return 2
    raw = subprocess.run(["git", "cat-file", "commit", h], capture_output=True).stdout
    if b"\n\n" not in raw:
        print("READ-ERROR: git cat-file returned no message body for %s" % h)
        return 2
    msg = clean(raw.split(b"\n\n", 1)[1])
    if disk == msg:
        print("MATCH len=%d" % len(msg))
        return 0
    n = min(len(disk), len(msg))
    i = next((k for k in range(n) if disk[k] != msg[k]), n)
    print("MISMATCH first-diff-index=%d file-len=%d commit-len=%d" % (i, len(disk), len(msg)))
    print("  file..: %r" % disk[max(0, i - 30):i + 30])
    print("  commit: %r" % msg[max(0, i - 30):i + 30])
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
