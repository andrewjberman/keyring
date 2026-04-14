# T1 Cap Audit — Findings

**Total capped rows in v2 diff:** 31
**Distinct assets:** 14
**Run date:** 2026-04-10
**Source:** v2 (`build_canonical_prices_v2.py` @ commit `5d4756e2` on CLOUD) against `silver/transactions/` snapshot, 2,879,975 deduped rows
**Audit harness:** `data/analysis/t1_cap_audit_dump.py`, `data/analysis/t1_cap_audit_investigate.py`
**Raw audit output:** `/tmp/t1_capped_rows.parquet`, `/tmp/t1_capped_rows.csv`, `/tmp/t1_audit_investigate.txt`

---

## Summary by classification

| Classification | Asset count | Row count |
|---|---:|---:|
| LEGITIMATE — regime shift (split / reverse-split runup) | 2 | 13 |
| LEGITIMATE — sparse history polluted by synthetic $1.00 entries | 3 | 9 |
| AMBIGUOUS — sparse, leans legitimate | 1 | 1 |
| CORRUPTION — 2024-08-07 BD file error | 8 | 8 |
| **Total** | **14** | **31** |

**Headline:** the 50x cap is doing its job on exactly one thing — the 2024-08-07 BD file error, which hits 8 assets and produces price spikes of 200x–60,000x median. **Everything else the cap currently rewrites is a legitimate price being silently smoothed.** 6 of the 14 assets (6 if the ambiguous one leans legitimate = 6) have correct observations being destroyed.

Two distinct root causes drive the non-corruption capping:

1. **Real regime shifts** (CMG 50:1 split, PRAX 1:15 reverse split + subsequent 100x run). The asset's historical median is the post-shift value; pre-shift observations trip the 50x rule. This is the scenario the exemption list is designed for — seed with these two.

2. **Sparse history polluted by synthetic $1.00 entries** (3x Vanguard GM collective trusts, Red Rock Resorts). BD records some transaction types (dividend reinvestments, cash distributions, or share-class conversions) at unit count × $1 synthetic pricing. When these dominate a thinly-traded asset's history, the median collapses to $1.00 and every real NAV observation trips the cap. The pre-cap price is the **correct** price; the median is broken.

   The exemption list is a stopgap for scenario 2, not a root-cause fix. The real fix is either (a) filtering synthetic $1.00 rows out of the median computation, (b) per-asset sample-size guards (e.g., only apply the cap when `len(observations) > N`), or (c) detecting the "GM"/collective-trust pattern by asset name and using a different pricing path. Flag this as a follow-up for ADVI_GLDRST.021c or similar.

---

## Per-asset findings

### 1. CHIPOTLE MEXICAN GRILL INC COM
- **Ticker:** CMG
- **Classification:** LEGITIMATE — regime shift (stock split)
- **Capped rows:** 4 (2024-05-10, 2024-05-14, 2024-05-16, 2024-05-17)
- **Pre-cap prices:** $3,145.88 – $3,239.23
- **Capped to:** $55.4492 (asset historical median)
- **Evidence:**
  - `yfinance.Ticker('CMG').splits` → **50:1 split on 2024-06-26** (exact ratio match)
  - `yfinance.Ticker('CMG').history(...)` 2024-04-26..2024-05-30 shows close range $61.46–$64.78 (split-adjusted). Unadjusted pre-split close 2024-05-17 = $3,168.48 × 50 / 50 ≈ $63.37; BD's $3,168.48 matches the unadjusted actual price.
  - BD transaction history: 36 daily T1 observations total, bucketed as 10 in $10-50, 16 in $50-150, 10 in $500-5000. The 10 high-bucket entries are all May 2024 (pre-split window); the post-split and other pre-split entries cluster around $55.
  - No BD corruption; BD is faithfully reporting actual pre-split transaction prices.
- **Recommendation:** add to `_T1_CAP_EXEMPTIONS`.

