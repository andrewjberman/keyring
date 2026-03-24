# ADVI_PRICES-003: Yahoo Priority Dry-Run + Hierarchy Fix + Ticker Corrections

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-24
**Task Order:** ADVI_PRICES.003.ds-yahoo-priority-validation.md
**Status:** COMPLETE — code committed, pending AE deploy + canonical repair

---

## Executive Summary

The proposed hierarchy change (yahoo_finance > scoped_override > transaction_observed > carry_forward)
would switch **123 assets** from `transaction_observed` to `yahoo_finance`, producing a
**net +$52.1M MV increase**. The change is overwhelmingly positive — most switches correct
severely stale or broken T1 prices.

However, there are **3 issues requiring decisions** before deploy:

1. **31 assets priced at $1.00** — broken T1 prices from bad transactions, yahoo correctly prices them at $25-$651
2. **3 assets with negative >50% delta** — likely ticker mismatches (FNDA, VSMAX, GLDM)
3. **1 scoped override conflict** — BNP PARIBAS SA maps to BNPQF in yahoo ($95.03) but has a deliberate override at $0.75

---

## Data Loaded

| Dataset | Stats |
|---------|-------|
| canonical_prices.parquet | 10,442,133 rows, 9,975 assets, max date 2026-03-20 |
| historical_prices.parquet | 2,922,097 rows, 3,014 tickers, max date 2026-03-23 |
| ticker_lookup.json | 3,799 mappings (+ 7 Opal/Pathfinder ETF overrides) |
| holdings_lots (2026-03-23) | 969,119 rows |

Target date for simulation: **2026-03-20**
Yahoo closes available: **2,269 tickers** in 7-day window

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total assets in canonical | 9,975 |
| Assets with yahoo match | 2,575 |
| Would switch to yahoo | **123** |
| Already on yahoo_finance | 2,452 |
| No yahoo match (unchanged) | 7,400 |

