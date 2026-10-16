# IRPT_ANLREQ round 44, workstream ~G (ENGINE) -- decomposition: yfinance first, YCharts second (PRD v0.22) -- the door, the trace of the YCharts-id dependencies, then the pacing

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO msg 9522 and PRD v0.22 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` section v0.22, Andrew-direct ~15:2xZ; CRO research `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261016_YCHARTS_PACING_AND_YFINANCE_FIRST.md`): (1) the door asks yfinance first and YCharts only for a symbol yfinance does not keep; (2) `opal_pricing` ON in the release that carries (1); (3) trace every YCharts-id dependency left in report generation and remove it in the same release, or name the one remaining call with its count; (4) the door lease counts per window, budget from one measured read. One resident release, its own pair (r34g). AR-g-129 (r34f) stays the fallback and ships first (round 43).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Item (1) is cell `AR-g-133`.** `intake/security_resolution.py`: `SecurityResolver.check` with a checker asks it ONCE for every uncached symbol (and for a cached provider NOT_FOUND, as today); a KEPT symbol never reaches the provider; the rest go to the provider in one call; a provider FOUND beats a NOT_KEPT; a provider NOT_FOUND after a NOT_KEPT stays NOT_FOUND with no second checker call; CHECK_FAILED and NOT_CHECKED symbols the provider does not find read UNAVAILABLE with the same reason words as today. `verified_suggestions` shows a candidate the checker KEPT as well as one the provider FOUND (otherwise a "Did you mean" hint Yahoo keeps would vanish). The resident wiring already passes the real checker (`ycharts/session/resident_session.py:149`), so no wiring changes.
- **The checker's per-upload cap (10, `yfinance_check.py:185`) is NOT changed in this cell.** Beyond it a symbol reads NOT_CHECKED and goes to YCharts, which is today's meaning. Raising it is a Yahoo-pushback question for the packet, named there.
- **Item (3) is cell `AR-g-134`, a read-only trace**, because its answer decides what the removal cell contains. Its record is a JSON trace (each dependency with `path:line`, the line's text, whether a Yahoo-priced holding needs the id, the id source and what removes it, a claim word). The removal cell (`AR-g-135`) is cut by recut once the trace is read; the spec of the rest is frozen.
- **Item (2) is a build flag**, not a product cell: the r34g build driver sets `"opal_pricing": {"enabled": true, ...}` (`reports/build_resident_package.py:119` is the builder's default). The issuer's tooling cell; it moves only if the trace says pricing cannot be turned on without the removal.
- **Item (4) waits on its measurement.** `AR-g-136` (the lease window) is cut after AQ2's paced read (six lookups about 90 s apart after a 390 s rest, then six about 5 s apart) is in hand; I ask `~Y2` for the door first so the read does not spend run 3's window.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-133` | the door asks yfinance first (above) with tests | `intake/security_resolution.py`, its test files, the worker's folder | LOCAL (code and tests; nothing deployed) |
| `AR-g-134` | `YCHARTS_ID_TRACE.json`: every YCharts-id dependency in report generation | the worker's folder only (read-only on `infra/`) | LOCAL (a record) |

## Edges and chains

- `AR-g-133` and `AR-g-134` are independent chains (disjoint write sets, no data edge): 2 of 2.
- `AR-g-135` (removal) depends on `AR-g-134`; `AR-g-136` (lease) depends on AQ2's read; both are later cuts of this round.

## Four-postulate record

(i) Domain: the door's resolver (`check`, `verified_suggestions`) and the report-generation call sites that need a YCharts id. (ii) One check file per cell. (iii) One intent: Yahoo first. (iv) What this cut does NOT move: the checker (its rule, cap and pacing), the provider port, the cache keys and TTLs, the swap pass, pricing code, the lease, the release tooling.

fanout: 2 of 2 chains, cap 8, reason: two disjoint worker cells (slots 265 and 266).
