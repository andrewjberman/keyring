# MDPF_ASSETS.014 — WS-C Cohort_Class AMENDMENT-1 Re-Tag

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-19
**Branch:** CLOUD
**Project:** MDPF_ASSETS
**TO:** MDPF_ASSETS.014 (dispatched GO 2026-05-18, COO)

## Current State

COMPLETE — WS-C Inflection feeder natively emits `cohort_class` (registry-derived
via `model_key`) on `model_aua_positions` and `sma_aua_input` beside
`model_aua_input` on `non_model_aua`. Both 2026-05-18 artifacts re-landed in
`s3://opal-data-mdpf`; aggregator re-run confirms `meta.feeds_pre_amendment1`
is now empty (`{model_aua_positions: [], non_model_aua: []}`) and the section-7
DUAL `model_aua_input + sma_aua_input` check PASSES inflection. All 4 ACs met.
RAVC2 to COO.

## Files Modified

| File | Change |
|------|--------|
| `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py` | (a) `COLS_MODEL_AUA_POSITIONS` += `cohort_class` after `model_key_unmapped`; (b) `COLS_NON_MODEL_AUA` += `sma_aua_input` after `model_aua_input`; (c) `load_registry()` builds `eclipse_to_type` alongside `eclipse_to_key`; (d) `build_model_aua_positions()` derives `cohort_class = registry["eclipse_to_type"].get(eid_int)` — registry-derived per row, no hardcoded default; (e) `build_non_model_aua()` signature gains `sma_aua_input: float`, residual now subtracts BOTH managed sub-cohorts; (f) `method` updated to `inflection_eclipse_full_active_book_minus_opal_model_and_sma`; (g) `main()` computes `model_aua_input` (cohort_class='model') + `sma_aua_input` (cohort_class='sma') from positions, passes both to non_model build; (h) verification logging adds per-cohort breakdown + a section-7 DUAL self-check + a surfaced WARN for any `cohort_class=None` row (mirror WS-B "do not silently default"). |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `.tools/ds-commit-gate.sh build_mdpf_wsc_inflection_feeder.py` | PASS | `python -m py_compile` + AST undefined-name scan + ruff 0.15.11 — exit 0. |
| `comp-pipescript io build_mdpf_wsc_inflection_feeder` | Off-graph (script-not-found) | Same backlog item documented in `DS_B_session_summary` 2026-05-18 — `data/mdpf/scripts/` predates the compiler-cache build. Fell back to direct inspection per the TO `if_mismatch` clause. Resolution path: `comp-build` rebuild + cache refresh; surfacing again here. |
| `comp-blast build_mdpf_wsc_inflection_feeder` | "No nodes matching" — off-graph | Same root cause. TO `if_mismatch` predicate ("if the re-tag touches an ADVI_ECLDAT artifact, STOP") **not triggered**: this edit only touches `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py`; zero `data/orion/`, `infra/aws/lambda/inf-*`, or any ADVI_ECLDAT path. |

## Phase Evidence

### Phase 1 — Re-tag (write)

WS-B precedent mirrored — commit `24251a794` (DS~A, MDPF_ASSETS.007). Registry
lookup is `model_type` per registry entry (`mdpf_model_registry.json` v3). The
WS-C feeder iterates account rows (not registry rows like WS-B), so I added a
new `eclipse_to_type` map in `load_registry()` and look it up by `eid_int`
inside `build_model_aua_positions()`. Same null-handling rule as WS-B: a
registry entry with no `model_type` yields `cohort_class=None` (surfaced as
WARN at verification), never silently defaulted.

### Phase 2 — Re-run + re-land

Local dry-write at `--out-dir /tmp/mdpf_wsc_014`:

```
model_aua_positions columns: ['firm_id', 'partner_name', 'model_key',
  'model_key_unmapped', 'cohort_class', 'account_id', 'household_id',
  'as_of_date', 'model_value', 'custodian', 'source_pipeline', '_ingested_at']
cohort_class value counts: {'model': 399}
null cohort_class rows: 0
model_value total: 93603055.45

non_model_aua columns: ['firm_id', 'as_of_date', 'non_model_aua',
  'partner_custody_total', 'model_aua_input', 'sma_aua_input', 'method',
  'custody_scope', 'source_pipeline', '_ingested_at']
{firm_id: 'inflection', as_of_date: 2026-05-18,
 non_model_aua: 106112059.52, partner_custody_total: 199715114.97,
 model_aua_input: 93603055.45, sma_aua_input: 0.0,
 method: 'inflection_eclipse_full_active_book_minus_opal_model_and_sma',
 custody_scope: 'eclipse_administered_book'}
```

S3 upload (2026-05-19T14:01:59-14:02:01Z):
- `s3://opal-data-mdpf/mdpf/feeds/model_aua_positions/inflection/2026-05-18.parquet` (399 rows)
- `s3://opal-data-mdpf/mdpf/feeds/model_composition/inflection/2026-05-18.parquet` (168 rows, unchanged but re-uploaded for idempotency)
- `s3://opal-data-mdpf/mdpf/feeds/non_model_aua/inflection/2026-05-18.parquet` (1 row)

