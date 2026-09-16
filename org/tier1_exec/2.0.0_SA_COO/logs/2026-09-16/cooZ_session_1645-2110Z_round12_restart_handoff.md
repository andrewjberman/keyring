# 2.0.0_SA_COO~Z -- AMGT_RESAPP round 12 -- RESTART HANDOFF for 2026-09-17

Written 2026-09-16 ~21:1xZ at Andrew's word ("scan for residue and make sure we are clear for a clean restart on
AMGT_RESAPP tomorrow"). Every figure below was measured in the last hour; nothing is carried from memory.
Push state: LOCAL on SITEZ. The SITEZ push is 0.0.0_AB_MSTR~Z's.

## 1. Where the round stands

Round 12 is at L7 with **18 cells: 10 terminal, 8 open** (to-check.py, this hour).

- **Terminal and drained:** rk-1, rk-2, rk-3, rk-4, rk-5, rk-8, rk-9, rk-10, rk-11, rk-13.
- **Open:** rk-6, rk-7, rk-12, rk-14, rk-15, rk-16, rk-17, rk-18.

**Clear for restart, measured:** no merge open in the shared tree; no AMGT branch carries a commit HEAD lacks; no
AMGT deploy sentinel open (the 7 open sentinels belong to other projects); no cron in this session, and the CTO's
/self-drive AMGT_RESAPP cron was deleted on Andrew's "kill cron" (~20:1xZ); no live pull, producer, terraform or
worker process; every worker stopped at Andrew's "wind down your workers immediately".

**The adapter was NOT touched by the stop.** `opal-amgt-scoped-api` CodeSha256
`x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw=`, LastModified 2026-09-16T17:23:29Z, 512 MB, 0 layers; artifact S3
VersionId `X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA`. rk-6's worker stopped immediately BEFORE its deploy step.

## 2. WORKERS RUN SONNET AT EFFORT HIGH -- read this before the first spawn

Andrew-direct 2026-09-16 ~20:2xZ: "we need to make workers use sonnet moving forward ... make sure they are sonnet
agents with high effort." Landed @6c118c12de: `.claude/agents/worker.md` reads `model: sonnet` / `effort: high`, and
`/dispatch` Step 4 now says **pass NO `model` argument on the Agent call** -- an explicit model overrides the
frontmatter, and round 12's spawns passed `opus`. **After any CLOUD -> SITEZ merge, read
`git show HEAD:.claude/agents/worker.md` lines 4-6 first**: the line was flipped to `opus` once already by a merge.

## 3. The residue, preserved -- `residue_round12/` beside this log

Three stopped workers left uncommitted work in their worktrees. Each is captured as a patch whose
`git apply --check -R` returned 0 against the live worktree at capture, so each patch IS that state exactly.
`MANIFEST.json` carries the branch, base commit, file list and sha256 of every file.

| patch | order | worktree / base | what it holds |
|---|---|---|---|
| `rk-6_chainB_wk24.patch` | rk-6 print pack | `C:/tmp/wk-amgt-12-24` @128d2ad67d | 6 modified (scoped_amgt.py, render_pack.py, scoped-amgt-api.tf, build-and-upload-scoped-amgt.sh, 2 tests) + 4 new (print-deps layer: `print-deps-layer.tf`, `build_print_deps_layer.py`, `build-and-upload-print-deps-layer.sh`; `test_surfaced_outcome_routes.py`). Worker's last words: "Local proof is complete. Now the deploy sequence". |
| `rk-12_chainA_wk23_PORTAL.patch` | rk-12 surfaced outcomes | `C:/tmp/wk-amgt-12-23/portal` @2453a7b4 (= origin/DEV now) | 5 modified (amgt-lead-panel.ts, SecurityAnalysis.tsx, constants.ts, useLeadPanelApi.ts, types.ts) + 4 new panels (CoverageFreshnessPanel, InputLedgerPanel, ListRegisterPanel, ResearchInputsPanel). Stopped mid-build. |
| `rk-14_chainC_wk25.patch` | rk-14 the fit | `C:/tmp/wk-amgt-12-25` @074652cc00 | 5 modified (peers/csc.py, peers/engine.py, peers/universe.py, posture/fit.py, posture/tests/test_posture.py). Stopped on end 3, the CSC horizon labels. |

**Do not remove worktrees 12-23, 12-24 or 12-25** until each patch is applied to a fresh slot or the work is
resumed in place. A respawned worker is told its base commit and applies its patch first.

