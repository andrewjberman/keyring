# TO NFRA_CTLPLN.TO-CT-ab-9 -- workstream NAMEGATE round 1 (cell CT-ab-9): the naming gate exempts test fixtures under both `tests/` and `test/` by an explicit list (dell1 row D1-W60-S3)

<to_id>NFRA_CTLPLN.TO-CT-ab-9</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~82</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>NAMEGATE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-9` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

The commit-time naming gate `.tools/naming-gate.py` (now owned by NFRA_CTLPLN) skips test fixtures, but only under a folder spelled `tests`: about :996-997 (`and "/tests/" not in "/" + hit`) and about :2169-2170 (`if "/tests/" in "/" + path: return rows  # fixtures under */tests/* are not graded`); the docstring at about :27 says "anything under */tests/*". A fixture under a folder spelled `test/` is graded, which refused a dell1 worker's fixture (row ADVI_FIRMBKTS D1-W60-S3). RULED: an explicit list of BOTH spellings, `("/tests/", "/test/")`, matched as whole path segments, never a substring (so `latest/`, `contest/` or `test_data/` are NOT exempt).

### BUILD

1. One module-level constant `FIXTURE_DIRS = ("/tests/", "/test/")` and one helper `_is_fixture(path)` returning True when any entry occurs in `"/" + path`; use it at both sites. The generated-file check must still run before the exclusion (as the comment at about :2141 says). Update the docstring at about :27.
2. Add two arms to `--self-test`, each printing one line that starts `SELF-TEST arm test-folder`: (a) a firm-token fixture under `infra/x/test/fixture.tf` is not graded; (b) the same token under `infra/latest/fixture.tf` IS graded (the control: `latest/` is not a test folder). Keep `NAMING-GATE-SELF-TEST: PASS` as the final line when every arm passes.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws, no push. `.tools/safe-commit.sh` for every commit (your edit to the gate runs in that gate at your commit; if it refuses, STOP and file a BLOCKING row). Do NOT commit the `portal` gitlink. ASCII only; Python 3.11; ruff clean. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W82-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab9-AC1" cell_refs="CT-ab-9"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>SELF-TEST arm test-folder</expect></criterion>
`CTab9-AC1` -- the new arms exist (report both their lines).

<criterion id="CTab9-AC2" cell_refs="CT-ab-9"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>NAMING-GATE-SELF-TEST: PASS</expect></criterion>
`CTab9-AC2` -- every arm passes, old and new (a control that PASSES at the base).
</proof_of_spec>

<expected_criteria>CTab9-AC1,CTab9-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~82/NFRA_CTLPLN.TO-CT-ab-9.naming-gate-test-folders.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab9-AC1,CTab9-AC2`, flip `<status>` to `complete` only when both pass and the instance is VALID (if refused as outside your grant, leave it `pending` and say so).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-9</owned_cells>
</decomp_ref>

<paths>
.tools/naming-gate.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a substring match that exempts `latest/` (arm b); the generated-file check skipped for a fixture (it runs before the exclusion); BLIND: other fixture spellings (`fixtures/`, `__tests__/`) not named by the ruling.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: MSTR msg 108754 (dell1 CTO msg 4865), row D1-W60-S3; taken by COO~C msg to MSTR 16:22Z.
