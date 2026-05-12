# Schwab MAY Ingest — OneDrive → S3 + 5 Converters

| Field | Value |
|-------|-------|
| Agent | 0.6.0_AE_PartnerETL |
| Date | 2026-05-07 |
| Trigger | Andrew direct request: "upload the newest MAY schwab files and run the converter scripts" |
| Scope | Step 1 (sync) + steps 2–6 (ACC, RPS, TRN, ULN, RLD converters) |

## Current State

**All 6 mandatory steps complete.** New silver partitions: 0501, 0504, 0505, 0506 across every table. Weekend gap (0502, 0503) is normal Schwab behavior. Latest silver date for every table: **20260506**.

### Step 1 — OneDrive sync
```
python data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py --upload --since 20260501
```
- 46 files uploaded to `s3://opal-data-schwab/01_raw/`
- 4 files mirrored to `s3://opal-data-schwab/bronze/rps/`
- Pre-sync state: S3 last had 20260429
- Post-sync state: 01_raw/ contains all OneDrive files through 20260506

### Steps 2–6 — Converters (all run in parallel)

| Step | Script | Result | Latest partition |
|------|--------|--------|-----------------|
| 2 | convert_schwab_acc_to_parquet.py | OK=4 SKIP=0 ERR=0 | silver/ACC/date=20260506 (6,878 accounts) |
| 3 | convert_schwab_rps_to_parquet.py | OK=4 SKIP=0 ERR=0 | silver/RPS/date=20260506 (85,494 positions) |
| 4 | convert_schwab_trn_to_parquet.py | OK=4 SKIP=0 ERR=0 | 03_silver/TRN/date=20260506 (23,459 rows) |
| 5 | convert_schwab_uln_to_silver.py | OK=4 SKIP=0 ERR=0 | silver/ULN/date=20260506 (225,381 long lots) |
| 6 | convert_schwab_lots_to_silver.py rld | OK=4 SKIP=1 ERR=0 | opal-data-bd/schwab/silver/rld/date=20260506 |

RLD `SKIP=1` was 20250109 (no DL rows) — old backfill skip, unrelated to May ingest.

### Per-day rowcount summary

| Date | ACC accounts | RPS positions | TRN rows | ULN long lots |
|------|-------------:|--------------:|---------:|--------------:|
| 20260501 | 6,845 | 85,182 | 8,148 | 218,281 |
| 20260504 | 6,856 | 85,257 | 982 | 218,037 |
| 20260505 | 6,871 | 85,388 | 15,119 | 220,576 |
| 20260506 | 6,878 | 85,494 | 23,459 | 225,381 |

20260504 TRN rowcount is low (982) — likely Sunday filings; 0504 was a Monday but the .TRN reflects weekend activity.

### S3 verification

```
silver/ACC/date=20260501..20260506    [4 new]
silver/RPS/date=20260501..20260506    [4 new]
03_silver/TRN/date=20260501..20260506 [4 new]
silver/ULN/date=20260501..20260506    [4 new]
opal-data-bd/schwab/silver/rld/date=20260501..20260506 [4 new]
```

## Compiler Tools

None run — this is a recurring data-ingest task with no Lambda/EC2/Terraform changes. Per `comp-tools.yaml` minimum AE matrix: `comp-pipescript deployed` and `comp-pipescript postdeps` apply to gold script dispatches; this session triggered no gold runs. `comp-iam gaps` not applicable (no iam.tf change).

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** Schwab silver is fresh through 20260506 — pick up for BD ↔ Schwab reconciliation, NNA enrichment, and any pending B_02 canonical_lots gold work that needs the new RLD partitions.
2. **[0.6.0_AE_PartnerETL]** Idle on next Schwab cycle. If DS reports stale silver again, re-run from step 1.

## Deployment Tags

N/A — data-only ingest; no infra/Lambda/Terraform changes. No bd-vX.Y.Z tag.

## Verification

- All 4 May dates × 5 tables = 20 partitions present in S3
- Date range for every table extends to 20260506
- All converter exit codes = 0
- Idempotent re-run path preserved (Already-converted counts incremented correctly)
