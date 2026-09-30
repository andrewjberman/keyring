# Post-crash restart of NFRA_OPLGTW: residue, worktrees, OG-n-1 gateway EIP -- 2.0.0_SA_COO~O

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE
**Date:** 2026-09-29 18:00Z .. 2026-09-30 01:05Z
**Task Order:** NFRA_OPLGTW.TO-OG-n-1 (issued and drained); post-crash order (MSTR~Z 1755Z record)
**Status:** IN PROGRESS (project L7 round 3; 4 orders held on external gates)

## Objective

Restart this seat after the site-Z crash (15:34Z) per
`org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260929_1755Z_POST_CRASH_RESIDUE_CLEANUP_AND_WORKTREE_ASSESSMENT.md`:
(1) clear crash residue, (2) assess worktrees with 3.0.0_SA_CVO~O by /canonical-flow position, (3) restart the
NFRA_OPLGTW drive.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| canonical-flow | `/canonical-flow NFRA_OPLGTW --report-only` | PASS | L7 r3, SEQUENCED-BEHIND; no UNFINISHED-EDITS, no ORPHAN-WORKTREE |
| to-check | `to-check.py --all --project NFRA_OPLGTW` | PARTIAL | reads the FIRST `<status>` tag, so OG-r-3 (staged, then superseded) shows ACTIVE |
| comp-find | `'OG-n-1\|R-2 ' org/missions/D9/NFRA/NFRA_OPLGTW --files` | PASS | 43 hits / 387 files; located the round-1 analysis R-2 text |
| comp-read | `ROUND_ANALYSIS.round1.md --enumerate 'R-2\|E8\|EIP\|halves'` | PASS | confirmed E8 needs safe-apply + ledger, no never-widen halves |
| proof-of-spec-check | OG-n-1 instance at 12d1de0062 | PASS | VALID rc=0 (issuer re-run) |
| safe-merge | `safe-merge.sh wk-NFRA_OPLGTW-14` | PASS | c72df75fce; branch needed 5 files, dropped 0, foreign 0 |
| surprise-row-gate | Z-S18 commit | FAIL then PASS | first refused: `surfaced_at` "20:2xZ" breaks the schema regex; fixed to a real minute |

**What worked:** canonical-flow's per-limb read plus a patch-id check (`git cherry`) settled every worktree verdict fast.
**What failed:** to-check's first-tag read of `<status>` misstates appended flips; CTO~O's own regex did the same on OG-n-1 (msg 26730, withdrawn 26734).
**Gap found:** safe-apply's tag-authz gate plans the WHOLE root, so a targeted apply still needs every gitignored build input of that root (row Z-W14-S2).

## Work Completed

### 1. Startup and residue (step 1)
- /watcher: registered, inbox Monitor armed, 23/23 messages READ since 00:00Z.
- Residue: `deliverables/2.0.0_SA_COO~O/round2_drafts/` (14 of 14 issued under the same names) and worker `.scratch/`
  (50 MB) moved to `.runtime/crash-investigation-20260929/wt-scratch-archive/coo-o-nfra-oplgtw/`. Stale OG-r-1 ledger
  copies and EC2_MANIFEST edits in release trees are superseded on CLOUD (45d1e43657, 1f15da8f48, a13797a324).

### 2. Worktree assessment and removal (step 2)
- Assessment @2981fdcc6e: 10 of 10 checkouts DISPOSE, branches kept. CVO~O concurred (@efa01d4120, relay 26655).
- Andrew "call 3 yes" (relay 26698): removed 11 of 11 (the 10 plus wk-oplgtw-14). First: 4 portal/node_modules
  junctions unlinked (main node_modules 263 entries before and after), wk-oplgtw-14 `.scratch` archived 5=5. Then
  `git worktree remove --force`, worktree prune, portal prune. 0 OPLGTW worktrees registered; 8 branches kept.

