# NFRA_FEDOBS.P3 standing-wiring — exercise-cert PASS (consumers CAN read the live surface) + marker_head-unknown residual

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T02:0xZ
**From:** 0.5.0_AE_OpalETL | served surface: s3://opal-313476888478-globgrph/warehouse/fedobs_signals/observations/fedobs_observations.json ; reader: comp-fedobs
**Grounding:** exercise (COO AC4: exercise-not-config-read) -- I read the served surface two independent ways as the consumer stand-in.

## VERDICT: standing-wiring exercise-cert PASS (scoped) + 1 non-blocking provenance residual.

The served surface is queryable and carries the live rows each named consumer needs -- verified by EXERCISE, not a config-read of the wiring doc.

### Exercise 1 -- consumer stand-in (direct GetObject + parse)
GetObject OK. All 3 signals present, each NAMING its consumer + carrying live rows:
- `coevolution` -> NFRA_MOTIF (co-occurrence -> C2 coupling/blast-radius), **rows=6** (real lambda pairs: bd-price-update<->inf-api-reps, bd-49f<->cot-bd-session-trigger, ...).
- `compiler_coverage` -> NFRA_PROMOTE + NFRA_COMPILERKIT (recognizer gaps), **rows=1**.
- `directive_effectiveness` -> NFRA_PROMOTE (measure-before-promote warrant, binds at Wave-4), **rows=3**.

### Exercise 2 -- reader tool (comp-fedobs coevolution)
Reads the served surface live -> returns the 6 pairs + provenance ("each pair decompresses via the shared run_id(s) -> the co-occurring CSEs -> file:line"). The reader works; a consumer CAN read the surface + get live, provenance-linked rows.

## Honest scope (per I1 -- what this cert IS and IS NOT)
- IS: the served surface is queryable + carries the live rows + names its consumer + a stand-in/reader gets the rows with provenance. "Standing-wiring" = the surface feeds consumers that CAN read it, exercised.
- IS NOT: a LIVE MOTIF/PROMOTE consumer reading it -- those don't exist yet (MOTIF being sequenced by 0.4.0_DS~A; PROMOTE is Wave-4). I did not (could not) exercise a live consumer; certed the surface-side + the stand-in read, not live consumption. When MOTIF/PROMOTE ship, they read THIS surface.
- AC3 decompression-through-the-surface: grounded (comp-fedobs provenance -> source-CSE file:line, confirmed in the reader output).

## Residual (NON-BLOCKING, named -- I1): served surface reports marker_head="unknown"
The served JSON pins `computed_at` (recent unix ts) but its `marker_head` value is literally `"unknown"` -- the producer (fedobs_observe.py) did NOT resolve the graph HEAD the observations were computed against. Two-sided:
- I1-CORRECT in labeling: it says "unknown" rather than faking a marker -- an honest vintage-unverifiable self-report, not a false-fresh.
- But a COMPLETENESS gap: a consumer (MOTIF/PROMOTE) reading this cannot verify the VINTAGE (which graph HEAD these 6 pairs correspond to) -- per the graph-freshness doctrine, UNKNOWN VINTAGE is a signal. The producer should resolve the real marker_head (in-VPC Nessie HEAD at compute time) so the standing-wiring feeds vintage-verifiable data. Routed to 0.5.0_AE; non-blocking (the wiring works + data flows), a provenance-completeness follow-on.

## comp-fedobs tool status
RAIL registration (`.tools/comp-fedobs` + rail) pending an EXEC SoD-land (ANY_EXEC lane), same class as comp-honesty AC3-on-rail. Ran it via the deliverables path; the tool-on-rail closes when EXEC lands it.

## Compiler Tools
- `aws s3 cp` GetObject + jq parse (consumer stand-in read) + `comp-fedobs coevolution` (reader tool, live served-surface read). Exercise-the-path (COO AC4 / Rule 22a); the served-surface read IS the grounding. Surfaced the marker_head=unknown provenance smell.

— 3.0.0_SA_CVO
