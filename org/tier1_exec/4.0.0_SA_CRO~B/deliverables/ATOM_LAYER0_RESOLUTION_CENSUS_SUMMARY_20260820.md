# ATOM_LAYER0 repo resolution census - CRO~B

**Status:** PROPOSED - PASS 2 COMPLETE | **Pass-1 vintage:**
`602b73a1f99d889dabbc884525b10dd8e7bf2e56` | **Pass-2 vintage:**
`6b48695dfab4c69f6c53b6beacd6947189b2d418` | **scope:** repo only; cloud execution explicitly
deferred. The denominator-only population landed first at `ee9431a49b`. No fixes were made.

## Result

The claim set contains **59 rows, all assessed**: **29 resolve and 30 do not**. These are row counts,
not independent-defect counts: Estate inherits Substrate, six W15 rows are one already-held
synchronization residual, and several stale status claims share one landed implementation event.

The surface denominator is **31 files**: 16 top-level ontology surfaces and 15 graph/consumer
surfaces. **All 31 are fully assessed; none remains partial or unassessed.** Pass 2 closed the 12
skipped ontology files and completed `LAYER_FIELD_ANATOMY.md`, `comp-tools.yaml`, and
`graph-call-manifest.yaml`. The separate registry annex denominator remains **18 terms carrying
`resolves_via`**: 9 resolve and 9 do not at the Pass-1 vintage.

## Worst first

1. **Two-home findings - 2 rows, now discriminated.** `Segment` is a
   `GOVERNED_DUAL_CARRIER`: block precedence is declared and O1 compares both blocks, detecting the
   `andrew-infrastructure` vs `estate-infrastructure` drift. `Contract_Record` remains
   `AMBIGUOUS_TWO_HOMES` with `CONTENT_MISMATCH`: its prohibited copied member list is an
   unauthorized second declaration, not legitimized by the adjacent healthy authority citation.
   Both were re-read directly. Owners: CRO and CTO respectively.
2. **SUPERSEDED_UNBANNERED - 11 rows.** Pass 2 found eight stale status surfaces across the learning
   loop, naming/content design, implementation handoff/spec, ontology index, and sensor-contract
   record; two stale vocabulary claims in `LAYER_FIELD_ANATOMY.md`; and one retired tool still
   presented as callable in `comp-tools.yaml`. The strongest repeated delta is "not landed/not built"
   surviving after the cited target landed.
3. **CONTENT_MISMATCH - 15 rows.** The original ten remain: `Contract_Record`, three O1 population
   rows (`Estate`, `Substrate`, `Domain`), and six already-known W15 rows. Pass 2 adds four
   intra-document or cross-document status contradictions and the manifest's measured
   subcommand-declaration drift. Several of these rows also carry `SUPERSEDED_UNBANNERED`;
   multi-label counts are occurrences, not independent defects.
4. **CODE_REDECLARATION - 2 rows, one engine.** `comp_legacywriter.py` copies the Lifecycle_Class
   enum and Contract_Record required-field vocabulary into code. Its conformance test can detect a
   drift, but the code still has a second home. Owner: CTO.
5. **NO_DECLARED_TARGET_CONTENT - 3 rows.** C0, C1, and Estate_Contracts derive current
   populations but declare no target population to compare. Owner routing is in-row.
6. **NON_INDEPENDENT_RESOLUTION - 1 row.** Chain declares and derives from the same frozen
   resolver artifact; O1's vacuous agreement is not promoted to resolved. Owner: CloudComp.
7. **NOT_EXERCISABLE - 1 row / tool gap.** `check_system_definitions.py` passes its form contract
   but does not implement the specified `resolves_via` execution mode. Owner: CTO.
8. **INSTRUMENT_UNKNOWN - 1 multi-label row.** Of 76 `tools_index` declarations, the standing
   checker can establish 28: 18 agree and 10 drift. The remaining 48 shapes are printed UNKNOWN,
   not promoted to clean; this is attached to the same manifest row as the measured drift.

No `DANGLING`, `UNRESOLVED_NO_AUTHORITY`, or `GRAIN_MISMATCH` row was established in the assessed
set. That zero is bounded by the printed residue; it is not a repo-wide metaphysical zero.

## Controls and instruments

- Positive control: `Lifecycle_Class` resolves from the registry to exactly one rule-bank lifecycle
  home. A separate consumer's code copy correctly fails independently.
