# AUA Gap Investigation and Pipeline Fixes -- 1.0.0_SA_CTO

**Date:** 2026-03-28 / 2026-03-29
**Start Time:** 8:15 PM ET (03-28)
**End Time:** 4:30 AM ET (03-29)

## Objective

Investigate and close the AUA gap between gold layer (positions cube x canonical prices) and silver layer (BD-reported account market values). Started at +$37.3M net gap (+2.34%) with $182.6M gross overvaluation and -$145.3M gross undervaluation. Three root causes identified and fixed, reducing net gap to +$8.5M (+0.53%) -- 77% reduction.

---

## Work Completed

### 1. Passthrough Types Fix (inherited from DS 03-27 session)

Commit `6e2ff75f` added PASSTHROUGH_TYPES (Journal, Valuation, Corporate Action Adjustment) to `02_build_positions_cube.py` and `03_build_holdings_lots.py`. Previously these transaction types were ignored, causing ~9,583 seeding transactions to be dropped.

Post-run 05e showed mixed results: gross over increased from $150.8M to $178.0M, gross under improved from -$138.1M to -$127.1M, accounts >50% off dropped from 995 to 635. The passthrough types added units but those units were priced at stale T1/interpolated prices, creating new overvaluation.

### 2. Hypothesis Testing -- Units vs Pricing

Multiple hypotheses tested and rejected:

| Hypothesis | Test | Result |
|-----------|------|--------|
| Cross-account dedup collision | 05f H1b: portfolio group analysis | ZERO cross-account collisions. Global dedup = account-scoped dedup. |
| Missing exit transaction types | 05m: unrecognized txn type analysis | No missing exit types. Buy/Sell/Transfer/CA taxonomy is complete. Dividend/Interest extend forward-fill but don't change units. |
| Bond face-value multiplier error | DS traced T1 construction for bonds | min(mv_price, raw_price) correctly picks $/unit. No multiplier error. |
| Global forward-fill cap (Option 3) | 05n: simulation | UNSAFE -- would drop $1.43B, kill 4,838 real accounts. Rejected. |

Andrew's key correction: agents repeatedly asserted "unit undercounting" without holding-level ground truth. Silver allocations have no per-holding units. The gap could not be attributed to units without proof. Andrew redirected to pricing source analysis.

### 3. Pricing Source Decomposition (05i, 05j)

05i decomposed the gap by pricing source. Key finding: Yahoo-dominated accounts (>80% Yahoo-priced) still showed $56M over / $68M under. This was initially interpreted as "units problem" but further investigation revealed:

- Yahoo and T1 prices are current (0 days stale)
- Interpolated prices: median 30 days stale, max 1,983 days, $288M of holdings
- IQLT: $36.8M at $49.08, 34 days stale, no Yahoo ticker match
- Shield products: $41M at $1.00/unit, 160+ days stale

05j staleness analysis confirmed interpolation as the worst source. This redirected the investigation from units to ticker resolution.

### 4. Account Gap Distribution (05k buckets)

Andrew designed the bucket analysis: within 1%, 1-5%, 5-15%, 15-30%, 30-50%, >50% -- separate for overshoot and undershoot. Results showed:
- 31% of accounts within 5% ($14.5M gap -- fine)
- >50% tails (1,024 accounts) drove $144.6M of $305M gross error
- Overshoot tail: ghost accounts + $1.00 interpolated assets
- Undershoot tail: zero-gold accounts + PDFE/PFOE gaps

This established the investigation framework for the rest of the session.

### 5. YF_OVERRIDES -- Yahoo Ticker Resolution (3 iterations)

**Phase 1 (57 entries, commit 27b2a482):** Wired `ASSET_NAME_TO_TICKER` from `etf_classification.py` into `build_canonical_prices_v2.py`. Impact: -$1.1M (modest).

**Design consolidation (commit 26750d23):** Andrew directed merging all separate override layers (OPAL_ETF_OVERRIDES, ETF_CLASSIFICATION_OVERRIDES, TICKER_CORRECTIONS) into a single `YF_OVERRIDES` dict. One table, one import, one place to add mappings.

**Phase 2 expansion (commit fef7ed1c):** Added 20 more entries from top-50 analysis. Found 3 actively wrong mappings: iShares Consumer Staples (XLP->IYK, Andrew confirmed IHF for Healthcare Providers), Invesco BulletShares year mismatches (BSCN->BSCQ/BSCR).

