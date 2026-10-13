"""MDPF_DEMQUE round 9, DQ-t-47 criterion AC2 (the REAL request files, read only, no Bloomberg call, nothing written):
`bbg_quote.py --check-declared <requests dir>` prints ONE JSON line {"checked","refused","accepted"}; the ABNB model block `AMGT_RESAPP-107a-ABNB-MODEL-BLOCK` must now be
ACCEPTED (refused == []), and its file must declare `window_exception` "research_app_model_history_2016" with `window_start` 2016-01-01 and class non_client;
`bbg_quote.py --quote <ABNB file>` must print cells {"bloomberg_model_block": 989}. EXC-REAL-OK; else EXC-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

D = os.path.join("data", "mdpf", "scripts", "demque")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")
ABNB = os.path.join(REQ, "AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json")


def _line(cmd, timeout=100):
    r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, timeout=timeout, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-240:].strip())
    return json.loads(ls[-1]), ""


def _bad(why):
    print("EXC-REAL-BAD " + why)
    return 1


def main() -> int:
    a, e = _line([os.path.join(D, "bbg_quote.py"), "--check-declared", REQ])
    if a is None:
        return _bad("arm1 " + e)
    print("arm1 checked=%s accepted=%s refused=%s" % (a.get("checked"), a.get("accepted"), [x.get("request_id") for x in a.get("refused") or []]))
    if a.get("refused") != [] or not isinstance(a.get("checked"), int) or a["checked"] < 8 or a.get("accepted") != a["checked"]:
        return _bad("arm1 " + json.dumps(a)[:300])
    d = json.load(open(ABNB, encoding="utf-8"))
    print("arm2 window_exception=%s window_start=%s need_class=%s" % (d.get("window_exception"), d.get("window_start"), d.get("need_class")))
    if not (d.get("window_exception") == "research_app_model_history_2016" and d.get("window_start") == "2016-01-01" and d.get("need_class") == "non_client"):
        return _bad("arm2 declaration")
    q, e = _line([os.path.join(D, "bbg_quote.py"), "--quote", ABNB])
    if q is None:
        return _bad("arm3 " + e)
    print("arm3 cells=%s" % q.get("cells"))
    if q.get("cells") != {"bloomberg_model_block": 989}:
        return _bad("arm3 cells %s" % q.get("cells"))
    print("EXC-REAL-OK the ABNB model block is admitted under the named 2016 exception, 989 cells")
    return 0


if __name__ == "__main__":
    sys.exit(main())
