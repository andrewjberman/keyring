# Session Log -- 0.4.0_DS_ClientPlatform
**Date:** 2026-03-24
**Task Order:** DEBT_1STRUN.001.scan + follow-on fixes
**Branch:** CLOUD

---

## Commits

| Hash | Description |
|------|-------------|
| `81220cd2` | cleanup(gold): delete archive/ (48 files), rewrite docs, add --delete to deploy sync |
| `c1bb4903` | fix(gold): extract shared lib, fix silent exits, remove emoji |

---

## Work Completed

### 1. DEBT_1STRUN.001 Scan (complete)

Scanned all 3 scope directories: `data/black_diamond/scripts/gold/`, `silver/`, `classification/`.
Deliverable: `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-23/debt_1strun_scan.md`

**47 findings** across 6 categories:
- C1 Dead Code: 10 (incl. archive/ = 31 files)
- C2 Deprecated: 7
- C3 Duplication: 6
- C4 Hardcoded Config: 9
- C5 Orphaned Infrastructure: 3
- C6 Stale Error Handling: 12
- High severity: 13

### 2. Gold Archive Cleanup (commit `81220cd2`)

**Deleted from local repo:**
- `data/black_diamond/scripts/gold/archive/` -- 48 files, entire directory removed
- `data/black_diamond/scripts/gold/run_all.sh` -- dead orchestrator referencing archived scripts

**Updated runner scripts:**
- `data/black_diamond/scripts/gold/run_gold_layer.sh` -- removed `--exclude "archive/*"` from S3 sync
- `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` -- same removal

**Updated deploy script** (`infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh`):
- Header comment: `00-08` changed to `00-12`
- Added `--delete` to SYNC_FLAGS so local deletions propagate to S3
- Added `--exclude '*.parquet'` safety guard to prevent data artifact deletion

**Rewrote documentation:**
- `data/black_diamond/scripts/gold/README_BUILD_SEQUENCE.md` -- complete rewrite with current 17-script inventory, dependency graph, deployment instructions
- `data/black_diamond/README.md` -- updated EC2 gold runner diagram, data flow diagram, S3 code/ structure, directory tree, gold scripts reference

### 3. Shared Library Extraction + Fixes (commit `c1bb4903`)

**Created `gold/lib/nna_flows.py`** (C3 High fix):
- Extracted from 05 and 05b: `INFLOW_TYPES`, `OUTFLOW_TYPES`, `FLOW_CAP`, `REAL_PRICE_SOURCES`, `load_flows_from_transactions()`
- Both scripts now import from lib. ~319 lines of duplication eliminated.
- Single source of truth for NNA classification rules -- changes propagate automatically.

**Created `gold/lib/helpers.py`** (C3 Medium fix):
- `modal_str()` extracted from 07 and 08
- `s3_object_exists()` extracted from 05c and 05d
- Both pairs now import from lib.

**Fixed silent `sys.exit(0)`** (C6 High fix):
- 05c: 2 error exits changed from exit(0) to exit(1)
- 05d: 3 error exits changed from exit(0) to exit(1)
- 05d line 99 preserved as exit(0) -- legitimate skip when no silver allocation exists (weekends)
- Orchestrator's `|| true` still controls whether pipeline halts; scripts now correctly signal failure.

**Removed emoji from print statements** (C1 Low fix):
- 01, 04, 05, 06: replaced checkmark emoji with ASCII `OK:` prefix
- Prevents CloudWatch log query breakage on Windows (CLAUDE.md rule 13)

### 4. Coordination with AE

Reviewed AE's S3 audit and next-steps brief. DS (local repo) and AE (S3) workstreams are complementary.
AE identified `--delete` on S3 sync as the key preventive measure; DS implemented it with `--exclude '*.parquet'` guard.

---

## Current Architecture -- Gold Layer

### Local Repo Structure

