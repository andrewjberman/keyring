# ATOM_LAYER0 repo resolution census - CRO~B

**Status:** PROPOSED | **read vintage:** `602b73a1f99d889dabbc884525b10dd8e7bf2e56` |
**scope:** repo only; cloud execution explicitly deferred. The denominator-only population landed first
at `ee9431a49b`. No fixes were made.

## Result

The assessed claim set contains **45 rows**: **43 assessed** and **2 explicitly NOT_ASSESSED**.
Of the assessed rows, **24 resolve and 19 do not**. These are row counts, not independent-defect
counts: Estate inherits Substrate, and six W15 rows are one already-held synchronization residual.

The surface denominator is **31 files**: 16 top-level ontology surfaces and 15 graph/consumer
surfaces. Coverage is 16 fully assessed, 3 partially assessed, and 12 not assessed; all 31 are named
in the structured artifact. The registry annex denominator is **18 terms carrying `resolves_via`**:
9 resolve and 9 do not at the pinned vintage.

## Worst first

1. **Two-home findings - 2 rows, now discriminated.** `Segment` is a
   `GOVERNED_DUAL_CARRIER`: block precedence is declared and O1 compares both blocks, detecting the
   `andrew-infrastructure` vs `estate-infrastructure` drift. `Contract_Record` remains
   `AMBIGUOUS_TWO_HOMES` with `CONTENT_MISMATCH`: its prohibited copied member list is an
   unauthorized second declaration, not legitimized by the adjacent healthy authority citation.
   Both were re-read directly. Owners: CRO and CTO respectively.
2. **CODE_REDECLARATION - 2 rows, one engine.** `comp_legacywriter.py` copies the Lifecycle_Class
   enum and Contract_Record required-field vocabulary into code. Its conformance test can detect a
   drift, but the code still has a second home. Owner: CTO.
3. **CONTENT_MISMATCH - 10 rows.** Three O1 families (`Substrate` plus inherited `Estate`, and
   `Domain`) remain open. Six rows are the already-known W15 L7 residual - four canonical
   `chain_count`s, one `spans_verticals`, and the held generated-resolver refresh - and are **not new
   findings**. Owner routing remains CTO / DS / COO+CloudComp as recorded per row.
4. **SUPERSEDED_UNBANNERED - 1 row.** `LAYER_FIELD_ANATOMY.md:760` still says
   `Lifecycle_Value` is contested/unresolved, while registry v3.11 records it as the deprecated
   naming-history alias of `Lifecycle_Stage`. The file has a global subordination clause but no
   local supersession marker on this claim. Owner: CRO.
5. **NO_DECLARED_TARGET_CONTENT - 3 rows.** C0, C1, and Estate_Contracts derive current
   populations but declare no target population to compare. Owner routing is in-row.
6. **NON_INDEPENDENT_RESOLUTION - 1 row.** Chain declares and derives from the same frozen
   resolver artifact; O1's vacuous agreement is not promoted to resolved. Owner: CloudComp.
7. **NOT_EXERCISABLE - 1 row / tool gap.** `check_system_definitions.py` passes its form contract
   but does not implement the specified `resolves_via` execution mode. Owner: CTO.

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

The TWO_HOMES discriminator is explicit for `Contract_Record`: the registry's `authority` pointer is
a healthy citation, but the registry `definition` separately copies both field lists and omits
`describes`. That copied stable-canon declaration and the rule-bank declaration are independently
editable; the citation itself is not counted as a home.

The discriminator is also explicit for `Segment`: its dual carry is ratified, block precedence is
declared, and O1 exercises both blocks. The remaining mismatch is governed and detected; it is not
an authority ambiguity. The structured artifact includes direct-read receipts for all 19 surfaces
claimed fully or partially assessed at the Pass-1 vintage.

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

Two enumerated surfaces have explicit NOT_ASSESSED rows (`comp-tools.yaml`, the 76-entry
`graph-call-manifest.yaml`); 12 more surface IDs remain unexpanded, and 59 `comp_*.py` files failed
the declared strong binding-signature predicate. The nested `worldmodel/**` evidence corpus and
other graph subtrees are outside this pass's declared layer, not silently treated as clean. The dirty
working-tree copy of `estate-coverage-resolver.json` predated this seat; the census read only the pinned
Git object and did not touch that delta.

## Runtime integration seam

The YAML is executable input, not a prose-only report. A future CRO~C integration seat can select an
assessed `rows[]` object directly and map `concept`, population surface role, evidence anchors,
resolution state/failures, owner, and vintage into atom_layer0 S0 without hand translation. The row
schema and its own Rule-24/token-hygiene record are attached in the machine artifact. Concept-consumer
discovery remains atom_layer0 S0 work rather than a guessed census field.

The machine-readable source of truth is
`ATOM_LAYER0_RESOLUTION_CENSUS_20260820.yaml`; this document is its rendered view.
