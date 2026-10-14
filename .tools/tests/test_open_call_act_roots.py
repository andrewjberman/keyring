#!/usr/bin/env python3
"""Arms for the OPEN-CALL act-row rule of .tools/crossbox-deploy-check.py (NFRA_CTLPLN cell CT-ad-5; CTO ruling on D2-S3).

An open_calls row of kind act (an act only Andrew can do) matches a root ONLY through the roots its own roots field names.
Its project code and a free-text mention of the root do not match it, and a row with no roots matches none. A fork row keeps
every rule it had, a closed row stays ignored, and the kind is compared on its stripped, case-folded value.

Every fixture is written into a temporary directory; no real open-calls file is read or written.

Run: python .tools/tests/test_open_call_act_roots.py   (LAST line: OPEN-CALL-ACT-ROOTS arms=<k>/<n> ok=<True|False>)
"""
import datetime
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import traceback
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("crossbox_deploy_check", str(TOOLS / "crossbox-deploy-check.py"))
cbc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(cbc)

IRPT = "infra/aws/terraform/irpt-status"
OTHER = "infra/aws/terraform/opal-ticket-api"
DATA_ROOT = "data/black_diamond/scripts/silver"
CARRIED = ["data/black_diamond/scripts/silver/x.py"]
NOW = datetime.datetime(2026, 10, 14, 3, 0, 0)
# (code, box, write path, field): IRPT_BCKEND's write set covers the irpt-status root
COVERING = [("IRPT_BCKEND", "dell2", "infra/aws/terraform/investor-reporting", "placement field")]
SUBJECT = "Send the execution ID of your own PROD analysis-request submission"


def row(rid, kind=None, roots=None, state="OPEN", project="IRPT_BCKEND", subject=SUBJECT):
    doc = {"id": rid, "project": project, "subject": subject, "state": state, "opened_at": "2026-10-13T21:47:15Z"}
    if kind is not None:
        doc["kind"] = kind
    if roots is not None:
        doc["roots"] = roots
    return doc


def run_arm(rows, rel, files=None):
    """Write one open_calls.json holding rows into a fresh temporary repo root, then measure it."""
    tmp = tempfile.mkdtemp(prefix="act_roots_")
    try:
        state_dir = os.path.join(tmp, "org", "devices", "state", "dell2")
        os.makedirs(state_dir)
        doc = {"schema": "open-calls/1", "device": "dell2", "written_at": "2026-10-13T22:00:00Z",
               "written_by": "fixture", "rows": rows}
        with open(os.path.join(state_dir, "open_calls.json"), "w", encoding="utf-8") as fh:
            json.dump(doc, fh)
        return cbc.measure_open_call(tmp, rel, COVERING, NOW, files)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# label, rows, root, carried files (None = root-wide), expected matched, substrings the hit text must carry
ARMS = [
    ("a", [row("dell2-a", kind="act")], IRPT, None, 0, []),
    ("b", [row("dell2-b", kind="act", roots=[IRPT])], IRPT, None, 1,
     ["row dell2-b act row names the root in its roots field (infra/aws/terraform/irpt-status)"]),
    ("c", [row("dell2-c", kind="act", roots=[OTHER])], IRPT, None, 0, []),
    ("d", [row("dell2-d", kind="fork")], IRPT, None, 1,
     ["row dell2-d names project IRPT_BCKEND in its project field"]),
    ("e", [row("dell2-e", kind="act", roots=[], subject="Confirm the apply on " + IRPT)], IRPT, None, 0, []),
    ("f", [row("dell2-f", kind="act", roots=[IRPT], state="CLOSED")], IRPT, None, 0, []),
    ("g", [row("dell2-g", kind="act")], DATA_ROOT, CARRIED, 0, []),
    ("h", [row("dell2-h", kind=" Act ")], IRPT, None, 0, []),
]


def main():
    results = []
    for label, rows, rel, files, expect, must in ARMS:
        ok = False
        try:
            hits, lines = run_arm(rows, rel, files)
            text = "\n".join(hits + lines)
            deciding = "OPEN-CALL calls_scanned=%d matched=%d" % (len(rows), expect)
            ok = len(hits) == expect and all(s in text for s in must) and lines[-1] == deciding
            print("ARM %s root=%s kind=%s matched=%d expect=%d ok=%s | %s" % (
                label, rel, rows[0].get("kind", "(none)"), len(hits), expect, ok, lines[-1]))
            for hit in hits:
                print("    hit: %s" % hit)
        except Exception:
            traceback.print_exc()
        results.append(ok)
    k = sum(1 for r in results if r)
    print("OPEN-CALL-ACT-ROOTS arms=%d/%d ok=%s" % (k, len(results), k == len(results)))
    return 0 if k == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
