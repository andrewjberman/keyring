# Post-crash residue + worktree assessment -- NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-09-29 ~18:2xZ

Order: `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260929_1755Z_POST_CRASH_RESIDUE_CLEANUP_AND_WORKTREE_ASSESSMENT.md`
(step 1 residue, step 2 worktrees with the CVO, step 3 restart). CVO for this project: 3.0.0_SA_CVO~O.

## /canonical-flow NFRA_MCPINDEX --report-only

```
LOCATE   home: org/missions/D9/NFRA/NFRA_MCPINDEX   placement: site-z (project.json fabric)   status: active
         TOs: round 4, 2 open (MX-s-14 pending, MX-t-10 pending); every other round-4 order terminal
         (MX-r-5 complete, MX-x-3 complete, MX-i-5 superseded; MX-m-1 round 3 complete)
         worker branches: wk-nfra_mcpindex-3-8..3-13, 4-14..4-18 -> 0 unmerged commits each vs CLOUD 0bbde7112f
         unfinished edits under the project home: none; stash: 0
         slug: REMEDIATION_v3 (round 3); answer: ROUND_ANALYSIS.round3 -> round 4 cut, in L7
         dep_stage (claimed): EXECUTING   closer_contract: none   mode lease: FULL
MEASURED limb: L7 round 4.  claimed vs measured: AGREE
CLASS    BLOCKED (MX-t-10): named blocker Z-W15-S5, the LGIC registry row for the platinum/etfs key (laptop CTO's,
         msgs 26487/26493). Re-measured 18:2xZ: 0 commits to infra/logic/registry/ or .tools/naming-gate.py since
         11:00Z (control: newest registry commit 03c7f7f593 resolves).
         IN-PROGRESS by schedule (MX-s-14): acceptance legs L5/L9 are tonight's 21:38/21:45/21:53/22:00Z fires.
ROLE     2.0.0_SA_COO~MI owns L7; next act after 22:00Z: close s-14, rule t-10, compile the round-4 L8 packet.
```

## Step 1 -- crash residue and loose ends (done)

| item | measured | act |
|---|---|---|
| Drive-log tick 14:30Z uncommitted | `drive_log_20260929T14Z.md` +9 lines, unstaged | committed in this record's commit |
| Issuer row Z-S60 | dfdd0343f7 ancestor of HEAD | none needed |
| Worker ~15 candidate (MX-t-10), uncommitted in `wk-mcpindex-r4-15` | 5 modified + 1 untracked, 317+/14- lines, sizes intact, 0 NUL bytes | pinned without touching the worktree: `refs/archive/wt-20260929/wk-mcpindex-r4-15-candidate` -> 03a19ac282 (temp-index snapshot, parent 5a450314de) |
| Open ledger `nfra-mcpindex-bd-playwright-strip` (MX-s-14) | L1-L4, L7, L8 closed; L6 (git) open though its commits 4110fd3b0c/138ed30f0a/3bc2dc3a78 are on CLOUD | L6 closed with that proof; L5, L9 stay open for tonight's fires (window ends 00:22Z 09-30) |
| Rollback files the ledger cites as worker `.scratch/` | worker ~17 checkout removed by MSTR~Z; files survive at `.runtime/crash-investigation-20260929/wt-scratch-archive/wk-mcpindex-r4-17/.scratch/` (`before/*.json`, `alloc_v4_exact.json`, sizes nonzero) | new path written into the L6 proof; SSM `get-document --document-version` stays the primary rollback source |
| Other `.open_deploys` entries for this project | 1 on CLOUD; the per-worktree read of every mx-*/wk-mcpindex tree finds the same one only (mx-dep6, r4-14 carry the older copy) | none |

## Step 2 -- worktrees (14 checkouts; branches are kept in every case)

