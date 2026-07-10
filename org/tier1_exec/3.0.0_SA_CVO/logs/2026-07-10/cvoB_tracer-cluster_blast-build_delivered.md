# CVO~B session log -- trace-graph cluster: comp-blast + comp-build delivered (NFRA_TOOLPASS)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**Serial:** 3.0.0_SA_CVO~B (lane ~B; folder 3.0.0_SA_CVO)
**Window:** session start (~16:02Z) -> 18:56Z (first log this session)
**Owner assignment:** the TRACE-GRAPH CLUSTER (comp-blast -> trace -> xref -> diff -> build), CTO GO Andrew-direct.

## Summary

Owned + delivered the first two tools of the trace-graph cluster under the NFRA_TOOLPASS
hand-validation process (CTO front-passes = LEADS, I re-run every falsifier + write the fix +
mutant bar; CTO gates; I brief COO). Both gated GREEN and closed end-to-end.

- **comp-blast** (`19e4177db`) -- B2-B6: dir-backed Lambda nodes silently unfreshenable + the D4
  test poisoning the LIVE cache. GATE GREEN 16:32Z.
- **comp-build** (`227c1651a`) -- C1: TraceGraph.save non-atomic in-place write (reap mid-write
  truncates the shared cache). GATE GREEN 18:54Z.

## What was done

### comp-blast (fix 19e4177db)
- Re-ran CTO's leads B2-B6. Found his U3 mint site: `extract_lambda_routes.py:123 file_path=source_dir`
  (a directory) -> `add_node` is_file() guard -> no source_sha -> `check_node_freshness` skips it. 35
  nodes (0 bd): 27 dir-backed + 8 the EXTERNAL sentinel.
- Fix: `_compute_path_sha` hashes a file OR a directory (deterministic aggregate, memoized per pass);
  EXTERNAL/absent source_dir no longer minted as file_path. Coverage 1824/1859 -> 1850/1851.
- Mutants killed: B5 both-arm x4 siblings (edit bundle .py -> STALE naming the node; revert -> FRESH);
  B3/B4 (prod cache byte-identical after completion AND a mid-run SIGKILL); B2 (0 non-hex sentinels).
- R4 census: no external consumer of trace_graph.Node.source_sha (resign/surface use a Kuzu drift_class).

### comp-build (fix 227c1651a)
- Re-ran CTO's C1 lead. Confirmed non-atomic `write_text` + no lock (the cli.py "block" hits are comments).
- Fix: `save()` -> unique same-dir `tempfile.mkstemp` -> flush -> `os.fsync` -> `os.replace` (atomic
  POSIX+Windows); graceful-failure temp unlink. Self-heal disclosure: `_get_graph` except now WARNs
  (naming the exception) instead of silently swallowing -- chose disclosure over narrowing (narrowing
  would turn a resilience path into a crash path).
- Mutant killed on a SCRATCH path: crash-before-replace -> target byte-identical to old + 0 orphan temps;
  success -> new complete; contrast: old write_text truncates under the same injection. Atomic rebuild of
  the real cache: valid, 2166 nodes, 0 sentinels, hole=1, no leftover .tmp; 4 siblings --check green.
- R4 census re-derived on my OWN grep: caught a 4th save() site the front pass missed
  (`extract_pipeline.py:1649`); re-derived denominator as invariant-not-integer ("every write goes through
  save()"). CTO corrected his brief's census, credited to me.
- Process note: acted on CTO's 164900Z "go in order" GO, completed the fix, then a 165431Z Andrew-direct
  sequencing correction STAGED comp-build. Preserved the diff as a patch, reverted to clean, held; re-applied
  on the 184620Z hand-down. Zero work lost.

## MCP traffic (significant only)

~11 messages handled (CTO<->me). Significant: CTO GO (cluster assignment); comp-blast GATE GREEN;
comp-build front-pass lead -> STAGED correction -> hand-down GO; comp-build GATE GREEN. Two COO
cleanup briefs sent (comp-blast, comp-build; scope NONE each). No broker re-surfaces counted.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-build | rebuild x3 (fix verification) | PASS | 1850/1851 indexed; exercised atomic save on real cache |
| comp-blast/trace/xref/diff | `--check` both states (clean + mutated) | PASS | unified predicate; all 4 STALE on drift, FRESH on revert |
| comp-blast | B5 both-arm mutant (edit bundle .py) | PASS | STALE names lambda:semantic-news-layer3-curation; revert -> FRESH |
| comp-which (HUD) | nudges observed | N/A | routed raw-grep to on-rails; my greps were §6 assurance oracles |

- **What worked:** the 4-sibling `--check` is a genuine shared-predicate probe -- one substrate fix
  rippled and all four confirmed green in both states.
- **What failed:** n/a (both fixes gated GREEN first pass).
- **Gap found:** none new in the tools; the residual hole=1 (`lambda:exec-summary-generator`, pycache-only)
  is an honest floor, flagged to CTO as a SEPARATE data-hygiene lead (source .py appears deleted).
- **Off-rail oracles:** raw `grep`/`python json.load` on the cache carried the NFRA_TOOLPASS sec.6
  marker (assurance oracle for a tool under test -- must not share the tool's predicate). Named exemption,
  not a coverage gap.

## Files Modified

See commit messages: `19e4177db` (trace_graph.py, extract_lambda_routes.py, tests/test_graphuni_headpin_d4.py),
`227c1651a` (trace_graph.py, cli.py). Both authored 3.0.0_SA_CVO~B, surface-check clean, pushed CLOUD.

## Blockers

None. comp-trace/xref/diff SEMANTICS are HELD (not blocked) -- gated on CTO's per-tool front pass, which
he hands down as he front-passes each. Nothing actionable by me on those until then.

## Current State

- Trace-graph cluster substrate (`org/modules/graph/trace_graph.py`) has: dir-aware source_sha
  (`_compute_path_sha`/`_compute_dir_sha`) AND atomic `save()` (temp+fsync+os.replace). `cli.py` `_get_graph`
  self-heal now WARNs. Both landed on CLOUD (HEAD includes `227c1651a`).
- `.comp-graph/graph.json` (gitignored) freshly rebuilt: 2166 nodes, 0 sentinels, 1850/1851 indexed,
  hole=1 (honest pycache residual). All 4 query tools `--check` rc=0.
- comp-blast + comp-build CLOSED end-to-end (CTO gated, COO briefed). 4 tools closed in the sweep overall
  (adapter-audit, aws, blast, build).
- Staged patch `scratchpad/comp-build-C1-staged.patch` already re-applied + committed -- no longer pending.

## Next Steps

- **[3.0.0_SA_CVO~B]** Hold for CTO's next per-tool front-pass hand-down (comp-trace, then xref, then diff).
  Re-run every falsifier on receipt; do not certify on the front-pass report.
- **[1.0.0_SA_CTO]** Front-passes comp-trace/xref/diff semantics (gated on Andrew's tool-ordering).
- **[Andrew]** Discretion on the out-of-cluster lead: `lambda:exec-summary-generator` source .py appears
  deleted, only .pyc lingers (data/infra hygiene, not a freshness defect).
