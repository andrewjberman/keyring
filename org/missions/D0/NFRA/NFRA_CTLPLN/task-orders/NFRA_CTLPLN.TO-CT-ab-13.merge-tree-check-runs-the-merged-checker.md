# TO NFRA_CTLPLN.TO-CT-ab-13 -- workstream MERGECHK round 1 (cell CT-ab-13): the project-tree check at a merge runs the MERGED copy of `missions-tree-index.py`, not the working tree's (MSTR msg 108862, site Z refusal)

<to_id>NFRA_CTLPLN.TO-CT-ab-13</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~86</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>MERGECHK</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-13` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`, Recut 4) | **outcome_ref:** FWD-2 |
**depends_on:** none (`CT-ab-8` is merged at your base)

---

## WORKER FACE

### THE CELL

`CT-ab-8` (merged) made `FABRIC_ENUM` in `.tools/to-pipeline-gate.py` a derived value (`tuple(_fabric_values())`) and taught `.tools/missions-tree-index.py` to read it (a literal symbol by `ast.literal_eval`, a register-derived symbol through `lib/devices.py`). MEASURED (MSTR msg 108862, site Z refusal at 19:3xZ; and on this box when worker 81's branch was merged): the project-tree check at a merge runs the WORKING TREE's `missions-tree-index.py` against the MERGE's staged bytes: `.tools/box-sync.sh` about :143 (`python "$ROOT/.tools/missions-tree-index.py" check --staged --act-from-env GRADE_ACT`) and about :177 (`check --staged --act .tools/box-sync.sh`), and `.tools/safe-merge.sh` about :618 (the same call). On a box whose working-tree checker is the OLD one, the merged gate's `FABRIC_ENUM = tuple(...)` makes `ast.literal_eval` raise `ValueError`, and the whole merge is refused. Any change to the checker that its own previous version cannot read repeats this. Extracting the whole merged tree to run its checker costs 1.1 GB and 55 s: not viable.

### BUILD

1. ONE shared helper, a shell function in a new file `.tools/merged-checker.sh` (sourced by both scripts), `merged_checker_path <git-dir> <fallback-root>`: it writes the checker the MERGE carries (`.tools/missions-tree-index.py` read from the private index at `<git-dir>`, `git --git-dir=<git-dir> show :.tools/missions-tree-index.py`) into a fresh file under the private git dir, prints that file's path, and prints the working-tree path instead (with a `merged-checker: FALLBACK` line on stderr) only when the merge does not carry the file. The checker must still resolve the repository root and its sibling files the way it does when run from `.tools/` (read the script's root discovery first; if it finds its root from its own location, pass the root explicitly or place the copy where the discovery lands on the working tree, and say which you chose).
2. Use it at the three call sites above, in `.tools/box-sync.sh` and `.tools/safe-merge.sh`; remove the temp file with the private git dir's cleanup. Change nothing else in either script.
3. A NEW test `.tools/tests/test_merged_checker.sh` (Git Bash 3.6.7 default utilities only; temporary git repositories only): case 1, a merge whose staged `missions-tree-index.py` is the CURRENT one and whose working-tree copy is the OLD one (`git show a71a0b4f68:.tools/missions-tree-index.py`) with the merged gate carrying `FABRIC_ENUM = tuple(_fabric_values())` passes the project-tree check; case 2 (the control), the same merge run the OLD way (the working-tree checker) is REFUSED with the `ValueError`; case 3, a merge that does not carry the file falls back and says so; case 4, the temp file is gone after the run. Final line `MERGED-CHECKER-TEST cases=<k>/<n> ok=<True|False>`. If a faithful temporary-repository fixture is not possible, say so and test the helper alone plus a dry read of both call sites, and state what was not exercised.
4. Run `bash .tools/safe-merge.sh --self-test` and the box-sync self-test if it has one; report each last line.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws, no push; tests in temporary directories only; do NOT run `box-sync.sh` against the real repository and do NOT run `safe-merge.sh` on a real branch (its `--self-test` only). `.tools/safe-commit.sh` for every commit (your edit to these scripts runs in the commit gate; if it refuses, STOP and file a BLOCKING row). Do NOT commit the `portal` gitlink. ASCII only; Git Bash 3.6.7-safe shell. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W86-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab13-AC1" cell_refs="CT-ab-13"><invocation>bash .tools/tests/test_merged_checker.sh</invocation><expect>ok=True</expect></criterion>
`CTab13-AC1` -- every case passes, the control arm included (report the whole last line with its denominator).

<criterion id="CTab13-AC2" cell_refs="CT-ab-13"><invocation>bash .tools/safe-merge.sh --self-test</invocation><expect>PASS</expect></criterion>
`CTab13-AC2` -- the merge refuser's own self-test still passes (a control that PASSES at the base; report its last line).
</proof_of_spec>

<expected_criteria>CTab13-AC1,CTab13-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~86/NFRA_CTLPLN.TO-CT-ab-13.merge-tree-check-runs-the-merged-checker.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab13-AC1,CTab13-AC2`, flip `<status>` to `complete` only when both pass and the instance is VALID (if refused as outside your grant, leave it `pending` and say so).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-13</owned_cells>
</decomp_ref>

<paths>
.tools/merged-checker.sh
.tools/box-sync.sh
.tools/safe-merge.sh
.tools/tests/test_merged_checker.sh
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a fallback that silently runs the old checker (case 3 requires the stderr line); a helper that leaves the temp file behind (case 4); a control arm that does not actually refuse (case 2); the root discovery of the copied checker landing on the temp directory instead of the repository; BLIND: a box whose private index lacks the checker path for another reason (the fallback line names it).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: MSTR msg 108862 (site Z bus ee09d867); the merge of worker 81 (CT-ab-8) on this box needed a two-step bridge for the same cause.
