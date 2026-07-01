"""
NFRA_COMPPROOF Workstream-B -- the blind-run HARNESS: isolation gate + 3-axis scorer + gap-charter
+ aggregation + re-runnable suite (AC#2-4). Builds on corpus_loader (AC#1 strip).

THE HARD GATE (arch doc sec 1.2): author != solver != judge, VOID-on-violation. This module:
  - builds the blind-solver spawn PAYLOAD (the solver-view; the actual FRESH-agent spawn is MSTR's).
  - isolation_gate(): asserts (author_id != solver_id != judge_id) AND (root_cause NOT-IN the payload
    actually handed to the solver). A run failing either is VOID -- not scored (B would measure nothing).
  - score_run(): the 3-axis verdict REACH x USABILITY x GROUNDING-RESILIENCE -> SOLVED/PARTIAL/MISS.
    SOLVED requires ALL three. The judgment is CVO's (TO-B2); this is the rubric + the machinery.
  - success_shaped_wrong_probe(): the canary the GROUNDING-RESILIENCE axis runs.
  - gap_charter(): every MISS/PARTIAL -> a filed gap-charter (feeds Workstream D).
  - aggregate(): coverage % across the corpus; re-runnable (a standing regression gate).

Author: 0.8.0_AE_CloudComp~D (NFRA_COMPPROOF.B1, CTO arch 1315f9a03). 2026-07-01.
"""

from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import corpus          # noqa: E402
import corpus_loader   # noqa: E402

# The corpus AUTHOR/builder -- verifies citations, writes the sealed judge-view, strips the
# solver-view. NEVER solves or judges (the isolation invariant).
AUTHOR_ID = "0.8.0_AE_CloudComp~D"

REACH = ("yes", "narrowed", "no")
USABILITY = ("usable", "too-slow", "fell-back")     # too-slow / fell-back-to-raw = functional PARTIAL
GROUNDING = ("resist", "trip")                       # resist = caught the success-shaped-wrong; trip = recorded it
AGGREGATE = ("SOLVED", "PARTIAL", "MISS", "VOID")


# ---- the HARD isolation gate --------------------------------------------------------------

def spawn_payload(incident: dict) -> dict:
    """The blind-solver's spawn payload = the solver-view ONLY. MSTR spawns a FRESH agent per
    incident with this and nothing else (no corpus doc, no root-cause, no prior-B result)."""
    return corpus_loader.solver_view(incident)


def isolation_gate(incident: dict, *, solver_id: str, judge_id: str,
                   author_id: str = AUTHOR_ID) -> dict:
    """The HARD gate (VOID-on-violation): (author != solver != judge) AND (root_cause NOT-IN the
    payload handed to the solver). Returns {case_id, void, reasons, distinct_roles, strip_clean}."""
    case_id = corpus_loader._case_id(incident)
    distinct = len({author_id, solver_id, judge_id}) == 3 and all([author_id, solver_id, judge_id])
    strip = corpus_loader.diff_gate(incident)          # re-run the strip proof on the actual payload
    strip_clean = strip["passed"]
    reasons = []
    if not distinct:
        reasons.append("roles not distinct (author=%s solver=%s judge=%s)" % (author_id, solver_id, judge_id))
    if not strip_clean:
        reasons.append("root_cause leaked into solver payload: %s" % (strip["leaked_terms"] or "full-string"))
    return {"case_id": case_id, "void": bool(reasons), "reasons": reasons,
            "distinct_roles": distinct, "strip_clean": strip_clean}


# ---- the 3-axis scorer (REACH x USABILITY x GROUNDING-RESILIENCE) --------------------------

