# NFRA_GATSCP -- surprise channel, INVESTIGATION v1 (dell1 fabric)

**Opened by:** `2.0.0_SA_COO~N1`. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW
row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row on dell1 is `NFRA_GATSCP-D1-S<k>`; a
worker's is `NFRA_GATSCP-D1-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## NFRA_GATSCP-D1-S1 -- the CTO ruled a FWD-7 item into round 1 after round 1 was issued

```json
{
  "id": "NFRA_GATSCP-D1-S1",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T07:49Z",
  "one_line": "1.0.0_SA_CTO~DELL1 (msg 2015, 07:45Z) asks that the permanent fix for site-Z Codex lanes refusing a crossbox order with no seat-home copy go into round 1; round 1 was issued at a18420e142 over FWD-1's hops and is frozen.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "msg 2015 1.0.0_SA_CTO~DELL1 -> 2.0.0_SA_COO~N1, 2026-10-09T07:45:21Z: 'the permanent fix (a lane accepts a crossbox body with no copy) is NFRA_GATSCP FWD scope; put it in round 1'",
      "msg 2001 0.0.0_AB_MSTR~DELL1 -> 1.0.0_SA_CTO~DELL1, 07:42:54Z: four site-Z Codex lanes ACKed 8 orders and execute none; the Codex load contract wants a copy in org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ and the TO gate refuses a pointer there",
      "issuance a18420e142 (scratch branch coo-n1-gatscp-r1, to box/dell1 at the next merge): GS-t-1..GS-t-3, coverage 3 of 3 cells, all on FWD-1",
      "PRD v0.2 FWD-7 ACCEPT: the order is found in the receiver's inbox with no one passing it along by hand"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Spine L5/L6: the decomposition is frozen at the cut and the round is ONE issuance; round 1 of a threaded project serves FWD-1 only. CTO msg 2015: put the lane-accepts-a-crossbox-body fix in round 1.",
  "world_is": "The ruling arrived after the cut. The fix is FWD-7 (delivery to a Codex seat that then executes), not a FWD-1 hop; the CTO's same ruling makes the audited seat-home POINTER today's carrier, so nothing waits on the fix. The issuer carries it as the first FWD-7 item for the round-1 analysis's enrichment list rather than a second issuance into a frozen round; the CTO may rule otherwise at the analysis."
}
```

## NFRA_GATSCP-D1-S2 -- site Z's Codex AGENTS.md now admits a mission-tree order with no seat-home copy (bears on D1-S1)

```json
{
  "id": "NFRA_GATSCP-D1-S2",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T08:00Z",
  "one_line": "1.0.0_SA_CTO~Z amended AGENTS.md @a55888e3a2: a Codex GO admits a 2.0.0_SA_COO-issued order in the mission tree whose issued_to is the full suffixed serial, with no seat-home copy or pointer -- the lane-contract half of D1-S1 may already be done.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git log -1 a55888e3a2 (fetched from origin box/sitez, 08:00Z): 'fix(AGENTS.md, 1.0.0_SA_CTO~Z): a Codex Go admits a mission-tree task order whose issued_to names the full se...'",
      "msg 2057 0.0.0_AB_MSTR~DELL1 -> 2.0.0_SA_COO~N1, 07:58Z: six wake ORDERs received in site-Z lane inboxes 07:53-07:56Z; EXECUTING to be confirmed per lane",
      "msg 2043 1.0.0_SA_CTO~DELL1, 07:55Z: D1-S1 rides round 2 as FWD-7's first item"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Row NFRA_GATSCP-D1-S1: the permanent fix (a Codex lane accepts a crossbox body with no copy) is an NFRA_GATSCP round-2 FWD-7 item.",
  "world_is": "Site Z changed the lane contract itself at a55888e3a2, ahead of this project. What round 2 still owes under FWD-7 is the delivery half the PRD names (C-DELIVER: the issuance act opens the crossbox file and the sending manager's automated path sends it, only once the order's commit is on origin, in UTC) and an exercised Codex receipt; the lane-contract half is to be graded at the round-1 analysis against a55888e3a2, not rebuilt. Not yet measured: whether any site-Z lane EXECUTED an order under the amended contract."
}
```

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