**Wrong ticker audit (05r):** Found 94 suspect wrong Yahoo tickers ($24.9M gold MV). Top offenders: IXJ mapped to US Healthcare Providers (should be IHF), SCHB for Schwab S&P 500 (should be SWPPX), VUG for Vanguard Admiral (should be VWUAX), SPY for an index fund (mutual fund share class).

**BD Unrealized Gain/Loss report integration:** Andrew provided `Unrealized Gain_Loss.xlsx` -- 402,623 tax lots across 7,244 accounts with BD's own Ticker and CUSIP assignments (99.5% coverage). This replaced all regex/heuristic ticker resolution with BD-authoritative mappings.

**Final build (commit a8925d3d, 783b1aa8):** 754 YF_OVERRIDES from BD's own ticker assignments. 498 new tickers fetched into historical_prices.parquet (4.97M rows, 3,738 tickers). DS ran backfill locally when EC2 was Yahoo rate-limited (HTTP 429).

**PFDE discovery:** The #1 gap contributor ($97M, 4,919 accounts) was PFDE -- a valid Yahoo ticker ($22.94) that was never in `historical_prices.parquet`. The Yahoo fetcher had never downloaded it. "PDFE" in diagnostic comments was a human transposition; the correct ticker is PFDE. Andrew confirmed the 49F model portfolio ETFs: PFDE, PFOE, DIVZ, IDVZ, PCHI.

**Net impact of ticker resolution:** +$37.3M -> +$24.8M (-$12.5M, -33%). Plateaued at 256 overrides; 757 added only $0.1M more. Ticker resolution ceiling reached.

### 6. Ghost Suppression (Option 3b)

Silver-gated phantom suppression in `02_build_positions_cube.py` `write_partition()`. Commit `f0dc06bf`.

Condition: exclude account from partition if gold_mv > 5x silver_mv AND silver_mv < $10K. With timeseries safety: suppression only applies to partitions >= silver allocation date.

Removed 11,415 phantom positions, eliminated 144 ghost accounts from >50% tail. z0821392551 ($7.4M ghost, silver=$3K) eliminated entirely. Net impact: -$17.2M overshoot reduction.

### 7. Scoped Override Pipeline Fix

**Root cause:** `run_gold_layer.sh` line 92 called `inject_scoped_overrides.py` WITHOUT `--upload` flag. The script defaulted to dry-run. **No scoped overrides had EVER been injected into canonical_prices.** All existing overrides (BNP Paribas $0.75, Waldrop $1.95, MBS, JPM structured, Destinations) were dead code.

Fixed in commit `cb00f031`. Added `--upload` flag.

### 8. Shield/AQR Back-Solved NAVs

Andrew suggested back-solving Shield product NAVs from silver allocations: `shield_implied_mv = silver_mv - sum(yahoo_priced_holdings)`. DS ran diagnostic on 113 clean accounts (par products as only non-Yahoo holding).

Results: Shield NAVs are $1.07-$1.19 (low std 0.03-0.18), consistent across accounts. AQR Delphi at $0.95. The $1.00 par pricing understated by 10-15%. 26 new scoped overrides added using median implied NAVs.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Reject dedup fix (transaction_id -> transaction_id + account_id) | Andrew flagged portfolio group duplication (~6x). 05f confirmed zero cross-account collisions. Change had no effect. |
| Reject global forward-fill cap (Option 3) | 05n simulation showed $1.43B dropped, 4,838 real accounts destroyed. |
| Single YF_OVERRIDES table replaces layered overrides | Andrew's design -- one table, one place to add mappings. Simpler. |
| Use BD Unrealized report for authoritative ticker mapping | 99.5% ticker coverage from BD's own assignments. Replaces regex/heuristic. |
| DS commits, AE pushes+deploys for gold layer work | Andrew directed: skip DT for data pipeline iteration. |
| Back-solve Shield NAVs from silver instead of requesting external data | Andrew's insight: silver already includes BD's real NAV. |
| Silver-gated ghost suppression over global forward-fill cap | Targets only accounts where gold >> silver AND silver < $10K. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | Passthrough types + ghost suppression | Yes -- `6e2ff75f`, `f0dc06bf` |
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Passthrough types | Yes -- `6e2ff75f` |
| `data/black_diamond/scripts/gold/run_gold_layer.sh` | inject_scoped_overrides --upload fix | Yes -- `cb00f031` |
| `data/black_diamond/scripts/silver/lib/ticker_overrides.py` | YF_OVERRIDES consolidated (754 entries) | Yes -- `26750d23`, `fef7ed1c`, `783b1aa8`, `a8925d3d` |
| `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` | Import YF_OVERRIDES | Yes -- `27b2a482` |
| `data/black_diamond/scripts/silver/bd_price_update.py` | Import YF_OVERRIDES + Shield/AQR scoped overrides | Yes -- multiple |
| `data/black_diamond/scripts/silver/inject_scoped_overrides.py` | Shield/AQR NAV overrides added | Yes |
| `data/black_diamond/scripts/gold/05f_diagnose_positions_cube.py` | Enhanced with portfolio group analysis | Yes |
| `data/black_diamond/scripts/gold/05i-05q diagnostic scripts` | Various gap decomposition diagnostics | Yes (on EC2 via S3) |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | ADVI_PRICES completion date corrected | Yes (local) |

