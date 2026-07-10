# CVO~B -- tracer-cluster full close-out + the SOVEREIGN bd-indexer chokepoint (5th bd-reader)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**Serial:** 3.0.0_SA_CVO~B (lane ~B; folder 3.0.0_SA_CVO)
**Window:** ~18:56Z (prev log 145f377fe) -> 22:53Z

## Summary

Closed the entire trace-graph comp-tool cluster under NFRA_TOOLPASS (CTO front-passes = LEADS,
CVO re-runs every falsifier + writes the fix + mutant bar; CTO gates; CVO briefs COO), and -- the
headline -- SURFACED + FIXED a sovereign-class finding: the graph indexer was READING
data/black_diamond/ CONTENT on every build + freshness check (the 5th and largest bd-reader).

## Tools closed this window (all CTO-gated GREEN)

- comp-chainrun `1fc318f31` -- CR1 atomic snapshot write (+ CR2 closed by exercise: real-S3 diff both ways).
- comp-coverage `33146f029` -- CV1 stdout-only default (0 repo churn) + CV2 the 11.3% headline was a
  MATCH ARTIFACT (id-tag-only) -> id-OR-stem match -> 17.1% (lower-bound disclosed).
- comp-diff `430e2f2ae` -- CD1 --json emitted human text on stdout -> broken --json. Found by exercise.
- comp-trace `f8bf876c8` (with CX1) -- CT1 --direction both --json = 2 concatenated docs -> single
  {"query","traces"} doc. Found by exercise (a path CTO never ran).
- comp-xref `f8bf876c8` -- CX1 no-baseline/load-failed/--save edge paths printed human under --json
  (the CD1 analog).
- comp-depth + comp-graph -- CONFIRMED CLEAN by exercise (no diff). comp-graph's same-expression MUTATION
  (force enforcer STALE-999 -> printed verdict moved WITH it) proved it calls cli.trace_freshness, not a
  re-modelled TTL.

## THE SOVEREIGN CHOKEPOINT (bd61228a4) -- design (b) content-only bd exclusion

- FINDING (source-confirmed + artifact): the indexer opened + READ data/black_diamond/ .py CONTENT --
  extract_s3 read_text the bd gold dir; extract_pipeline read_text+ast.parse'd it (build_pipeline_dag:
  _parse_s3_layout, _parse_dispatch, _extract_script_io, gold_dispatch.sh); add_node/_compute_file_sha
  hashed every bd .py for source_sha. Proof: all 724 bd-file-backed nodes carried a source_sha.
- FIX (CTO-ruled design-b): a held-path file (SOVEREIGN_HELD_MARKERS) is MINTED as a node (metadata ->
  reachability preserved) but NEVER read_text/ast.parse/sha'd. Pure-string _held_path_hit; markers mirror
  comp_constants_cli, drift-guarded. Gated: trace_graph add_node + check_node_freshness; extract_s3 gold
  loop; extract_pipeline _extract_script_io + _parse_s3_layout + _parse_dispatch + parse_gold_direct_invoke.
- FIXTURE-FIRST (pre-commit proof, synthetic, no live bd): tests/test_indexer_bd_content_exclusion.py --
  exclusion ON = 0 held reads, MUTATION off = 6 reads (RED). The fixture CAUGHT 2 sites the first pass
  missed (_parse_s3_layout, _parse_dispatch) before commit.
- ACCEPTANCE (instrumented real rebuild): 0 data/black_diamond/ + schwab/silver/ content reads, 0 bd sha.
  bd nodes 724->69 file-level (design-b correctly drops ~655 content-derived function/builder nodes;
  file-grain reachability preserved). CTO ruled both accepted; 5th-reader CLOSED.
- FLAGGED (not fixed): comp-iam (6th) + comp-validate (7th) are separate bd-readers (CTO front-passes);
  comp-depth reads the globgrph/Nessie MARKER-HEAD graph (separate builder, potential 9th surface) -- my
  chokepoint does NOT cover it; CTO acting on it.

## MCP traffic (significant only)

~30 CTO<->me exchanges (tool GOs, per-tool GATE GREENs, the sovereign RULING + ACCEPTANCE RULING + the
chokepoint gate). 4 COO cleanup briefs (chainrun / coverage / comp-build / tracer-cluster). One
sequencing correction handled (comp-build STAGED -> patch-preserve + revert-to-clean -> re-applied on hand-down).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-build | definitive bd-safe rebuild | PASS | 1390 nodes, 69 bd file-level, 0 bd sha, 0 sentinels |
| comp-blast/trace/xref/diff | --check (repeatedly, both states) | PASS | shared-predicate; green after every fix |
| comp-chainrun | selfcheck + live opal-data-inf snapshot/diff | PASS | CR2 real-S3 both ways |
| comp-coverage | report (stdout-only) | PASS | 11.3% -> 17.1% (match fix) |
| comp-depth / comp-graph | grains/scope/drill/rollup + status | PASS | confirmed clean by exercise |

- **What worked:** confirmation-by-exercise caught a real --json/parse defect in THREE tools CTO
  front-verdicted CLEAN (CD1, CT1, CX1). The fixture-first mandate caught the 2 missed chokepoint sites.
- **Off-rail oracles:** raw grep / json.load / build_graph instrumentation carried the NFRA_TOOLPASS sec.6
  marker (assurance oracle for a tool under test -- must not share the tool's predicate).
- **Gap found:** the graph indexer was an ungated bd-content-reader (now fixed); 2 more bd-reader surfaces
  (comp-iam, comp-validate) + a potential 9th (globgrph builder) surfaced for CTO.

## Files Modified

See commit messages: 1fc318f31, 33146f029, 430e2f2ae, bd61228a4 (+ new test), f8bf876c8, 19e4177db,
227c1651a. All authored 3.0.0_SA_CVO~B, surface-check clean, pushed CLOUD.

## Blockers

None. Cluster fully closed. (Sovereign holds were respected throughout: bd read as metadata only, no bd
data/source read by me; all mutants on non-bd INF/find/scratch nodes.)

## Current State

- Trace-graph cluster (org/modules/graph/{cli,trace_graph,extract_s3,extract_pipeline}.py + chainrun_cli
  + coverage_cli) fully fixed + gated. `.comp-graph/graph.json` rebuilt bd-safe (1390 nodes, 0 bd sha).
- All 5 cluster tools + comp-chainrun + comp-coverage CLOSED; comp-depth + comp-graph CONFIRMED CLEAN.
- Sovereign chokepoint live; 724 bd nodes -> 69 file-level metadata nodes (reachability), 0 content read.

## Next Steps

- **[2.0.0_SA_COO]** Cluster cleanup: stale coverage-report/ artifact disposition + (post-sweep) held-marker
  consolidation into one shared constant.
- **[1.0.0_SA_CTO]** Front-pass comp-iam (6th) + comp-validate (7th) bd-readers; verify the globgrph/Nessie
  builder (potential 9th surface, comp-depth's data source).
- **[Andrew]** The sovereign escalation (indexer was a fabric-wide bd-content-reader; CTO routed it to you).
- **[3.0.0_SA_CVO~B]** Cluster complete; reachable for the next assignment.