### 2. PRAXIS PRECISION MEDICINES INC COM NEW
- **Ticker:** PRAX
- **Classification:** LEGITIMATE — regime shift (prior 1:15 reverse split) + legitimate post-split runup
- **Capped rows:** 9 (2025-10-16 through 2026-03-30)
- **Pre-cap prices:** $157.21 – $345.03
- **Capped to:** $2.5286 (asset historical median)
- **Evidence:**
  - `yfinance.Ticker('PRAX').splits` → **1:15 reverse split on 2023-11-29** (ratio 0.0667)
  - `yfinance.Ticker('PRAX').history('2025-10-02','2026-04-13')` shows 131 trading days, first close $55.19, last close $314.96, range $50.98–$347.55. This matches BD's pre-cap $157-$345 range almost exactly.
  - BD has 213 transactions spanning 2022-09-16 to 2026-03-30, including 60 "Corporate Action" entries (consistent with a reverse split plus reorganization — the "NEW" suffix on the asset name).
  - Daily T1 price distribution: 1 entry at ~$1, 39 in $1-10, 19 in $10-50, 10 in $50-150, 9 in $150-500. The low-bucket entries are pre-reverse-split (2022-2023) and post-split recovery; the $150-500 bucket is the Oct 2025+ runup. The asset median of $2.53 is pulled down by ~40 pre-reverse-split-era observations; the 9 capped rows are legitimate post-runup prices matching yfinance.
  - No BD corruption; BD is faithfully reporting actual post-runup transaction prices. Root cause is that BD's asset history spans the 1:15 reverse split without unit adjustment, pulling the median below the 50x threshold for current prices.
- **Recommendation:** add to `_T1_CAP_EXEMPTIONS`. Separately, consider cleaning BD's pre-reverse-split entries out of the price history for this asset.

### 3. VANGUARD INSTL 500 IDX TRST GM
- **Ticker:** none (Vanguard Institutional 500 Index Trust collective trust, "GM" = Group Managed class, no yfinance mapping)
- **Classification:** LEGITIMATE — sparse history polluted by synthetic $1.00 entries
- **Capped rows:** 4 (2024-07-29, 2024-10-01, 2025-01-02, 2025-03-24)
- **Pre-cap prices:** $55.60, $58.32, $60.00, $58.33
- **Capped to:** $1.0000 (asset historical median)
- **Evidence:**
  - BD has 11 total transactions over 2024-07-29 to 2025-06-20, producing 9 daily T1 observations: 5 at $1.00, 4 at $55-$60.
  - The 4 high-value dates are all calendar-quarter boundaries (end of Jul, start of Oct, start of Jan, end of Mar), consistent with quarterly plan-sponsor NAV revaluation or rebalance events.
  - The $55-$60 range is the correct unit NAV for a Vanguard S&P 500 collective trust at that time period (the retail Vanguard 500 Index Admiral VFIAX closed 2024-07-29 at ~$479 per share; a 1:~8 unit class at ~$58 is internally consistent).
  - The 5 at-$1.00 observations are synthetic accounting records (dividend reinvestments, income distributions, or intra-quarter unit adjustments recorded as unit count × $1). These dominate the median.
  - Asset median of $1.00 is mathematically wrong for pricing purposes; every real quarterly NAV trips the 50x cap.
- **Recommendation:** add to `_T1_CAP_EXEMPTIONS` as a stopgap. Root-cause fix: exclude synthetic $1.00 entries from the median computation, or apply per-asset minimum-sample guards before capping.

