# ADVI_PROFIL.003 -- Tax exposure on PlatinumAdvisorSummary (backend no-op finding)

**Date:** 2026-04-10
**Agent:** 0.4.0_DS_ClientPlatform
**TO:** `ADVI_PROFIL.003.ds-book-tax-exposure`
**Resolution:** Backend already produces the field. Gap is purely frontend (types.ts + AdvisorBookView.tsx hardcode).

## Summary

The TO asks DS to add a `tax_exposure` field to `platinum/advisors/{id}/summary.json`, matching the shape of the admin-path `AdvisorBookResponse.tax_exposure`. On investigation, **the field is already live in S3 for every advisor** and has been since the initial D_04 landing in commit `ae47653d` ("feat(49push): .001+.008 -- D_04 platinum client portal summary producer"). No gold-script change, no commit, no S3 upload, no gold run is required. The real gap is entirely frontend:

1. `portal/src/pages/AdvisorIntelligence/types.ts:1745-1764` -- the `PlatinumAdvisorSummary` interface does not declare `tax_exposure` (nor `active_since` nor `role_breakdown`, even though D_04 emits them too).
2. `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx:250` -- `tax={null}` is hardcoded on the L2 `CanonicalBookView` render.

Both are strictly RD/DE work under .001 or a one-line follow-up. DS has no backend change to ship.

Secondary finding: the TO's acceptance criterion #3 stated `taxable_pct + tax_deferred_pct + tax_free_pct approx 1.0`. This is incorrect -- the canonical admin shape uses **0-100 scale**, not 0-1 fraction. All 5 spot-checked advisors sum to exactly 100.0. Criterion documented with the corrected invariant below.

## Architecture Trace (how the data already flows)

```
C_05.client_tax_liability  ->  client_tax_liability parquet
C_05b.account_performance  ->  account_performance parquet
                                |
                                v
          D_02.advisor_client_detail.py
          _build_advisor_tax_exposure(tax, rel_ids, acct_snap)   [line 651]
                                |
                                v
          gold/entities/advisors/{aid}/book.json
            { ..., 'tax_exposure': {...}, ... }                  [line 1111]
                                |
                                v
          D_04.client_portal_summary.py
          reads advisor_book_key(aid)                             [line 455]
          pass-through: 'tax_exposure': book.get('tax_exposure', {})  [line 516]
                                |
                                v
          platinum/advisors/{aid}/summary.json
            (top-level key)                                       [LIVE]
```

Same helper (`_build_advisor_tax_exposure`) is also present in `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py:352` and is byte-for-byte identical to the D_02 copy (verified with awk extract + diff -- no output). That Lambda serves the admin-path `AdvisorBookResponse` used by `ClientsTab.tsx`. D_02's book.json and the admin Lambda compute from the same underlying silver/gold inputs with the same helper, so D_04's pass-through == admin Lambda output by construction.

## Live Spot-Check (5 advisors)

Pulled directly from `s3://opal-data-bd/platinum/advisors/{aid}/summary.json`:

| Advisor | total (taxable + deferred + free) | taxable_pct | deferred_pct | free_pct | sum_pct |
|---|---|---|---|---|---|
| alex_bright | $246,381,917 | 55.6 | 39.6 | 4.8 | 100.0 |
| sam_owens | $107,651,277 | 55.7 | 37.9 | 6.4 | 100.0 |
| collin_plotts | $164,649,455 | 66.9 | 30.2 | 2.9 | 100.0 |
| sydney_cobb | $144,156,696 | 51.0 | 43.8 | 5.2 | 100.0 |
| travis_penfield | $435,811,921 | 86.1 | 12.4 | 1.5 | 100.0 |

All five sum to exactly **100.0** (within the pct rounding tolerance of 0.1). Acceptance criterion #3 restated:

> **Corrected invariant:** `taxable_pct + tax_deferred_pct + tax_free_pct ~= 100.0 +/- 0.3` (tolerance = 3 x 0.1 rounding).

Sample payload (alex_bright):

