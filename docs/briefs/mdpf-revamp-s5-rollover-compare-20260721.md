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
- **Serving path grounded (comp-routes):** the FE's `/api/general/mdpf/*` + `/api/general/portfolios/*` fall under the CloudFront `/api/general/*` behavior → origin **S3-opal-data-portal-v2-json**, with the **public-data-router L@E** (origin-request) doing the path→S3-key rewrite (+ cache-control-injector on response). This behavior serves ALL `/api/general/*` → a repoint touches a shared surface; scope tightly.
- **Serving-target options + the DURABILITY finding:**
  - **Option 1 (repoint origin → opal-data-assets):** point the `/api/general/mdpf|portfolios/*` serving at an opal-data-assets S3 origin (+ OAC) / adjust the public-data-router rewrite to the revamp keys. Legacy producer keeps writing opal-data-portal-v2 UNTOUCHED (shadow); the revamp publisher feeds the served origin durably. **Rollback = single router-revert** (legacy 100% intact). Cost: a CloudFront/L@E/OAC change on a shared behavior.
  - **Option 2 (overwrite portal-v2 served keys, no CF change):** copy revamp artifacts onto `json/mdpf/*` + `json/portfolios/*`; FE keeps same URLs. Rollback = version-restore those keys. **⚠ NOT DURABLE:** the legacy nightly (dispatch Stage 3.5 build_legacy_compat_emit + Stage 4 build_aggregate_aua_timeseries + the account-dist script) REWRITES those exact served keys every run → it clobbers the overwrite within a day. Making it durable requires DISABLING the legacy producer's serving-writes → breaks "legacy untouched" + removes the shadow/rollback-source.
  - **AE reco:** **Option 1** for a DURABLE cutover (legacy stays a clean shadow + instant router-revert rollback). Option 2 only if this is a one-shot demo (not a standing cutover). Final target set with DE once the FE-delta audit says whether fetch URLs change.
  - **LOCKED (CTO 183625Z + 183814Z):** Option A = the STANDING cutover (B ruled out on durability). Push-now = durable serve, not a demo.

### S5 standing-cutover SEQUENCE (CTO 183814Z — verify-before-serve; publisher auto-arm DEFERRED past cycle-1)
Risk closed (CVO-adopted): the first post-cutover SCHEDULED cycle produces from freshly-deployed, UNEXERCISED S4/publish wiring — if the publisher auto-copied, a bad first-scheduled artifact would reach the live page before verify. So the publisher stays HELD through cycle-1.
0. **Pre-repoint populate (one-time, gated, SAFE — not a serve-widen):** manual publisher invoke on the CURRENT verified hand-staged gold/mdpf_revamp/* (all 7, pre-proof) → opal-data-assets/portal/*; verify fresh+complete (ListObjectsV2, ETag==staged). Nothing serves it yet.
1. **REPOINT (the single co-signed serve-cutover):** router /api/general/mdpf|portfolios/* origin opal-data-portal-v2 → opal-data-assets/portal/* (serving the verified pre-proof). Publisher = ON-DEMAND/HELD (NOT auto-scheduled).
2. First scheduled PRODUCER run → new gold/mdpf_revamp. **Publisher STILL HELD** → opal-data-assets/portal/* keeps serving the pre-proof (an unverified scheduled artifact CANNOT auto-reach the page).
3. **VERIFY-BEFORE-SERVE:** CTO+DT+CVO 3-pass verify cycle-1 gold/mdpf_revamp. CLEAN → CTO GO a MANUAL/gated publisher run (gold→portal/*) → page now serves verified cycle-1. DELTA → HOLD (pre-proof keeps serving).
4. **ONLY AFTER cycle-1 proves the scheduled path end-to-end** → ARM the publisher auto-schedule (marker-driven on gold/mdpf_revamp/meta/cycle-complete.json — producer-trigger, not an alert) → cycles 2+ auto-publish, legacy shadow + router-revert rollback throughout.
- Rollback at ANY step = **router-revert** (primary, instant, legacy portal-v2 100% intact) + version-manifest (secondary). Legacy Stage-3.5/4/account-dist keep writing portal-v2 = the shadow.
- **Full pre-push gate (all required):** DE FE-aligned + /frontend-dev render-check on the revamp origin (full-depth clean) + CTO count-wire re-verify + AE router-revert TESTED-armed BEFORE repoint + COO re-co-sign A + CTO GO on the scoped CF/L@E/OAC change.
- **Rollback (TESTED + ARMED):** both buckets versioned=Enabled. Restore = `aws s3api copy-object --bucket <B> --key <K> --copy-source "<B>/<K>?versionId=<pre-capture VID>" --metadata-directive COPY` (exercised byte-identical baseline→cutover→baseline); net-new key = `aws s3api delete-object`. Procedure captures each target key's current VersionId into a rollback manifest IMMEDIATELY before the copy. For Architecture A, primary rollback = router-revert (legacy untouched); data-version-restore is secondary cleanup.
- **Gates before push:** FE aligned (DE) → mandatory `/frontend-dev` render check on the revamp artifacts passes → CTO GO → publish with rollback armed → post-cutover monitoring window (rollback STAYS armed) → confirm clean render over the window → disarm.

## 7. Open cross-refs (not blockers to the audit)
- Publisher (opal-assets-mdpf-portal-publisher) currently targets `opal-data-assets/portal/*` — final serving-target mapping set with DE per the FE-alignment outcome.
- DS in-flight data finalization (does not change the schema frame): account_count served-real wiring (82c4d1ec6), inflection 2026-05-15 launch-date call, source_vintage_last value-exemption → converge to co-sign before AE publish.
- N=3 SCHEDULED streak (CVO/DT/CTO) is a SEPARATE track; this push-now is the Andrew-sovereign path on the verified hand-staged data.
