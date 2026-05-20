# DS~B Session Log -- MDPF_ASSETS.024 rework + .025 WS-E re-scope

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TOs:** MDPF_ASSETS.024 (rework) + MDPF_ASSETS.025 -- landed together per COO~B GO (16:27Z)

## Summary

COO~B GO 2026-05-20 16:27Z re-issued the MDPF data lane to DS~B: .024-rework +
.025 (land together) -> .016 re-run -> .022. This log covers .024 + .025.

Both ship the Andrew 2026-05-20 PRD v0.8 taxonomy: Cohort 1c (SMA) is a
SUB-SLICE of Cohort 1b (non-model), not a disjoint sibling. Headline
`opal_aggregate_aua` = 1a + 1b + 2a (1c is non-additive, inside 1b).

### MDPF_ASSETS.024 -- aggregator headline rework

70e73d4e8 (base DS) shipped a half-corrected state: the docstring described the
PRD-v0.8 two-way taxonomy, but the code body still did the 3-term
`total_aua = model_aua + sma_aua + non_model_aua`. CTO~B's validation verdict
was REWORK. Applied the correction to `mdpf_aggregate_aua.py`:

- `build_partners`: `total_aua = model_aua + non_model_aua` (2-term; dropped the
  `+ sma_aua` double-count). sma_aua stays as a non-additive reported sub-slice.
- `reconcile` sentinel-3 (2nd-producer cross-validation): independent recompute
  filters `cohort_class == 'model'` only (was `isin(['model','sma'])`) -- so the
  SMA is not summed separately; otherwise it double-counts ~$25M.
- Headline-formula string + all `1a+1b+1c+2a` comments -> `1a+1b+2a`.
- Fixtures (`mdpf_aggregate_aua_fixtures.py`) re-baselined: 49F NON_MODEL
  `non_model_aua` 70M -> 90M (SMA-inclusive 1b); `aggregate.non_model_aua`
  assert 100M -> 120M; total_aua label `model+sma+non_model` -> `model+non_model`.

### MDPF_ASSETS.025 -- WS-E full-book re-scope

`build_mdpf_wse_49f_non_model_aua.py` re-scoped to Andrew Ruling 2 (full BD
book) + PRD v0.8 taxonomy. The bulk of the code change was pre-existing
working-tree WIP from base DS (full-book re-scope + taxonomy correction already
applied); DS~B reviewed it against the .025 amendment block, confirmed it
correct, ran the gate, and carried it forward:

- `non_model_aua(49F) = certified_aua - model_aua(1a)` -- SMA-inclusive, NO
  `- sma_aua` term. certified_aua read from BD gold
  `gold/aua_certification/{date}.json .certified_aua` (full BD book, all four
  custodians).
- Schwab custodian-crosswalk removed from the WS-E daily path. Per COO~B
  Option A (Correction 7): the crosswalk funcs are RETAINED as an explicit
  marked LEGACY block (two live importers -- build_mdpf_process_backfill.py +
  build_custody_crosswalk_cache.py); .016 owns their staged retirement. Not
  dead code -- ds-commit-gate AST scan clean.
- In-script full-book identity check `model + non_model == certified_aua`.

## Empirical verification (live, 2026-05-20)

WS-E dry-run + upload run:
- 1a model_aua_input $1,342,459,542.78 ; 1c sma_aua_input $24,940,150.25
- certified_aua $1,812,084,304.28 (full BD book, partition 2026-05-18 roll-fwd)
- non_model_aua(49F, 1b SMA-inclusive) = $469,624,761.50
- full-book identity model+non_model == certified_aua -> PASS
- vs PRD v0.8 ref ~$476.4M -> -1.42% (date offset, expected)

End-to-end aggregator upload run (`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-20.json`):

