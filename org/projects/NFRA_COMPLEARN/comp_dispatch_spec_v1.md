# comp-dispatch -- SPEC v1 (NFRA_COMPROUTE Stage-1 candidate #1)

**Author:** 0.8.0_AE_CloudComp~E · 2026-07-01 · for CTO ratification (COMPROUTE PRD owner)
**Origin:** the gap_heat build-next worklist v0 (grounded #1 gap). This spec RAVC = the Stage-1
ratification ask (a grounded spec, not a bare worklist line). Net-new tool, P2-scorer-independent.

## The gap (grounded, live demand)

`comp-dispatch` fronts the GOLD-DISPATCH ORCHESTRATION LAYER -- the one thing no comp-tool answers.
`data/black_diamond/scripts/gold/gold_dispatch.sh` (1419 lines) is the **#1 gap_heat build-next**
(bd 7 escapes/heat 0.89 hot; cot 6/0.66 warm), and EVERY escape asks the same class of question:
- "what scripts does chain X run, in what ORDER?" (`E_*`, `run_stage`, `python3?.*[A-E]_[0-9]`)
- "does the dispatch run script Y?" (`C_00.canonical_performance|C_02.client_performance`)
- "what conditionally SKIPS?" (`\.py.*\|\|.*-f|test -f|\[ -f|missing|not found|SKIP`)
- "which scripts are in group/stage Z?" (`E_18|E_25|aua_decomposition|diagnostic`)

comp-which BACKSTOPS this intent (no direct route; grounded 2026-07-01). comp-pipescript is
per-SCRIPT (io/deployed); NOTHING parses the dispatch `.sh`'s DAG. A 1419-line shell script is the
worst possible thing to raw-grep for "what runs when" -- hence the escape concentration on a hot path.

## Why this is a clean, deterministic parse (no LLM, no fragility)

`gold_dispatch.sh` is HIGHLY structured -- comp-dispatch parses declared blocks, not free text:
- **CATALOG** (heredoc `ID|filename|default_flags`): the script inventory
  (e.g. `D_00|D_00.portal_aggregates.py|--upload`). ~24 entries.
- **CHAIN_* vars** (ordered script-ID lists): `CHAIN_CANONICAL="B_00 B_01 B_01b B_02 B_03 C_00 C_01 C_02 C_04"`,
  `CHAIN_DOWNSTREAM`, `CHAIN_DIMENSIONS`, `CHAIN_HOLDINGS_SEED`, `CHAIN_SILVER_PREP`, and
  `CHAIN_FULL="$CHAIN_DIMENSIONS $CHAIN_CANONICAL $CHAIN_DOWNSTREAM"` (a resolvable composition).
- **GROUP_* vars** (`GROUP_A..GROUP_D` = script IDs by letter).
- **Conditional GATES** (named functions/flags): `check_freshness()` (silver-latest vs gold
  data_as_of; SKIP if not advanced; `--force` overrides), the `_checkpoint_done()` / `GOLD_RESUME`
  per-script `.done` resume-skip, and the `--incremental` skip-already-processed mode.
- **Modes/flags** (in `show_help` -- the single-source-of-truth per the file's own DH-3 rule):
  `--chain <name>` / `--single <ID>` / `--group <letter>` / `--incremental` / `--dry-run` / `--force`
  / `--status` / `--kill` / `--bg`.

Both firms (bd + cot) share this exact structure -- so comp-dispatch is FIRM-PARAMETERIZED, not
bd-special. The parser reads the declared blocks; it does not execute or interpret the bash.

## Tool surface

```
comp-dispatch <firm|path>                 # the full dispatch map: chains -> ordered scripts, catalog, groups, gates, modes
comp-dispatch <firm> --chain <name>       # one chain expanded to its ordered script list (CHAIN_FULL resolves its nested chains)
comp-dispatch <firm> --script <ID>        # reverse: which chains/groups include this script + its file + default_flags + run position
comp-dispatch <firm> --gates              # the conditional skips: freshness gate, checkpoint/resume-skip, --incremental (+ how to override)
comp-dispatch <firm> --undispatched       # scripts present in the gold dir but NOT in the CATALOG (the E_* diagnostics -- run standalone, not in any chain)
comp-dispatch --list                      # which firms have a parseable gold_dispatch.sh
[--json]                                  # machine-readable (for the graph / comp-which / a future consumer)
```

## Output shape (the `<firm>` default view)

- **CHAINS** (name -> ordered [script IDs], nested chains resolved + de-duped), each ID annotated
  with its filename + default_flags from the CATALOG.
- **CATALOG** (ID -> filename -> default_flags).
- **GROUPS** (letter -> [IDs]).
- **GATES** (freshness: silver/allocations vs gold header data_as_of, `--force` override; resume:
  `.done` markers under `gold/.checkpoints/<run_date>/`, `GOLD_RESUME=1`; `--incremental`).
- **UNDISPATCHED** (gold-dir scripts absent from the CATALOG = standalone diagnostics, e.g.
  E_18.detect_new_securities, E_25.aua_decomposition_audit -- the "why isn't E_* in the chain?" answer).

## How it complements comp-pipescript (layering, not duplication)

- **comp-pipescript** = the PER-SCRIPT view: `io` (a script's reads/writes/columns + portal
  consumers), `deployed` (is my code on the runner). Grain = one script.
- **comp-dispatch** = the ORCHESTRATION view ABOVE it: which scripts run, in what ORDER, under
  which chain/group/flag, past which GATE. Grain = the dispatch DAG.
- They COMPOSE: `comp-dispatch bd --chain canonical` -> the ordered B_00..C_04 list ->
  `comp-pipescript io B_02` -> that script's IO. Full pipeline comprehension = dispatch DAG (what/when)
  x pipescript IO (what-data). comp-dispatch is the missing top layer of the comp-pipescript family
  (a candidate name: `comp-pipescript dag` if CTO prefers it as a subcommand vs a sibling tool).

## Fit + routing (COMPROUTE Stage-1)

- Register in `org/modules/graph/graph-call-manifest.yaml` (the catalog) + a comp-which curated rule:
  "what scripts does the gold dispatch run / in what order / conditional skips" -> `comp-dispatch`.
  This rule ALSO closes the routing-miss for the many dispatch-intent escapes (a COMPROUTE Stage-1
  routing-rule mutation, per the LD-0226 model).
- The `--json` surface makes the dispatch DAG a graph-populatable object (a future RUNS/ORCHESTRATES
  edge: dispatch -> script), so comp-dispatch feeds the estate graph too.

## Build plan (on CTO's nod)

A single Python tool (`org/modules/graph/comp_dispatch.py` + a `.tools/comp-dispatch` shim, the
comp-tool convention) that: locates `data/<firm>/scripts/gold/gold_dispatch.sh` (firm map, like the
other comp-tools), parses the CATALOG heredoc + the `CHAIN_*`/`GROUP_*` var assignments (regex on the
declared blocks) + detects the named gates, resolves `CHAIN_FULL`'s nested composition, cross-refs the
gold dir for UNDISPATCHED scripts, and renders the views + `--json`. ~1 light-cycle. No AWS, no LLM,
read-only over the committed `.sh`.

## Acceptance (proposed)

`comp-dispatch bd --chain canonical` returns exactly `B_00 B_01 B_01b B_02 B_03 C_00 C_01 C_02 C_04`
(byte-match the CHAIN_CANONICAL var); `--script C_02` reports it's in canonical + full + GROUP_C with
`--upload`; `--undispatched` surfaces the E_* diagnostics; `--gates` names the freshness + resume +
incremental skips; identical structure resolves for cot. A dispatch-intent comp-which query routes to
comp-dispatch (routing-miss closed).
