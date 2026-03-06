# ADVI_AUAVAR: UNKNOWN Bucket Transaction Type Inspection — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 20:15
**End Time:** 20:25

---

## Objective

Execute `diag_unknown_txn_types.py` (DS commit `0991adbf`) on `bd-gold-layer-runner`
to determine whether the 161 UNKNOWN activity-gap accounts represent a pattern extension
gap or a genuinely new fix bucket.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Confirm `0991adbf` in origin/CLOUD + script in S3 | Present — no push needed |
| 2 | SSM send-command | CommandId: `76f68ff0-cb1f-4a12-ac83-331fd81b617c` |
| 3 | Poll status (~4 min) | `Success` |
| 4 | Verify S3 artifacts | JSON: 2,235 bytes / stdout: 9,595 bytes |

---

## Verification

```
s3://opal-data-bd/diagnostics/unknown_txn_inspection_2026-03-02.json    2,235 bytes
s3://opal-data-bd/diagnostics/unknown_txn_inspection_2026-03-02_stdout.txt  9,595 bytes
```

**SSM Command:** `76f68ff0-cb1f-4a12-ac83-331fd81b617c` | EXIT_CODE: 0

---

## Results

**Note on re-derivation:** The JSON from `diag_acat_confirmation.py` did not contain
pre-extracted `unknown_account_ids`, so the script re-derived from transactions directly.
Re-derived count: **376** (vs 161 from previous run) — the additional accounts are those
previously classified via the 90-day recent lookback only; the full-history re-derivation
surfaces more accounts with the UNKNOWN pattern. The prior 161 is a subset.

**All transaction_type labels present for UNKNOWN accounts (13 unique):**

| transaction_type | Rows | Pattern label |
|-----------------|------|--------------|
| Cash Withdrawal | 12,709 | UNKNOWN — not in POSITION_BROAD_PATTERN |
| Cash Deposit | 3,946 | UNKNOWN |
| Transfer In | 3,549 | UNKNOWN |
| Interest | 1,772 | FLOW |
| Sale | 1,219 | UNKNOWN — position-affecting, not matched |
| Dividend | 902 | FLOW |
| Expense | 440 | UNKNOWN |
| Management Fee | 343 | UNKNOWN |
| Journal | 235 | FLOW |
| Transfer Out | 101 | UNKNOWN |
| Valuation | 9 | UNKNOWN |
| Income | 4 | FLOW |
| Capital Gains | 4 | UNKNOWN |

**Unit/quantity check:** 24,920 of 25,233 rows have non-zero `units` — these ARE
position-affecting. Cash Withdrawal, Cash Deposit, Transfer In, Sale, Expense, Management
Fee, Transfer Out, Capital Gains all carry non-zero unit values. They are position
transactions recorded under labels the current `POSITION_BROAD_PATTERN` doesn't match.

---

## Verdict: PATTERN EXTENSION

376 UNKNOWN accounts have position-affecting records (non-zero units) under non-standard
type labels. Extending `POSITION_BROAD_PATTERN` to include these terms will reclassify
all 376 into known buckets.

**Key non-standard position labels:** `Cash Withdrawal`, `Cash Deposit`, `Transfer In`,
`Sale`, `Expense`, `Management Fee`, `Transfer Out`, `Capital Gains`, `Valuation`.

`Sale` (1,219 rows) is the clearest miss — unambiguously a position transaction.
`Transfer In` (3,549 rows, 3,241 with non-zero units) matches the extended pattern term
`transfer` (3,650 rows matched across 2 types).

**Expected reclassification:** All 376 accounts should move from UNKNOWN → OLD_POS or
FLOW_ONLY once patterns are extended. Given that `Sale` and `Transfer In` are position
types, most should land in OLD_POS — which means the BKF fix covers them. No new
engineering required for this bucket.

---

## Impact on Fix Path Sizing

| Bucket (current) | Count | AUA |
|-----------------|-------|-----|
| OLD_POS — self-resolves via BKF rebuild | 327 | $31.5M |
| FLOW_ONLY — positions seed feed (AE scope) | 215 | $36.4M |
| UNKNOWN → reclassifies (pattern extension) | 376 | $52.9M |
| NO_HISTORY | 12 | $4.7M |

After pattern extension re-run, UNKNOWN collapses into OLD_POS or FLOW_ONLY. If the
majority land in OLD_POS (likely, given Sale + Transfer In), the positions seed feed
scope stays at ~$36.4M (215 accounts). If a significant portion land in FLOW_ONLY,
seed feed scope expands. DS has the JSON — re-running `diag_acat_confirmation.py` with
extended patterns gives the clean split.

**BD profile of the 376 UNKNOWN accounts:**
Standard investment account types — Trust (32, $20.5M), Joint (26, $11.6M), IRA (76,
$6.9M), Brokerage (70, $5.9M) are the top four by AUA. No Insurance or liability
accounts. Total AUA: $52,909,165.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_unknown_txn_inspection_ec2.md` | New — this file | Pending |

---

## Blockers

None. JSON in S3 — DS unblocked.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

PATTERN EXTENSION verdict. 376 UNKNOWN accounts have real position-affecting records
under non-standard type labels (Sale, Transfer In, Cash Withdrawal/Deposit, etc.).
Extending POSITION_BROAD_PATTERN and re-running `diag_acat_confirmation.py` will
produce the clean bucket split. Expected outcome: most UNKNOWN accounts reclassify as
OLD_POS → self-resolve via BKF rebuild. Positions seed feed scope ($36.4M baseline)
may expand slightly if any reclassify as FLOW_ONLY.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Extend POSITION_BROAD_PATTERN + re-run diag_acat_confirmation.py** — incorporate Sale, Transfer In, Cash Withdrawal/Deposit, Capital Gains into pattern; re-run for clean OLD_POS/FLOW_ONLY/NO_HISTORY split
2. **COO/Andrew decision** — authorize positions seed feed (AE scope) for FLOW_ONLY bucket once final size confirmed
3. **No further DT action required until DS re-runs with extended patterns or authorizes rebuild**
