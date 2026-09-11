# 2.0.0_SA_COO~F -- MANAGED WINDDOWN handoff, 2026-09-11 17:35Z -- for a successor with this serial and none of this context

Andrew-direct (0.0.0_AB_MSTR 95996, ~17:1xZ): let workers finish, start nothing new, /log and commit, reboot follows. Nothing respawns; relaunch is Andrew's act. This file is the record of intent.

## 1. What this lane holds
Project IRPT_FNTEND (D9/IRPT), round 2, dep_stage EXECUTING. PRD v0.6 @d1479bc5f0. Decomposition v0.2 @430c5fcb4a (round-2 section R2.1..R2.8). Issuance @75d2e353a8 (seven orders FE-s-12..18). Amendments since: 4c8c085334 (phase BUILD-GENERAL), fcfb09d071 (FE-s-18 Lato Bold), af013bcb9e (FE-s-14 carries R1; 15/16/18 aligned to contract v1). Channel: `surprise-channel/investigations/INVESTIGATION_v2.md` (8 rows at 13a291505e: W1-S15..S17, W2-S7, W2-S8, S18..S20). Prior logs in this folder (0310-0710Z, 0710-1000Z, 1000-1520Z) carry the round-1 close and the round-2 opening.

## 2. Order state at this instant (measured 17:3xZ)
| order | status | where |
|---|---|---|
| FE-s-12 typecheck | complete, DRAINED both repos | portal 32a744dc / ws 69aa29687c |
| FE-s-13 seam | complete, DRAINED both repos | portal 8cc43736 / ws 392531b8d5 |
| FE-s-17 Lato | complete, DRAINED both repos | portal 2b46540a / ws ae023bb3d7 |
| FE-s-14 firm route + R1 (v1 re-pin, merge repairs) | IN FLIGHT, worker `0.9.0_WK_IRPT_FNTEND~2` (a subagent of THIS session; it dies with the session) | worktree pair `/c/tmp/wk-irpt_fntend-2-4-fe-s-14` (ws branch `wk-irpt_fntend-2-4-fe-s-14` @ffa98ac525, no workspace commits yet) and `/c/tmp/wk-irpt_fntend-2-4-fe-s-14/portal` (portal branch `wk-irpt_fntend-2-4-fe-s-14` @e1d78ce6: THREE COMMITS -- 7151f2c4 R1 client re-pin, 9e7ea2f3 R1 fixtures/tests, e1d78ce6 the firm-route cell; portal worktree clean). What is NOT yet on the branch: the proof-of-spec instance, result.md, the PNGs, any rows, the `<status>` flip. |
| FE-s-15 composer | blocked (not seated) | face amended to v1 |
| FE-s-16 export mount + narrative | blocked (not seated) | face amended to v1 |
| FE-s-18 evidence + mobile + Lato Bold | blocked (not seated, last) | face amended |

Portal DEV (local) 8cc43736 is RED (tsc rc=2, 6 test fails; row S20) until FE-s-14 drains. origin/DEV 5b959f63. **Portal is FROZEN by Andrew ("nobody does any portal promotes until i say so"): no DEV push, no gitlink bump** (workspace gitlink at HEAD e85f6eb8 resolves on origin/DEV; the forward bump waits behind the push). Workspace CLOUD is pushed by MSTR on Andrew's cadence.

## 3. If the reboot lands BEFORE FE-s-14 reports (the likely case)
The worker subagent cannot be resumed after a session turnover (`No transcript found`; banked). Its BRANCH state survives on disk. A successor:
1. Verifies the pair exists (`git worktree list` in both repos) and the portal branch is at e1d78ce6 or later; reads `git -C /c/tmp/wk-irpt_fntend-2-4-fe-s-14/portal log --oneline 8cc43736..HEAD`.
2. Does NOT re-cut FE-s-14 and does NOT spawn a new worker into the OLD worktree (banked trap: the face stays off the branch). Two sanctioned paths, the successor's call: (a) spawn a FRESH `0.9.0_WK_IRPT_FNTEND~2` on a NEW pair whose portal branch is cut FROM e1d78ce6 (not DEV) so the three commits are inherited, with the same face and an identity line saying "R1 and the firm-route code are committed on your base; your work is the proof: run every criterion, write the instance/result/PNGs/rows, flip"; or (b) if the branch already carries the flip and a VALID instance, drain it as-is.
3. Drain sequence (unchanged all round): checker re-run from the worktree; `bun run typecheck` and `bun test src/pages/InvestorReporting` in the worker's portal worktree (must be rc=0 / 0 fail -- R1's whole point); gitlink check (`git show --format= --name-only <c> -- portal` empty for every workspace commit); portal `safe-merge.sh <branch>` from `portal/`; workspace `safe-merge.sh <branch>` (channel conflict is normal: resolve with the scratch union script -- ours' rows byte-identical, theirs' new rows appended -- then `--continue`; NEVER a bare commit; never pair `-m` with `$(` in one call); teardown (`rmdir` the node_modules junction, remove both worktrees, delete both branches, prune both repos).
4. Then seat FE-s-15 (slot ~1, port 5181) and FE-s-16 (slot ~3, port 5183) in parallel on fresh pairs from HEAD/DEV with `--host 127.0.0.1`; FE-s-18 last on slot ~1. Round-2 row ids: W1 from S18, W2 from S9 (W2-S9 may be taken by FE-s-14), W3 from S3. Seat rows continue from S21.

## 4. What a successor must NOT re-do
- Do not re-fetch Lato: Bold (700) is on the box at `.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/Lato-Bold.ttf` sha256 8a0aace75d33794eece4b28187bfc1df0bbd2888b5d8a56e01788c8d65d16be1 (CTO fetched it on Andrew's word); FE-s-18 packages it.
- Do not re-pin the seam by hand: FE-s-14's R1 commits do it against `docs/contracts/investor-reporting/v1` @7ce4761a2f (header `X-Contract-Version: v1`, envelope `{contract_version, operation, firm_id, data, status?}`, producer operation ids; `default.json` is the consumer's published map the counterpart's paired test reads).
- Do not edit the shims beyond R1 item (1); do not re-run the census for its own sake; do not push anything portal.
- Do not send the CTO anything before every order is terminal (L10 is ONE message).

## 5. Open for L10 (round 2), so far
W1-S16 (fixture plane keeps `submit-correction` / `export-preview` for round-1 tests); W1-S17 (AnalysisReport.release.protected_pdf_ref is server-only, the vendor PDF preview renders nothing live until the producer carries a route); W2-S7 (the portal shell's Google-hosted Inter -- D13's, not IRPT's); W2-S8 (RENDER_PACKAGE.fonts flat array); the v1 artifact landing mid-round (S20); the counterpart's paired test reads `default.json`, not `fixtures/wire/requests/`.

PUSH STATE: workspace LOCAL (this file's commit); portal DEV LOCAL @8cc43736, FROZEN.