### 3. Drive restart and OG-n-1 (step 3)
- `/canonical-drive NFRA_OPLGTW` armed on CTO~O ruling 26668 (cron cd73453e, 17,47).
- OG-n-1's gate (MP-a-1 build) found MET by its re-cut MP-a-2. Amendment A1 + GO @9310101b1d (placeholders filled by a
  run-time read of the live writer's key, never printed; claim sub, length 43). CTO~O kept C:/tmp/mp3-1 (msg 26676).
- Worker ~14 blocked at safe-apply (row Z-W14-S2); ruled by A2 @81af5f02c0 (issuer placed the writer's `.build/staged`,
  diff -r identical). Fresh ~14 resumed; applied with no override.
- Drained c72df75fce after issuer re-run: AC1 PASS (EIP 3.214.118.242 = instance public IP), AC2 PASS (targeted plan
  no changes), AC3 PASS (ledger closed 473217c119, /mcp 401), proof VALID. Row Z-S18 @6e8f8083d8. CTO~O disarmed S45
  (Z-S19 @18badb8d01).

### 4. Andrew's G-C answer
- "call 2 need to talk to IT, so blocked externally there" (relay 26701): project blocking item (1) recorded as
  BLOCKED-EXTERNAL on Opal IT @c9df617652.

## Decisions Made

- OG-n-1 released on a measured gate (MP-a-2 CLOSED, zip present, key measured live), not on the stale "MP-a-1" text.
- A2: the issuer places a gitignored build input copied from the tree that built it; the worker never builds or fetches.
- Z-W14-S3 accepted INERT: terraform `-auto-approve` under non-interactive safe-apply is not a gate override.

## Files Modified

See commit messages: 2981fdcc6e, 9310101b1d, f635306e54, 81af5f02c0 (worker branch), c72df75fce (drain), 6e8f8083d8,
558493e689, c9df617652, c121013a3b, ac5bf4de12.

## Blockers

- OG-g-1 then OG-v-7: BLOCKED-EXTERNAL on Opal IT (a new unprivileged M365 test user); Andrew's word, record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_204xZ_OPEN_CALLS_PUSH_YES_GC_IT_REMOVE_34_YES.md`.
  OG-v-7 also needs G-D (Andrew's controlled walkthrough).
- OG-t-2: held on the switchover sitting's Part D record (Andrew).
- OG-v-8: held on G-E and G-F.

## Current State

- Project `org/missions/D9/NFRA/NFRA_OPLGTW/`: status active, dep_stage EXECUTING, lease FULL, L7 round 3. Open: OG-g-1
  (pending, 0.7.0_AE_CloudOps~OG), OG-v-7, OG-t-2, OG-v-8 (staged). OG-n-1 complete; OG-r-3 superseded (last tag).
- Gateway i-07dccb1615503ac99: EIP 3.214.118.242 (eipalloc-093d97376b28d2388, eipassoc-03d10cd025b196726), declared
  in `infra/aws/terraform/opal-gateway/eip.tf`; old auto address 54.197.78.28 is gone for good.
- No OPLGTW worktree exists; branches wk-NFRA_OPLGTW-10..14 and the three rel-nfra-oplgtw-* branches are kept.
- Drive cron cd73453e (session-only) fires at :17 and :47; ticks in `org/mcp/drive_ticks/2.0.0_SA_COO~O.md`.
- Push state: all commits LOCAL; origin CLOUD read 0c955d5493 at 20:2xZ (ls-remote), unread since.

## Next Steps

1. On a gate clearing: OG-g-1 when [0.7.0_AE_CloudOps~OG] receives the new user's tid/oid; OG-t-2 on the Part D record
   (tell [2.0.0_SA_COO~MI] before its cut and rebase by content on the live gateway); OG-v-7/OG-v-8 on G-C..G-F.
2. [3.0.0_SA_CVO~O]: move S45 out of REMEDIATION_v1's ARMED list at the next L8 compile (cite Z-S19).
3. At round end: the L8 packet to [3.0.0_SA_CVO~O] once every round-3 order is terminal.