def score_run(*, reach: str, usability: str, grounding_resilience: str) -> str:
    """Aggregate the 3 axes (arch doc sec 1.3). SOLVED requires reach=yes AND usable AND resist.
    MISS if can't reach OR tripped the success-shaped-wrong grounding trap. Else PARTIAL."""
    if reach not in REACH or usability not in USABILITY or grounding_resilience not in GROUNDING:
        raise ValueError("axis out of vocab: reach=%s usability=%s grounding=%s"
                         % (reach, usability, grounding_resilience))
    if reach == "no" or grounding_resilience == "trip":
        return "MISS"                # can't reach, OR recorded a success-shaped-wrong output as truth
    if reach == "yes" and usability == "usable" and grounding_resilience == "resist":
        return "SOLVED"              # reached, usable in-the-moment, resisted the mis-grounding trap
    return "PARTIAL"                 # reaches-but-slow / narrows-only / grounding-resist-but-slow


def success_shaped_wrong_probe() -> dict:
    """The GROUNDING-RESILIENCE canary (corpus.SUCCESS_SHAPED_WRONG_PROBE): a tool-call that SHOULD
    return N but a slip returns 0/empty/rc=0. A grounded solver cross-checks (expected-nonzero /
    sharp test) -> RESIST; a blind-trust solver records the phantom -> TRIP. Returns the probe spec
    the solver is scored against (trip/resist)."""
    return dict(corpus.SUCCESS_SHAPED_WRONG_PROBE)


# ---- gap-charter emitter (100% of MISS/PARTIAL -> a filed charter, feeds D) ----------------

def gap_charter(incident: dict, verdict: str, *, reach: str, usability: str,
                grounding_resilience: str, note: str = "") -> dict | None:
    """A MISS/PARTIAL emits a gap-charter (a graph-enrichment / new-comp-tool proposal). SOLVED/VOID
    emit none. This is the roadmap generator + the Workstream-D feed."""
    if verdict not in ("MISS", "PARTIAL"):
        return None
    axis_gap = ("REACH" if reach == "no" else "GROUNDING" if grounding_resilience == "trip"
                else "USABILITY" if usability != "usable" else "REACH-narrowed")
    return {
        "charter_for": corpus_loader._case_id(incident),
        "incident_id": incident["id"],
        "failure_class": incident.get("failure_class"),
        "verdict": verdict,
        "gap_axis": axis_gap,
        "proposal": "graph-enrichment or new-comp-tool to close the %s gap for the %s class"
                    % (axis_gap, incident.get("failure_class")),
        "note": note,
        "feeds": "Workstream-D gap-feed",
    }


# ---- aggregation + the re-runnable suite ---------------------------------------------------

def aggregate(scored_runs: list) -> dict:
    """Coverage % across the corpus. scored_runs = [{case_id, verdict, ...}]. VOID excluded from the
    denominator (a void run measured nothing -- it must be re-run, not counted as a miss)."""
    valid = [r for r in scored_runs if r.get("verdict") in ("SOLVED", "PARTIAL", "MISS")]
    counts = {v: sum(1 for r in valid if r["verdict"] == v) for v in ("SOLVED", "PARTIAL", "MISS")}
    n = len(valid)
    void = [r for r in scored_runs if r.get("verdict") == "VOID"]
    return {
        "n_scored": n, "n_void": len(void),
        "counts": counts,
        "solved_pct": round(100.0 * counts["SOLVED"] / n, 1) if n else 0.0,
        "reach_pct": round(100.0 * (counts["SOLVED"] + counts["PARTIAL"]) / n, 1) if n else 0.0,
        "void_case_ids": [r.get("case_id") for r in void],
    }


def run_incident(incident: dict, solver_result: dict, *, solver_id: str, judge_id: str,
                 judge_axes: dict) -> dict:
    """One blind-run: isolation-gate -> (if not void) score the CVO judge's 3 axes -> gap-charter.
    solver_result = {concluded_root_cause, traversal_path, confidence, ...} (the fresh solver's output).
    judge_axes = {reach, usability, grounding_resilience} (CVO/TO-B2 judgment vs the sealed judge-view)."""
    gate = isolation_gate(incident, solver_id=solver_id, judge_id=judge_id)
    rec = {"case_id": gate["case_id"], "incident_id": incident["id"],
           "isolation": gate, "solver_result": solver_result}
    if gate["void"]:
        rec["verdict"] = "VOID"
        rec["charter"] = None
        return rec
    verdict = score_run(**judge_axes)
    rec["verdict"] = verdict
    rec["axes"] = judge_axes
    rec["charter"] = gap_charter(incident, verdict, **judge_axes)
    return rec


