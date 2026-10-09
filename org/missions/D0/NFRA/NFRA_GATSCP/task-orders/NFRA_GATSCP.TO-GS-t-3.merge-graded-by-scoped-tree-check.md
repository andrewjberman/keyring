# TO NFRA_GATSCP.TO-GS-t-3 -- round 1 GS-t-3: a box sync and a fast-lane drain are graded by the scoped tree check on the merged bytes

<to_id>NFRA_GATSCP.TO-GS-t-3</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~2</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-t-3` (`decompositions/NFRA_GATSCP_DECOMP.md`) | **outcome_ref:** FWD-1 |
**depends_on:** `GS-t-2` merged (this order is handed to the same worker after it)

---

## WORKER FACE

### CONTEXT

`GS-t-2` gave the tree check two flags: `python .tools/missions-tree-index.py check --staged --act PATH [--act PATH ...]` (or
`--act-from-env VAR`) reads every input from the git index git resolves (`GIT_INDEX_FILE`, `GIT_DIR`) and refuses only a violation
in a project the act's paths touch, printing every other violation as `STANDING <CODE> <rule_id> <path> <detail>`. Two merge
paths still never run the tree check, so a merge is never graded on the register at all:

- `.tools/box-sync.sh` `grade_merge P1 P2 T` (:100-119): computes the merge's graded path set (paths T changes against BOTH
  parents, plus paths both sides changed since the merge base, :103-105), builds a private GIT_DIR pinned to the merge
  (`GIT_DIR="$PRIV" GIT_WORK_TREE="$ROOT" git read-tree "$t"`, :112), and runs only the row gate there (`STAGED="$paths" ...
  python "$GATE"`, :115). `make_merge` (:143-) calls it after `git merge-tree --write-tree`. Modes are `box|integrate|status`
  (:32); `box` and `integrate` need an MSTR serial, `status` is any seat. `git fetch` runs after the status branch (:97).
- `.tools/safe-merge.sh` `_sm_fast_lane` (:517-): the same merge-tree, private GIT_DIR and path set (:545-547), the row gate at
  :560, and a `commit-tree` landing, so no commit hook (and so no tree check) fires. Its in-tree path commits with `git commit`,
  which fires the hook `GS-t-2` already scoped; leave the in-tree path alone. `--self-test` (:58-140) has 25 structural arms.

### THE CELL

`GS-t-3`. box-sync's `grade_merge` and safe-merge's fast lane run the `GS-t-2` tree check on the merged bytes with the merge's
graded path set as the act; box-sync gains a read-only `grade P1 P2` mode that computes the merge and grades it, landing nothing.

**Build:**
1. In `grade_merge`, after the row gate and under the SAME private GIT_DIR, run `python .tools/missions-tree-index.py check
   --staged --act-from-env <a variable holding $paths>` (or one `--act` per path). Refuse when it returns non-zero, with a
   `box-sync: REFUSED BY THE TREE CHECK on the merge's own paths (rc=N)` line; print its STANDING lines. Do it even when the path
   set has no tree path (the check then has no in-act project and only prints STANDING), but keep the existing early `SKIP`
   when the path set is empty.
2. `bash .tools/box-sync.sh grade P1 P2`: any seat; no fetch, no lock, no ref moved, no audit row, no push. It runs `git
   merge-tree --write-tree` on P1 and P2, resolves a known-class conflict exactly as `make_merge` does or exits 4 on any other
   conflict, then `grade_merge`. Exit 0 pass, 1 refused. Add it to the usage line and the header's USAGE block.
3. In `_sm_fast_lane`, the same tree-check call on its private GIT_DIR with its graded path set, refusing the same way. Add one
   `--self-test` arm for it.

### ACCEPTANCE

<criterion id="GS3-AC1" cell_refs="GS-t-3"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_boxsync_grade.py"</invocation><expect>GS-T3-BOXSYNC ok=True</expect></criterion>
`GS3-AC1` -- a merge whose parents both carry `LGIC_BLANKFIX`'s drift (from the merge base) is graded and passes with
`STANDING LGIC_BLANKFIX`; a merge where both sides changed that row is refused (the difference control). The check builds its
commits with plumbing only; it moves no ref and touches no working-tree file.

<criterion id="GS3-AC2" cell_refs="GS-t-3"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_fastlane.py"</invocation><expect>GS-T3-FASTLANE ok=True</expect></criterion>
`GS3-AC2` -- the fast lane calls `missions-tree-index.py` with `--staged` and `--act`, and `safe-merge.sh --self-test` exits 0.

<expected_criteria>GS3-AC1,GS3-AC2</expected_criteria>

Read each check before you build. Each prints its arms and ONE last line. Both FAIL at the base. You do not edit the checks.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. Do not run `box-sync.sh box` or `integrate`, do not push, do not merge into any shared branch.
  `grade` is the only mode you exercise.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the check or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.

<paths>
.tools/box-sync.sh
.tools/safe-merge.sh
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular `.tools/missions-tree-index.py` and
the check files under `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.md</decomp_doc> (round 1), cell `GS-t-3`.
<owned_cells>GS-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GS3-AC1, GS3-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~2/NFRA_GATSCP.TO-GS-t-3.merge-graded-by-scoped-tree-check.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> GS3-AC1,GS3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the `grade` output of AC1's first arm; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; box-sync's scheduled task is not changed, only the grade it runs.
comp-iam: DECLARED-NOT-APPLICABLE the thread touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; AC1 carries the difference control (the drift inside the graded set is refused). BLIND: AC2's fast-lane arm is structural; the fast lane's seam is exercised at the issuer's one real run.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @7cb6183997 (FWD-1; C-SCOPE, C-BYTES); decomposition round 1. Base dry-run at the cut (box/dell1 95669cba44):
GS3-AC1 FAIL as expected (no grade mode, usage rc 2); GS3-AC2 FAIL as expected (fast lane not wired; self-test arm PASS).
