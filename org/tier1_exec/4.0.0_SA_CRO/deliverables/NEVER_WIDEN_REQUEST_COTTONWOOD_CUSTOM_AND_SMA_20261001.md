# Never-widen request -- Cottonwood custom models into Models > Custom, Opal SMA sleeves into SMA

**Author:** 4.0.0_SA_CRO (Chief Research Officer). **For:** `1.0.0_SA_CTO` and one `2.0.0_SA_COO` seat. This file is
the request; it signs nothing.
**Authority:** Andrew-direct 2026-10-01 ~20:3xZ and ~20:4xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261001_203xZ_COTTONWOOD_CUSTOM_MODELS_AND_SMA_SLEEVES_YES_TO_ALL_FOUR.md`:
"yes to all four, move them into Custom and add DIVZ SMA and The Disciplined Equity SMA and any others you find
similarly"; "anything that is Pathfinder Disciplined Equity that is PFDE SMA, Whereas pathfinder focused opportunity
sma would be PFOE SMA".
**Candidate:** branch `wk-mdpf_taxsma-cro` @e20899bce7 (85dd7adc26 feature, 8c842b4d44 and e20899bce7 two latent
defects the rehearsal surfaced). NOT deployed. The deployed Gold function runs pin 0f1a67e196.

## The act

One Gold deploy: `mdpf-gold-lambda` from pin 0f1a67e196 to the candidate pin (code only; the four TAXSMA_ settings
unchanged). Writers of the moved properties: ONE -- `mdpf-gold-lambda` writes every dated A4 document; the publisher
copies them. No override path: the first served effect is the next scheduled production run (13:30Z) and the 13:50Z
publisher run. Dated keys for that run's data_as_of are new keys, so `conditional_put` writes them; no delete-mark is
needed.

## The blast radius, measured

Two local `qa_local` builds of the packaged code, zero writes, Tax disabled in both (so only this change differs):
baseline = deployed pin 0f1a67e196, candidate = e20899bce7. Both green, 16 of 16 documents (21:16Z and 21:5xZ;
Cottonwood/Inflection also compared on one same-input pair at 21:4xZ with identical results). Process-time fields
excluded. Denominator: 16 documents; 9 move.

| Scope | Document | What changes (latest point, valuation 2026-09-30) |
|---|---|---|
| cottonwood | category-views | Models 178,495,341.63 -> 202,516,015.64 (Custom 0 -> 24,020,674.01: Opal Fixed Income 8,236,852.21; Opal Moderate Income Portfolio 7,597,526.06; Opal Income Portfolio - Gillham 3,996,545.12; Opal Moderate Income Tax Efficient 3,149,002.79; Opal Muni Sleeve 549,076.95; Opal 15/85 Income Portfolio 299,702.09; Opal Moderate Income 191,968.79). SMA 0 -> 405,856.99 (PFDE). Client 362,817,714.13 -> 338,391,183.13. Total 541,313,055.76 both ways |
| cottonwood | aggregate-aua-timeseries | model_aua +24,020,674.01, non_model_aua -24,020,674.01, total unchanged; 40 of 487 dates differ (every date a custom model existed); by_model gains nine custom keys and `pfde` (cohort `sma`) |
| cottonwood | aum-metrics | model_aum +24,020,674.01, non_model_aum the same down, account_count 361 -> 378; total unchanged |
| cottonwood | account-distribution | seven custom by_model rows; funded accounts 355 -> 372; total_aum 190,476,646.23 -> 206,068,499.24 |
| global | aggregate-aua-timeseries | opal_aggregate_aua and model_aua +24,020,674.01 (2,060,678,513.01 -> 2,084,699,187.02); non_model unchanged; 52 of 487 dates differ; nine custom by_model keys |
| global | aum-metrics | total 2,060,678,513.01 -> 2,084,699,187.02 |
| global | category-views | Models +24,020,674.01; Custom 42,899,101.50 -> 66,919,775.51; SMA and Client unchanged |
| 49financial | category-views | the Custom member LIST gains nine members with null aum; no dollar moves (the portal filters null members) |
| inflection | category-views | the same: nine null members; no dollar moves |
| everything else (49financial x3, inflection x3, global account-distribution) | IDENTICAL | |

Identities that hold on every scope: Cottonwood's total does not move; its Models gain equals its Custom sum; its
Client loss equals Custom plus SMA; Global's total and Custom move by exactly Cottonwood's Custom sum; Global's SMA
and Client do not move.

## What the rehearsal cannot show, and what production adds (both branches named)

1. **DIVZ SMA.** Anna Thiessen's 7% "DIVZ SMA" sleeve enters only when the production run mints the day's dim
   partition (a dry run never writes it). Expected: Cottonwood SMA gains about 1,365,000 (7% of the account's
   19,496,354.72 on 09-30) and Client loses the same; no Global move (Cottonwood's SMA sleeves are not folded into
   Global -- Global's population excludes Cottonwood's non-model dollars, so folding them would need a mixed
   carve-out/additive basis on one registry member; not built). Branch where the sleeve is absent that day: nothing
   from it moves.
2. **Global account-distribution.** In a dry run it reads the staged Cottonwood sidecar from S3; production restages
   it, so global gains the seven custom rows and the 17 accounts. Unit-tested (`account_dist_display` for every custom
   key).
3. **Tax is ON in production.** Cottonwood SMA = Tax 6,045,602.28 + PFDE (+ DIVZ): the Tax figures and identities
   of TX-r-3 are untouched (the 9 Tax documents are a separate, signed change).
4. **A new Opal-named model** with no CUSTOM_KEY row still routes to the named residual (Client) until registered.

## Two latent defects fixed inside the candidate (both found by this rehearsal on real data)

- `_shape_category_views`: the Models > Primary/Custom bucket sum added a member whose latest value is null
  (`opal_income`, last seen 2026-08-20) and raised TypeError, aborting build_all for every scope. It now omits it,
  as the member loop already did. 49financial/inflection unchanged (measured IDENTICAL).
- `_distribution_stats`: a one-account model's sample std dev was NaN, which the canonical writer refuses. It is
  None for n < 2; every n >= 2 figure unchanged.

## Rollback per key

Code: the prior S3 artifact version + `MDPF_GOLD_COMMIT` back to 0f1a67e196, plan, safe-apply. Served: the dated
documents the new code wrote for that run's data_as_of are delete-marked (prior versions restorable), the Gold run and
the publisher run once on the old code.

## Interaction with an open ledger -- the CTO's call

`mdpf-gold-healgap-hookup-20261001` leg V2 reads the **2026-10-02 13:30Z** run and rolls back on "any served change
outside the five cottonwood dates and global's same five, EXCEPT exactly TX-r-3 branch 1". Deployed before that run,
this change trips that trigger. Either (a) amend V2's trigger to admit exactly the changes in the table above under
the identities stated, and deploy tonight so the 10-02 run serves it; or (b) deploy after V2's read, so the 10-03 run
serves it. This seat recommends (a): the identities separate the two changes cleanly, and Andrew is waiting on it.

## Tests

`data/assets/scripts/gold/tests/test_cottonwood_custom_and_sma.py` (27). Suites data/mdpf/tests +
data/assets/scripts/gold/tests + data/mdpf/scripts/gold/tests: all pass except failures that fail identically at CLOUD
head (pair_identity_cents x4, slice_rekey x2, cottonwood_aua live, global_fold_flag2 x3).

## Outside this deploy, named

`investor_reporting/holdings_snapshot.py` reads `OPAL_SMA_LEAF_KEYS` by exact name: on ITS next deploy the
Pathfinder Disciplined US Equity leaf reads SMA (pfde) instead of Client. Its CANONICAL_KEY (Primary) and
is_auto_custom (Custom) readings are unchanged.