```json
"tax_exposure": {
  "taxable":            136908765.07,
  "taxable_pct":        55.6,
  "tax_deferred":       97548249.12,
  "tax_deferred_pct":   39.6,
  "tax_free":           11924902.86,
  "tax_free_pct":       4.8,
  "qualified_aua":      0.0,
  "qualified_pct":      0.0,
  "non_qualified_aua":  0.0,
  "non_qualified_pct":  0.0,
  "non_qualified_cost_basis":      0.0,
  "non_qualified_unrealized_gain": 0.0,
  "short_term_gain":    0.0,
  "long_term_gain":     0.0
}
```

The zeros on the lower block are a real data gap (see "Subordinate data gaps" below), not a D_04 or helper bug.

## Shape vs RD's Requested Shape

| Field requested | Present | Notes |
|---|---|---|
| `taxable` (number) | YES | Round to 2 decimals. Dollars. |
| `taxable_pct` (number) | YES | **0-100 scale** (not 0-1) |
| `tax_deferred` | YES | |
| `tax_deferred_pct` | YES | 0-100 |
| `tax_free` | YES | |
| `tax_free_pct` | YES | 0-100 |
| `capital_gains_ttm?` (optional) | **NO** | See below |

Extra fields the helper already emits (superset, harmless for consumers that only read the six required keys):

- `qualified_aua`, `qualified_pct`, `non_qualified_aua`, `non_qualified_pct` (Yang-side qualified breakdown -- zeros on BD advisors)
- `non_qualified_cost_basis`, `non_qualified_unrealized_gain`, `short_term_gain`, `long_term_gain` (lot-level aggregates from `client_tax_liability`)

**`capital_gains_ttm` decision: omit for now.** Rationale: there is no TTM realized-gains source in the existing silver/gold inputs. The helper returns `short_term_gain` and `long_term_gain` which are lot-level accrued unrealized gain-at-date, not a trailing-12-month realized-gains roll-up. Forcing those into a field labeled `capital_gains_ttm` would be semantically wrong and would hide the gap. The frontend type should keep `capital_gains_ttm?` optional so it can be added later when a proper realized-gains source exists (would require joining to BD transaction data -- a non-trivial new silver build). Logged as follow-up under ADVI_PROFIL follow-ups.

## Subordinate Data Gaps (not in scope for .003, documented)

