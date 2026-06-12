# Project Request Brief: ADVI_49NNAFIX

**For:** 1.0.0_SA_CTO (project creation)
**Proposed owner:** 0.4.0_DS_ClientPlatform (data/pipeline lane)
**Requested by:** Andrew (direct, 2026-06-12) via 0.4.0_DE_ClientPlatform
**Priority:** ASAP (Andrew-direct)
**Diagnosed by:** 0.4.0_DE_ClientPlatform — FE control-trace + live-S3 ground-truth

---

## Problem (user-facing)

On **49 Financial** Advisor Intelligence → Segment Analytics → **Continuous-NNA**, only the
**OFC** cohort renders. The **GEO** and **ADV** cohorts are empty. (Inflection's GEO/ADV
Continuous-NNA work — this is 49F-specific.)

## Root cause (DATA, not frontend)

The portal's Continuous-NNA **GEO/ADV** path reads the canonical artifact
`advisor_nna_canonical.json` (portal: `getAdvisorNnaCanonical`, `advisor-intelligence.ts:382-383`,
served from `…/platinum/firm/advisor_nna_canonical.json`). **That artifact does not exist for 49F.**

Evidence (live S3, 2026-06-12):
- `aws s3 ls s3://opal-data-inf/platinum/firm/advisor_nna_canonical.json` → **present** (2.4 MB, gen 2026-06-11)
- `aws s3 ls s3://opal-data-bd/platinum/ --recursive | grep nna_canonical` → **0 hits** (absent for 49F/bd)
- 49F **does** have the upstream NNA data — `s3://opal-data-bd/platinum/firm/cumulative_chart.json`
  carries `nna_geo`, `nna_adv`, `nna_ofc`, `nna_geo_drill`, `nna_adv_drill` (gen 2026-06-12 01:12).

Why OFC still works: the **OFC** cohort reads `nna_ofc` directly from `cumulative_chart.json`
(portal `synthesizeOfcPeriods(data.nna_ofc)`), a different (older) path that does not depend on the
canonical artifact. GEO/ADV were migrated to the canonical NNA source (the F5 "fixes the ~60%
flow-loss" canonical per `getAdvisorNnaCanonical` doc); 49F was never backfilled onto it.

**FE is correctly wired** — 49F's `_partners/49financial/layout.ts` has `geo/adv/ofc` all `enabled`;
the FE surfaces all three. The cohorts are empty purely because the canonical artifact is missing.

## Scope (DS lane) — TWO deliverables

### D1 — Publish 49F `advisor_nna_canonical.json` (the primary 49F fix)

Run/extend the canonical-NNA publisher (the pipeline that already produces inflection's artifact) to
emit for the **bd** firm. The underlying inputs already exist (49F `cumulative_chart.json` has the
geo/adv NNA series), so this is a publisher-coverage gap, not a missing-upstream-data problem.
Match the inflection artifact's shape: `firm.series` (weekly/monthly/quarterly), `geo.states[*].series`,
`advisors[*].series`, `window_bounds` (QTD/YTD/1Y/3Y/MAX), `granularity_coverage`.

### D2 — FIPS state-code "34" — ASSESS SOURCE (Orion-input vs our-pipeline), then RECTIFY (Andrew-direct)

Inflection `advisor_nna_canonical.json` `geo.states` has a literal key **`"34"`** (FIPS for New
Jersey) next to proper USPS abbrevs (AZ/CA/TX/…). The portal maps only 2-letter abbrevs, so it
renders "34". **Andrew directive (2026-06-12): DS must first ASSESS whether "34" is an INPUT error on
Orion's side (the upstream provider emitting a FIPS code for that record) or whether it is introduced
by OUR pipeline's normalization (our bug) — and in EITHER case DS rectifies it.**

Lineage trace DS should run: follow the state field from the **Orion raw pull (bronze)** → silver →
gold/canonical, and find where "34" enters and where the USPS normalization should have caught it.
- If Orion emits "34" (or mixed FIPS/USPS) → our pipeline must defensively normalize FIPS→USPS
  (and DS should flag the Orion inconsistency).
- If Orion emits "NJ"/clean and our normalization mangled it to "34" → fix our pipeline step.
Rectification (both cases): canonical `geo.states` keys are uniformly USPS 2-letter abbrevs; no raw
FIPS leaks. Re-audit for any OTHER numeric/FIPS leaks across both firms while in there.
(Independent optional FE hardening, DE lane, not blocking: FIPS-fallback in `formatStateLabel`.)

## Acceptance

- **D1:** `s3://opal-data-bd/platinum/firm/advisor_nna_canonical.json` published, schema-parity with
  the inflection artifact (firm/geo/advisor series weekly/monthly/quarterly + window_bounds). Portal
  49F Segment Analytics → Continuous-NNA → **GEO** + **ADV** cohorts render (verify DEV/5173; no
  portal code change — FE already reads the canonical).
- **D2:** written source-assessment verdict (Orion-input vs our-pipeline, with the lineage evidence)
  + canonical `geo.states` keys all USPS abbrev (0 FIPS/numeric leaks, both firms).
- Validated on the scheduled nightly artifacts (not an ad-hoc gold run), per cost-governance.

## Related finding (CTO to fold or spin separately; NOT 49F-blocking)

**No annual series** — inflection `firm.series` is weekly/monthly/quarterly only (`series_policy:
"full weekly/monthly/quarterly"`); the portal's "Year" interval has nothing to show for
Continuous-NNA. Either emit an annual series (DS) or hide "Year" for Continuous-NNA (FE). Lower
priority than D1/D2.

## NOT in this project (separate FE bug, DE/RD lane)

Advisor-drill **Continuous-ADV-AUM** Interval/Window toggles are a genuine **frontend** bug (the
`relationship_stacked_periods` path drops `granularity`/`timeWindow` — query key omits them, render
uses data as-is). Data supports it (`window_bounds` has real 1Y/3Y/MAX). This is a portal fix, not DS.

---

*Brief by 0.4.0_DE_ClientPlatform 20260612. Diagnosis evidence: live S3 + DistributionTab FE trace.*
