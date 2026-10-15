# IRPT_ANLREQ round 23, workstream ~G (ENGINE) -- decomposition: the backend swap pass, its pool builder and its Yahoo history port

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** PRD v0.14, v0.18 and v0.19 (C-SWAP): every UNRESOLVED holding enters a backend pass that replaces it from a class-matched pool (the longest Yahoo history wins, ties by ticker), records the substitution and names it in the report; the filer is never asked. CTO msgs 8711, 8714 and 8723 (ADDENDA 4, 5, 6): the pool is a DATED SNAPSHOT shipped in the resident package (ticker, asset_class, sub_asset_class only; claim `held`; `pool_as_of` on every swap record; older than 30 days still swaps and says so; no IAM change); a holding with no class and no replacement is named "not analysed; Opal Staff will manage the replacement" and never blocks the run (the model classifier is its own cell and pair after run 3; agent-curated classes are refused); the r34 packet states the swap's Yahoo calls per holding and their bound.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Three modules, three seams, no shared file.** `swap_pass.py` (the pass and the pool reader) and `build_swap_pool.py` (the snapshot builder) are cell `AR-g-98`; `yahoo_history_days.py` (the history port) is cell `AR-g-99`. They meet only through two plain contracts: the pool file's schema `irpt-swap-pool.v1`, and the `history_days(ticker)` callable with an optional `prefetch(tickers)` (the same request size, 50, is written in both, and `AR-g-100`'s tests assert the two constants equal). Wiring (the producer reads UNRESOLVED rows, runs the pass, prices and classifies the replacement, writes the swap records and disclosures) is round 24 (`AR-g-100`), the resident release packaging (`AR-g-101`) round 25 or later.
- **The class of the missing security** comes from a port (`classify`, the resident's classifier over `etf-classifications`, whose role holds `GetItem` only) or from the pool itself; there is no model step. Read live 2026-10-15: BREIT, SREIT, KPEC and TIMXX have NO row in `etf-classifications`, so run 3's unpriceable holdings take the "not analysed" branch (CTO ADDENDUM 6, option b). Stated so nobody reads a green swap check as "run 3 swaps BREIT".
- **Yahoo's cost.** A class of n candidates costs ceil(n / 50) batched monthly requests per swapped holding (the port prefetches the class once); `build_swap_pool.py` prints the largest class and the per-holding bound from the snapshot it builds, for the r34 packet. A failed request is never cached or read as "unpriced": `choose_replacement` records it as `HISTORY_ERROR` and the swap record counts dropped reasons.
- **Record fields.** `proxy_for`, `proxy`, `status`, `method`, `confidence`, `low_confidence`, `sources`, `pool_as_of`, `pool_claim`, `pool_stale`, `candidates_priced`, `dropped_reasons`, `merged`, `named` (+ `history_days` or `why`): C-SWAP (5)'s list plus the pool vintage the CTO required. No amount is ever in a record.
- **`low_confidence` is False** for every swap in this cut: the class-match-and-history rule has no confidence score; the model path that would set it is the later classifier cell.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-98` | `ycharts/research/swap_pass.py` (pool reader, the pass, the record), `ycharts/research/build_swap_pool.py` (the snapshot builder), thirteen named tests in two files | the four files named in the order + the worker's folder | WORLD (floor of an infrastructure path; new source and tests only) |
| `AR-g-99` | `ycharts/research/yahoo_history_days.py` (the batched history port), six named tests | the two files named in the order + the worker's folder | WORLD (same) |

## Edges and chains

- TWO independent chains (no shared file, no import between them). Both feed `AR-g-100` (round 24), which edits `ycharts/research/opal_producer.py` and imports both. Neither is imported by anything yet, so neither moves a deployed or resident byte.

## Four-postulate record

(i) Domain: the swap pass's inputs (UNRESOLVED rows, a pool file, a class lookup, a history port) and outputs (rows, records); the pool file's six schema checks; the port's cases. (ii) One pool schema, one record shape, one request size. (iii) One intent per module: choose and place (98), build the snapshot (98), fetch history (99). (iv) What this cut does NOT move: `swap_replacement.py`, the producer, the resident bindings and builder, the door, the classifier, any deployed byte.

fanout: 2 of 2 chains, cap 8, reason: two disjoint new modules with no import between them; slots 199 and 200.