| worktree | branch | unmerged vs CLOUD | dirt | disposition |
|---|---|---|---|---|
| Desktop/wk-mcpindex-r4-15 | wk-nfra_mcpindex-4-15 | 0 | the MX-t-10 candidate (6 files) | **KEEP** -- the only needed checkout; t-10 resumes here when Z-W15-S5 lands |
| Desktop/wk-mcpindex-r3-11 | wk-nfra_mcpindex-3-11 | 0 | .scratch/ only | DISPOSE -- MX-m-1 complete |
| Desktop/wk-mcpindex-r4-14 | wk-nfra_mcpindex-4-14 | 0 | .scratch/ only | DISPOSE -- MX-r-5 complete |
| Desktop/wk-mcpindex-r4-16 | wk-nfra_mcpindex-4-16 | 0 | .scratch/ only | DISPOSE -- MX-i-5 superseded |
| C:/tmp/mx-rel3, mx-rel4 | rel-nfra-mcpindex-r3-gateway(-b) | 16, 17 (release branches, not for merge) | mcportal/ build dir | DISPOSE -- r3 gateway ledger closed 20260929T0137Z |
| C:/tmp/mx-rel5, mx-rel6 | rel-nfra-mcpindex-r4-gateway(-b) | 22, 22 (release) | mcportal/ build dir | DISPOSE -- r4 gateway ledger closed 20260929T0954Z |
| C:/tmp/mx-dep4, mx-dep5, mx-dep6 | dep-nfra-mcpindex-r3/r4-gateway(-b) | 2 each (deploy) | mcportal gitlink / dir | DISPOSE -- same two closed ledgers |
| C:/tmp/mx-rb4, mx-rb5, mx-rb6 | detached | 14, 20, 21 | mcportal/ dir | DISPOSE -- each HEAD (d287ffb346, 4248b70b39, 63264dfb22) is contained in a named rel-* branch, so nothing is orphaned |

The next gateway release (MX-t-10) is cut fresh on whatever base is LIVE at that time, resolved by content over SSM;
no current release checkout is its base. Removal = `git worktree remove` per checkout after archiving each
`.scratch/` beside MSTR~Z's archive; it waits on 3.0.0_SA_CVO~O's concurrence and Andrew's go (recursive deletion).

## Step 2 executed -- 2026-09-29 ~20:5xZ-21:3xZ

Authority: Andrew "call 3 yes" (~20:4xZ), relayed by 1.0.0_SA_CTO~O msg 26699, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_204xZ_OPEN_CALLS_PUSH_YES_GC_IT_REMOVE_34_YES.md`.
3.0.0_SA_CVO~O concurred (msg 26642, relayed 26656).

- Re-measured the 13: 0 other dirt, every HEAD contained in a named branch.
- Reparse points: 0 at depth 2 in all 13, and 0 at full depth in the 10 `mcportal/` dirs. Positive control: a planted
  `portal/node_modules` junction read 1, and `cmd /c rmdir` removed the link and left its target.
- `.scratch/` archived to `.runtime/crash-investigation-20260929/wt-scratch-archive/<name>/`: r3-11 721 files, r4-14
  949, r4-16 991, file count and bytes equal each; the other 10 had none. The gitignored `org/` hook logs of the 7
  rel/dep checkouts are archived under `<name>/ignored/`, bytes equal.
- `git worktree remove --force` x13: rc=0 each; 0 of 13 paths remain on disk; `git worktree prune` and
  `git -C portal worktree prune` run.
- Branches: 20 mcpindex branch tips identical before and after. `wk-mcpindex-r4-15` intact (6 candidate files);
  `refs/archive/wt-20260929/wk-mcpindex-r4-15-candidate` -> 03a19ac282.

## Step 3 -- restart

`org/ref/LIVE_ARMS.md` carries a live row for `2.0.0_SA_COO~MI` `/canonical-drive NFRA_MCPINDEX 30m`, paired with
1.0.0_SA_CTO~O's `/self-drive`. Re-armed ~19:4xZ at :15/:45 on 1.0.0_SA_CTO~O's ruling msg 26669 (record
@680afc11fd), which separated the restart from the removals. The first act that matters is the tick after 22:00Z
(close s-14, rule t-10).
