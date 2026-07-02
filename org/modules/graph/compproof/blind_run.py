"""
NFRA_COMPPROOF Workstream-B -- the blind-RUN orchestration driver + report/charter emitter (AC#3/#4
wiring). The turnkey "standing re-runnable suite" the harness feeds: MSTR drops each incident's
fresh-solver result; CVO (TO-B2) drops each incident's 3-axis judgment; this driver runs the isolation
gate + scorer per incident, aggregates coverage %, and emits the gap-charters (feeds Workstream D).

The AUTHOR (~D) runs this DRIVER (pure aggregation over provided solver+judge inputs) -- it does NOT
solve or judge (isolation preserved): the solver_results come from MSTR-spawned fresh agents, the
judge_axes from CVO. Re-running with fresh inputs reproduces the coverage line (the regression gate).

Inputs (keyed by opaque case_id B-NN):
  solver_results[case_id] = {concluded_root_cause, traversal_path, confidence, ...}   # MSTR-spawned solver
  judge_axes[case_id]     = {reach, usability, grounding_resilience}                  # CVO/TO-B2 judgment
Missing case_id -> PENDING (not yet run; excluded from the denominator, never silently a MISS).

Author: 0.8.0_AE_CloudComp~D (NFRA_COMPPROOF.B1, CTO arch 1315f9a03). 2026-07-01.
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import corpus          # noqa: E402
import corpus_loader   # noqa: E402
import harness         # noqa: E402

SOLVER_ID_DEFAULT = "MSTR-spawned-blind-solver"   # the fresh per-incident agent (distinct from author)
JUDGE_ID_DEFAULT = "3.0.0_SA_CVO~B"               # TO-B2 judge (distinct from author + solver)


def run_all(solver_results: dict, judge_axes: dict, *, solver_id: str = SOLVER_ID_DEFAULT,
            judge_id: str = JUDGE_ID_DEFAULT) -> dict:
    """Run every incident that has BOTH a solver_result and judge_axes; aggregate; collect charters.
    Incidents missing either input are PENDING (recorded, not scored -- never a silent MISS)."""
    runs, pending, charters = [], [], []
    for inc in corpus.INCIDENTS:
        cid = corpus_loader._case_id(inc)
        sr, ja = solver_results.get(cid), judge_axes.get(cid)
        if sr is None or ja is None:
            pending.append({"case_id": cid, "incident_id": inc["id"],
                            "missing": [n for n, v in (("solver_result", sr), ("judge_axes", ja)) if v is None]})
            continue
        rec = harness.run_incident(inc, sr, solver_id=solver_id, judge_id=judge_id, judge_axes=ja)
        runs.append(rec)
        if rec.get("charter"):
            charters.append(rec["charter"])
    agg = harness.aggregate(runs)
    # AC: 100% of MISS/PARTIAL -> a filed charter (the harness emits one per non-clean run).
    non_clean = [r for r in runs if r["verdict"] in ("MISS", "PARTIAL")]
    charter_complete = len(charters) == len(non_clean)
    return {"aggregate": agg, "runs": runs, "pending": pending, "charters": charters,
            "charter_complete": charter_complete, "n_incidents": len(corpus.INCIDENTS)}


def render_report(result: dict) -> str:
    a = result["aggregate"]
    lines = ["=== NFRA_COMPPROOF B -- blind-run coverage report ===",
             "  incidents: %d | scored: %d | pending: %d | void: %d"
             % (result["n_incidents"], a["n_scored"], len(result["pending"]), a["n_void"]),
             "  SOLVED %d / PARTIAL %d / MISS %d  ->  solved %.1f%% | reached %.1f%%"
             % (a["counts"]["SOLVED"], a["counts"]["PARTIAL"], a["counts"]["MISS"],
                a["solved_pct"], a["reach_pct"]),
             "  gap-charters filed: %d (complete=%s)" % (len(result["charters"]), result["charter_complete"])]
    for r in result["runs"]:
        lines.append("  [%-7s] %s (%s)" % (r["verdict"], r["case_id"], r["incident_id"]))
    if result["pending"]:
        lines.append("  PENDING (awaiting solver/judge): %s"
                     % ", ".join("%s[%s]" % (p["case_id"], "+".join(p["missing"])) for p in result["pending"]))
    return "\n".join(lines)


def _load_json(path: str) -> dict:
    if not path or not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="compproof-blind-run",
                                 description="NFRA_COMPPROOF B blind-run driver (aggregate + charters)")
    ap.add_argument("--solver-results", default="", help="JSON {case_id: solver_result} (MSTR-spawned)")
    ap.add_argument("--judge-axes", default="", help="JSON {case_id: {reach,usability,grounding_resilience}} (CVO/B2)")
    ap.add_argument("--caveats", default="", help="JSON judge-methodology caveats companion (CVO/B2) to "
                    "fold into the report so the Andrew-facing aggregate carries the known-error "
                    "corrections + rubric caveats instead of silently dropping them")
    ap.add_argument("--out", default="", help="write the full result JSON here")
    ap.add_argument("--json", action="store_true", help="print the result JSON instead of the report")
    a = ap.parse_args(argv)
    result = run_all(_load_json(a.solver_results), _load_json(a.judge_axes))
    if a.caveats:
        result["methodology_caveats"] = _load_json(a.caveats)
    if a.json:
        print(json.dumps(result, indent=1, default=str))
    else:
        print(render_report(result))
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2, default=str)
        print("OK: wrote %s" % a.out)
    # exit 0 always -- an empty/pending run is a valid state (not yet executed), not a failure.
    return 0


if __name__ == "__main__":
    sys.exit(main())
