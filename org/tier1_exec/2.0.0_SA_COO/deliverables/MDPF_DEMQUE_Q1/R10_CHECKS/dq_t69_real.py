"""MDPF_DEMQUE DQ-t-69 criterion AC2 (read-only, no network, no vendor): the REAL allowance file and the REAL surface-C request, quoted through the
real bbg_quote CLI for the Saturday 2026-10-17 with nothing drawn.
SURF-OK when: (1) the real request org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-C1-CLOSE-OWED-REST-20261017.json (surface C, 93,104 cells)
quotes allowance_today 400000 and finish_date 2026-10-17; (2) the NEGATIVE ARM, the same request with its "surface" member removed (a temp copy),
quotes allowance_today 5858 (the history ceiling, unchanged) and a finish_date later than 2026-10-17. Else SURF-BAD <why>. Run from the worktree root.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

REAL = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests", "ETFS_RIVALS-C1-CLOSE-OWED-REST-20261017.json")
QUOTE = os.path.join("data", "mdpf", "scripts", "demque", "bbg_quote.py")


def bad(why: str) -> int:
    print("SURF-BAD " + why)
    return 1


def quote(path: str) -> dict:
    r = subprocess.run([sys.executable, QUOTE, "--quote", path, "--today", "2026-10-17"], capture_output=True, text=True, timeout=100, check=False)
    if r.returncode != 0:
        raise RuntimeError("bbg_quote rc=%d: %s" % (r.returncode, (r.stderr or r.stdout)[-300:]))
    return json.loads(r.stdout.strip().splitlines()[-1])


def main() -> int:
    if not os.path.isfile(REAL):
        return bad("no file " + REAL)
    req = json.load(open(REAL, encoding="utf-8"))
    if req.get("surface") != "C":
        return bad("the real request does not carry surface C: %r" % (req.get("surface"),))
    try:
        q = quote(REAL)
        if q.get("allowance_today") != 400000:
            return bad("surface-C request allowance_today is %r, not 400000" % (q.get("allowance_today"),))
        if q.get("finish_date") != "2026-10-17":
            return bad("surface-C request finish_date is %r, not 2026-10-17" % (q.get("finish_date"),))
        del req["surface"]
        with tempfile.TemporaryDirectory() as tmp:
            p = os.path.join(tmp, "untagged.json")
            json.dump(req, open(p, "w", encoding="utf-8"))
            n = quote(p)
        if n.get("allowance_today") != 5858:
            return bad("untagged copy allowance_today is %r, not 5858" % (n.get("allowance_today"),))
        if not n.get("finish_date") or n["finish_date"] <= "2026-10-17":
            return bad("untagged copy finish_date is %r, not later than 2026-10-17" % (n.get("finish_date"),))
    except Exception as exc:  # a failed read is BAD, never an error
        return bad("%s: %s" % (type(exc).__name__, exc))
    print("SURF-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
