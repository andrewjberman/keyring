# comp-symbols -- SPEC v1 (NFRA_COMPROUTE Stage-1 candidate #3)

**Author:** 0.8.0_AE_CloudComp~E · 2026-07-01 · for CTO ratification (COMPROUTE PRD owner)
**Origin:** gap_heat worklist v0 item #3. COO~B dispatched it build-vs-route -- GROUNDED as NET-NEW
BUILD (comp-which grep-fell-back; no tool lists a file's symbols; comp-blast needs a function NAME,
not "list the functions"). So: spec -> RAVC CTO (like comp-dispatch) -> build on nod. Net-new tool,
P2-scorer-independent.

## The gap (grounded, live demand)

`comp-symbols` fronts the INTRA-FILE SYMBOL INVENTORY -- "what functions/classes/constants ARE
defined in file X, and where". No comp-tool answers it. Agents raw-grep large HOT files for their own
symbols: `infra/aws/globgrph/derive_runner.py` (90KB, heat 0.94, a gap_heat build-next) is grepped for
`def ingest_|ingest_ts_semantic|ingest_cluster|def commit_to_iceberg|def main|_PRODUCERS|for .* in
.*producer` and `node_type|drift_class|layer|props`. A 90KB file is miserable to raw-grep for "where
is function Y" / "what functions are in here".

- comp-which GREP-FELL-BACK on "list the functions/classes/constants in a file" (grounded 2026-07-01)
  -- no direct route.
- comp-blast = the function-BLAST-RADIUS of a NAMED function (what breaks if I change fn X). It needs
  a name you already have; it does NOT enumerate a file's symbols. Different concern.

## Why net-new + clean (deterministic, no LLM)

Python's `ast` module gives an EXACT, deterministic parse -- functions (`FunctionDef`/
`AsyncFunctionDef`), classes (`ClassDef`), module-level constants (`Assign` at module scope, esp.
UPPER_CASE), and imports -- each with its line number. No regex fragility, no execution, read-only.
The demand files are Python (derive_runner.py, the gold scripts, cli.py), so an AST tool covers the
live demand; .ts/.sh can extend later (v1 = Python).

## Tool surface

```
comp-symbols <file>                       # the symbol index: functions, classes, constants, imports (+ line numbers)
comp-symbols <file> --grep <pattern>      # filter symbols by name (the "def ingest_" / "commit_to_iceberg" intent)
comp-symbols <file> --kind func|class|const|import   # one symbol class
comp-symbols <file> --json                # machine-readable (graph-populatable: a DEFINES edge file->symbol)
```

`<file>` = a repo path (or a resolvable name via the same firm/script maps the other comp-tools use).

## Output shape

- **FUNCTIONS** (name @ line, with args + whether nested/method vs module-level; async flagged).
- **CLASSES** (name @ line, with its methods indented).
- **CONSTANTS** (module-level UPPER_CASE assignments @ line -- e.g. NODE_TYPE_LAYER, _PRODUCERS).
- **IMPORTS** (what the file pulls in @ line) -- optional, `--kind import`.
- Counts per class in the header. `--grep` filters by name across all classes.

## How it complements comp-blast (layering, not duplication)

- **comp-blast** = the BLAST-RADIUS view: given a NAMED symbol, what depends on / breaks with it.
  Grain = one named symbol's dependency graph.
- **comp-symbols** = the INVENTORY view: what symbols a FILE defines + where. Grain = one file's
  symbol table.
- They COMPOSE: `comp-symbols derive_runner.py --grep ingest_` -> pick `ingest_graphuni_producers`
  -> `comp-blast ingest_graphuni_producers` for its blast radius. Inventory (what's here) -> blast
  (what depends on it). Different GRAIN + CONCERN -> distinct one-home node.

## Open design Q for CTO (parallel to the comp-dispatch ruling)

Sibling `comp-symbols` vs a `comp-blast symbols <file>` subcommand? By the comp-dispatch reasoning:
comp-blast's home = the symbol-DEPENDENCY concern (blast radius); comp-symbols' home = the
file-INVENTORY concern (symbol table). Different grain + concern -> RECOMMEND SIBLING (also more
discoverable: "what's in this file" won't reach for the blast tool). CTO's ruling requested.

## Fit + routing (COMPROUTE Stage-1)

- COMPUNIFY map home node (~C lands it, one-home): grain=file/symbol-inventory, concern=symbol-table,
  distinct_from comp-blast by grain+concern.
- comp-which routing rule (~C): "list the functions/classes/symbols in file X", "what's defined in
  file X", "where is function Y in file X", "what constants does file X define" -> comp-symbols.
  Another COMPROUTE Stage-1 routing mutation (LD-0226).

## Build plan (on CTO's nod)

`org/modules/graph/comp_symbols.py` + a `.tools/comp-symbols` shim (the comp-tool convention;
read-side lane-portable, like comp-dispatch). `ast.parse` the file -> walk for FunctionDef/
AsyncFunctionDef/ClassDef/module-Assign/Import -> render + `--json`. ~1 light-cycle. No AWS, no LLM,
read-only.

## Acceptance (proposed)

`comp-symbols infra/aws/globgrph/derive_runner.py` lists `commit_to_iceberg`, the `ingest_*`
functions, and the `NODE_TYPE_LAYER` constant with CORRECT line numbers (verifiable against the file);
`--grep ingest_` filters to the ingest functions; `--kind const` shows the module constants;
`--json` round-trips. Line numbers match `ast` (the deterministic-parse correctness proof).
