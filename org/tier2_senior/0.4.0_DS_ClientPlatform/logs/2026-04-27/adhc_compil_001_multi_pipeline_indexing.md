# Session Log — 0.4.0_DS_ClientPlatform — 2026-04-27

## Work Item: ADHC_COMPIL.001 — Multi-Pipeline Indexing

### Commit
`39fafc6a` — pushed CLOUD

### Objective
Extend comp-pipescript graph builder to index INF gold + BD/INF silver + bronze layers
alongside existing BD gold indexing. Required foundation for ADHC_COMPIL.005
(nested-key reverse lookup).

### Implementation Summary

**New public API (`extract_pipeline.py`)**:
- `build_inf_gold_dag(workspace_root)` — reads orion-gold-dispatch.sh catalog, walks INF gold scripts, detects I/O via module-constant resolver + hardcoded path scanner
- `build_silver_dag(workspace_root, pipeline_label, script_dir_rel)` — walks any silver directory, pipeline-agnostic
- `build_multi_pipeline_dag(workspace_root)` — merges all four DAGs with namespaced IDs (bd-gold:D_04, inf-gold:D_04)

**Module-constant resolver** (new mechanism):
- `_extract_module_s3_constants(content)` — finds `UPPERCASE = 'gold/...'` module-level assignments
- `_extract_s3_calls_with_constants(content, module_constants)` — resolves variable-based S3 calls like `_write_json_s3(obj, TIMESERIES_CHART_KEY)` and `_read_s3_parquet(SILVER_ACCOUNTS_DIM)`
- Required because INF scripts don't use `lib/s3_layout.py` — keys are module-level constants

**pipeline_cli.py**:
- `--pipeline` / `-p` flag on dag, io, chain, feeds, consumers, overlap, deployed
- `_build_dag()` routes to correct builder based on pipeline choice
- `cmd_deployed()` extended for inf-gold (uses inf-gold-layer-runner from EC2_MANIFEST)
- All output nodes labeled with [bd-gold], [inf-gold], [bd-silver], [inf-silver]

**ScriptIO dataclass**:
- Added `pipeline: str = "bd-gold"` field (backward compat — defaults to bd-gold)

### AC Verification

```
AC #1 — comp-pipescript io data/orion/scripts/gold/D_04.client_portal_summary.py --pipeline inf-gold
  READS: gold/artifacts/firm_mix_views.json, silver/accounts_dim/latest.parquet, gold/timeseries/client_performance.parquet
  WRITES: platinum/firm/timeseries_overview.json, platinum/firm/dashboard.json, platinum/firm/header_metrics.json, gold/artifacts/summary/header_metrics.json, platinum/firm/partner_analytics_{*}.json
  STATUS: PASS

AC #2 — comp-pipescript io convert_assets_to_silver --pipeline bd-silver
  WRITES: silver/bd_assets.parquet
  STATUS: PASS

AC #3 — comp-pipescript io convert_orion_to_silver --pipeline inf-silver
  READS: silver/meta/trn_watermark.json
  WRITES: silver/meta/gap_manifest.json, silver/meta/trn_watermark.json
  STATUS: PASS

AC #4 — Pipeline labeling ([bd-gold], [inf-gold], etc.) visible in output
  BD gold D_04 pipeline='bd-gold', INF gold D_04 pipeline='inf-gold', BD silver pipeline='bd-silver'
  STATUS: PASS

AC #5 — comp-pipescript deployed <any INF gold script> vs inf-gold-layer-runner
  Routed to inf-gold-layer-runner (i-0ed5afded2ebd4ed4) from EC2_MANIFEST.json
  STATUS: PASS

AC #6 — Existing BD-gold behavior unchanged
  build_pipeline_dag() signature unchanged, all 28 BD gold scripts load correctly
  STATUS: PASS

AC #7 — >=5 new test fixtures
  20 fixtures across 5 test classes: TestInfGoldScriptIO (6), TestBdSilverScriptIO (3),
  TestInfSilverScriptIO (4), TestCrossPipelineEdge (4), TestPipelineLabeling (3)
  All 20 PASS with extension. All 20 FAIL (ImportError/AttributeError) without extension.
  File: org/modules/graph/tests/test_multi_pipeline.py
  STATUS: PASS
```

### Pre-commit gate
`ds-commit-gate.sh extract_pipeline.py pipeline_cli.py tests/test_multi_pipeline.py` — CLEAN (3 ruff warnings fixed: unused `esc` variable, two f-strings without placeholders, unused `e` in except)

### RAVC4 Sent
- 2.0.0_SA_COO (2026-04-27)
- 1.0.0_SA_CTO (2026-04-27)
