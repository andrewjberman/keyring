# MDPF_ASSETS.024 -- Aggregator Headline Formula = Cohort 1a+1b+1c+2a

**Agent:** 0.4.0_DS_ClientPlatform (DS Base)
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.024 (COO~B 2026-05-20, from Andrew's headline-formula ruling)

## Current State

COMPLETE -- `mdpf_aggregate_aua.py` headline `opal_aggregate_aua` is now
Cohort 1a+1b+1c+2a; Cohort 2b + Cohort 0 are explicit audit fields. Commit
`70e73d4e8`, pushed to CLOUD, S3-deployed to `s3://opal-data-mdpf/code/scripts/gold/`
(both files etag MATCH). All 7 ACs met. RAVC2 to COO~B (routes to CTO~B).

## What shipped

Andrew 2026-05-20 ruling: the Model Portfolios headline AUA = 1a (49F model) +
1b (49F non-model) + 1c (49F SMA) + 2a (Inflection model). Cohort 2b
(Inflection non-model) + Cohort 0 (ETF public residual) are tracked daily but
audit-only -- not in the headline.

- `HEADLINE_NONMODEL_FIRMS = ("49financial",)` -- the firms whose non-model
  (Nb) enters the headline.
- `opal_aggregate_aua = partner_aua_subtotal - cohort_2b` where
  `cohort_2b = sum of every non-headline partner's non-model`. New named audit
  fields on the aggregate block: `cohort_2b_audit`, `headline_formula` (a
  plain-text statement of the derivation); `etf_public_residual_total`
  retained (Cohort 0 audit). `partner_aua_subtotal` = the all-cohort sum.
- `identity_1` reconciles `opal_aggregate_aua` against
  `partner_sum - cohort_2b` (cohort_2b recomputed independently of the
  aggregate block) -- a correct run PASSes, does not false-fail.
- **MDPF_ASSETS.019 sentinel-3 interaction (the TO flagged it):** sentinel 3's
  independent feeder-direct recompute of `opal_aggregate_aua` summed ALL
  partners' non-model. With the new headline that would false-ERROR every run
  (indep would be the all-cohort sum, WS-A the 2b-excluded headline). Fixed:
  the independent recompute now filters `non_model` to
  `HEADLINE_NONMODEL_FIRMS`, mirroring the headline. Verified $0.00 divergence
  on the Phase-4 run.

## Acceptance Criteria

| AC | Result |
|----|--------|
| AC1 | PASS -- `opal_aggregate_aua = 1a+1b+1c+2a`. Verified by direct read + the new `test_cohort_2b_excluded_from_headline` fixture. |
| AC2 | PASS -- `cohort_2b_audit` + `etf_public_residual_total` emitted as named audit fields; `headline_formula` string makes the headline/audit split unambiguous. |
| AC3 | PASS -- `identity_1` reconciles against the new headline (`partner_sum - cohort_2b`); cohort_2b independently recomputed. identity_2/3 unaffected. Real run identity_1/2/3 PASS. |
| AC4 | PASS -- fixtures 6/6: `test_valid` headline 360M->330M + audit-field asserts; new `test_cohort_2b_excluded_from_headline` (fails if 2b leaks). |
| AC5 | PASS -- Phase-4 real run 2026-05-19 (`--source s3`): headline `$1,742,546,667.10`, down from `partner_aua_subtotal $1,848,801,032.18` (drop = `cohort_2b $106,254,365.08`); `etf_public_residual_total $91,310,278.05`; reconcile overall PASS (identity_1/2/3 + all 3 sentinels). |
| AC6 | PASS -- commit `70e73d4e8` via safe-commit.sh, push CLOUD, `aws s3 cp` both files to `s3://opal-data-mdpf/code/scripts/gold/` (mdpf_aggregate_aua.py etag `818131b8344a7a934cee4113b5341776`, fixtures `14cbf7a9114a25c2abfecd3b9ae38d31`, MATCH). ds-commit-gate exit 0; Rule 15; no emoji. comp-pipescript deployed / comp-validate N/A -- MDPF scripts off the comp graph per CTO 2026-05-20 (builder scan-path gap); MATCH verified via md5/etag + fixtures 6/6 + real-data dry-run as the validation substitute. |
| AC7 | This session log. RAVC2 to COO~B. |

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/gold/mdpf_aggregate_aua.py | `HEADLINE_NONMODEL_FIRMS`; `opal_aggregate_aua = partner_total - cohort_2b`; `cohort_2b_audit` + `headline_formula` audit fields; identity_1 reconciles vs the new headline; sentinel-3 independent recompute filtered to headline firms; run() log line. |
| data/mdpf/scripts/gold/mdpf_aggregate_aua_fixtures.py | `test_valid` 360M->330M + audit asserts; new `test_cohort_2b_excluded_from_headline`; registered in `main()`. |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io` / `comp-pipescript deployed` / `comp-validate` | N/A -- `data/mdpf/scripts/` off the comp graph (CTO 2026-05-20: builder scan-path gap, comp-tooling-backlog). Direct file-read for the formula/identity block; md5/etag MATCH + fixtures 6/6 + real-data dry-run as the validation. |
| `.tools/ds-commit-gate.sh` | exit 0 on both files. |
| `mdpf_aggregate_aua_fixtures.py` | 6/6 -- regression gate (no comp node to blast). |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | RAVC2 -- MDPF_ASSETS.024 complete; route to CTO~B for output RAVC-validation. On accept, MDPF_ASSETS.json phase narrative update (DS lane-blocked on project JSONs -- exec/AE commits). |
| **DS Base (self)** | Proceed to MDPF_ASSETS.016 (re-issued) -- it inherits this headline formula via `build_mdpf_process_backfill.py`'s import of the aggregator. |
