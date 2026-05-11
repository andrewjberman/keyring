# Schwab MAY Ingest (0507 + 0508) — OneDrive → S3 + 5 Converters

| Field | Value |
|-------|-------|
| Agent | 0.6.0_AE_PartnerETL |
| Date | 2026-05-11 |
| Trigger | Andrew direct request: "get all the new Schwab files uploaded and converted, i just downloaded the new batch of may files" |
| Scope | Step 1 (sync) + steps 2–6 (ACC, RPS, TRN, ULN, RLD converters) |
| Prior run | 2026-05-07 — silver landed through 20260506 |

## Current State

**All 6 mandatory steps complete.** New silver partitions: 20260507 + 20260508 across every table. Weekend gap (0509, 0510) is normal Schwab behavior. Latest silver date for every table: **20260508**.

### Step 1 — OneDrive sync
```
python data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py --upload --since 20260507
```
- 24 files uploaded to `s3://opal-data-schwab/01_raw/`
- 2 files mirrored to `s3://opal-data-schwab/bronze/rps/`
- Pre-sync state: S3 last had 20260506
- Post-sync state: 01_raw/ contains all OneDrive files through 20260508

### Steps 2–6 — Converters (all run in parallel)

| Step | Script | Result | Latest partition |
|------|--------|--------|-----------------|
| 2 | convert_schwab_acc_to_parquet.py | OK=2 SKIP=0 ERR=0 | silver/ACC/date=20260508 (6,897 accounts) |
| 3 | convert_schwab_rps_to_parquet.py | OK=2 SKIP=0 ERR=0 | silver/RPS/date=20260508 (85,877 positions) |
| 4 | convert_schwab_trn_to_parquet.py | OK=2 SKIP=0 ERR=0 | 03_silver/TRN/date=20260508 (1,372 rows) |
| 5 | convert_schwab_uln_to_silver.py | OK=2 SKIP=0 ERR=0 | silver/ULN/date=20260508 (226,608 long lots) |
| 6 | convert_schwab_lots_to_silver.py rld | OK=2 SKIP=1 ERR=0 | opal-data-bd/schwab/silver/rld/date=20260508 |

RLD `SKIP=1` was 20250109 (no DL rows) — old backfill skip, unrelated to May ingest (same skip observed in 2026-05-07 session).

### Per-day rowcount summary

| Date | ACC accounts | RPS positions | TRN rows | ULN long lots | RLD lots |
|------|-------------:|--------------:|---------:|--------------:|---------:|
| 20260507 | 6,886 | 85,547 | 871 | 226,134 | 799 |
| 20260508 | 6,897 | 85,877 | 1,372 | 226,608 | (converted) |

TRN rowcounts are low because 0507/0508 are mid-week with limited transaction activity vs the larger 0501/0505/0506 days in the prior batch.

### S3 verification

```
silver/ACC/date=20260507, date=20260508       [2 new]
silver/RPS/date=20260507, date=20260508       [2 new]
03_silver/TRN/date=20260507, date=20260508    [2 new]
silver/ULN/date=20260507, date=20260508       [2 new]
opal-data-bd/schwab/silver/rld/date=20260507, date=20260508 [2 new]
```

All confirmed via `aws s3 ls` — every table tail shows `PRE date=20260508/`.

## Compiler Tools

None run — this is a recurring data-ingest task with no Lambda/EC2/Terraform changes. Per AE minimum matrix: `comp-pipescript deployed` and `comp-pipescript postdeps` apply to gold script dispatches; this session triggered no gold runs. `comp-iam gaps` not applicable (no iam.tf change).

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** Schwab silver is fresh through 20260508 — pick up for BD ↔ Schwab reconciliation, NNA enrichment, and B_02 canonical_lots gold work that needs the new RLD partitions.
2. **[0.6.0_AE_PartnerETL]** Idle on next Schwab cycle. If DS reports stale silver again, re-run from step 1.

## Deployment Tags

N/A — data-only ingest; no infra/Lambda/Terraform changes. No bd-vX.Y.Z tag.

## Verification

- All 2 May dates × 5 tables = 10 partitions present in S3
- Date range for every table extends to 20260508
- All converter exit codes = 0
- Idempotent re-run path preserved (Already-converted counts incremented correctly: 579→581 ACC, 580→582 RPS, 507→509 TRN, 363→365 ULN, 615→617 RLD)
