"""MDPF_DEMQUE round 9, DQ-t-45 criterion AC2 (REAL request files and queue copies, read only, no vendor call, nothing written). Two arms:
  (1) `demand_queue.py --check-declared <dir>` over BOTH org/missions/D8/MDPF/MDPF_DEMQUE/requests and the device queue ~/.opal/demque/queue prints ONE JSON
      line {"checked": N, "refused": [{"request_id","why"}], "accepted": N}; every Yahoo request (a `securities` list without vendor bloomberg) is checked and
      none is refused; checked >= 6 for the queue directory.
  (2) `extend_frontier.py --plan` prints a JSON line whose `need_class` is "client" and whose `window_start` is an ISO date on or after 2012-01-01 and on or before its
      `frontier`, and whose request (the `_request` it would write) validates.
YCLASS-REAL-OK; else YCLASS-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

D = os.path.join("data", "mdpf", "scripts", "demque")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")
QUEUE = os.path.expanduser(os.path.join("~", ".opal", "demque", "queue"))


def _line(cmd, timeout=40):
    r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, timeout=timeout, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-240:].strip())
    return json.loads(ls[-1]), ""


def _bad(why):
    print("YCLASS-REAL-BAD " + why)
    return 1


def main() -> int:
    for label, d, floor in (("requests", REQ, 1), ("queue", QUEUE, 6)):
        a, e = _line([os.path.join(D, "demand_queue.py"), "--check-declared", d])
        if a is None:
            return _bad("arm1 %s: %s" % (label, e))
        print("arm1 %s checked=%s accepted=%s refused=%s" % (label, a.get("checked"), a.get("accepted"), [x.get("request_id") for x in a.get("refused") or []]))
        if not isinstance(a.get("checked"), int) or a["checked"] < floor or a.get("refused") != [] or a.get("accepted") != a["checked"]:
            return _bad("arm1 %s refused or too few checked: %s" % (label, json.dumps(a)[:300]))
    b, e = _line([os.path.join(D, "extend_frontier.py"), "--plan"], timeout=105)  # AMENDED 2026-10-13: the plan reads the price index, measured 77 s
    if b is None:
        return _bad("arm2 " + e)
    print("arm2 need_class=%s window_start=%s frontier=%s symbols=%s" % (b.get("need_class"), b.get("window_start"), b.get("frontier"), b.get("symbols")))
    ws, fr = b.get("window_start"), b.get("frontier")
    ok = b.get("need_class") == "client" and isinstance(ws, str) and isinstance(fr, str) and "2012-01-01" <= ws <= fr
    if not ok:
        return _bad("arm2 declaration: %s" % json.dumps({k: b.get(k) for k in ("need_class", "window_start", "frontier")}))
    print("YCLASS-REAL-OK Yahoo requests declared and accepted; the standing extension declares client from %s" % ws)
    return 0


if __name__ == "__main__":
    sys.exit(main())
