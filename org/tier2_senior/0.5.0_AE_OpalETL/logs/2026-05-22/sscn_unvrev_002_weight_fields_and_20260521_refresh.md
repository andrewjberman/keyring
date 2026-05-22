# SSCN_UNVREV.002 — Lambda model-weight exclusion + divzWeight/universeWeight emit + 20260521 refresh

**Agent:** 0.5.0_AE_OpalETL (AWS Engineer, base lane)
**Date:** 2026-05-22
**TO:** `SSCN_UNVREV.002.ae-lambda-weight-fields-and-20260521-refresh.md` (DE-authored, COO-committed/GO'd)
**Status:** COMPLETE — all 6 acceptance criteria PASS.

---

## Summary

Yang feedback (via Andrew, 2026-05-22): the Security Scanner page needs weight-of-DIVZ
and weight-of-universe columns. DE shipped the portal side to DEV (`7786eef9`); this TO
ships the Lambda side — `opal-security-scanner-processor` now excludes the 4 new
model-weight columns from factor scoring and emits the two weight fields per row — plus
the data refresh from Yang's new 20260521 source file.

## Deployment Sequence (Part A)

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit `lambda_function.py` | 5 edits — see below; `py_compile` OK |
| 2 | `comp-iam service` | 3 pre-existing S3 ops, no new boto3 call — clean |
| 3 | `build-and-upload.sh security-scanner-pipeline opal-security-scanner-processor` | artifact SHA256 `XgwQibtfQQLSUH8kGXIKmWG+MXNwCBOiUmdpsXkYXgo=` |
| 4 | Commit source + source map | `5fd7d6049` feat(security-scanner): SSCN_UNVREV.002 -- model-weight exclusion + divzWeight/universeWeight emit |
| 5 | `safe-apply.sh ... apply` (HALTGT-gated) | 0 added, 1 changed, 0 destroyed |
| 6 | 0-diff plan | `No changes. Your infrastructure matches the configuration.` |
| 7 | `record-terraform-deploy.sh` | `939cdb2d4` ci: record deploy — CHANGELOG `security-scanner-v1.3.0` + source map |
| 8 | Tag + push | `security-scanner-v1.3.0`, pushed `--follow-tags` to CLOUD |

### Lambda edits (`infra/aws/lambda/opal_security_scanner_processor/lambda_function.py`)

1. `NON_SCORING_COLS` — added `wt_divz`, `wt_idvz`, `wt_pfde`, `wt_pfoe` (4 model-weight
   columns in the new 20260521 file) so they are not percentile-ranked as scoring
   factors / polluting `factor_metadata.json`.
2. `_build_universe_rows` — emits `divzWeight` (from `wt_divz`) per row.
3. `_build_scanner_rows` — signature gains `universe_col`; call site updated; each row
   emits `universeWeight` (selected-universe weight, Andrew ruling 2026-05-22) +
   `divzWeight`.

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| security-scanner-pipeline | `security-scanner-v1.3.0` | `5fd7d6049` (code) / `939cdb2d4` (record-deploy) |

## Part B — data refresh

Uploaded Yang's `Screening_DIVZ_IDVZ_20260521 (1).xlsx` (renamed to drop the browser
" (1)" suffix) to `s3://opal-data-portal-v2/security_scanner/uploads/20260521/Screening_DIVZ_IDVZ_20260521.xlsx`
(8,670,540 bytes). ObjectCreated triggered the processor; all 6 universes + factor
metadata regenerated under `latest/`.

CloudWatch trigger run (stream `2026/05/22/[$LATEST]8036aeae...`):
```
asOf=20260521 | Loaded 2707 rows x 339 columns | Identified 284 scoring factor columns
sp500 502 | r1000 1002 | r1000v 864 | acwx 1682 | eafe 677 | eafev 405
Processing complete. asOf=20260521, universes processed=6
```
No ERROR. 284 scoring columns — identical to the 335-col 20260519 file's 284, confirming
the 4 new columns (339-335) were all excluded from `scoring_cols`.

---

## Acceptance Criteria — all PASS

- **AC1** — PASS. Deployed Lambda `CodeSha256 = XgwQibtfQQLSUH8kGXIKmWG+MXNwCBOiUmdpsXkYXgo=`
  byte-matches the `security-scanner-v1.3.0` artifact; `NON_SCORING_COLS` contains the
  4 model-weight columns (confirmed by AC6 — none leaked into scoring).
- **AC2** — PASS. `terraform plan` 0-diff after apply; `security-scanner-v1.3.0` tagged
  + pushed `--follow-tags`.
- **AC3** — PASS. xlsx present at `uploads/20260521/Screening_DIVZ_IDVZ_20260521.xlsx`.
- **AC4** — PASS. All 6 universes' `universe_data.json` + `scanner_data.json` + `latest/
  factor_metadata.json` regenerated 2026-05-22 12:06-12:07Z. r1000 spot-check: every
  `universe_data.json` row carries `divzWeight`; every `scanner_data.json` row carries
  both `universeWeight` + `divzWeight`. The row builders emit these fields
  unconditionally for every row of every universe — structural across all 6.
- **AC5** — PASS. r1000 `scanner_data.json`: 1002/1002 rows `universeWeight > 0`
  (weight-filtered members). `divzWeight` populated for 24 holdings (DIVZ ~25-name
  model), null for 978. Both cases confirmed: populated — ABBV `divzWeight=2.9139`;
  null — SPOT `divzWeight=null`.
- **AC6** — PASS. `wt_divz/wt_idvz/wt_pfde/wt_pfoe` do NOT appear as factor codes in
  `factor_metadata.json` and are NOT keys in any row's `values`/`pctls` — excluded from
  `scoring_cols` as intended.

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-iam service opal-security-scanner-processor` | 3 S3 ops (`get_object` x2, `put_object`) — all pre-existing; the edit added no boto3 call. No MISSING. Clean. |
| `comp-pipescript deployed` | N/A — Lambda, not a gold runner. 0-diff `terraform plan` is the deployed-state check (AC2). |
| `comp-iam gaps` | N/A — `iam.tf` not touched. |
| `python -m py_compile` | PASS on `lambda_function.py` post-edit. |

---

## Current State

- `security-scanner-v1.3.0` deployed; `opal-security-scanner-processor` excludes the 4
  model-weight columns and emits `divzWeight` (both row builders) + `universeWeight`
  (scanner rows). All 6 universes refreshed in S3 from the 20260521 export.
- TO `SSCN_UNVREV.002` self-flipped to `complete`.
- `pipeline_inventory.xml` security-scanner `current_tag` -> `security-scanner-v1.3.0`.

## Next Steps / flags

- `[0.3.0_DE_TradingOperations]` RAVC2 sent with AC1-AC6 evidence (CC `2.0.0_SA_COO`).
  PROD coupling: portal DEV (`7786eef9`) renders the new columns once AC4 is met — now
  satisfied. DT bundles the portal PROD push after Andrew's DEV smoke.
- `[2.0.0_SA_COO~B]` SSCN doc-canonicalization (COO~B lane): `SSCN_DATA_CONTRACT.md`
  Section 5 should gain `UniverseDataRow.divzWeight`, `ScannerRow.universeWeight`,
  `ScannerRow.divzWeight`. Flagged, not blocking — per the TO's cross-domain note.
- `[follow-up, non-blocking — needs sign-off]` 3 stale v0.2-only S3 prefixes
  (`msciusa/`, `rmidcap/`, `sp400/` under `latest/universes/`) still present from the
  pre-revert era — carried over from SSCN_UNVREV.001's flag; S3 deletion needs sign-off.
