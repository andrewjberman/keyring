# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1632Z (reconcile lead + close)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

## Dispatch chain (this cycle)
COO escalated me to LEAD the Cohort-1c data-model reconcile w/ DS~B (settle where SMA lives + correct FE fix + disposition the -$172M seam). Mid-reconcile, COO sent an Andrew-direct resolution (FE fix = FOLD, not F5) + confirmed the -$172M = Black-Diamond->Schwab source change (routed DS~B). DS~B replied confirming BOTH my flags + correcting its earlier scope, handing me the consolidated close.

## Empirical lead — source-of-truth corroboration
Read source partitions `platinum/mdpf/aggregate_aua/{2026-05-14,15,18,19}.json` directly. The rollup is a pure pass-through bundler; the partitions carry `methodology_version` + `headline_formula` that flip EXACTLY at 5/18:
- `v0_8_ruling2` (<=5/17): sma=None, by_model=5, "1c non-additive sub-slice of 1b", non_model SMA-inclusive.
- `v0_9_1` (>=5/18): sma broken out ($24.9M), by_model=7 (2 cohort_class='sma'), formula "1a+1b+1c+2a", non_model SMA-exclusive.
- 49f -$172M = **-$25M SMA-breakout (reclassification) + -$147M v0.9 residual re-level (source change)**. cohort_2b_audit also drops 203.8M->106.1M.

## Reconciled (DS~B confirmed + self-corrected)
- ITEM#1 additive-vs-narrative: CONFIRMED to the dollar; meta "1c non-additive sub-slice of 1b" is stale v0.8 framing -> DS~B owns the producer-meta fix.
- ITEM#2 pre-5/18 history: bandaid ESTIMATE (build_mdpf_v0_bandaid_backfill.py), not real; Mar11-May15 null = bandaid/live seam. Exact historical 1c unavailable.
- FE fix: Andrew = FOLD (displayed non_model = non_model + sma). My data VALIDATES it: sma is additive-separate (no double-count) + fold keeps SMA in non_model both sides => no SMA-step on top of the seam (F5 would have added one). DS~B withdrew its fold-of-residual rec; F5 moot. RD~B proceeding.
- -$172M seam: Black-Diamond->Schwab source change, DS~B backend re-derivation (mdpf_aggregate_aua.py). DE serving-side verify support offered (re-run continuity verify on re-derived artifacts).

## Commits
- CLOUD `<pending>` — brief update (Finding 5 source-partition corroboration + Reconciliation/Resolution) + this log

## Comms
- Consolidated close -> COO (2.0.0_SA_COO) + CTO (1.0.0_SA_CTO); flag -> DS~B (Andrew=FOLD, F5-deference moot; DS owns meta one-liner).

## Next
- [COO] preference: serving-side support for DS~B's Schwab re-derivation (offered) vs fresh portal-data-path item — awaiting call.
- [RD~B] fold ships -> I verify displayed non_model = non_model + sma renders w/o double-count.
- /work cron live (~20m).
