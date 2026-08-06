# C2 detector coverage: 38.4% of the graph — and the frontend's ONLY motifs are its defects

**Seat:** `3.0.0_SA_CVO`. **Date:** 2026-08-06 ~2355Z.
**Andrew-directed:** *"Check the generator code and make sure that it covers ALL structural motifs in
the graph, not debt-focused or otherwise filtered."*
**Answer: IT DOES NOT.** Measured, not read.

## The measurement

Generator: `NFRA_MOTIF_P1_canonical_ab_catalog.py` (589 lines) — **13 detectors, 9 plane-A + 4 plane-B.**
Universe: the canonical kuzu graph.

```
DENOMINATOR                      20,585 nodes across 58 node_type(s)
COVERED by the 13 A+B detectors   7,908 nodes (38.4%) across 21 type(s)
UNCOVERED                        12,654 nodes (61.5%) across 35 type(s)
```

**The uncovered 61.5% is not residue. It is two coherent planes plus an AWS tail.**

| uncovered | nodes | |
|---|---|---|
| `MS_FILE` | 4,758 | **M365 plane — ZERO detectors of any kind** |
| `MS_FOLDER` | 1,053 | same |
| `JSXElement` | 2,205 | **frontend interior — ZERO detectors of any kind** |
| `JSXRender` | 1,433 | same |
| `TypeDecl` | 807 | same |
| `ReactComponent` | 442 | **covered ONLY by a DEBT motif, 8 of 442** |
| `Module` / `Prop` / `Hook` / `PanelCluster` / `ReactQueryKey` | 374 / 359 / 111 / 91 / 57 | none |
| `LOG_GROUP` / `SECRET` / `SECURITY_GROUP` | 238 / 82 / 24 | **plane-A tail, uncovered** |

## The inversion — this is the part that matters

Which motifs touch frontend types at all:

```
AServeMotif     (canonical)  -> DataFetch 50 · Endpoint 48 · ServedURL 45
DeadComponent   (DEBT)       -> ReactComponent 8
OrphanEndpoint  (DEBT)       -> Endpoint 8
```

**One canonical motif reaches the frontend's SERVING EDGE. The frontend's INTERIOR — 5,000+ nodes of
JSX, render trees, components, hooks, props, type declarations — is touched by NOTHING canonical, and
by exactly two DEBT detectors covering 16 nodes.**

>> **THE CANONICAL ONTOLOGY'S OWN LAW IS `population_law: canon-first-debt-subset` — *"a debt motif is
> a shadow; this file is the object."* FOR THE FRONTEND PLANE THAT IS INVERTED: THE SHADOW IS ALL
> THERE IS.** The estate's entire frontend structural layer is represented exclusively by eight dead
> components and eight orphan endpoints. **Not "under-covered" — structurally unrepresented, and what
> little exists describes only what is broken.** <<

## Why this was invisible

The generator is honest about what it is: `tier: "canonical"`, `plane: A|B`, and its commit says
*"canonical A+B motif catalog (13 detectors, 9A+4B)."* **It never claimed to be complete.** The
incompleteness only becomes a defect when a consumer reads `C2Motif` as *the* motif population —
which is exactly what F1 would have done, and what my own grain-overlap spec assumed.

**Nothing in the graph carries the coverage boundary.** A query returns `C2Motif` with full
provenance and no marker that 61.5% of the estate has no detector pointed at it.

## What this changes for the materializer build

1. **The population is not just un-individuated, it is PARTIAL.** My spec's Stage 1 said "emit one
   node per match." **Matches only exist where detectors do.** Individuating today's matches yields a
   complete instance layer over 38.4% of the estate — and it would *look* complete.
2. **A COVERAGE DENOMINATOR IS MANDATORY ON EVERY EMISSION.** `composed N instances over M nodes in
   detector scope, of T nodes in the graph`. Without the third figure the layer reports its own
   completeness dishonestly. **This is the same law as F1's `K of N` — you cannot read a numerator
   without the universe it came from.**
3. **New detector planes are a real build, and they are NOT mine to scope.** A frontend plane (C?) and
   an M365 plane are ~59% of the graph between them. **Whether they are wanted, and what shapes are
   canonical there, is a naming/ontology act → Andrew.** I am recording the gap, not proposing the
   catalog.
4. **F1's denominator inherits this.** `structures_touched: K of N` over a 38.4% substrate is a real
   figure about a partial estate. **That must be declared in F1's `boundary_declaration` as
   `address_space`, or F1 silently reports blast reach over the AWS+pipeline planes only.**

## Method note

Two query errors caught in the run, both the same class and both worth recording:
`comp-grep` **warned me** that my escaped-BRE pattern (`\|`, `\(`) is treated literally by Python `re`
and that a 0-match *"may be this, not a real absence"* — **it was**, and the warning is why I did not
record a false absence for the generator. And `MATCH (a)-[e:CONTAINS]->(b)` failed with *"Table
CONTAINS does not exist"* — edge_type is a PROPERTY, not a label, the same trap CTO~B hit on
`C3System` an hour earlier. **Both instruments failed loudly. Neither returned a clean zero.**

-- `3.0.0_SA_CVO`
