#!/usr/bin/env python3
"""Planted-mutant battery: a deploy-ledger re-render keeps hand-written prose (NFRA_MCPORTAL-Z-S24; 1.0.0_SA_CTO~Z msg 32830).

`hold` and `close-leg` re-render the change_management entry from the sentinel. Before the fix only `## Sign-off` survived,
so MP-x-4's entry fell from 137 lines to 23 at rc=0 (ca9b6c05f0..b8fc617e2e). Every arm here writes an entry, re-renders it
through the module's own _write_entry, and re-reads the file against its prior text.

SEALED: WORKSPACE, STATE_DIR, CM_DIR and COO_INBOX are redirected into a temp tree; no live ledger is touched.
Run: python .tools/tests/test_deploy_ledger_prose_carry.py      LAST line  PROSE-CARRY cases=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

_WS = Path(__file__).resolve().parent.parent.parent
CASES: list = []


def rec(name, ok, detail=""):
    CASES.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, ("   " + detail) if (detail and not ok) else ""))


def load():
    spec = importlib.util.spec_from_file_location("deploy_ledger_under_test", _WS / ".tools" / "deploy_ledger.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def state(slug, legs_closed=0):
    legs = [{"id": "L%d" % i, "kind": "apply", "target": "t%d" % i, "proof_required": "rc0",
             "proof": ("ok%d" % i) if i <= legs_closed else None, "closed_at": "2026-10-09T12:00:00Z" if i <= legs_closed else None}
            for i in (1, 2)]
    return {"slug": slug, "status": "OPEN", "opened_at": "2026-10-09T10:00:00+00:00", "title": "T", "author": "a",
            "window_hours": 4.0, "entry_path": "org/critical_paths/change_management/%s.md" % slug, "legs": legs,
            "log": ["opened"]}


def main() -> int:
    dl = load()
    tmp = Path(tempfile.mkdtemp(prefix="dl_prose_carry_"))
    dl.WORKSPACE = tmp
    dl.CM_DIR = tmp / "org" / "critical_paths" / "change_management"
    dl.STATE_DIR = tmp / "org" / "critical_paths" / ".open_deploys"
    dl.COO_INBOX = tmp / "inbox"
    dl.CM_DIR.mkdir(parents=True)

    s = state("arm")
    entry = tmp / s["entry_path"]
    dl._write_entry(s)
    base = entry.read_text(encoding="utf-8")
    hand = (base.rstrip("\n") + "\n- HAND: recorded the plan sha 1f2e3d per the order\n"
            "\n## Sign-off\n\nCTO half signed @abc123\n\n## Preflight evidence\n\nterraform plan: 0 to add, 1 to change\n"
            "census 4 of 4 functions\n")
    hand = hand.replace("**Window:**", "PREAMBLE HAND NOTE: started from the bastion\n**Window:**", 1)
    entry.write_text(hand, encoding="utf-8", newline="\n")

    s["legs"][0]["proof"], s["legs"][0]["closed_at"] = "ok1", "2026-10-09T12:00:00Z"     # a close-leg
    s["log"].append("L1 closed")
    dl._write_entry(s)
    one = entry.read_text(encoding="utf-8")
    for needle in ("- HAND: recorded the plan sha 1f2e3d per the order", "## Sign-off", "CTO half signed @abc123",
                   "## Preflight evidence", "terraform plan: 0 to add, 1 to change", "census 4 of 4 functions",
                   "PREAMBLE HAND NOTE: started from the bastion"):
        rec("close-leg keeps %r" % needle[:40], needle in one)
    rec("the manifest row regenerated (L1 now CLOSED, no stale OPEN row kept)", "| L1 | apply | t1 | rc0 | ok1 | CLOSED" in one
        and one.count("| L1 |") == 1)
    rec("the status line is still the first one (drift reader unaffected)", one.splitlines()[2].startswith("**Status:** OPEN"))

    s["status"], s["gate"], s["held_at"] = "HELD", {"type": "external", "ref": "OG-ap-4"}, "2026-10-09T13:00:00Z"   # a hold
    dl._write_entry(s)
    two = entry.read_text(encoding="utf-8")
    dl._write_entry(s)
    three = entry.read_text(encoding="utf-8")
    rec("hold keeps every hand line", all(n in two for n in ("- HAND: recorded", "CTO half signed", "census 4 of 4",
                                                            "PREAMBLE HAND NOTE")))
    rec("re-render is idempotent (a second identical render changes nothing)", two == three)
    rec("no hand line duplicated across three renders", three.count("- HAND: recorded the plan sha") == 1
        and three.count("PREAMBLE HAND NOTE") == 1 and three.count("## Sign-off") == 1)
    rec("the new status is rendered", "**Status:** HELD" in three)

    # REAL-SHAPE regression: replay MP-x-4's prior entry (ca9b6c05f0) through a hold re-render.
    rel = "org/critical_paths/change_management/20261009T1414Z_nfra-mcportal-r5-control-plane-release_deploy_completion.md"
    srel = "org/critical_paths/.open_deploys/nfra-mcportal-r5-control-plane-release.json"
    try:
        old = subprocess.run(["git", "-C", str(_WS), "show", "ca9b6c05f0:" + rel], capture_output=True, text=True,
                             encoding="utf-8", timeout=30).stdout
        after = subprocess.run(["git", "-C", str(_WS), "show", "b8fc617e2e:" + srel], capture_output=True, text=True,
                               encoding="utf-8", timeout=30).stdout
    except (OSError, subprocess.SubprocessError):
        old, after = "", ""
    if old and after:
        import json
        st = json.loads(after)
        st["entry_path"] = "org/critical_paths/change_management/mp-x-4.md"
        (tmp / st["entry_path"]).write_text(old, encoding="utf-8", newline="\n")
        dl._write_entry(st)
        new = (tmp / st["entry_path"]).read_text(encoding="utf-8")
        lost = [ln for ln in old.splitlines() if ln.strip() and not ln.strip().startswith("|")
                and not any(ln.strip().startswith(g) for g in dl._GENERATED_PREAMBLE) and ln not in new.splitlines()]
        rec("MP-x-4 real entry: no hand line lost on the hold re-render (was 137 -> 23)", not lost,
            "%d lost, e.g. %r" % (len(lost), lost[:2]))
        print("  MP-x-4 lines: prior=%d after-fix=%d (before the fix: 23)" % (len(old.splitlines()), len(new.splitlines())))
    else:
        print("SKIP MP-x-4 real-shape replay: git objects not readable here (not counted)")
    ok = all(CASES)
    print("PROSE-CARRY cases=%d/%d ok=%s" % (sum(CASES), len(CASES), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
