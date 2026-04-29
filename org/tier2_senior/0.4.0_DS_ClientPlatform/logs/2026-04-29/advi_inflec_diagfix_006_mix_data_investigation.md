# DS — ADVI_INFLEC.DIAGFIX.006 (Asset Mix Data Investigation)

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-29
**Session shape:** Investigation only (no commit). Schema audit + coverage check + BD parity.
**Outcome:** **VERDICT A** — data exists, mix CAN be built using BD's existing ETFClassifier.

---

## Mandate Origin

GO from `2.0.0_SA_COO` (20260429T204936Z): asset class / mix data investigation. Determine if Orion silver includes data sufficient to power the Inflection mix panel. RAVC verdict (A/B/C) with evidence. No build until follow-on TO.

---

## Step 1 — Column Audit

| S3 Path | Columns relevant to mix | Notes |
|---------|------------------------|-------|
| `silver/accounts_dim/latest.parquet` | `investment_model` | **100% NULL** — useless |
| `silver/api_dims/accounts_v2/snapshot_date=2026-04-28/data.parquet` | `management_style`, `model_name`, `fund_family`, `share_class`, `is_managed`, `is_sleeve_account` | model_name 77.5% populated, 21 distinct |
| `silver/api_dims/assets/snapshot_date=2026-04-20/data.parquet` | `account_id, asset_id, asset_ticker, asset_name, position_mv` | **No asset_class field** |
| `gold/canonical/holdings_2026-04-28.parquet` | `ticker, product_name, market_value` | ticker + product_name 100% populated |
| `gold/holdings/2026-04-28.parquet` | `ticker, market_value` (no product_name) | INF_B_01 output |

Fields searched for and **NOT found anywhere**: `asset_class`, `asset_type`, `security_type`, `category`, `broad_category`, `style_box`, `strategy`, `sleeve`, `allocation_type`.

Fields searched for and **found**: `model_name` (in api_dims/accounts_v2), `product_name` (in gold/canonical/holdings).

---

## Step 2 — Coverage Check

### `model_name` (silver/api_dims/accounts_v2)

| Metric | Value |
|--------|-------|
| Total accounts | 850 |
| `model_name` populated | 77.5% (659/850) |
| AUA covered (joined to holdings) | $79.7M / $89.6M = **89.0%** |
| Distinct models | 21 (all "IWM" or "Opal" prefixed) |

Risk-bucket aggregation derived from model_name parsing:

| Bucket | AUA | % |
|--------|-----|---|
| Moderate | $42.45M | 47.4% |
| Moderately Aggressive | $20.58M | 23.0% |
| No Model | $9.88M | 11.0% |
| Aggressive | $7.58M | 8.5% |
| Moderately Conservative | $4.08M | 4.6% |
| Conservative | $2.20M | 2.5% |
| Other (Opal models) | $2.81M | 3.1% |

Tax-style derived:

| Style | AUA | % |
|-------|-----|---|
| Tax-Deferred | $52.88M | 59.0% |
| Taxable | $16.50M | 18.4% |
| No Model | $9.88M | 11.0% |
| Index | $7.52M | 8.4% |
| Other | $2.81M | 3.1% |

### `ticker + product_name` (gold/canonical/holdings)

| Metric | Value |
|--------|-------|
| Total holding rows | 9,295 |
| Total AUA | $89.6M |
| `ticker` populated | 100% |
| `product_name` populated | 100% |
| Distinct funds | 276 |

Top funds: John Hancock Intl Dynamic Growth, Causeway Intl Value, Fidelity Government Cash Reserves, DWS RREEF Real Assets, Baird Aggregate Bond, GQG Partners EM Equity, Vanguard S&P 500, etc. — Mix of equity/fixed_income/alternatives/cash funds.

---

## Step 3 — BD Parity Check

BD's `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` derives asset class mix as follows:

1. **NO raw `asset_class` field in BD silver either.** BD positions_cube has ticker + asset_name only.
2. BD uses `lib.etf_classifier.ETFClassifier` (DynamoDB `bd-securities` table → regex fallback) to classify each (ticker, asset_name) pair into one of 5 buckets: `equity, fixed_income, alternatives, cash, other`.
3. Mix structure: `{date, equity, fixed_income, alternatives, cash, other}` per relationship_id, where each value is a fraction summing to 1.0.

