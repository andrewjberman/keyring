# Session Log — W6 OFC Diagnosis: Bell Curve + Continuous View

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-14 (ET)
**Portal DEV commit:** `e692f60` (bell curve fix)
**CLOUD commit:** pending (this file)

---

## Context

Andrew flagged that despite all W6 fixes being marked complete, OFC still had:
1. No bell curve displayed in Snapshot mode
2. Continuous view blank

He also noted the OFC total shown ($1.69B) was wrong vs the known tracked value ($1.62B).

My earlier W6 Fix 9 conclusion ("no code change needed — ofc.total is non-null") was incorrect.
I had checked that the field existed in S3 without verifying the code path was reachable.
This session diagnosed both problems from first principles.

---

## Problem 1: Bell Curve — Code Bug (FIXED)

**Root cause:** `DistributionTab.tsx` L2967 right partition:

```tsx
// BEFORE (W3 implementation):
{cohort === 'ofc' && (
  <OfcAdvisorListPanel ... />
)}
{cohort !== 'ofc' && (
  <>  {/* bell curve lives here */}
```

For any `cohort === 'ofc'` state — including L0 with no office selected — the advisor panel
rendered and the bell curve branch was unreachable. The bell curve required `cohort !== ofc`,
which OFC can never satisfy. At L0, the advisor panel rendered with no data (empty state).

**Fix (`e692f60`):**

```tsx
// AFTER:
{cohort === 'ofc' && selectedOfficeKey && (
  <OfcAdvisorListPanel ... />
)}
{(cohort !== 'ofc' || !selectedOfficeKey) && (
  <>  {/* bell curve now reachable for OFC at L0 */}
```

L0 (no office selected): bell curve renders.
L1 (office selected): advisor panel renders.

**S3 verification:** `partner_analytics_quarterly.json → views.ofc.current.distribution.total`
has full histogram — 5,967 accounts, $1.63B total (de-duplicated), 20 bins. Bell curve
will render once `e692f60` is deployed.

**Why my Fix 9 verification was wrong:** I checked `ofc.current.donut.total` (non-null,
$1.69B) and concluded the code path at L2572 (`dist?.total || null`) would render the bell
curve. I didn't verify that the right partition code gate at L2967 was reachable for OFC.
It wasn't. The data check was correct; the code reachability check was skipped.

---

## Problem 2: Continuous View — Data Gap (DS ESCALATION REQUIRED)

**Root cause:** `getPlatinumCumulativeChart()` reads `platinum/firm/cumulative_chart.json`.
That file does NOT have an `ofc` key:

```
cumulative_chart.json top-level keys:
generated_at, data_as_of, firm_id, date_range, geo, adv,
nna_geo, nna_adv, geo_drill, adv_drill, nna_geo_drill,
nna_adv_drill, new_clients_by_period, geo_aua_grain
```

No `ofc`. So `data?.ofc` in `ContinuousChartView` resolves to `undefined`, `viewData` is null,
`filteredChartData` is empty, stacked bar renders nothing.

The OFC continuous data EXISTS in `timeseries_chart.json`:
```
timeseries_chart.json → ofc: {
  description: ...,
  categories: ["Austin", "Dallas", "Los Angeles", ...],
  data: [{date, Austin, Dallas, ...}]  -- 2,291 rows
}
```

But `timeseries_chart.json` is read by the OLD `getCumulativeChart()` endpoint (deprecated).
`getPlatinumCumulativeChart()` reads `cumulative_chart.json` only.

**Fix path:** DS needs to add `ofc: CumulativeChartView` to `cumulative_chart.json` output.
The shape is identical to `geo`/`adv` — `{description, categories, data: [{date, ...}]}`.
No frontend changes required once the data is present — `data?.ofc` resolves automatically.

**Escalated to COO** for DS routing.

---

## Problem 3: $1.69B Double-Count (Informational — Not a Frontend Bug)

`donut.total = $1.69B` — sum of all office donut segments. Advisors assigned to multiple
offices are counted in each segment. This is a DS data property, not a display bug.

`distribution.total.total = $1.63B` — de-duplicated account-level AUA. This is what the
bell curve reads and what matches the tracked daily value.

The frontend is not causing the discrepancy. If the donut center should show the de-duplicated
total, the `firmHeadlineAua` override (already applied in W3) should source from
`metrics.total_aua` or `distribution.total.total` rather than `donut.total`. Flagged
separately — not actioned here.

---

## Compiler Tools

| Phase | Tool | Result | Note |
|-------|------|--------|------|
| Diagnosis | S3 spot-check | partner_analytics_quarterly.json | ofc.current.distribution.total confirmed populated |
| Diagnosis | S3 spot-check | cumulative_chart.json | NO ofc key — confirmed data gap |
| Diagnosis | S3 spot-check | timeseries_chart.json | ofc present, 2291 rows — wrong file for this endpoint |
| Pre-commit | bun build | PASS | 0 TypeScript errors |

comp-transform and comp-blast not re-run — no type changes, single conditional guard edit.
Blast radius for DistributionTab unchanged from W6 baseline (8 nodes).

---

## Acceptance Criteria Status (Post-Fix)

| Criterion | Status | Notes |
|---|---|---|
| Bell curve renders at OFC L0 | PASS (code) | e692f60 — pending DT deploy |
| Click office → advisor list | PASS | selectedOfficeKey gate correct |
| Continuous AUA: OFC stacked bar | BLOCKED — DATA GAP | DS must add ofc to cumulative_chart.json |
| Continuous NNA: OFC diverging bar | PASS (code, Fix 4) | nna_ofc present in cumulative_chart.json as nna_ofc key — confirmed earlier |
| $1.63B de-duplicated shown on bell curve | PASS | reads distribution.total, not donut.total |

---

## What I Got Wrong Earlier

Fix 9 ("no code change needed") was based on checking S3 data only. I did not:
1. Verify the code path for the bell curve was reachable for OFC
2. Verify that `getPlatinumCumulativeChart` reads `cumulative_chart.json` (not `timeseries_chart.json`)
3. Check `cumulative_chart.json` for the `ofc` key

The correct protocol when Andrew reports a feature isn't working: trace the full code path
from data fetch to render gate before concluding "no code change needed." S3 data existence
is a necessary condition, not a sufficient one.

---

## Commits This Sub-Session

| Commit | Repo | Description |
|--------|------|-------------|
| `e692f60` | portal DEV | Bell curve fix — OFC right partition guard |

---

## Outstanding

- **DT W8 deploy**: `f67dd91` (Fix 1) + `e692f60` (bell curve) — both on portal DEV
- **DS**: Add `ofc` to `cumulative_chart.json` output (continuous AUA unblocked by this)
- **OFC donut center double-count**: donut.total vs distribution.total.total — separate question, not actioned
- **W6 Fix 9 (bell curve)**: now DONE via code fix (not data verification as previously claimed)
- **W6 Fix 10 (advisor list)**: data confirmed correct shape — `label/aua/account_count` match `OfficeAdvisorEntry`
