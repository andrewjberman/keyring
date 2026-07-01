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
import re
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


# ---- the CLEAN-ROOM anti-cheat gate (the spine-validity guard; CTO ruling 143421Z) ---------
# Clean-room boundary: reaching the root cause via the ALLOWED substrate = a valid GRAPH-SOLVED;
# reading a FORBIDDEN narrative/resolution record = the answer-lookup cheat (a false SOLVED).
#
# ALLOWED (the substrate B tests -- NOT flagged): comp-tools (comp-which/blast/kuzu/aws/...), the
#   graph DB, LIVE estate reads (S3/SSM/DDB/served artifacts), and SOURCE CODE (data/*/scripts,
#   infra/, portal/, org/modules/graph). This is exactly what the real ADVI_BREAKS solve used.
# FORBIDDEN (answer-lookup): the NARRATIVE/RESOLUTION records that document an incident's root-cause
#   + fix -- reading one is the cheat.
ALLOWED_AFFORDANCES = ("comp-tools (comp-which/blast/kuzu/trace/xref/platinum/drift/freshness/"
                       "pipescript/iam/routes/depth)", "the graph DB (Nessie/Kuzu @ marker HEAD)",
                       "LIVE estate reads (S3/SSM/DDB/served artifacts)",
                       "SOURCE CODE (data/*/scripts, infra/, portal/, org/modules/graph)")


def _is_forbidden_path(p: str) -> bool:
    """True if a repo path is a NARRATIVE/RESOLUTION record (CTO clean-room denylist), not source."""
    p = p.strip().lower().lstrip("./").replace("\\", "/")
    if p.startswith("memory/") or p.startswith("org/critical_paths/"):
        return True
    if p.startswith("org/") and "/logs/" in p:            # session logs
        return True
    if p.startswith("org/daily_log/"):                    # daily narrative logs
        return True
    if p.startswith("org/modules/graph/debtscan/"):       # incident debtscan ledgers (resolution records
        return True                                       # under an otherwise-allowed source tree)
    if "compiler-tools-log" in p:                         # the running narrative tool-log
        return True
    if p.startswith("docs/") and "postmortem" in p:       # postmortem docs (arch/PRD docs stay allowed)
        return True
    if "claude.md" in p:                                  # incident-prose / NEVER-history
        return True
    return False


def resolution_artifacts(incident: dict) -> list:
    """THIS incident's specific answer-bearing citation path(s) -- the definite resolution record.
    Reading one is the unambiguous cheat (the incident's own postmortem). Derived from the citation."""
    arts = []
    for c in str(incident.get("citation", "")).split(";"):
        c = c.strip().split(":")[0].strip()              # drop a trailing :line-number
        c = c.replace(" origin", "").replace(" (verbatim incident text)", "").strip()
        if c and ("/" in c or c.lower().endswith(".json") or c.lower().endswith(".md")):
            arts.append(c)
    return arts


def cheat_check(traversal_path, incident: dict) -> dict:
    """Post-hoc audit (CTO's judge-path-validation HARD gate): did the solver READ a forbidden
    narrative/resolution record (answer-lookup) rather than reach via the allowed substrate? Returns
    {cheated, citation_hits, narrative_hits}. Any hit VOIDs the run -- B measures graph-reachability,
    not 'is the answer written down'. Two layers: (a) THIS incident's citation path (definite); (b)
    ANY forbidden narrative-category path (the clean-room denylist)."""
    steps = [str(s) for s in (traversal_path or [])]
    path_text = " ".join(steps).lower()
    citation_hits = [a for a in resolution_artifacts(incident) if a.lower() in path_text]
    # scan each cited step's tokens for a forbidden narrative path
    narrative_hits = sorted({tok for s in steps for tok in re.findall(r"[A-Za-z0-9_./\\-]+", s)
                             if ("/" in tok) and _is_forbidden_path(tok)})
    return {"cheated": bool(citation_hits or narrative_hits),
            "citation_hits": citation_hits, "narrative_hits": narrative_hits}


# Fabric-injection markers: files a `claude -p` launch auto-loads by walking UP from its cwd (CLAUDE.md
# + memory auto-recall + org/XXX.md startup). CLAUDE.md states several corpus root-causes VERBATIM
# (incl. #1 ADVI_BREAKS) -- so a launch whose cwd sits inside the fabric tree injects the answer with
# NO tool-call (invisible to the tool-log audit). The clean-room launch MUST run from a cwd with no
# such ancestor. (CTO FINAL refinement 143953Z; MSTR caught the context-injection hole.)
# The ANSWER-BEARING fabric injectors: project CLAUDE.md (states corpus root-causes verbatim), the
# org/XXX.md fabric startup, and the auto-recall memory index. NOT ~/.claude/settings.json -- that is
# benign global CC config (permissions), present above every temp dir under the user home, not narrative.
_FABRIC_INJECTION_MARKERS = ("CLAUDE.md", os.path.join("org", "XXX.md"), os.path.join("memory", "MEMORY.md"))


