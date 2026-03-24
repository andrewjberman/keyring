# Session Log -- 0.4.0_DS_ClientPlatform
**Date:** 2026-03-24
**Task Order:** DEBT_1STRUN.001.scan + follow-on gold cleanup
**Branch:** debt/0.3.1-rd-portfolio-management-cleanup

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

### 2. Gold Archive Cleanup (complete -- local repo)

Deleted from local repo:
- `data/black_diamond/scripts/gold/archive/` -- 48 files, entire directory removed
- `data/black_diamond/scripts/gold/run_all.sh` -- dead orchestrator referencing archived scripts

Updated runner scripts:
- `data/black_diamond/scripts/gold/run_gold_layer.sh` line 71 -- removed `--exclude "archive/*"` from S3 sync (no longer needed)
- `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` line 62 -- same removal

Updated deploy script:
- `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh`:
  - Header comment: `00-08` changed to `00-12` (reflects actual script range)
  - Added `--delete` to SYNC_FLAGS so local deletions propagate to S3
  - Added `--exclude '*.parquet'` safety guard to prevent data artifact deletion

Rewrote documentation:
- `data/black_diamond/scripts/gold/README_BUILD_SEQUENCE.md` -- complete rewrite with current 17-script inventory, dependency graph, both execution modes, deployment instructions
- `data/black_diamond/README.md` -- updated 4 sections: EC2 gold runner diagram, data flow diagram, S3 code/ structure, directory tree, gold scripts reference

### 3. Coordination with AE

Reviewed AE's S3 audit (`org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-03-24/s3_gold_script_cleanup_audit.md`).
Reviewed AE's next-steps brief (`org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-03-24/ds_cleanup_next_steps_brief.md`).

Assessment: DS (local repo) and AE (S3) workstreams are complementary, no conflicts.

---

## Current Architecture -- Gold Layer

### Local Repo Structure (after cleanup)

```
data/black_diamond/scripts/gold/
  00_build_accounts_dimension.py
  01_build_advisor_assignments_history.py
  02_build_positions_cube.py
  03_build_holdings_lots.py
  04_build_client_dimension.py
  05_build_client_performance.py
  05b_build_account_performance.py
  05c_validate_aua_vs_silver.py
  05d_write_aua_certification.py
  06_build_client_tax_liability.py
  06b_build_client_mix_timeseries.py
  07_build_nna_aua_by_geography.py
  08_build_nna_aua_by_advisor.py
  08b_build_architect_attribution.py
  09_generate_partner_analytics.py
  10_generate_advisor_rolling_flows.py
  12_build_composition_artifacts.py
  detect_new_securities.py
  lib/etf_classifier.py
  lib/__init__.py
  aua_overrides.json
  insurance_accounts.json
  run_gold_layer.sh              <-- sole orchestrator
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

deploy-to-ec2.sh now uses `--delete` with `--exclude '*.parquet'` safety guard.

### S3 Canonical Prefixes (per AE convention, Phase C)

| Prefix | Purpose |
|--------|---------|
| `code/gold/` | Gold layer scripts (production) |
| `code/silver/` | Silver layer scripts (production) |
| `code/bronze/` | Bronze layer scripts (production) |
| `code/diagnostics/` | Ad-hoc diagnostic scripts |
| `code/runner/` | EC2 runner entrypoints |
| `config/` | Configuration files |
| `scripts/` | DEPRECATED -- being emptied by AE |

---

## What Remains (not DS scope)

### AE Scope (S3 cleanup)
- Phase A: `aws s3 rm` on 7 stale paths (scripts/gold_layer/, scripts/gold/, code/gold/archive/, root strays, dead runners)
- Phase B: move `scripts/fetch_historical_prices_yfinance.py` to `code/silver/`, update scheduler Lambda
- Phase C: enforce `code/` prefix convention, empty `scripts/`

### DS Scope (future DEBT_1STRUN .002+ task orders)
From the scan, the remaining tech debt priorities NOT yet addressed:
1. **C3 High: NNA flow duplication** -- `INFLOW_TYPES`/`OUTFLOW_TYPES` and `load_flows_from_transactions()` copy-pasted between 05 and 05b. Extract to `gold/lib/nna_flows.py`.
2. **C6 High: Silent sys.exit(0)** -- 05c and 05d swallow all exceptions and report success. Pipeline blind to validation/certification failures.
3. **C3 Medium: Duplicated helpers** -- `modal_str()` in 07+08, `s3_object_exists()` in 05c+05d, `_OPAL_ETF_OVERRIDES` in two silver scripts.
4. **C4 Medium: Hardcoded bucket name** -- `'opal-data-bd'` in every gold script. Should be env var.
5. **C1 Low: Emoji in print statements** -- 4 scripts (01, 04, 06, 07) violate CLAUDE.md rule 13.

### Not Yet Committed
All local changes are unstaged. Pending commit per AE's recommendation as a single commit.