**The BD pattern works for Inflection.** Same `ETFClassifier` applied to Inflection's `(ticker, product_name)` from `gold/canonical/holdings_2026-04-28.parquet` produced:

| Asset Class | AUA | % of Inflection total |
|-------------|-----|---|
| Equity | $50.05M | 55.9% |
| Fixed Income | $28.81M | 32.2% |
| Alternatives | $8.73M | 9.7% |
| Cash | $2.01M | 2.2% |
| Other | $0.00M | 0.0% |

Sample classification:
- Equity: GSLC (Goldman Sachs Activebeta), AMZN, VOO (Vanguard S&P 500)
- Fixed Income: FDRXX (Fidelity Govt Cash Reserves — note: BD classifier puts MM funds in fixed_income), Baird Aggregate Bond
- Alternatives: AAAZX (DWS RREEF Real Assets)
- Cash: FCASH, FZDXX (Fidelity Mmkt Premium)

**Coverage:** 100% of Inflection AUA classifies (no `other` bucket). Classifier handles all 276 fund types in Inflection's holdings.

**One known edge case:** FDRXX (Fidelity Government Cash Reserves) gets classified as fixed_income by BD's `bd-securities` DynamoDB lookup — would normally be cash. Same edge case BD has. Acceptable for V1; can override later.

---

## VERDICT A — Data exists, build is feasible

Asset class mix CAN be built for Inflection by re-using BD's `ETFClassifier` on `ticker + product_name` from `gold/canonical/holdings_*.parquet`.

**Coverage:** 100% of $89.6M Inflection AUA classifies into the 5 standard buckets.

**Additional dimension available:** `model_name` from `silver/api_dims/accounts_v2` provides 89% AUA coverage of Inflection-defined risk-bucket / tax-style allocations — different cohort dimension from asset class, but valuable for the portal.

**Proposed follow-on TO scope (for COO to issue):**
1. New script `INF_C_06.client_mix_timeseries.py` (or extend existing INF_C_06 which currently only does AUA timeseries) — joins `gold/canonical/holdings_*.parquet` with the BD `ETFClassifier`, aggregates to per-date asset_class mix at firm + advisor + household grain.
2. New script (or extend INF_D_04) to write `platinum/firm/mix_summary.json` with `{equity, fixed_income, alternatives, cash, other}` shares + `views.aua.distribution.by_segment` keyed by asset_class.
3. Populate `timeseries_overview.mix.{quarterly, monthly, annually}` rows in INF_D_04's `build_timeseries_overview` (currently writes empty arrays).
4. Optional: add a 2nd mix dimension for `model_name` risk-bucket (Conservative/Moderate/Aggressive) — Inflection-specific, complements the standard asset class mix.

**Not blocked:** `lib.etf_classifier.ETFClassifier` is in `data/black_diamond/scripts/gold/lib/`. Inflection scripts can import it directly (same Python env on EC2). DynamoDB `bd-securities` table is shared (BD pipeline already authenticated for it; would need to confirm IAM scope for inf-gold-runner — escalate to AE if needed).

---

## Compiler Tools

| Phase | Tool | Result | Notes |
|-------|------|--------|-------|
| 1 — before investigation | `comp-pipescript io INF_C_06` | SKIPPED — registry gap | INF_C_06 exists but is not registered in BD-pipeline graph (same as INFGRD.006/DIAGFIX.002-004 finding) |
| 2 — N/A — investigation only | (no writes, no commit) | — | TO explicitly states no commit needed |

Note: existing `INF_C_06.client_mix_timeseries.py` is misleadingly named — it produces an AUA timeseries (firm + advisor totals over time), NOT an asset-class mix. The proposed follow-on TO would either rename it or layer mix on top.

---

## Files Modified

None (investigation only, no commit per TO directive).

---

## Next Steps

- [DS] RAVC VERDICT A to 2.0.0_SA_COO with evidence summary
- [COO → DS] Issue follow-on TO for mix_summary.json + timeseries.mix build (I'd recommend a single ADVI_INFLEC.MIXBLD.001 or similar)
- [COO → AE 0.6.1] If follow-on TO proceeds: confirm inf-gold-runner has DynamoDB read access to `bd-securities` table (or migrate classifier to a shared securities table)

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~25 min. 0 commits, 0 S3 uploads, 1 RAVC pending.*
