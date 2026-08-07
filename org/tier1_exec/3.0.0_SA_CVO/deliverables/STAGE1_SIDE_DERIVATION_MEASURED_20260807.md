# Stage 1 side-derivation, measured: 6,686 instances, ZERO cross-side — and the serve seam has no detector

**Seat:** `3.0.0_SA_CVO`. **Date:** 2026-08-07 ~00:20Z. **Andrew-directed** ("do it").
**Method:** ran each canonical detector's OWN query against the live graph, rewriting only the
`RETURN` clause to yield each constituent's `layer` instead of its `node_id`. **Read-only; nothing
composed, nothing written.** Harness: `stage1_sides.py`.
**Basis:** the generator's own semantics — `recurrence += len(rows)  # each matched path row = one
instance of the idiom` (`NFRA_MOTIF_P1_canonical_ab_catalog.py:188`).

## The measurement

```
TOTAL MOTIF INSTANCES        6,686          (vs 19 class nodes today)
CROSS-SIDE INSTANCES             0  (0.0%)
  BACKEND                    5,680 (85.0%)
  FRONTEND                   1,006 (15.0%)
```

Per-detector instance counts reproduce the generator's `recurrence` values (a-store 232, a-api 82,
b-struct 1623, b-run 248, b-io 573, b-dataflow 956, a-orch 28 — exact; a-access/a-grant differ by
~2-5% because the graph advanced since 07-18). **That agreement is the control that the rewrite
preserved the detectors' semantics.**

## Finding 1 — `AServeMotif`'s cross-side span is a BUNDLING ARTIFACT

At **class** grain `AServeMotif` spans two substrates and looked like the estate's one serve-seam
motif. At **instance** grain it resolves as:

```
a-serve   instances=59   cross-side=0   {FRONTEND: 50, BACKEND: 9}
```

It is a **compound detector with two subqueries** (`:107-119`) and neither crosses:

| subquery | shape | sides |
|---|---|---|
| CDN-serve | `(CLOUDFRONT_DISTRIBUTION)-ORIGIN\|USES_OAI->(S3_BUCKET)` | aws → aws — **BACKEND only** |
| FE-serve | `(DataFetch)-IS_ENDPOINT->(Endpoint)-READS_URL->(ServedURL)` | portal → portal — **FRONTEND only** |

>> **THE CLASS SPANS TWO SIDES ONLY BECAUSE IT BUNDLES TWO SINGLE-SIDE SUB-SHAPES UNDER ONE NODE.**
> The "spanning" is an artifact of the class grain the whole materializer thread is about — **it
> disappears the moment instances are individuated, which is itself an argument for individuating
> them.** <<

## Finding 2 — THE SERVE SEAM IS ONE EDGE TYPE, AND NO DETECTOR MATCHES IT

Every edge crossing the boundary, both directions:

```
aws|pipeline -> portal :  0 edges                                    (zero rows)
portal -> aws|pipeline : 28 edges, ALL SERVED_FROM
                          ServedURL -SERVED_FROM-> S3_BUCKET_POLICY
```

**`SERVED_FROM` appears 0 times in the 13-detector catalog** (positive control: `OWNED_BY`, a verb
that IS used, appears 4 times — so the search works).

>> **THE ONLY STRUCTURAL CROSSING OF THE SERVE BOUNDARY IN THE ENTIRE ESTATE IS 28 `SERVED_FROM`
> EDGES, AND NOTHING LOOKS AT THEM.** That is why cross-side instances are zero — **not because the
> seam is absent, but because the one edge type that constitutes it has no detector.** <<

**This is precisely what F1 exists to watch.** The friction battery's stated purpose is bridging
c3.i↔c3.ii to find risk surfaces on the semantic plane; **the literal bridge is 28 unmatched edges.**
A `serve-boundary` detector over `SERVED_FROM` is therefore the highest-value missing detector in the
catalog — it is small, it is unambiguous, and it is the only shape that can ever produce a cross-side
instance under the current graph.

## What this does NOT say

- **Not that the frontend is disconnected.** It is connected through `SERVED_FROM` and through
  application-level calls the graph does not model as edges. **The graph's edge vocabulary is the
  limit here, not the estate's architecture.**
- **Not that a cross-side detector would find many instances.** 28 edges is the ceiling today.
- **Not a defect in the generator.** It is `tier: canonical, plane: A|B` and never claimed to cover
  the seam. **The defect is that nothing declares the seam uncovered.**

## Method note — my parser dropped exactly the rows that mattered, and a cross-check caught it

The first run reported `a-serve instances=50` and **0 cross-side**. The generator's recurrence for
a-serve is **59**. That 9-row gap is the only reason I did not publish.

Cause: `comp-kuzu` sizes its table rule to the column width, so a **single-digit count renders as a
one-character rule** (`---  ---  -`). My row-detector required `-{2,}` per column and rejected the
whole line, returning `[]` **with no error**.

>> **IT SILENTLY DROPPED EVERY RESULT WHOSE COUNT WAS 1-9 — I.E. EXACTLY THE RARE COMBINATIONS, WHICH
> IS WHERE A CROSS-SIDE INSTANCE WOULD LIVE.** A false "0 cross-side" was the natural output of that
> bug, and it agreed with my prior. **What caught it was not the parser and not the result — it was
> the disagreement with a known-good number produced by someone else.** <<
Fixed to `-+` per column; a-serve then reports 59, matching exactly.

-- `3.0.0_SA_CVO`
