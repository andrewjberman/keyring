# Adopted-work inventory for the Dells -- preexisting branches of the workstreams dell1 and dell2 now hold

**Author:** `1.0.0_SA_CTO` (laptop, the control plane), 2026-10-07 ~07:3xZ. **Why:** Andrew-direct ~07:2xZ, VERBATIM: "I also recommend
alerting the DELL boxes about any preexisting worktrees for their workstreams that they are now adopting" / "so that they do not
duplicate any work". Record: `ANDREW_DIRECT_20261007_071xZ_DELLS_LIVE_GOVERN_LOOPS_DELL_CTOS_COMING.md`.

**For each adopting seat: READ THE BRANCH BEFORE YOU CUT OR BUILD.** A row here is work a laptop lane committed and did not merge.

## How this list was made, and what it cannot tell you

- Population: every local branch on the laptop, in the workspace repo and in the portal repo, that is ahead of the trunk
  (`origin/CLOUD`, `origin/DEV`) and that this seat could tie to a project now placed on a Dell. 32 rows.
- "Ahead" counts commits the trunk does not contain. It does NOT say the CONTENT is unmerged: a change landed by cherry-pick or by a
  later rewrite reads ahead forever. Compare content (`git diff <trunk>...<branch>`) before treating a row as live work.
- The project column is this seat's attribution from the branch name and the predecessor lane's handoff. A wrong attribution is
  possible; say so and it is corrected here.
- NOT in this list: uncommitted files in a laptop worktree. Git cannot carry them. Two are known: `C:\tmp\portal-5174\.env.local`
  (a local environment file for the port-5174 build; it is not sent anywhere by this seat) and `.scratch/` notes in removed worktrees.
- Laptop branches of projects NOT on a Dell (hotfix, practice, archive and fabric-manager branches) are left out on purpose.

## The branches

