# IRPT_ANLREQ round 14, workstream ~G (ENGINE) -- decomposition: the price stage in the Opal producer

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the engine compose read `AR-g-54` (`ENGINE_COMPOSE_READ.json` q4: the price seam, the swap seam, the pricing-flag seam), the chain core `AR-g-70` (`price_source.py`), the series builder `AR-g-63` (`portfolio_series.py`), the four adapters `AR-g-81` to `AR-g-84` (merged `dc80bdd32c`, `5058a29160`, `eecb6d8aa8`, `3cb1344c88`), CTO msg 8377, PRD v0.15 C-PRICES.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The seam is narrower than the read's.** The read put the price result "as a kept-shaped answer and as the benchmark and risk_free arguments". Building the reference showed that only the `portfolio_level_series` call feeds a computed element (`OWN_SERIES`); a call-sourced element that is NOT computed (the series' last date, the benchmark chart, the snapshot metrics) is always NOT_AVAILABLE in the producer's trace (`_entry` passes an empty kept dict). So the page is built with an EMPTY kept dict, so that the page and the trace agree, and only the computed elements print a value. The benchmark and risk-free arguments stay `None` in this cut: beta, alpha, Sharpe and Sortino read `INPUT_MISSING:risk_free` or `INPUT_MISSING:benchmark`, which is true and in the closed reason set.
- **Only the price call is kept in the map's budget.** Keeping every call name (the read's smallest change) would turn the roughly 60 vendor-sourced elements from NOT_IN_THIS_VERSION into INPUT_MISSING; keeping the one call the stage supplies leaves them as they are.
- **Claims.** The sources are the chain's own tier names (`estate`, `yfinance`, `ycharts`); `replaced` joins when the swap cell lands. They sit in `run.json` `prices.symbols[..].source` and in the document's `effective_inputs.settings.price_sources`, both free objects (schema read: `settings` has no `additionalProperties`, `disclosure_id` is a free string), so no schema change.
- **Named omission.** An unpriced symbol makes the first disclosure `UNPRICED`, in words; the run completes and the series covers the priced share (the coverage is recorded).
- **Window.** Ten years to `as_of` (T-1). The YCharts reader takes `zoom=max` and the Yahoo reader `period=max`, so the window only cuts.
- **Where `as_of` and the readers come from** is the wiring cell's: `stores` keys here, set by nobody yet. Every caller keeps today's output until then.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-86` | `opal_producer.py`: `_opal_map(pricing)`, `_start_of`, `_price_stage`, the pricing branch of `produce` and `produce_package`; `tests/test_opal_producer_prices.py` (10 named tests) | those two files + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. `AR-g-85` (merged `002a88bdc3`) edits other files; no overlap.

## Cut after this one (each with its own read or reference and checks)

1. The wiring: `make_opal_stores` extras / the resident assembly set `pricing`, `price_readers` (the four adapters over the host's clients) and `as_of` (the T-1 date; `lib/trading_calendar.py` is not in the resident tarball, so the date is handed in or the module joins the package list in the release cell).
2. The swap: `swap_replacement.choose_replacement` for the MISSING symbols (a class-matched pool and a Yahoo history length need a pool source: the registry rows) with source `replaced` and the replacement named in the report.
3. The benchmark and risk-free series (a symbol decision for the CRO), the YCharts-snapshot elements computed from the portfolio series, and the map statistic defects p2.e08, p2.e13, p6.e22.
4. The ONE resident release r32: this seat's, with the CTO's two additions (msg 8568): `irpt-anlreq-x10-v1` in `additional_policy_revisions` with its pinned test, and run 3's producer address `fwd1-staff-r41b@opal.invalid` in place of `r41a` (`~Y2` msg 8570).

## Four-postulate record

(i) Domain: the C-PRICES chain applied to the holdings of one report. (ii) One stage, one place (`produce` and `produce_package` share it). (iii) One intent: the figures that need prices are valued, or say why not. (iv) What this cut does NOT move: any deployed byte, the layout, the chain core, the adapters, the wiring, the swap, the benchmark.

fanout: 1 of 1 chain, cap 8, reason: one stage in one product file and its test file; slot 186.
