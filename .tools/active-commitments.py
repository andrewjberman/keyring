#!/usr/bin/env python3
"""active-commitments -- print every seat's recent promised work from its .active-commitments ledger. Awareness only.

Andrew-direct 2026-09-24 ~18:4xZ (record org/tier1_exec/4.0.0_SA_CRO/deliverables/
ANDREW_DIRECT_20260924_184xZ_SELF_DRIVE_READS_ACTIVE_COMMITMENTS.md): /self-drive and /stimulus-scan read these ledgers
so the CTO sees what the fabric has promised. Nothing is refused on what this prints.

The ledgers are org/mcp/inbox/<base>/.active-commitments and org/mcp/inbox/<base>/~<lane>/.active-commitments, one
`<ISO time>|<text>` line per promise. The promise detector appends and nothing pops, so lines accumulate. This reader
filters by age (default: the last 24 hours) and prints the denominators it read.

  active-commitments.py [--hours N] [--per-seat K]
"""
import datetime as dt
import glob
import os
import sys


def main(argv):
    hours, per_seat = 24.0, 5
    if "--hours" in argv:
        hours = float(argv[argv.index("--hours") + 1])
    if "--per-seat" in argv:
        per_seat = int(argv[argv.index("--per-seat") + 1])
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cut = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
    files = sorted(glob.glob(os.path.join(root, "org", "mcp", "inbox", "*", ".active-commitments"))
                   + glob.glob(os.path.join(root, "org", "mcp", "inbox", "*", "~*", ".active-commitments")))
    total, recent, shown = 0, 0, []
    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            lines = [ln for ln in fh.read().splitlines() if ln.strip()]
        total += len(lines)
        new = [ln for ln in lines if ln[:20] >= cut]
        recent += len(new)
        if new:
            seat = os.path.relpath(os.path.dirname(f), os.path.join(root, "org", "mcp", "inbox")).replace("\\", "/")
            shown.append((seat, new))
    print("ACTIVE COMMITMENTS since %s: %d line(s) in %d of %d ledger(s); %d lines total (awareness only)"
          % (cut, recent, len(shown), len(files), total))
    for seat, new in shown:
        print("  %s  (%d)" % (seat, len(new)))
        for ln in new[-per_seat:]:
            print("    " + ln[:200])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
