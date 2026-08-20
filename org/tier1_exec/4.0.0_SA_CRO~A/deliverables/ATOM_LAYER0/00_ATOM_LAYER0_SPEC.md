# atom_layer0 specification

**Version:** 0.1.0-proposed, 2026-08-20
**Author:** 4.0.0_SA_CRO~A
**Status:** PROPOSED; no gate, registry entry, or canonical naming act is created here.
**Authority:** Andrew-direct founding record at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260820_ATOM_LAYER0_PROGRAM.md`.

## 1. Product definition

`atom_layer0` is a mechanical method for testing whether a concept can serve as a
declared conceptual base. It separates four acts that are often collapsed:

1. characterize the candidate concept;
2. search for an admissible decomposition;
3. certify only the bounded frontier that was actually exhausted;
4. define how every adjacent or higher layer resolves to the resulting authority.

The method never proves metaphysical indivisibility. Its strongest output is:

`ATOMIC_WITHIN(decomposition_grammar@version x scope)`

The atom is where decomposition explicitly stops, not where nobody has yet split.

## 2. Package boundary and sources of record

- `schemas/atom_layer0_run.schema.json` is the structured source of record for a run.
- `rule24/SCHEMA_ENUMERATION_RECORDS.json` is the source of record for every enum,
  outcome array, and predicate authored or adopted by this package.
- `skill/atom-layer0/SKILL.md` is the portable entrypoint.
- `skill/atom-layer0/references/` holds conditional workflow detail.
- `scripts/validate_run.py` validates the schema and the method's cross-field laws.
- `templates/atom_layer0_run.template.json` is a non-authoritative fill-in instance.

Prose explains the method. It does not duplicate member sets owned by the structured
sources. Where prose and schema disagree, the schema wins and the prose is the defect.

### 2.1 Resolution-census input seam

The run schema accepts `source_census_row` directly. To compile one `~B` row into an
unassessed but valid run bundle:

`python scripts/validate_run.py --compile-census-row <row.json> --output <run.json>`

| Census row field | atom_layer0 field |
|---|---|
| `row_id` | `run_id` provenance |
| `surface` + `concept` | default run scope |
| `concept` | `subject.concept` |
| optional `claimed_content` | `subject.definition` |
| optional `declared_layer` | `subject.claimed_layer` |
| optional `declared_grain` | `subject.declared_grain` |
| optional `scope` | `subject.scope` |
| `vintage` | run evidence vintage |
| `verdict`, `verdict_schema`, `evidence_pointer`, `candidate_owner` | preserved unchanged in `source_census_row` |

The census verdict is intentionally opaque to this package and carries its external
schema pointer. `atom_layer0` does not copy or reinterpret `~B`'s verdict array. Missing
concept definition, layer, or grain remains null until S0 assesses it; the compiler does
not manufacture ontology from a resolution finding.

## 3. Core predicates

### 3.1 Admissible decomposition

A proposed split is admissible only when all of the following hold:

- every child is normalized to the subject's declared grain;
- at least two children are independently instantiable or falsifiable;
- the parent can be reconstructed from the children by exactly one declared operator:
  `CONJUNCTIVE_DECOMPOSITION` or `DISJUNCTIVE_DECOMPOSITION`;
- the split changes a decision, failure direction, remedy, authority, or resolution
  obligation at that grain;
- the children are not merely synonyms, examples, properties, evidence fields, or
  causal antecedents of the parent.

The predicate is deliberately stricter than "the definition contains several words."
A complex description can still name one concept; a short name can hide several.

### 3.2 Atomicity certificate

An atomicity certificate exists if and only if:

- the splitter result is `DECLARED_FRONTIER_EXHAUSTED`;
- every production in the versioned grammar was exercised by a differently-derived
  splitter over the declared scope;
- the normalized candidate frontier is empty;
- no required instrument is unknown or unreachable;
- the run prints its grammar version, scope, grain, evidence vintage, and residue.

Failure to find is not frontier closure. Budget exhaustion, instrument failure, and an
unavailable independent splitter all terminate in an honest lesser state.

### 3.3 Resolution

A binding resolves if and only if it reaches exactly one live authority member at the
declared grain, its pointer resolves at HEAD, the target carries the claimed content,
and any code surface cites the authority rather than re-declaring its vocabulary.
Mechanical, declarative, and semantic seam checks must all pass. Resolution is a
predicate over one binding, never an impression about a document.

## 4. Workflow

The method runs S0-S5. These are stages, not new estate gates.

| Stage | Purpose | Structured output |
|---|---|---|
| S0 | Pin concept, claimed layer, grain, authority, consumers, and molecule-style characterization | `s0_pin` |
| S1 | Run declared generators, normalize candidates before union, and print generator residue | `s1_sweep` |
| S2 | Exercise the splitter against the versioned grammar and render one typed terminal result | `s2_challenge` |
| S3 | If and only if S2 closes, attach the Rule 24 record, population predicate, denominator, and token census | `s3_legislation` |
| S4 | Declare and test one resolution contract per binding layer on all three seam axes | `s4_resolution` |
| S5 | Run one externally selected, cheap real subject; expose and repair at least one method defect | `s5_proving` |

Every stage carries one of the package's stage states. `STAGE_NOT_ASSESSED` residue is
printed even when empty. `STAGE_UNREACHABLE` is never treated as a completed run.

Detailed execution and halt rules are in
`skill/atom-layer0/references/workflow.md`.

## 5. Splitter challenge

The splitter is a challenge control on a universal claim. It is differently derived
from the concept author or the generator set it challenges. It attempts to produce a
concrete admissible decomposition at cite-don't-gesture specificity.

Terminal results are the exact five-member array defined and tested in the Rule 24
record:

- `DECOMPOSITION_FOUND`
- `DECLARED_FRONTIER_EXHAUSTED`
- `BUDGET_EXHAUSTED_WITH_FRONTIER_OPEN`
- `INSTRUMENT_UNKNOWN`
- `NOT_EXERCISABLE`

Only `DECLARED_FRONTIER_EXHAUSTED` can mint an atomicity certificate. The precedence
rule is part of the structured record so an instrument failure cannot be hidden by a
simultaneous budget expiry.

## 6. Decomposition frontier

The grammar is versioned separately from the concept. Version 1 contains only two
composition operators. Candidate generators remain open and declared per run; they
are not forced into a false exclusive taxonomy.

Grammar v1 is authored target-blind and must be committed before any proving or live
subject is selected. Every S2 run cites both grammar version and grammar commit. A
grammar edit is a knowledge-basis event: historical certificates remain honest records
of their old basis, but they lose current eligibility wherever the changed grammar
applies and must re-run. They are never grandfathered into the new grammar.

One declared layer binds to one `decomposition_grammar@version`. The layer's Rule 24
declaration names that grammar beside its grain. A rival admissible grammar may run only
as a challenge control; divergent atom sets are a routed finding for the layer owner,
never a silent last-run-wins selection.

Each generator emits candidates with provenance. Candidates from different generators
are normalized to one declared grain before deduplication, counting, or challenge.
The run records:

- generator population and derivation dependencies;
- raw candidates;
- normalized candidates and merge lineage;
- excluded non-decompositions with reasons;
- grammar productions attempted and still open;
- all unassessed or unreachable residue.

## 7. Legislation through Rule 24

S3 is prohibited until S2 earns `DECLARED_FRONTIER_EXHAUSTED`. Legislation includes:

- declared axis intent and grain;
- MECE test with collective exhaustion against the declared layer;
- intent-coherence test;
- state-coherence stability frame and values that do not move together, if any;
- word-boundary token census over declared canon files with a positive control;
- a population predicate and denominator-generation process, never a roster;
- authority and home. Abstract concepts may route to the abstract registry; local value
  enums remain with their machine contract or producing package, differentiated by home.

Adoption is an authoring act. Reused arrays and axes carry their own fresh record here.

## 8. Resolution contract

S4 emits one contract per adjacent or higher binding layer. Each contract declares:

- binding identity, source layer, target authority, and grain;
- pointer or compile mechanism and HEAD vintage;
- claimed content and a direct content check;
- exactly-one authority cardinality check;
- code citation and re-declaration check;
- mechanical, declarative, and semantic seam checks;
- failure direction, detector, evidence, owner, and re-run trigger.

The primary binding form is exactly one of `RESOLVES_VIA_POINTER`,
`VIEW_TIME_COMPILED`, or `CITED_ENUM`. Each row names both loud and clean failure
possibilities and places the detecting check beside the condition. A dangling pointer
normally fails loud at read; a compiler operating over a silently stale source and a
copied enum drifting from its authority can fail clean. Form alone never substitutes
for the row's observed failure-direction analysis.

The contract's formula and code-specific requirements live in
`skill/atom-layer0/references/resolution-contract.md`.

## 9. Proving-run acceptance

The method is not accepted from prose or self-test alone. S5 requires a subject selected
outside the method authoring seat, one end-to-end structured run, and at least one method
defect that is repaired and regression-tested. A run that finds no defect remains suspect
and does not satisfy this package's founding acceptance bar.

The proving run may conclude `DECOMPOSITION_FOUND`; if so, the method must recurse or
record why the branch legitimately stops. An end-to-end atomic certificate requires an
externally selected subject whose frontier actually closes.

## 10. Bounds

- This package characterizes and proposes; it does not ratify concepts or install gates.
- It does not fix ontology or consumer defects discovered by a run; findings route to owners.
- It does not infer atomicity from corpus silence, one search tool, or one author.
- It does not register itself. Registration and root-project placement route through CTO.
- It does not replace `/molecule` or `/seams`; it composes their node and edge disciplines.
