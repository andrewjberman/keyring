# TO NFRA_GATSCP.TO-GS-e-1 -- round 2 GS-e-1: every box sync shows the standing defects it carries, and says how many

<to_id>NFRA_GATSCP.TO-GS-e-1</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~3</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-e-1` (`decompositions/NFRA_GATSCP_DECOMP.round2.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

`.tools/box-sync.sh` grades every merge it makes in `grade_merge P1 P2 T` (:104-131). It computes the merge's graded path set
(paths T changes against both parents, plus paths both sides changed), and when that set is EMPTY it returns at :112 with
`box-sync: grade SKIP -- ...` before anything runs. A sync that takes CLOUD usually has an empty set, so a box carrying another
project's fresh error prints nothing about it. When the set is non-empty, :119 runs the row gate (`STAGED="$paths" ... python
"$GATE"`, the corpus pass inside it only when a path is a surprise-channel document) and :127 runs the tree check (`GRADE_ACT="$paths"
... missions-tree-index.py check --staged --act-from-env GRADE_ACT`), both under the private `GIT_DIR="$PRIV"` pinned to the merge.

The CTO ruled (R1): a sync SHOWS standing defects as information, never as a refusal, and says `0 standing` when there are none.
Both tools already do the showing when given an act that belongs to no project:
- `python .tools/missions-tree-index.py check --staged --act <a path in no project>` puts every violation on a
  `STANDING <CODE> <rule> <path> <detail>` line and returns 0.
- `python .tools/surprise-corpus-validate.py --act <a path that is no channel document>` puts every NEW failure on a
  `STANDING <CODE> surprise-corpus ...` line; it still returns 1 for a RESOLVED tuple or a missing baseline.
`bash .tools/box-sync.sh grade P1 P2` (any seat, read-only) runs the same `grade_merge`.

### THE CELL

`GS-e-1`. box-sync's `grade_merge` shows standing defects on every sync, as information, plus `box-sync: N standing`.

**Build** in `.tools/box-sync.sh`, inside `grade_merge` only:
1. When the graded set is empty: keep the `grade SKIP` line, then, under a private GIT_DIR pinned to the merge exactly as the
   non-empty branch builds it, run the tree check and the corpus pass with an act that belongs to no project and no channel
   (use `.tools/box-sync.sh` itself as the act path). Print their `STANDING ` lines. Their exit codes never refuse this
   information pass; a tool that cannot run prints one `box-sync: WARN standing pass could not run (<tool> rc=N)` line.
   Return 0, as today.
2. When the graded set is non-empty: grade exactly as today (refusal power unchanged), and add the corpus pass's standing view
   when no channel path was in the set (the row gate does not run the pass then), as information only.
3. In both cases, the last line `grade_merge` prints is `box-sync: <N> standing`, where N counts the `STANDING ` lines the
   sync printed (0 included). Clean up every private dir, as the existing code does.

### ACCEPTANCE

<criterion id="GE1-AC1" cell_refs="GS-e-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/r2_sync_standing.py"</invocation><expect>GS-E1-SYNC ok=True</expect></criterion>
`GE1-AC1` -- an empty-set sync over a base carrying `LGIC_BLANKFIX`'s drift and channel failure prints both as STANDING and a count
two above the clean sync's count; a sync where both sides changed the bystander's row still refuses (the negative arm, P1).

<criterion id="GE1-AC2" cell_refs="GS-e-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_boxsync_grade.py"</invocation><expect>GS-T3-BOXSYNC ok=True</expect></criterion>
`GE1-AC2` -- round 1's grade check still passes (no regression in the non-empty branch).

<expected_criteria>GE1-AC1,GE1-AC2</expected_criteria>

Each check builds unreferenced commits with plumbing; it moves no ref and touches no working-tree file. Read both before you build.
Each prints its arms and ONE last line. AC1 FAILs at the base. You do not edit the checks.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. Do not run `box-sync.sh box` or `integrate`, do not push, do not merge into any shared branch.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W3-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the check
  or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.

<paths>
.tools/box-sync.sh
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round2.md</decomp_doc> (round 2), cell `GS-e-1`.
<owned_cells>GS-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GE1-AC1, GE1-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~3/NFRA_GATSCP.TO-GS-e-1.proof_of_spec.json` with `to_id`
`NFRA_GATSCP.TO-GS-e-1`, validated with `python .tools/proof-of-spec-check.py <instance> GE1-AC1,GE1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the `grade` output of AC1's second arm; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE box-sync's scheduled task keeps its trigger; only the grade's output changes.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is touched.
comp-adversary: RUN -- AC1 arm 3 is the negative arm (a defect the sync introduces still refuses); the count is measured against the same box's clean sync, so an organic standing defect cannot fake or break it.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @5c65160327 item 1, ruling R1; decomposition round 2. Base dry-run (box/dell1 7611122124): GE1-AC1
FAIL as expected (no count line; the SKIP is silent); GE1-AC2 PASS as expected (a control).
