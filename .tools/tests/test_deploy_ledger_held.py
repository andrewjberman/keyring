#!/usr/bin/env python3
"""Planted-mutant battery for the deploy-ledger HELD state (NFRA_DEPLOYLEDGER.HELD-STATE HS-1/HS-2/HS-4).

WARNING: SEALED FIXTURES ONLY. STATE_DIR, CM_DIR *and* COO_INBOX are redirected into a temp tree before
anything runs, so no live ledger is mutated and NO ALERT EVER REACHES A REAL INBOX. A battery that
spams a peer's inbox to prove a point has broken something more expensive than it verified.

Both directions are exercised, per HS-4:
  (a) a HELD whose re-read DATE has passed  -> fires HELD-PAST-REREAD (its own class)
  (b) a HELD missing its re-read condition  -> refused, stays RED

Run: python .tools/tests/test_deploy_ledger_held.py
"""
from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
from pathlib import Path

_WS = Path(__file__).resolve().parent.parent.parent
dl = None   # the spec-loaded deploy_ledger module; set inside _run_battery(), never at import

PASS = FAIL = 0
ARMS: list[str] = []


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        ARMS.append("  PASS  %s" % name)
    else:
        FAIL += 1
        ARMS.append("  FAIL  %s   %s" % (name, detail))


def mk(slug, reread, held_days=1.0):
    """A ledger whose APPLY legs are all proven and whose only open leg is a verify leg --
    i.e. structurally eligible for HELD. The ONLY variable across arms is `reread`."""
    held_at = (datetime.now(timezone.utc) - timedelta(days=held_days)).isoformat()
    gate = {"type": "external", "ref": "a specifically named third-party dependency"}
    if reread is not None:
        gate["reread"] = reread
    return {
        "slug": slug, "title": "fixture " + slug, "author": "0.8.0_AE_CloudComp",
        "opened_at": held_at, "held_at": held_at, "window_hours": 4.0,
        "status": dl.HELD_STATUS, "gate": gate,
        "entry_path": str(dl.CM_DIR / (slug + ".md")),
        "legs": [{"id": "apply", "kind": "git", "proof": "sha123"},
                 {"id": "L4", "kind": "verify"}],
    }


_RAN = False


