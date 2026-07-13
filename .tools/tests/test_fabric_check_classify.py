"""Exercise fabric-check's classify_declared(). Rule 22a: acceptance rests on it FIRING/PASSING.

THE REGRESSION THIS PINS (COO, 2026-07-13): the classifier scored the SUBSTRING "blocked on" --
inside the words "NOTHING BLOCKED ON ME" -- as a BLOCK, and flagged two healthy agents. The failure
was ANTI-CORRELATED with the truth: the more explicitly an agent declared itself unblocked, the more
certainly it tripped, while an agent that said nothing passed clean. `blocked>0` is a /drive GATE,
so it taxed exactly the reporting behaviour the fabric wants.

The two REAL summaries that were mis-flagged are the first two tests, verbatim.

AND THE MUTANT BAR: a classifier that never says BLOCKED would pass every negative test here. So the
POSITIVE cases must fire. A gate never observed to fire has not been shown to exist.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_p = Path(__file__).resolve().parents[1] / "fabric-check.py"
_spec = importlib.util.spec_from_file_location("fabric_check", _p)
fc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fc)

PASS = FAIL = 0


def chk(name, summary, want):
    global PASS, FAIL
    got, _ = fc.classify_declared(summary)
    if got == want:
        PASS += 1
        print(f"  PASS  {name:<52} -> {got}")
    else:
        FAIL += 1
        print(f"  FAIL  {name:<52} -> {got} (want {want})")


print("fabric-check classify_declared -- EXERCISED\n")

print("*** THE REGRESSION -- the two REAL summaries that were falsely flagged BLOCKED: ***")
chk("CTO: 'IDLE-AVAILABLE: ... Nothing blocked on me.'",
    "IDLE-AVAILABLE: all AoR blockers RULED (F1 closed; F4/F7/F8 ruled -> DS building). "
    "All 4 gates BUILT+LIVE. Nothing blocked on me.", "IDLE")
chk("CVO~B: 'WORKING: ... F1 class CLOSED ...'",
    "WORKING: AoR gate-2 (LD-0277). F1 class CLOSED; remaining blockers F2/F4/F7 ruled and "
    "with DS. Gate-2 WITHHELD.", "WORKING")

print("\nPOSITIVE -- a REAL block must still FIRE (else the classifier is a no-op):")
chk("BLOCKED: prefix", "BLOCKED: waiting on DS's round-8.2 hash", "BLOCKED")
chk("BLOCKED-SOVEREIGN: prefix", "BLOCKED-SOVEREIGN: needs an Andrew ruling on 49F scope", "SOVEREIGN")
chk("BLOCKED prefix + sovereign in prose", "BLOCKED: awaiting sovereign call on the cutover", "SOVEREIGN")
chk("no token, genuine prose block", "waiting -- blocked on the CVO gate-2 verdict", "BLOCKED")
chk("no token, blocker: phrasing", "blocker: comp-iam cannot model the resource axis", "BLOCKED")

print("\nNEGATION GUARD -- token-less summaries that DECLARE the absence of a block:")
chk("'no blockers' (no token)", "grinding the round-8.2 build, no blockers", "WORKING")
chk("'nothing blocked on me' (no token)", "driving the gate ports, nothing blocked on me", "WORKING")
chk("'unblocked' (no token)", "unblocked and building F7 now", "WORKING")

print("\nPREFIX AUTHORITY -- the token WINS over any prose beneath it:")
chk("WORKING: + heavy blocker prose",
    "WORKING: ruling on the blockers -- blocked on nothing, blocker: none, blocked: no", "WORKING")
chk("IDLE: + blocker prose", "IDLE: available. Prior blockers all cleared.", "IDLE")

print("\nBASELINE:")
chk("empty summary", "", "UNCLEAR")
chk("plain work description", "running the nightly gold chain for INF", "WORKING")

print("\n" + "=" * 66)
print(f"PASS: {PASS}   FAIL: {FAIL}")
if FAIL:
    print("FAILURES -- do NOT ship.")
    sys.exit(1)
print("ALL PASS -- classifies the DECLARED STATE, never a substring of the prose.")
sys.exit(0)