---

## Diagnostic Scripts Created This Session

| Script | Purpose | Key Finding |
|--------|---------|-------------|
| 05i_gap_by_pricing_source.py | Decompose gap by Yahoo/T1/interpolation | Yahoo accounts still had gaps -- not purely pricing |
| 05j_staleness_analysis.py | Price staleness by source | Interpolation median 30d stale, $288M affected |
| 05k_account_gap_buckets.py | Bucket distribution of account-level gaps | >50% tails drive $144.6M of $305M gross error |
| 05l_tail_drill.py | Asset-level drill into >50% tails | PDFE/PFOE frequency, AQR/Shield $1.00 pricing |
| 05m_ghost_pattern.py | Forward-fill timing analysis | 5,236 positions ($54.7M) held open by dividend activity |
| 05n_option3_simulation.py | Global forward-fill cap safety check | UNSAFE: $1.43B dropped |
| 05o_unmatched_assets.py | Non-Yahoo asset categorization | $326M likely-public, 70% resolvable |
| 05q_tail_decomposition.py | Granular overshoot + undershoot decomposition | 81 ghosts ($20.7M), $53.7M interpolation, 389 zero-gold accounts |
| 05r_yahoo_mapping_audit.py | Wrong ticker detection | 94 suspect wrong tickers, $24.9M affected |
| 05s_yf_overrides_coverage.py | Validate override tickers have Yahoo data | 76/272 initially had data, rest needed backfill |

---

## Results Progression

| Run | Net Gap | Gross Over | Gross Under | >50% Over | Within 5% |
|-----|---------|-----------|-------------|-----------|-----------|
| Baseline (pre-session) | +$37.3M (+2.34%) | $182.6M | -$145.3M | 411 | 1,986 |
| 57 YF_OVERRIDES | +$36.1M (+2.27%) | $181.4M | -$145.3M | 406 | 1,986 |
| 256 YF_OVERRIDES + PFDE | +$24.9M (+1.56%) | $173.0M | -$148.1M | 388 | 2,027 |
| 757 YF_OVERRIDES (plateau) | +$24.8M (+1.55%) | $172M | -$147M | 386 | 2,039 |
| **Ghost + Scoped + --upload fix** | **+$8.5M (+0.53%)** | **$69M** | **-$59M** | **267** | **~2,100** |

---

## Current State

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

Net AUA gap reduced from +$37.3M (+2.34%) to +$8.5M (+0.53%) through three classes of fixes: Yahoo ticker resolution (754 BD-authoritative mappings), silver-gated ghost suppression (11,415 phantom positions removed), and scoped override pipeline repair (--upload flag, 33 override assets now flowing). EC2 instance i-01003b035d2988dfb (c6i.16xlarge) still running with AutoShutdown=disabled -- needs tag removal when work is complete.

Remaining $8.5M net gap: $69M gross over (267 accounts >50%) vs $59M gross under (1,369 accounts, mostly zero-gold with small silver AUA). The gross figures are now much closer to structural limits: assets genuinely not on Yahoo (munis, private placements), accounts BD never sent transaction history for, and residual pricing methodology differences between BD custodial NAV and Yahoo market close.

