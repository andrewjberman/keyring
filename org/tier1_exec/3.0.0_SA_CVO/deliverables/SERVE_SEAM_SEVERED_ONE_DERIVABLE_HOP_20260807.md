# The serve chain is severed at exactly one derivable hop — you cannot trace a served API endpoint to the bucket that fills it

**Seat:** `3.0.0_SA_CVO`. **Date:** 2026-08-07 ~00:45Z. Andrew-directed drive on the C2/C3.i thread.
**Every figure below is a live `comp-kuzu` query. Read-only.**
**Follows:** `STAGE1_SIDE_DERIVATION_MEASURED_20260807.md` (6,686 instances, 0 cross-side).

## The chain, and where it breaks

```
endpointurl:/api/general/mdpf/aggregate-aua-timeseries.json     layer=portal   [FRONTEND]
        |
        |  SERVED_FROM                      <- the ONLY edge type crossing the serve boundary
        v                                      (28 edges; 0 edges cross the other way)
opal-data-assets                                layer=aws      [BACKEND]
        node_type = S3_BUCKET_POLICY
        outbound edges: ZERO                 <- TERMINAL NODE. The traversal dies here.
        |
        X  MISSING EDGE
        |
arn:aws:s3:::opal-data-assets                   node_type = S3_BUCKET
        EXISTS in the graph, fully connected onward to S3Key / producers / pipelines
```

**The policy node's `node_id` IS THE BARE BUCKET NAME.** The bucket's is `arn:aws:s3:::<name>`.
**The missing hop is string concatenation.**

## Measured

| | |
|---|---|
| `SERVED_FROM` edges (portal → aws) | **28** |
| edges crossing aws → portal | **0** |
| `S3_BUCKET_POLICY` OUTBOUND edges, any type | **0** — terminal by construction |
| `S3_BUCKET_POLICY` INBOUND | 28, all `SERVED_FROM` |
| policies with a derivable `S3_BUCKET` (`'arn:aws:s3:::' + node_id`) | **11** |
| **seam edges that WOULD reach a real bucket** | **28 of 28 — all of them** |

**The served URLs are live client-facing product surfaces**, not test fixtures:
`/api/general/mdpf/aggregate-aua-timeseries.json` · `/api/general/portfolios/aum-metrics.json` ·
`/api/general/portfolios/aum-timeseries.json` · `/api/general/market/all_returns.json` ·
`/api/general/trending/latest.json`

## What this costs, stated plainly

>> **YOU CANNOT TRAVERSE FROM WHAT A CLIENT SEES TO WHAT PRODUCED IT.** A blast radius from
> `aum-metrics.json` reaches a policy node and stops — it never reaches the bucket, the S3 keys, the
> gold script that writes them, or the pipeline that runs it. **The producer→consumer chain, which is
> the question comp-blast exists to answer, is severed at the frontend boundary in every one of its
> 28 instances.** <<

This is why the estate reads as two disconnected halves and why every C2 motif is single-side: **it is
not that backend and frontend are unrelated — it is that the one modeled connection between them
terminates on a node with no outbound edges.**

## Why nothing caught it

Three independent instruments each returned a *true* answer that concealed it:

1. **`comp-blast`** on a `ServedURL` returns a radius that terminates at the policy — **correct, and
   it looks like the end of the chain rather than a break.** Its `WARNING: affects >= N` counts the
   policy as reached, so nothing reads as missing.
2. **The C2 catalog** has no detector for `SERVED_FROM` (0 occurrences; positive control `OWNED_BY`
   = 4), so no motif instance ever spans the seam — which I measured yesterday as
   *"0 cross-side instances"* and could easily have read as *"the halves are genuinely separate."*
3. **The graph itself** models the edge honestly. **`S3_BUCKET_POLICY` is a real AWS object and
   `SERVED_FROM` is a real relationship.** Nothing is wrong; a hop is simply absent, and an absent
   hop has no error state.

**No instrument was broken. The gap lives between them**, which is the class this seat exists for.

## Remedy — small, and NOT mine to land

**One derived edge**, at derive time, from data already present:
```
(S3_BUCKET_POLICY {node_id: N}) -[GOVERNS|POLICY_OF]-> (S3_BUCKET {node_id: 'arn:aws:s3:::' + N})
```
- **28 of 28 seam edges connect immediately**; 11 distinct buckets.
- The edge TYPE is a naming act → **Andrew/CTO**, not me. I have deliberately not chosen between
  `GOVERNS` / `POLICY_OF` / `APPLIES_TO`.
- Belongs in the graph derivation (`derive_runner`), owned by the graph lane — **routing to
  `1.0.0_SA_CTO~D` alongside the grain-overlap and vertical-join specs**, since it is the same
  substrate and the same seam those two exist to cross.

**And it makes the seam detector real:** with the hop present, a `serve-boundary` C2 detector over
`SERVED_FROM` yields **the estate's first cross-side motif instances** — `[BACKEND, FRONTEND]`,
28 of them, each one a client endpoint traceable to its producing pipeline. **That is precisely the
c3.i↔c3.ii bridge F1 was specified to watch**, and today it has neither an edge nor a detector.

## Scope discipline

**I did not add the edge, and I did not write the detector.** Both are the graph lane's, the edge
type is a naming act, and I hold the verification seat. **Measured, recorded, routed.**

-- `3.0.0_SA_CVO`
