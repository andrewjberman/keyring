# ADVI_MVPLVL.010 Session Log -- L2 Composition, Mix, Tax Diagnostic
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-26
**Task Order:** ADVI_MVPLVL.010.ds-l2-mix-tax-diagnostic.md

---

## WS1: L2 Advisor Composition (Books Tab)

### Diagnostic Findings

**Artifacts exist.** 20 advisor composition.json files confirmed on S3, all from the 2026-03-25 gold run:
```
gold/advisors/boston_prachyl/composition.json    (5,907 bytes)
gold/advisors/brandon_lanz/composition.json     (5,416 bytes)
gold/advisors/chase_bertrand/composition.json   (6,514 bytes)
gold/advisors/david_farrell/composition.json    (6,861 bytes)
gold/advisors/josh_henson/composition.json      (7,529 bytes)
... (20 total, including unresolved)
```

**JSON well-formed.** Sample (josh_henson):
- total_market_value: $144,167,098.04
- mix[]: 3 asset classes (equity, fixed_income, alternatives) with market_value > 0
- top_holdings[]: 9 items with valid keys, labels, pct values
- scope: `{"advisor_id": "josh_henson", "firm_id": "49financial"}`

**Sanitization aligned.** Python `_advisor_id()` (script 12, line 163) and TypeScript `handleSelectAdvisor` (ClientsTab.tsx:415) produce identical outputs:
- Python: `re.sub(r'[^a-z0-9_]+', '_', str(name).lower().strip()).strip('_')[:60]`
- TypeScript: `name.toLowerCase().trim().replace(/[^a-z0-9_]+/g, '_').replace(/^_+|_+$/g, '')`

**Lambda handler deployed.** `handle_advisor_composition` (lambda_function.py:1104) reads `gold/advisors/{advisor_id}/composition.json` via `serve_s3_json_nocache()`. Commit `885719e3` is an ancestor of `partners-api-v1.9.0` (confirmed via `git merge-base --is-ancestor`).

**Routing correct.** Lambda route at line 1275: `action == 'composition' and entity_type == 'advisor'` -> `handle_advisor_composition(bucket, entity_id)`.

### Root Cause Assessment

**Data layer is complete and correct.** All 20 advisor composition artifacts exist with matching S3 keys, well-formed JSON, and correct schema. The Lambda has the handler deployed.

