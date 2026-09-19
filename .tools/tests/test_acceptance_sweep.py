#!/usr/bin/env python3
"""Battery for `_acceptance_sweep` / `_classify_acceptance` (AMGT-rk-57, row AMGT_RESAPP-Z-S169,
ruling s.3.3 @9c8e04cd9a `:81-85`).

WHAT THIS PROVES: the sweep's PURE classifier is exercised against fixtures (arms 1-4, mirroring the
gate's own `--self-test`), then against THIS PROJECT'S OWN REAL BYTES AT HEAD (arms 5-7) -- an order
whose criterion genuinely FAILS while `_open_tos_census` still counts it terminal by a VALID
proof-of-spec instance, the exact disagreement S169 named, printed SIDE BY SIDE.

THE FIXTURE SUBSTITUTION, RECORDED RATHER THAN FORCED (Rule 22, "record the difference, do not force
agreement" -- the same discipline this order's own AC3 names for rk-26): the task order's RULED text
cites `AMGT_RESAPP.TO-AMGT-rk-30.page-scores-render.proof_of_spec.json` as the negative control (AC1
PASS, AC2 FAIL). At THIS worktree's HEAD that instance now reads AC1 PASS AND AC2 PASS -- commit
9074091db1 ("rk-19 page half and rk-30 page half AC2 both genuinely PASS now") landed AFTER the
ROUND_ANALYSIS this order cites and is an ancestor of this worktree's cut (047aee5478; confirmed by
`git merge-base --is-ancestor 9074091db1 047aee5478`). Arm 5 below measures and states this directly
rather than asserting the order's now-stale premise. The disagreement itself is still live on THREE
OTHER round-13 orders the CTO's own hand sweep named as criterion defects -- rk-20, rk-23 and the
rk-30 scores-adapter half -- all three still genuinely FAIL at HEAD and all three are counted terminal
by `_open_tos_census`'s proof limb (none carries a <status> tag at all). Arms 6-7 use rk-20's AC1 as
the live substitute. Filed as a surprise row (AMGT_RESAPP-Z-W57-S1); see this cell's proof-of-spec
instance for the row id and citation.

Run: python .tools/tests/test_acceptance_sweep.py
Exit 0 = every arm PASS. Exit 1 otherwise.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WORKSPACE = TOOLS.parent
GATE_PATH = TOOLS / "surprise-row-gate.py"

results: list = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, ok, detail))
    return ok


def _load_gate():
    spec = importlib.util.spec_from_file_location("surprise_row_gate_under_test", str(GATE_PATH))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    gate = _load_gate()
    root = str(WORKSPACE)

    # ARMS 1-4: pure classifier, fixtures only (no repo read) -- the same four shapes the gate's own
    # `--self-test` proves, re-derived here with a DIFFERENT instrument (this standalone battery) per
    # Rule 22's "never re-run the same command" discipline.
    res, p, f, u = gate._classify_acceptance(
        {"AC1": {"criterion_id": "AC1", "status": "PASS"},
         "AC2": {"criterion_id": "AC2", "status": "FAIL", "status_reason": "x"}},
        [{"id": "AC1", "judgment": False}, {"id": "AC2", "judgment": False}])
    check("classify: PASS and FAIL map 1:1", p == 1 and f == 1 and u == 0,
         "res=%r p=%d f=%d u=%d" % (res, p, f, u))

    res2, p2, f2, u2 = gate._classify_acceptance(
        {"AC1": {"criterion_id": "AC1", "status": "UNCOMPUTABLE-BY-CONSTRUCTION"}},
        [{"id": "AC1", "judgment": False}])
    check("classify: a non-PASS/FAIL legal status maps to UNVERIFIABLE", u2 == 1 and p2 == 0 and f2 == 0,
         "res2=%r" % res2)

    res3, p3, f3, u3 = gate._classify_acceptance(
        {"AC1": {"criterion_id": "AC1", "status": "PASS"}}, [{"id": "AC1", "judgment": True}])
    check("classify: a judgment criterion is UNVERIFIABLE even beside a PASS row", u3 == 1 and p3 == 0,
         "res3=%r" % res3)

    res4, p4, f4, u4 = gate._classify_acceptance({}, [{"id": "AC9", "judgment": False}])
    check("classify: a missing row is UNVERIFIABLE, reason-carrying",
         u4 == 1 and "no acceptance row" in res4[0]["reason"], "res4=%r" % res4)

    # ARM 5: REAL BYTES -- the task order's own named fixture, measured rather than assumed. This is
    # the fixture-staleness finding itself, made mechanical.
    rk30_page_to = ("org/missions/D5/AMGT/AMGT_RESAPP/task-orders/"
                    "AMGT_RESAPP.TO-AMGT-rk-30.page-scores-render.md")
    st, otext = gate._blob(root, "HEAD", rk30_page_to)
    crit30 = gate._order_criteria(otext) if st == "OK" else []
    inst_st, inst_path, payload = gate._instance_for_order(root, rk30_page_to)
    if inst_st == "OK":
        rows30, err30 = gate._acceptance_rows_from_instance(payload)
    else:
        rows30, err30 = {}, inst_st
    res30, p30, f30, u30 = gate._classify_acceptance(rows30, crit30) if not err30 else ([], 0, 0, 0)
    ac1_30 = next((r for r in res30 if r["id"] == "AC1"), None)
    ac2_30 = next((r for r in res30 if r["id"] == "AC2"), None)
    both_pass = bool(ac1_30 and ac1_30["status"] == "PASS" and ac2_30 and ac2_30["status"] == "PASS")
    check("REAL BYTES: rk-30 page-half instance classifies -- MEASURED %s/%s (the order's own cited "
         "negative control, AC1 PASS/AC2 FAIL, is STALE at this HEAD: commit 9074091db1 fixed AC2 "
         "after the ROUND_ANALYSIS this order cites and before this worktree's cut; both read PASS now)"
         % (ac1_30["status"] if ac1_30 else "?", ac2_30["status"] if ac2_30 else "?"),
         both_pass, "ac1=%r ac2=%r inst_st=%s" % (ac1_30, ac2_30, inst_st))

    # ARM 6: REAL BYTES -- the LIVE substitute (rk-20 AC1), one of the CTO's three named criterion
    # defects (ROUND_ANALYSIS.round13.md s.1), still genuinely FAIL at this HEAD.
    rk20_to = "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-20.price-generation-contract.md"
    st20, otext20 = gate._blob(root, "HEAD", rk20_to)
    crit20 = gate._order_criteria(otext20) if st20 == "OK" else []
    inst_st20, inst_path20, payload20 = gate._instance_for_order(root, rk20_to)
    rows20, err20 = gate._acceptance_rows_from_instance(payload20) if inst_st20 == "OK" else ({}, inst_st20)
    res20, p20, f20, u20 = gate._classify_acceptance(rows20, crit20) if not err20 else ([], 0, 0, 0)
    ac1_20 = next((r for r in res20 if r["id"] == "AC1"), None)
    check("REAL BYTES: rk-20 (price-generation-contract) classifies AC1 FAIL",
         bool(ac1_20 and ac1_20["status"] == "FAIL"), "ac1_20=%r inst_st20=%s" % (ac1_20, inst_st20))

    # ARM 7: THE SIDE-BY-SIDE -- the sweep lists rk-20's FAIL (round_n=None, since rk-20 carries no
    # <round> tag at all; see the surprise row on this -- a full unfiltered sweep on this project's 127
    # orders measures ~160s, so `_paths` is injected with just this one order: the SAME classification
    # path `_acceptance_sweep` runs in production, on a single-order listing rather than the full
    # `git ls-files`), printed beside `_proof_terminal` -- the SAME function `_open_tos_census` calls,
    # on its OWN read of this one order -- reading it terminal by a VALID proof-of-spec instance. (The
    # full project census reads the same true answer but measures ~118s ALONE, too close to this
    # battery's 120s grading bound to also run here; `_proof_terminal` on one order is the same
    # instrument `_open_tos_census` uses internally, called directly rather than through the whole
    # project sweep.) S169's disagreement, live: FAIL by criterion, terminal by proof, both printed.
    sweep_all = gate._acceptance_sweep(root, "AMGT_RESAPP", round_n=None, _paths=[rk20_to])
    fail_rows = gate._flagged_rows(sweep_all, "FAIL")
    fail_hit = [r for r in fail_rows if "rk-20" in r and ":AC1" in r]
    terminal_ok, terminal_why = gate._proof_terminal(root, rk20_to, otext20)
    check("SIDE BY SIDE: the acceptance sweep lists rk-20:AC1 under FAIL (%s) while _proof_terminal "
         "(the instrument _open_tos_census's own census calls) reads the SAME order terminal by a "
         "VALID proof-of-spec instance (%s: %s)"
         % (fail_hit or "NOT FOUND", terminal_ok, terminal_why),
         bool(fail_hit) and terminal_ok is True,
         "fail_rows=%r terminal_ok=%r terminal_why=%r" % (fail_rows, terminal_ok, terminal_why))

    print()
    for nm, ok, detail in results:
        print("  %-4s %s%s" % ("PASS" if ok else "FAIL", nm, ("   <- " + detail[:300]) if (detail and not ok) else ""))
    failed = len([r for r in results if not r[1]])
    print("RESULT: %d arm(s) failed of %d" % (failed, len(results)))
    if failed == 0:
        print("BATTERY PASS")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