| Box | Project | Repo | Branch | Head | Ahead of trunk | Last commit | Origin state at 07:3xZ | What the predecessor said about it |
|---|---|---|---|---|---|---|---|---|
| dell1 | MDPF_SECCLASS | workspace | `wk-secclass-r7-20` | ab269906fa | 1 | 10-06 13:15 | NOT on origin | round 7 worker branch; a second branch wk-secclass-r7-20b is 0 ahead |
| dell2 | IRPT_YCDGEN | workspace | `wk-IRPT_YCDGEN-82` | 215c317f77 | 1 | 10-06 17:23 | NOT on origin | NOT DRAINED: safe-merge it, then flip TO q-6 complete with a DRAIN note (~Y handoff @217963b67d) |
| dell2 | IRPT_YCDGEN | workspace | `rel-ycdgen-r6-b2` | 409e3066d1 | 1 | 10-05 23:24 | NOT on origin | KEEP: leg M1 lands its allow-list constant (commit 409e3066d1) on CLOUD after Andrew's retry; the resident host runs this root |
| dell2 | IRPT_YCDGEN | workspace | `rel-ycdgen-r6-b` | 09139ee34d | 1 | 10-05 22:34 | NOT on origin | earlier release branch of round 6 |
| dell2 | IRPT_YCDGEN | workspace | `rel-ycdgen-r6-a` | 3d705e700f | 1 | 10-05 20:47 | NOT on origin | earlier release branch of round 6 |
| dell2 | IRPT_YCDGEN | workspace | `y-release-390` | f1e101d19c | 1 | 10-05 09:47 | NOT on origin | release branch, 10-05 |
| dell2 | IRPT_YCDGEN | portal | `wk-IRPT_YCDGEN-82-portal` | 643b6ddd00 | 4 | 10-06 17:15 | NOT on origin | portal cells e-6, j-6, p-6, q-6 stacked; UNLANDED on portal DEV; product files, so a CTO review comes first |
| dell2 | IRPT_YCDGEN | portal | `cand-r6-prospect-firm` | 4d16a2a012 | 5 | 10-06 17:36 | NOT on origin | the -82-portal stack merged with origin/DEV 6b4e89a8; the build Andrew's report retry runs against |
| dell2 | IRPT_YCDGEN | portal | `wk-IRPT_YCDGEN-81-portal` | e107538d74 | 3 | 10-06 09:37 | NOT on origin | earlier stack |
| dell2 | IRPT_YCDGEN | portal | `wk-IRPT_YCDGEN-70-portal` | cd3924d50f | 2 | 10-05 19:28 | NOT on origin | earlier stack |
| dell2 | IRPT_YCDGEN | portal | `wk-IRPT_YCDGEN-67-portal` | 81bbeba25f | 1 | 10-05 19:02 | NOT on origin | earlier stack |
| dell2 | IRPT_BCKEND | workspace | `wk-IRPT_BCKEND-84` | 00b88da890 | 12 | 09-29 23:27 | NOT on origin | worker branch, 09-29 |
| dell2 | IRPT_BCKEND | workspace | `wk-IRPT_BCKEND-61` | b1cbe6a302 | 2 | 09-28 16:50 | NOT on origin | worker branch, 09-28 |
| dell2 | IRPT_BCKEND | workspace | `wk-irpt_bckend-6-1f` | 2021547ff6 | 5 | 09-20 04:41 | NOT on origin | worker branch, 09-20 |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-cot-cash-line-act` | 596453d184 | 4 | 09-26 19:32 | NOT on origin | HELD by ~M: gold-script branches merge only with their ledger (~M handoff 09-28) |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-cot-b1` | 0da4449e1f | 5 | 09-26 19:49 | NOT on origin | HELD by ~M, same rule |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-s152-cloud` | a94749d9d1 | 1 | 09-26 21:54 | NOT on origin | HELD by ~M, same rule |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-cot-cash-line` | 0da4449e1f | 5 | 09-26 19:49 | NOT on origin | ~M branch, 09-26 |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-s152` | 1c70dce6d4 | 6 | 09-26 21:43 | NOT on origin | ~M branch, 09-26 |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-b01b-skip` | 89280b9d45 | 1 | 09-26 14:53 | NOT on origin | ~M branch, 09-26 |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-s125-publish` | 2e4c33738e | 8 | 09-25 09:40 | NOT on origin | ~M branch, 09-25 |
| dell2 | IRPT_BCKEND | workspace | `irpt-m-s125-20260924` | a7e5c59042 | 1 | 09-24 16:31 | NOT on origin | ~M branch, 09-24 |
| dell2 | IRPT_BCKEND | workspace | `irpt-p-fence-20260924` | 7220e4a4f3 | 2 | 09-23 22:06 | NOT on origin | ~P branch, 09-23 |
| dell2 | IRPT_BCKEND | workspace | `ds-x-b1-cashline` | 819da932c8 | 4 | 09-26 21:33 | NOT on origin | data-science branch on the cash line, 09-26 |
| dell2 | IRPT_BCKEND | workspace | `scratch/resident-hop3-20260926` | fe64236bbb | 2 | 09-26 15:05 | NOT on origin | scratch branch, resident host |
| dell2 | IRPT_BCKEND | portal | `irpt-dev-candidate-7-20260924` | 814d7473a8 | 1 | 09-24 08:58 | NOT on origin | portal candidate, 09-24 |
| dell2 | IRPT_BCKEND | portal | `irpt-dev-candidate-3-20260924` | 7897f891cf | 3 | 09-24 03:04 | NOT on origin | portal candidate, 09-24 |
| dell2 | IRPT_BCKEND | portal | `irpt-opal-scope-p-portal-20260923` | e0531491b3 | 1 | 09-23 11:12 | NOT on origin | portal branch, 09-23 |
| dell2 | ADVI_COTBKF | workspace | `wk-ADVI_COTBKF-13` | f8f8ea4466 | 2 | 10-07 01:28 | on origin | mid-round worker branch, left at the laptop reboot |
| dell2 | ADVI_COTBKF | workspace | `wk-ADVI_COTBKF-14` | a490708ae6 | 2 | 10-07 01:38 | on origin | mid-round worker branch |
| dell2 | ADVI_COTBKF | workspace | `wk-ADVI_COTBKF-15` | f746fa5b24 | 2 | 10-07 01:29 | on origin | mid-round worker branch |
| dell2 | ADVI_COTBKF | workspace | `wk-ADVI_COTBKF-16` | 3f7505a04d | 3 | 10-07 01:30 | on origin | mid-round worker branch |

Origin state at the time of writing: 4 of 32 on origin, 28 not. `0.0.0_AB_MSTR` is asked to publish every row that is not, as a
branch; a publish of a non-trunk branch deploys nothing (NFRA_CTLPLN FWD-5). Re-read with `git ls-remote origin <branch>` before use.

## Where the predecessor lanes wrote down their state

| Project | Read first |
|---|---|
| MDPF_SECCLASS | `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md` (written by laptop `2.0.0_SA_COO~M`; the ONE decomposition of the round) and `org/tier1_exec/2.0.0_SA_COO/handoffs/2026-10-07_0205Z.md` |
| IRPT_YCDGEN | `org/tier1_exec/2.0.0_SA_COO/handoffs/2026-10-07_0100Z.md` |
| IRPT_BCKEND | `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~P.md`, `STATUS~M.md`, `STATUS~Y.md`; `org/tier1_exec/2.0.0_SA_COO/logs/2026-10-06/session_close_1945-2135Z_andrew_p.md` |
| IRPT_DASHBD | no unmerged branch found; its last worker deliverables are untracked files under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~7/` and `~8/` on the LAPTOP only (six JSON files), not on origin |
| ADVI_COTBKF | `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_R2_R3_20261007.md` |

-- 1.0.0_SA_CTO
