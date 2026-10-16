# IRPT_ANLREQ round 48, workstream ~G (ENGINE) -- decomposition: the resident's YCharts price tier and the host's call-budget binding

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** round 46 scoped the third price tier (`YCHARTS_PRICE_TIER_SCOPE.json`, AR-g-141, 51 cited rows, 7 gaps). CTO msgs 9727, 9757 and 9761: build the four code gaps offline-tested in its own r34h pair; ONE per-window call budget per host, shared by the door's lookups, the price tier and the SPY/BIL calls; the budget is (6 calls, 390 s), a floor not the limit, counts every `securities_info` call (an unknown symbol costs two), and is set in the bindings. Round 47 (AR-g-142 the lease budget, AR-g-143 the resolve-hop requeue) holds the mechanism; this round holds the resident side, which needs `ResidentSession(window_budget=)` from AR-g-142.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **One cell, one new module.** `AR-g-144` edits `reports/resident_installed.py` (the tier list, the optional `ycharts_window_budget` binding and its validator, `_pricing_extras(..., session=None)`, `build_resident_runtime` passing the budget to the session and the session to the pricing extras) and adds `ycharts/research/price_transport_ycharts.py` (the stored-session transport the existing `price_adapter_ycharts` reader calls). The reader itself is not changed.
- **A refusal over the budget is that tier's ERROR, not a failure.** `price_source._ask_tier` records an exception as `ERROR:<name>`; the symbol then falls to the backend replacement (C-SWAP) or is reported unpriced in words (FWD-7). The pricing stage does not wait out the window.
- **The budget NUMBER lives in the bindings.** The r34h build sets `ycharts_window_budget` to (6, 390); the code has no default.
- **Three items stay unmeasured and are named, not guessed:** the YCharts id form for a plain ticker, the served single-ticker shape, and whether the price route answers a signed-out caller. They are measured by a read-only applier order AFTER window 4 (CTO msg 9727 condition 2); the cell uses the session-bearing acquire.
- **Round 48 is its own round** because the gate allows one issuance per round per workstream and round 47 is issued.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-144` | the `ycharts` tier, the budget binding and its validator, the transport module, the runtime wiring; tests | `reports/resident_installed.py`, the new `ycharts/research/price_transport_ycharts.py`, `test_opal_pricing_binding.py`, two new test files, the worker's folder | WORLD (infra path; nothing deployed) |

## Edges and chains

- ONE chain. `AR-g-144` depends on `AR-g-142` (merged before the worker's branch is cut). It does not depend on `AR-g-143`.
- The r34h release (tier, budget binding, lease, resolve requeue, plus whatever the unknown-symbol read adds) follows once 142, 143 and 144 are merged and the budget number is in the bindings.

## Four-postulate record

(i) Domain: the resident's bindings, pricing extras and runtime wiring, and the stored-session price transport. (ii) One check file (`ar_g144_checks.py`), dry-run against a reference fix and five mutants. (iii) One intent: the third price tier under the host's one budget. (iv) What this cut does NOT move: the lease (round 47), the resolve hop, the door, the price reader, the existing tiers, any deployed byte.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 271) after AR-g-142.