BD Unrealized Gain/Loss report (`C:\Users\AndrewBerman\Downloads\Unrealized Gain_Loss.xlsx`) ingested for ticker mapping but not yet integrated as a recurring pipeline feed. Realized Gain/Loss report was empty (needs date range parameter from BD).

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Remove AutoShutdown=disabled tag** on EC2 once no further gold runs are needed
2. **[0.4.0_DS_ClientPlatform] Investigate remaining $69M gross overshoot** -- 267 accounts still >50% over. What assets drive them after ghost suppression and scoped overrides?
3. **[0.4.0_DS_ClientPlatform] BD Unrealized report as recurring feed** -- design integration into the pipeline so positions cube can cross-reference BD's holding snapshot daily
4. **[Andrew] Re-pull Realized Gain/Loss from BD with date range** -- closed positions data would identify what BD considers sold vs what gold still holds
5. **[0.4.0_DS_ClientPlatform] Continue YF_OVERRIDES expansion** for the long tail of unmatched assets (diminishing returns but +$0.1M per batch)
6. **[1.0.0_SA_CTO] Assess whether to register this as a project** -- the work has been ad-hoc across ADVI_PRICES spillover; may warrant its own project code if continuing

**Files to touch next:**
- `data/black_diamond/scripts/silver/inject_scoped_overrides.py` -- add more Shield product variants as they're identified
- `data/black_diamond/scripts/silver/lib/ticker_overrides.py` -- continue expanding YF_OVERRIDES from BD unrealized report
- `data/black_diamond/scripts/gold/02_build_positions_cube.py` -- potential integration of BD unrealized as position existence filter

**Do NOT:**
- Claim dollar magnitudes for phantom/missing positions from the unrealized report (no units column)
- Apply global forward-fill caps (Option 3 proven unsafe at $1.43B blast radius)
- Change dedup logic without proving portfolio group duplication is handled
- Assume "units" as root cause without holding-level ground truth

---

## Phase 2: BD Reports Integration (post-05k investigation)

### New BD Data Sources Provided by Andrew

| Report | File | Rows | Accounts | Key Fields |
|--------|------|------|----------|-----------|
| Unrealized Gain/Loss | Unrealized Gain_Loss.xlsx | 402,623 lots | 7,244 | AccountID, Asset Name, Ticker, CUSIP, Unit Cost, Open Date (NO units) |
| Realized Gain/Loss Q1 2026 | Realized Gain_Loss (1).xlsx | 147,884 | 5,305 | AccountID, Asset Name, Ticker, CUSIP, Trade Date, Unit Cost (NO units) |
| Realized Gain/Loss Q4 2025 | Realized Gain_Loss (2).xlsx | 95,420 | 4,739 | Same schema |
| Realized Gain/Loss Q3 2025 | Realized Gain_Loss (3).xlsx | 75,688 | — | Same schema |
| Realized Gain/Loss Q2 2025 | Realized Gain_Loss (4).xlsx | — | — | Same schema |
| Snapshot | Snapshot (2).xlsx | 337,901 | 11,447 | AccountID, Asset Name, Ticker, CUSIP (broadest account coverage) |

### Unrealized Report Findings

- 93,239 unique (AccountID, Asset Name) holdings after lot dedup
- 99.5% have BD-assigned tickers, 99.6% have CUSIPs
- BD-authoritative ticker mappings used to rebuild YF_OVERRIDES from 256 to 754 entries
- 7,244 accounts vs silver's 6,464 — 788 unrealized-only accounts (likely closed/out-of-scope)

### Position Existence Comparison (Unrealized vs Cube)

| Category | Count | Notes |
|----------|-------|-------|
| Cube positions (3/26) | 106,802 | |
| BD unrealized holdings | 93,239 | |
| Matched | ~65-70K | Varies by join method (ticker vs CUSIP vs asset_name) |
| Cube-only (phantoms) | ~40-42K | Positions our cube has that BD doesn't list as open |
| BD-only (missing) | ~21-24K | Holdings BD has that our cube doesn't |

Whitelist filter (suppress phantoms) produced -$337M gap — too aggressive because it removes positions without adding replacements. The net +$8.5M masks ~$370M phantom overshoot offset by ~$360M missing-position undershoot.

### Realized Report Findings (12 months, Q2 2025 - Q1 2026)

- 373,656 combined rows across 5,891 accounts
- 49,524 unique confirmed-closed (account, asset) pairs (in realized, NOT in unrealized)
- Matched against 41,953 cube phantoms: **9,266 confirmed sold (22.3%)**
- Top confirmed: VTV (4,676 closed), QUAL (3,787), VIX products (7,115), VGSH (2,270)
- 32,372 phantoms unexplained — likely rotated before Q2 2025 or closed through non-sale mechanisms

