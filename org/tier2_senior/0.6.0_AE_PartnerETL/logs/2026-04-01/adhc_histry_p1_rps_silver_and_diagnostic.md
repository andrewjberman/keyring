# ADHC_HISTRY P1 -- RPS Silver Build + DS Diagnostic -- 0.6.0_AE_PartnerETL

**Date:** 2026-04-01
**Task Orders:** ADHC_HISTRY.003 (COO) + ADHC_HISTRY.003 (CTO)
**EC2 Instance:** bd-gold-layer-runner (i-01003b035d2988dfb, c6i.16xlarge)

---

## Objective

Build `opal-data-schwab/silver/RPS/` (daily position snapshots) and run the DS
authority injection calculator diagnostic. DS was blocked on this for ADHC_HISTRY.002.

---

## Converter Bug History

Two bugs found and fixed during this session before the converter ran successfully.

### Bug 1: ThreadPoolExecutor GIL serialization

**Root cause:** `convert_schwab_rps_to_parquet.py` used `ThreadPoolExecutor` with
Python's GIL. RPS files are 70MB each (vs ACC at ~9MB). The CPU-bound DataFrame
creation (`pd.DataFrame(list_of_lists, columns=cols)`) doesn't release the GIL,
so 16 threads serialize and effective throughput = ~1 thread. Estimated runtime
for 534 files: 20+ hours.

**Fix (commit 4ccc90da):**
- Switch to `ProcessPoolExecutor` (each process has its own GIL)
- Move `boto3.client()` creation inside worker (required for multiprocessing pickling)
- Add `flush=True` and per-result counters

### Bug 2: Duplicate H2 column names

**Root cause:** RPS `.H2` header line has duplicate column names. `pd.read_csv()` 
(introduced in the ProcessPoolExecutor refactor) raises `DuplicateNamesError`. The
original manual list-comprehension approach silently allowed duplicates.

**Fix (commit 64bcacf2):**
- Read CSV with `header=None` (integer column indices)
- Map `KEY_FIELD_PATTERNS` against `raw_cols` by position index, not name
- Avoids duplicate-name issue entirely

---

## RPS Silver Build

| Item | Value |
|------|-------|
| SSM command | `c8de24ea-3041-4f45-984f-9308ad39b30a` |
| S3 output | `s3://opal-data-schwab/silver/RPS/` |
| Total partitions | **534** |
| Date range | 2024-01-12 to 2026-02-27 |
| OK | 534 |
| SKIP | 0 |
| ERR | 0 |
| Positions per day (approx) | 37K-80K (growing over time) |

Note: 217 Glacier-class RPS files were correctly skipped (GLACIER filter in `list_rps_keys()`).

---

## DS Diagnostic Run

**Script:** `adhc_histry_005_schwab_authority_calc.py` (commit c8db9f09, DS-authored)
**SSM command:** `5aa46df1-ef6b-43c4-80d3-8238cbe129e2`
**Output CSV:** `s3://opal-data-bd/diagnostics/schwab_authority_calc.csv` (4.5MB, confirmed present)

### Key Inputs

| Item | Value |
|------|-------|
| Account mappings | 6,510 total, 6,424 Schwab->BD pairs |
| BD transaction files | 1,759 files -> 2,791,225 deduped txns |
| FIFO open positions | 131,757 |
| Silver total MV (reference) | $1,587,368,576 |
| RPS dates available | 534 (2024-01-12 to 2026-02-27) |

### Part 1: Latest-Date Comparison (RPS 2026-02-27)

| Metric | Value |
|--------|-------|
| RPS rows (raw) | 80,919 |
| RPS mapped accounts | 78,809 |
| Unique mapped Schwab accounts | 5,237 |
| Positions needing injection (RPS > FIFO) | 36,788 |
| Accounts needing injection | 4,347 |
| **Total injection MV** | **$402,305,169** |
| Positions overcounted (FIFO > RPS) | 5,590 |
| Over-count MV | $32,620,353 |
| Full FIFO MV | $1,957,982,123 |
| FIFO + injection | $2,360,287,292 |
| Silver total MV | $1,587,368,576 |
| Residual gap after injection | $+772,918,717 |

### Top Injection Assets (2026-02-27)

| Asset | Inject MV | Units | Positions |
|-------|-----------|-------|-----------|
| POLEN DIVIDEND INCOME ETF (DIVZ) | $117,009,120 | 3,148,792 | 3,859 |
| ISHARES CORE MSCI EAFE ETF | $59,561,396 | 679,227 | 3,316 |
| STATE STREET SPDR PORTFOLIO S&P 500 ETF | $46,512,897 | 625,341 | 3,379 |
| OPAL INTERNATIONAL DIVIDEND INCOME ETF | $24,580,983 | 739,945 | 3,427 |
| ISHARES CORE MSCI EMERGING MARKETS ETF | $19,736,660 | 293,177 | 3,082 |

### DIVZ (Polen DIVIDEND INCOME ETF) Detail

| | Value |
|-|-------|
| FIFO total | $46,665,071 |
| Injection MV | $117,009,120 |
| Injection units | 3,148,792 |
| Post-injection total | $163,674,191 |
| Target range | $150-160M |

Post-injection is slightly above target ($163.7M vs $150-160M target). DS to assess.

### Part 2: Time Series Observation

Injection gap trend:
- Jan 2024: ~$254M injection, ~2,800 accounts
- Jul 2024: ~$335-340M, ~3,100-3,200 accounts
- Sep 2024: ~$450-455M, ~3,300 accounts
- Feb 2026 (latest): ~$402M, ~4,347 accounts

The gap grew substantially through 2024 as more accounts joined and positions accumulated
without corresponding BD transaction coverage.

---

## Files Modified

| File | Change | Commit |
|------|--------|--------|
| `data/black_diamond/scripts/bronze/convert_schwab_rps_to_parquet.py` | ProcessPoolExecutor + read_csv | `4ccc90da` |
| `data/black_diamond/scripts/bronze/convert_schwab_rps_to_parquet.py` | Duplicate H2 column name fix | `64bcacf2` |

---

## Acceptance Criteria Status

| Criterion | Status |
|-----------|--------|
| silver/RPS/ populated (534 partitions, 2024-01-12 to 2026-02-27) | DONE |
| adhc_histry_005 runs to completion (no BLOCKED exit) | DONE |
| s3://opal-data-bd/diagnostics/schwab_authority_calc.csv exists | DONE (4.5MB) |
| DS notified via MCP | DONE (this session) |

---

## Do NOT

- Deploy gold layer changes based on this diagnostic alone -- DS must review
- Restore Glacier RPS files (2024-09 to 2025-11) without checking cost (~$0.03/GB)
- Re-run the converter unless DS requests additional dates