```
data/black_diamond/scripts/gold/
  00_build_accounts_dimension.py
  01_build_advisor_assignments_history.py
  02_build_positions_cube.py
  03_build_holdings_lots.py
  04_build_client_dimension.py
  05_build_client_performance.py          <-- imports lib/nna_flows
  05b_build_account_performance.py        <-- imports lib/nna_flows
  05c_validate_aua_vs_silver.py           <-- imports lib/helpers, exits 1 on error
  05d_write_aua_certification.py          <-- imports lib/helpers, exits 1 on error
  06_build_client_tax_liability.py
  06b_build_client_mix_timeseries.py      <-- imports lib/etf_classifier
  07_build_nna_aua_by_geography.py        <-- imports lib/helpers
  08_build_nna_aua_by_advisor.py          <-- imports lib/helpers
  08b_build_architect_attribution.py
  09_generate_partner_analytics.py
  10_generate_advisor_rolling_flows.py
  12_build_composition_artifacts.py       <-- imports lib/etf_classifier
  detect_new_securities.py
  lib/
    __init__.py
    etf_classifier.py                     <-- pre-existing
    nna_flows.py                          <-- NEW: NNA flow types + loader
    helpers.py                            <-- NEW: modal_str, s3_object_exists
  aua_overrides.json
  insurance_accounts.json
  run_gold_layer.sh
  README_BUILD_SEQUENCE.md
```

### Orchestration

`run_gold_layer.sh` on `bd-gold-layer-runner` EC2 (r6i.xlarge, 32GB RAM).
All scripts sequential (prevents read-during-write on shared S3 parquets).

| Mode | Schedule | Scripts |
|------|----------|---------|
| incremental | Daily Mon-Fri ~6 PM ET | 00, 02, 05, 05c, 05d, 07, 08b, 12, 06b, 08, 09, 10 |
| full | Monthly 1st 3 AM ET | 00, 01, 02, 04, 03, 05, 05b, 05c, 05d, 06, 06b, 07, 08b, 12, 08, 09, 10 |

### Deployment Path

```
local repo --> deploy-to-ec2.sh --> s3://opal-data-bd/code/gold/ --> EC2 pulls on boot
```

deploy-to-ec2.sh uses `--delete` with `--exclude '*.parquet'` safety guard.

---

## Remaining Debt (for next session)

### C2 Deprecated (7 findings)
- Stale comments referencing `silver/bd_transactions.parquet` in 01, 04
- AUA overrides section in 05 may be fully removable (RC6 ghost accounts)
- Comment referencing nonexistent `.tmp_insurance_ap_gate.py` in 06b
- `security_ticker_mapping_final.py` superseded by S3 config
- OpenAI discovery path in `fetch_historical_prices_yfinance.py` never runs
- `gpt-4o-mini` hardcoded in `classify_bd_securities.py`

### C4 Hardcoded Config (9 findings)
- `'opal-data-bd'` bucket name in every gold script -- env var candidate
- Business rule constants in 05 (FLOW_CAP, VELOCITY_WINDOW_DAYS) -- now in lib but still hardcoded
- Color palettes in 09 -- presentation constants in backend code
- Magic number `CORRECT_COL_COUNT = 71` in merge-daily-incremental.py
- `MAX_WORKERS = 64` in build_canonical_prices_v2.py
- Region, table names, secret IDs hardcoded in classification scripts

### C3 Medium (1 remaining)
- `_OPAL_ETF_OVERRIDES` duplicated in `build_canonical_prices_v2.py` and `bd_price_update.py` (silver scope)

### C5 Orphaned (3 findings)
- `build_interpolated_prices.py` output never consumed
- `merge-daily-allocation-incremental.py` orphaned manifest
- 05c validation JSON output has no verified consumer

### AE Scope (S3 cleanup -- not DS)
- Phase A: `aws s3 rm` on 7 stale S3 paths
- Phase B: move scheduler script to `code/silver/`
- Phase C: establish `code/` prefix convention
