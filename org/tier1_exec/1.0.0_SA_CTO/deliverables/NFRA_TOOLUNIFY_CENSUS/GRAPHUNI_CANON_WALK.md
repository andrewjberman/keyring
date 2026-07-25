# NFRA_GRAPHUNI CANON-WALK — intermediate-node canonicalization re-assert (final gate pass)

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T072855Z
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY · **boundary observed:** measurement only,
ingestion hard-gated.

**Prediction under test (CVO~Z's, on the record verbatim before this run — not mine, so the two-commit
provenance standard is satisfied by CVO~Z's own MCP message being the prior, immutable record):** *"the
gap shrinks again and class A largely dissolves. If it does NOT shrink, the producer has a real structural
deficit and non-viability comes back with actual grounding."*

---

## MEASURED, no smoothing: mixed result — the sharp case's gap did NOT shrink; the control target's did

```
CANON-WALK v3 VERDICT: SET-IDENTITY REFUTED 11/28   (aggregate unchanged from v2)
SHARP CASE (gold:D_01.partner_analytics):   old_n=216  new_n=228  missing=19   (UNCHANGED from v2's 19)
CONTROL (s3:gold/timeseries/client_performance.parquet): old_n=168  new_n=150  missing=36  (down from ~49 in v2)
```

**The sharp case's missing count is IDENTICAL to the pre-canonicalization v2 measurement (19 both times).**
The prediction does not hold here. **`new_n` went UP (200→228, +28)** — the glob bridge added 28 extra
nodes to this target's radius without closing any of the 19 gaps. **The control target DID improve**
(missing dropped from roughly 49 to 36) — a real, if partial, shrink.

## Method

**Normalization 1 — glob↔prefix, implemented as alias edges:** loaded the fixture's own pinned graph,
enumerated its 76 `{*}`-containing nodes (matches CVO~Z's count exactly). For each, computed a directory
stem (text before `{*}`) + extension (text after). For every producer S3 node whose canonicalized key
matches that stem+extension, copied all of its edges onto the glob-form id as well — so the existing,
unmodified BFS can traverse through a glob id transparently, as if the producer had emitted it directly.
**202 alias edges added across the 76 glob targets.**

**Normalization 2 — unqualified↔firm-qualified — checked, found ALREADY NATIVE, not newly built:** this
reconstruction's `un_s3_id()` strips the firm-prefix (`opal-data-<firm>/` → `s3:`) uniformly at
edge-construction time, for every S3 edge, terminal or intermediate — so a key written by one firm and
read by another already collapses onto ONE canonical node in this graph; there was no split node to bridge.
**Directly checked** on the `canonical_prices.parquet` convergence key: it has 16 writers in ONE node in
this reconstruction (confirms the collapse), but **none of those 16 carry the `INF_`-firm prefix
CVO~Z's own read expected** — meaning the specific `gold:INF_build_canonical_prices` write is simply
**not present in the producer's raw output at all**, independent of any firm-qualification issue. **This
narrows CVO~Z's "splits into two firm-qualified nodes" read**: that may describe the producer's raw,
pre-canonicalization JSON, but it is not what blocks THIS reconstruction's BFS — this reconstruction never
had two nodes to begin with.

## Interpreting the sharp case's non-improvement

Two candidate explanations, stated as candidates, not concluded:
1. **The glob bridge is over-broad, not under-broad.** A directory-stem match (e.g. everything under
   `silver/allocations/`) is a loose heuristic — it can connect the glob node to producer keys that share a
   directory but aren't the SAME real-world relationship the fixture's glob-edge represents. The `+28`
   extra nodes on the sharp case are consistent with this: the bridge added reachability, just not to the
   *right* 19 targets.
2. **The 19 missing members' actual blocking hop isn't a glob node at all, for this specific target.**
   Revisiting the chain-trace: only 1 of the 8 traced gold members' first-absent-hop was a
   `silver/allocations/{*}.parquet` glob hop (3 members shared it); the other classes (lambda-sourced,
   grain-mismatch) are untouched by a glob bridge by construction — this canon-walk pass doesn't touch
   those. **So even a perfect glob bridge could only ever have helped a subset of the 19**, and the
   measured zero movement suggests it helped none of them, consistent with explanation 1 (the bridge fired
   but landed on the wrong nodes) rather than "no glob nodes were in play here."

**Not resolved which explanation is right this pass** — flagged as the honest state, not smoothed toward
either.

## What this settles, per the dispatch's own two-outcome framing

The dispatch named both outcomes as decision-grade. **This measured outcome is closer to "does not shrink"
for the specific sharp case that has anchored this entire thread**, even though the control target
partially improved. **Per CVO~Z's own prior standard (a prediction should be judged on its demanding limb,
not its easy one) — the sharp case is the demanding limb here** (it's the target every other measurement in
this thread has been checked against), and it did not move. **Recommend reading this as evidence AGAINST
"class A largely dissolves" for the dominant, most-scrutinized target — though not as conclusive evidence
of producer non-viability either**, given the bridging implementation's own over-broad-vs-under-broad
ambiguity is unresolved.

## Denominator + honesty

Full 28-target aggregate re-run (100% of sample, not narrowed). Both named check-targets (sharp case,
control) run with full missing/extra member detail in the sidecar. 76/76 fixture glob nodes processed for
bridging, none skipped or sampled.

## What this lane did NOT do

Did not refine or tune the glob-bridge heuristic to test explanation 1 vs. 2 above (a tighter, filename-
pattern-aware match instead of a bare directory-stem match would be the natural next iteration — not
attempted this pass, named as a candidate follow-on, not started). Did not re-run comp-trace/comp-xref.
Did not wire anything into live ingestion.

## Files

| File | Role |
|---|---|
| `deliverables/NFRA_GRAPHUNI_REASSERT/canon_walk.py` | glob-bridge + re-assert script |
| `deliverables/NFRA_GRAPHUNI_REASSERT/CANON_WALK_result.json` | full 28-target result + sharp/control detail |
