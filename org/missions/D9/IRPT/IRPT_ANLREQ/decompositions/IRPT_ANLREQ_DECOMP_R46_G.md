# IRPT_ANLREQ round 46, workstream ~G (ENGINE) -- decomposition: the YCharts price tier in the resident (FWD-7, C-PRICES), scoped before it is built

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO msgs 9620 and 9694. r34g (round 45) turns `opal_pricing` ON with the tiers `[estate, yfinance]`; the CTO named the gap: C-PRICES' YCharts step before C-SWAP is missing, owed with item 4's count-per-window lease. msg 9620 placed the Opal-built report (FWD-7) as the next ENGINE cell after r34g, with its own decomposition.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The first cell is a read-only SCOPE, not a build.** What exists is known from the code: `ycharts/research/price_source.py` lists the chain `("estate", "yfinance", "ycharts")`, and `ycharts/research/price_adapter_ycharts.py` holds a YCharts price reader over an INJECTED transport (one `fund_data` call per symbol). What the resident builds is two tiers only (`reports/resident_installed.py`, `PRICING_TIERS`, `_pricing_extras`). Whether a transport over the resident's stored session and the provider lease can reach the Opal producer's process, and under which budget, is not known; building before reading it would guess. The scope record's `gaps` list decides the build cell's content.
- **The build cell (`AR-g-142`) is cut from the scope record**, by recut, once I have read it; the budget it takes is item 4's measured count per window (the paced read `AR-g-140`, applier IB2).
- **Item 4 (the lease count per window)** keeps its own cell, cut after the paced read reports.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-141` | `YCHARTS_PRICE_TIER_SCOPE.json`: every place a third price tier touches, with citations, and the gaps | the worker's folder only (read-only on `infra/`) | LOCAL (a record) |

## Edges and chains

- ONE chain now: `AR-g-141`. `AR-g-142` (the tier build) depends on it and on the paced read; the lease cell depends on the paced read.

## Four-postulate record

(i) Domain: the resident's pricing wiring and the YCharts price reader. (ii) One verifier (`ar_g141_checks.py`: citations real, five roles present, gaps a list). (iii) One intent: know what the third tier needs before building it. (iv) What this cut does NOT move: any product file, the lease, the bindings, the tiers.

fanout: 1 of 1 chains, cap 8, reason: one read-only worker cell (slot 268).
