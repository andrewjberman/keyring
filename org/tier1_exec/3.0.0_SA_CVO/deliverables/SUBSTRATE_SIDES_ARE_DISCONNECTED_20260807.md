# The substrate_sides do not connect: BACKEND and FRONTEND are two components joined by one dead end

**Serial:** 3.0.0_SA_CVO · **2026-08-07** · **FINDING, not a build.** The serve-seam edge is on this
pass's CUT LIST and nothing here builds it.

## Why this was measured

Andrew's north star, verbatim: *"lock in these deterministic relationships and coverage as substrate
**across the substrate_sides**."* Auditing DONE-MEANS item 3 (`substrate_side` **multi-valued**) I
found that on live data it never is:

| | |
|---|---|
| C2 motif instances | 6,138 |
| purely BACKEND | 5,137 |
| purely FRONTEND | 1,001 |
| **MULTI-VALUED (BACKEND+FRONTEND)** | **0** |
| `side_status` | RESOLVED 6,138 / 6,138 |

The multi-value path is implemented and mutation-proven, but **zero live instances exercise it**, so
on real data it is indistinguishable from a single-valued field. That could be a detector-scope
artifact or an estate fact. Those are distinguishable, so I distinguished them.

## The measurement (whole graph, not detector-scoped)

Over `layer IN (aws, pipeline, portal)`; `aws`+`pipeline` = BACKEND, `portal` = FRONTEND.
`ms` (KNOWLEDGE, 5,851 nodes) is excluded — no detector reaches it, and including it would mix a
coverage fact into a connectivity one.

```
portal   -> portal      16784
aws      -> aws          3808
pipeline -> pipeline     2957
pipeline -> aws           573
aws      -> pipeline      248
portal   -> aws            28   <- CROSS-SIDE
                         -----
same-side edges          24370
CROSS-SIDE edges            28
```

**All 28 cross-side edges are the serve seam**, confirmed by shape rather than by matching counts:

```
ServedURL --SERVED_FROM--> S3_BUCKET_POLICY    28    (the ONLY cross-side shape)
distinct target nodes                           1    (opal-data-portal-v2)
onward edges from those targets                 0
```

## What it means

**THE TWO SUBSTRATE_SIDES ARE DISCONNECTED COMPONENTS.** Every edge in the estate stays on its own
side except 28, and those 28 terminate immediately at a single node with no outbound edges. There is
**no traversable path from any frontend node to any backend node**, in either direction.

So the zero multi-valued instances are **not a detector gap**. A motif is a path; a path cannot span
the sides because no spanning path exists. No detector, however written, could produce a
cross-side instance against this graph.

**This is the gap between the current state and the north star.** "Substrate across the
substrate_sides" presumes the sides are joined. Today the axis is well-formed and its two halves
never meet — `substrate_side` correctly *labels* both sides while nothing *crosses* between them.

## The remedy is one edge, already routed

`S3_BUCKET_POLICY 'opal-data-portal-v2'` → `S3_BUCKET 'arn:aws:s3:::opal-data-portal-v2'`.

Both endpoints already exist, so this is an **edge-creation act, not a node-creation act**, and the
target id is derivable (`'arn:aws:s3:::' + policy.node_id`). Independent corroboration from a
different derivation (1.0.0_SA_CTO~C): **7 of 7** `aws_s3_bucket_policy` blocks in Terraform declare
their bucket via a first-class HCL resource reference, while the graph carries zero such edges — so
the relationship is absent from the GRAPH, not from the ESTATE.

Pending with Andrew as a usage confirmation (via CTO~C): `GOVERNS` is already ratified
(`NFRA_ONTOLOGY_RULE_BANK.yaml:144`, *"D3: narrow policy/authority"*) and currently zero-live —
CTO~C source-confirmed at `:146` that its bound token was **re-pointed to `OWNS`** in the 0.4→0.5
bump, which is why it sits vacant. That explains the vacancy, not the occupant; whether policy→bucket
belongs in it is Andrew's call.

## AMENDED — the finding was UNDERSTATED: `ms` is a fully isolated island

Found by `0.7.0_AE_CloudOps` closing the gap this doc had explicitly flagged as *"ms excluded and
NOT assessed"*, and **re-derived here rather than accepted**:

```
ms cross-layer edges, BOTH directions:  []      (zero rows)
ms node count:                          5,851   (28% of the graph, 2nd-largest layer)

POSITIVE CONTROL, same query shape on `portal`:
  semctl -> portal   1512
  portal -> aws        28
  -> the control FIRES, so the ms zero is a MEASUREMENT, not a broken query
```

`portal` at least has a thin (dead-ended) bridge of 28. **`ms` has none at all.** Any motif requiring
an `ms`↔anything path yields zero *structurally*.

**The blast radius is larger than portal's, and the wrong diagnosis is more available.** Post-landing,
a reader doing the obvious sanity check — *"5,851 ms nodes and zero ms motifs, something is broken"* —
reaches the wrong conclusion with apparently excellent evidence. The discriminating question is never
*"is the reader dropping layers"* but *"does a spanning path exist"*, and it is already measured: no.

AE's reason for verifying rather than filing is worth preserving, because it applies to this whole
document: **a pre-registered structural explanation is the right thing to publish before the evidence
exists, and it is also the most dangerous kind of claim to accept unchecked — "that's structural" is
unfalsifiable once everyone believes it, and would become a ready-made excuse for a REAL frontend
defect.** It therefore needed an independent derivation. AE queried cross-LAYER connectivity rather
than `substrate_side`, so their check does not inherit this doc's side mapping. It holds on both.

*Note on `semctl`: it carries 1,512 edges to `portal` and is the layer the C2Motif/C3System nodes
themselves occupy. It cannot bridge the sides in this model — `side_of()` returns None for `semctl`
by ruling (`01_substrate.md:39`, semctl is not a substrate), so it contributes no side and creates no
cross-side path. Recording it so the 1,512 is not later mistaken for a bridge.*

## Denominators and limits, stated

- Connectivity is measured over the **whole graph**, not the detector scope — it is not limited by
  detector coverage. Instance counts ARE detector-scoped (1,103 of 6,138 carry no catalog anchor).
- Scope of the ORIGINAL measurement was `aws`/`pipeline`/`portal`. **`ms` has since been
  assessed (see the amendment above): ZERO cross-layer edges, positive-controlled.** The
  limit this line originally declared is now closed rather than outstanding.
- **One edge restores traversal for all 28 served URLs.** An earlier statement of mine —
  "28 of 28 seam edges would reach a real bucket" — counted traversals restored and reads as 28
  missing edges. It is one. Corrected to CTO~C before it reached Andrew.
- Whether a *reconnected* graph would actually yield multi-valued instances is **UNTESTED** — it
  depends on whether any detector query traverses that shape. Do not read this as a promise that the
  count becomes non-zero; it removes the structural impossibility, nothing more.

-- 3.0.0_SA_CVO
