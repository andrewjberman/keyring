# MDPF_REVAMP.S5 Roll-Over — Compare & Contrast + Strategy

**TO:** MDPF_REVAMP.S5-ROLLOVER · **Date:** 2026-07-21 · **Status:** DRAFT (tandem: 0.4.0_DE_ClientPlatform + 0.7.0_AE_CloudOps) · **Gate:** CTO · **Coord:** COO
**Andrew-direct frame:** models-only by design; data-side is CORRECT; the roll-over is **frontend alignment** to the revamp schema; ETFs are a **future** schema expansion, not this cutover.

## 1. Frame (Andrew rulings, verbatim)
- "this is focused solely on models, if we want to incorporate ETFs we can expand on the schema as needed to do so"
- "our structure is correct on the data side from what I can tell, the issue is more a factor of making sure that we are clear on the frontend side with the 0.4.0_DE_ClientPlatform"
- Cutover is a sovereign PUSH-NOW on the verified hand-staged data, **rollback-armed** ("be ready to roll it back immediately if it doesn't work").

**Consequence:** the FE aligns FORWARD to the revamp (model-focused) schema. We do NOT reproduce the legacy schema in the producer. CTO's initial lean-(a) (producer reproduces served schema) was superseded by Andrew's FE-alignment frame (CTO confirmed 182520Z).

## 2. Leg split
| Lane | Owner | Scope |
|---|---|---|
| Frontend alignment | **0.4.0_DE_ClientPlatform** | FE-consumption audit → per-key FE deltas → the FE changes (endpoint transforms + components + queryFns) to consume the revamp schema off `opal-data-assets` |
| Cutover mechanics | **0.7.0_AE_CloudOps** | publish path, origin/router (CloudFront/L@E) repoint execution, rollback arming/exercise, per-key VersionId manifest |
| Gate | 1.0.0_SA_CTO | gates each step; final co-sign |
| Coord | 2.0.0_SA_COO | cross-lane coordination |

## 3. Shared grounding — the 7 keys (revamp → served → FE)
Served keys (what the FE reads today) are on `opal-data-portal-v2` via the `public-data-router`/`shared-advisor-router` L@E. Revamp keys are on `opal-data-assets`. Day-depth matches (427≈429; revamp is *more* recent, 07-20 vs 07-18).

| # | Revamp key (opal-data-assets) | Served key (opal-data-portal-v2, FE reads) | Served sz | Revamp sz | Note |
|---|---|---|---|---|---|
| 1 | gold/mdpf_revamp/global/aggregate_aua_timeseries.json | json/mdpf/aggregate-aua-timeseries.json (== platinum/mdpf/aggregate_aua_timeseries.json, byte-identical) | 443868 | 165549 | **schema delta (global)** — see §4 |
| 2 | gold/mdpf_revamp/49financial/aggregate_aua_timeseries.json | json/mdpf/49financial/aggregate-aua-timeseries.json | 156730 | 152815 | close |
| 3 | gold/mdpf_revamp/inflection/aggregate_aua_timeseries.json | json/mdpf/inflection/aggregate-aua-timeseries.json | 122801 | 126188 | close |
| 4 | gold/mdpf_revamp/49financial/account_distribution.json | json/mdpf/49financial/account-distribution.json | 5392 | 5473 | close |
| 5 | gold/mdpf_revamp/inflection/account_distribution.json | json/mdpf/inflection/account-distribution.json | 6878 | 6904 | close |
| 6 | gold/mdpf_revamp/global/account_distribution.json | json/portfolios/account-distribution.json | 7708 | 7234 | close |
| 7 | gold/mdpf_revamp/global/non_model_assets.json | json/portfolios/non_model_assets.json | 114616 | 82101 | schema/size delta (global) — audit |

## 4. Schema delta (the GLOBAL aggregate — the material one)
- **Served global keys:** `[as_of_first, as_of_last, source_vintage_last, n_dates, dates, methodology_version, aggregate{opal_aggregate_aua,model_aua,non_model_aua}, partners{49financial,inflection}, etf_decomposition{DIVZ,IDVZ,PFDE,PFOE}, meta]`
- **Revamp global keys:** `[firm_id, as_of_first, as_of_last, n_dates, dates, opal_aggregate_aua, model_aua, non_model_aua, by_model, source_vintage_last, meta]`
- **Deltas:** revamp (correctly, per Andrew) drops `etf_decomposition` (OLD/future-expansion) + `partners` (audit if FE-consumed) + `methodology_version`; **flattens** `aggregate.*` to top-level; **adds** `by_model` + `firm_id`.
- **Why parity "passed":** DT/CVO date-joined parity compared VALUES at mapped paths, not the served SCHEMA / field-completeness. Values tie to the penny; shape does not.

## 5. FE-consumption audit — **[0.4.0_DE_ClientPlatform to fill]**
Ground on the real FE queryFns + the revamp artifacts (never assume). For each of the 7 keys:
- which component(s)/endpoint-transform(s) read it, and every field they access;
- which revamp deltas actually affect a read (e.g., nested `aggregate.model_aua` → flat `model_aua`; `partners` reads?);
- the exact FE change to consume the revamp schema (transform + component + type);
- confirm no legacy-only field (partners/etf/nested/methodology_version) is load-bearing for a **models** view — if one is, surface to Andrew (models-scope drop, not a default).
- Starting pointers (AE-grounded, verify): `portal/src/api/endpoints/aum.ts`, `portal/src/api/portal-proxy.ts` (interfaces `MdpfGlobalTimeSeries` L451 nested `aggregate/partners/etf_decomposition`; per-firm slice = flat top-level, L423/492), `portal/src/pages/ModelPortfolios.tsx` (reads `rawTimeSeriesData.aggregate`, L480/629/633/756). `partners`/`etf_decomposition` not obviously accessed in pages/components (grep) → likely vestigial for the models view, DE to confirm.

## 6. Cutover mechanics — **[0.7.0_AE_CloudOps]**
- **Mechanism (CTO-approved):** Architecture A — origin-repoint. Publish the 7 revamp artifacts to the serving path, then repoint the router/L@E to serve the revamp (off opal-data-assets or into the portal-v2 served keys — final target set with DE once FE deltas are known). Legacy stays 100% untouched (Stage 5 shadow keeps producing) → rollback is a single revert.
- **Rollback (TESTED + ARMED):** both buckets versioned=Enabled. Restore = `aws s3api copy-object --bucket <B> --key <K> --copy-source "<B>/<K>?versionId=<pre-capture VID>" --metadata-directive COPY` (exercised byte-identical baseline→cutover→baseline); net-new key = `aws s3api delete-object`. Procedure captures each target key's current VersionId into a rollback manifest IMMEDIATELY before the copy. For Architecture A, primary rollback = router-revert (legacy untouched); data-version-restore is secondary cleanup.
- **Gates before push:** FE aligned (DE) → mandatory `/frontend-dev` render check on the revamp artifacts passes → CTO GO → publish with rollback armed → post-cutover monitoring window (rollback STAYS armed) → confirm clean render over the window → disarm.

## 7. Open cross-refs (not blockers to the audit)
- Publisher (opal-assets-mdpf-portal-publisher) currently targets `opal-data-assets/portal/*` — final serving-target mapping set with DE per the FE-alignment outcome.
- DS in-flight data finalization (does not change the schema frame): account_count served-real wiring (82c4d1ec6), inflection 2026-05-15 launch-date call, source_vintage_last value-exemption → converge to co-sign before AE publish.
- N=3 SCHEDULED streak (CVO/DT/CTO) is a SEPARATE track; this push-now is the Andrew-sovereign path on the verified hand-staged data.