def assert_clean_context(cwd: str) -> dict:
    """NEVER#4 standing gate: the bare-launch cwd must inject NO fabric narrative. `claude -p`
    discovers CLAUDE.md / memory / org-XXX by walking UP from cwd, so a clean launch dir is one where
    NO ancestor carries an injection marker (i.e. OUTSIDE the workspace tree). A false-clean launch
    would silently false-SOLVE the whole corpus (the answer arrives before any traversal). Returns
    {clean, leaks}. Pair with the tool-log path-audit: context-suppress + file-audit = airtight."""
    leaks, cur, seen = [], os.path.abspath(cwd), set()
    while cur not in seen:
        seen.add(cur)
        for marker in _FABRIC_INJECTION_MARKERS:
            mp = os.path.join(cur, marker)
            if os.path.exists(mp):
                leaks.append(mp)
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return {"clean": not leaks, "leaks": leaks}


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
        rec["void_reason"] = "isolation: " + "; ".join(gate["reasons"])
        rec["charter"] = None
        return rec
    # clean-room anti-cheat (CTO FINAL 143701Z): the HARD VOID-gate audits the solver's ACTUAL
    # captured tool-log (every Read/Grep/comp-tool call), NOT its self-reported path -- reading a
    # forbidden narrative/resolution record VOIDs the run (answer-lookup, not graph-traversal). The
    # spine's validity guard -- else every historical incident is a false SOLVED via postmortem-grep.
    audit_source = solver_result.get("tool_log") or solver_result.get("traversal_path")
    cheat = cheat_check(audit_source, incident)
    rec["cheat_check"] = cheat
    if cheat["cheated"]:
        rec["verdict"] = "VOID"
        rec["void_reason"] = ("postmortem-cheat: solver read a forbidden resolution record "
                              "(citation=%s narrative=%s)" % (cheat["citation_hits"], cheat["narrative_hits"]))
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

    # postmortem anti-cheat: a solver that READ the incident's resolution record VOIDs (cheat != solve),
    # even with a perfect-looking 3-axis judgment -- the spine-validity guard.
    cheat_solver = {"concluded_root_cause": "the stranded 4-layer cutover",
                    "traversal_path": ["read org/modules/graph/debtscan/2026-06-12_LIVE_inf-ADVI-stranded-deploy-P0.md"],
                    "confidence": "high"}
    cheat_run = run_incident(adv, cheat_solver, solver_id="B-SOLVER-fresh", judge_id="3.0.0_SA_CVO~B",
                             judge_axes={"reach": "yes", "usability": "usable", "grounding_resilience": "resist"})
    assert cheat_run["verdict"] == "VOID" and "postmortem-cheat" in cheat_run.get("void_reason", ""), \
        "reading the resolution record must VOID (cheat != solve), got %s" % cheat_run["verdict"]

    # NEVER#4 (CTO 143953Z): the sanitized bare-launch cwd must inject NO fabric narrative. A temp dir
    # outside the ws is clean; the fabric tree (this module's dir) is CONTAMINATED (CLAUDE.md up-tree).
    import tempfile
    _canary = tempfile.mkdtemp(prefix="compproof_canary_")
    try:
        assert assert_clean_context(_canary)["clean"], "a temp dir outside the ws must be clean-context"
    finally:
        os.rmdir(_canary)
    assert not assert_clean_context(_HERE)["clean"], \
        "the fabric tree MUST read as context-CONTAMINATED (CLAUDE.md/memory up-tree) -- else false-SOLVE"

    # scorer vocab: SOLVED / MISS boundaries.
    assert score_run(reach="yes", usability="usable", grounding_resilience="resist") == "SOLVED"
    assert score_run(reach="yes", usability="usable", grounding_resilience="trip") == "MISS"  # mis-grounding
    assert score_run(reach="no", usability="usable", grounding_resilience="resist") == "MISS"

    # aggregate over a mixed set.
    agg = aggregate([{"case_id": "B-01", "verdict": "PARTIAL"}, {"case_id": "B-02", "verdict": "SOLVED"},
                     {"case_id": "B-03", "verdict": "MISS"}, {"case_id": "B-04", "verdict": "VOID"}])
    assert agg["n_scored"] == 3 and agg["n_void"] == 1 and agg["counts"]["SOLVED"] == 1
    print("SELF-TEST PASS: strip 20/20 | scaffolding-invariant HOLDS | payload excludes answer |"
          " isolation VOID-on-violation | postmortem-cheat VOIDs | clean-context gate | ADVI_BREAKS"
          " -> PARTIAL + charter | scorer + aggregate OK")
    return 0


if __name__ == "__main__":
    sys.exit(_selftest())