### Why the Net Gap Stays Near Zero

The +$8.5M net gap conceals ~$370M gross over and ~$360M gross under. These are structurally correlated: model portfolio rotations sell ETF A and buy ETF B for the same dollar amount. When our pipeline misses the sell, ETF A persists as a phantom (overshoot) while ETF B is correctly added. The account-level total stays approximately correct because the rotation is dollar-neutral. This explains why every gold run, regardless of fixes, yields a net within 0-3% of silver.

### Key Architectural Conclusion

The transaction-reconstruction approach (building positions from cumulative buy/sell history) is fundamentally incomplete for model portfolio accounts. BD closes positions through mechanisms outside the transaction feed (model rebalances, corporate actions, fund conversions). The unrealized report represents BD's current position truth, but lacks units/market value per holding.

### Next Phase: BD Report Integration (not started)

To close the holding-level decomposition gap, the pipeline needs:
1. **Daily unrealized feed** as position existence authority — suppress any cube position BD doesn't confirm
2. **Daily realized feed** as sell-side evidence — close phantom positions when BD reports a sale
3. **A mechanism to reconstruct missing positions** — for the ~21K holdings BD has that we don't, either from the unrealized report (if units can be obtained) or from a BD holdings/positions report that includes units and market value
4. **Ticker alias table** — map systematic ticker differences between our pipeline and BD's reports (BIL/CLIP, SMDV/XSVM, ACSG/QGRO, GARP/SPGP)

This is a project-level effort requiring a PRD. The current session's fixes (ticker resolution, ghost suppression, scoped overrides, --upload fix) address the pricing layer. The position existence layer requires the BD report integration.

---

## Phase 3: Lot-Level Three-Way Reconciliation

### Realized Gain/Loss Reports

Andrew provided 5 quarters of realized data (Q1 2025 through Q1 2026). Key findings:

- Realized report covers TAX EVENTS only (sales with gain/loss). Model rotations via journal entries, corporate actions, or internal rebalances do NOT appear.
- IQLT example: 26 realized accounts vs 1,950 phantom accounts. BD closes most positions through non-sale mechanisms invisible to the realized report.
- Combined 15 months: 461,665 rows, 5,891 accounts, 49,524 confirmed-closed (account, asset) pairs.

### Lot-Level Three-Way Reconciliation (Best Result)

DS matched our cube lots against BD unrealized + realized at the lot level using (AccountID, CUSIP, Open Date, Unit Cost):

| Category | Lots | Gold MV | Meaning |
|----------|------|---------|---------|
| Confirmed open | 189,829 | $699M | In cube + BD unrealized. Validated. |
| Partial sale | 9,002 | $150M | In all three reports. Some lots sold, some kept. |
| **Phantom-sold** | **34,618** | **$74M** | In cube + BD realized, NOT unrealized. Definitive phantoms. |
| Our-only | 135,235 | $783M | In cube only. Likely inflated by unit cost rounding mismatches between FIFO and BD cost basis. |
| BD unrealized-only | 182,680 | — | BD lots we don't have (missing positions). |
| BD realized-only | 213,356 | — | BD sold lots we never had. |

**$74M phantom figure is the most precise estimate** — dramatically tighter than the earlier $374M (position-level) claim. Lot-level matching on (CUSIP, date, cost) eliminates false positives from ticker mismatches and cost basis rounding.

### Why Realized Covers Only 22% of Phantoms

BD closes positions through multiple mechanisms:
- **Sales** (taxable event) — appears in realized report
- **Journal entries** (in-kind transfer between sleeves) — no taxable event, NOT in realized
- **Corporate actions** (merger, exchange, ticker conversion) — may or may not generate realized event
- **Internal rebalance** (BD processes at portfolio level) — no per-lot sell, NOT in realized

The unrealized report captures the END STATE regardless of how the position was closed. The realized report only captures one closure mechanism (sales). This is why the unrealized whitelist is more reliable than the realized-based approach for phantom detection.

### BD Reports Documentation

