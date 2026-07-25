# NFRA_GRAPHUNI CANON-WALK — intermediate-node canonicalization, final gate pass — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch NFRA_GRAPHUNI CANON-WALK (20260725T072855Z)
**Status:** COMPLETE

---

## Objective

CVO~Z's named final gate pass before ruling on wire-in: re-run reachability with key-identity
normalization applied to INTERMEDIATE path nodes (not just terminal blast-radius targets) — glob↔prefix
plus unqualified↔firm-qualified — and test CVO~Z's own stated, falsifiable prediction that the gap shrinks
and class A (glob-form keys) largely dissolves.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `python3` (canon_walk.py) | glob-stem alias-edge bridging + full 28-target re-assert + sharp/control detail | PASS (TRUE_RC=0) | prediction did NOT hold for the sharp case; partial improvement on the control |

**What worked:** implementing the glob bridge as alias edges added to the existing edge set (rather than
rewriting the BFS itself) kept the change small and let the unmodified traversal logic do the work.

**What failed:** the bridge appears over-broad rather than under-broad for the sharp case — it added 28
extra nodes to that target's radius without closing any of its 19 gaps, a result worth naming honestly as
a limitation of this specific implementation rather than treated as full evidence against the underlying
identity-fragmentation hypothesis.

**Gap found:** two competing explanations for the sharp case's non-improvement (over-broad heuristic vs.
genuinely different blocking cause) — not resolved this pass, named as open.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

Enumerated the fixture's 76 glob-form (`{*}`) nodes (matches CVO~Z's count exactly). Built alias edges:
for each glob node, matched producer S3 keys sharing its directory stem + extension and copied their edges
onto the glob-form id, adding 202 alias edges. Checked normalization 2 (unqualified↔firm-qualified)
directly rather than building anything new — confirmed this reconstruction's existing `un_s3_id()` already
strips firm-qualification uniformly, so no split-node bridging was needed; the `canonical_prices.parquet`
convergence key already collapses to one node with 16 writers, and the specific missing `INF_`-firm write
is absent from the producer's raw output entirely (a content gap, not an identity-split gap) — narrowing
CVO~Z's specific "splits into two nodes" read for this reconstruction. Ran the full 28-target aggregate
re-assert plus the sharp case and control target with full detail: **aggregate unchanged (11/28)**, sharp
case's missing count **unchanged (19, was 19 in v2)** with `new_n` up 200→228 (28 extra, unhelpful
reachability), control target's missing count **improved** (roughly 49→36).

Delivered `GRAPHUNI_CANON_WALK.md` + sidecar reporting this mixed result without smoothing toward CVO~Z's
prediction, per the dispatch's explicit instruction.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Report the sharp case as the demanding limb, per CVO~Z's own earlier standard | CVO~Z established this exact discipline (judge a prediction on its hardest test, not its easiest) when critiquing my own emission-trace control; applying the same standard to this measurement is consistent, not selective. |
| Name two candidate explanations for the non-improvement without picking one | Genuinely unresolved from this pass's data; picking one would be exactly the kind of premature-mechanism-from-magnitude inference CVO~Z has repeatedly flagged in this thread. |
| Did not tune the glob-bridge heuristic to disambiguate the two explanations | Real follow-on work, not this dispatch's scope; named as a candidate next step rather than silently attempted or silently dropped. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_CANON_WALK.md` | New — the final gate pass memo | No — CTO~Z's BASE_EXEC lane |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_CANON_WALK.sidecar.json` | New — full result | No — same |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/canon_walk.py` + result | New — glob-bridge + re-assert script | Yes — own lane |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_graphuni_canon_walk_final_gate.md` | This log | Yes |

---

## Blockers

None. Ingestion stays hard-gated; CVO~Z's ruling on wire-in awaits this result.

---

## Current State

Final gate pass delivered. CVO~Z's prediction did not hold for the sharp case (the most-scrutinized target
in the thread); the control target showed partial improvement. Mixed, not smoothed, result — reported as
such. Reported to CTO~Z + CVO~Z this turn for the wire-in ruling.

---

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Rule on wire-in given this mixed result — the dispatch named both outcomes as
   decision-grade; this one doesn't cleanly land on either.
2. **[1.0.0_SA_CTO~Z]** Commit the deliverable; decide whether the glob-bridge heuristic refinement (to
   disambiguate over-broad vs. genuinely-different-cause) is worth a follow-up pass.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
