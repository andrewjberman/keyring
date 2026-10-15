# IRPT_ANLREQ round 19, workstream ~G (ENGINE) -- decomposition: the benchmark and the risk-free rate through the price chain

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the open call `dell2-20261015T201345Z-b238` (file `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/CALL_BENCHMARK_AND_RISK_FREE_SERIES_20261015.md`), answered by the CTO's msg 8630 (`CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` ADDENDUM 2 @77c0e9fde2): option A, SPY as the benchmark and BIL as the risk-free rate, adjusted close, priced through the C-PRICES chain with a source claim each, named in words as proxies; an unpriced one leaves its statistics INPUT_MISSING, never a silent substitute. The price stage `AR-g-86` (merged `1c84d38bf4`) and the Opal wording `AR-g-89` (merged `8762c03234`), the issuer's reference build.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **A separate resolve for SPY and BIL.** They are resolved apart from the holdings, so an unpriced reference symbol never lowers the portfolio's coverage or lands in the holdings' `missing` list, and a client holding named SPY is still a holding. Cost: a symbol may be read twice in one run.
- **No trace noise.** The layout adds a named series' `key` to the trace inputs of EVERY element it computes (`_named_series`), including a plain total return that never reads it. The series therefore go in as plain lists, and the sources are stated where they are true: the `prices` block of run.json, the document's `settings` and the two disclosures.
- **"Adjusted close" is the chain's level.** Every adapter hands back a base-100 TOTAL-RETURN level (dividends included), which is the adjusted-close basis the ruling names.
- **The words are fixed in the order,** character for character, so the check can compare them: the CTO's two phrases (`SPY, a proxy for the S&P 500 Total Return index`; `BIL, 1-3 Month T-Bill ETF`) in a sentence each, and a missing form for each that names the statistics that are then unavailable.
- **A consequence found by the reference build:** the merged prices test (`AR-g-86`) asserts the exact disclosure ids of a run with an unpriced holding; it changes by that one line and the order names it. The issuer's older check `ar_g86_checks.py` asserted the ids of a fully priced run exactly; it now asserts them as "no NO_PRICING, no UNPRICED, ending in WEIGHTING".
- **Not changed:** the benchmark chart `p7.e15` (a call-sourced element, always NOT_AVAILABLE in the producer's trace), the layout, the chain, the adapters. Which tiers can read SPY and BIL in production is a matter of the resident's binding: the estate's Bloomberg history may not hold them, in which case Yahoo does.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-93` | `opal_producer.py`: the benchmark and risk-free resolve, the `named` series to the layout, the two statements, the settings; `tests/test_opal_producer_benchmark.py` (6 named tests); one assertion of `tests/test_opal_producer_prices.py` | those three files + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. No other cell of this round. The r32 release build (round 20) takes this cell if it merges before the release pin.

## Four-postulate record

(i) Domain: the two reference series the risk statistics need. (ii) One resolve, one pair of statements. (iii) One intent: beta, alpha, Sharpe and Sortino print, with their basis said. (iv) What this cut does NOT move: the layout, the map, the chain, any grant, any deployed byte.

fanout: 1 of 1 chain, cap 8, reason: one producer file, its new test file and one assertion of another; slot 195.