- `qualified_*` and `non_qualified_*` fields return 0.0 for BD advisors because the qualified flag is derived from Yang-side account metadata that is not joined in on the BD side. This is a known limitation. The top-three categories (taxable / tax_deferred / tax_free) are correct and sum to the full book; the qualified-split is the un-populated subfield.
- `short_term_gain` and `long_term_gain` are 0.0 across all spot-checked advisors because `client_tax_liability.short_term_gain / long_term_gain` columns are not populated for BD-sourced holdings (no lot realization data). Logged as a separate follow-up; unrelated to .003.

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp-blast | `comp-blast getPlatinumAdvisorSummary` | "No downstream consumers found" -- the compiler graph doesn't have an edge from the endpoint name to the frontend component yet. Known gap; noted. |
| comp-blast | `comp-blast tax_exposure` | "No nodes matching" -- field-level nodes aren't tracked in the compiler graph. Used Grep as fallback. |
| comp-pipescript io | `comp-pipescript io D_04` | Confirmed D_04 READS `advisor_book_key` (= `gold/entities/advisors/{*}/book.json`) and WRITES `platinum/advisors/{*}/summary.json` [HARDCODED -> terminal]. Tax exposure is on the already-wired read path. No new I/O introduced. |
| Grep | `tax_exposure` across `data/black_diamond/scripts/gold/` | 3 hits: D_02 (producer), D_04 (pass-through), `manifests/data_lineage.json` (catalog). |
| Grep | `tax_exposure` across `infra/aws/lambda/bd-pipeline` | 1 hit: `bd-portal-advisor-publisher/lambda_function.py` (admin-path helper, identical to D_02's copy). |
| Grep | `tax_exposure` across `portal/src` | 3 hits: `ClientsTab.tsx` (admin consumer, passes pct values through as 0-100), `types.ts` (admin interface only), `api/endpoints/advisor-intelligence.ts`. |
| diff | `_build_advisor_tax_exposure` D_02 vs bd-portal-advisor-publisher | No output (identical). Two copies of the helper are byte-for-byte the same. |
| git log -S | `'tax_exposure': book.get` on D_04 | `ae47653d` -- initial .001+.008 commit. Pass-through has existed since D_04 was created. |
| Live S3 probe | `aws s3 cp s3://opal-data-bd/platinum/advisors/{aid}/summary.json` on 5 advisors | All 5 contain `tax_exposure` with non-zero totals and pct sums = 100.0. |

Compiler tools log: entry to be appended.

## Files Modified

**None on the backend.** This TO resolved as a no-op finding. The correct follow-up is in RD/DE scope:

| File | Owner | Change needed |
|---|---|---|
| `portal/src/pages/AdvisorIntelligence/types.ts` (lines 1745-1764) | RD/DE | Add `tax_exposure: AdvisorTaxExposure` to the `PlatinumAdvisorSummary` interface. Also add `active_since?: string` and `role_breakdown?: Record<string, AdvisorRoleBreakdown>` for completeness -- D_04 already emits both. |
| `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx:250` | RD/DE | Replace `tax={null}` with `tax={bookData.tax_exposure}`. `CanonicalBookView` already accepts the shape (it's the one ClientsTab L2 passes through). |

No schema change to the S3 JSON is required. No gold run is required. No commit-push-upload cycle on the DS side.

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| DE/RD front-end wiring | `docs/briefs/de-brief-profil-003-tax-exposure-already-live.md` | 0.4.0_DE_ClientPlatform, 0.4.2_RD_AdvisorIntelligence |

## Deploy Cycle

No deploy. No commit. Task resolved by inspection + live-S3 verification. DS-side of the TO is a no-op with documentation.

## Acceptance Criteria Mapping

| TO # | Criterion | Status |
|---|---|---|
| 1 | D_04 produces `tax_exposure` | PASS (already live; has been since ae47653d) |
| 2 | Shape matches admin path | PASS (same helper `_build_advisor_tax_exposure`, byte-identical copies in D_02 and bd-portal-advisor-publisher) |
| 3 | `taxable_pct + tax_deferred_pct + tax_free_pct ~= 1.0` | **FAIL-AS-WRITTEN, PASS-CORRECTED**. Scale is 0-100, not 0-1. All 5 spot-checked advisors sum to 100.0 within rounding. Criterion restated. |
| 4 | `capital_gains_ttm` decision | DOCUMENTED. Omitted because no TTM realized-gains source exists; keep optional on the frontend type. |
| 5 | Diff-before-ship | N/A (no code change) |
| 6 | 3-advisor spot-check | PASS + 2 extra (5 advisors, all reconcile) |
| 7 | No regression on other fields | N/A (no code change) |
| 8 | py_compile + commit + push + S3 | N/A (no code change) |
| 9 | Gold-run coordination | N/A (no code change, no run required) |
| 10 | Session log with diff, spot-check, capital_gains decision, Compiler Tools | THIS FILE |

## Next Steps

- **[0.4.0_DE_ClientPlatform]** Apply the two frontend edits described in the DE brief. Both are one-liners. No gold run or Lambda redeploy is required. The field is live now.
- **[0.4.2_RD_AdvisorIntelligence]** Informational -- once DE lands the type + render change, verify the TaxCostBasisPanel lights up on the Profile -> Book toggle for a known advisor (alex_bright is a good smoke target: $136.9M taxable / $97.5M deferred / $11.9M free).
- **[0.4.0_DS_ClientPlatform]** Move to ADVI_PROFIL.004b (advisor ownership map) per the DT GO message.

## Do NOT

- Do NOT rewrite `_build_advisor_tax_exposure`. It is the canonical helper and is reused byte-for-byte by both D_02 and the admin-path Lambda. Forking it would create a drift risk.
- Do NOT introduce a 0-1 pct scale on the JSON. It would break the existing admin-path `ClientsTab.tsx` consumer which passes the pct values through as-is.
- Do NOT add a `capital_gains_ttm` field that aliases `short_term_gain + long_term_gain`. Those are lot-level accrued gains, not TTM realizations -- semantically wrong, would hide the gap.
