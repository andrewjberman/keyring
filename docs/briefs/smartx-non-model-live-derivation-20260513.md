# SmartX Non-Model AUM — Live Derivation + Historical Backfill Brief

**Author:** 0.4.0_DS_ClientPlatform (base)
**Date:** 2026-05-13
**Audience:** 2.0.0_SA_COO (for decomposition)
**Scope:** Replace the stuck "$272M plug" non-model figure on the ModelPortfolios page with a daily-fresh, historically-backfilled non-model AUM series sourced from Black Diamond's 49Financial enterprise data.

---

## TL;DR

The Non-Model bar on `/model-portfolios` has been frozen at $271,228,563.96 since 2026-01-05 because the upstream 49F enterprise AUM CSV stopped updating on 12/26/2025. A live source already exists: the **BD pipeline is 49Financial-exclusive** (`FIRM_ID = '49financial'` hardcoded), publishes a daily `certified_aua` JSON in `s3://opal-data-bd/gold/aua_certification/{date}.json`, and additionally has a daily 49F book snapshot in `s3://opal-data-bd/silver/allocations/{date}.parquet` covering 2026-01-16 → present (79 partitions today).

**The surgical fix:** rewrite the existing `non_model_assets.json` on S3 with five chained data segments stitched together — preserving the existing portal contract, requiring zero frontend code change. CloudFront serves the new file on next cache pop, the existing roll-forward logic handles any gaps, and the Non-Model bar starts moving daily with the rest of the chart.

**Going forward:** wire a small daily extension step into the SmartX ingestion Lambda chain (Step 6) that appends today's row to the file using the live BD certified_aua + SmartX model AUM.

---

## Current state (verified 2026-05-13 17:55Z)

**The dead pipe:**
- File: `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json`
- Last modified: 2026-01-13 (4 months stale)
- 431 daily rows, range 2024-11-01 → 2026-01-05
- `latest`:
  ```json
  {
    "date": "2026-01-05",
    "enterprise_total": 1380141678.94,    // 49F CSV 12/26/2025 value, ffill'd to 1/5
    "model_aum":        1108913114.98,
    "non_model_aum":     271228563.96,    // ← the "$272M plug"
    "non_model_pct":     19.65
  }
  ```

**The source script** (`data/smartx/scripts/compute_non_model_assets.py`) reads `s3://opal-data-smartx-v2/raw/enterprise_aum/49_financial_group_daily_aum.csv` which itself stops at 12/26/2025. Script is NOT in the daily Lambda chain — manual-only. Hasn't been run since 2026-01-13.

**The portal wiring is correct:**
- Frontend (`portal/src/pages/ModelPortfolios.tsx:430-436`) renders Non-Model as a third bar in the stacked AUM chart.
- `getNonModelAumForDate()` (lines 91-109) does roll-forward lookup — naturally absorbs day-level gaps.
- API path: `/api/general/portfolios/non_model_assets.json` served via `opal-portal-data-proxy` Lambda + CloudFront edge cache.

**Why surgery on the file works:** the contract is already shaped exactly for what we need — `latest{} + time_series[]` with the right fields. Replacing the file's body is invisible to the portal.

---

## Available data sources (verified)

### 1. BD `aua_certification/{date}.json` — primary live source

- Path: `s3://opal-data-bd/gold/aua_certification/{YYYY-MM-DD}.json`
- Date range: **2026-03-11 → 2026-05-11** (37 daily files; 2026-05-11 written 2026-05-13 00:36Z)
- Schema (verified):
  ```json
  {
    "date": "2026-05-11",
    "certified_aua": 1804326383.80,
    "gold_aua":      1767637047.06,
    "gap_abs":         36689336.74,
    "gap_pct":             0.020756,
    "liability_types_excluded": {
      "CreditCard": { "count": 22, "mv":   -83678.21 },
      "Mortgage":   { "count":  5, "mv": -2441513.54 },
      "Loans":      { "count":  4, "mv": -2242689.33 }
    }
  }
  ```
- **`certified_aua` is the BD-blessed daily 49F enterprise total.** Excludes liabilities cleanly. Use for 2026-03-11 onward.

