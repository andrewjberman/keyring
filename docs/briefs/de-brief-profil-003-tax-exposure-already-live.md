# DE Brief -- ADVI_PROFIL.003 tax_exposure is already live (frontend-only follow-up)

**To:** 0.4.0_DE_ClientPlatform, 0.4.2_RD_AdvisorIntelligence
**From:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**TO:** ADVI_PROFIL.003 (DS side resolved as no-op)

## TL;DR

`tax_exposure` is already being written into `platinum/advisors/{id}/summary.json` at the top level by D_04 and has been since the initial D_04 commit `ae47653d`. No backend change, no gold run, no Lambda redeploy is required. Two small frontend edits unblock the tax panel on `AdvisorBookView`.

## Proof -- live in S3 for every advisor

```
$ aws s3 cp s3://opal-data-bd/platinum/advisors/alex_bright/summary.json -
{
  ...,
  "tax_exposure": {
    "taxable":          136908765.07,
    "taxable_pct":      55.6,
    "tax_deferred":     97548249.12,
    "tax_deferred_pct": 39.6,
    "tax_free":         11924902.86,
    "tax_free_pct":     4.8,
    "qualified_aua":    0.0,
    "qualified_pct":    0.0,
    "non_qualified_aua": 0.0,
    "non_qualified_pct": 0.0,
    "non_qualified_cost_basis":     0.0,
    "non_qualified_unrealized_gain": 0.0,
    "short_term_gain":  0.0,
    "long_term_gain":   0.0
  },
  ...
}
```

Spot-checked 5 advisors: alex_bright, sam_owens, collin_plotts, sydney_cobb, travis_penfield. All five have non-zero totals and all five sum to exactly 100.0 on (taxable_pct + tax_deferred_pct + tax_free_pct).

**Important: the pct fields are 0-100 scale**, not 0-1 fraction. This matches the existing admin-path `ClientsTab.tsx` (line 440-442) which passes the values through as `taxablePct: tax_exposure.taxable_pct`. Do not divide by 100.

## Frontend edits

### 1. `portal/src/pages/AdvisorIntelligence/types.ts` (line 1745)

The `PlatinumAdvisorSummary` interface is missing three fields that D_04 actually emits. Minimum change for .003:

```typescript
export interface PlatinumAdvisorSummary {
  generated_at: string
  data_as_of: string
  advisor_id: string
  book: {
    book_name: string
    client_count: number
    account_count: number
    total_aua: number
    nna_qtd: number
    nna_ytd: number
    nna_mtd: number
    growth: AdvisorGrowth
    clients: AdvisorClient[]
  }
  mix: PlatinumMixSnapshot
  mix_periods: FirmMixPeriodPoint[]
  concentration: PlatinumConcentrationData
  fee_summary: FeeSummaryByRole | null

  // ADD THESE -- D_04 already emits all three
  tax_exposure: AdvisorTaxExposure         // reuses the existing admin-path type
  active_since?: string                    // ISO date, .040
  role_breakdown?: Record<string, AdvisorRoleBreakdown>  // .040 drilldown
}
```

`AdvisorTaxExposure` is already defined at line ~1000 and is the same shape the D_02 helper produces. Reuse it -- do not fork.

`AdvisorRoleBreakdown` may need to be declared if it doesn't exist yet. Shape (from D_02 line 1068 and D_00c equal-split logic):
```typescript
export interface AdvisorRoleBreakdown {
  aua: number
  nna: number
  inflows: number
  outflows: number
  client_count: number
  account_count: number
  pct_of_tagged: number
  fee_paying?: { aua: number; nna: number; ... }
  no_fee?:     { aua: number; nna: number; ... }
}
```

If the exact shape is unclear, defer `role_breakdown` to a follow-up and only land `tax_exposure` + `active_since` in this change.

### 2. `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx` (line 250)

Replace:

```tsx
tax={null}
```

with:

```tsx
tax={bookData.tax_exposure}
```

`CanonicalBookView` already accepts the `AdvisorTaxExposure` shape -- it's the same panel that `ClientsTab.tsx` drives in admin mode. Nothing else needs to change in that render.

## Optional: `capital_gains_ttm`

The original RD shape spec listed `capital_gains_ttm?: number` as optional. **DS recommendation: leave this optional on the frontend type and do not populate it.** Rationale:

- There is no trailing-12-month realized-gains source in the existing silver/gold inputs.
- The helper's `short_term_gain` + `long_term_gain` are lot-level accrued unrealized gain-at-date, not TTM realizations. Aliasing them would be semantically wrong and would hide the gap.
- Populating properly requires a new silver build joining BD transaction data to holdings -- a non-trivial follow-up.

Keep the field on the TypeScript interface as `capital_gains_ttm?: number` so a future DS pass can add it without a breaking type change.

## Verification (RD, after DE lands the change)

1. `bun run dev` in `portal/`, open the AdvisorIntelligence page, switch to Profile -> Book for any advisor.
2. The TaxCostBasisPanel should now render.
3. Smoke target: alex_bright -> expect $136.9M taxable (55.6%), $97.5M deferred (39.6%), $11.9M free (4.8%), totals ~$246M.

## What DS did and did not do

**Did:**
- Traced the data path: `client_tax_liability` -> D_02 helper -> `book.json` -> D_04 pass-through -> `platinum/advisors/{id}/summary.json`.
- Verified the helper is identical between D_02 and the admin-path Lambda (`bd-portal-advisor-publisher`).
- Verified 5 advisors in live S3 all carry the field with correct totals and pct sums.
- Documented the pct-scale mismatch in the TO (criterion #3 said ~1.0, actual is ~100.0).
- Logged the `capital_gains_ttm` decision with rationale.

**Did not:**
- Touch any backend code -- no change was needed.
- Touch any frontend code -- that is DE/RD scope.
- Trigger the gold runner -- no code change to deploy.

## Follow-up tickets (not scoped to .003)

- Populate `qualified_aua` / `qualified_pct` for BD advisors -- currently 0.0 because qualified flag is Yang-side only.
- Populate `short_term_gain` / `long_term_gain` from BD transaction data -- currently 0.0 because lot realization data is not joined in.
- Add a proper `capital_gains_ttm` once a TTM realized-gains source exists.
