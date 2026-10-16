# IRPT_ANLREQ round 25, workstream ~G (ENGINE) -- decomposition: the resident installer supplies the swap store

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO ADDENDA 4 and 5 (msgs 8711, 8714): the swap pool is a dated snapshot SHIPPED in the resident package, pinned by content like the maps, with no IAM change; the resident r34 carries it. Round 23 merged the swap pass, the pool builder and the Yahoo history port; round 24 (in flight) wires the Opal producer to an optional `swap` store.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The installer mirrors the pricing binding.** An optional binding `opal_swap_pool` `{path, sha256}` selects the pool file; absent, no `swap` store is supplied and the producer refuses an UNRESOLVED holding as it does today (r32 as applied is in this state). The store is built PER JOB (the pin is re-read, the run date is the clock's UTC date), so a replaced pool needs a new pin and an old pool is stale-flagged by the day, not by a restart.
- **The pool ships through the release tooling, not through the repo builder.** The r34 build uses the issuer's release-tool copy of the builder (as r32 did), which adds the pool member and the bindings key; this cell does not touch `build_resident_package.py`.
- **Not claimed:** a host with the `yfinance` library (the first real read is the r34 apply's smoke read; a missing library degrades to candidates dropped as HISTORY_ERROR, never a wrong replacement).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-101` | `reports/resident_installed.py` (the binding's validation, `_swap_extras`, `make_opal_stores(swap_extras=)`, the call in `build_resident_runtime`), six named tests in one file | the two files named in the order + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. Depends on `AR-g-98` and `AR-g-99` (merged) and on the swap store contract that `AR-g-100` (round 24) consumes; it imports nothing from `opal_producer.py`. The r34 release (build, pair, apply) follows `AR-g-100` and `AR-g-101`.

## Four-postulate record

(i) Domain: the installer's bindings and the stores it hands the Opal producer. (ii) One binding shape, one store shape. (iii) One intent: supply the swap store. (iv) What this cut does NOT move: `opal_producer.py`, the builder, the bindings file, any deployed byte.

fanout: 1 of 1 chain, cap 8, reason: one installer file and its tests; slot 203.
