# MDPF v0.9 post-deploy chain verification (verify-channel sweep)

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B (verifier; NOT the v0.9/.028 author -- verifier != fixer holds)
**Directed by:** 2.0.0_SA_COO~B (stimulus-scan dispatch)
**Type:** non-mutating read-only verification sweep. **Verdict: PASS** (one honest-limit, no drift).

---

## Verdict

**PASS.** The live v0.9 platinum aggregate artifact is healthy and the v0.9 `.028`
scripts are MATCH-deployed to the mdpf-daily-runner code path. No drift -- no stale-code,
no v0.8/v0.9 mismatch in the live artifact, chain firing on schedule. One honest-limit
(below): the empirical "a daily-chain run produces v0.9" is pending the next scheduled
fire -- structurally assured by the deploy-MATCH, not yet chain-run-demonstrated.

## Step 1 -- delivery contract

- Consumer path: `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` (the
  CloudFront-served portal bucket; `PLATINUM_BUCKET` in `mdpf_aggregate_aua.py:66`).
  Note: COO~B's brief said `opal-data-mdpf` -- the actual consumer path is
  `opal-data-portal-v2`; `opal-data-mdpf/platinum/mdpf/aggregate_aua/` is empty.
- Producer: `mdpf_aggregate_aua.py` (WS-A) + the WS-E feeder `build_mdpf_wse_49f_non_model_aua.py`.
- Cadence: mdpf-daily chain, `cron(0 15 ? * MON-FRI)` UTC.

## Step 2 -- 4-check method (artifact: 2026-05-20.json)

| Check | Result | Evidence |
|-------|--------|----------|
| **EXISTS** | PASS | `2026-05-20.json` present, 7950 bytes. |
| **FRESH** | PASS | head-object LastModified `2026-05-20T21:59:30Z`; `generated_at 2026-05-20T21:59:27Z`, `as_of_date 2026-05-20`. Today's data, recent honest write-stamp. (Written by the `.028` v0.9 re-emit, not the 15:00 cron -- see Step 2.5.) |
| **SCALED** | PASS | 7950 bytes vs prior 2026-05-19 (6771) / 2026-05-18 (6829) -- in-family, slightly larger (v0.9 added `etf_decomposition` + cohort fields). Not a partial run. |
| **NOT-FROZEN** | PASS | ETag `3b0402e7...` vs 2026-05-19 ETag `71175ac8...` -- distinct; content genuinely different (different as_of_date, figures, `methodology_version`). |

**v0.9 headline content -- all expected values confirmed:**
- `methodology_version: v0_9` (expected v0_9).
- `aggregate.opal_aggregate_aua: 1748030393.45` (expected ~$1.748B -- EXACT match to the `.028` headline $1,748,030,393.45).
- 49financial partner `total_aua: 1654331683.26` = model 1349272608.00 + sma 24929683.38 + non_model 280129391.88 -- the v0.9 3-term basis (1a+1c+1b), 49F_total ~$1.65B confirmed; reconciles to the cent.
- `headline_formula`: "opal_aggregate_aua = 1a+1b+1c+2a = partner_aua_subtotal - cohort_2b_audit" -- 1854284758.53 - 106254365.08 = 1748030393.45, reconciles exactly.

## Step 2.5 -- sharp structural test (aggregate-identity masking)

The `reconciliation` block -- every gate PASS:
- `identity_1_aggregate_sum` PASS (residual 0.0) -- AND a per-component `model_aua_input_check` PASS ("model_aua_input + sma_aua_input match the cohort_class sums for all firms"), so it is not a bare aggregate identity.
- `identity_2_etf_residual` PASS; `identity_3_no_double_count` PASS.
- `sentinel_1_cohort0_dod` PASS (Cohort 0 DoD 0.0% -- $91,335,123.78 vs $91,310,278.05).
- `sentinel_2_partners_present` PASS ([49financial, inflection], none missing -- the 2026-05-19 Cohort-0-incident class).
- **`sentinel_3_cross_validation` PASS -- WS-A $1,748,030,393.45 vs INDEPENDENT recompute $1,748,030,393.45, diff $0.00.** This is the 2nd-producer cross-validation that defeats the identity_1-masking class (`feedback_identity1_masks_absolute_value_class`): the headline is confirmed by an independent recompute, not just an internal sum. Sharp test PASS.

## Step 2 (check 2) -- chain consuming the v0.9 scripts

- v0.9 gold scripts committed at `dd3cd4d22` (MDPF_ASSETS.028 atomic co-land); local working tree clean.
- **Runner code path MATCH** (`s3://opal-data-mdpf/code/scripts/gold/`, the path the mdpf-daily-runner bulk-syncs):
  - `mdpf_aggregate_aua.py` -- local md5 `1b0915f2...` == S3 ETag `1b0915f2...` -> **MATCH** (S3 deployed 21:48:45Z).
  - `build_mdpf_wse_49f_non_model_aua.py` -- local md5 `93d7873c...` == S3 ETag `93d7873c...` -> **MATCH** (21:48:41Z).
- Chain firing on schedule: telemetry history shows today's runs -- `mdpf_daily_20260520_150030` (the 15:00 cron fired), `_151238` (15:12 re-run), `_193329` (19:33 re-trigger). The cron is firing.
- (`comp-pipescript deployed` only models `opal-data-bd` gold/silver -- N/A for the mdpf pipeline; direct md5-vs-ETag MATCH substituted.)

## HONEST-LIMIT (Step 3.5 -- the one thing to flag; NOT drift, NOT a defect)

The live v0.9 artifact (2026-05-20.json, written 21:59Z) was produced by the
**MDPF_ASSETS.028 manual v0.9 re-emit** (scripts deployed 21:48Z -> aggregator re-run
21:59Z), **not by a daily-chain run.** The most recent mdpf CHAIN run (`_193329`, 19:33Z)
predated the 21:48Z `.028` deploy and therefore ran the pre-v0.9 (v0.8) code.

So: "the daily chain delivers v0.9" is **verified-by-deploy-MATCH** (the v0.9 scripts are
correctly on the runner code path -> the runner's boot-time `code/scripts/` sync picks
them up) but **not yet verified-by-a-chain-run.** The next scheduled daily chain
(2026-05-21 15:00Z) is the first chain run that consumes v0.9 -- a passive post-15:00Z
check of tomorrow's `2026-05-21.json` (`methodology_version=v0_9`, single write, sentinels
PASS) closes the last empirical gap. This is correct sequencing, not drift -- the `.028`
re-emit was the interim bridge; the deploy-MATCH guarantees the next chain run is v0.9.

## Decision-useful (Step 3.5)

The artifact is the platinum aggregate the portal Model Portfolios headline consumes.
opal_aggregate_aua $1,748,030,393.45 is a meaningful, plausible firm-AUA headline; the
`headline_formula` is explicit and reconciles; `sentinel_3` independently recomputes it
to the cent. Decision-useful PASS -- assessed structurally (reconciliation + independent
cross-validation), with the honest-limit that run-to-run stability was not re-probed
(overwrite-in-place per date; a 2nd run would make the verifier the producer).

## Routing

PASS -> RAVC2 to 2.0.0_SA_COO~B (CC 1.0.0_SA_CTO~B). No defect found -> nothing to route
for repair. The single honest-limit (chain-run empirical confirmation pending tomorrow's
15:00Z fire) is a passive post-fire check, not a repair -- noted for whoever sweeps after
the 2026-05-21 chain.
