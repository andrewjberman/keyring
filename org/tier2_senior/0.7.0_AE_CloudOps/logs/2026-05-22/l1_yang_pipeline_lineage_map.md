# Session Log — 0.7.0_AE_CloudOps — YALP_MDSRC.L1 — 2026-05-22

## Summary

YALP_MDSRC.L1 — yang-pipeline mirror-image lineage map (I lead; 0.3.0_DE
co-owns the React side). ~3-5 day TO. This session: Phase-1 survey complete +
**Deliverable A complete + committed**. Deliverable B (the mirror-image map)
is set up for continuation below.

## Progress

| Item | Status |
|------|--------|
| Phase 1 — survey (comp-graph schema, extractors, yang scripts) | COMPLETE |
| Deliverable A — Yang-scripts structured rubric | COMPLETE — `287502c28` |
| Deliverable B — write-side map (yang Lambda -> source -> S3) | COMPLETE (artifact-grain) — checkpoint this session |
| Deliverable B — extractor gap diagnosis | COMPLETE — root cause pinned (see below) |
| Deliverable B — read-side map (S3 -> CF route -> React) | NOT STARTED — next phase |
| comp-graph extractor FIX (implement) | NOT STARTED — next phase (scoped) |

## Session 2 (2026-05-22 cont.) — write-side map + extractor gap

Artifact: `docs/reference/yang-pipeline-lineage-map.md`.

**Write-side map COMPLETE at artifact granularity.** All 27 yang-pipeline Lambdas
enumerated from `infra/aws/terraform/yang-pipeline/lambdas.tf` (ground truth).
14 portal-data generators mapped to their output S3 key(s) + procurement source +
manifest trigger; 12 orchestration/state Lambdas mapped; 3 cross-pipeline feeders
(SmartX sidecars, FRED cache, BD aum-metrics) identified.

**Stale-doc finding:** in-repo `LAMBDA_REGISTRY.md` + `PORTAL_DATA_FLOW.md`
(2026-01-19) are stale on folder paths AND output keys (e.g. CMA writes
`json/capital-markets/{assumptions,views}.json` not `json/cma/*`; macro-timeseries
writes a `json/macro/timeseries/` prefix; etf-returns -> `json/benchmarks/`).
Lineage-map artifact supersedes them.

**Extractor gap diagnosed (AC4 groundwork).** `comp-trace yang-generate-valuation`
returns 0 edges; comp-graph has all 27 yang LAMBDA nodes but only 4 edges touch
them, 0 WRITES_S3. Root cause: `extract_s3.py` Lambda branch does not resolve
module-level constants — yang generators write via `Key=key` (variable holding
`OUTPUT_KEY` constant); regex captures the bare name `key`, discarded at the
`'/' in key` filter. Gold branch resolves constants but only from
`gold/lib/s3_layout.py`. Fix scoped in artifact §3 (extension, not new compiler).

## Compiler Tools (session 2)

| Tool | Use | Result |
|------|-----|--------|
| `comp-trace yang-generate-valuation --direction both` | verify yang edge coverage | 0 up / 0 down — confirms extractor gap |
| direct `graph.json` inspection | enumerate yang nodes/edges | 27 LAMBDA nodes, 4 edges touching yang, 0 WRITES_S3 |
| `grep` over yang lambda source | write-side key + procurement extraction | OUTPUT_KEY constants + put_object/get_object patterns mapped |

## Phase 1 — survey findings

**comp-graph** (`.comp-graph/graph.json`, 1.28MB): 1952 nodes, 2143 edges.
- Node container = dict keyed by id. `node_type` values: `GOLD_SCRIPT` (1219),
  `LAMBDA` (306), `S3_ARTIFACT` (184), `ENDPOINT` (162), `EVENTBRIDGE` (56),
  `COMPONENT` (25). Node fields: id, node_type, label, file_path,
  function_name, run_order, metadata, source_sha.
