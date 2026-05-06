# Session Log — ADVI_INFLEC B3: L3 Client Detail Render Investigation

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-06
**GO source:** COO 20260506T~1900Z
**Session type:** Phase 0 investigation — root cause diagnosis

---

## Scope

INFLEC audit YELLOW #3: L3 client detail BooksTab — cost basis/tax/fee summary render correctly,
but asset mix donut, time machine performance snapshot, and top holdings are missing.

COO questions:
1. What S3 key / Lambda does L3 fetch?
2. comp-transform schema-check for L3 component
3. Is composition.json fetched at L3? Or per-client artifact at platinum/clients/{hh_id}/?
4. Does static-path adapter resolve correctly, or fall through to BD-shape crash?

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-routes trace | `comp-routes trace getPlatinumClientDetailStatic` | URL: `/api/scoped/advisor-intelligence/platinum/clients/{param}/detail.json`; S3 key: `platinum/clients/{param}/detail.json`; Router: shared-advisor-router (swaps bucket for inflection→opal-data-inf) |
| comp-transform schema-check | `comp-transform schema-check ClientDetailPage` | `BooksClientDetailResponse` type not found in types.ts (x2 functions). No MISSING rendered fields. NOTE: separate debt item; non-blocking for this investigation. |

---

## Investigation Trace

### Step 1 — Identify L3 component

Two distinct "L3" contexts exist:
- **Inline L3** (within BooksTab): `AdvisorBookClientDetail.tsx` — pure renderer, props fed by `AdvisorBookView.tsx`
- **Full-page L3**: `ClientDetailPage.tsx` — separate navigation target

The INFLEC audit "L3" = the **inline L3** within AdvisorBookView / ClientsTab. Cost basis/tax/fee summary rendering confirms this — these come from `getPlatinumClientDetailStatic` which is wired in `AdvisorBookView.tsx:123-125`.

### Step 2 — How composition/quarterlyMix/decomposition are derived

`AdvisorBookView.tsx` derives the three missing-panel inputs as:

```tsx
// l3Composition (asset mix donut + concentration / top holdings)
const l3Composition = useMemo(() => {
  if (!clientSummary) return null
  return normalizeMixTo4Class(
    platinumToComposition(clientSummary.mix, clientSummary.concentration, clientSummary.data_as_of),
  )
}, [clientSummary])   // AdvisorBookView.tsx:244-249

// l3QuarterlyMix (time machine performance snapshot)
const l3QuarterlyMix = clientSummary?.mix_periods ?? null   // AdvisorBookView.tsx:251

// l3Decomposition
const l3Decomposition = useMemo(() => {
  const d90 = clientSummary?.decomposition_90d
  if (!d90) return null
  if (!d90.market_growth && !d90.nna && !d90.synthetic_correction) return null
  return d90
}, [clientSummary])   // AdvisorBookView.tsx:253-258
```

### Step 3 — What getPlatinumClientDetailStatic returns for these fields

From `advisor-intelligence.ts:839-854` docstring:
> "Mix / concentration / decomposition fields are left empty (null / []) — those panels
> gracefully empty-state when missing."

Adapter sets: `mix = null`, `concentration = []`, `mix_periods = null`, `decomposition_90d = null`

Therefore:
- `l3Composition = normalizeMixTo4Class(platinumToComposition(null, [], ...))` → null → asset mix empty state
- `l3QuarterlyMix = null` → time machine empty state
- `l3Decomposition = null` → decomposition panel not rendered

### Step 4 — S3 artifact audit

```
aws s3 ls s3://opal-data-inf/platinum/clients/100/
  → 2026-04-27  detail.json (469 bytes)  ONLY

aws s3 ls s3://opal-data-inf/platinum/clients/1000/
  → 2026-04-27  detail.json (575 bytes)  ONLY

aws s3 ls s3://opal-data-inf/platinum/clients/1001/
  → 2026-04-27  detail.json (758 bytes)  ONLY
```

ABSENT for all households:
- `composition.json`
- `mix_timeseries.json`
- `concentration.json`
- `top_holdings.json`

### Step 5 — FE wiring correctness

AdvisorBookView Inflection branch (lines 120-125):
```tsx
const isInflectionFirm = firmOverride === 'inf' || firmOverride === 'inflection'
queryFn: () => isInflectionFirm
  ? getPlatinumClientDetailStatic(selectedClientKey!, firmOverride)  // static adapter
  : getPlatinumClientSummary(selectedClientKey!, firmOverride),      // Lambda (49F)
```

FE wiring is **complete and correct**. The static adapter is called for Inflection.
The panels gracefully empty-state when mix/composition/mix_periods are null.
No crash, no error boundary — audit YELLOW classification is accurate.

---

## Root Cause

**DATA PUBLISHER GAPS — DS B2a-c scope.**

The FE correctly calls the static adapter, which correctly reads `detail.json`.
`detail.json` provides: tax ✓, billing/fee_summary ✓, accounts ✓.
`detail.json` does NOT provide: mix, concentration, mix_periods, decomposition.

Those fields require separate per-client artifacts that DS B2a-c must publish:
- `platinum/clients/{hh_id}/composition.json` (or extend detail.json to include mix+concentration+mix_periods)
- Alternatively, FE could scope advisor-level `top_holdings.json` to household (possible FE optimization, not needed for correctness)

---

## Disposition

| Missing panel | Data source needed | Publisher | Availability |
|---|---|---|---|
| Asset mix donut | `clientSummary.mix` + `clientSummary.concentration` | DS B2a | ABSENT |
| Time machine performance | `clientSummary.mix_periods` | DS B2b | ABSENT |
| Top holdings | `clientSummary.concentration` (top-N) | DS B2c | ABSENT |

**FE action: NONE.** Wiring is complete. Panels empty-state correctly.
**DS action: Author composition publisher for platinum/clients/{hh_id}/**.

Secondary note: `BooksClientDetailResponse` type not found in types.ts
(affects `ClientDetailPage.tsx` — the full-page L3, not the inline L3).
Separate debt item; non-blocking.

---

## Files Modified

None — investigation only.

---

## RAVC Log

| # | To | Subject | Status |
|---|----|---------|--------|
| RAVC1 | 2.0.0_SA_COO | B3 GO ACK | Sent 20260506T191331Z |
| RAVC2 | 2.0.0_SA_COO | B3 root cause: DATA PUBLISHER GAP — DS B2a-c scope | Sent 20260506T191749Z |

---

## Current State

| Item | Status |
|------|--------|
| B3 investigation | COMPLETE — BLOCKED on DS B2a-c publishers |
| Portal code change | NONE — no FE fix possible or needed |
| DE queue | Empty — standing by |
