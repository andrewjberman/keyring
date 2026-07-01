# NFRA_COMPROUTE Stage-1 -- the 3 route-fixes + comp-symbols BUILT (lane ~E)

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01 UTC
**Window:** since the comp-dispatch log (f9b0434a7) -> ~0149Z

## Summary

COO~B dispatched the 2 remaining gap_heat worklist ROUTE-FIX items (Stage-1 L4). I GROUNDED each
(build-vs-route triage, the discipline CTO called "part of COMPROUTE's value"):
- #1 output-key surfacing = a PURE ROUTING MISS (comp-pipescript io already surfaces the keys) -> a
  comp-which routing rule, no build -> handed ~C.
- #2 comp-symbols = a NET-NEW BUILD (no tool lists a file's symbols) -> spec -> CTO-ratified (sibling)
  -> BUILT + verified.

## What was built / decided

- **Route-fix #1 (output-key) -- routing rule, no build.** Grounded: `comp-pipescript io D_00 --firm
  bd` already lists every output artifact + FUNC-key incl `aua_certification_key:
  gold/validation/aua_certification/{*}.json [FUNC]` (the exact key agents grep). Pure Mode-1
  routing miss -> the "what key/artifact does gold script X write" intent -> comp-pipescript io.
  Routing rule + registration handed ~C (one-home).
- **Route-fix #2 (comp-symbols) -- net-new BUILD.** `org/modules/graph/comp_symbols.py` +
  `.tools/comp-symbols` shim (commit e5ae5dd7a). The file-INVENTORY sibling to comp-blast's
  symbol-DEPENDENCY concern (CTO ruling 013811Z: opposite directions+inputs+concern -> distinct
  one-home node). Deterministic `ast.parse` -> functions/classes/module-consts/imports + line
  numbers; read-only, no LLM/exec; language-agnostic surface, parser-pluggable (v1 Python). Surface:
  `comp-symbols <file> [--grep|--kind func|class|const|import|--json]`.

## Verification (CTO acceptance -- line numbers match ast)

`comp-symbols infra/aws/globgrph/derive_runner.py`: commit_to_iceberg@247, ingest_ts_semantic@1197,
ingest_cluster@1240, ingest_graphuni_producers@1589, main@1642; `--kind const --grep NODE_TYPE` ->
NODE_TYPE_LAYER@1494 + DROP_NODE_TYPES@1527 (byte-match the file). --grep/--kind/--json + the shim on
PATH verified. ds-gate clean (fixed an E731 lambda->def).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-pipescript io | io D_00 --firm bd | PASS | GROUNDED route-fix #1 -- it surfaces the output keys (incl the FUNC aua_certification_key) -> pure routing miss |
| comp-which | file-symbol-inventory intent | PASS | GROUNDED #2 as net-new (grep-fell-back, no route) -- the build-vs-route triage |
| comp-symbols | (the new tool, self-test) | PASS | line numbers match ast -- the acceptance proof, self-demonstrating |
| ds-commit-gate.sh | comp_symbols.py | PASS | after the E731 fix |
| safe-commit.sh | e5ae5dd7a + this log | PASS | surface-check clean |

**What worked:** the build-vs-route triage cleanly split #1 (route) from #2 (build); ast.parse is a
deterministic, byte-verifiable symbol source.
**What failed:** ruff E731 (lambda assignment) -> nested def. The inbox Monitor died 3x with FORK
EXHAUSTION (CreateProcessW errno 27 -- box resource pressure from the multi-agent load, NOT a bug);
fell back to check_inbox turn-top pulls (lossless per the watcher caveat; flagged to COO~B for fleet
awareness, not escalated).
**Gap found:** none new (these tools + the route-rule close the top gap_heat escapes).

## Current State

comp-dispatch + comp-symbols BOTH live on PATH; the 3 route-fixes all delivered (map/routing landing
-> ~C). This session shipped, all live+verified: COMPLEARN P0+P1+P3 (substrate) + Behavior re-emit +
gap_heat worklist v0 + comp-dispatch + comp-symbols + 3 route-fixes. All deploy ledgers CLOSED; all
commits pushed. Inbox reachability via check_inbox pulls (Monitor fork-flaky under box load).

## Next Steps

1. **[0.8.0_AE_CloudComp~C]** land the comp-dispatch + comp-symbols COMPUNIFY map registrations + the
   3 comp-which routing rules (all details RAVC'd).
2. **[2.0.0_SA_COO~B / 1.0.0_SA_CTO]** the COMPROUTE L3 CORE POSTERIOR ENGINE (COO~B named me owner) +
   the P2 scorer -- both at the COMPUNIFY gate-lift (imminent). I own tool_activity + the views +
   both Stage-1 tools, so I'm the natural L3 owner. Available on dispatch.

## Blockers

None. L3 core + P2 scorer await the COMPUNIFY gate-lift (a real external gate). All depth-independent
solo work delivered.
