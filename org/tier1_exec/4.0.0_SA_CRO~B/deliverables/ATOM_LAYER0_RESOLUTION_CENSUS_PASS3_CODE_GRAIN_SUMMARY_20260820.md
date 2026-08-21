# ATOM_LAYER0 Resolution Census — Pass 3 Code-Grain Sweep

**Seat:** `4.0.0_SA_CRO~B`  
**Population act:** `76ba5fec3d`  
**Assessment vintage:** `f36d572be864e56b9175caac06b01f62fc141e2a`  
**Status:** COMPLETE — ready for Base ingestion

## Outcome

The fixed Pass 3 population contains exactly 59 `comp_*.py` engines. All 59
committed blobs were present, parsed by AST, directly read, and given immutable
blob receipts. Six engines carry nine unresolved ontology/code bindings. One
additional engine has a governed binding that resolves by citing and loading its
implementation authority. The remaining 52 engines have receipts but no
adjudicated ontology binding row.

| Measure | Result |
|---|---:|
| Fixed engines | 59 |
| AST/direct-read receipts | 59 / 59 |
| Engines with unresolved bindings | 6 |
| Engines with a resolved binding | 1 |
| Engines without a binding row | 52 |
| Binding rows | 10 |
| `CODE_REDECLARATION` rows | 9 |
| Rows also carrying `CONTENT_MISMATCH` | 3 |

## Findings

| Engine | Governed concept | Verdict | Why |
|---|---|---|---|
| `comp_aws_cli.py` | concrete edge vocabulary | `CODE_REDECLARATION` | The graph producer emits/interprets 26 governed concrete-edge tokens but never loads the canonical rule bank. |
| `comp_aws_cli.py` | concrete node-type vocabulary | `CODE_REDECLARATION` | It independently carries 26 governed node-type spellings plus an auxiliary-type roster. |
| `comp_blast_universe.py` | producer-edge set | `CODE_REDECLARATION` + `CONTENT_MISMATCH` | Its local producer set assigns trigger/composite edges to producer semantics and omits six canonical producer bindings. |
| `comp_blast_universe.py` | function-grain node types | `CODE_REDECLARATION` + `CONTENT_MISMATCH` | It places `Hook` and `DataFetch` at function grain; the governed grain contract places those at component grain. |
| `comp_coverage_check.py` | drilldown/rollup direction map | `CODE_REDECLARATION` | Although the file reads the ledger, `assemble_rollup` separately re-encodes `RUNS`/`CONTAINS` forward and `OWNED_BY` reverse. |
| `comp_depth_cli.py` | breadth-edge scope | `CODE_REDECLARATION` | `_BREADTH_EDGES` is documented as “kept in sync” with a sibling code roster instead of being derived from it. |
| `comp_ladder.py` | C0–C3 runtime ladder | `CODE_REDECLARATION` + `CONTENT_MISMATCH` | It copies the four labels and renders one `C3=SYSTEMS` bucket, omitting the repaired C3.i/C3.ii dual partition. |
| `comp_marker_read.py` | drilldown fallback | `CODE_REDECLARATION` | The normal path derives from the ledger, but the fail-soft branch retains a separately editable canonical three-seam roster. |
| `comp_marker_read.py` | tracegraph edge scope | `CODE_REDECLARATION` | The five-edge compatibility roster is code-carried and already has a second code home in `comp_depth_cli.py`. |
| `comp_recognizers_tsx.py` | D1 `EdgeKind` normalization | `RESOLVED` | Input serialization spellings map to values loaded from `cse_schema.EdgeKind`; the governed target values are cited, not copied. |

The three mismatch rows are not separate outcome rows. They are additional
failed properties on the same surface × concept bindings; display precedence
correctly renders `CODE_REDECLARATION`.

## Controls and adjudication discipline

`comp_legacywriter.py` remained outside the 59-engine denominator and served as
the positive type control. The AST instrument detected both known defects:
`_UNIVERSAL_REQUIRED` for `Contract_Record`, and `GATED_CLASSES` plus
`_LIFECYCLE_ENUM` for `Lifecycle_Class`. This is a passing control, not a new
Pass 3 finding.

`comp_api.py` supplied a clean negative control. `comp_toolgraph.py` supplied a
lexical-collision control: its runtime strings `C1` and `C2` are explicitly local
AC-0 registration clauses meaning “catalogued” and “convention,” not ontology
rails. No row was minted. Likewise, ordinary identifiers such as the SmartX
asset channel, AWS `ACTIVE`, and the English output field `completeness` were not
promoted into findings without a governed binding at the same grain.

## Reproducibility and residue

The machine scan is rerunnable from pinned Git objects:

```powershell
python org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ATOM_LAYER0_PASS3_CODE_GRAIN_SCAN_20260820.py
```

The instrument verifies every engine blob against the population artifact,
excludes docstrings, reports exact governed runtime tokens and literal clusters,
and prints the `comp_legacywriter` control separately. The YAML census contains
all 59 engine receipts and the human grain/meaning adjudications; the JSON is the
unabridged machine output.

Fresh-vintage residue is explicit: `comp_directives.py` postdates the frozen
59-engine cohort and is outside this denominator. Working-tree-only engine files
were not read under the Git-object rule. No engine is silently unassessed.

## Routing boundary

This is census, not chase. No engine, ontology authority, or registry record was
modified. Owner candidates are attached to every finding from path lane,
source header, and pinned blame where derivable. The `resolves_via` completion
drive stayed fenced with zero authored changes. C7-CLOSURE remained held through
Pass 3 and may begin only after Base receives this completion signal.

## Machine artifacts

- Population: `ATOM_LAYER0_RESOLUTION_CENSUS_PASS3_CODE_POPULATION_20260820.yaml`
- Census and 59 receipts: `ATOM_LAYER0_RESOLUTION_CENSUS_PASS3_CODE_GRAIN_20260820.yaml`
- Scanner: `ATOM_LAYER0_PASS3_CODE_GRAIN_SCAN_20260820.py`
- Raw scan: `ATOM_LAYER0_PASS3_CODE_GRAIN_SCAN_RESULTS_20260820.json`
