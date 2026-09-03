#!/usr/bin/env python3
"""cvo_send_guard -- the L8 correspondence guard of the canonical fabric workflow.

Spine (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md v2.1, L8 "Not engaged"): every worker is a
correspondent the CVO does not have; the CVO's findings travel UP to 2.0.0_SA_COO (or to 1.0.0_SA_CTO
for a scope change) and never DOWN to a worker. Andrew-direct 2026-09-03 ~04:5xZ at the CTO terminal,
"Recs approved" on /open-calls CALL 1 (record org/tier1_exec/1.0.0_SA_CTO/deliverables/
ANDREW_DIRECT_20260903_045xZ_RECS_APPROVED_CVO_SEND_REFUSED_L7_L9_GATE_III_INVESTIGATIONS_LIMB.md):
a broker send from 3.0.0_SA_CVO to a Tier-2 serial is REFUSED -- not announced -- while any tree
project reads dep_stage EXECUTING, the stage L7, L8 and L9 all carry (spine section 3).

WHY A REFUSAL: an announced message still reaches the worker, and the harm is the worker acting on it.
WHY THE WHOLE SEND: a per-recipient partial delivery would let a "cc" to the COO carry the same body
to the worker; either every recipient is lawful or the seat did not send, and nothing is written.
MEASURED: the round-1 compiled step logs (org/missions/D11/NFRA/NFRA_COMPEFFICACY/ledger/
STEP_LOG_COMPILED.round1.md, gate-candidate class 4) hold four rows of this class, three after the
ruling was known.

Two halves, kept apart so a harness exercises the decision without a repo:
  executing_tree_projects(repo_root)      the ONE I/O read -- every org/missions/D*/*/*/project.json
                                          and its dep_stage; (None, note) when the census cannot run.
  cvo_worker_send_refusal(from, to, exe)  PURE decision -- the refusal text, or None to admit.
A census that cannot run REFUSES (fail-closed): a guard that cannot see the loop's stage must not
admit the send. Callers: org/mcp/server.py send_message (the MCP tool, which codex-send.py also uses)
and org/mcp/broker.py /send-message (the daemon's HTTP path, reachable without the server).
Self-test: python org/mcp/cvo_send_guard.py --self-test (8 arms, red and green, plus one live census).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CVO_SERIAL = "3.0.0_SA_CVO"
LOOP_STAGE = "EXECUTING"
UP_ROUTE = "2.0.0_SA_COO (or 1.0.0_SA_CTO for a scope change)"
# The same expression as .tools/to-pipeline-gate.py TIER01_RE: Tier-0 is 0.0.<n>_<XX>_..., Tier-1 is <n>.0.0_SA_...;
# a serial that resolves in org and matches neither is a Tier-2 worker for this guard's purpose.
TIER01_RE = re.compile(r"^(?:0\.0\.\d+_[A-Z]{2}_|\d+\.\d+\.\d+_SA_)")
PROJECT_GLOB = "D*/*/*/project.json"


def base_serial(serial: str) -> str:
    """The serial without its ~lane suffix; '' for an empty input."""
    return (serial or "").strip().split("~", 1)[0]


def is_tier2(serial: str) -> bool:
    b = base_serial(serial)
    return bool(b) and not TIER01_RE.match(b)


def executing_tree_projects(repo_root) -> tuple[list[str] | None, str]:
    """(codes, note): the tree projects whose project.json reads dep_stage == EXECUTING, with the denominator
    in the note. codes is None when the census could not run (missing tree, unreadable or unparseable file)."""
    missions = Path(repo_root) / "org" / "missions"
    if not missions.is_dir():
        return None, "org/missions/ not found under %s" % repo_root
    codes: list[str] = []
    n = 0
    for pj in sorted(missions.glob(PROJECT_GLOB)):
        n += 1
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            return None, "%s unreadable or unparseable (%s: %s)" % (pj.as_posix(), type(exc).__name__, exc)
        if isinstance(d, dict) and d.get("dep_stage") == LOOP_STAGE:
            codes.append(pj.parent.name)
    return codes, "%d tree project(s) read" % n


def cvo_worker_send_refusal(from_agent: str, recipients, executing: tuple) -> str | None:
    """PURE. The refusal text when `from_agent` is the CVO (any ~lane), at least one recipient is Tier-2, and
    the tree holds a project in EXECUTING (or the census could not run); None admits the send."""
    if base_serial(from_agent) != CVO_SERIAL:
        return None
    workers = [r for r in (recipients or []) if is_tier2(r)]
    if not workers:
        return None
    codes, note = executing
    if codes is None:
        return ("SEND REFUSED (L8 guard, fail-closed): %s -> %s could not be graded because the tree-project "
                "census did not run (%s). A guard that cannot see the loop's stage admits nothing. Nothing was "
                "written for any recipient." % (from_agent, ", ".join(workers), note))
    if not codes:
        return None
    return ("SEND REFUSED (spine L8: the CVO's findings travel UP, never DOWN): %s -> %s while %d tree "
            "project(s) read dep_stage=%s (L7-L9): %s [%s]. A worker hears from the CVO only through a task "
            "order or an operating note 2.0.0_SA_COO issues; route the finding to %s. Nothing was written for "
            "ANY recipient of this send (%d named). Andrew-direct 2026-09-03 'Recs approved' (CTO /open-calls "
            "CALL 1)." % (from_agent, ", ".join(workers), len(codes), LOOP_STAGE, ", ".join(codes), note,
                          UP_ROUTE, len(recipients or [])))


def _self_test() -> int:
    exe = (["NFRA_COMPEFFICACY"], "1 tree project(s) read")
    idle = ([], "1 tree project(s) read")
    arms = [
        ("CVO -> Tier-2 while EXECUTING: REFUSED, names project + recipient",
         lambda: (lambda r: r is not None and "NFRA_COMPEFFICACY" in r and "0.8.0_AE_CloudComp" in r)(
             cvo_worker_send_refusal("3.0.0_SA_CVO", ["0.8.0_AE_CloudComp"], exe))),
        ("CVO -> COO while EXECUTING: admitted (up the loop)",
         lambda: cvo_worker_send_refusal("3.0.0_SA_CVO", ["2.0.0_SA_COO"], exe) is None),
        ("CVO -> CTO while EXECUTING: admitted (scope change route)",
         lambda: cvo_worker_send_refusal("3.0.0_SA_CVO", ["1.0.0_SA_CTO"], exe) is None),
        ("CVO -> [COO, Tier-2] while EXECUTING: the WHOLE send refused",
         lambda: cvo_worker_send_refusal("3.0.0_SA_CVO", ["2.0.0_SA_COO", "0.7.0_AE_CloudOps"], exe) is not None),
        ("CVO -> Tier-2 with NO project EXECUTING: admitted",
         lambda: cvo_worker_send_refusal("3.0.0_SA_CVO", ["0.8.0_AE_CloudComp"], idle) is None),
        ("CVO~A -> Tier-2~B while EXECUTING: refused (tilde-blind on both ends)",
         lambda: cvo_worker_send_refusal("3.0.0_SA_CVO~A", ["0.8.0_AE_CloudComp~B"], exe) is not None),
        ("MSTR -> Tier-2 while EXECUTING: admitted (not the CVO)",
         lambda: cvo_worker_send_refusal("0.0.0_AB_MSTR", ["0.8.0_AE_CloudComp"], exe) is None),
        ("CVO -> Tier-2, census could not run: REFUSED fail-closed",
         lambda: "fail-closed" in (cvo_worker_send_refusal("3.0.0_SA_CVO", ["0.8.0_AE_CloudComp"], (None, "x")) or "")),
    ]
    failed = 0
    for name, fn in arms:
        ok = False
        try:
            ok = bool(fn())
        except Exception as exc:  # noqa: BLE001
            name += " (raised %s: %s)" % (type(exc).__name__, exc)
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        failed += 0 if ok else 1
    root = Path(__file__).resolve().parents[2]
    codes, note = executing_tree_projects(root)
    print("  LIVE  executing_tree_projects(%s) -> %r (%s)" % (root.as_posix(), codes, note))
    print("RESULT: %d arm(s) failed of %d; live census %s" % (failed, len(arms), "ran" if codes is not None else "DID NOT RUN"))
    return 1 if failed or codes is None else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    print(__doc__)