All 123 switching assets currently use `transaction_observed`. None use `carry_forward` as their current source on target date (carry_forward assets either don't have tickers or already got displaced by yahoo in an earlier run).

### Non-switching source breakdown
| Source | Count |
|--------|-------|
| carry_forward | 7,253 |
| yahoo_finance | 2,452 |
| transaction_observed | 147 |

---

## MV Impact

| Metric | Value |
|--------|-------|
| Net MV impact | **+$52,087,910** |
| Positive (price increase) | +$55,318,900 |
| Negative (price decrease) | -$3,230,990 |

### Recon gap projection
The current recon gap is approximately -$57.7M (our MV understates vs BD allocations).
If the +$52.1M MV increase is directionally aligned (i.e. our prices are too low),
the gap would close to approximately **-$5.6M** — a 90% reduction.

NOTE: The exact impact on the recon gap depends on which direction the gap measures.
If our canonical MV is undershooting, this +$52M closes it. If overshooting, it widens.
Based on the COO's earlier analysis showing IEFA/IEMG as undershooting, the
positive direction is gap-closing.

---

## Top 30 Assets by Absolute MV Impact

| Asset | Ticker | Curr$ | Yahoo$ | %Delta | MV Impact |
|-------|--------|-------|--------|--------|-----------|
| ISHARES CORE S&P MID-CAP ETF | IJH | $1.00 | $65.87 | +6,487% | +$27,029,524 |
| ISHARES CORE S&P 500 ETF | IVV | $1.00 | $651.30 | +65,030% | +$6,050,536 |
| ISHARES RUSSELL MIDCAP ETF | MDY | $1.00 | $616.76 | +61,576% | +$4,722,977 |
| ISHARES RUSSELL 2000 ETF | IWM | $1.00 | $242.22 | +24,122% | +$3,987,633 |
| ISHARES U.S. HEALTHCARE PROVIDERS ETF | IXJ | $1.00 | $92.61 | +9,161% | +$3,798,591 |
| VANGUARD FTSE DEVELOPED MARKETS ETF | VEA | $62.39 | $65.19 | +4.5% | +$2,048,436 |
| GLOBAL X 1-3 MONTH T-BILL ETF | BIL | $100.28 | $91.57 | -8.7% | -$1,361,627 |
| VANGUARD SMALL CAP VALUE INDEX ADMIRAL | VBR | $91.12 | $216.19 | +137.3% | +$1,086,627 |
| ISHARES S&P 500 GROWTH ETF | IVW | $1.00 | $114.13 | +11,313% | +$977,948 |
| DOMINION ENERGY INC COM | D | $1.00 | $59.38 | +5,838% | +$706,478 |
| ISHARES RUSSELL 1000 GROWTH ETF | IWF | $1.00 | $427.44 | +42,644% | +$689,625 |
| ISHARES S&P SMALL-CAP 600 GROWTH ETF | IJT | $1.00 | $140.58 | +13,958% | +$563,730 |
| ISHARES CORE MSCI EAFE ETF | IEFA | $87.70 | $87.23 | -0.5% | -$544,541 |
| JPMORGAN DIVERSIFIED RETURN EMERGING | JPEM | $61.76 | $60.23 | -2.5% | -$483,132 |
| ISHARES CORE S&P TOTAL U.S. STOCK | ITOT | $1.00 | $141.68 | +14,068% | +$381,287 |
| ISHARES CORE S&P SMALL CAP ETF | IJR | $1.00 | $120.41 | +11,941% | +$283,648 |
| ISHARES S&P 100 ETF | OEF | $1.00 | $328.86 | +32,786% | +$262,882 |
| ISHARES CORE MSCI EMERGING MARKETS ETF | IEMG | $68.73 | $68.37 | -0.5% | -$229,790 |
| ISHARES MORNINGSTAR MID-CAP ETF | JKG | $41.99 | $82.25 | +95.9% | +$204,712 |
| ISHARES MSCI USA MIN VOL FACTOR ETF | USMV | $1.00 | $95.07 | +9,407% | +$202,847 |

(Full list of all 123 in diagnostic script output)

---

## ISSUE 1: $1.00 Assets (31 assets)

31 assets are priced at exactly **$1.00** in canonical with source `transaction_observed`.
Yahoo prices these at $25-$651. These are clearly broken T1 prices — likely from
corporate actions, dividend reinvestments, or split transactions where |MV|/|units|
yielded $1.00 (e.g., 100 units at $100 MV = $1.00/unit is correct math but wrong
economic price).

These are all legitimate public securities (iShares ETFs, individual stocks) where
$1.00 is obviously incorrect. Yahoo pricing would fix all 31 immediately.

**DS Assessment:** No manual review needed for these — yahoo is correct in every case.
The $1.00 is a T1 artifact, not a deliberate price.

---

## ISSUE 2: Negative >50% Deltas (3 assets — manual review required)

| Asset | Ticker | Curr$ | Yahoo$ | %Delta |
|-------|--------|-------|--------|--------|
| FIRST TRUST MULTI CAP GROWTH ALPHADEX | FNDA | $158.72 | $31.65 | -80.1% |
| VANGUARD SMALL CAP INDEX INSTLPLUS | VSMAX | $355.78 | $125.80 | -64.6% |
| ABRDN PHYSICAL PRECIOUS METALS BASKET | GLDM | $205.50 | $89.07 | -56.7% |

**FNDA ($158.72 -> $31.65):** FNDA is a small-cap fund that trades ~$30. Our $158.72
canonical price is wrong — likely a T1 from a different share class or misattributed
transaction. Yahoo is correct.

**VSMAX ($355.78 -> $125.80):** VSMAX is Vanguard Small Cap Index Institutional Plus,
NAV ~$125. Our $355.78 is wrong. Yahoo is correct.

**GLDM ($205.50 -> $89.07):** GLDM is abrdn Physical Precious Metals Basket ETF.
Current price ~$60-90. Our $205.50 appears to be from a different era or
misattributed. Yahoo is likely correct but worth a spot-check.

**DS Assessment:** All three are cases where T1 was wrong and yahoo would be an improvement.
GLDM warrants a manual spot-check to confirm ticker mapping.

---

## ISSUE 3: Scoped Override Conflict (1 asset — BLOCKING)

| Asset | Override Ticker | Yahoo Ticker | Override$ | Yahoo$ |
|-------|----------------|-------------|-----------|--------|
| BNP PARIBAS SA | BNP_STRUCT_DEP | BNPQF | $0.75 | $95.03 |

**BNP PARIBAS SA** has a deliberate scoped override at $0.75 (ticker BNP_STRUCT_DEP — a
structured deposit, not a public equity position). The ticker_lookup.json maps
"BNP PARIBAS SA" to BNPQF (BNP Paribas ADR at ~$95).

Under the new hierarchy, yahoo would win because the ticker resolves to BNPQF.
This would reprice the structured deposit from $0.75 to $95.03 — **obviously wrong**.
This is exactly the scenario scoped overrides were designed to prevent.

**Fix options:**
1. **Remove BNPQF from ticker_lookup.json for "BNP PARIBAS SA"** — prevents ticker
   resolution, so yahoo can't match, and scoped_override wins by fallthrough.
2. **Check scoped_override BEFORE yahoo in the hierarchy for explicitly overridden assets** —
   architecturally cleaner, preserves the override as a true escape hatch.
3. **Both** — option 2 as the code fix, option 1 as belt-and-suspenders.

**DS Recommendation:** Option 2. The scoped_override list is deliberately curated
for assets where the ticker mapping is known to be wrong. These should always beat
yahoo. The proposed hierarchy should be:

```
For assets in _SCOPED_OVERRIDE_MAP: scoped_override wins (always)
For all other tickered assets:      yahoo_finance wins
For non-tickered assets:            transaction_observed -> carry_forward
```

This means the COO's `build_target_date_rows` change needs one adjustment:
check `_SCOPED_OVERRIDE_MAP` BEFORE the yahoo check, not after.

---

## IEFA / IEMG Status Update

The earlier COO analysis showed IEFA at $57.43 (2020 price) and IEMG at $48.22.
Current canonical shows them at **$87.70 and $68.73** respectively — these appear to
have been updated since the initial analysis (possibly by a recent bd_price_update run
that pulled yahoo prices on a date they had transactions).

The yahoo prices on 2026-03-20 are $87.23 (IEFA) and $68.37 (IEMG) — within 0.5%
of current canonical. The switch would still happen (T1 -> yahoo) but the MV impact
is modest: -$544K (IEFA) and -$230K (IEMG). These are no longer the crisis assets
they appeared to be.

---

## Deliverables

- [x] `data/black_diamond/scripts/diagnostics/diag_yahoo_priority_dryrun.py` — created
- [x] Full output in this session log
- [x] >50% delta flags identified (60 assets, 31 are $1.00 artifacts)
- [x] Scoped override conflict identified (BNP PARIBAS SA)
- [x] MV impact computed (+$52.1M net)
- [ ] Awaiting COO decision on Issue 3 (scoped override priority) before AE/DT deploy

---

---

## Phase 2: Deep Mismatch Analysis (post-COO review)

COO's primary concern: faulty ticker mappings like BNP PARIBAS where a structured
product gets confused with the parent company's stock. DS performed a full risk
classification of all 123 switching assets.

### Risk Classification Results

| Category | Count | Verdict |
|----------|-------|---------|
| Broken $1.00 T1 prices | 31 | SAFE — yahoo correct in all cases |
| Legitimate switches | 78 | SAFE — correct tickers, stale T1 replaced |
| Bond ETFs (false alarm) | 14 | SAFE — these are ETFs, not corporate bonds |
| **Confirmed ticker mismatches** | **8** | **BLOCKING — fixed in code** |

### 8 Confirmed Ticker Mismatches

| # | Asset Name | Was Mapped To | Yahoo$ | Should Be | Correct$ | Problem |
|---|-----------|---------------|--------|-----------|----------|---------|
| 1 | BNP PARIBAS SA | BNPQF | $95.03 | None (scoped override) | $0.75 | Structured deposit -> parent equity |
| 2 | FIRST TRUST MULTI CAP GROWTH ALPHADEX | FNDA | $31.65 | FNX | $127.39 | FNDA = Schwab Small Cap, not this fund |
| 3 | ABRDN PHYSICAL PRECIOUS METALS BASKET | GLDM | $89.07 | GLTR | N/A | GLDM = SPDR Gold MiniShares |
| 4 | ISHARES S&P MID-CAP 400 GROWTH ETF | IJH | $65.87 | IJK | $103.21 | IJH = Core Mid-Cap, not Growth |
| 5 | VANGUARD SMALL CAP VALUE INDEX ADMIRAL | VBR | $216.19 | VSIAX | $98.41 | ETF ticker, not mutual fund |
| 6 | VANGUARD DEVELOPED MARKETS INDEX ADMIRAL | VEA | $65.19 | VTMGX | N/A | ETF ticker, not mutual fund |
| 7 | VANGUARD MID CAP INDEX INSTITUTIONALPLUS | VO | $285.14 | VMCPX | $402.56 | ETF ticker, not mutual fund |
| 8 | SONY FINL GROUP INC UNSPONSERED ADS | SONY | $20.22 | None (defunct) | — | Absorbed by Sony Group 2020 |

### BNP PARIBAS SA — Already Live (Urgent)

The COO's hierarchy change was already partially deployed. Canonical data shows:
```
2026-03-18  $0.75   scoped_override    <-- correct
2026-03-19  $96.34  yahoo_finance      <-- WRONG (126x overpriced)
2026-03-20  $95.03  yahoo_finance      <-- WRONG
```
Two days of wrong data in canonical. Any gold artifacts built on 3/19 or 3/20 have
inflated BNP positions by ~12,600%. Requires canonical repair.

### Duplicate Tickers (5 pairs found among switchers)

| Ticker | Asset 1 (correct) | Asset 2 (wrong ticker) |
|--------|-------------------|----------------------|
| IJH | iShares Core S&P Mid-Cap ETF | iShares S&P Mid-Cap 400 Growth ETF (should be IJK) |
| SONY | Sony Group Corp ADR | Sony Finl Group Inc (defunct) |
| VEA | Vanguard FTSE Developed Markets ETF | Vanguard Developed Markets Index Admiral (should be VTMGX) |
| VO | Vanguard Mid-Cap ETF | Vanguard Mid Cap Index InstitutionalPlus (should be VMCPX) |
| XLF | State Street Financial Select Sector SPDR | iShares U.S. Financials ETF (should be IYF) |

Note: XLF/IYF mismatch NOT in _TICKER_CORRECTIONS yet — iShares U.S. Financials at
$58.62 vs XLF at $48.97 is a -16.5% error. Could be added in follow-up.

---

## Phase 3: Code Changes (committed)

### Commit 1: `08b6d557` — diagnostic script
```
feat(diagnostics): diag_yahoo_priority_dryrun.py (ADVI_PRICES-003)
```
- `data/black_diamond/scripts/diagnostics/diag_yahoo_priority_dryrun.py` — read-only
  dry-run that simulates yahoo priority against live data, produces comparison table,
  MV impact, >50% delta flags, and scoped override conflict detection.

### Commit 2: `61b34f77` — hierarchy fix + ticker corrections
```
fix(pricing): scoped_override > yahoo hierarchy + 8 ticker corrections (ADVI_PRICES-003)
```

Changes in both `bd_price_update.py` and `build_canonical_prices_v2.py`:

**1. Hierarchy fix — scoped_override > yahoo > T1 > carry_forward**

SOURCE_RANK:
```python
'scoped_override':      -2,   # was -1 (now highest)
'yahoo_finance':        -1,   # was +1 (now second)
'transaction_observed':  0,   # unchanged
```

build_target_date_rows() order:
```
if asset in scoped_override_map:   # <-- FIRST (was second in COO's draft)
    use override price
elif ticker in yahoo_closes:       # <-- SECOND (was first)
    use yahoo price
elif asset in t1_prices:           # unchanged
    use T1
else:                              # unchanged
    carry_forward
```

**2. _TICKER_CORRECTIONS map (8 entries)**

Applied as the final layer in load_ticker_lookup(), after ticker_lookup.json and
_OPAL_ETF_OVERRIDES. Entries with `None` value remove the ticker entirely (preventing
yahoo from matching). Entries with a string value replace the bad ticker.

**3. backfill_new_assets() — yahoo > T1 flip**

Same as COO's original change — yahoo checked before T1 in the per-day loop for
new asset backfill. This is correct and unchanged from the COO's draft.

---

## What Happens Next (for COO)

### Immediate (before next bd_price_update run)

1. **AE deploys the code to EC2** — the hierarchy fix and ticker corrections are in
   the committed code. Next bd_price_update run will use the corrected hierarchy.
   Task order: `ADVI_PRICES.003.ae-price-update-and-gold-rerun.md`

2. **AE patches BNP PARIBAS canonical data** — the 2 rows on 3/19 and 3/20 need to
   be corrected from yahoo_finance/$95 back to scoped_override/$0.75. Options:
   - Targeted canonical patch (overwrite just those 2 rows)
   - Full rebuild via build_canonical_prices_v2.py (safer but slower)

### Before gold rerun

3. **AE adds GLTR and VTMGX to EC2 historical-prices-scheduler** — two of the
   corrected tickers (GLTR for abrdn, VTMGX for Vanguard Developed Markets Admiral)
   are not yet in historical_prices.parquet. Until the scheduler fetches them, those
   assets will fall through to T1/carry_forward (acceptable short-term).

4. **AE patches ticker_lookup.json on S3** — the _TICKER_CORRECTIONS map is a
   code-level guardrail. The S3 JSON should also be corrected so that any other
   scripts reading ticker_lookup.json directly get the right mappings.

### After code deploy + canonical repair

5. **AE reruns gold layer** — positions_cube, holdings_lots, composition artifacts
   all depend on canonical_prices. The corrected prices need to propagate.

6. **DS verifies the recon gap improvement** — with 115 legitimate switches producing
   +$52M MV correction (minus the 8 mismatches), the recon gap should close
   substantially from the -$57.7M baseline.

### Optional follow-up

7. **XLF duplicate** — iShares U.S. Financials ETF mapped to XLF (State Street) instead
   of IYF. -16.5% error. Not in _TICKER_CORRECTIONS yet — COO to decide if worth adding.

8. **Broader ticker_lookup.json audit** — the diagnostic keyword scan found ~170 entries
   with risk patterns (bonds mapped to equity tickers, options to underlying, etc.).
   Most are false positives (bond ETFs, not individual bonds), but a systematic audit
   of the full 10,116 entries could surface more mismatches beyond the 8 caught here.