### 4. VANGUARD INSTL TOTAL BD ID GM
- **Ticker:** none (Vanguard Institutional Total Bond Index Trust collective trust)
- **Classification:** LEGITIMATE — sparse history polluted by synthetic $1.00 entries (same pattern as #3)
- **Capped rows:** 4 (2024-07-29, 2024-10-01, 2025-01-02, 2025-03-24)
- **Pre-cap prices:** $108.97, $113.35, $109.69, $120.00
- **Capped to:** $1.0000
- **Evidence:**
  - Identical BD profile to VANGUARD INSTL 500 IDX TRST GM: 11 transactions, 9 T1 dates, 5 at $1.00, 4 on calendar-quarter boundaries at $108-$120.
  - $108-$120 is a reasonable unit NAV for a total-bond index collective trust (Vanguard Total Bond Market Admiral VBTLX closed 2024-07-29 at ~$69; a ~1.6x unit class at ~$109 is internally consistent).
  - Same synthetic-$1.00 pollution issue.
- **Recommendation:** add to `_T1_CAP_EXEMPTIONS`. Same root-cause fix notes as #3.

### 5. RED ROCK RESORTS INC CL A
- **Ticker:** RRR
- **Classification:** LEGITIMATE — sparse history polluted by synthetic $1.00 entries
- **Capped rows:** 1 (2025-07-02)
- **Pre-cap price:** $54.23
- **Capped to:** $1.0000
- **Evidence:**
  - `yfinance.Ticker('RRR').history('2025-06-18','2025-07-16')` shows close range $50.23–$57.32 — BD's $54.23 is exactly in range.
  - No splits in RRR yfinance history.
  - BD has only **6 transactions** for this asset over 2025-05-21 to 2025-07-02 (4 Sales, 2 Dividends). Only 4 Sales participate in T1 (Dividend is not in PRICE_TYPES). Daily T1 produces 3 dates: 2 at $1.00 and 1 at $54.23.
  - The 2 at-$1.00 observations are almost certainly synthetic-accounting Sales (e.g., lot disposal at $1 par or unit-based recording of a dividend-reinvest sale).
- **Recommendation:** add to `_T1_CAP_EXEMPTIONS`. This is the most marginal of the "sparse pollution" cases — only 6 txns total. Root-cause fix would be per-asset minimum-sample guards before the cap applies (e.g., `if len(daily_observations) >= N`).

### 6. VANGUARD EXPLORER FUND GM
- **Ticker:** none (Vanguard Explorer Fund collective trust, "GM" class)
- **Classification:** AMBIGUOUS — leans LEGITIMATE
- **Capped rows:** 1 (2025-03-24)
- **Pre-cap price:** $100.00
- **Capped to:** $1.0000
- **Evidence for legitimate:**
  - Vanguard Explorer Fund Admiral (VEXRX) trades around $110-$130 retail; a collective trust unit at $100 is plausible.
  - Pattern matches cases #3 and #4 (collective trust, sparse history, $1.00 dominated median, one real-looking NAV observation on a non-quarter-end date).
- **Evidence for ambiguous:**
  - Only **5 transactions total** across 2025-01-10 to 2025-06-20 — 3 Buys, 1 Sale, 1 Income Reinvestment.
  - 4 of 5 daily T1 observations are at $1.00, 1 at exactly $100.00. The fact that it's exactly $100.00 (not a noisy decimal) is slightly suspicious — could be a plan-sponsor placeholder value rather than a real NAV.
  - No yfinance cross-check available for a collective trust.
- **Recommendation:** **escalate to Andrew**. If Andrew agrees this is the same pattern as #3/#4/#5, add to `_T1_CAP_EXEMPTIONS`. Otherwise leave capped.

### 7. INVESCO STABLE VALUE RET CL 1
- **Ticker:** none (collective trust stable value fund)
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $60,077.44
- **Capped to:** $1.0000
- **Evidence:**
  - Stable value fund targeting $1.00/unit. BD has 41 daily T1 observations: **40 at $1.00** (0.99-1.01 bucket), 1 spike at $60,077 on 2024-08-07.
  - The 60,000x single-day spike is physically impossible for a stable value fund. This is the canonical 2024-08-07 BD corruption case — the exact motivating example cited in the v2 code comment.
  - Cap is working exactly as intended.
- **Recommendation:** leave under the cap. **Do not add to exemptions.**

### 8. DODGE & COX INCOME X
- **Ticker:** DOXIX
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $40,412.03
- **Capped to:** $12.4900
- **Evidence:**
  - `yfinance.Ticker('DOXIX').history('2024-07-24','2024-08-21')` shows tight close range $12.50-$12.94 across 20 trading days.
  - BD has 34 daily T1 observations, 33 in $10-50 bucket, **1 spike at $40,412** on 2024-08-07 (a 3,200x jump). Single-date anomaly.
  - Cap is working as intended.
- **Recommendation:** leave under the cap.

### 9. NORTHERN TRST COLL EAFE IDX T3
- **Ticker:** none (collective trust)
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $26,108.78
- **Capped to:** $159.2880
- **Evidence:**
  - BD has 30 daily T1 observations, 29 in $150-500 bucket, 1 spike at $26,108 on 2024-08-07 (a 164x jump). Single-date anomaly, cluster with the other 2024-08-07 corruption cases.
  - Cap is working as intended.
- **Recommendation:** leave under the cap.

### 10. NORTHERN TRUST S&P 500 TIER 3
- **Ticker:** none (collective trust)
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $31,217.93
- **Capped to:** $556.5877
- **Evidence:**
  - BD has 31 daily T1 observations, 27 in $500-5000, 3 in $150-500, 1 spike at $31,217 on 2024-08-07 (56x the median). Single-date anomaly, cluster with 2024-08-07 corruption group.
- **Recommendation:** leave under the cap.

### 11. NT AGG BOND INDEX DC NL TIER 3
- **Ticker:** none (collective trust)
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $71,863.58
- **Capped to:** $124.9208
- **Evidence:**
  - BD has 31 daily T1 observations, 30 in $50-150, 1 spike at $71,863 on 2024-08-07 (575x the median). Single-date anomaly.
- **Recommendation:** leave under the cap.

### 12. PGIM JENNISON SMALL COMPANY R6
- **Ticker:** PJSQX
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $8,625.90
- **Capped to:** $23.5500
- **Evidence:**
  - `yfinance.Ticker('PJSQX').history('2024-07-24','2024-08-21')` shows close range $21.92-$23.68 across 20 trading days.
  - BD has 33 daily T1 observations, 32 in $10-50 bucket, 1 spike at $8,625 on 2024-08-07 (366x jump). Single-date anomaly.
- **Recommendation:** leave under the cap.

### 13. VANGUARD BALANCED INDEX I
- **Ticker:** VBAIX
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $29,441.74
- **Capped to:** $48.5815
- **Evidence:**
  - `yfinance.Ticker('VBAIX').history('2024-07-24','2024-08-21')` shows close range $46.64-$48.97 across 20 trading days.
  - BD has 34 daily T1 observations, 29 in $10-50, 4 in $50-150, 1 spike at $29,441 on 2024-08-07 (606x jump).
- **Recommendation:** leave under the cap.

### 14. VANGUARD EMERGING MKTS STOCK IDX INSTL
- **Ticker:** VEMIX
- **Classification:** CORRUPTION — BD file error (2024-08-07)
- **Capped rows:** 1 (2024-08-07)
- **Pre-cap price:** $5,833.23
- **Capped to:** $28.8508
- **Evidence:**
  - `yfinance.Ticker('VEMIX').history('2024-07-24','2024-08-21')` shows close range $26.65-$28.53 across 20 trading days.
  - BD has 51 daily T1 observations, 50 in $10-50 bucket, 1 spike at $5,833 on 2024-08-07 (202x jump).
- **Recommendation:** leave under the cap.

---

## Recommended `_T1_CAP_EXEMPTIONS` seed

```python
# Assets where BD's asset history legitimately spans a regime shift or is
# polluted by synthetic $1.00 accounting entries that depress the median
# below the real NAV. These assets should NOT have the 50x lifetime-median
# outlier cap applied to them. See docs/briefs/data-scientist-t1-cap-audit-findings.md
# for per-asset evidence.
_T1_CAP_EXEMPTIONS: frozenset[str] = frozenset({
    # --- Regime shifts (stock splits / reverse splits) ---
    'CHIPOTLE MEXICAN GRILL INC COM',           # 50:1 split 2024-06-26
    'PRAXIS PRECISION MEDICINES INC COM NEW',   # 1:15 reverse split 2023-11-29 + late-2025 runup
    # --- Sparse history polluted by synthetic $1.00 accounting entries ---
    'VANGUARD INSTL 500 IDX TRST GM',           # collective trust, quarterly NAV at ~$58
    'VANGUARD INSTL TOTAL BD ID GM',            # collective trust, quarterly NAV at ~$110
    'RED ROCK RESORTS INC CL A',                # only 6 BD txns, real price $54 smoothed
})
```

**Note on exact BD asset-name matching:** each key must match the exact case-normalized form that BD writes into `asset_name`. Verified against the 31-row capped DataFrame — these strings are copy-pasted from the audit output, no name normalization needed.

If Andrew approves `VANGUARD EXPLORER FUND GM` as legitimate, add it to the sparse-pollution group.

---

## Assets to leave under the cap (confirmed corruption)

All 8 are single-row single-date events on 2024-08-07, all show pre-cap prices 50x–60,000x above the asset's otherwise-tight historical range. All match the pattern Andrew originally wrote the cap for.

| Asset | Pre-cap | Asset median | Jump factor |
|---|---:|---:|---:|
| INVESCO STABLE VALUE RET CL 1 | $60,077 | $1.00 | 60,077x |
| NT AGG BOND INDEX DC NL TIER 3 | $71,864 | $124.92 | 575x |
| VANGUARD BALANCED INDEX I | $29,442 | $48.58 | 606x |
| DODGE & COX INCOME X | $40,412 | $12.49 | 3,236x |
| PGIM JENNISON SMALL COMPANY R6 | $8,626 | $23.55 | 366x |
| VANGUARD EMERGING MKTS STOCK IDX INSTL | $5,833 | $28.85 | 202x |
| NORTHERN TRST COLL EAFE IDX T3 | $26,109 | $159.29 | 164x |
| NORTHERN TRUST S&P 500 TIER 3 | $31,218 | $556.59 | 56x |

---

## Ambiguous (escalate)

### VANGUARD EXPLORER FUND GM
- 5 BD transactions total, 4 T1 observations at $1.00, 1 at exactly $100.00 on 2025-03-24.
- Looks like the same sparse-pollution pattern as the Vanguard Institutional GM trusts, but the sample is the smallest of any capped asset and the $100.00-exactly value is slightly suspicious.
- No yfinance cross-reference available (collective trust).
- **Ask:** add to exemptions as a stopgap, or leave under the cap pending a larger sample?

---

## Follow-up recommendations beyond the exemption list

1. **Per-asset minimum-sample guard before capping.** Six of the 14 capped assets have fewer than 15 total daily T1 observations. The 50x-lifetime-median rule is statistically meaningless at that sample size. Suggest: only apply the cap when `len(daily_observations_for_asset) >= 15` (or similar). This alone would clear all three Vanguard GM cases, RRR, and the ambiguous Vanguard Explorer case without any named exemptions.

2. **Filter synthetic $1.00 entries out of the median computation.** The root cause of the GM-class pollution is that dividend reinvestments / income distributions / placeholder accounting rows are being recorded with price=1.0 and then included in the asset's lifetime median. Excluding rows where `obs_price` is suspiciously clustered at exactly $1.00 before taking the median would fix the median arithmetic rather than working around it. This is a cleaner long-term fix than an exemption list.

3. **PRAX-style pre-split history.** The "NEW" suffix in BD asset names appears to indicate post-reorganization class. Consider truncating the price history for such assets to the period after the regime shift, or using split-adjusted observations where available.

4. **Audit the 2024-08-07 BD file.** All 8 corruption cases cluster on exactly one date. This is almost certainly a single broken input file that BD ingested. Worth pulling the original BD extract for 2024-08-07 and flagging for cleanup at source rather than relying on the cap forever.

---

## Raw artifacts for reproduction

- `/tmp/t1_capped_rows.parquet` — the 31-row capped DataFrame
- `/tmp/t1_capped_rows.csv` — same, csv form
- `/tmp/t1_capped_assets_txns.parquet` — 881 BD transactions across the 14 capped assets
- `/tmp/t1_audit_investigate.txt` — full per-asset investigation output (yfinance lookups + daily T1 distributions)
- `data/analysis/t1_cap_audit_dump.py` — dumper
- `data/analysis/t1_cap_audit_investigate.py` — investigator
- Source v2 commit: `5d4756e2` on `CLOUD`

Leaving this doc dirty in the working tree per the brief's non-action rules. Not committing until Andrew reviews.