The L2 composition "not rendering" issue is **portal-side or Lambda integration**. Possible causes:
1. Portal rendering logic for advisor-level composition fails silently (the `.catch()` at ClientsTab.tsx:391 falls back to `synthesizeFromAssetAllocation` which may produce a shape the renderer doesn't expect)
2. The `normalizeMixTo4Class()` transform might drop data when the composition uses `'other'` as an asset class key vs the expected portal keys

**Escalation to DE:** Investigate why `getBooksAdvisorComposition()` calls fail or why the fallback synthesis doesn't render. The data is present and correct.

---

## WS2: PartnerAnalytics Mix Toggle (firm_mix_views.json)

### Diagnostic Findings

**firm_mix_views.json is RICH -- NOT sparse.**
- views.quarterly: 24 periods (Q2'20 through Q1'26)
- views.monthly: 69 periods (Jun'20 through Mar'26)
- views.annually: 7 periods (2020 through 2026)
- data_as_of: "2026-03-23"
- All periods have non-zero total_aua and class breakdowns
- Latest: $1.638B total AUA (equity 78.2%, fixed_income 18.5%, alternatives 3.2%)

**firm_mix_views.json is correct for the firm-level Mix toggle.** The 03-24 full gold run populated full history. No sparseness issue at firm level.

### Per-Advisor Mix Files

**Dual key paths exist on S3:**
- Old (2026-03-20, ~977 bytes): `gold/advisors/Boston Prachyl/mix.json` (unsanitized, stale)
- New (2026-03-24, ~25KB): `gold/advisors/boston_prachyl/mix.json` (sanitized, full history)

The new sanitized paths contain full multi-period views (25KB vs 977 bytes confirms full history, not sparse).

### mix_timeseries.json Key Mismatch -- CONFIRMED

- **Script 06b writes:** `gold/advisors/{advisor_id}/mix.json`
- **Lambda reads:** `gold/advisors/{advisor_id}/mix_timeseries.json` (handle_advisor_mix_timeseries, line 1056)
- **No mix_timeseries.json files exist on S3.** `aws s3 ls --recursive | grep mix_timeseries.json` returns empty.

This is a confirmed S3 key mismatch for the advisor-level mix-timeseries route. The firm-level Mix toggle (`firm_mix_views.json`) is unaffected.

### Fix Applied

**Script 06b modified** (`_write_advisor_mix`, after line 305): after writing `mix.json`, also write `mix_timeseries.json` as an alias using the same payload. This avoids a Lambda/Terraform deploy.

```python
# Alias: Lambda handle_advisor_mix_timeseries reads mix_timeseries.json
alias_key = f'{ADV_MIX_PREFIX}/{advisor_id}/mix_timeseries.json'
_get_s3().put_object(Bucket=S3_BUCKET, Key=alias_key, Body=mix_body, ...)
```

**Next steps for AE:** A gold rerun of script 06b (or full gold layer) is needed to populate the `mix_timeseries.json` files on S3.

---

## WS3: Tax Liability vs AUA Divergence

### Diagnostic Findings

**Ghost account exclusion is the primary gap.** Script 06 (tax liability) has ZERO account exclusion logic. Script 05 (AUA) applies two layers:
1. **aua_overrides.json** (RC6): 4 ghost accounts with combined gold AUA of $7.4M
   - z0812933851: $2,260,087 (silver $0.04)
   - z0818413191: $2,089,843 (silver $6,430)
   - z0819915221: $1,871,933 (silver $922)
   - z0815983871: $1,177,506 (silver $0)

2. **Phantom exclusion** (script 02): Accounts with <$100 in silver allocations excluded from positions_cube entirely. This is upstream of script 05 -- positions_cube already lacks phantom accounts, so script 06 (which reads holdings_lots, not positions_cube) includes them.

**Gap (a) -- ghost accounts: ~$7.4M** in stale holdings_lots market_value that inflates tax liability but is absent from AUA. This is the known primary driver.

**Gap (b+c) -- base dataset + pricing:** Script 06 reads holdings_lots (FIFO lots with pre-computed market_value from lot-level pricing). Script 05 reads positions_cube (cumulative units priced via canonical_prices with forward-fill). Different pricing methodologies produce secondary divergence for all overlapping accounts.

**Gap (d) -- date semantics:** Script 06 uses a single holdings_lots snapshot. Script 05 uses a daily timeseries. Minor impact.

**Gap (e) -- backfill capping:** Script 02 caps forward-fill for backfill-only accounts. Script 03/06 does not. Contributes phantom positions in holdings_lots that don't exist in positions_cube.

### Fix Applied

**Script 06 modified** to load and apply ghost account exclusions from `aua_overrides.json`:

1. Added `load_ghost_account_ids()` function (same logic as script 05's `load_aua_overrides()`)
2. Added `ghost_accounts` parameter to `build_tax_liability_view()`
3. Ghost accounts filtered after open lots selection, before aggregation
4. Filter logs excluded lot count and market value for audit trail

**Before (estimated):** 4 ghost accounts contributing ~$7.4M to tax liability totals that don't appear in AUA.

**After:** Ghost accounts excluded. Remaining divergence is from gaps (b)-(e) which are structural methodology differences. Full alignment is GLDRST scope.

### Remaining Divergence (for GLDRST)

The gaps (b)-(e) are inherent to using holdings_lots vs positions_cube as base datasets. These are methodology choices, not bugs:
- Holdings_lots = FIFO lot grain, pre-computed MV from BD pricing
- Positions_cube = cumulative units, canonical_prices with forward-fill

Full canonical methodology alignment (choosing one authoritative pricing source, one account universe) is the GLDRST project's charter.

---

## Commits

Pending commit:
- `06b_build_client_mix_timeseries.py`: mix_timeseries.json alias write
- `06_build_client_tax_liability.py`: ghost account exclusion from aua_overrides.json

---

## Next Steps

| Owner | Action | Priority |
|-------|--------|----------|
| **DE (0.4.0_DE_ClientPlatform)** | Investigate L2 advisor composition rendering failure. Data artifacts exist and Lambda handler is deployed. Check portal-side normalizeMixTo4Class() and fallback rendering. | P1 |
| **AE (0.6.0_AE_PartnerETL)** | Gold rerun needed for script 06b to populate mix_timeseries.json aliases on S3. Can be incremental (06b only) or full. | P2 |
| **AE (0.6.0_AE_PartnerETL)** | Gold rerun needed for script 06 to apply ghost account exclusion. | P2 |
| **DS (GLDRST project)** | Use WS3 findings (gaps b-e) to design canonical methodology for tax-AUA alignment. | Future |
