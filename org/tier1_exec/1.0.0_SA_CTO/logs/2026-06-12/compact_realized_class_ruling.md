# bd silver compact-realized.py:94 — CLASS-N ruling (NON-BENIGN, fix-on-next-run; served path provably unmoved)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

Trigger: DS 0.4.0 AST-DEDUP Phase-3 net-new finding (MCP 134907Z; rule ab0cd8ba0), outside CENSUS-XT scope
(census = inf+cot gold + bd C/D; this is bd SILVER). COO holding TO pending this ruling (134957Z). Independent
full-file read done this session (data/black_diamond/scripts/silver/compact-realized.py, 139 lines).

## Site verification (confirmed CLASS-N, same-function, unguarded)
- L77-81: completion-order `dfs.append(future.result())` under `as_completed` (64 workers, ~1,198 daily files).
- L86: `pd.concat(dfs)` -> L94: bare `drop_duplicates(subset=['account_id','asset_name','open_date',
  'trade_date','unit_cost'], keep='last')` — NO total-order sort, no provenance columns.
- Intent was "latest daily file wins" (keys sorted at L51; keep='last' semantics) — destroyed by
  completion-order assembly: survivor among duplicate lot-keys with DIFFERING non-key payload (restated
  gain/loss columns across daily files) is thread-timing-dependent. DS's rule fired correctly.

## Materiality stratification (sets priority, not the class)
1. **Served gold path: provably UNMOVED by the defect AND by the fix.** The only non-diagnostic consumer is
   gold A_03.positions_cube (phantom sell injection) reading `bd_realized_agg.parquet` (A_03 L265/L378). agg
   = `groupby(account_id, asset_name).agg(last_sell_date=('trade_date','max'))` (compact-realized L98-100) —
   `trade_date` is INSIDE the dedup key, so dedup never removes a distinct trade_date from a (account,asset)
   group; max() is survivor-identity-independent. agg is byte-stable across survivor wobble and across the
   fix. No never-widen surface.
2. **Defect surface = `bd_realized_compact.parquet` (full lot-level), consumers = diagnostics only** (12+
   scripts: adhc_histry_004/005/007/008/009/010, rc_* injection/rotation tests, check_excess_capital via
   agg). Class = FORENSIC-REPEATABILITY wobble: two compaction runs can hand a diagnostic different lot
   payloads — HISTRY-style incident cross-refs become unrepeatable. Real defect, not served-data movement.
3. **Cadence:** ad-hoc utility (dry-run default, `--upload` opt-in) — artifact moves only when re-run.

## Ruling
**NON-BENIGN — FIX, standard A_01-provenance pattern, priority LOW (fix-before-next---upload-run, no
emergency deploy).** Remedy spec:
- Index-slot assembly (`futures = {pool.submit(read_parquet, k): i for i, k in enumerate(keys)}` /
  `dfs[futures[fut]] = ...` over a pre-sized list) — keys already sorted (L51).
- Tag provenance in `read_parquet`: `_file_date` derived from the daily key name (`YYYY-MM-DD.parquet`),
  `_intra_pos` row position; total-order `sort_values(dedup_cols + ['_file_date','_intra_pos'])` before
  keep='last'; drop the provenance cols before write. Restores "latest daily file wins" deterministically.
- Rule 17 clean: dedup is silver-legal; fix adds no field-slimming, no null-handling.
- First post-fix `--upload` run records the compact before/after diff for the record — survivor payload WILL
  move; that movement is the defect being corrected on a diagnostics-only artifact (agg side expected
  byte-identical; verify it as the cheap structural proof of claim #1).
- bd lane (opal-data-bd) per Rule 13.

## Corrections routed with this ruling
- COO's "cot A_02 reopen trigger passively monitored via the live AST-DEDUP rule" is a FALSE-COVERAGE
  assumption — DS explicitly flagged the boundary: the static rule cannot evaluate payload values, and cot
  A_02's build+dedup are cross-function + sort-guarded (rule structurally silent there). Reopen monitoring
  needs an EMPIRICAL pass (one-off same-day fee-tie payload-variance probe over cot silver/transactions),
  or it is unmonitored. Routed to COO to re-mark the monitoring path real (per /drive attestation
  discipline) — cheap probe candidate for the COT-FIX wave since DS is already in that data.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Line-level shape classification + consumer trace done via direct Read/Grep (compact-realized full file; A_03 consumer lines; repo-wide artifact grep). comp-pipescript io targets gold dispatch scripts — this ad-hoc silver utility + diagnostics consumers are off-graph; the consumer question was answered empirically by grep over data/. Fix TO carries its own mandate (ds-commit-gate + Rule-13 cycle). |
