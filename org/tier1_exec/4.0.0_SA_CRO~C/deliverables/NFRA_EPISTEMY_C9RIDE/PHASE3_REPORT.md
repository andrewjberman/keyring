# C9-RIDE Phase 3 — proto-Observation_Records from the landed atom_layer0 bundles (PROPOSED)

**Seat:** 4.0.0_SA_CRO~C · **TO:** NFRA_EPISTEMY.C9-RIDE (COO, GO 63646) · **Slot:** parallel to Batch 4,
per base 64140 · **Emitter:** `scripts/phase3_emit_proto_records.py` · **Artifact:**
`phase3/PHASE3_PROTO_RECORDS.json`

## What it does

Each atom_layer0 run is an **instrument invocation** whose return is a bundle. This emitter converts every
landed bundle into an Observation_Record against ~A's Component-1 envelope — making this seat the
envelope's **first live data source** rather than a competing evidence path (the TO's stated purpose).

**Cited, never copied:** the envelope schema (`observation_record.schema.json`), PRD §2.1, base's A5
ruling (63827), the hybrid interim axis (63662/63664). No schema was widened and no field invented.

## Denominators (printed, from the run — not recalled)

| | |
|---|---|
| bundles landed → records emitted | **36 → 36** |
| envelope-valid | **34 / 36** |
| substantive KNOWN / UNKNOWN | **34 / 2** |
| interim `DERIVED_FROM_BUNDLE` | 36 |
| interim `ACQUISITION_FAILED_NO_BUNDLE` | **29 — from the PROGRAM MANIFEST's queue, never the run set** |
| reproducible | two runs at one HEAD, byte-identical (`f07930a487f3123f`) |

## The shape the envelope forced, reported rather than worked around

**F-C1-01 — the sidecar is not a choice.** The envelope is `additionalProperties: false` over a closed
14-field required list, so the pre-envelope axes the TO requires (`stage_class`, `interim_status`) **cannot
live inside a valid record**. Each artifact is therefore two parts: an envelope-valid `observation_record`
plus a declared `pre_envelope` sidecar. Rider (c) asks the interim shape be declared *in the artifact* —
satisfied at artifact level, not record level, and routed as a field question.

**F-C1-04 — the envelope cannot represent a decomposed subject.** `population_predicate` is required
non-empty, but a `DECOMPOSITION_FOUND` run has **no population at its own grain**: S3 legislation is
correctly not assessed because the population belongs to the children. The sequence's two such runs (**C3**
and **Territory**) are emitted **envelope-INVALID on purpose** and counted. Inventing a predicate string to
pass the schema would be precisely the fabrication the honest-populability audit forbids. Remedy is base's
call: make the field nullable with a declared absence semantic (the S6 0.1.1 pattern — *null = population
belongs to the children*), or declare decomposed subjects out of the envelope's domain.

Worth separating: this is **independent of** the Territory stage-state item base ruled at 63827. Even with
`s3 = STAGE_CORRECTLY_EMPTY` (which would stop A5 firing UNKNOWN), `population_predicate` would still be
null and the record still invalid.

**F-C1-02 — `plane` is one value per record; a run can span two.** Most bundles read repo text (DESIRED);
Runs 25/26/33/35 additionally measured the live graph (APPLIED). These records declare **DESIRED** — the
plane each certificate's scope is bounded to — and the live-graph limb stays visible in
`traversal_residue` rather than being folded silently into one plane.

**F-C1-03 — A5 is what makes PRD §2.1 survive contact with this instrument.** Applied literally to
`stage_states`, the governing rule ("any absent/failed status ⇒ UNKNOWN") would render *every* production
bundle UNKNOWN, because `s5` is NOT_ASSESSED by design. Both computations are printed side by side so a
reader can see they agree on the acquisition axes and differ only on the method stage.

## Bind-time condition: discharged, measured

CTO's condition (via base 63746) barred any consumer from parsing or keying off a fused `plane` until ~A's
amendment landed. Measured at the schema pin: **`plane` is a ratified enum and `substrate` is its own
field**. Nothing here splits a fused string.