### 2. BD `silver/allocations/{date}.parquet` — historical backfill fallback

- Path: `s3://opal-data-bd/silver/allocations/{YYYY-MM-DD}.parquet`
- Date range: **2026-01-16 → 2026-05-11** (79 daily files)
- Per-account: `account_market_value` column = market value at end-of-day per account
- **Daily 49F total** = `df['account_market_value'].sum()`
- Empirical validation on overlap date 2026-05-11:
  - `silver/allocations` sum = **$1,799,558,502.72**
  - `aua_certification.certified_aua` = $1,804,326,383.80
  - Δ = -$4.77M (-0.26%) — matches the certification's `liability_types_excluded` total ($84K + $2.44M + $2.24M = $4.77M) **exactly**.
- **Silver naturally excludes liabilities.** Methodology consistent with certification for the 2026-01-16 → 2026-03-10 fallback window. Will produce a ~$5M step at 2026-03-10→3-11 when we transition from silver-sum to certified-aua (silver is ~0.3% lower).

### 3. SmartX `aum-timeseries.json` — model AUM per day

- Path: `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json`
- Date range: 2024-11-01 → today (398 periods, fresh daily)
- `by_model` carries per-model daily series; `aggregate[]` carries the total model AUM
- Per-date model_aum = `aggregate[i].aum` (already-summed across UST/ST/INT/LTC/LTA)
- Already live; this is what's already on the chart.

### 4. Legacy 49F enterprise CSV — preserved historical

- Path: `s3://opal-data-smartx-v2/raw/enterprise_aum/49_financial_group_daily_aum.csv`
- Date range: 2020-06-29 → **2025-12-26** (frozen)
- Already reflected in existing `non_model_assets.json` rows for 2024-11-01 → 2026-01-05

---

## Proposed solution — five-segment time series

The output `non_model_assets.json` is rebuilt as the concatenation of five segments:

| Segment | Date range | Source(s) | `enterprise_total` derivation | `non_model_aum` derivation |
|---|---|---|---|---|
| **A** | 2024-11-01 → 2026-01-05 | Existing file (preserve) | Existing `enterprise_total` per row | Existing `non_model_aum` per row |
| **B** | 2026-01-06 → 2026-01-15 | **HOLD** | Hold last value of segment A flat ($1,380,141,678.94) | Hold $271,228,563.96 flat — Andrew-confirmed acceptable plug for this 10-day gap (CSV stops 12/26/2025, silver starts 1/16/2026) |
| **C** | 2026-01-16 → 2026-03-10 | `silver/allocations/{date}.parquet` | `df['account_market_value'].sum()` per date | `enterprise_total − model_aum` per date |
| **D** | 2026-03-11 → 2026-05-11 | `aua_certification/{date}.json` | `certified_aua` per date | `enterprise_total − model_aum` per date |
| **E** | 2026-05-12 → forward | Daily Lambda chain step (new) | `certified_aua` from latest BD daily | `enterprise_total − model_aum` |

**Per-date model_aum lookup** (uniform across C/D/E): read `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json`, find `aggregate[].period == {date}`, take `aggregate[].aum`. SmartX is fresh daily and covers the entire 2024-11-01 → today range, so this lookup never misses.

**Computed fields per row:**
```python
{
  "period":           "YYYY-MM-DD",
  "enterprise_total":  float,    # per segment rule
  "model_aum":         float,    # from aum-timeseries.json aggregate
  "non_model_aum":     enterprise_total - model_aum,
  "non_model_pct":     100.0 * non_model_aum / enterprise_total
}
```

**Forward-fill behavior:** existing file holds weekends flat (e.g., 2024-11-01 Fri value repeated on 2024-11-02/03 weekend rows). Preserve this pattern via business-day-aware ffill across segments C and D — same logic as SmartX's existing `forward_fill_missing_dates.py`.

---

## Validation plan (before publishing)