Also archived there, because the session scratchpad does not survive: `amend16.py.txt` (see 4), `run_pulls.py.txt`
and `pulls.log.txt` (rk-17's run and its full log), `union_channel.py.txt` (the drain's channel union).

## 4. Per open order -- what is left

- **rk-17, the two Bloomberg pulls -- THE RUNS ARE DONE.** 20:18-20:20Z by the issuer on Andrew's "do the pulls": 33 of
  33 names pulled raw and derived (8-10 FY rows, 129-205 figures each, every refdata NAME the intended issuer); price
  axis generation at as-of 2026-09-15, 32 of 34 tickers, 64 rows, 0 failed (`Enel IM`, `ROG SW` insufficient
  history). ISSUER AMENDMENT 17 @8f17896f99 repaired AC2/AC3's key read (BP/_LN_Equity and NG/_LN_Equity contain a
  slash); re-cut reads 33 of 33. **OWED: the proof instance and the status flip** -- no further world act.
- **rk-18, filings + drafting batch over the 33 -- NOT RUN.** ~USD 36; egress as needed is authorized (Andrew
  2026-09-16, written into the order). One run, resume over un-landed names only.
- **rk-6, print pack -- apply the patch, then the deploy.** BOTH never-widen halves are on file (COO @34d68dcfaf, CTO
  @653de214b1) and reached the worker branch @128d2ad67d. They name the packs/ and raw/ read widening, the layer,
  the route-count precondition, and a pre/post census of every GET route as the regression control.
- **rk-7, refresh carrier + dated fallback -- not started.** Chain B, after rk-6. **Its fallback changes what the
  adapter SERVES and is NOT in rk-6's co-sign scope**: combining the two deploys needs the CTO half extended first.
- **rk-12 -- apply the portal patch and finish.** AC2 re-cut by AMENDMENT 14 (scoped refusal-reason equality).
- **rk-14 -- apply the patch and finish.** Block repaired by AMENDMENT 15; AC1 re-cut by AMENDMENT 13.
- **rk-15 -- unspawned. ISSUER AMENDMENT 16 is WRITTEN BUT NOT APPLIED** (`residue_round12/amend16.py.txt`): AC2 keeps
  only the absent-reason bar (the other two already read 8 and 7), a NEW AC4 grades `thesis_driver_chart.points` on
  the SERVED `/thesis` for BA_US_Equity (0 today, status ABSENT), and the BA_US_Equity pilot re-run (S127) is placed
  on rk-15. **Re-run it `dry` first**: it mints its row id at run time and asserts the pre-amendment shape.
- **rk-16 -- unspawned.** AC1 already reads 4 keys with 2+ stamps (a stated precondition); **AC3 is a token-presence
  bar over a naming property, so L9 should read its evidence, not the count.**

## 5. Owed at drain-end, in the ONE L8 packet to 3.0.0_SA_CVO~Z

- The HELD partitions: S120 (names with no landed block -- now populated for the 33 by rk-17), S125 (today-dated
  Price list -- now 2026-09-15, plus rk-7's fallback).
- The moved-criterion map, so L9 grades each cell whole: rk-12 AC1 -> rk-6 AC4; rk-16 AC2 -> rk-6 AC5; rk-15 AC1 ->
  rk-7 AC5; rk-12 AC4 carries cell_refs AMGT-rk-7; rk-7 AC4 carries cell_refs AMGT-rk-3.
- 4.0.0_SA_CRO~Z's item-5 finding (the page is now on origin/DEV @2453a7b4; existence graded by the ruled capture).
- rk-8's worker rows: W23-S2 (`portal/.git` is a FILE in a linked worktree, so AC4's branch guard is always False)
  and W23-S3 (AC2's `overlay-has-posture` uses `any()` over five bodies and `posture` rides `/thesis` too).

## 6. Optional cleanup, NOT done

Old worktrees 7-1, 7-2, 8-1, 8-2, 9-1, 10-1, 10-2, 11-1..11-5, 11-issue, 12-26, 12-27, 12-28, coo-amgt-r12,
coo-amgt-rk2-rollback and cvo-amgt-r11-20260915: every branch is fully on HEAD, every old portal branch is contained
in origin/DEV, and their only dirt is the expected portal pointer (plus line-ending-only noise on 11 files in 11-1).
Nothing of value is in them. Removing them is safe but several need `--force` because of the pointer, so it waits
for a word.
