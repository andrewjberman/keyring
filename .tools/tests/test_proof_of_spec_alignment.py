#!/usr/bin/env python3
"""PIPELINE GATE LAYER 1 -- the mutant battery for decomp_ref + bidirectional alignment.

Subject: `.tools/proof-of-spec-check.py` `alignment_check()`, built 2026-08-24 by
`0.8.0_AE_CloudComp~F` per org/ref/DIRECTIVE_EXECUTION_PIPELINE.md:170 (build routed;
Andrew's word granted in the ratification). CTO ruling 66492 set the ramp shape.

    A PASSING ASSERTION NEVER MUTATED HAS NEVER BEEN TESTED.

So every arm below is reachable from a DIFFERENT TRUTH. The conformant fixture is
planted first and must read VALID with its denominators COMPUTED (not merely present);
each mutant then breaks exactly ONE thing and must flip exactly that verdict. A suite
whose arms all pass for the same reason is a brick, and a gate that cannot be shown to
FAIL has not been shown to gate.

WHY A SEALED TEMP WORKSPACE, NOT THE LIVE ONE: alignment_check() joins across three
real artifacts (project JSON -> TO -> DECOMP.md). Pointing the arms at live estate files
would make this battery pass or fail on estate edits it does not control, and CVO
re-runs it independently -- it must be reproducible from the repo alone.

Run: python .tools/tests/test_proof_of_spec_alignment.py
Exit 0 = all arms as expected. Exit 1 = at least one arm did not.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
CHECKER = TOOLS / "proof-of-spec-check.py"

PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL, detail))


def _load_checker():
    """The module name carries hyphens, so a plain import cannot reach it."""
    spec = importlib.util.spec_from_file_location("pos_check", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


DECOMP = """# FIXTURE DECOMP -- sealed
| cell_id | surface |
|---|---|
| `FIX-a-1` | first build cell |
| `FIX-a-2` | second build cell |
| `FIX-b-1` | third build cell |
| `FIX-b-2` | a cell the fixture TO does NOT declare |
"""

TO_TEMPLATE = """# TO FIX_PROJ.TO-1 -- sealed fixture
<task_order id="FIX_PROJ.TO-1" project="FIX_PROJ">
{decomp_ref}
<issued_by>2.0.0_SA_COO</issued_by>
<status>ACTIVE</status>
<proof_of_spec>
{criteria}
  <expected_criteria>FIX-C1,FIX-C2</expected_criteria>
