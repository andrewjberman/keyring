# IRPT_DASHBD -- ROUND ANALYSIS, round 24

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~17:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 891), REMEDIATION_v10 @f7bd5e9a6c.
- 7 rows: 4 dismissed; W21-S4, S5 and S6 OPEN.
- W20-S2 is closed.
- ARMED 0.
- Suite: 78 passed.

## 1. FWD-4 -- exercised locally, not yet served

- **The exercised window:** one window with a realized gain AND both flows ties term by term. The CVO re-added the terms himself, and
  the gap is -0.0075, inside one cent.
- **Across the sample:** 55 of 91 windows tie. 32 of the 36 misses are 0.05 or less.
- **The grade:** FWD-4's DONE WHEN is a person reading the activity summary, so it grades REALIZED only when the tables are served.
  The release waits on the 4 non-rounding windows (W21-S4), as REMEDIATION_v10 says.
- **The rounding misses:** they are classed and carried. Before the release, the served table states its tolerance where a reader
  meets it.

## 2. ENRICHMENT -- round 25, ONE issuance by `2.0.0_SA_COO~D2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The 4 non-rounding windows named** (W21-S4): 3 MISSING-TERM (a lot basis above the cash paid), 1 OTHER (lots re-selected on an in-kind departure) | (1) each window read against the custodian's lot events, with the term or vendor behaviour named from the rows; (2) a fix goes through the activity or lot rule with the 91-window re-run printed (ties, misses by class), never a per-account patch; anything left is carried and labelled | LOCAL |
| E2 | **The lot-lag bound measured** (W21-S5) | (1) the lag between each trade and its lot row over the read window, printed as a distribution; `LEG_LAG_DAYS` is set from it, with the percentile it covers stated | LOCAL |
| E3 | **The pandas option set once per process** (W21-S6, the build side) | (1) `future.infer_string` is set once per process, or classification runs outside the pool; a threaded test that would flip under the old per-call context passes; (2) the served producer's `classify_and_sum` is hardened against None in the repository, with a test on pandas 3 semantics. Shipping it is the next release's half; today's served layer is pandas 2.2.3 and is unaffected | LOCAL |

The release of the activity and lot tables follows E1, under its own halves, carrying W20-S1 and W20-S3.

-- 1.0.0_SA_CTO~DELL2
