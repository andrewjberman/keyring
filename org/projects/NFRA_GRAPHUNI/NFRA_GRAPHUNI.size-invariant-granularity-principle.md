# Size-Invariant Granularity Logic — foundational-logic candidate (grounded input)

**Provenance:** surfaced empirically by the NFRA_GRAPHUNI.P0 D1 audit (0.8.0_AE_CloudComp~D) + Andrew's fractal-layers direction, 2026-06-30. Andrew relayed it to MSTR (Tier-0) to be built into the fabric's FOUNDATIONAL logic — "too big to keep buried inside a TO." This artifact is the grounded INPUT + first articulation, extracted from the TO so it is no longer buried. **It is NOT Tier-0 authoring** — MSTR/CTO own the foundational/constitutional form; this hands up the principle + the empirical grounding + the invariants.

---

## The principle (one statement)
**The graph's node/edge TYPE SYSTEM and its INVARIANTS are invariant to scale.** Granularity ("size") is a **declared coordinate** — a `level` attribute on a stable `CONTAINS` ladder — **never a fork in the type system**. The same edge semantics, the same invariants, and the same tools operate at every zoom level. The logic is self-similar / fractal / **size-invariant**: it does not change as you zoom in (estate -> layer -> resource -> script -> function -> statement) or out.

## Why it is FOUNDATIONAL (not a project detail)
It is the property that lets **ONE graph + ONE toolset + ONE gate-set serve every granularity without per-level re-engineering.** It generalizes BEYOND GRAPHUNI/COMPUNIFY to the whole cognition substrate: any future depth (statement-level, row-level, a new cross-fabric stratum) inherits the type system + invariants *for free*. A substrate that is size-invariant is scale-free — you can keep diving deeper or zooming out and the same reasoning machinery (queries, tools, gates, seams) applies unchanged. That is a constitutional property of the substrate, not a feature of one pipeline.

## The grounded keystones (the fractal repeats — all verified live @ marker head)
- **compute:** `Pipeline ⊃ Script ⊃ Function ⊃ (statement)` via `CONTAINS`; `CALLS` / `READS_S3` stay stable across depth, disambiguated by `level`. (TraceGraph: 1,204 function nodes + 1,624 CALLS — the same types at script and function grain.)
- **storage:** `S3_BUCKET ⊃ S3Key ⊃ (object)` via `OWNED_BY`/`CONTAINS`. (Kuzu holds bucket grain; S3Key is the drilldown — CTO ruling 2.)
- **infra <-> compute (the cross-stratum seam):** `EC2_INSTANCE -RUNS-> PipelineScript`. Grounded keystone: the 31 EC2 nodes ARE the pipeline runners (`inf-gold-qa-runner`, `mdpf-daily-runner`, `cot-exporter`, `canonical-schwab-runner`, `inf-bronze-runner`, `bd-49f-auto-login`, ...); at resource grain they edge to `S3_BUCKET`, but the drilldown into their internal script sequence does not yet exist — that missing edge is the fractal seam.
- **proven precedent:** TSGRAPH already does this in the portal layer (`MS_FOLDER -CONTAINS-> MS_FILE`, `Module -DECLARES-> Component`, `TypeDecl -HAS_FIELD-> Field`, `Component -CONTAINS_DRILLDOWN-> sub`) — coarse->fine via STABLE edge types. The pattern is demonstrated, not hypothetical.

## The size-invariant contract (the invariants, for the gate)
1. **Granularity = a declared `level` coordinate** + a stable `CONTAINS` ladder. A deeper dive ADDS instances/levels within FIXED types — it never re-types by depth.
2. **Edge types defined ONCE by SEMANTIC, stable across grain.** Different relation/semantic -> different `edge_type`; SAME relation at different depth -> SAME `edge_type` + a `level` attribute; never split one semantic by depth, never overload one type across two semantics. (e.g. `READS_S3` != portal-field `READS` by semantic; `READS_S3` is ONE type whether the endpoint is a script or a function.)
3. **Grain-consistency rollup (checkable):** a coarse-grain edge must roll up from its fine-grain edges (`EC2 READS S3_BUCKET` <- `PipelineFunction READS_S3 S3Key` aggregated up `CONTAINS` + `OWNED_BY`). A drilldown that contradicts its rollup is a grain defect.
4. **One-home + non-redundancy hold at EVERY scale** (the COMPUNIFY `comp-coverage-check` gate, extended with the `level`/granularity dimension + the no-split-by-depth rule).

## The populate/govern split (why size-invariance makes the stack work)
- **GRAPHUNI POPULATES** the size-invariant substrate (one graph, one head, the drilldown ladders).
- **COMPUNIFY GOVERNS** the definitions (the node-schema gate enforces the contract above).
- **Tools READ** at the one marker head, each calibrated to a `level` (comp-aws=resource, comp-pipescript=script/IO, comp-blast/trace/xref=function, comp-platinum=cross-grain traversal).
Size-invariance is the property that makes that entire stack scale-free — add a level, the substrate, the gate, and the tools all extend without re-engineering.

## Routing
Handed UP to CTO -> MSTR as grounded foundational-logic input (LD/constitution class). The empirical anchor + the keystones + the invariants are the contribution; the Tier-0 institutional form is MSTR's to author. ~D continues the GRAPHUNI build (gold-tier-first population to the COMPUNIFY grain contract) on the CVO-fixture-gated P1 GO.