</proof_of_spec>
</task_order>
"""

CONFORMANT_CRITERIA = (
    '    <criterion id="FIX-C1" cell_refs="FIX-a-1"/>\n'
    '    <criterion id="FIX-C2" cell_refs="FIX-a-2, FIX-b-1"/>'
)


# Set by _build(): the real commit hash of the sealed fixture repo. The vintage check
# runs `git cat-file -e <hash>^{commit}` with cwd = the (temp) WORKSPACE, so the fixture
# must be a genuine repo or the conformant arm would fail for the wrong reason.
FIXTURE_VINTAGE = "abc1234"


def _instance(decomp_doc: str, to_ref: str, vintage: str = "") -> dict:
    """A schema-valid instance. Kept minimal but COMPLETE -- if it were not schema-valid
    the arms would go red for the wrong reason and the battery would be measuring the
    fixture instead of the gate."""
    return {
        "schema_version": "1.0",
        "to_id": "FIX_PROJ.TO-1",
        "phase": "BUILD-GENERAL",
        "spec_ref": {"doc": "docs/fixture.md", "group": "OTHER",
                     "vintage_commit": "abc1234"},
        "assignee": "0.8.0_AE_CloudComp~F",
        "decomp_ref": {"doc": decomp_doc,
                       "vintage_commit": vintage or FIXTURE_VINTAGE,
                       "to_ref": to_ref},
        "artifacts_produced": [{
            "path_or_key": "docs/fixture_artifact.md", "kind": "doc",
            "commit_or_etag": "abc1234",
            "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
            "deploy_evidence": "fixture; no deploy scope",
        }],
        "acceptance": [
            {"criterion_id": "FIX-C1", "criterion_verbatim": "the first fixture criterion",
             "method": "command", "invocation": "true", "output_evidence": "fixture output one",
             "denominator": "1 of 1", "status": "PASS"},
            {"criterion_id": "FIX-C2", "criterion_verbatim": "the second fixture criterion",
             "method": "command", "invocation": "true", "output_evidence": "fixture output two",
             "denominator": "1 of 1", "status": "PASS"},
        ],
        "controls": {
            "mutant": {"description": "fixture mutant description",
                       "expected": "flips", "observed": "flipped",
                       "status": "FIRED-AS-EXPECTED"},
            "determinism": {"method": "two identical runs compared",
                            "observed": "identical", "status": "STABLE"},
        },
        "declared_exclusions": [],
        "surprises": [],
        "session_log": "org/fixture/log.md",
        "compiler_tools": [{"tool": "comp-find", "invocation": "comp-find x",
                            "result": "fixture"}],
    }


def _build(ws: Path, *, decomp_ref_line: str, criteria: str, dep_stage: bool = True) -> Path:
    """Plant a sealed workspace. Returns the TO path."""
    (ws / "org" / "projects").mkdir(parents=True, exist_ok=True)
    body = {"code": "FIX_PROJ", "status": "active"}
    if dep_stage:
        body["dep_stage"] = "EXECUTING"
    (ws / "org" / "projects" / "FIX_PROJ.json").write_text(
        json.dumps(body), encoding="utf-8")
    dec = ws / "workflows" / "runs" / "fixture"
    dec.mkdir(parents=True, exist_ok=True)
    (dec / "DECOMP.md").write_text(DECOMP, encoding="utf-8")
    (dec / "rectangle.final.certified.json").write_text(json.dumps({"cells": [
        {"cell_id": "FIX-a-1"}, {"cell_id": "FIX-a-2"},
        {"cell_id": "FIX-b-1"}, {"cell_id": "FIX-b-2"},
    ]}), encoding="utf-8")
    tod = ws / "org" / "tier2_senior" / "0.8.0_AE_CloudComp" / "task_orders"
    tod.mkdir(parents=True, exist_ok=True)
    to = tod / "FIX_PROJ.TO-1.fixture.md"
    to.write_text(
        TO_TEMPLATE.format(decomp_ref=decomp_ref_line, criteria=criteria), encoding="utf-8")
    _init_repo(ws)
    return to


def _git(ws: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-c", "user.name=battery", "-c", "user.email=battery@opal.agent", *args],
        cwd=ws, capture_output=True, text=True)


def _init_repo(ws: Path) -> None:
    """Make the sealed fixture a REAL repo so the vintage check exercises real git.

    Bypassing it (pointing the resolver at the live repo) would test a code path the
    production checker does not take, and would reintroduce the estate dependency the
    sealed workspace exists to remove.
    """
    global FIXTURE_VINTAGE
    _git(ws, "init", "-q")
    _git(ws, "add", "-A")
    _git(ws, "commit", "-q", "-m", "fixture")
    out = _git(ws, "rev-parse", "HEAD").stdout.strip()
    FIXTURE_VINTAGE = out[:10] if out else "abc1234"


DECOMP_REL = "workflows/runs/fixture/DECOMP.md"
CELL_DOC_REL = "workflows/runs/fixture/rectangle.final.certified.json"
TO_REL = "org/tier2_senior/0.8.0_AE_CloudComp/task_orders/FIX_PROJ.TO-1.fixture.md"
CONFORMANT_REF = (
    f"<decomp_ref>{DECOMP_REL} -- cells FIX-a-1, FIX-a-2, FIX-b-1</decomp_ref>")
PARENTHESIZED_REF = (
    f"<decomp_ref>({DECOMP_REL}) -- cells FIX-a-1, FIX-a-2, FIX-b-1</decomp_ref>")
EXPLICIT_CELL_DOC_REF = (
    f"<decomp_ref><decomp_doc>{CELL_DOC_REL}</decomp_doc>"
    f"<owned_cells>FIX-a-1, FIX-a-2, FIX-b-1</owned_cells></decomp_ref>")

# PRODUCTION-SHAPED FIXTURES. Modelled on the real ADVI_PERFRP round-1 TOs as they stood
# BEFORE COO's relocation fix @249e0687c8: owned cells, a READ-DEPENDENCY clause and an
# EXPLICIT EXCLUSION clause all inside the one element. Until these existed, every arm in
# this battery exercised the harvest against a decomp_ref naming ONLY owned cells -- so
# the shape that actually broke the gate in production could not fail any arm here.
REF_UNDELIMITED_WITH_PROSE = (
    f"<decomp_ref>{DECOMP_REL} -- cells FIX-a-1, FIX-a-2 "
    f"(reads FIX-b-1; NOT in this TO: FIX-b-2)</decomp_ref>")
REF_DELIMITED_WITH_PROSE = (
    f"<decomp_ref>{DECOMP_REL} -- cells FIX-a-1, FIX-a-2 "
    f"(reads FIX-b-1; NOT in this TO: FIX-b-2)"
    f"<owned_cells>FIX-a-1, FIX-a-2</owned_cells></decomp_ref>")
REF_DELIMITED_OVERCLAIM = (
    f"<decomp_ref>{DECOMP_REL} -- the delimiter claims a cell no criterion discharges"
    f"<owned_cells>FIX-a-1, FIX-a-2, FIX-b-1, FIX-b-2</owned_cells></decomp_ref>")
REF_DELIMITER_CARRYING_PROSE = (
    f"<decomp_ref>{DECOMP_REL}"
    f"<owned_cells>FIX-a-1, FIX-a-2 (render half)</owned_cells></decomp_ref>")


def _run(mod, ws: Path, inst: dict) -> tuple[list, list]:
    mod.WORKSPACE = ws
    return mod.alignment_check(inst)


def _has(violations: list, needle: str) -> bool:
    return any(needle in v for v in violations)


def _frame(frames: list, needle: str) -> str:
    return next((f for f in frames if needle in f), "")


def main() -> int:
    mod = _load_checker()

    # ---- ARM 1: CONFORMANT -> no violations, and the denominators COMPUTED ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        check("conformant: no violations", not v, str(v))
        check("conformant: ENFORCE branch taken", bool(_frame(f, "alignment: ENFORCE")))
        # The denominators must be the RIGHT numbers, not merely present. 4 cells exist
        # in the decomp; the TO declares 3; 2 criteria cite 3 distinct cells.
        check("conformant: decomp id space = 4",
              "= 4 distinct cell id(s)" in _frame(f, "decomp id space"),
              _frame(f, "decomp id space"))
        check("conformant: forward-1 = 2/2",
              "2/2 criteria" in _frame(f, "forward-1"), _frame(f, "forward-1"))
        check("conformant: forward-2 = 3/3",
              "3/3 distinct cell_ref" in _frame(f, "forward-2"), _frame(f, "forward-2"))
        check("conformant: backward = 3/3",
              "3/3 cell(s) declared" in _frame(f, "backward"), _frame(f, "backward"))

    # ---- ARM 1b: R4-DT-6 recurrence -- punctuation is not part of a legacy path ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=PARENTHESIZED_REF, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        check("parenthesized legacy path: delimiter excluded and join VALID", not v, str(v))
        check("parenthesized legacy path: full 4-cell doc resolved",
              "= 4 distinct cell id(s)" in _frame(f, "decomp id space"),
              _frame(f, "decomp id space"))

    # ---- ARM 1c: explicit cell-bearing artifact, not a narrative-only face ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=EXPLICIT_CELL_DOC_REF, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(CELL_DOC_REL, TO_REL))
        check("explicit decomp_doc JSON: no violations", not v, str(v))
        check("explicit decomp_doc JSON: 4-cell id space resolved",
              "= 4 distinct cell id(s)" in _frame(f, "decomp id space"),
              _frame(f, "decomp id space"))

    # ---- ARM 2: MUTANT -- drop decomp_ref from the instance ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF, criteria=CONFORMANT_CRITERIA)
        inst = _instance(DECOMP_REL, TO_REL)
        del inst["decomp_ref"]
        v, f = _run(mod, ws, inst)
        check("mutant drop-decomp_ref: INVALID", _has(v, "this instance MUST carry a decomp_ref"), str(v))

    # ---- ARM 3: MUTANT -- a criterion with NO cell_refs (forward-1) ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF,
               criteria='    <criterion id="FIX-C1" cell_refs="FIX-a-1"/>\n'
                        '    <criterion id="FIX-C2"/>')
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        check("mutant no-cell_refs: refused", _has(v, "carries NO cell_refs"), str(v))
        check("mutant no-cell_refs: forward-1 denominator drops to 1/2",
              "1/2 criteria" in _frame(f, "forward-1"), _frame(f, "forward-1"))

    # ---- ARM 4: MUTANT -- cell_ref naming a cell the decomp does not declare ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF,
               criteria='    <criterion id="FIX-C1" cell_refs="FIX-a-1"/>\n'
                        '    <criterion id="FIX-C2" cell_refs="FIX-a-2, FIX-z-9"/>')
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        check("mutant phantom-cell: refused", _has(v, "'FIX-z-9'"), str(v))
        check("mutant phantom-cell: names the citing criterion",
              _has(v, "FIX-C2"), str(v))

    # ---- ARM 5: MUTANT -- a declared cell no criterion reaches (BACKWARD) ----
    # This is the arm the whole backward direction exists for: the TO claims a cell it
    # never discharges. A forward-only checker reads this as perfectly clean.
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=REF_DELIMITED_OVERCLAIM, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        check("mutant unreached-cell (DELIMITED): refused",
              _has(v, "'FIX-b-2'") and _has(v, "never discharges"), str(v))
        check("mutant unreached-cell: backward denominator drops to 3/4",
              "3/4 cell(s) declared" in _frame(f, "backward"), _frame(f, "backward"))

    # ---- ARM 6: NEGATIVE CONTROL -- TO with no <decomp_ref> stays VALID (ANNOUNCE) ----
    # Without this arm the battery cannot tell a working gate from one that refuses
    # everything. A gate that fails every input is not a gate.
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line="", criteria=CONFORMANT_CRITERIA)
        inst = _instance(DECOMP_REL, TO_REL)
        del inst["decomp_ref"]
        v, f = _run(mod, ws, inst)
        check("negative control: pre-pipeline TO -> no violations", not v, str(v))
        check("negative control: ANNOUNCE branch stated",
              bool(_frame(f, "alignment: ANNOUNCE")))

    # ---- ARM 7: FAIL-CLOSED -- declared to_ref that does not resolve ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(DECOMP_REL, "org/nope/task_orders/ghost.md"))
        check("fail-closed: bogus to_ref is a violation, not a pass",
              _has(v, "does not resolve"), str(v))

    # ---- ARM 8: FAIL-CLOSED -- unresolvable TO on a pipeline-registered project ----
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF, criteria=CONFORMANT_CRITERIA)
        inst = _instance(DECOMP_REL, TO_REL)
        del inst["decomp_ref"]
        inst["to_id"] = "FIX_PROJ.TO-NOSUCH"
        v, f = _run(mod, ws, inst)
        check("fail-closed: unresolvable TO on pipeline project is a violation",
              _has(v, "UNRESOLVED"), str(v))

    # ---- ARM 9: the same miss on a NON-pipeline project stays an announce ----
    # Proves ARM 8 fires on dep_stage, not on unresolvability alone -- otherwise it
    # would invalidate the 126 instances whose projects are not pipeline-registered.
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF, criteria=CONFORMANT_CRITERIA,
               dep_stage=False)
        inst = _instance(DECOMP_REL, TO_REL)
        del inst["decomp_ref"]
        inst["to_id"] = "FIX_PROJ.TO-NOSUCH"
        v, f = _run(mod, ws, inst)
        check("scope: unresolvable TO on NON-pipeline project -> announce only",
              not v, str(v))

    # ---- ARMS 11-14: VINTAGE RESOLUTION (CVO 66693, routed CTO 66702) ----
    # THE DEFECT THESE CLOSE: decomp_ref.vintage_commit was REQUIRED by schema and its
    # VALUE was never checked, so a hash ONE CHARACTER OFF the true one read VALID.
    # My original battery could not have caught this -- every arm it had used the same
    # fixture vintage, so no arm ever varied the field under test. Found by CVO in
    # independent verification.
    #
    # EACH ARM ASSERTS ITS MUTATION ACTUALLY CHANGED THE ARTIFACT BEFORE ITS VERDICT
    # COUNTS (CVO's rule, adopted into this battery's contract): CVO's own first probe
    # mutated a field that DOES NOT EXIST behind an isinstance guard, the mutation never
    # fired, and the run returned VALID -- which is BYTE-IDENTICAL to a mutation that
    # fired and was wrongly accepted. A mutant that silently no-ops is not a control.
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=CONFORMANT_REF, criteria=CONFORMANT_CRITERIA)
        real = FIXTURE_VINTAGE
        base = _instance(DECOMP_REL, TO_REL)
        v, f = _run(mod, ws, base)
        check("vintage: real commit hash -> no violation (positive control)",
              not v and bool(_frame(f, "RESOLVES")), str(v))
        one_off = real[:-1] + ("b" if real[-1] != "b" else "c")
        for label, bad in (("fabricated deadbeef99", "deadbeef99"),
                           ("all zeros", "0000000000"),
                           ("ONE CHARACTER OFF the true hash", one_off)):
            mutated = _instance(DECOMP_REL, TO_REL, vintage=bad)
            fired = mutated["decomp_ref"]["vintage_commit"] != base["decomp_ref"]["vintage_commit"]
            v2, _ = _run(mod, ws, mutated)
            check(f"vintage: {label} -> REFUSED",
                  fired and _has(v2, "does NOT resolve to a commit"),
                  f"mutation_applied={fired}; violations={v2}")

    # ---- ARMS 15-18: THE DELIMITED OWNED-CELLS CLAUSE (AE~G 66872, CTO 66893) ----
    # THE DEFECT: the wide harvest read EVERY cell id in the whole <decomp_ref> as a cell
    # the TO CLAIMS. A read-dependency became an unclaimed claim; an EXPLICIT EXCLUSION
    # ("NOT in this TO: X") was INVERTED into a claim the TO was then faulted for not
    # discharging -- a seat reading that violation without opening the TO would conclude
    # the exact OPPOSITE of what the TO says. Measured in production on 5 round-1 TOs.
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=REF_UNDELIMITED_WITH_PROSE, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        # THE INVERSION ARM. FIX-b-2 appears ONLY in "NOT in this TO:" -- the old code
        # asserted a violation on it. It must now announce and stay clean.
        check("undelimited + exclusion prose: NO violation asserted",
              not v, str(v))
        check("undelimited + exclusion prose: announced with the reason",
              "UNDELIMITED" in _frame(f, "alignment-backward: UNDELIMITED"),
              _frame(f, "alignment-backward: UNDELIMITED"))

    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=REF_DELIMITED_WITH_PROSE, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        check("delimited + exclusion prose: VALID (prose ignored, delimiter binds)",
              not v, str(v))
        check("delimited + exclusion prose: backward is 2/2 over the OWNED set only",
              "2/2 cell(s) declared" in _frame(f, "backward")
              and "<owned_cells>" in _frame(f, "backward"), _frame(f, "backward"))

    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=REF_DELIMITER_CARRYING_PROSE, criteria=CONFORMANT_CRITERIA)
        v, f = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
        check("prose INSIDE the delimiter is refused (ids-only is mechanical)",
              _has(v, "non-id text"), str(v))

    # THE PAIRED CONTROL, and it is the one that makes the three above mean anything:
    # the SAME exclusion prose, one delimited and one not, differing ONLY in whether the
    # <owned_cells> element is present. If both read the same way, the delimiter is inert.
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=REF_UNDELIMITED_WITH_PROSE, criteria=CONFORMANT_CRITERIA)
        _, f_un = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        _build(ws, decomp_ref_line=REF_DELIMITED_WITH_PROSE, criteria=CONFORMANT_CRITERIA)
        _, f_de = _run(mod, ws, _instance(DECOMP_REL, TO_REL))
    un_b, de_b = _frame(f_un, "backward"), _frame(f_de, "backward")
    check("delimiter CHANGES the harvest (4-wide vs 2-owned), so it is not inert",
          "4 cell(s)" in un_b and "2/2 cell(s)" in de_b, f"undelimited={un_b} | delimited={de_b}")

    # ---- ARM 10: SEAL -- the fixture instance is genuinely schema-valid ----
    # If it were not, every green arm above would be green for the wrong reason.
    try:
        import jsonschema
        schema = json.loads(mod.SCHEMA_PATH.read_text(encoding="utf-8"))
        errs = sorted(jsonschema.Draft7Validator(schema).iter_errors(
            _instance(DECOMP_REL, TO_REL)), key=str)
        check("seal: fixture instance is schema-valid against the LIVE schema",
              not errs, "; ".join(f"{'/'.join(str(p) for p in e.absolute_path)}: {e.message}"
                                  for e in errs))
    except ImportError:
        check("seal: fixture instance is schema-valid against the LIVE schema",
              False, "jsonschema not installed -- SEAL UNVERIFIED, not assumed passing")

    width = max(len(n) for n, _, _ in results)
    for name, verdict, detail in results:
        line = f"  {verdict:4s} {name.ljust(width)}"
        if verdict == FAIL and detail:
            line += f"   <- {detail[:200]}"
        print(line)
    failed = [r for r in results if r[1] == FAIL]
    print(f"\nproof-of-spec alignment battery: {len(results) - len(failed)}/{len(results)} arms as expected")
    if failed:
        print("BATTERY FAILED -- the gate does not behave as specified.")
        return 1
    print("BATTERY PASS -- conformant reads VALID, every mutant flips, and the "
          "negative controls keep it from being a brick.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
