# Andrew-direct 2026-09-27 ~12:3x-12:4xZ at 2.0.0_SA_COO~M: the worktree branches come onto CLOUD, gold scripts after Monday's R1

## Verbatim

1. "we should bring all these onto main branch" (on 0.0.0_AB_MSTR's /cleanup list of ~M's worktrees).
2. After ~M's /open-calls card, "Merge the gold-script branches into CLOUD now (a) or on Monday after the first COT
   run checks out (b)?", with REC (b): "rec approved".

## What it rules

- Everything on ~M's branches lands on CLOUD (the main branch).
- Anything that deploys lands on Monday 2026-09-28, right after the first COT run's R1 read-back, each act under its
  own ledger. A CLOUD push deploys every changed gold script (S141); `.tools/safe_deploy_core.file_to_s3_target`
  maps every path under `data/*/scripts/gold/`, tests included, to a live S3 target.
- The signed order stands: the CTO's and CRO's halves say "the deploy follows Monday's R1".

## What lands now (deploys nothing)

- Nothing more can land today. Every branch change is under a gold path, except two kinds of file:
  - ~X's four records: the owned-paths gate (TREE_DELIVERABLES) lets only 0.4.0_DS_ClientPlatform~X commit under its
    folder. They reach CLOUD with the `ds-x-b1-cashline` merge, which keeps ~X as author.
  - `comp-constants.config.yaml`: it must travel with ~X's BD commit, or the drift check refuses the next BD commit.
- ~X's surprise rows are already on CLOUD as S153-S156 (@92244581d2); the branch's copies are dropped at its merge.

## What lands Monday (runbook `IRPT_MVP_M/MONDAY_20260928_RUNBOOK.md`)

| Branch | Head | Act | Ledger |
|---|---|---|---|
| `irpt-m-cot-cash-line-act` | 0deac23f1e | COT cash line: C_06, D_03 positive rows, D_04; Holdings `classify_security` | cot-cash-line-m-20260928 |
| `irpt-m-s152-cloud` | ff63895521 | S155: COT mix_views admits cash and other | same act |
| `ds-x-b1-cashline` + `irpt-m-cot-b1` | 146876e75a, ccb9b38dd8 | ETF Part B step B1 (BD, 49F a07/d06, COT d08, both mix_views, COT C_06/D_03/D_04 admissions); `comp-constants.config.yaml` (9135feae97) travels with ~X's BD commit | B1's own ledger |
| `irpt-m-s152` | 9135feae97 | superseded; only the comp-constants commit is taken | -- |
