# NFRA_GATSCP -- surprise channel, INVESTIGATION v1

**Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A worker's row on dell1 is `NFRA_GATSCP-D1-W<n>-S<k>`.
**Append-only during the round.** Never edit an existing row.

## NFRA_GATSCP-D1-W2-S1 -- the tree-index wrapper test was already RED at the base (stale arm count 18, tool prints 38)

```json
{
  "id": "NFRA_GATSCP-D1-W2-S1",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_GATSCP~2",
  "surfaced_at": "2026-10-09T08:03:00Z",
  "one_line": "TO-GS-t-2 says the wrapper test .tools/tests/test_missions_tree_index_selftest.py keeps passing, but at the base it fails W2 (EXPECTED_ARMS = 18, the tool prints 38/38); the channel file named in <paths> also did not exist.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/tests/test_missions_tree_index_selftest.py at base a18420e142 (before any edit): 'FAIL  W2 DENOMINATOR: 18/18  (printed 38/38)' and 'MISSIONS-TREE-INDEX WRAPPER: 3/4 PASS (denominator 4)'",
      "git log -1 -- .tools/tests/test_missions_tree_index_selftest.py = 6eac560149; git log -1 -- .tools/missions-tree-index.py = 651f750a5a (the tool grew arms after the wrapper pinned 18; its own header says a tool change that adds arms updates EXPECTED_ARMS in the same commit)",
      "ls org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel at base a18420e142: no such directory; this file was created by 0.9.0_WK_NFRA_GATSCP~2 with this row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-GS-t-2 build step 4: 'Keep .tools/tests/test_missions_tree_index_selftest.py passing' (a premise that it passes now), and <paths> names an existing INVESTIGATION_v1.md.",
  "world_is": "The wrapper was RED at the base on W2 only. The file is inside this order's <paths>, so EXPECTED_ARMS was set to the new self-test count (52) in the same commit as the arms (wrapper 4/4 PASS afterwards); no rule, mutant anchor or other wrapper arm was changed. The channel file was absent and is created with this row.",
  "notes": "Worker 2 of NFRA_GATSCP. The order names the id form NFRA_GATSCP-W2-S<k>; the row gate refuses a bare id with fabric dell1 (a bare id is the laptop's), so the dell1 coordinate D1- is carried. The disposition is the CVO's."
}
```

## NFRA_GATSCP-D1-W2-S2 -- GS3-AC1 arm 1 cannot pass: its merge has an EMPTY graded path set, which the order says to SKIP

```json
{
  "id": "NFRA_GATSCP-D1-W2-S2",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_GATSCP~2",
  "surfaced_at": "2026-10-09T08:15:37Z",
  "one_line": "TO-GS-t-3 says keep grade_merge's early SKIP on an empty graded path set, and r1_boxsync_grade.py arm 1 (bystander-lands) requires a STANDING line from a merge whose graded path set is empty, so the order and its check contradict.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r1_boxsync_grade.py arm 1 builds X = B0 + probe_x and Y = B0 + probe_y (B0 = HEAD + bystander drift); box-sync's graded set = (diff X..T) AND (diff Y..T) = {probe_y} AND {probe_x} = empty, plus (diff B0..X) AND (diff B0..Y) = {probe_x} AND {probe_y} = empty; box-sync.sh grade prints 'grade SKIP -- the merge introduces nothing and no path changed on both sides' and 'graded=0/1', rc 0, no STANDING line",
      "arm 2 (X1,Y1 both carry the drift from HEAD): rc=1, 'ACT SCOPE: in-act=1 STANDING=0 (act projects: LGIC_BLANKFIX)', 'REFUSED BY THE TREE CHECK' -- passes",
      "positive control with a NON-empty graded set (both sides write probe_s identically, plus probe_x / probe_y): grade rc 0, 'ACT SCOPE: in-act=0 STANDING=1 (act projects: NFRA_GATSCP)' and 'STANDING LGIC_BLANKFIX INDEX-DRIFT org/projects/LGIC_BLANKFIX.json ...', 'graded=1/1' -- the wiring works; only the empty-set case is out of reach"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-GS-t-3 build 1: 'keep the existing early SKIP when the path set is empty'; GS3-AC1: a merge whose parents both carry the drift from the merge base is graded and passes with STANDING LGIC_BLANKFIX.",
  "world_is": "For arm 1's merge the path set is empty, so the SKIP returns before any tree check runs and no STANDING line can print; the tree check itself refuses an empty act (rc 2). Both statements cannot hold. Not weakened: the SKIP stays as ordered and the check is unedited, so GS3-AC1 reads FAIL (arm 1) and the order stays open. A resolution is the issuer's: either the check builds a merge with a non-empty graded set (e.g. both sides write the same probe file), or the order lets grade_merge run the tree check informationally (every violation STANDING) on an empty set.",
  "notes": "Worker 2 of NFRA_GATSCP. The rest of the order is built: grade mode, grade_merge tree check, fast-lane tree check, self-test arm (GS3-AC2 passes)."
}
```

```json
{
  "id": "NFRA_GATSCP-D1-W2-S3",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_GATSCP~2",
  "surfaced_at": "2026-10-09T08:23Z",
  "one_line": "NFRA_GATSCP-D1-W2-S2 is resolved by AMENDMENT 2 @f980747a55: r1_boxsync_grade.py now adds the same new file on both sides, so the graded set is non-empty; GS3-AC1 last line 'GS-T3-BOXSYNC ok=True arms=2 failed=0'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python r1_boxsync_grade.py at the amended bytes (git show f980747a55): rc=0; bystander-lands PASS standing_LGIC_BLANKFIX=True (graded=1/0); own-refused PASS rc=1 (graded=1/1); last line 'GS-T3-BOXSYNC ok=True arms=2 failed=0'",
      "box-sync.sh and safe-merge.sh unchanged since c8d936bf7a; the SKIP stays"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 2: the check builds a merge with a non-empty graded set and the SKIP stays.",
  "world_is": "Amended check passes 2 of 2 arms against the unchanged build; D1-W2-S2 (issuer-side defect) is resolved by the amendment.",
  "notes": "Worker 2 of NFRA_GATSCP closing TO-GS-t-3."
}
```

```json
{
  "id": "NFRA_GATSCP-D1-W2-S4",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_GATSCP~2",
  "surfaced_at": "2026-10-09T08:27Z",
  "one_line": "The lane gate refuses committing the amended check file r1_boxsync_grade.py on this branch: the order's <paths> does not name it (lane TREE_DELIVERABLES, ADHC_OWNPTH.005), so the copy of f980747a55 stays uncommitted in the worktree; the bytes already exist at f980747a55 on box/dell1.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit with the four paths of the close instruction: 'VIOLATION: .../round1_prep/checks/r1_boxsync_grade.py -- lane=TREE_DELIVERABLES ... WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block'",
      "order <paths> block: .tools/box-sync.sh, .tools/safe-merge.sh, INVESTIGATION_v1.md; the order also says the check files are READ-only for the worker"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Close instruction step 5: one commit carrying the order, the check copy, the proof instance and the investigation file.",
  "world_is": "The gate admits only the order's <paths>; the check copy cannot ride this branch's commit. The three other paths are committed; the criteria were run against the byte-identical copy in the worktree. The issuer may take the check file from f980747a55 at the drain.",
  "notes": "No override used."
}
```
