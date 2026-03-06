# ADVI_AUAVAR Phase 2: Missing Cube Accounts EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 17:15
**End Time:** 17:25

---

## Objective

Execute `diag_aua_missing_cube_accounts.py` on `bd-gold-layer-runner` (`i-01003b035d2988dfb`)
per DS brief `docs/briefs/devops-brief-auavar-missing-cube-accounts-ec2-run.md`.
Classify the 895 BD accounts ($104.1M) missing from `positions_cube/2026-03-02.parquet`
into closed/open/gap-candidate buckets so DS can complete the AUAVAR variance memo.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push CLOUD (DS commits `2b76456c` + `8078f1c0`) | `ffcca1cf..8078f1c0` pushed |
| 2 | Upload script to S3 | `s3://opal-data-bd/diagnostics/diag_aua_missing_cube_accounts.py` — 17,342 bytes |
| 3 | Write `.tmp_ssm_params.json` | Pull + run + stdout upload + exit code |
| 4 | SSM send-command | CommandId: `0b232872-4d73-45c7-8f6b-dbbec1038c82` |
| 5 | Poll status | `Success` (completed in <60s — txn load fast at 90 partitions, 1.07M rows) |
| 6 | Verify S3 artifacts | JSON: 3,562 bytes / stdout: 6,943 bytes — both non-zero |
| 7 | Download + inspect JSON | All expected keys confirmed |
| 8 | Write session log + commit + push | This file |

---

## Verification

**S3 Artifacts:**
```
s3://opal-data-bd/diagnostics/aua_missing_cube_accounts_2026-03-02.json    3,562 bytes (2026-03-06 17:19 UTC)
s3://opal-data-bd/diagnostics/aua_missing_cube_accounts_2026-03-02_stdout.txt  6,943 bytes (2026-03-06 17:19 UTC)
```

**SSM Command:** `0b232872-4d73-45c7-8f6b-dbbec1038c82`
**Instance:** `i-01003b035d2988dfb` (bd-gold-layer-runner)
**Exit code:** 0
**Transactions loaded:** 1,067,312 rows across 90 partitions

**JSON Top-Level Keys confirmed:** `run_metadata`, `phase1_recap`, `open_flag_analysis`, `closed_date_analysis`, `rel_termination_analysis`, `open_status_breakdown`, `account_type_breakdown`, `dim_analysis`, `txn_analysis`

**Attribution Waterfall (from JSON):**

| Bucket | Count | BD MV | Interpretation |
|--------|-------|-------|----------------|
| [A] Closed (account_is_open=False) | 0 | $0 | None — all 895 are open per BD |
| [B] Open (account_is_open=True) | 895 | $104,066,865.20 | All need explanation |
| [B1] Open + has transactions (90d) | 397 | $13,945,727.45 | Coverage gap candidates — INVESTIGATE |
| [B2] Open + no transactions | 498 | $90,121,137.76 | Cash-only or non-investment accounts |

**Key classification signals:**
- `account_is_open=True` for all 895 — no closed/terminated flags anywhere
- `closed_date`: 0 accounts have one; `relationship_termination_date`: 0 accounts have one
- 868/895 matched in `accounts_dimension` (all with `closed_date=NaT` in dim)
- Tax status on dim-matched: 652 taxable, 157 tax-deferred, 59 tax-exempt

**Account type breakdown (top contributors to B2/no-txn group):**

| Type | Count | BD MV | Note |
|------|-------|-------|------|
| Insurance | 99 | $53,741,359 | Dominant — insurance products not in positions_cube |
| Brokerage | 184 | $11,908,458 | Standard — unexpected to be missing |
| IRA | 167 | $10,847,737 | Standard — unexpected to be missing |
| 401K | 25 | $6,678,255 | Standard |
| Annuity | 4 | $4,008,291 | Insurance-adjacent |
| TermLife | 15 | $1,736,825 | Insurance-adjacent |
| Mortgage | 4 | $-2,327,620 | Liability — negative MV |
| Loans | 2 | $-1,102,660 | Liability — negative MV |
| CreditCard | 20 | $-84,393 | Liability — negative MV |

**Notable findings for DS:**
- Insurance/Annuity/TermLife accounts (118 accounts, ~$59.5M) explain the bulk of B2. These
  are non-investment products — BD tracks MV but no tradeable positions exist for cube
- Liability accounts (Mortgage/Loans/CreditCard, 26 accounts, −$3.5M) contribute negative MV
  to BD's total — artificially widening the raw gap vs gold
- B1 (397 accounts, $13.9M) with transaction history but no cube entry is the genuine
  bug surface area — standard account types (Brokerage, IRA, etc.) that should have cube entries

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Baked stdout upload into main SSM command (no Step 3 separate run) | Consistent with Phase 1 pattern; simpler, one command to track |
| No MSYS_NO_PATHCONV=1 | Same finding as Phase 1 — breaks Python executable path resolution; not needed when no `/` args |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tmp_ssm_params.json` | Overwritten with Phase 2 SSM params | No — temp file |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_phase2_missing_cube_accounts_ec2.md` | New — this file | Pending |

**S3 writes (diagnostics prefix only):**
- `s3://opal-data-bd/diagnostics/diag_aua_missing_cube_accounts.py`
- `s3://opal-data-bd/diagnostics/aua_missing_cube_accounts_2026-03-02.json`
- `s3://opal-data-bd/diagnostics/aua_missing_cube_accounts_2026-03-02_stdout.txt`

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Both Phase 2 S3 artifacts confirmed. All 895 missing-cube accounts are open per BD with no
closed/termination flags. Dominant explanation: 118 Insurance/Annuity/TermLife accounts
($59.5M) are non-investment products with no tradeable positions. 26 liability accounts
(Mortgage/Loans/CC, −$3.5M) pull BD total negative relative to gold. True coverage gap
surface: 397 accounts ($13.9M) — open, have transactions, no cube entry.
DS (`0.4.0_DS_ClientPlatform`) is unblocked to read both Phase 1 + Phase 2 JSON and
write the AUAVAR variance memo for COO.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Write AUAVAR variance memo** — DS reads Phase 1 + Phase 2 JSON, produces memo for COO. Key callouts: Insurance exclusion ($59.5M), liability MV drag (−$3.5M), B1 bug surface ($13.9M)
2. **No further DT action required for ADVI_AUAVAR Phase 2**

**Do NOT:**
- Re-run either diagnostic script without DS/COO approval
- Modify any gold/ or silver/ data