| Check | Method | Pass threshold |
|---|---|---|
| Segment C↔D continuity | Compare 2026-03-10 silver-sum to 2026-03-11 certified | Expected ~$5M step; flag if >$15M |
| Segment B↔C continuity | Compare 2026-01-15 hold value ($1.380B) to 2026-01-16 silver-sum | Expected step is genuine — silver is the BD-side measurement, plug was a frozen 12/26 CSV value. Should NOT smooth this; flag magnitude in commit message |
| Identity per row | `enterprise_total − model_aum − non_model_aum == 0` ± rounding | Strict |
| Monotonic-ish enterprise | No day-over-day jump in enterprise_total >$50M (no real-world market move that fast on 49F's mix) | If exceeded, suspect partition data issue; investigate before publishing |
| Certification overlap | For 37 dates in segment D, cross-check `silver/allocations` sum vs `certified_aua` (informational only — already showed 0.26% delta is the liability-exclusion) | Document gap range; should be tight |
| File schema | `non_model_assets.json` `time_series[]` row schema unchanged from existing portal contract | Bytes-level diff on type stubs (`NonModelAssetsTimeSeriesPoint` in `portal-proxy.ts:359-365`) |

**Visual smoke:** before publishing to production path, write to a side-by-side preview key (`json/portfolios/non_model_assets_preview.json`), pull it into a local dev port-5175 portal, verify the stacked chart renders smoothly with no discontinuity except at the genuine 2026-01-15→16 transition.

---

## Going-forward daily extension

After backfill ships, add a new step to the SmartX ingestion Lambda chain (`infra/aws/lambda/smartx_ingestion_pipeline/lambda_function.py`):

```
Step 6 (NEW): Append Non-Model row
  - Read latest aua_certification/{date}.json from opal-data-bd
  - Read aum-timeseries.json from opal-data-portal-v2
  - Compute today's non_model row
  - Append-only: read non_model_assets.json, append the new row, write back
  - Update latest{} block
```

Alternative if AE prefers: a new dedicated Lambda triggered by the SmartX ingestion Lambda's completion (decoupled). Either works. The IAM additions are identical.

**Required IAM additions** for whichever Lambda owns Step 6:
- `s3:GetObject` on `arn:aws:s3:::opal-data-bd/gold/aua_certification/*`
- `s3:GetObject` on `arn:aws:s3:::opal-data-bd/silver/allocations/*` (for catch-up if certified is missing)
- `s3:GetObject` + `s3:PutObject` on `arn:aws:s3:::opal-data-portal-v2/json/portfolios/non_model_assets.json`

Currently `smartx-ingestion-lambda-role` only has policy on `opal-data-smartx-v2` and `opal-data-portal-v2`. Cross-bucket read into `opal-data-bd` is new.

---

## Decomposition — proposed assignments

| Lane | Owner | Scope | Effort |
|---|---|---|---|
| **TO-1: Backfill script + one-shot run** | **DS** (base 0.4.0_DS_ClientPlatform) | Write `data/smartx/scripts/backfill_non_model_assets.py` implementing the 5-segment logic. One-shot run to produce the rebuilt JSON. Validation checks pass (table above). Upload to S3 preview path first; after DE smoke-test, promote to production path. | ~3-4 hours |
| **TO-2: Daily Lambda chain extension** | **DS** | Add Step 6 to `infra/aws/lambda/smartx_ingestion_pipeline/lambda_function.py` + supporting module `append_non_model_today.py`. Same append-only invariant as Steps 2/3. | ~2 hours |
| **TO-3: IAM + Lambda deploy** | **AE** (0.6.0_AE_PartnerETL or generalist) | Update `smartx-ingestion-lambda-role` IAM with cross-bucket reads to `opal-data-bd`. `build-and-upload.sh` for the Lambda zip. `terraform apply` on smartx-pipeline + smartx-v{X.Y.Z} tag. | ~1 hour |
| **TO-4: Portal smoke test** | **DE** (0.4.0_DE_ClientPlatform) | After preview JSON is uploaded to `non_model_assets_preview.json`, render `/model-portfolios` against it (local override or temporary route hack); verify stacked chart looks correct with no false discontinuities; verify the 2026-01-15→16 transition is the only visible step. No code change expected. | ~30 min |
| **TO-5: Decommission `compute_non_model_assets.py`** | **DS** | Move legacy script to `data/smartx/scripts/_deprecated/` or delete. Document the replacement in `CANONICAL_DATA_LOGIC.md` and `SMARTX_BIBLE.md`. | ~30 min |

**Total effort:** ~7-8 hours serialized, parallelizable across DS / AE / DE.

**Suggested sequence:** TO-1 → TO-4 (smoke) → TO-2 + TO-3 in parallel → TO-5 (cleanup).

---

## Risks / open questions

1. **The 2026-01-15→16 transition step** is real — silver-allocations-based methodology vs. CSV-based plug. Won't be smooth. Need to decide if this is acceptable (Andrew's framing implies yes) or whether to apply a one-time level-shift adjustment to segment A to align with segment C at the boundary. **Recommend: accept the step. It's the true value moving into a real measurement; smoothing it away would mask methodology change.**