- Edges = list of {source, target, edge_type, metadata}; edge_type e.g. `CALLS`.
- The node model L1 needs (LAMBDA / S3_ARTIFACT / ENDPOINT / COMPONENT) ALREADY
  EXISTS — L1's job is verifying + completing the yang-pipeline edges, not a new
  compiler. Only 25 COMPONENT nodes — the React-component coverage is likely
  the thinnest edge class (0.3.0_DE's half + an extractor gap to assess).
- Extractors: `org/modules/graph/extract_{api,eventbridge,iam,lambda_routes,
  pipeline,routes,s3,transforms,validate}.py`.

**yang-original-scripts**: 2 notebooks — see Deliverable A.

## Deliverable A — Yang-scripts structured rubric (DONE)

`docs/reference/yang-original-scripts/YANG_SCRIPTS_RUBRIC.md` (`287502c28`).
Full dc_index (10 groups / 84 instruments) + dc_macro (13 groups / 84 series)
Bloomberg ticker maps, dc_fields_all (13 field codes), the 3 pulls + data-pkl
structure; the regression notebook — 5 models, BENCHMARKS, 6 FACTOR_SPREADS,
the drift-adjusted model-return + rolling-regression methodology + model-pkl
structure. Satisfies AC1.

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| direct `graph.json` inspection | survey the comp-graph node/edge model | Node types + edge schema enumerated (above). |
| `comp-trace` / `comp-pipescript` / `comp-routes` / `comp-transform` | Deliverable B building blocks | NOT YET RUN — Deliverable B work. |

## Deliverable B — setup for continuation

The mirror-image map, both directions per data point, atomic + grouped:
1. **Write-side** — enumerate the yang-pipeline producer Lambdas (yang-pipeline
   terraform `infra/aws/terraform/yang-pipeline/`, source `infra/aws/lambda/
   v2_portal/yang_pipeline/`). For each: `comp-pipescript io` / `comp-trace`
   -> the S3 bucket+key it writes + the procurement source (cross-ref the Yang
   rubric for Bloomberg origin; note SmartX/FRED divergences e.g. B3 daily-direct).
2. **Read-side** — for each yang S3 artifact: `comp-pipescript consumers` /
   `comp-platinum reverse` -> the portal-publisher Lambda -> ENDPOINT ->
   COMPONENT. The React-component leaf is 0.3.0_DE's half (coordinate).
3. **Extractor gaps** — if the COMPONENT edges are thin, extend
   `extract_transforms.py` / `extract_routes.py`; flag COO before any net-new tool.
4. **Atomic + grouped** — emit data-point-by-data-point + the 3 roll-ups
   (by component / by lambda-read / by lambda-write). Cross-check the "Data
   Refresh" portal page.

## Current State

L1 Deliverable A shipped. Deliverable B write-side map COMPLETE (artifact-grain)
+ extractor gap diagnosed — committed as `docs/reference/yang-pipeline-lineage-map.md`.
Remaining: implement the extractor fix, build the read-side map, emit atomic
field-grain detail + the 3 grouped roll-ups, RAVC2. Multi-day TO (~3-5d SLA).

## Next Steps

1. [~self] Implement the `extract_s3.py` Lambda-constant-resolution fix (artifact
   §3) — module-level constant map + `key = CONSTANT` alias; rebuild graph;
   re-verify with `comp-trace`. Lights up yang WRITES_S3/READS_S3 edges.
2. [0.3.0_DE_TradingOperations] React-component side: which granular component
   renders which datum; the "Data Refresh" page as a visibility source.
3. [~self] Deliverable B read-side map (S3 -> CF `/api/public/*` route -> React)
   + atomic field-grain write-side (cross-ref Yang rubric) + the 3 grouped
   roll-ups (best emitted from the fixed comp-graph).
4. [~self] RAVC2 to COO on the full lineage-map artifact.
