# Session Log -- 0.2.0_DT_PortfolioAnalytics -- 2026-07-17 ~1600-1655Z
**Archetype:** Andrew-direct assessment -> triage -> deploy cure -> backfill verify
**Project:** BD 49f dim chain (tax-pt2 fee-schedule consumers) / opal-assets

## Ask (Andrew-direct)
Assess the BD additional-table chain designed for Alyssa's tax-pt2: is the daily bronze ETL +
silver conversion trigger implemented? Begin work.

## Findings (grounded)
- BRONZE: implemented + LIVE. opal-assets-bd49f-daily-pull, EventBridge 02:30Z + 04:30Z reattempt;
  current through date=2026-07-16 (fees_435407 + allocation_390224 + roster).
- SILVER TRIGGER: implemented (Scheduler opal-assets-bd49f-dim-convert-daily, 03:05Z) but the
  lambda had NEVER succeeded on schedule -- 07-14/15 partitions were DS hand-runs; the 07-17
  first scheduled fire crashed ModuleNotFoundError x3 and silver froze at 07-15.
- Cured 3 stacked runtime defects (each surfaced by exercising the prior fix): stream_parquet
  unvendored (manifest closure claim was a hand census -> now mechanical ast-scan) + openpyxl
  layer missing (runtime-only pandas dep) + IAM writes-only (own-silver SCD2 seed reads +
  schwab 0833 fact_acc ship-gate reads granted narrowly).
- Deployed opal-assets-v0.26.0 (3x plan->safe-apply->0-diff, tagged, pushed); backfilled
  {"date":"2026-07-16"} rc=0; both dims listing-verified (16,008 + 6,200 rows, coverage 74.0%,
  1 fee conflict flagged). Absence twin PUBLISHED at 05:00Z = detection proven live.
- Ledger 20260717T1615Z CLOSED. CTO quadruple-residual ("writes vs cron") answered w/ mechanism.
  MEMORY trigger row rewritten: 07-18 03:05Z = first unattended fire, owner me + CTO backstop.

## Compiler tools
comp-grep (fees_435407 trace, TF resources, stream_parquet census), comp-glob (canonical lib
location). comp-iam not used for the grant verdict -- it fails GREEN on (action,resource); the
behavior-grade lambda invoke was the instrument (three successive denials surfaced the exact
missing pairs, sharper than simulate).
