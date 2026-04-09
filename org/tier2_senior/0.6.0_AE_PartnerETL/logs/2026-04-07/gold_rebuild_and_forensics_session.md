# Session Log: Gold Rebuild + Vectorization Audit + Fee Split Forensics

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-07 (into 2026-04-08 02:38 UTC)
**Duration:** ~7 hours

---

## Summary

Full gold pipeline rebuild after DS renamed all scripts to A-E group taxonomy. Audited all 42 gold scripts for vectorization/parallelism. Ran forensic analysis on unassigned "49F House" accounts. Stood up a new QA EC2 runner. Ran multiple diagnostic scripts (E_22, E_23, E_24). Fixed 5 runtime bugs caught during deployment.

---

## 1. Gold Pipeline Rebuild

### Initial Deploy (--chain full, skipping Group A)

S3 sync with `--delete` removed 42 old-named scripts, uploaded 38 new-named scripts.
Instance: bd-gold-layer-runner (i-01003b035d2988dfb, c6i.16xlarge).

**Bugs fixed during run:**

| # | Script | Line | Bug | Fix |
|---|--------|------|-----|-----|
| 1 | B_02.canonical_lots.py | 450 | `if schwab_rld_key:` on DataFrame triggers ambiguous truthiness | `if schwab_rld_key is not None:` |
| 2 | gold_dispatch.sh | 93 | C_03 passed `--process-workers WORKERS` but doesn't accept it | Removed flag from catalog entry |
| 3 | C_07.advisor_attribution.py | 119 | tz-aware cutoff vs tz-naive column comparison | `.tz_localize(None)` on cutoff |
| 4 | D_01.partner_analytics.py | 58 | `as_completed` used but not imported (GPT edit) | Added to import |
| 5 | C_00.canonical_performance.py | 291-292 | Column reorder dropped `_date_str` before groupby write (GPT edit) | Keep `_date_str` in DataFrame, drop in write function |

### Full Rebuild (--chain rebuild)

After discovering Group A changes weren't picked up (D_00 failed on missing `local_ops` column), ran `--chain rebuild` covering all 22 scripts A_00 through D_03.

All 22 scripts completed successfully.

### Additional Runs

- **Full C+D rerun** after DT deployed updated scripts (C_02 NNA fix, C_08 log-log regression, D_00 leaderboard NNA, D_01 zeros fix, lib/mix_views.py rename). Commit 5f485323.
- **C_08 targeted run** for fee efficiency scorecard validation.

---

## 2. Vectorization & Parallelism Audit

Audited all production gold scripts (Groups A-D, 22 scripts) for:
- Row-level Python loops (iterrows, apply axis=1)
- Serial S3 I/O in loops
- Missing parallelism (ThreadPoolExecutor/ProcessPoolExecutor)
- Memory loading anti-patterns

### Critical Findings

| Priority | Script | Issue |
|----------|--------|-------|
| CRITICAL | A_04 | No S3 parallelism at all -- serial loop reading ~1,764 partitions |
| CRITICAL | D_02 | Re-reads ~4,000 client JSONs from S3 that it just wrote |
| CRITICAL | D_03 | 3,500 serial S3 PUTs, no ThreadPoolExecutor anywhere |
| CRITICAL | C_06 | classify_series() row-by-row Python loop |

GPT patched top offenders: A_01, A_02, A_04 (vectorized SCD builders), B_01 (shared-memory FIFO pool), C_06 (deduplicated classifier), D_02 (in-memory reuse), D_03 (parallel S3 writes).

### Process Improvement

Added **py_compile gate** to EC2 deployment workflow. All `.py` files must pass compile check before S3 upload. Added to `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md` Step 2 and saved as feedback memory.

---

## 3. S3 Path Verification (ADVI_REBORN W1-003)

Verified 29 gold artifact S3 keys for existence and freshness.

**Result:** 28 PASS / 1 STALE / 0 MISSING

Stale key: `gold/artifacts/firm_composition.json` (27.5h, legacy path superseded by `gold/views/firm_composition.json`).

---

## 4. Fee Split Forensics

### Account Segmentation

