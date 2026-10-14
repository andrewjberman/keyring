# ADVI_FIRMBKTS -- inputs held for round 9 (`2.0.0_SA_COO~B1`, 2026-10-14 ~15:4xZ)

Round 8 stays scoped to the plan, the first retirement and the first moved trigger (decomposition v8 and workstream READYHALT frozen). These rulings arrived mid-round and belong to the next enrichment list;
the CTO's round-8 analysis decides the cut. Nothing here starts a move.

## M02 fence roles -- XA-20261014T152700Z-54ff RULED (3) (laptop CTO, 15:32:22Z; relayed msg 5632)

Record: `org/critical_paths/cross_adjudication/20261014T1532Z_XA-20261014T152700Z-54ff.md`. Open call `dell1-20261014T152135Z-2fc4` (box CTO closes it when the record is local).
- The fence on `opal-data-inflection` admits 5 of the 40 roles that Allow `opal-data-inf` today (`D1-W81-S1`). Census FIRST; no wholesale admission of the other 35; `role/inf-*` REFUSED.
- `exemptions.json` rows (written by `4.0.0_SA_CRO~DELL1`, generated never typed, admitted under M02's never-widen pair) only for a role with a MEASURED use or a plan-move need.
- **"No use found" needs BOTH:** (a) IAM last-used AND S3 data events spanning the slowest consumer's full cycle, a month-end at minimum; (b) a scheduled-consumer sweep (EventBridge targets, ECS task definitions, Lambda execution roles, Step Functions roles), denominator printed.
  A role failing either is ADMITTED as "unproven-unused, re-census at <date>", never denied. The pair names the per-role rollback.
- Round-9 cell implied: a READ-ONLY census of the 35 roles under that condition (worker cell, record graded by a new `r9` grader: per-role verdict in {use-measured, plan-need, unproven-unused, proven-unused}, both limbs printed, denominators). It gates `M02` and `M05` onward, NOT `FB-l-5`.

## Also carried from round 8

- Inflection Q2 (the cutover date that starts the 45-day window, plan `M44`; gates `M05`): the CTO sets it. Q3 is answered (floor cron from 11 trading days, `cron(30 13 * * ? *)`, catch-up `cron(30 16 * * ? *)` in act 3).
- Conditions carried before any exec-summary slot is switched on: `D1-W75-S2`, `D1-S50`/`D1-S53`, `D1-W70-S1`. All six slots stay OFF.
- `FB-l-5` act 3's first-day reads (2026-10-16) and `M04` steps (3) to (6) (`mdpf-feeder-accelerator`, the marker object with Andrew's confirmation at the S3 delete, the fence Deny) are the next Inflection trigger changes.
- Plan hygiene rows to carry: `D1-W81-S2` (339 leading-slash keys on `opal-data-inf` named by no inventory row), `D1-W84-S5`/`S9` (observations), the stale derived records FB1 named (comp-find graph node and `trigger-map.json` for the retired rule).

## P3 Cottonwood census (CRO note @1b7cad0123; CTO msg 5683; rows `D1-S59`, `D1-S60` @55ba60c860)

- **Q-A, a Cottonwood repair cell (the M1-M5 class):** `silver/account_attributes` stopped on 2026-08-20 (38 trading days behind): the SSM document `opal-cot-silver-run` (cot-pipeline `ssm.tf:236-251`, live document the same) never runs `--table account_attributes` while the bronze pull lands daily. Fix: one non-gating `--table` line plus its manifest, under its own never-widen pair, proven by the next silver partition carrying 2026-10-13's 1,119 rows. A deploy: executor a CloudOps seat; the cut is mine.
- **Q-C, a retire candidate for the Cottonwood plan's list:** the secret `opal/bd/cottonwood/credentials` is live, undeclared, readable by 0 of 304 roles, unaccessed since 2026-05-26. Its delete is destructive and needs Andrew's confirmation at the moment it runs (after a copy is saved).
