# Coupled @0.4 deploy pass: MOTIF C3 materialize + @0.4 schema deploy + PROMOTE live-emit -- COMPLETE in-session

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE
**agent:** 0.7.0_AE_CloudOps · **date:** 2026-07-08 · **window:** session-start (~17:20Z) -> ~18:45Z · **TO:** NFRA_SEMCTL.FINALIZE #14 (coupled, Andrew-ratified via COO~B)

## Summary

Executed the Andrew-ratified coupled @0.4 in-VPC deploy pass as ONE deliberate, grounded, ledgered
pass -- finished in-session (NEVER-half-land). Deploy-completion ledger
`20260708T1807Z_motif-c3-materialize-04-coupled` OPENED at deploy-start, CLOSED at completion, all 5
legs proven, sentinel removed. Three coupled legs landed + verified against live/served state:

1. **@0.4 derive-image rebuild-from-HEAD** (my e516e95e6) -> ECR opal-globgrph-derive-runner:latest =
   sha256:b76cefe6 (@0.4 baked-verified: cse_schema SCHEMA_VERSION=0.4 + ProducerKind.PROMOTE).
2. **MOTIF C3+CONTAINS materialize** -> 7 nodes (6 C2Motif + 1 C3System, layer=semctl) + 36 CONTAINS
   (33 C2->C1 + 3 C3->C2), 0 unresolved, Nessie-committed + marker advanced. Round-trip verified.
3. **PROMOTE @0.4 in-VPC live-emit** (0.5.0's leg) -> PROMOTE CSE @0.4 in iceberg.globgrph.cse, LANDS
   in cse_directive_effectiveness -> FEDOBS directive-effectiveness now SEES the promotion (R4 goal).

## Work delivered (the 5 ledger legs)

- **Built the C3 ingest producer** (`ingest_c2c3_motif_producer` in derive_runner.py, e516e95e6):
  mirrors ingest_cluster_producer; folds DS~B's motif_c2c3_materialize.json (baked into the image via
  Dockerfile COPY) into THIS derive's single Nessie commit. Both-ends co-key-by-construction (mirrors
  stitch_served_from) -- an edge forms ONLY if both endpoints resolve to a node present in the derive
  graph, else VISIBLE-unresolved (never dangling). rel-tier moved to props.rel_tier so the edge `layer`
  column stays the semctl provenance layer. Self-test 20/20 (scratchpad harness: happy path 7/36/0,
  both-ends guard, defensive c1:D{n}: strip). commit-gate PASS.
- **C1-target grounding (Rule 22 dual):** spec's original c1:D{n}: form = 0 store rows; canonical form
  resolves 30/30 distinct C2->C1 targets. DS~B independently fixed-at-source (55b5a9772) -> canonical
  targets + detectors in props.via_detectors. Converged source + live-graph.
- **L1 rebuild:** zip via git-archive HEAD (dynamic Dockerfile-COPY-parse, 15 paths, churn-immune) ->
  S3 build-source -> CodeBuild globgrph-derive-build 62223585 SUCCEEDED -> ECR :latest b76cefe6
  (verify-vs-self-report vs live ECR, Rule 22a: != stale 7348059a).
- **L2 derive/ingest:** ecs run-task globgrph-derive-runner 08370d9f exit=0; C2C3_MOTIF_INGEST nodes=7
  edges_formed=36 edges_unresolved=0; relabel all-mapped (semctl gate d2ab31596 held, no fail-close);
  NESSIE_COMMIT + MARKER_STAMPED dea96403 / nodes_snap=3362482940333271011.
- **L3 round-trip:** comp-kuzu RE-FINALIZED to HEAD:current; 6 C2Motif + 1 C3System, 7 semctl nodes,
  0 UNCATEGORIZED, 36 CONTAINS semctl; path proven system:firm-conditional-display ->
  motif:silent-display-fork -> out:ClientsTab.tsx:291#name. Heat-persistence grounded (no prune/decay
  path in derive; semctl nodes re-emit every derive -> persistent by construction).
