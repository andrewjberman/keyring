# DS~D — silver/transactions/ Gap Investigation and Backfill (04/21–04/28)

**Agent serial:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-04-29
**Session shape:** Andrew request → S3 audit → API pull → targeted silver build → S3 write → watermark update
**Outcome:** 6 missing silver/transactions/ partitions written (04/21–04/28); watermark advanced to 2026-04-28

---

## Request Origin

Andrew: "check transactions in the s3 bucket, i think we may be missing transactions between 4/20 and 4/27 or something like that, if so need you to backfill and process"

Triggered after ADVI_INFSHIP.B5 bronze fix (commit `79bf2afbc`) was shipped.

---

## Audit Findings

### Silver state before backfill

`s3://opal-data-inf/silver/transactions/` — latest partition was `2026-04-20.parquet`.

Gap confirmed: **2026-04-21 through 2026-04-28** had no silver coverage (6 business days; 04/25-04/26 are weekend non-trading days).

### Root cause of gap

`data/orion/scripts/silver/convert_orion_to_silver.py` reads from `bronze/orion/` (legacy manual export prefix). The final manual export Andrew ran on 2026-04-21 covered transactions through ~2026-04-20. No subsequent bronze/orion/ objects exist beyond that date.

The new API-sourced bronze (`bronze/orion-api/2026-04-28/transactions.csv`, `2026-04-29/transactions.csv`) uploaded by the B5 fix was NOT automatically picked up by the silver builder — the builder does not read from `bronze/orion-api/`. The gap predates the B5 fix: April 21-27 were never covered by any bronze pull.

### Weekend dates (no transactions expected)

- 2026-04-25 (Saturday): no trading — confirmed absent from API pull
- 2026-04-26 (Sunday): no trading — confirmed absent from API pull

### 04/29 trade-date lag

Transactions for 2026-04-29 have not yet settled at API query time. Will come through on tomorrow's scheduled bronze runner cron cycle (v2 orchestrator wired; `pull_inflection_transactions_v2.py` runs daily).

---

## Backfill Procedure

### Step 1 — API pull (04/21/2026 → 04/29/2026)

Used `pull_inflection_transactions_v2.py` logic (Custom Reports 28198, `prompts[]` format, `@RepIDs=3,11,12`) to pull the full window. Result:

- 4,326 raw data rows
- CSV: `data/orion/manual_api/pulls/2026-04-29_inflection_transactions.csv` (already written by B5 session)

### Step 2 — Targeted silver normalization

Imported normalization functions directly from `convert_orion_to_silver.py`:

```python
from data.orion.scripts.silver.convert_orion_to_silver import (
    _normalize_trn_df,
    _apply_scopefix,
    PARTNER_FIRM_TAGS,
)
```

Applied same pipeline as the silver builder:
1. `_normalize_trn_df()` — column rename, type coercion, date parsing, enrichment cols
2. `_apply_scopefix()` — filter rep_id IN {3, 11, 12}, add advisor_key / rep_bucket / advisor_firm / custodian

### Step 3 — Date partitioning + S3 write

Partitioned normalized dataframe by `trade_date`. For each date:
- Deduplicated by `transaction_id` globally (same logic as silver builder)
- Wrote snappy parquet to `s3://opal-data-inf/silver/transactions/{date}.parquet`

### Step 4 — Watermark update

Updated `s3://opal-data-inf/silver/meta/trn_watermark.json`:
```json
{"last_silver_date": "2026-04-28", "updated_at": "2026-04-29T...Z"}
```

---

## Deliverables Matrix

| Partition | Rows | S3 Key |
|-----------|------|--------|
| 2026-04-21 | 91 | `silver/transactions/2026-04-21.parquet` |
| 2026-04-22 | 49 | `silver/transactions/2026-04-22.parquet` |
| 2026-04-23 | 992 | `silver/transactions/2026-04-23.parquet` |
| 2026-04-24 | 1,640 | `silver/transactions/2026-04-24.parquet` |
| 2026-04-27 | 1,479 | `silver/transactions/2026-04-27.parquet` |
| 2026-04-28 | 75 | `silver/transactions/2026-04-28.parquet` |
| **Total** | **4,326** | 6 partitions written |

Weekend dates (04/25–04/26): confirmed absent from API pull — no trading activity.

---

## Silver Builder Notes (no code changes)

`convert_orion_to_silver.py` was NOT modified. Backfill used its normalization functions in-memory. The builder's `bronze/orion/` read path remains unchanged — this backfill is a one-time gap fill, not a structural change to the silver pipeline.

**Outstanding architectural item (flagged for AE):** The silver builder does not read from `bronze/orion-api/`. As the pipeline transitions fully to API-sourced bronze, the builder will need a dual-prefix reader or a secondary silver builder that consumes `bronze/orion-api/{date}/transactions.csv`. This is an AE-scope architectural decision — no silver builder changes were made in this session.

---

## Outstanding

- `silver/transactions/2026-04-29.parquet` — will arrive on 2026-04-30 cron cycle via v2 orchestrator
- Silver builder `bronze/orion-api/` reader — architectural decision pending AE 0.6.1

---

*Authored by `0.4.0_DS_ClientPlatform~D`. Session arc: silver audit → API pull → targeted build → 6 partitions written.*