# ---- self-test (phase-2 AC: ADVI_BREAKS #1 end-to-end, mock solver+judge) ------------------

def _selftest() -> int:
    # AC#1: the strip DIFF-GATE holds for all 20.
    gate_all = corpus_loader.diff_gate_all()
    assert gate_all["passed"], "STRIP DIFF-GATE must pass 20/20 (got %s)" % gate_all["violations"]

    # CTO arch guard (B1 review): the diff-gate's exclude-scaffolding scoping is sound ONLY while the
    # scaffolding is incident-INVARIANT. If a future incident parameterizes it, this fails -> widen the gate.
    inv = corpus_loader.assert_scaffolding_invariant()
    assert inv["invariant_holds"], \
        "scaffolding must be incident-invariant (diff-gate scoping guard); diverged: %s" % inv["divergent_fields"]

    adv = next(i for i in corpus.INCIDENTS if i["id"] == "ADVI_BREAKS")
    payload = spawn_payload(adv)
    # AC#2: the spawn payload PROVABLY excludes the answer.
    assert "true_root_cause" not in payload and "how_it_was_actually_found" not in payload, \
        "solver payload must NOT contain the answer fields"
    assert corpus_loader.diff_gate(adv)["passed"], "ADVI_BREAKS strip must be clean"

    # isolation VOID-on-violation: same-id (author==solver) must VOID.
    void_run = isolation_gate(adv, solver_id=AUTHOR_ID, judge_id="3.0.0_SA_CVO~B")
    assert void_run["void"], "author==solver must VOID"
    ok_gate = isolation_gate(adv, solver_id="B-SOLVER-fresh", judge_id="3.0.0_SA_CVO~B")
    assert not ok_gate["void"], "distinct roles + clean strip must NOT void"

    # ADVI_BREAKS expected on TODAY's substrate (arch doc sec 4): PARTIAL/MISS (comp-freshness/
    # comp-pipescript timed out; root cause found via raw SSM/S3) -> a gap-charter must emit.
    mock_solver = {"concluded_root_cause": "stale served AUA; suspected a stuck pipeline",
                   "traversal_path": ["comp-freshness (timeout >150s)", "comp-pipescript (timeout)",
                                      "fell back to raw SSM/S3"], "confidence": "low"}
    run = run_incident(adv, mock_solver, solver_id="B-SOLVER-fresh", judge_id="3.0.0_SA_CVO~B",
                       judge_axes={"reach": "narrowed", "usability": "fell-back", "grounding_resilience": "resist"})
    assert run["verdict"] == "PARTIAL", "ADVI_BREAKS mock (narrowed+fell-back) -> PARTIAL, got %s" % run["verdict"]
    assert run["charter"] is not None, "a PARTIAL must emit a gap-charter"

    # scorer vocab: SOLVED / MISS boundaries.
    assert score_run(reach="yes", usability="usable", grounding_resilience="resist") == "SOLVED"
    assert score_run(reach="yes", usability="usable", grounding_resilience="trip") == "MISS"  # mis-grounding
    assert score_run(reach="no", usability="usable", grounding_resilience="resist") == "MISS"

    # aggregate over a mixed set.
    agg = aggregate([{"case_id": "B-01", "verdict": "PARTIAL"}, {"case_id": "B-02", "verdict": "SOLVED"},
                     {"case_id": "B-03", "verdict": "MISS"}, {"case_id": "B-04", "verdict": "VOID"}])
    assert agg["n_scored"] == 3 and agg["n_void"] == 1 and agg["counts"]["SOLVED"] == 1
    print("SELF-TEST PASS: strip 20/20 | scaffolding-invariant HOLDS | payload excludes answer |"
          " isolation VOID-on-violation | ADVI_BREAKS -> PARTIAL + charter | scorer + aggregate OK")
    return 0


if __name__ == "__main__":
    sys.exit(_selftest())
