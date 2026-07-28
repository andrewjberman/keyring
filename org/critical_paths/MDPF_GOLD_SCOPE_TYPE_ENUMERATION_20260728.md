# PIN-1 (D3): pinned (scope,type) design set — `opal-data-assets/portal/gold/mdpf/**`

**Authored:** 2026-07-28 ~23:00Z by 0.7.0_AE_CloudOps, AFTER WO-1's chain re-run
(`mdpf_daily_20260728_225137`, Stage 6 rc=0, cycle-complete.json first emit 22:55:12Z) and the
P1 accrual pass (22:57:22Z, written=4 skipped_existing=7 errors=3), and BEFORE any WO-2
publisher invoke. This is the design set the written `platinum/mdpf/**` set is diffed against,
BOTH directions (PIN-1/D3, CVO pins @d75f736c53).

## The design set: 11 (scope,type) pairs expected in the first publish

| scope | artifact-type | latest gold date-key | data as-of basis |
|---|---|---|---|
| 49financial | aggregate-aua-timeseries | 2026-07-27 | as_of_last (T-1 frontier) |
| 49financial | account-distribution | 2026-07-28 | period |
| inflection | aggregate-aua-timeseries | 2026-07-27 | as_of_last |
| inflection | account-distribution | 2026-07-27 | period (eclipse D+1 cadence) |
| cottonwood | aggregate-aua-timeseries | 2026-07-27 | axis frontier; cottonwood values as-of 2026-07-24 (BD vendor reach) |
| cottonwood | account-distribution | 2026-07-24 | value_date (assignment 07-28 x value 07-24, labelled on artifact) |
| cottonwood | aum-metrics | 2026-07-24 | period=value_date |
| cottonwood | account-units | 2026-07-24 | value_date |
| global | aggregate-aua-timeseries | 2026-07-27 | as_of_last |
| global | account-distribution | 2026-07-28 | period |
| global | non-model-assets | 2026-07-27 | time_series_last_period |

## Declared-but-absent (NOT in the publish set; known gaps, named — R4 errors are correct output)

- `49financial/aum-metrics`, `inflection/aum-metrics`, `global/aum-metrics` — DECLARED all-scopes
  (ruled DRIFT, not by-design: CTO 195158Z on consumer evidence `portal/src/api/endpoints/aum.ts:696`
  templated on firmId). Missing because the revamp source tree does not yet produce them. A
  publisher run must NOT invent these; their later appearance extends the design set.

## Declaration status flags carried from the accrual's DECLARED_TYPES (read, not inferred)

- `non-model-assets` scopes={global}: DECLARED by design.
- `account-units` scopes={cottonwood}: DECLARED cottonwood-only, **status UNVERIFIED — needs a
  consumer trace** (open question on the record; CTO routed).

## Known content caveat (disclosed, not a design-set change)

`global/aggregate-aua-timeseries` @07-27 headline (`opal_aggregate_aua` $1,826,143,796.13)
EXCLUDES cottonwood at the frontier (fold provenance: cottonwood `absent` on 07-23/24/27; only
2 measured + 45 interpolated dates). Andrew-stated correct headline ≈ $1.95bn = 49F custody
$1,684.26mm + INF models $141.88mm + COT models $125.13mm (the ruled fee-basis composition).
Fold roll-forward-vs-absent at the frontier is a producer ruling pending at CTO.
