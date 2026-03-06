# ADVI_AUAVAR Phase 5: Cash-Only Account Profile EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 19:45
**End Time:** 20:00

---

## Objective

Execute `diag_cash_only_accounts.py` (DS commit `fb71afa4`) on `bd-gold-layer-runner`
(`i-01003b035d2988dfb`) to profile the ~$34M B2 "cash-only/new account" residual bucket
and determine whether it is ready for a clean inclusion path.

Script sourced from `s3://opal-data-bd/code/diagnostics/` (DS pre-uploaded; no local
upload needed). Result: `s3://opal-data-bd/diagnostics/cash_only_account_profile_2026-03-02.json`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Confirm `fb71afa4` in origin/CLOUD | Present — no push needed |
| 2 | Verify script in S3 | `s3://opal-data-bd/code/diagnostics/diag_cash_only_accounts.py` — 23,403 bytes |
| 3 | SSM send-command | CommandId: `72b9ed5a-ade4-4454-b8b9-851ceee84525` |
| 4 | Poll status (~3.5 min) | `Success` |
| 5 | Verify S3 artifacts | JSON: 4,637 bytes / stdout: 10,981 bytes |

---

## Verification

**S3 Artifacts:**
```
s3://opal-data-bd/diagnostics/cash_only_account_profile_2026-03-02.json    4,637 bytes
s3://opal-data-bd/diagnostics/cash_only_account_profile_2026-03-02_stdout.txt  10,981 bytes
```

**SSM Command:** `72b9ed5a-ade4-4454-b8b9-851ceee84525`
**Instance:** `i-01003b035d2988dfb` (bd-gold-layer-runner) — EXIT_CODE:0

---

## Results by Section

**Scope:** 411 open BD accounts with no transaction activity in the 90-day lookback window.
Total AUA: $91,541,826.90.

Note: this is larger than the Phase 2 B2 estimate of ~$34.1M because this script runs
on ALL open accounts without the Phase 2 cube-miss filter. The investment-only subset
(after non-investment exclusions) will be ~$32M, consistent with Phase 2.

### Section 2 — Account Type Composition [FAIL]

Four non-investment account types present — must be excluded before any inclusion decision:

| Type | Count | AUA |
|------|-------|-----|
| Insurance | 99 | $53,741,359 |
| Annuity | 4 | $4,008,291 |
| TermLife | 15 | $1,736,825 |
| CreditCard | 1 | $648 |
| **Non-investment total** | **119** | **~$59.5M** |

Investment-eligible remainder after exclusion: ~411 − 119 = 292 accounts / ~$32M.

### Section 3 — BD Cash vs Non-Cash Field Split [PASS]

| Field | Total |
|-------|-------|
| `account_market_value` (carrier) | $91,541,827 |
| `cash_market_value` | $878,281 |

Zero "cash-primary" accounts — `account_market_value` carries the value throughout.
These accounts hold money market funds or FDIC sweep programs that BD treats as
securities. The gold cube would capture them via position replay IF transaction
records exist — but they don't (hence the no-txn classification).

81 accounts have both fields < $100 (phantom/zero-balance accounts — $756 total).

### Section 4 — Multi-Date Value Stability [PASS]

| Date | Accounts | Total MV | DoD Change |
|------|----------|----------|------------|
| 2026-02-24 | 411 | $91,519,718 | — |
| 2026-02-25 | 411 | $91,585,233 | +$65,515 (+0.07%) |
| 2026-02-26 | 411 | $91,581,160 | −$4,073 (−0.00%) |
| 2026-02-27 | 411 | $91,540,765 | −$40,395 (−0.04%) |
| 2026-02-28 | 411 | $91,540,765 | $0 (+0.00%) |
| 2026-03-02 | 411 | $91,541,827 | +$1,062 (+0.00%) |
| 2026-03-03 | 411 | $91,396,546 | −$145,281 (−0.16%) |
| 2026-03-04 | 411 | $91,447,120 | +$50,575 (+0.06%) |
| 2026-03-05 | 411 | $91,447,120 | $0 (+0.00%) |

MV range: $188,687 over 10 dates. Pct variation: 0.21%. Account set: 411 on every date.
Verdict: **rock-solid stable** — consistent with parked/sweep cash.

### Section 5 — Flow Event Check [WARN]

| Metric | Value |
|--------|-------|
| Target accounts | 411 |
| With ANY historical transaction (ever) | 392 |
| Truly zero history | 19 |
| With flow events (deposit/withdrawal/transfer) | 389 |
| Flow event percentage of no-txn set | **94.6%** — far exceeds 10% threshold |

Top flow event types: Cash Withdrawal (2,111), Cash Deposit (2,078), Transfer In (1,825), Journal (387), Transfer Out (131).

The WARN text in the script reads "flow-event accts < 10% of no-txn set" but the actual ratio is 389/411 = 94.6% — the majority of this bucket are NOT cash-only. They are established accounts with real money-movement history and a recent position-transaction gap.

---

## Validation Check Results

| Check | Result | Detail |
|-------|--------|--------|
| Section 2: no non-investment types | **FAIL** | 119 accounts flagged (Insurance/Annuity/TermLife/CreditCard) |
| Section 3: cash_market_value column present | PASS | $878K cash MV vs $91.5M account MV |
| Section 4: MV variation < 5% | PASS | 0.21% — stable |
| Section 4: account set stable | PASS | 411 on every date (delta: 0) |
| Section 5: flow-event accts < 10% | WARN | 94.6% have flow events — sub-bucket split required |

**Verdict: inclusion path is NOT clean.** Section 2 FAIL blocks any bulk inclusion.
Section 5 result forces a mandatory sub-bucket split before any policy decision.

---

## Sub-Bucket Structure for COO Decision

After stripping non-investment types (119 accounts, ~$59.5M), the remaining 292 accounts split as:

| Sub-bucket | Count | Note |
|------------|-------|------|
| **A** Truly zero transaction history (ever) | 19 | Genuinely new/pre-deployment — cleanest candidates |
| **B** Has history, no recent position txn | 392 (before non-investment strip) | Established accounts with activity gap |
| — of which: has flow events | 389 | Real money-movement — NOT cash-only |
| — of which: position txn only (old) | 3 | Possibly fully liquidated |

The 389 accounts with flow history are misclassified as "cash-only" — they are accounts
that have had deposits, withdrawals, and transfers but no position-level transactions in
the 90-day lookback. The $32M investable residual is predominantly this group.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_cash_only_profile_ec2.md` | New — this file | Pending |

---

## Blockers

None. JSON in S3 — DS unblocked.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Both S3 artifacts confirmed. Section 2 FAIL (119 non-investment accounts) and Section 5
WARN (94.6% flow-event accounts) mean the B2 "cash-only" bucket is not a clean monolith.
DS has the JSON to produce the sub-bucket recommendation for COO.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Sub-bucket recommendation to COO** — with Section 2/5 results, define exclusion list and inclusion criteria for the investment-eligible remainder (~$32M, ~292 accounts, predominantly activity-gap accounts with flow history)
2. **No further DT action required unless DS issues another script**
