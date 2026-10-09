"""MDPF_DEMQUE round 7, DQ-t-23 criterion AC2: `python data/mdpf/scripts/demque/quote_vs_actual.py --all` reads EVERY frozen quote file
under requests/ (one JSON line each, rc 0, no traceback). The count of lines must equal the count of requests/*.quote.json files, and
the SECHIST card's older-shape quote reads verdict "UNQUOTED". QALL-OK; else QALL-BAD <reason>.
"""
from __future__ import annotations

import glob
import json
import os
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "quote_vs_actual.py")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")

if __name__ == "__main__":
    n = len(glob.glob(os.path.join(REQ, "*.quote.json")))
    r = subprocess.run([sys.executable, MOD, "--all"], capture_output=True, text=True, timeout=100, check=False)
    print(r.stdout[-2500:] + r.stderr[-800:])
    rows = [json.loads(ln) for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    sech = [x for x in rows if str(x.get("request_id", "")).startswith("MDPF_SECHIST-CARD-A")]
    if r.returncode != 0 or "Traceback" in r.stderr or len(rows) != n or not sech or sech[0].get("verdict") != "UNQUOTED":
        print("QALL-BAD rc=%d lines=%d of %d quote files; sechist=%r" % (r.returncode, len(rows), n, sech[:1]))
        sys.exit(1)
    print("QALL-OK %d of %d quote files read" % (len(rows), n))
    sys.exit(0)