| Category | Accounts | % | Splits=100% | Splits=0% |
|----------|----------|---|-------------|-----------|
| Named architect | 3,633 | 36.6% | 3,581 (98.6%) | 25 (0.7%) |
| 49F House | 3,574 | 36.0% | 916 (25.6%) | 2,658 (74.4%) |
| Unassigned | 2,720 | 27.4% | 2,332 (85.7%) | 381 (14.0%) |

### 49F House + splits=0 Deep Dive (2,658 accounts)

- 99.6% have NO advisor at all (no implementor, consultant, or local_ops)
- Only 13.8% (366) are alive in silver allocations
- 2,064 are marked "open" in BD but absent from allocations -- stale/abandoned
- NOT a rotation pattern -- 93% share a relationship name with alive tracked accounts, but only 3.2% have close dates
- These are legacy/dormant accounts BD never formally closed

### Canonical AUA Impact (alive accounts only)

| Segment | Canonical AUA |
|---------|--------------|
| 49F House splits=0 | $172.8M (605 alive accounts) |
| 49F House splits=100 | $357.1M |
| Named architect | $1,078.0M |

### Canonical Asset Breakdown (from bd-securities DynamoDB)

49F House splits=0 (alive): $172.8M
- Equity: $71.9M (41.6%) -- US Large Cap dominant
- **Alternatives: $66.2M (38.3%) -- $60M in structured notes (Opal products)**
- Fixed Income: $22.3M (12.9%) -- skewed to cash ($20M)
- Unclassified: $12.5M (7.2%)

**Conclusion:** These are Opal-managed accounts where fees come through embedded expense ratios on structured products, not advisory fee splits. The $176M is real AUA but revenue flows through a different channel than the split system. Pipeline handles this correctly -- no phantom inflation.

---

## 5. QA EC2 Runner

Launched **bd-gold-qa-runner** (i-0090b823a4a0997e3, c6i.2xlarge, 8 vCPU / 16GB, ~$0.34/hr).

- Same IAM role, subnet, security group as production
- No auto-run on boot -- manual SSM dispatch only
- No auto-shutdown -- must stop manually
- Added to EC2_MANIFEST.json
- Python deps installed: boto3, pandas, pyarrow, python-dateutil, yfinance, openpyxl
- AWS CLI v2 installed

**Finding:** Too slow for loading 2,103 fee detail partitions (timed out at 5 min). Use production runner for heavy partition loads; QA runner suitable for single-script diagnostics with small data.

---

## 6. Diagnostic Scripts Run

| Script | Instance | Result |
|--------|----------|--------|
| E_22.diagnose_unassigned_accounts.py | Production | 762 unassigned accounts, $133.4M AUA |
| E_23.diagnose_fee_splits.py | QA runner | 68.8% of accounts sum to 100%, 3,064 all-zero |
| E_24.rebuild_fee_scorecard.py | Production | 152 advisors, 5 windows, R2 0.14-0.86, JSON uploaded |
| resolve_tickers.py | Production | Ticker resolution table rebuilt |

---

## 7. CloudFront Invalidations

- Partial: `/api/scoped/advisor-intelligence/artifacts/*` (IDGO7SE24ZFILRTM9D2KV9DP5I)
- Full: `/*` (I6VUMW4ZK1ZK6ON5YOWEEFIZG4) -- required due to query-string-keyed cache variants

---

## Infrastructure State

| Instance | ID | State |
|----------|-----|-------|
| bd-gold-layer-runner | i-01003b035d2988dfb | STOPPED |
| bd-gold-qa-runner | i-0090b823a4a0997e3 | STOPPED |

---

## Next Steps

- [DS] Investigate the 381 "Unassigned + splits=0" accounts (96% alive, 96% no advisor -- new accounts awaiting onboarding)
- [DS] Consider portal enhancement: "advisor-managed AUA" vs "firm-managed/embedded fee AUA" distinction
- [AE] Run `--chain rebuild` after next Group A logic change
- [AE] Nightly trigger verified correct: `--chain full --incremental` for daily, `--chain rebuild` monthly
- [DS/AE] Fix E_24 FutureWarning: cast efficiency_pctile column to float before assignment