| Field | Value |
|-------|-------|
| opal_aggregate_aua (headline 1a+1b+2a) | **$1,905,783,014.47** |
| 49financial | model $1,342,459,542.78 / sma $24,940,150.25 / non_model $469,624,761.50 / total $1,812,084,304.28 |
| inflection | model $93,698,710.19 / sma $0.00 / non_model $106,254,365.08 / total $199,953,075.27 |
| partner_aua_subtotal (1a+1b+2a+2b) | $2,012,037,379.55 |
| cohort_2b_audit | $106,254,365.08 |
| etf_public_residual_total (Cohort 0 audit) | $91,310,278.05 |
| reconciliation.overall | **PASS** (identity_1/2/3 + sentinel_1/2/3 all PASS) |

- 49F total $1,812,084,304.28 == certified_aua -- 1a+1b reconstruct the full BD
  book to the cent; sma $24.94M is inside 1b, NOT a separate addend.
- No SMA double-count: sentinel-3 independent recompute = WS-A headline EXACTLY
  ($1,905,783,014.47 vs $1,905,783,014.47, diff $0.00). A 3-term sum would
  inflate the headline to $1,930.72M.
- Before/after (.024 rework effect, post-.025 feeders): 3-term would yield
  $1,930,723,164.72; 2-term yields $1,905,783,014.47 -- the rework removes the
  $24,940,150.25 SMA double-count.

## Files Modified

| File | Change | Commit |
|------|--------|--------|
| data/mdpf/scripts/gold/mdpf_aggregate_aua.py | .024 rework -- total_aua 2-term, sentinel-3 model-only recompute, headline 1a+1b+2a | ca2e71ad6 |
| data/mdpf/scripts/gold/mdpf_aggregate_aua_fixtures.py | .024 -- fixtures re-baselined to 2-way taxonomy, 6/6 PASS | ca2e71ad6 |
| data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py | .025 -- full-book certified_aua re-scope, no -sma term, LEGACY crosswalk block | 21b203acc |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 -- 3 files (py_compile + AST undefined-name + ruff) |
| Commit .024 | ca2e71ad6 (aggregator + fixtures) |
| Commit .025 | 21b203acc (WS-E) |
| Push | origin/CLOUD 3fb4784e6..21b203acc |
| S3 upload | s3://opal-data-mdpf/code/scripts/gold/ -- all 3 files, md5 local==S3 MATCH |
| End-to-end run | platinum 2026-05-20.json written, reconciliation PASS |

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-pipescript io mdpf_aggregate_aua.py | "Unknown script" -- known data/mdpf/ comp-graph gap; direct-read fallback per TO if_mismatch |
| comp-pipescript deployed | only scans s3://opal-data-bd/code/ -- does NOT cover the opal-data-mdpf bucket; substituted md5 local-vs-S3 (all 3 MATCH) |
| comp-validate mdpf_aggregate_aua / build_mdpf_wse_49f_non_model_aua | "not a known artifact-id" -- no mdpf config in gold_validate_config.yaml. NOT a BLOCK (no-config != exit-1). Verification substituted: the script-embedded reconciliation block (identity_1/2/3 + 3 sentinels, all PASS on the live end-to-end run) + the fixture suite (6/6) + the WS-E full-book identity check (PASS) |
| ds-commit-gate.sh | exit 0 all 3 files |

**comp-tools backlog (re-flagged to CTO):** `data/mdpf/scripts/` remains off
the comp-graph; `comp-pipescript deployed` does not cover the `opal-data-mdpf`
code bucket; `comp-validate` has no mdpf artifact config. Three distinct gaps,
all carried from prior DS~B/DS-Base sessions.

## Current State

MDPF_ASSETS.024 + .025 COMPLETE -- landed together (commits ca2e71ad6 +
21b203acc, pushed, S3-deployed, end-to-end verified). RAVC2 to COO~B.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | RAVC2 -- .024 + .025 complete; route output to CTO~B (headline $1,905,783,014.47, 1b $469.6M, no SMA double-count). On accept, MDPF_ASSETS.json phase narrative (DS lane-blocked on project JSONs). |
| **DS~B (self)** | Proceed to MDPF_ASSETS.016 -- empirically verify the 81 platinum partitions, then re-run on the v0.8 formula via build_mdpf_process_backfill.py. |
