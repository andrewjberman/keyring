# NFRA_OPLGTW -- post-crash residue and worktree assessment (2.0.0_SA_COO~O, 2026-09-29 ~18:1xZ)

Order: `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260929_1755Z_POST_CRASH_RESIDUE_CLEANUP_AND_WORKTREE_ASSESSMENT.md`
(steps 1 and 2). For 3.0.0_SA_CVO~O to read and concur or object in its own file.

## Position at the crash (/canonical-flow NFRA_OPLGTW --report-only)

- Home `org/missions/D9/NFRA/NFRA_OPLGTW/`; status active; dep_stage EXECUTING; lease FULL; closer_contract none.
- Measured limb: L7, round 3. Last COO tick 14:30Z (10:30 ET), one hour before the 11:34 ET crash: NO-OP. No worker
  was in flight. 6 orders non-terminal, all waiting on named gates (project.json `blocking` items 1-5):
  - OG-g-1 `pending`, 0.7.0_AE_CloudOps~OG: waits on a brand-new unprivileged M365 test user (Andrew).
  - OG-v-7 `staged`: held on G-C (after OG-g-1) and G-D (Andrew's controlled walkthrough).
  - OG-t-2 `staged`: held on the switchover sitting's Part D record (Andrew).
  - OG-v-8 `staged`: held on G-E and G-F.
  - OG-n-1 `staged`: held on NFRA_MCPORTAL MP-a-1's build (2.0.0_SA_COO~MP).
  - OG-r-3: last `<status>` is `superseded` (by OG-x-4). to-check lists it ACTIVE because it reads the first tag.
- Class: SEQUENCED-BEHIND on the gates above. No UNFINISHED-EDITS and no ORPHAN-WORKTREE (see below).

## Residue (step 1)

| item | measured | disposition |
|---|---|---|
| shared-tree edits under the project | 1 untracked dir: `deliverables/2.0.0_SA_COO~O/round2_drafts/` (14 TO drafts + 23 checks, 2026-09-28 16:34-17:06 ET) | all 14 were issued under the same file name in `task-orders/`, so these are superseded drafts. MOVED to `.runtime/crash-investigation-20260929/wt-scratch-archive/coo-o-nfra-oplgtw/round2_drafts/` |
| shared index | `git diff --cached` empty | none |
| open deploy entries | CLOUD `.open_deploys/`: 0 OPLGTW entries. Worktrees: og-x4-rel carries `nfra-oplgtw-og-r-1-first-release.json` OPEN | a stale copy; CLOUD closed it at 45d1e43657 (2026-09-18). Not a deployer (same class as row Z-W11-S4) |
| EC2_MANIFEST edits (uncommitted) | og-x3-rel2: opal-gateway 4248b70b39; og-x4-rel: 63264dfb22 | both already on CLOUD (1f15da8f48 x-3, a13797a324 x-4); live has moved to 093fc247c6 (MX-r-5, 1ad8c00d76). Superseded |
| worker `.scratch/` | wk-oplgtw-10..13, 50 MB total of proof and message ephemera | MOVED to the same archive dir as `wk-oplgtw-<n>.scratch/` |
| broker | 23/23 messages since 00:00Z READ; inbox empty | none |

## Worktrees (step 2): 10 checkouts, all DISPOSABLE, all branches kept

| worktree | HEAD | commits not in CLOUD by patch | held by a branch | remaining dirt | verdict |
|---|---|---|---|---|---|
| C:/tmp/wk-oplgtw-10 | 2df96ab2b2 | 0 | wk-NFRA_OPLGTW-10 | portal gitlink ` M`, .venv-og (143 MB) | DISPOSE |
| C:/tmp/wk-oplgtw-11 | b6e52b09d5 | 0 | wk-NFRA_OPLGTW-11 | same | DISPOSE |
| C:/tmp/wk-oplgtw-12 | 62e58c94ef | 0 | wk-NFRA_OPLGTW-12 | same | DISPOSE |
| C:/tmp/wk-oplgtw-13 | a10ce5eb72 | 0 | wk-NFRA_OPLGTW-13 | same | DISPOSE |
| C:/tmp/og-x3-rb (detached) | d287ffb346 | release lineage | 8 branches | untracked mcportal/ build dir | DISPOSE |
| C:/tmp/og-x3-rb2 (detached) | 7c7ebe14d3 | release lineage | 1 branch | mcportal gitlink ` M` | DISPOSE |
| C:/tmp/og-x3-rel | 7b729821a9 | release lineage | rel-nfra-oplgtw-stream-export | mcportal/ | DISPOSE |
| C:/tmp/og-x3-rel2 | 4248b70b39 | release lineage | rel-nfra-oplgtw-stream-export-v2 (+3) | mcportal/ (84 MB), superseded manifest edit | DISPOSE |
| C:/tmp/og-x4-rb (detached) | 4248b70b39 | release lineage | 4 branches | mcportal/ | DISPOSE |
| C:/tmp/og-x4-rel | 63264dfb22 | release lineage | rel-nfra-oplgtw-export-flat (+1) | mcportal/, superseded manifest edit | DISPOSE |

Why none is needed:
- Worker trees: every worker branch is fully in CLOUD (`rev-list CLOUD..<b>` = 0). No worker is in flight. The
  held orders re-dispatch to fresh slots cut from CLOUD HEAD when their gates clear.
- Release trees: OG-x-3 and OG-x-4 are deployed with ledgers closed, and the gateway has since moved to MX-r-5
  (093fc247c6). OG-t-2, the next OPLGTW release, is cut fresh from the live gateway by content, as agreed with
  2.0.0_SA_COO~MI (msg 26531). Each HEAD stays reachable from a branch, so a rollback tree can be re-created with
  `git worktree add <path> <commit>`.
- The remaining dirt is regenerable (venv, bun build output) or superseded (manifest edits, gitlink pointers).

Branches with no checkout (wk-NFRA_OPLGTW-7-e1 / -8-e2 / -9-s1: 2 patch-unique commits each, SITEZ-era; -15: in
CLOUD): kept, not touched. The /cleanup policy covers branches.

## Removal command (runs after CVO~O concurs and the operator confirms, since it is a recursive delete)

`git worktree remove --force <path>` for each of the 10 paths above, then `git worktree prune`. It removes no
branch and no commit.

## Step 3 (restart)

On restart, re-arm `/canonical-drive NFRA_OPLGTW 30m` from the live LIVE_ARMS row (1.0.0_SA_CTO~O self-drive,
DIRECTED). Every open order is gate-held, so ticks will be NO-OP until a gate clears.
