# TO NFRA_GATSCP.TO-GS-f-6 -- round 3 GS-f-6: safe-merge --continue refuses a merge commit that does not carry every path the conflicted merge staged

<to_id>NFRA_GATSCP.TO-GS-f-6</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~13</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-f-6` (`decompositions/NFRA_GATSCP_DECOMP.round3.md`) | **outcome_ref:** FWD-6 |
**rows:** D1-S5 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

`.tools/safe-merge.sh` leaves a CONFLICTED merge open and finishes it with `--continue` (the limb :383-442 checks a merge
is open, the `$STATE` file, the lock, no unresolved paths, and foreign staged paths against `$STATE` (:427-430)). The shared path
then snapshots a private index (:702-703), drops late paths outside `HEAD..MERGE_HEAD` (:708-714), grades with the row gate
(:738-778), commits at :850 (`GIT_INDEX_FILE="$_PRIV_IDX" git commit --no-edit --author "$_AUTH" -m "$SUBJECT"`) and then runs
`_verify_merge_tree HEAD` (:867) and `_verify_shared_index HEAD` (:875). On conflicted parents `_verify_merge_tree` only WARNs on a
partial drop (:304-307), and nothing compares the committed paths with the paths the merge staged. Row D1-S5 (ARMED): a drain's
`--continue` committed 1 of 4 staged files and exited 0. `--self-test` (:57-145) has 28 structural arms; it states "NO GREEN MERGE
ARM" and points to `.tools/exercise-safe-merge-continue.sh`.

### THE CELL

`GS-f-6`. Safe-merge --continue refuses a merge commit that does not carry every path the conflicted merge staged.

**Build:**
1. After the merge commit on the `--continue` path (and the in-tree path generally), compare the paths the merge commit
   changes against its first parent with the paths the conflicted merge staged (`$STATE`'s list, plus every path that differs
   between HEAD and MERGE_HEAD the resolution kept). When any staged path is missing from the commit, print
   `safe-merge: REFUSED -- the merge commit lacks N staged path(s): <paths>` and exit non-zero (choose a code distinct from the
   existing ones and document it in the header's EXIT CODES). Do not rewrite or reset the commit; say how to recover in one line.
2. Write `.tools/tests/test_safe_merge_continue.py`: in a throwaway linked worktree of THIS repository on a scratch branch (never a
   shared branch; removed at the end, its branches deleted), build two branches that conflict on two files, run
   `bash .tools/safe-merge.sh <branch>` to open the conflict, then (a) resolve BOTH and `--continue`: exit 0, both files in the
   commit; (b) the planted partial: resolve both but unstage one resolved path the way D1-S5's drain lost it, then `--continue`:
   non-zero, the REFUSED line names it. Print one last line `SM-CONTINUE ok=<True|False> cases=<passed>/<total>`. No push, no
   shared branch moved.

### ACCEPTANCE

<criterion id="GF6-AC1" cell_refs="GS-f-6"><invocation>python .tools/tests/test_safe_merge_continue.py</invocation><expect>SM-CONTINUE ok=True</expect></criterion>
`GF6-AC1` -- the full resolution exits 0 with both files committed; the planted partial exits non-zero naming the missing path (the negative arm).

<criterion id="GF6-AC2" cell_refs="GS-f-6"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_fastlane.py"</invocation><expect>GS-T3-FASTLANE ok=True</expect></criterion>
`GF6-AC2` -- safe-merge's self-test stays green and the fast lane keeps its tree check (a control).

<expected_criteria>GF6-AC1,GF6-AC2</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~13/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W13-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/safe-merge.sh
.tools/tests/test_safe_merge_continue.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round3.md</decomp_doc> (round 3), cell `GS-f-6`.
<owned_cells>GS-f-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GF6-AC1, GF6-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~13/NFRA_GATSCP.TO-GS-f-6.continue-refuses-a-partial-commit.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-f-6`,
validated with `python .tools/proof-of-spec-check.py <instance> GF6-AC1,GF6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** every criterion's last line whole; the self-test's last line; rows; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- each criterion carries its negative or control arm (decomposition round 3, battery); BLIND: a census's conclusions are the CTO's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @0ef2dc8325 (with ADDENDUM 1); CTO msg 2258 for D1-S5; decomposition round 3. Base dry-run: see the
issuance commit.
