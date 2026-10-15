"""MDPF_DEMQUE round 9, DQ-t-66 criterion AC2 (REAL S3 price index and the V2 active set: READ ONLY, NO vendor call, writes nothing).

`extend_frontier.py --plan` (the day's standing request over the store's landed names) must now leave every V2-held name out: its JSON line carries the integer key excluded_active > 0,
a securities list of 1..380 entries none of whose CUSIPs is in the V2 active set, symbols == len(securities), and excluded_p2 == 0 and excluded_p3 == 0 (the Yahoo gate no longer uses P2/P3).
`extend_frontier.py --plan-week --from 2026-10-19 --days 10` must print max_requests <= 380 and excluded_active > 0.
GATE-REAL-OK; else GATE-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

D = os.path.join("data", "mdpf", "scripts", "demque")


def _bad(why):
    print("GATE-REAL-BAD " + why)
    return 1


def _run(*args):
    env = dict(os.environ)
    env["PYTHONPATH"] = os.getcwd()
    r = subprocess.run([sys.executable, os.path.join(D, "extend_frontier.py")] + list(args), capture_output=True, text=True,
                       timeout=200, check=False, env=env)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def main() -> int:
    sys.path.insert(0, D)
    import active_set  # noqa: E402
    v2 = set(active_set.load().keys())
    p, e = _run("--plan")
    if p is None:
        return _bad("--plan " + e)
    secs = p.get("securities")
    ea = p.get("excluded_active")
    print("plan symbols=%s excluded_active=%s excluded_p2=%s excluded_p3=%s" % (p.get("symbols"), ea, p.get("excluded_p2"), p.get("excluded_p3")))
    if type(ea) is not int or ea <= 0:
        return _bad("excluded_active is missing or not above 0")
    if not isinstance(secs, list) or not (1 <= len(secs) <= 380) or p.get("symbols") != len(secs):
        return _bad("the securities list is not 1..380 entries equal to symbols")
    if {s.get("cusip") for s in secs} & v2:
        return _bad("a V2 active-set CUSIP is in the day's request")
    if p.get("excluded_p2") != 0 or p.get("excluded_p3") != 0:
        return _bad("excluded_p2 or excluded_p3 is not 0")
    w, e = _run("--plan-week", "--from", "2026-10-19", "--days", "10")
    if w is None:
        return _bad("--plan-week " + e)
    print("week max_requests=%s excluded_active=%s" % (w.get("max_requests"), w.get("excluded_active")))
    if not (type(w.get("max_requests")) is int and w["max_requests"] <= 380) or type(w.get("excluded_active")) is not int or w["excluded_active"] <= 0:
        return _bad("the week's max_requests is over 380 or excluded_active is missing")
    print("GATE-REAL-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
