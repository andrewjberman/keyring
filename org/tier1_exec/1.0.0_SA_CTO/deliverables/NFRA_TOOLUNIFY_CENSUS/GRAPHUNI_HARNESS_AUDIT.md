# NFRA_GRAPHUNI HARNESS-AUDIT — reconstruction pipeline reconciliation (the pre-committed final pass)

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T073908Z
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY · **pre-committed outcome structure (both branches
named by the dispatch itself):** audit CLEAN → 19 is real, producer ruled NON-VIABLE, chain terminates.
Audit finds unaccounted drops → affected numbers re-measured ONCE, that number rules.

---

## VERDICT: **AUDIT CLEAN. Every raw edge is accounted for by a named, intended reason. Zero unaccounted
loss.**

```
TOTAL RAW EDGES: 3609   ACCOUNTED: 3609   MATCH
DROP-COUNT BY REASON:
  CONTAINS-skip (intentional -- not a TraceGraph/fixture edge type): 1362
  unmapped-source (un_pipeline_id failed): 0
  unmapped-target (un_s3_id/un_pipeline_id failed): 0
  kept (survives into the graph): 2247
DUPLICATE (source,target,type) triples before add_edge: 0
```

`1362 + 0 + 0 + 2247 = 3609` — exact. No silent loss anywhere in the pipeline: not at the `CONTAINS`
filter, not at either canonicalization function, not at node pre-population, not at `add_edge` dedup.

## Positive control: `s3:silver/prices/canonical_prices.parquet` — my count (16) holds; CVO~Z's count (18)
does not, checked directly

```
GRAPH writers into the key: 16
RAW-JSON writers that SHOULD survive (un_pipeline_id + un_s3_id both succeed): 16
MISSING FROM GRAPH despite surviving both transforms: 0
```

**Disagrees with CVO~Z's 073716Z count of 18 (with `gold:INF_build_canonical_prices` named as one of the
18 survivors).** Checked this specific disagreement directly and exhaustively — not by re-running my own
pipeline again, but by dumping **every single edge in the raw producer JSON with
`pipeline:inf:gold:INF_build_canonical_prices` as source, any edge type**: 30 edges total, all `CONTAINS`
(internal function structure) or `CALLS` (internal call graph), plus **exactly one `READS_S3`** edge
(`opal-data-bd/silver/historical_prices.parquet`). **Zero `WRITES_S3` edges from this id, to this key or
any key, anywhere in the raw JSON.** The producer genuinely never emits a write from this script to
`canonical_prices.parquet` — my original count and my harness's behavior are both correct on this specific,
now-exhaustively-checked case.

**Not asserting CVO~Z's count was wrong for a different reason (a different target, a different
canonicalization) — only that the specific claim (this id, this key, present as a `WRITES_S3` source) does
not hold under direct, exhaustive inspection of the raw JSON,** which is the most primitive, least-derived
evidence available (no transform, no reconstruction, just the file's own edges filtered by source string).

## What this means for the chain

Per the dispatch's own pre-committed structure: **the audit is CLEAN.** No unaccounted drops exist to
re-measure against. **19 (the sharp case's missing-member count, stable across v2, the emission trace, the
chain trace, and canon-walk) is real** — it is not an artifact of this reconstruction harness losing edges
it shouldn't. The pre-commitment's own language names the consequence: the producer would be ruled
NON-VIABLE, chain terminated, no further passes.

**I am reporting the audit result, not self-issuing that ruling** — consistent with this thread's
established pattern (CVO~Z/CTO~Z hold the ruling authority; this lane reports the grounded measurement).
The CVO~Z-18-vs-my-16 disagreement is surfaced explicitly, with the most primitive evidence I could produce
for it, so it can be checked independently before the ruling lands — a clean audit result that rests on a
disputed sub-claim would be a shakier foundation for "producer ruled NON-VIABLE, no further passes" than
one where the dispute is resolved or at least fully exposed.

## Denominator + honesty

All 3609 raw edges in the fresh `--full` producer artifact accounted for, none sampled. The positive
control was checked at the most primitive evidence level available (raw JSON, string-matched, zero
transforms) specifically because two prior independent counts (mine: 16; CVO~Z's: 18) disagreed and a
third derived-from-transforms count would not have settled which one has a bug.

## What this lane did NOT do

Did not re-run the affected numbers (audit is clean, so the dispatch's "re-measure once" branch does not
apply). Did not rule non-viability myself. Did not resolve WHY CVO~Z's independent count differs from mine
— named the disagreement and grounded my own side of it exhaustively, but did not speculate about what
went wrong in CVO~Z's reproduction (their own re-check, not mine to diagnose from outside).

## Files

| File | Role |
|---|---|
| `deliverables/NFRA_GRAPHUNI_REASSERT/harness_audit.py` | instrumented reconciliation script |
| `deliverables/NFRA_GRAPHUNI_REASSERT/HARNESS_AUDIT_result.json` | full drop-count + positive-control detail |
