# ADVI_AUAVAR: ACAT Confirmation Diagnostic EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 20:10
**End Time:** 20:15

---

## Objective

Execute `diag_acat_confirmation.py` (DS commit `bb794d8b`) on `bd-gold-layer-runner`
(`i-01003b035d2988dfb`) to classify the activity-gap account population and determine
the fix path verdict: ACAT_CONFIRMED, BUY_AND_HOLD, or MIXED.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push pending DT commit `1094bb17` | `bb794d8b..1094bb17` pushed |
| 2 | Verify script in S3 | `s3://opal-data-bd/code/diagnostics/diag_acat_confirmation.py` — 27,900 bytes |
| 3 | SSM send-command | CommandId: `c4ebbaeb-c20c-40d0-91fb-573066342ea8` |
| 4 | Poll status | `Success` (<2 min) |
| 5 | Verify S3 artifacts | JSON: 4,399 bytes / stdout: 8,905 bytes |

---

## Verification

```
s3://opal-data-bd/diagnostics/acat_confirmation_2026-03-02.json    4,399 bytes
s3://opal-data-bd/diagnostics/acat_confirmation_2026-03-02_stdout.txt  8,905 bytes
```

**SSM Command:** `c4ebbaeb-c20c-40d0-91fb-573066342ea8` | EXIT_CODE: 0

---

## Results

**Scope (re-derived):** 715 activity-gap accounts / $89,070,388 AUA
(stripped 120 non-investment accounts from full open set before derivation)

### Section 2 — Full Transaction History Classification

| Label | Count | AUA | Meaning |
|-------|-------|-----|---------|
| FLOW_ONLY (no position records ever) | 215 | $36,437,923 | Deposits/withdrawals only — ACAT/cash candidates |
| OLD_POS (position records, predating 90d) | 327 | $31,487,092 | Buy-and-hold — BKF fix territory |
| UNKNOWN | 161 | $16,471,242 | No recognizable pattern |
| NO_HISTORY (truly zero records) | 12 | $4,674,132 | New/pre-deployment |
| ACAT_ONLY | 0 | $0 | None labeled explicitly as ACAT |

### Section 3 — ACAT Pattern Detection

Zero explicit ACAT-labeled transaction_type values found in the data. The ACAT
keyword pattern matched nothing. All FLOW-type transactions for activity-gap accounts are:

| Type | Count |
|------|-------|
| Dividend | 19,041 |
| Interest | 6,535 |
| Journal | 385 |
| Income | 15 |

**Implication:** In-kind transfers are NOT labeled "ACAT," "Transfer In Kind," or "Receive" —
they arrive as Dividend/Interest/Income records or are simply absent from the transaction
feed entirely. The 215 FLOW_ONLY accounts had only these income-type events, never a
position buy or sell.

### Section 4 — OLD_POS Account Age Distribution (327 accounts)

| Age bucket | Count |
|------------|-------|
| 91–180d since last position txn | 93 |
| 181–365d | 100 |
| 366–730d (1–2 years) | 83 |
| > 730d (2+ years) | 51 |

Median: 266 days. Mean: 380 days. Max: 1,355 days.
All 327 genuinely beyond the 90-day lookback — no pipeline parsing issue.

### Section 5 — Security Detail

Not available from allocations — BD's `silver/allocations/` is account-level only.
Security holdings would require a separate BD positions feed (`silver/positions/`),
which does not exist in this environment.

---

## Determination

**MIXED** — no single dominant explanation.

| Path | Accounts | AUA | Pct |
|------|----------|-----|-----|
| FLOW_ONLY + NO_HISTORY (zero position records) | 227 | $41,112,054 | 31.7% |
| OLD_POS (buy-and-hold, BKF fix territory) | 327 | $31,487,092 | 45.7% |
| UNKNOWN | 161 | $16,471,242 | 22.5% |

Neither threshold (≥70%) reached → two separate fix paths required.

---

## Key Findings for DS

**1. OLD_POS (327 accounts, $31.5M) — BKF fix (`91b1918a`) likely already covers these.**
These are buy-and-hold accounts with real position records older than 90 days. Median
266 days since last position txn. `_compute_account_end_dates()` currently caps them at
their last-txn-date; the deployed fix extends confirmed-open accounts to `global_end_date`.
If these accounts appear in `silver/allocations/2026-03-02.parquet` with `account_is_open=True`,
they will get cube entries in the next rebuild. No additional fix needed — verify after rebuild.

**2. FLOW_ONLY (215 accounts, $36.4M) — NOT ACAT in the traditional sense.**
These accounts have Dividend, Interest, Journal, and Income records but zero position
buy/sell records ever. They are not "transfer in kind" candidates — the transaction
feed simply never contained position-level events for them. Two explanations:
  - Their holdings arrived via a non-transaction mechanism (balance snapshot feed, not
    replayed from trades) — this is the true positions seed gap
  - They hold only cash/money-market instruments that generate income but no position events

A separate positions seed feed (Bronze→Silver path for initial balance snapshots) would
be needed to cover this sub-bucket. This is AE scope.

**3. ACAT label does not exist in this transaction dataset.** Whatever in-kind transfers
occurred are not tagged as such. If a positions seed feed is built, it cannot rely on
an "ACAT" transaction_type filter — it needs a different detection mechanism or a
separate Bronze data source (e.g., BD's positions export file rather than the transaction
feed).

**4. UNKNOWN (161 accounts, $16.5M)** — neither flow-only nor position-bearing. Likely
accounts where the transaction pattern doesn't match any known label (Journal In, corporate
actions, or other non-standard types). DS should inspect a sample from the JSON
`unknown_sample_ids` field.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_acat_confirmation_ec2.md` | New — this file | Pending |

---

## Blockers

None. JSON in S3 — DS unblocked.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

MIXED verdict confirmed. 327 OLD_POS accounts ($31.5M) should resolve after the BKF
cube rebuild (verify post-rebuild). 215 FLOW_ONLY accounts ($36.4M) require a positions
seed feed — AE scope, new pipeline path. 161 UNKNOWN accounts ($16.5M) need DS
inspection of sample IDs from JSON. No ACAT transaction labels exist in the feed —
in-kind detection cannot rely on transaction_type keyword matching.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Verify OLD_POS after next cube rebuild** — 327 accounts should appear in cube once BKF fix runs; if not, secondary investigation needed
2. **AE scope decision (COO/Andrew)** — positions seed feed for 215 FLOW_ONLY accounts ($36.4M) is a new Bronze→Silver pipeline path
3. **[0.4.0_DS_ClientPlatform] Inspect UNKNOWN sample IDs** — 161 accounts / $16.5M unexplained; JSON has `unknown_sample_ids` field
4. **No further DT action required until rebuild authorized or AE scope confirmed**
