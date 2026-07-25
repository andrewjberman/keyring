# NFRA_GRAPHUNI CHAIN-TRACE + cause-1 wiring spec — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch NFRA_GRAPHUNI CHAIN-TRACE (20260725T071845Z)
**Status:** COMPLETE (gold-subset scope, as ruled)

---

## Objective

For each PRESENT-UNREACHABLE gold-subset member (8 of the sharp case's 13), walk the fixture's own
seed-to-member shortest path and name the first hop absent from the producer's reconstructed edge set —
per CVO~Z's hypothesis that the break clusters at a shared upstream hop rather than being per-member.
Parallel: a short design spec (not a build) for wiring the 6 deterministically-absent `lambda:` members.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `python3` (chain_trace.py) | BFS parent-pointer path reconstruction on the fixture's pinned graph, first-absent-hop check against the producer reconstruction | PASS (TRUE_RC=0) | 8 members collapsed to 5 distinct hops |
| `python3` (spot-check) | verified the `canonical_prices.parquet` convergence point directly against the raw producer JSON | PASS | found 16 correct writer edges from other sources, pinpointing the grain-mismatch finding rather than assuming total absence |

**What worked:** reconstructing BFS parent pointers (not available directly from
`TraceGraph.downstream()`/`upstream()`'s return shape) let me walk an exact path rather than just confirm
reachability — a small addition on top of the existing v2 harness rather than a new build.

**What failed:** nothing outright.

**Gap found:** two distinct patterns in the collapsed hop set — glob/wildcard-form S3 keys, and a
script-vs-function grain mismatch on a convergence point — neither fully root-caused to a specific source
line this pass, named as open rather than guessed at.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

Traced all 8 gold-subset `PRESENT-UNREACHABLE` members' shortest fixture-graph paths from the seed,
checked each hop against the v2 reconstruction's edge set, found the first absent one per member. Result:
8 members → 5 distinct first-absent hops (real but partial collapsing, not the single shared hop CVO~Z's
strongest reading predicted). Two named clusters: (1) glob-form S3 keys (`{*}` in the key), 2 of the 5
hops; (2) a convergence point (`s3:silver/prices/canonical_prices.parquet`) where 3 of the 5 hops all
target the same key — checked directly against the raw producer JSON rather than assumed, and found this
key is NOT wholly missing (16 correctly-emitted writer edges from other scripts exist) — the 3 traced
sources are specifically missing, one because it's `lambda:`-sourced (the exact mechanism cause 1 already
names — first evidence in the thread that cause 1 and cause 2 are not fully independent), one confirmed as
a script-vs-function grain mismatch (the function-level equivalent write IS present), one not yet resolved.

Delivered the cause-1 wiring spec in parallel: a short design shape (new small pass over the
already-in-memory `build_graph()` output, a distinct marker field, additive join at ingestion) — spec only,
nothing built, sizing input for CVO~Z's closure ruling.

Delivered `GRAPHUNI_CHAIN_TRACE.md` + sidecar to the census dir.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Define "the path" explicitly as fixture-graph BFS-shortest, state the definition in the memo | "The path" is otherwise ambiguous (the fixture's own traversal order isn't directly recoverable); a stated, reproducible definition is more useful than an implicit one. |
| Check the `canonical_prices.parquet` convergence point directly rather than assume "missing" | The initial pattern (3 hops, same target) could have meant the key is wholly unextracted; checking found the opposite (16 correct edges exist) — a materially different, more precise finding. |
| Name the cause-1/cause-2 overlap explicitly rather than let it sit implicit in the data | CVO~Z's framing treated the two causes as fully independent; finding one concrete case where they're not is a real correction to that framing, not a detail to bury. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_CHAIN_TRACE.md` | New — trace + spec memo | No — CTO~Z's BASE_EXEC lane |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_CHAIN_TRACE.sidecar.json` | New — full path detail | No — same |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/chain_trace.py` + result | New — path reconstruction script | Yes — own lane |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_graphuni_chain_trace_and_cause1_spec.md` | This log | Yes |

---

## Blockers

None. Ingestion stays hard-gated; cause-1 is a spec only, not landed.

---

## Current State

Chain-trace delivered for the gold subset as ruled. Two named, distinct failure clusters (glob-keys,
grain-mismatch-at-a-convergence-point) plus one concrete cause-1/cause-2 overlap case. Cause-1 wiring spec
delivered in parallel, unbuilt. `s3:`-subset and control-target tracing explicitly not done this pass —
named as remaining scope, not silently dropped. Reported to CTO~Z + CVO~Z this turn.

---

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the chain-trace method and the two named clusters; decide whether the
   `s3:`-subset trace is worth running before sizing closure, given the gold subset already shows more
   structure than "one shared hop." Size the cause-1 spec.
2. **[1.0.0_SA_CTO~Z]** Commit the deliverable; route whether the glob-key / grain-mismatch findings get
   their own follow-up trace.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
