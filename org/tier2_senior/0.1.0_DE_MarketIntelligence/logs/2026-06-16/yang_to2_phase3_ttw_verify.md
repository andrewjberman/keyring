# YANG_SITTW TO-2 — Phase-3 independent TTW verification (producer LIVE)

**archetype:** VALIDATE

**Serial:** 0.1.0_DE_MarketIntelligence
**Date:** 2026-06-16 (~19:12-19:22Z)
**TO:** YANG_SITTW.TO-2 (FE leg done DEV 27299745; data leg now LIVE via AE TO-4)
**Trigger:** AE 0.7.0_AE_CloudOps msg 191202Z — producer LIVE, all-returns.json emits TTW.

## Summary

AE deployed the additive TTW key to the market-overview producer (TO-4). Ran independent Phase-3
verification (NOT the AE self-report) on both axes — MECHANISM (deployed code) + VALUES (served vs
independent calc). **Verdict: PASS — TTW is correct.** TO-2 functionally COMPLETE pending the DT
promote of the FE. RAVC2 sent to COO (192105Z), RAVC close to AE (192111Z), promote flagged to DT
(192130Z), cross-pod basis note to TO-3 (192202Z).

## Verification

### MECHANISM (deployed Lambda market-overview-tiered-generator) — PASS
`returns['TTW'] = calculate_trailing_sessions_return(time_series, 10)`, where the new fn compounds
`time_series[-10:]` (the last 10 rows). The market-overview series is trading-days-only, so last-10-rows
= 10 trading SESSIONS. **Explicitly NOT a `PERIOD_CALENDAR_DAYS` entry** (docstring: "a calendar
window would violate §5") — the §5 calendar-vs-trading-day trap is avoided BY CONSTRUCTION. Compounds
the same daily total-return field as every sibling period -> methodology identical to 1D/1M/etc.

### VALUES (served all-returns.json vs independent trailing-10-session calc) — PASS
Pulled each ticker's `timeseries/{ticker}.json` (newest-first `historical_prices[{date,price,return}]`);
computed `price[0]/price[10]-1` AND compound of last-10 daily returns (telescope -> identical), vs served TTW:

| ticker | served TTW | indep (price-ratio) | abs diff | 10-session span |
|---|---|---|---|---|
| Gold | -0.07068538 | -0.07068538 | 3.9e-09 | 05-29 -> 06-12 |
| Bitcoin | -0.06032665 | -0.06032667 | 1.0e-08 | 06-02 -> 06-12 |
| MSCI Spain | 0.02127085 | 0.02127206 | 1.2e-06 | 05-29 -> 06-12 |
| MSCI South Korea | -0.03620688 | -0.03620788 | 1.0e-06 | 05-29 -> 06-12 |
| Silver | -0.09663269 | -0.09667995 | 4.7e-05 | 05-29 -> 06-12 |
| Dow Jones | 0.00466249 | 0.00332729 | 1.3e-03 | 05-29 -> 06-12 |
| Utilities | 0.00235568 | 0.00053368 | 1.8e-03 | 05-29 -> 06-12 |
| MSCI Taiwan | -0.01375702 | -0.01545678 | 1.7e-03 | 05-29 -> 06-12 |
| MSCI China | -0.00404523 | -0.00762255 | 3.6e-03 | 05-29 -> 06-12 |

- **Non-dividend instruments (Gold/Bitcoin/Silver/Spain/Korea): EXACT** (<5e-5) -> window + formula correct.
- **Dividend-paying equities differ 0.1-0.36pp, ALL same sign (served higher)** = the total-return-vs-
  price-return basis. The producer compounds the DDB total-return field (incl. distributions); my proxy
  `timeseries.return` field is price-only (compound == price-ratio confirms it). June = EU/Asia ex-div
  season -> the skew is largest for Utilities/Dow/China/Taiwan. Coherent, NOT a bug; the total-return
  basis is correct + consistent with the page's other periods.
- Additive: 71/71 non-null TTW; decimal unit (FE x100); every existing period byte-unchanged.

### Caveat (recorded)
This week's 10-session window (05-29 -> 06-12) has NO market holiday, so it equals 14 calendar days —
the VALUE check alone cannot distinguish trading-day from calendar count this run. The DEPLOYED CODE
(`time_series[-10:]`, not `PERIOD_CALENDAR_DAYS`) closes that definitively.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `aws s3 cp all-returns.json` (LIVE) | TTW presence/units/additivity | PASS — TTW 71/71 non-null, decimal, existing periods unchanged, gen 19:09:47Z |
| `aws s3 cp timeseries/{ticker}.json` x10 + python indep calc | trailing-10-session value verify | PASS — non-div exact (<5e-5); div-payers = total-return basis |
| Read deployed Lambda `calculate_trailing_sessions_return` | mechanism (trading-day-counted) | PASS — `time_series[-10:]`, NOT PERIOD_CALENDAR_DAYS |

**What worked:** the non-dividend exact matches proved window+formula; the deployed-code read closed the
trading-vs-calendar question the degenerate (holiday-free) window left open. **What failed:** nothing.
**Gap/finding:** the producer's total-return basis vs §5's literal price-ratio formula is a cross-pod
nuance §5 doesn't spell out -> flagged TO-3 (0.4.0_DE) to confirm their FE-computed TTW uses the same
total-return basis so dividend-bearing holdings agree across the two pages.

## Blockers
- None. (Data leg LIVE + verified; FE leg correct.)

## Current State
- **Data:** all-returns.json carries TTW (trailing 10 trading sessions, total-return, decimal) — VERIFIED.
- **FE:** portal DEV 27299745, correct + /seams-SOUND; renders real TTW now that data is live. NOT yet promoted.
- **TO-2:** functionally complete; only the DT DEV->PROD promote remains (flagged 0.1.0_DT, sequencing satisfied).

## Next Steps
- [0.1.0_DT_MarketIntelligence] Promote portal DEV 27299745 to PROD (producer-first sequencing satisfied).
- [0.4.0_DE_ClientPlatform] Confirm TO-3 TTW uses the TOTAL-return basis (cross-page agreement on dividend-bearing instruments).
- [2.0.0_SA_COO] RAVC2 verification received; close TO-2 on DT promote confirmation.