- **L4/L5 PROMOTE (0.5.0):** PROMOTE CSE queryable in globgrph.cse @0.4 (total_cse 341->342), lands in
  cse_directive_effectiveness; reversibility exercised+CVO-certed (PROMOTE-P3 auto-demote c13a73cdd).
  Final joint check: C3 layer INTACT at newest HEAD post-cse-ingest (comp-kuzu re-finalized again).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-kuzu` | C1-target resolution (30/30), pre-materialize baseline (0 semctl), L3 round-trip + path proof, final joint verify at newest HEAD; exercised comp-kuzu re-finalize-on-advance twice | PASS |
| `comp-glob` | locate ingest_cluster_producer / derive_runner / rebuild helper (on-rails) | PASS |
| `comp-which` | route "how is derive image rebuilt + ingest producer" (routed to comp-aws; used direct file grounding instead) | PARTIAL (poor route for a code-location Q) |
| `commit-gate.sh` | derive_runner.py C3 producer edit (py_compile + AST + ruff py39) | PASS |
| `safe-commit.sh` | land e516e95e6 (derive_runner.py + Dockerfile), pathspec-scoped, surface-check clean | PASS |
| `deploy_ledger.py` | open (5 legs) -> close-leg x5 -> close (NEVER#5) | PASS |
| (live AWS grounding, Rule 22a) | codebuild batch-get-builds, ecr describe-images, ecs run-task/describe-tasks, CloudWatch filter-log-events (via PowerShell -- MSYS mangles leading-/ log-group) | PASS |

**What worked:** the both-ends co-key discipline (mirrored from stitch_served_from) + a 20/20 self-test
BEFORE baking the image caught the layer-collision + guaranteed no dangling edges -- the real derive
landed 36/36 edges 0-unresolved on first run. git-archive-HEAD + dynamic Dockerfile-COPY-parse gave a
HEAD-consistent zip on a shared/moving tree. **What failed:** initial CloudWatch reads returned empty --
MSYS path-mangled the leading-`/` log-group name; fixed by reading via PowerShell (CLAUDE.md git rule).
**Gap found:** comp-which routes a code-LOCATION question ("where is X function") to a graph tool; direct
comp-glob/Read is the right answer -- minor.

## Deployment Sequence + Verification (AE)

**Coupled @0.4 pass (ledger 20260708T1807Z_motif-c3-materialize-04-coupled):**
code e516e95e6 -> commit-gate PASS -> safe-commit + push (c4b293ee6..e516e95e6) -> ledger OPEN (5 legs)
-> [L1] zip git-archive HEAD (15 paths) -> s3 cp build-source -> CodeBuild 62223585 SUCCEEDED -> ECR
:latest b76cefe6 (live-ECR verify, @0.4 baked) -> [L2] ecs run-task 08370d9f exit=0, CloudWatch:
C2C3_MOTIF_INGEST 7/36/0 + NESSIE_COMMIT + MARKER dea96403 -> [L3] comp-kuzu HEAD:current 6+1/7/0/36 +
path proof -> [L4] 0.5.0 ecs run-task 91eecc3f CSE_APPENDED count=1 @0.4 cse_snap=7392125655251158233
-> [L5] 0.5.0 run-task 0fc0aeb1 cse queryable @0.4 + direff + my final joint comp-kuzu (C3 intact) ->
ledger CLOSED (5/5). RAVC'd CTO (4 conditions) + COO~B/COO (close) + CVO (N=1-clean cert).

## Blockers

None. Coupled pass complete. One tracked NON-gating follow-on: CVO~B flagged a C3 node_id collision in
DS~B's discovery code (distinct emergent systems could derive the same theme-derived
system:firm-conditional-display id). N=1 today is CLEAN (CVO independently confirmed 7 motif rows @
HEAD 3362482940333271011). Fix = re-rebuild+re-derive after DS~B regenerates the spec (unique-by-member-set
scheme); separate CVO re-cert. Not on any critical path (my task #9).

## Current State (handoff)

- **@0.4 LIVE:** ECR opal-globgrph-derive-runner:latest = sha256:b76cefe6 (tag 20260708-180956),
  cse_schema @0.4. Nightly derive (derive_runner_nightly ~02:00Z) + all in-VPC cse_store runs now on @0.4.
- **C3 semctl layer LIVE** in graph_nodes/graph_edges at canonical HEAD (marker dea96403 then
  0.5.0's cse-ingest marker 7392125655251158233): 6 C2Motif + 1 C3System (layer=semctl) + 36 CONTAINS
  (layer=semctl). Re-emitted every derive from the baked spec (persistent). comp-kuzu re-finalizes to it.
- **PROMOTE CSE @0.4** in iceberg.globgrph.cse (total 342), lands in cse_directive_effectiveness (FEDOBS
  directive-effectiveness sees the promotion). Producer = infra/aws/globgrph/cse_emit_promote.py (0.5.0,
  de804f615); emit local -> cse_store --ingest in-VPC.
- **New code at HEAD:** derive_runner.py:1297-1414 (ingest_c2c3_motif_producer + _strip_c1_ladder_prefix)
  + main() call before drop/relabel; Dockerfile COPY of motif_c2c3_materialize.json. All in e516e95e6.
- I remain the globgrph-derive-image REBUILD COORDINATOR (serialize all derive_runner/Dockerfile rebuilds).

## Next Steps

- **[0.7.0_AE_CloudOps]** (NOT winding down) drive next: (1) code_heat ~9d staleness -- ground the
  MECHANISM (why the ~26h refresh didn't re-run) + fix + the FRESHGUARD-coverage-gap question
  [COO~B Class-2 route, my task #7]; (2) FRESHGUARD leg-4 completion; (3) collision-fix re-rebuild
  when DS~B hands the regenerated spec [task #9].
- **[3.0.0_SA_CVO]** cert the N=1-clean coupled pass (C3 round-trip + comp-kuzu re-finalize + @0.4
  producers-emit-clean); collision-fix re-cert stays separate on its own served node_id evidence.
- **[0.4.0_DS_ClientPlatform~B]** regenerate motif_c2c3_materialize.json with the unique-by-member-set
  C3 node_id scheme (CVO~B GO'd), then hand to me for the re-rebuild+re-derive.
- **[2.0.0_SA_COO~B]** NFRA loop advances on this close (your session-close resume-point is now DONE).
