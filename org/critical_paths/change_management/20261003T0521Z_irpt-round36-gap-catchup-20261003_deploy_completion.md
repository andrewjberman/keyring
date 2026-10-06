# Deploy Completion Record
**Date opened:** 2026-10-03T05:21:15.240724+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T001445Z
**Deploy:** IRPT_BCKEND round 36: holdings producers' catch-up + own-prefix listing grant (D2, CTO half @d9f15bc006 batch 207) and the adapter's missing-trading-day disclosure (D1, re-cut to claim inferred, pending) -- packet @3c2ad28cf3
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 60.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | verify | holdings-performance plan exactly 0/4/0 (two functions' code, two role policies) and the producer artifact's map hash = S3 content-sha256 | PASS + equal | ~05:1xZ holdings-performance plan 0 to add / 4 to change / 0 to destroy (module.irpt_holdings_performance + _inf code: s3_object_version OJ.bVNs_0q -> IPBj.bgy4, source_code_hash kKgvbKtG -> 0PuFBxdJ; aws_iam_role_policy.irpt_holdings_performance + _inf: one ListBucket statement each); producer map artifact_sha256 0PuFBxdJ = S3 content-sha256 = zip sha256 (@e629c381ac); vs deployed bytes exactly handler.py moves (13 of 14 equal) | CLOSED 20261003T052234Z |
| D2 | activation | targeted safe-apply of both producers' code (0PuFBxdJ) and both role policies; read-back CodeSha256 x2 + policies; targeted re-plan No changes | CodeSha + policy + No changes | targeted plan 0/4/0; safe-apply ~05:2xZ Apply complete 0/4/0 (naming PASS 6); read-back: irpt-holdings-performance-lambda and irpt-inf-holdings-performance-lambda CodeSha256 0PuFBxdJSbFHNJ9+Z3weyzLvXyZhgZFk2dkGAbIYb/0= Active Successful; irpt-49f-holdings-performance-role ListTheOwnDailyGoldPrefixForCatchUp s3:prefix irpt/49financial/gold/holdings_performance_daily/*; irpt-inf-holdings-performance-role ListTheOwnInflectionDailyGoldPrefixForCatchUp s3:prefix irpt/inflection/gold/holdings_performance_daily/*; full re-plan No changes | CLOSED 20261003T052739Z |
| V2 | verify | one dry-run invoke of each producer WITHOUT date: plans exactly today's one day, no 'WARN: gold listing failed' | invoke logs | dry-run invokes WITHOUT date ~05:2xZ: irpt-holdings-performance-lambda {dry_run, source schwab_08335338} planned [2026-10-01] (Saturday's T-1 by today's rule), rows 7570 complete, no 'listing failed' WARN; irpt-inf-holdings-performance-lambda {dry_run, source orion} planned [2026-10-01], rows 966 complete, no WARN -- the listing grant took (a failed listing prints WARN and still plans T-1) | CLOSED 20261003T052825Z |
| D1 | activation | the adapter re-cut (claim inferred, batch 207) built, its new blob signed by the CTO, targeted safe-apply, read-back, re-plan No changes | CodeSha + CTO half + No changes | CTO half on blob U+miRkw3 signed (batch 210, @47dc514ff1); targeted plan 0/1/0 (s3_object_version 7GwiGHEP -> iw5pK0Bh, source_code_hash /K1eLPuP -> U+miRkw3); safe-apply ~06:09Z Apply complete 0/1/0; read-back CodeSha256 U+miRkw3 Active Successful; re-plan No changes; the deployed holdings_gold.py (zip member == HEAD blob) run over LIVE gold, read-only, ruled YTD 2026-01-01..2026-10-01: 49financial claim measured, absences unchanged (accrual_basis, fees_and_income, money_weighted_return, excluded_rows); inflection claim measured, no missing_trading_days -- its 2026-05-11/06-30/08-10 are LINKED rows (the next day's prior_business_date is the day before the gap: 05-08, 06-29, 08-07), already disclosed as linked_days, so the new disclosure correctly does not fire | CLOSED 20261003T062357Z |
| A1 | verify | Mon 2026-10-05 scheduled fires of both producers: each computes 2026-10-02 only, one new key each, no listing WARN | log read | Mon 2026-10-05 scheduled fires read from CloudWatch: irpt-holdings-performance-lambda 11:30:11Z computing date=2026-10-02 upload=True, 7577 rows LANDED, census complete=True; irpt-inf-holdings-performance-lambda 14:00:27Z computing date=2026-10-02 upload=True, 974 rows LANDED, complete=True; each EMIT 1 day landed, 0 not computed; no WARN or ERROR line in either log (filter ?WARN ?ERROR ?Traceback over each fire window). One new key each: date=2026-10-02/data.parquet single version, LastModified 11:30:18Z (49F) and 14:00:29Z (INF), equal to the fire times. Separate finding (not this leg's wording): Inflection gold lacks 3 2026 trading-day partitions, row IRPT_BCKEND-S338 | CLOSED 20261006T001445Z |

## Log

- 20261003T052115Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20261003T052234Z LEG C1 closed: ~05:1xZ holdings-performance plan 0 to add / 4 to change / 0 to destroy (module.irpt_holdings_performance + _inf code: s
- 20261003T052739Z LEG D2 closed: targeted plan 0/4/0; safe-apply ~05:2xZ Apply complete 0/4/0 (naming PASS 6); read-back: irpt-holdings-performance-lambd
- 20261003T052825Z LEG V2 closed: dry-run invokes WITHOUT date ~05:2xZ: irpt-holdings-performance-lambda {dry_run, source schwab_08335338} planned [2026-1
- 20261003T062357Z LEG D1 closed: CTO half on blob U+miRkw3 signed (batch 210, @47dc514ff1); targeted plan 0/1/0 (s3_object_version 7GwiGHEP -> iw5pK0Bh, 
- 20261006T001445Z LEG A1 closed: Mon 2026-10-05 scheduled fires read from CloudWatch: irpt-holdings-performance-lambda 11:30:11Z computing date=2026-10-0
- 20261006T001445Z CLOSED -- all 5 legs proven