def _run_battery():
    """EVERY piece of work the battery does lives here, so IMPORT IS INERT (the T-16 pass-2 shape,
    03cf4d17ac; NFRA_COMPEFFICACY F6, 92794). Called once per process by test_all_arms_pass (pytest)
    or _report (direct). Before this, deploy_ledger.py was spec-loaded and a temp tree built at import, and every arm ran at import."""
    global _RAN
    if _RAN:
        return
    _RAN = True
    global dl
    spec = importlib.util.spec_from_file_location("dl", _WS / ".tools" / "deploy_ledger.py")
    dl = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dl)

    TMP = Path(tempfile.mkdtemp())
    dl.STATE_DIR = TMP / "open_deploys"
    dl.CM_DIR = TMP / "change_management"
    dl.COO_INBOX = TMP / "coo_inbox"          # <- nothing may reach a real inbox
    for d in (dl.STATE_DIR, dl.CM_DIR, dl.COO_INBOX):
        d.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------------------- HS-1 predicate arms
    ok, why = dl._qualifies_as_held(mk("clean", {"kind": "event", "value": "Andrew's word"}))
    check("HS-1 negative control: a well-formed event-gated HELD qualifies", ok, why)

    ok, why = dl._qualifies_as_held(mk("clean-date", {"kind": "date", "value": "2026-12-31"}))
    check("HS-1 negative control: a well-formed date-gated HELD qualifies", ok, why)

    ok, why = dl._qualifies_as_held(mk("no-reread", None))
    check("HS-1 MUTANT (b) reason-less/re-read-less HELD is REFUSED", not ok, why)
    check("HS-1 the refusal NAMES the missing condition", "re-read condition" in why, why)

    ok, why = dl._qualifies_as_held(mk("bad-kind", {"kind": "someday", "value": "x"}))
    check("HS-1 MUTANT: an off-enum reread.kind is REFUSED", not ok, why)

    ok, why = dl._qualifies_as_held(mk("empty-val", {"kind": "event", "value": "   "}))
    check("HS-1 MUTANT: an EMPTY reread.value is REFUSED (blank is not a claim)", not ok, why)

    ok, why = dl._qualifies_as_held(mk("bad-date", {"kind": "date", "value": "next tuesday"}))
    check("HS-1 MUTANT: kind=date with non-ISO value is REFUSED", not ok, why)

    # the anti-escape-hatch must still hold WITH the new clause present
    half = mk("half-landed", {"kind": "event", "value": "Andrew's word"})
    half["legs"][0].pop("proof")
    ok, why = dl._qualifies_as_held(half)
    check("HS-1 the ORIGINAL anti-escape-hatch still fires (open APPLY leg cannot claim HELD)",
          not ok and "APPLY" in why, why)


    # --------------------------------------------------------------- HS-2 check() arms
    class A:
        red = False
        window_hours = None
        held_stale_days = dl.DEFAULT_HELD_STALE_DAYS


    def run_check(states):
        for f in dl.STATE_DIR.glob("*.json"):
            f.unlink()
        for st in states:
            (dl.STATE_DIR / (st["slug"] + ".json")).write_text(json.dumps(st), encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            try:
                dl.cmd_check(A())
            except SystemExit:
                pass
        return buf.getvalue()


    past = (datetime.now(timezone.utc) - timedelta(days=3)).strftime("%Y-%m-%d")
    future = (datetime.now(timezone.utc) + timedelta(days=90)).strftime("%Y-%m-%d")

    out = run_check([mk("past-reread", {"kind": "date", "value": past}, held_days=1.0)])
    check("HS-2 MUTANT (a) re-read date in the PAST fires HELD-PAST-REREAD",
          "HELD-PAST-REREAD" in out, out.strip()[:200])
    check("HS-2 (a) the line is NOT an aged OPEN and NOT HELD-STALE",
          "HELD-PAST-REREAD" in out and "\nOPEN: past-reread" not in out and "HELD-STALE" not in out,
          out.strip()[:200])
    check("HS-2 (a) the row quotes the date the HOLD ITSELF stated",
          past in out and "re-read-due" in out, out.strip()[:200])

    out = run_check([mk("future-reread", {"kind": "date", "value": future}, held_days=1.0)])
    check("HS-2 negative control: a re-read date in the FUTURE stays plain HELD",
          "HELD:" in out and "HELD-PAST-REREAD" not in out, out.strip()[:200])

    out = run_check([mk("event-gated", {"kind": "event", "value": "Andrew's word"}, held_days=99.0)])
    check("HS-2 an EVENT-gated hold NEVER fires HELD-PAST-REREAD (it cannot go past a date)",
          "HELD-PAST-REREAD" not in out, out.strip()[:200])
    check("HS-2 the event-gated hold re-surfaces on the AGE cadence instead, event printed",
          "HELD-STALE" in out and "Andrew's word" in out, out.strip()[:200])

    out = run_check([mk("no-reread-red", None, held_days=99.0)])
    check("HS-2 MUTANT (b) a re-read-less HELD falls through to RED/OPEN, not HELD",
          "OPEN: no-reread-red" in out and "HELD-CLAIM REJECTED" in out, out.strip()[:250])

    # --------------------------------------------------------------- moratorium
    inbox_writes = list(dl.COO_INBOX.glob("*"))
    check("NO NOTIFICATION: the new class wrote NOTHING to any inbox (moratorium honoured)",
          not inbox_writes, "unexpected inbox writes: %s" % [p.name for p in inbox_writes])

    src = (_WS / ".tools" / "deploy_ledger.py").read_text(encoding="utf-8")
    blk = src.split("HELD-PAST-REREAD:")[0].split("past_reread = False")[-1]
    check("NO NOTIFICATION: the HELD-PAST-REREAD branch contains no alert/nudge call",
          "_held_nudge_alert" not in blk and "_red_alert" not in blk,
          "an alert call inside the new branch would breach the moratorium")


def _report() -> int:
    _run_battery()
    print("deploy-ledger HELD-STATE planted-mutant battery")
    print("\n".join(ARMS))
    print()
    print("ARMS: %d passed / %d failed / %d total" % (PASS, FAIL, PASS + FAIL))
    return 1 if FAIL else 0


def test_all_arms_pass():
    _run_battery()
    failed = [a.strip() for a in ARMS if a.startswith("  FAIL")]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), PASS + FAIL, failed)
    print("ARMS: %d passed / %d failed / %d total" % (PASS, FAIL, PASS + FAIL))


if __name__ == "__main__":
    sys.exit(_report())
