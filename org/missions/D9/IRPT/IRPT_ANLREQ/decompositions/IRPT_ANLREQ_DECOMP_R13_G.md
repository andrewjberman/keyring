# IRPT_ANLREQ round 13, workstream ~G (ENGINE) -- decomposition: the filer's report variant reaches the Opal engine's map

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the engine compose read `AR-g-54` (`deliverables/0.9.0_WK_IRPT_ANLREQ~173/r7/ENGINE_COMPOSE_READ.json`, `q3` the variant selection and its smallest change), the ticket stamp `AR-g-67` (merged `c11be0ffdb`, which already changed the same two product files), CTO msg 8377, PRD v0.15 FWD-7 (the Comparison and Multi-Comp variants).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Where the variant lives.** The read named a change to `resident_worker.run_opal` (carry the variant in `request_ref`). Reading the code instead: the accepted record does not hold the variant, and the only resident-side source of it (`frozen.recipe_inputs`) is the vendor path, which refuses an UNRESOLVED row since `AR-g-68`; an Opal job must not read it. The variant is therefore stamped on the record at the accept step, where the validated `comparison_keys` are in hand, and `opal_stores(principal, record)` reads it from the record it is already given. `resident_worker.py` and `opal_producer.py` are untouched; `request_ref` is a closed shape and is left alone.
- **Backward compatibility.** A record accepted before this change carries no `report_variant` and is an overview; `load_map` is called with no argument for an overview, so every existing zero-argument test double stands.
- **Honest failure until the release.** The Comparison and Multi-Comp maps are pinned into the package by the release cell (r32), not here. Until then a Comparison or Multi-Comp record on the Opal path refuses `OPAL_MAP_BINDING_REQUIRED` rather than rendering an Overview for a filer who asked for another report.
- **Two existing tests change by exactly the new key** (`test_acceptance_actor.py`, `test_commentary_requested_member.py`, plus the JSON the second one regenerates). Found by running the reference build against the 65-test regress guard: they failed, and are now named in the order's `<paths>`.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-85` | `acceptance.py` stamps `report_variant`; `resident_installed.py` selects the pinned map by it; 13 named tests in two new files; two existing tests edited by the one key | the six product files named in the order + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. Later cells of this workstream that touch other files (the map statistic fix, the compose into `opal_producer.py`, the IAM leg, the release r32) are cut after their own reads.

## Not moved by this cut

Any deployed byte; `build_resident_package.py` and the bindings (the release cell's); `resident_worker.py`, `opal_producer.py`, any map; the YCharts-field tables of the Comparison and Multi-Comp maps (NOT_AVAILABLE: no vendor call).

## Four-postulate record

(i) Domain: the three variants the composition derives from the comparison count (0, 1, 2 or more). (ii) One stamp, one selection. (iii) One intent: the asked variant reaches its map. (iv) What this cut does NOT move: any pin, any deployed byte, the engine's rendering of a map.

fanout: 1 of 1 chain, cap 8, reason: one small change across two product files and their tests; slot 185.