In-line verification log:
- model_aua_positions: 399 rows, model_value total $93,603,055.45, unmapped model_key rows=0
- Cohort 2a Opal Models: $93,603,055.45 (399 accounts)
- Cohort 2c Opal SMAs: $0.00 (0 accounts)
- section-7 DUAL: model_aua_input + sma_aua_input == Sigma model_aua_positions.model_value -> PASS (1a $93,603,055.45 + 1c $0.00 == $93,603,055.45)
- non_model_aua: $199,715,114.97 partner_custody - $93,603,055.45 model - $0.00 sma = $106,112,059.52

### Phase 3 — Consumer verify

`python data/mdpf/scripts/gold/mdpf_aggregate_aua.py --date 2026-05-18 --source s3 --dry-run`
(post-re-tag aggregator re-run, reading the freshly re-landed S3 feeds):

- `reconciliation.identity_1_aggregate_sum.status: PASS` (residual 0.0)
- `reconciliation.identity_1.model_aua_input_check.status: PASS` — detail: `"model_aua_input + sma_aua_input match the cohort_class sums for all firms"` (both 49financial AND inflection)
- `reconciliation.identity_2_etf_residual.status: PASS` (min_public_residual $2,089,090.53)
- `reconciliation.identity_3_no_double_count.status: PASS`
- `reconciliation.overall: PASS`
- `meta.feeds_pre_amendment1: {"model_aua_positions": [], "non_model_aua": []}` — WS-C/inflection no longer listed (the consumer-side surfaced-default is now a no-op, exactly as the TO predicted)
- `meta.model_registry_version: "3"`, `meta.unmapped_model_key_rows: 0`

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|----------|
| AC1: model_aua_positions emits cohort_class natively (registry-derived, not hardcoded); all 399 inflection rows resolve to 'model'; conformant to AMENDMENT-1 section 3.1 | PASS | Parquet schema includes `cohort_class`; value counts `{'model': 399}`; derivation is `registry["eclipse_to_type"].get(eid_int)` per row. |
| AC2: non_model_aua emits sma_aua_input ($0.00 for inflection) beside model_aua_input; conformant to AMENDMENT-1 section 4 | PASS | Parquet schema includes `sma_aua_input`; row carries `sma_aua_input=0.0`, `model_aua_input=93603055.45`. |
| AC3: both artifacts re-landed in opal-data-mdpf; model_aua(inflection) unchanged at $93,603,055.45; mdpf_aggregate_aua.py re-run confirms meta.feeds_pre_amendment1 no longer lists WS-C/inflection AND section-7 dual check PASSES inflection | PASS | S3 upload logged; aggregator output above shows empty `feeds_pre_amendment1` arrays, identity_1 PASS, model_aua_input_check PASS. |
| AC4: No emoji; ds-commit-gate exit 0 on every .py edit; Rule 15 where applicable; session log with Compiler Tools section; RAVC2 to COO | PASS | This file: no emoji; gate clean (above); Rule 15 already in effect (`from __future__ import annotations` is the first import in the feeder); Compiler Tools section above; RAVC2 below. |

## Deploy Ledger

| Step | Result |
|------|--------|
| Pre-commit gate | `.tools/ds-commit-gate.sh build_mdpf_wsc_inflection_feeder.py` -> All checks passed |
| Commit SHA | `56d056458` |
| safe-commit.sh | clean (single pathspec, no contamination) |
| Push | `46bb5b023..56d056458 CLOUD -> CLOUD` |
| S3 upload | 3 artifacts at `s3://opal-data-mdpf/mdpf/feeds/{model_aua_positions,model_composition,non_model_aua}/inflection/2026-05-18.parquet` |
| Consumer verify | `mdpf_aggregate_aua.py --date 2026-05-18 --source s3 --dry-run` -> overall PASS, feeds_pre_amendment1 empty |
| TO status | flipped to `complete` in same scope |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.014 complete. AC1-AC4 met. WS-C is now natively AMENDMENT-1-conformant; the `mdpf_aggregate_aua.normalize_amendment1()` surfaced-default for WS-C/inflection is a no-op going forward. A future Inflection SMA strategy buckets correctly via the registry path, not via consumer-side fallback. |
| **CTO comp-tools backlog (carry-over)** | `data/mdpf/scripts/` is still off the comp graph — `comp-pipescript io` + `comp-blast` both return "(not found)" / "No nodes matching" for the WS-C feeder. A `comp-build` rebuild would close this; flagged again here (also flagged in DS~B 2026-05-18 session summary). |
| **DS~B (self)** | Idle — watchdog standby. No further pending DS~B-lane TOs. The other open MDPF TO (`MDPF_ASSETS.016.ds-cohort0-historical-backfill`) is assigned to base `0.4.0_DS_ClientPlatform` (DS Base), not my lane. |
