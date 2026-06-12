# NFRA_DEBTSCAN — PRD-request brief: employing the global graph for tech-debt, dead-path, canon-deviation, and latent-risk scanning

**Author:** 3.0.0_SA_CVO (Andrew-direct request 2026-06-12 ~17:55Z) · **For:** 1.0.0_SA_CTO (PRD + macro project code NFRA_DEBTSCAN) · **CC:** 2.0.0_SA_COO
**Status:** brief / PRD-request — CTO authors the PRD; nothing here is binding spec.

## 1. Objective (Andrew, paraphrased)

Put the graph system to the test against the whole estate: find **tech debt**, **dead paths**, **out-of-pattern / unusual routes** (weed complexity and canon-breaks), and **latent bugs / risk factors** — systematically, from the graph, not from ad-hoc greps.

## 2. Why this is tractable NOW (and wasn't three weeks ago)

- **The substrate exists and is certified.** The unioned stitch (pipeline + aws + portal, ~3,100 nodes / cross-layer edges) is live in Kuzu; comp-aws is existence-F1 = 1.0 against live oracles (COMPAWS Wave-4); the freshness contract (F1–F6) means a scan provably runs against HEAD, not a stale vintage — with the provenance header to prove it per run.
- **History is queryable.** Nessie versioning means debt questions get a TIME axis: when did this path die, how long has this orphan existed, is debt accreting or burning down (diff N snapshots; `graph_metrics` per-class trend).
- **The scan engine is piloted.** NFRA_GRAPHS D7 (closed today) built exactly the right machine shape: finding-families, per-finding triage (real / FP / expected-by-design / coverage-gap), graded severity, day-0 baseline. DEBTSCAN is substantially **D7 generalized from 5 critical surfaces to the whole graph**, plus new finding-families.

## 3. The four scan families — mechanics + known-incident anchors

### 3a. Dead paths (reachability sweeps)
Forward-reachability from the entry-point set (CloudFront routes, gold dispatcher lines, EventBridge rules, cron/SSM triggers) — anything unreached is a dead-path candidate. Backward from served artifacts — anything unfed is a never-written/stale candidate.
- Known classes this catches, each with a live precedent: dispatch-orphan gold scripts (the inf bare-vs-`INF_` 29-file shadow set; orphan D_04), fetches with no resolving route (`getAUMMetrics`, DE day-0), TF-unmanaged live residue (`comp-aws` LIVE-no-DECLARED currently ~320; the `77005oklok` API-GW class), S3 keys written-never-read, Lambdas with zero invocations + zero graph in-edges.
- **Hard doctrine carried in:** candidates are NEVER auto-deleted. The verify-before-delete chain is banked memory: orphan→orphan invocation chains (`_run_script` sub-publishers), name-vs-edge blast radius (the trade-recon teardown 4-layer gate), bare/canonical twin sets across firms. A dead-path finding routes to its owner with the trace, period.

### 3b. Tech debt (structural-duplication + layer-violation census)
- Duplicated subgraphs: near-identical script/artifact chains that should share a lib (the bd/cot canonical-twin vs fork-shadow distinction matters — twins are DESIGNED, shadows are debt).
- Layer violations: gold reading bronze directly past an existing silver; silver scripts carrying business logic (Rule 17 violations — `output_cols` projections, fillna classes); components fetching S3 directly past the route layer.
- Version coexistence: v1/v2 endpoints or scripts both live with consumers split across them (the LEGACY-CSV vs NEW-REST dual-writer class — ADVI_DWSPLT's "different data" incident).
- Config drift: same logical constant materialized in N places with M values (the INFLECTION_REP_IDS x5 drift found this week).

### 3c. Out-of-pattern routes (canon-deviation / motif mining)
Define **canon as a library of named Cypher path-patterns** (extend `graph-call-manifest.yaml`): pipeline canon = bronze→silver→gold→platinum→S3→route→component; auth canon = route→Lambda@Edge→S3; deploy canon = repo→S3-code→runner. Then:
1. Enumerate every concrete instance of each pattern-class in the graph; score against canon.
2. Motif-frequency outliers: edge-type combinations or path shapes occurring 1–2 times where a dominant motif occurs N times are *unusual-by-construction* — exactly Andrew's "series where a route is out-of-pattern."
- Live precedents this would have caught structurally: the Lambda@Edge gate keyed on a pre-rewrite URI (silent no-op guard); dual-writers to one artifact; a cross-firm bucket reference; an EC2 service as the only reader of a bucket no canon path touches.

### 3d. Latent bugs / risk factors (compositional analytics)
Mostly **composition of existing certified tools, run estate-wide instead of per-incident**: `comp-pipescript io` column-gaps (accessed-not-loaded — the geo_drill/fee_earning $0 class) across all 71+ gold scripts; `comp-iam gaps` (boto3-call-without-permission — the s3:DeleteObject watchdog loop); `comp-cache collisions`; auth=NONE fetch edges (DE's day-0 FP shows the triage shape); postdeps-missing (the $22M phantom-override class). Plus graph-native risk metrics: betweenness-centrality hotspots (one node feeding many SEV1 surfaces = concentration risk), no-freshness-contract artifacts, high-author-churn nodes, single-writer-no-oracle artifacts.
- **FP discipline is the make-or-break.** Banked FP classes go in the scan config as suppressions-with-reasons: `Deny`+`Principal:*` is a guardrail not a public grant; expected aliases in schema-checks; designed twins. Every family ships with a sampled precision gate (the comp-aws score-vs-oracle pattern) before bulk-filing.

## 4. Outputs

- **Graded findings ledger** — same shape as D8-findings.md: family, severity, firm-scope, triage state, owner-routed. Suggest registry at `org/modules/graph/debtscan/` with per-sweep dated findings files; SEV-tiering reuses the D8 vocabulary.
- **Burn-down trend** — per-family counts written to `graph_metrics` per scan, so Nessie history shows debt accreting/burning across weeks. This is the number Andrew can watch.
- **Relationship to org/critical_paths/** (the ledger system requested earlier today): DEBTSCAN findings touching a critical-surface subgraph ALSO land in `org/critical_paths/change_management/` per that spec; the two systems share the carve machinery and severity vocabulary but DEBTSCAN is estate-wide and advisory, while critical-paths is surface-scoped and gating.

## 5. Suggested phasing (CTO's call)

- **P1 — Reachability + composition sweeps** (cheapest, highest precision): dead-path forward/backward sweeps + the 3d tool-composition runs estate-wide. Mostly existing machinery; output = first ledger + first precision measurement.
- **P2 — Canon library + motif mining**: author the canon pattern library (CTO authority — this IS an architecture artifact), build the scorer, run deviation census.
- **P3 — Risk analytics + trend automation**: centrality/churn/concentration metrics; scheduled (nightly-piggyback, no manufactured runs); burn-down into graph_metrics.

## 6. Open questions for the PRD

1. Owner lanes: D7's pilot was DE; estate-wide sweeps touch every pod's lane — findings-routing protocol needs COO design (suggest: scan-runner files, owners adjudicate, nothing auto-fixed).
2. Cadence + cost: scheduled sweeps should ride the nightly graph refresh (LD-0176 — no manufactured derives); ad-hoc sweeps are QUERY-class (cheap, Kuzu-local).
3. Precision bar per family before a family's findings are filed as more than ADVISORY (suggest: sampled precision ≥0.8 measured by CVO adjudication, mirroring the COMPAWS cert pattern).
4. Whether portal-side debt (unused components, dead exports) is in-scope P1 or rides comp-graph's existing surface.

— 3.0.0_SA_CVO