All BD reports documented at `data/black_diamond/bd_reports/README.md`:
- Unrealized Gain/Loss (402K lots, 7,244 accounts)
- Realized Gain/Loss Q1-Q4 2025 + Q1 2026 (461K rows, 15 months)
- Snapshot (337K rows, 11,447 accounts — broadest coverage)
- Source files in `C:\Users\AndrewBerman\Downloads\`

---

## Final Session Summary

### Delivered (Deployed)

| Fix | Impact | Commits |
|-----|--------|---------|
| YF_OVERRIDES (754 BD-authoritative ticker mappings) | -$12.5M net gap | 27b2a482, 26750d23, fef7ed1c, 783b1aa8, a8925d3d |
| Ghost suppression (silver-gated) | -$17.2M overshoot, 11,415 phantoms removed | f0dc06bf |
| Scoped overrides --upload fix | Shield/AQR/BNP/MBS now flowing for first time | cb00f031 |
| Shield/AQR back-solved NAVs | 26 new scoped overrides at $1.07-$1.19 | — |
| Yahoo backfill (498 new tickers) | 4.97M rows in historical_prices.parquet | Local upload to S3 |
| Passthrough types (inherited) | 9,583 seeding transactions recovered | 6e2ff75f |

**Net result: +$37.3M (+2.34%) -> +$8.5M (+0.53%). 77% reduction.**

### Discovered (Not Yet Deployed)

| Finding | Scale | Next Step |
|---------|-------|-----------|
| ~35K phantom lots ($74M) from model rotations | Lot-level three-way confirms | Daily unrealized feed as position authority |
| ~183K BD lots we don't have | Missing purchase history | BD holdings snapshot with units needed |
| Non-sale position closures (journals, CAs) | Invisible to transaction + realized feeds | Unrealized whitelist is the only reliable source |
| 69 ticker aliases (SMDV/XSVM, ACSG/QGRO, etc.) | ~2,846 positions | Alias table for cross-system joins |
| Net accuracy (0-3%) is structurally guaranteed | Dollar-neutral rotations | Holding decomposition is wrong but totals are right |

### Next Project: BD Report Integration

**Scope:** Integrate unrealized + realized + snapshot as recurring pipeline feeds for position reconciliation.

**Design (from this session's prototyping):**
1. Daily unrealized feed -> position existence whitelist (suppress phantoms BD doesn't confirm)
2. Lot-level reconciliation on (AccountID, CUSIP, Open Date, Unit Cost) -> precise phantom detection
3. Ticker alias table -> resolve systematic cross-system ticker differences
4. Realized feed as audit trail -> confirms WHY positions were closed (for the subset that are taxable sales)

**Prerequisite:** BD needs to provide the unrealized report as an automated daily export (same mechanism as allocations and transactions). Andrew to configure in BD.

**EC2 note:** Instance i-01003b035d2988dfb (c6i.16xlarge) still running with AutoShutdown=disabled. Remove tag when no further gold runs needed.

---

## Phase 4: Full Realized History + Root Cause Confirmation + Pipeline Design

### Realized Gain/Loss — Full History (11 unique files, 2021-2026)

Andrew provided quarterly realized exports going back to 2021. Each additional quarter confirmed more phantoms:

| Window | Confirmed | Unexplained |
|--------|-----------|-------------|
| Q1 2026 only (15mo) | 22.3% | 77.7% |
| + Q2-Q4 2024 (24mo) | 87.4% | 12.6% |
| + 2021-2023 (33mo) | 88.9% | 11.1% |
| + DIVZ name fix | **91.6%** | **8.4% (3,390)** |

**Root cause confirmed:** Opal onboarded as partner ~4/30/2024. 32,632 trades on that date alone. Model portfolios rotated from prior advisor holdings (VTV, IQLT, QUAL, BIL, COWZ, JEPI) into Opal model (PFDE, PFOE, DIVZ, IDVZ, IEFA, CLIP). Sells hit the realized report but our transaction feed never received them.

### DIVZ Name Mismatch (1,173 false phantoms eliminated)

BD's unrealized report uses "POLEN DIVIDEND INCOME ETF" (50,838 lots). Our cube has it under two names:
- "POLEN DIVIDEND INCOME ETF" (2,994 positions) — matches BD
- "OPAL DIVIDEND INCOME ETF" (1,176 positions) — doesn't match BD

1,173 of the 1,176 "OPAL" accounts exist in BD under "POLEN". The fund was renamed. This single name fix eliminated 1,173 false phantoms. Implies more name variants hiding in the remaining 3,390.

### Remaining 3,390 Unexplained Phantoms

Positions closed through non-sale mechanisms (journals, corporate actions, internal rebalances) that never generate realized gain/loss events. Top: treasury money markets (522), Fidelity cash reserves (210), institutional mutual funds, individual stocks. This is the structural floor — only the unrealized whitelist can catch these.

### AE Pipeline Design (Approved)

AE pitched extending `merge-daily-incremental.py` with `--realized` and `--unrealized` flags. Approved.

```
Bronze (BD export):
  s3://opal-data-bd/forwardfill_v2/realized/REALIZED_YYYY-MM-DD.xlsx
  s3://opal-data-bd/forwardfill_v2/unrealized/UNREALIZED_YYYY-MM-DD.xlsx

