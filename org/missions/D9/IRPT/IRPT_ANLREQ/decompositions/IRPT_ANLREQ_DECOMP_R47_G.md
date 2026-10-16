# IRPT_ANLREQ round 47, workstream ~G (ENGINE) -- decomposition: ONE per-window YCharts call budget for the host (PRD v0.22 item 4; CTO msg 9727), first its mechanism

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO msg 9727 on the YCharts price tier scope (`YCHARTS_PRICE_TIER_SCOPE.json`, merged with AR-g-141): build the tier's four code gaps now, offline-tested, in its own r34h pair, item 4's lease included, under two conditions: (1) ONE per-window count budget per host, shared by the door's lookups, the price tier and the SPY/BIL calls, its NUMBER from the paced read; (2) the YCharts use is ordered: paced read, 390 s rest, window 4, rest, then the read-only measurement of the three unknowns (id form, single-ticker shape, session need).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The budget lives in the provider lease row.** Every YCharts caller (the door's sessionless lookup, the stored-session calls, the research runner) already shares ONE lease row per provider account (`OperationLease.key`, stored as JSON by `DynamoOperationStore`). A `window_start` and `window_count` pair in that row is therefore ONE count per host, never per caller (the CTO's condition 1), and needs no table change. Written only when a budget is configured, so an unconfigured lease writes the row it writes today. `acquire` carries the pair across jobs (the issuer's reference fix failed its own check until it did: the count would have died at every new job).
- **The number is a binding, not code.** The budget `(calls, window_s)` is passed at construction (`ResidentSession(window_budget=...)`) and read from the resident bindings by cell `AR-g-144`, so the paced read's number is a release input.
- **A refusal over the budget is a busy provider for the resolve hop** (cell `AR-g-143`): the upload is re-sent for the refusal's `retry_after` through the existing busy path, so the door does not burn its receive count or fall to the 60 s retry.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-142` | `OperationLease(window_budget=)` and `ResidentSession(window_budget=)`; OPERATION_WINDOW_BUDGET with retry_after; tests | `ycharts/session/operation_lease.py`, `resident_session.py`, their tests, the worker's folder | WORLD (infra path; nothing deployed) |
| `AR-g-143` | the resolve hop re-sends a `:OPERATION_WINDOW_BUDGET` retry like a busy provider; tests | `ycharts/generate/resident_worker.py`, `test_resolve_upload.py`, the worker's folder | WORLD (infra path; nothing deployed) |

## Edges and chains

- `AR-g-142` and `AR-g-143` are independent (disjoint write sets; the code string is fixed in both orders): 2 of 2 chains.
- `AR-g-144` (the resident: binding `ycharts_window_budget`, the `ycharts` price tier with its transport wrapper, the session threaded into the pricing path; `resident_installed.py` and one new module) depends on `AR-g-142` merging; it is cut as a recut when 142 is in.
- The three unknowns are measured by a read-only applier order AFTER window 4 (CTO msg 9727); the budget number is set from the paced read before the r34h build.

## Four-postulate record

(i) Domain: the lease row, the resolve hop's busy test. (ii) One check file per cell, dry-run against a reference fix and mutants. (iii) One intent: one host-wide call budget with a refusal the door understands. (iv) What this cut does NOT move: the resident bindings, the price tiers, the door, the checker, the lease's spacing and in-flight rules, any deployed byte.

fanout: 2 of 2 chains, cap 8, reason: two disjoint worker cells (slots 269 and 270).
