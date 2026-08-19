"""Acceptance battery: proof-of-spec-check artifact-coverage tests COVERAGE, not NAMING.

COO's acceptance note, honoured literally: exercise BOTH id grammars, because a one-sided test
would let a fix that simply DISABLES the rule look correct. So this battery asserts in four
directions, and two of them must still FAIL:

  A  DS-grammar instance that passes today            -> MUST STILL PASS   (no regression)
  B  WP1-N-grammar instance that fails today          -> MUST FLIP to pass (the force-class fix)
  C  genuinely uncovered artifact                     -> MUST STILL FAIL   (rule not disabled)
  D  artifact "covered" only by an incidental mention
     of its stem inside an UNRELATED exclusion        -> MUST NOW FAIL     (the silent false pass)

D is the one this seat found on its OWN accepted deliverable: TO-1's broker.py passed because an
exclusion about the site-Z fabric leg contains the word "broker". A false FAIL is loud and gets
argued with; a false PASS is believed.

Usage: python org/standards/test_artifact_coverage_both_grammars.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

WS = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         cwd=str(Path(__file__).resolve().parent),
                         capture_output=True, text=True).stdout.strip())
CHECKER = WS / ".tools" / "proof-of-spec-check.py"
RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


def base(criterion_ids, artifacts, exclusions=None, rows_extra=None):
    return {
        "schema_version": "1.0", "to_id": "FIXTURE.T", "phase": "NON-BUILD-OTHER",
        "spec_ref": {"doc": "docs/architecture/D0_INFRA_TIGHTENING_PRD.md", "group": "T",
                     "vintage_commit": "4bf291b26c"},
        "assignee": "0.8.0_AE_CloudComp",
        "artifacts_produced": artifacts,
        "acceptance": [
            {"criterion_id": c,
             "criterion_verbatim": "a criterion long enough to satisfy minLength",
             "method": "command",
             "invocation": (rows_extra or {}).get(c, "python -c 'pass'"),
             "output_evidence": "OK: exercised", "denominator": "1 of 1", "status": "PASS"}
            for c in criterion_ids],
        "controls": {
            "mutant": {"description": "a mutant description long enough", "expected": "x",
                       "observed": "y", "status": "FIRED-AS-EXPECTED"},
            "determinism": {"method": "two runs compared", "observed": "same", "status": "STABLE"}},
        "declared_exclusions": exclusions or [],
        "surprises": [], "session_log": "org/x/log.md",
        "compiler_tools": [{"tool": "t", "invocation": "i", "result": "r"}],
    }


def run(inst) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "i.json"
        f.write_text(json.dumps(inst), encoding="utf-8")
        p = subprocess.run([sys.executable, str(CHECKER), str(f)],
                           cwd=str(WS), capture_output=True, text=True)
        return p.returncode, (p.stdout or "") + (p.stderr or "")


ART = "data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py"

# --- A: DS grammar, artifact stem inside the criterion id. Must PASS. ---
rc, out = run(base(["MDPF-A-AUMMETRICS-01"], [{"path_or_key": ART, "kind": "script",
              "commit_or_etag": "abc1234", "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
              "deploy_evidence": "n/a"}]))
rec("A-DS-GRAMMAR-STILL-PASSES", rc == 0 and "artifact-coverage" not in out,
    f"DS-grammar id carrying the artifact stem -> rc={rc} (must be 0; no regression)")

# --- B: WP1-N grammar, artifact referenced by the ROW's invocation. Must PASS now. ---
rc, out = run(base(["WP1-1"], [{"path_or_key": ART, "kind": "script",
              "commit_or_etag": "abc1234", "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
              "deploy_evidence": "n/a"}],
              rows_extra={"WP1-1": f"python {ART} --dry-run"}))
rec("B-WP1-GRAMMAR-FLIPS", rc == 0 and "artifact-coverage" not in out,
    f"WP1-N id whose row INVOKES the artifact -> rc={rc} (must be 0; the force-class fix)")

# --- C: genuinely uncovered. Must STILL FAIL. ---
rc, out = run(base(["WP1-1"], [{"path_or_key": ART, "kind": "script",
              "commit_or_etag": "abc1234", "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
              "deploy_evidence": "n/a"}]))
rec("C-UNCOVERED-STILL-FAILS", rc != 0 and "artifact-coverage" in out,
    f"artifact referenced NOWHERE -> rc={rc} + artifact-coverage violation "
    f"(must FAIL; proves the rule was not disabled)")

# --- D: the silent false pass -- stem mentioned only in an UNRELATED exclusion. Must FAIL now. ---
rc, out = run(base(["WP1-1"], [{"path_or_key": ART, "kind": "script",
              "commit_or_etag": "abc1234", "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
              "deploy_evidence": "n/a"}],
              exclusions=[{"item": "the site-Z leg",
                           "reason": "unreachable; note dim_mdpf_aum_metrics is unrelated here"}]))
rec("D-INCIDENTAL-EXCLUSION-NOW-FAILS", rc != 0 and "artifact-coverage" in out,
    f"stem appears ONLY incidentally in an unrelated exclusion's REASON -> rc={rc} "
    f"(must FAIL now; this is the silent false pass found on a real accepted instance)")

# --- E: explicit artifact_covered_by citing a REAL row. Must PASS. ---
rc, out = run(base(["WP1-1"], [{"path_or_key": ART, "kind": "script",
              "commit_or_etag": "abc1234", "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
              "deploy_evidence": "n/a", "artifact_covered_by": ["WP1-1"]}]))
rec("E-EXPLICIT-FIELD-PASSES", rc == 0 and "artifact-coverage" not in out,
    f"artifact_covered_by naming a real row -> rc={rc} (must be 0)")

# --- F: explicit field citing a row that does NOT exist. Must FAIL. ---
rc, out = run(base(["WP1-1"], [{"path_or_key": ART, "kind": "script",
              "commit_or_etag": "abc1234", "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
              "deploy_evidence": "n/a", "artifact_covered_by": ["WP9-9"]}]))
rec("F-DANGLING-CITATION-FAILS", rc != 0 and "do not exist" in out,
    f"artifact_covered_by citing a NONEXISTENT row -> rc={rc} "
    f"(must FAIL; a citation to a row that is not there is worse than no citation)")

n = sum(1 for _, v, _ in RESULTS if v == "PASS")
print()
print("=" * 80)
print(f"ARTIFACT-COVERAGE BATTERY: {n}/{len(RESULTS)} PASS (denominator {len(RESULTS)})")
print("  C and D are the anti-disable controls -- they must FAIL the checker to PASS here.")
print("=" * 80)
sys.exit(0 if n == len(RESULTS) else 1)