- Author-selected negative: `Segment` classifies `GOVERNED_DUAL_CARRIER` by direct reads of both
  canonical blocks. Its block precedence and O1 detector cover the still-extant one-member drift.
- Independent O1-annex negative: `Contract_Record` was externally established as one of O1's five
  non-agreements. Direct read classifies it `AMBIGUOUS_TWO_HOMES` with secondary
  `CONTENT_MISMATCH`, not RESOLVED; the false-green check therefore passes.
- `comp-state --self-test`: PASS 4/4. Live report: 925 BEHIND/POST-CLOSE of 2,538 records; advisory,
  not used as a content verdict.
- `check_system_definitions.py`: self-test PASS 10/10; live PASS 65/0. It checks form, not resolution.
- `comp-ontolint`: seeded mutants PASS; live Role/Relation invariant PASS (10 base relations,
  3 composites, 14-role total order).
- `l0b_conformance.py`: PASS at its ratified bar, 13 satisfied plus 1 declared-exempt, 17/17 harness
  cells; the document-derived denominator is 9 source-change and 5 input-degradation members.
- `boundary_report` conformance: 24/24 tests PASS.
- `content_relate_prototype.py`: synthetic mechanism floor and pooled-decoy control PASS; the artifact
  remains explicitly reference-only pending the real-content blinded verdict.
- `comp-manifest-check completeness`: PASS, 91 tracked executables accounted and 76 registered tools.
  Its subcommand annex prints 10 standing drifts and 48 UNKNOWN shapes rather than hiding them.

The TWO_HOMES discriminator is explicit for `Contract_Record`: the registry's `authority` pointer is
a healthy citation, but the registry `definition` separately copies both field lists and omits
`describes`. That copied stable-canon declaration and the rule-bank declaration are independently
editable; the citation itself is not counted as a home.

The discriminator is also explicit for `Segment`: its dual carry is ratified, block precedence is
declared, and O1 exercises both blocks. The remaining mismatch is governed and detected; it is not
an authority ambiguity. The structured artifact includes direct-read receipts for all 19 surfaces
claimed fully or partially assessed at the Pass-1 vintage and 15 Pass-2 receipts whose union is all
31 declared surfaces.

Three rows were rerun from their exact pinned file+anchor pairs after Base's adversarial challenge:
R010 Segment, R015 Contract_Record, and R027 comp_legacywriter Lifecycle_Class. All three reproduced
their committed verdicts. The structured artifact gives the exact reads and defines how every O1 row
shorthand expands to a pinned JSONL line.

## Rule-24 correction to the verdict schema

The brief's starting list mixed three intents on one axis. The structured artifact separates
`assessment_state`, binary `resolution_state`, and multi-label `failure_classes`, then derives the
requested display verdict by fixed precedence. The layer-coverage test added four missing mechanisms:
`GOVERNED_DUAL_CARRIER`, `NO_DECLARED_TARGET_CONTENT`, `NON_INDEPENDENT_RESOLUTION`,
`INSTRUMENT_UNKNOWN`, and `NOT_EXERCISABLE`. The attached record gives all four postulates, the
two-home discriminator postulates, and the token-hygiene census.

## Residue

No declared surface remains as traversal residue. What remains is only the population boundary named
before verdicting: 59 `comp_*.py` engines that failed the strong binding-signature inclusion predicate,
the nested `worldmodel/**` evidence corpus, other graph subtrees, and cloud execution deferred by
Andrew's sequence. The dirty working-tree copy of `estate-coverage-resolver.json` predated this seat;
Pass 1 read only its pinned Git object and did not touch that delta. The next two allocations named by
Base - the 59-engine code-grain sweep and the 9/18 unresolved `resolves_via` completion drive - were
not started or folded into Pass 2.

## Runtime integration seam

The YAML is executable input, not a prose-only report. A future CRO~C integration seat can select an
assessed `rows[]` object directly and map `concept`, population surface role, evidence anchors,
resolution state/failures, owner, and vintage into atom_layer0 S0 without hand translation. The row
schema and its own Rule-24/token-hygiene record are attached in the machine artifact. Concept-consumer
discovery remains atom_layer0 S0 work rather than a guessed census field.

The machine-readable source of truth is
`ATOM_LAYER0_RESOLUTION_CENSUS_20260820.yaml`; this document is its rendered view.