2. **Segment C/D internal step at 2026-03-10/11** of ~$5M from silver-sum (excludes via summation absence) vs. certified-aua (excludes via certification subtraction). Predictable, small, documented in commit message. **Recommend: accept; surface in validation log.**

3. **Cache pop timing.** CloudFront edge cache TTL on the file is `?` — need to confirm from CF behaviors. May want to either bust the cache after publish (AE call) or accept a 5-60 minute lag for natural expiration.

4. **Authoritative source for segment E going forward.** If `aua_certification/{date}.json` ever stops getting written (BD pipeline failure), the daily extension step degrades to silver-sum fallback. Both should be coded; certification preferred, silver fallback secondary. Both missing = log error, skip the append (don't write a hallucinated row).

5. **The 2026-01-06 → 2026-01-15 hold-flat decision** ($271M plug for 10 days) is Andrew-explicit. Document in the commit message and in the file's metadata block (add a `methodology_segments[]` array if we want to be precise about provenance).

6. **`certified_aua` excluded the daily holidays already?** Sample range 2026-03-11 → 2026-05-11 has only 37 files — that's roughly business days only. No 2026-03-14/15 (Sat/Sun) etc. The output JSON should ffill weekends/holidays exactly like the current SmartX timeseries does. Verify the existing portal roll-forward `getNonModelAumForDate` handles this — yes, it does (lookback to most recent ≤ targetDate).

7. **Cross-firm risk:** the non_model_assets.json file is firm-scoped (49Financial-only). The portal proxy serves it at `/api/general/portfolios/non_model_assets.json` (public path, no auth). For multi-firm portal expansion, this would need a per-firm variant — but that's out of scope for this brief.

---

## Acceptance criteria

- [ ] `non_model_assets.json` `time_series[]` covers 2024-11-01 → today (no gaps in business days)
- [ ] `latest.date` == today (or T-1 if today's BD certification hasn't landed)
- [ ] All 5 segments respect their source-of-truth rule per table above
- [ ] Identity check: every row satisfies `enterprise_total − model_aum − non_model_aum < $0.01`
- [ ] Validation report committed to `docs/briefs/` documenting all step magnitudes at segment boundaries
- [ ] Portal renders the stacked AUM chart with smooth daily progression from 2026-01-16 forward
- [ ] Daily Lambda chain extension adds a new row per business day going forward
- [ ] `compute_non_model_assets.py` retired or rewritten as a runner of the new backfill script

---

## References

- Existing dead file: `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json`
- BD certification source: `s3://opal-data-bd/gold/aua_certification/{date}.json`
- BD silver fallback: `s3://opal-data-bd/silver/allocations/{date}.parquet`
- Legacy CSV (frozen): `s3://opal-data-smartx-v2/raw/enterprise_aum/49_financial_group_daily_aum.csv`
- Portal proxy route: `infra/aws/lambda/portal_data_proxy/lambda_function.py:2222-2224`
- Frontend consumer: `portal/src/pages/ModelPortfolios.tsx:91-109,430-436`; `portal/src/api/portal-proxy.ts:340-396`
- Existing SmartX canonical logic: `data/smartx/CANONICAL_DATA_LOGIC.md`
- SmartX pipeline bible: `data/smartx/SMARTX_BIBLE.md`
- Legacy backfill script (retire): `data/smartx/scripts/compute_non_model_assets.py`

---

— 0.4.0_DS_ClientPlatform (base)