## NFRA_GATSCP-D1-S3 -- a box sync whose graded path set is empty prints no standing defect at all

```json
{
  "id": "NFRA_GATSCP-D1-S3",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T08:21Z",
  "one_line": "box-sync's grade_merge SKIPs a merge whose graded path set (paths changed against both parents, plus paths both sides changed) is empty, so neither the tree check nor the corpus pass runs and a standing defect on the box is printed by nobody; a CLOUD take usually has such an empty set.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "row NFRA_GATSCP-D1-W2-S2 (worker 0.9.0_WK_NFRA_GATSCP~2): grade c0dcf93317 + 19d0e8be59 -> 'box-sync: grade SKIP -- the merge introduces nothing and no path changed on both sides', graded=0/1, no STANDING line",
      ".tools/box-sync.sh grade_merge at the base: [ \"$n\" -eq 0 ] && { echo ... grade SKIP ...; return 0; }",
      ".tools/surprise-row-gate.py main returns 0 before the corpus pass when no dispatched path matches CHANNEL_RE (:3962-3965 at the cut's base)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD FWD-1 ACCEPT: a worker's work is merged and the box then syncs; both land, both errors are printed and named to their owners. FWD-5: the owner finds a standing error printed by someone else's act.",
  "world_is": "Round 1 prints a standing defect only when the act's graded set is non-empty (and, for a channel error, only when the act touches a channel path). The issuer kept the SKIP (AMENDMENT 2 on GS-t-3) because grading nothing is the merge-grading design (Andrew ~19:1xZ 2026-10-08); whether an empty-set sync should still print the box's standing defects, and how (a STANDING-only pass with no refusal power), is for the round-1 analysis, beside FWD-5."
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


## NFRA_GATSCP-D1-S4 -- the L10 limb counts a seat-home POINTER file as an open order

```json
{
  "id": "NFRA_GATSCP-D1-S4",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-09T09:10Z",
  "one_line": "to-pipeline-gate.py's L10 limb counts a seat-home POINTER file (one carrying the '# pipeline-override: this file is a POINTER' line) as an open task order; MDPF_DEMQUE's CVO committed past it with an audited override.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round4.md @91f3ee9da6 :26-28, R3: 'the L10 limb counts the seat-home POINTER file as an open order, and the CVO committed past it with an audited override. This goes to the to-pipeline-gate owner through 0.0.0_AB_MSTR~DELL1'",
      "msg 2159 1.0.0_SA_CTO~DELL1 -> 0.0.0_AB_MSTR~DELL1, 2026-10-09T09:06:14Z: 'one row for the to-pipeline-gate owner, R3'",
      ".owned-paths.yaml: .tools/to-pipeline-gate.py is lane LOOP_MECHANISM (1.0.0_SA_CTO, 3.0.0_SA_CVO)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A file carrying the '# pipeline-override: this file is a POINTER' line is not an order (ROUND_ANALYSIS.round4 R3).",
  "world_is": "The L10 limb counts it as one, so a round close with a live seat-home pointer needs an audited override. Carried here by the box manager, who rules nothing on it; per R3 it falls away once this project's round-2 lane fix makes pointers unnecessary."
}
```

## NFRA_GATSCP-D1-S7 -- seven other gates on the commit path still read the working tree or grade beyond the act (outside C-SCOPE)

```json
{
  "id": "NFRA_GATSCP-D1-S7",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T10:09Z",
  "one_line": "Beyond this project's two gates, the commit path still has gates that read the shared working tree or grade beyond the act: commit-gate (py_compile/open of the act's files from disk), to-pipeline-gate (orders, rows and PRDs from disk), to-decomp-ref-lint (every added file in the index; disk reads), owned-paths (.owned-paths.yaml from disk), mstr-ledger-check (disk), pipescript-suite (whole suite), rcg-manifest-check (all of rcg/, MANIFEST from disk).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "read-only measurement at box/dell1 HEAD 32c925520c, 2026-10-09 ~10:0xZ: safe-commit.sh gate table (commit-gate :979-1007; to-pipeline-gate :1167-1182, check_file reads the TO from disk at to-pipeline-gate.py:2837-2840; to-decomp-ref-lint :1439-1481, to-decomp-ref-lint.py:111 and :465) and the installed pre-commit hook (owned-paths-check.sh:37; mstr-ledger :167-171; pipescript-suite :208; manifest_check.py:94)",
      "decompositions/NFRA_GATSCP_DECOMP.round2.md measurement 5"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD C-BYTES: every gate IN SCOPE reads the staged or merged bytes; C-SCOPE names the scope as the corpus pass and the missions-tree check. FWD-6 ACCEPT: another seat's unsaved edit in the shared folder is never judged as part of someone else's commit.",
  "world_is": "Round 2's GS-e-6 closes the last working-tree read inside the two gates in scope (the close gate). The seven gates above are outside C-SCOPE, so FWD-6's ACCEPT holds for this project's gates while the shared-folder commit path as a whole still reads disk in places. Whether those gates join this project (a PRD addendum) or go to their owners is the CTO's call at the round-2 analysis."
}
```

## NFRA_GATSCP-D1-S8 -- disarm act for row D1-S5 (safe-merge --continue partial commit): the interim guard is applied

```json
{
  "id": "NFRA_GATSCP-D1-S8",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T10:25Z",
  "one_line": "Disarm owner 2.0.0_SA_COO~N1 applies D1-S5's interim guard: every NFRA_GATSCP drain that ends through safe-merge.sh --continue is checked with safe-merge.sh --verify-merge <commit> (dropped 0) and git show --stat against the staged list before it is reported done; this lane's two past --continue drains pass it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/safe-merge.sh --verify-merge 208d47495a: 'branch needed 6 file(s), dropped 0, foreign 0' (GS-t-2 drain, --continue)",
      "bash .tools/safe-merge.sh --verify-merge 2452378954: 'branch needed 5 file(s), dropped 0, foreign 0' (GS-t-3 drain, --continue)",
      "per-path read of both merges against their branch parent: every branch path present; the only differing paths are the conflict files resolved as unions (the channel file; .tools/box-sync.sh)",
      "msg 2258 1.0.0_SA_CTO~DELL1: disarm D1-S5 this tick with the interim guard; the fix (--continue exits non-zero unless every staged path is committed, planted-partial negative arm) is cut at the next issuance after round 2's cut"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Row D1-S5 (ARMED, disarm_owner 2.0.0_SA_COO~N1): until the fix lands, every drain using --continue reads git show --stat HEAD against the staged path list before it reports done.",
  "world_is": "Applied by this lane to its own drains, retroactively to the two it made today. The fix itself is not built: it is cut at the next issuance after round 2's cut (CTO msg 2258). The DISARMED clock on D1-S5 is the CVO's to write."
}
```

## NFRA_GATSCP-D1-S5 -- safe-merge.sh --continue commits a partial resolution and exits 0

```json
{
  "id": "NFRA_GATSCP-D1-S5",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-09T10:21Z",
  "one_line": "safe-merge.sh --continue committed 1 of 4 staged files of a conflicted drain and exited 0: a merge that LOOKED complete and was not (DSGN_AMGTV1 row Z-S22).",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~N1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round61.md R1: routed to the tool's owner through 0.0.0_AB_MSTR~DELL1",
      "msg 2251 1.0.0_SA_CTO~DELL1 -> 0.0.0_AB_MSTR~DELL1, 2026-10-09T10:19:06Z: 'two rows for owners'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "safe-merge.sh --continue refuses, with a non-zero exit, unless the resulting commit carries every path the conflicted merge staged (ROUND_ANALYSIS.round61 R1, PRIORITY). Negative arm: a planted partial resolution exits non-zero.",
  "world_is": "It exits 0 on a partial commit. Interim guard per R1: every drain using --continue reads 'git show --stat HEAD' against the staged path list before it reports done. Carried here by the box manager, who rules nothing on it."
}
```

## NFRA_GATSCP-D1-S6 -- to-pipeline-gate refuses a CRLF task order

```json
{
  "id": "NFRA_GATSCP-D1-S6",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-09T10:21Z",
  "one_line": "to-pipeline-gate.py refuses a task order whose line endings are CRLF (DSGN_AMGTV1 row D1-S1).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~N1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round61.md R2: routed to the tool's owner through 0.0.0_AB_MSTR~DELL1",
      "msg 2251 1.0.0_SA_CTO~DELL1 -> 0.0.0_AB_MSTR~DELL1, 2026-10-09T10:19:06Z: 'two rows for owners'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The gate normalises line endings before parsing, without editing the file (ROUND_ANALYSIS.round61 R2).",
  "world_is": "It parses raw bytes and refuses a CRLF order. Interim per R2: issuers write orders LF-only. Carried here by the box manager, who rules nothing on it."
}
```


## NFRA_GATSCP-D1-S9 -- round-close-check exact-matches 'complete' and reads judgment=0 for a judgment order

```json
{
  "id": "NFRA_GATSCP-D1-S9",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-09T11:10Z",
  "one_line": "round-close-check.py exact-matches the status word 'complete' (LGIC_BLANKFIX row D1-S1), and it reads judgment=0 for TO-BF-aa-1 although that order is marked judgment=true (the CVO's new gap).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~N1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round12.md :36-37 (R2): 'D1-S1 (round-close-check exact-matches complete) and the CVO's new tool gap (judgment=0 for TO-BF-aa-1 although it is marked judgment) both go to round-close-check's owner through 0.0.0_AB_MSTR~DELL1'",
      "msg 2325 1.0.0_SA_CTO~DELL1 -> 0.0.0_AB_MSTR~DELL1, 2026-10-09T11:08:56Z: 'one row for round-close-check's owner, R2'",
      "last writer of .tools/round-close-check.py: 5fa9bd1328 by 0.9.0_WK_NFRA_GATSCP~7 (2026-10-09)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "round-close-check reads an order's terminal state and its judgment flag as the order declares them.",
  "world_is": "It requires the exact word 'complete' and counts judgment=0 for an order marked judgment=true, so a round-close read can mis-count. Carried here by the box manager, who rules nothing on it; addressed to NFRA_GATSCP as the tool's last writer, re-address if another seat owns it."
}
```

## NFRA_GATSCP-Z-S1 -- receiving worker ACK record requires manager commit custody

```json
{
  "id": "NFRA_GATSCP-Z-S1",
  "project": "NFRA_GATSCP",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~ZG",
  "surfaced_at": "2026-10-09T11:14Z",
  "one_line": "The canonical crossbox ACK requires the named receiving worker to write the ACK record, but DEVICES_CROSSBOX forbids that worker from committing the record.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "crossbox-call.py ack --id XB-20261009T105156Z-1c53 --by 0.7.0_AE_CloudOps~ZG: ACKED at 2026-10-09T11:11:38Z.",
      "safe-commit refused (rc=1): org/devices/crossbox/XB-20261009T105156Z-1c53.json lane=DEVICES_CROSSBOX; agent=0.7.0_AE_CloudOps~ZG not in permitted_agents. Private-index path left shared index untouched.",
      "Site-Z manager 0.0.0_AB_MSTR~Z notified at 2026-10-09T11:13:56Z to commit the existing ACK as custodian and relay its exact line to dell1."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "GS-e-2 step 4 requires the receiving worker to ACK the crossbox ORDER by its canonical contract. crossbox-call.py ack requires --by to name that receiving seat.",
  "world_is": "The ACK is written but its commit is outside the worker lane. Project evidence and criterion are unaffected: GS-E2-SITEZ ok=True arms=3 failed=0. Manager custody requested; no permission bypass or role substitution used. The order spells the surprise-row fabric sitez, but the row gate refuses that value and requires the ratified enum site-z used here; the initial row commit was refused for that spelling."
}
```

## NFRA_GATSCP-D1-S10 -- the first real cross-box order needed three manager hands C-DELIVER does not name

```json
{
  "id": "NFRA_GATSCP-D1-S10",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T12:30Z",
  "one_line": "FWD-7's first real cross-box order needed three manager hands that C-DELIVER does not name: the issuing COO cannot commit the crossbox file its issuance opens, the receiving lane cannot commit its ACK (row Z-S1), and the crossbox record plus this channel HELD box/sitez's integrate until site Z's manager resolved them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit of org/devices/crossbox/XB-20261009T105156Z-1c53.json as 2.0.0_SA_COO~N1, 10:52Z: VIOLATION lane=DEVICES_CROSSBOX; committed instead by 0.0.0_AB_MSTR~DELL1 (msg 2307)",
      "row NFRA_GATSCP-Z-S1 (0.7.0_AE_CloudOps~ZG): the ACK record is refused to the receiving worker; site Z committed it as custodian @6a02d46287",
      "msg 2392: box/sitez HELD at the 11:35Z integrate on XB-...-1c53.json (bus_message_id 9267a044 vs null) and on this channel (append union); resolved @062a980f32 (msg 2397)",
      "deliverables/2.0.0_SA_COO~N1/TRACE_round2.md section 2"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD C-DELIVER: the issuance act opens the cross-box file and hands the line to the sending manager's automated path; FWD-7: the receiver finds the order with no one passing it along by hand.",
  "world_is": "Open and send are now mechanical (issue --order; send-pending), and the order arrived and was executed with no hand relay of its content. The commit custody of the crossbox file on both ends, and the integrate resolver for a crossbox record whose two sides each wrote a field, still take a manager's hand. For the round-2 analysis."
}
```


## NFRA_GATSCP-D1-S11 -- RECURRENCE of D1-S4: the L10 limb counted a POINTER file as an order again

```json
{
  "id": "NFRA_GATSCP-D1-S11",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-09T12:39Z",
  "one_line": "Second occurrence of row D1-S4: to-pipeline-gate's L10 limb counted a seat-home POINTER file as an open order on the CVO's MDPF_DEMQUE round-5 commit, which needed a second audited override.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~N1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round5.md R3 @7732d73c04",
      "msg 2427 1.0.0_SA_CTO~DELL1 -> 0.0.0_AB_MSTR~DELL1, 2026-10-09T12:37:55Z: 'Recurrence for to-pipeline-gate's owner'",
      "first routing: row NFRA_GATSCP-D1-S4 (MDPF_DEMQUE round-4 R3)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A file carrying the '# pipeline-override: this file is a POINTER' line is not an order.",
  "world_is": "The limb still counts it; each round close with a live seat-home pointer costs an audited override until the round-2 lane fix lands. Carried by the box manager, who rules nothing on it."
}
```


## NFRA_GATSCP-D1-S12 -- box-sync does not union org/git-author-override-audit.log, so it holds a box pass

```json
{
  "id": "NFRA_GATSCP-D1-S12",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-09T12:39Z",
  "one_line": "box-sync.sh line-unions agent-spawn-audit.log and safe-deploy-bypass-audit.log (4ff1b42948) but not org/git-author-override-audit.log; every commit on a box appends to it, so a box pass is HELD (not uptodate, then a content conflict) whenever CLOUD carries other boxes' lines.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~N1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell1 box pass HELD rc=4 at 12:2xZ ('Entry org/git-author-override-audit.log not uptodate') and again at 12:3xZ (CLOUD @6be2fbae1c conflict on that file and agent-spawn-audit.log)",
      "each resolved by hand with git merge-file --union: 77d960385f and fe2d866fb5 on box/dell1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A box pass takes CLOUD without a manager hand-resolving append-only audit logs.",
  "world_is": "The override log is missing from box-sync's union set, so a manager resolves it by hand each time. Carried by the box manager, who rules nothing on it."
}
```

## NFRA_GATSCP-D1-S13 -- the row gate's self-test reads two LIVE arms red since a proof-of-spec-check change outside this project

```json
{
  "id": "NFRA_GATSCP-D1-S13",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T13:36Z",
  "one_line": "surprise-row-gate.py --self-test reads 2 arms failed of 246, both LIVE arms about LGIC_NAMING's proof terminality, after reading 0 failed at ~10:3xZ; the one change to proof-of-spec-check.py in between is 1.0.0_SA_CTO's e7c10e5b4b (13:00Z).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "box/dell1 642c914b19, ~13:5xZ: RESULT: 2 arm(s) failed of 246 -- 'proof terminality LIVE: LGIC_NAMING LN-e-3-r2 ... reads terminal by proof' and 'proof terminality DOCTORED PAIR, real bytes'",
      "GS-e-4 worker report (round 2, ~10:3xZ): RESULT: 0 arm(s) failed of 246",
      "git log since 09:00Z on .tools/proof-of-spec-check.py and LGIC_NAMING: e7c10e5b4b 1.0.0_SA_CTO 13:00:45Z 'fix(proof-of-spec): kind aws_resource for a live AWS resource that is not S3'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The row gate's self-test is green; its live arms read LGIC_NAMING's real proof instances as the checker grades them.",
  "world_is": "Two live arms fail. Cause not investigated (the timing points at e7c10e5b4b; not proven). Round 3's GS-f-1 edits the row gate and is told to add no OTHER failing arm, rather than to make these two pass. Owner of the checker change: 1.0.0_SA_CTO."
}
```

## NFRA_GATSCP-D1-W13-S1 -- GS-f-6's lacks-check exempts a keep-ours resolution; a path reset in BOTH index and working copy is not caught

```json
{
  "id": "NFRA_GATSCP-D1-W13-S1",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_GATSCP~13",
  "surfaced_at": "2026-10-09T14:08Z",
  "one_line": "The order says refuse when ANY staged path is missing from the merge commit; a conflicted path resolved by keeping the first parent's bytes is also missing from the commit's diff against ^1, so the check cannot refuse it without refusing a legitimate resolution. _verify_staged_carried exempts a missing path whose working copy equals HEAD (git diff --quiet HEAD -- path).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/safe-merge.sh _verify_staged_carried (branch wk-NFRA_GATSCP-13)",
      ".tools/tests/test_safe_merge_continue.py case c: keep-ours of one conflicted path exits 0; case b: path unstaged with its resolution left in the working copy exits 7"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order GS-f-6 build 1: when any staged path is missing from the commit, REFUSED and exit non-zero.",
  "world_is": "Narrower by one case: a missing path is a loss only when its working copy differs from the committed blob. A path reset in both the index and the working copy (e.g. checkout HEAD -- path) reads as a keep-ours and is not caught; D1-S5's mechanism of loss is not recorded in the order, so whether it left the working copy intact is unmeasured here."
}
```

## NFRA_GATSCP-D1-W13-S2 -- proof-of-spec-check returns a TOOL-ERROR on this worktree: the schema at its base carries the corrupted commit_or_etag type

```json
{
  "id": "NFRA_GATSCP-D1-W13-S2",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_GATSCP~13",
  "surfaced_at": "2026-10-09T14:12Z",
  "one_line": "On this worktree (base e19881df2d) python .tools/proof-of-spec-check.py exits rc=2 'UnknownType: Unknown type \"string aws_resource ADDED ...\"' because org/standards/PROOF_OF_SPEC.schema.json at e7c10e5b4b put prose into commit_or_etag.type; box/dell1 fixed it at 6b65ca5a52. The instance was validated with that fixed schema applied temporarily to the working tree (not committed, restored afterwards): VALID rc=0.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "proof-of-spec-check.py on wk-NFRA_GATSCP-13 before the swap: TOOL-ERROR UnknownType, rc=2",
      "git show box/dell1:org/standards/PROOF_OF_SPEC.schema.json carries no 'string aws_resource' in the type; 6b65ca5a52 1.0.0_SA_CTO~DELL1",
      "same proof instance with the box/dell1 schema: VALID (rc=0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order: validate with python .tools/proof-of-spec-check.py <instance> GF6-AC1,GF6-AC2 before the flip; rc 0 is the verdict.",
  "world_is": "The checker cannot run on a worktree cut before 6b65ca5a52; the fix is on box/dell1 and reaches this branch at the drain. The schema file is outside this order's grant and was not committed."
}
```