Silver (parquet):
  s3://opal-data-bd/silver/realized/YYYY-MM-DD.parquet
  s3://opal-data-bd/silver/unrealized/YYYY-MM-DD.parquet
```

Same S3 artifact model, no new infra, same EventBridge trigger chain as transactions/allocations.

**BD template note:** Andrew created two BD report templates (realized + unrealized), both set to current day. Unrealized works as a daily snapshot. Realized (current day) only shows that day's sells — accumulates over time like transactions. The historical backfill (11 quarterly files) provides full coverage through 3/26.

**Open question:** BD realized template may only capture sells with trade dates ON the selected date. Need to verify whether a single-day pull captures same-day trades only or includes recent settlements.

### DS Realized Sell Injection (ON HOLD — Not Validated)

DS committed a realized sell injection mechanism (65612b84) that injects 51,317 synthetic sells into the positions cube based on silver/realized/ + silver/unrealized/ cross-reference. Also removed ghost suppression (eece84ac) as "redundant."

**CTO placed this ON HOLD:**
1. Realized report has no units column — DS is selling "all current units" which assumes full liquidation for every phantom. Partial sells would be miscounted.
2. 51,317 synthetic sells vs 37,024 confirmed phantoms — 14K unexplained extras.
3. Removing ghost suppression before validating injection removes both safety nets.
4. Ghost suppression should be RESTORED as fallback until injection is proven via 05k comparison.

### BD Reports — All Files Documented

All 15 BD report files documented at `data/black_diamond/bd_reports/README.md`:
- Unrealized Gain/Loss (402K lots, 7,244 accounts)
- Realized Gain/Loss: 11 unique quarterly files (files 10, 12, 13 are duplicates), 892K rows, 2021-2026
- Snapshot (337K rows, 11,447 accounts)

### Name Reconciliation (Instructed, Not Yet Delivered)

DS instructed to build comprehensive asset name reconciliation map:
- Use CUSIP as canonical join key (same CUSIP = same security)
- BD unrealized report has current canonical names
- Output: old_name -> canonical_name mapping at config/asset_name_aliases.json
- Apply during silver ingestion and cube building

---

## Current Status (End of Session)

**Deployed and validated:**
- Net gap: +$37.3M -> **+$8.5M (+0.53%)** — 77% reduction
- 754 YF_OVERRIDES (BD-authoritative), ghost suppression, scoped overrides (--upload fix), Shield NAVs, 498 Yahoo tickers backfilled

**Committed but ON HOLD (not yet gold-run validated):**
- Realized sell injection (65612b84) — needs unit quantity validation before deploy
- Ghost suppression removal (eece84ac) — should be reverted, keep as fallback

**Designed but not implemented:**
- Daily realized + unrealized feed pipeline (AE design approved)
- Asset name reconciliation map (DS instructed)

**Root cause fully identified:**
- 91.6% of phantom positions confirmed as Opal onboarding rotation sells (~4/30/2024)
- 8.4% (3,390) are non-sale closures (journals, CAs) — only catchable via unrealized whitelist
- Net gap stays 0-3% because rotations are dollar-neutral (old + new positions = same account MV)

**Next steps (priority order):**
1. Validate realized sell injection — DS must explain sell quantity logic, restore ghost suppression as fallback
2. Gold rerun with validated injection + 05k comparison — the breakthrough test
3. Daily unrealized + realized feed automation (AE implements)
4. Asset name reconciliation map (DS delivers)
5. Remove EC2 AutoShutdown=disabled tag when done

**Do NOT:**
- Deploy the realized sell injection without validating sell quantities (no units in realized report)
- Remove ghost suppression until injection is proven
- Trust DS's phantom MV dollar figures derived from gold's own positions (circular reasoning)
- Assume the remaining 3,390 unexplained phantoms are all real — name normalization will reduce this further
