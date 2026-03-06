# ADVI_AUAVAR B1 Root Cause Rerun (Script 02 _source_file check) — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 18:00
**End Time:** 18:10

---

## Objective

Re-run revised `diag_aua_b1_root_cause.py` (DS commit `645229ea`) after DS rewrote
hypothesis framework to check `_source_file` on all B1 account transactions.
New script classifies B1 accounts as ACT (Script 02 bug), BKF (backfill-only, capped
by design), or UNK. Runtime ~8-12 min (loads all 1,743 transaction partitions).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push DS commit `645229ea` | `b8569829..645229ea` pushed |
| 2 | Upload revised script to S3 | `s3://opal-data-bd/diagnostics/diag_aua_b1_root_cause.py` — 17,372 bytes |
| 3 | SSM send-command | CommandId: `d443cb2f-b95d-4058-939a-3d3993dc365c` |
| 4 | Poll status (5 min) | `Success` (completed in <5 min — full 1,743-partition scan, B1-filtered) |
| 5 | Verify S3 artifacts | JSON: 4,310 bytes / stdout: 6,328 bytes — both non-zero |
| 6 | Inspect stdout SUMMARY | Clean — EXIT_CODE:0, JSON written |

---

## Verification

**S3 Artifacts:**
```
s3://opal-data-bd/diagnostics/aua_b1_root_cause_2026-03-02.json    4,310 bytes (2026-03-06 18:05 UTC)
s3://opal-data-bd/diagnostics/aua_b1_root_cause_2026-03-02_stdout.txt  6,328 bytes (2026-03-06 18:05 UTC)
```

**SSM Command:** `d443cb2f-b95d-4058-939a-3d3993dc365c`
**Instance:** `i-01003b035d2988dfb` (bd-gold-layer-runner)
**Exit code:** 0
**Transactions loaded:** 57,579 B1-account rows from 1,743 total partitions

---

## Results

**B1 attribution (397 accounts, $13,945,727.45):**

| Bucket | Count | BD MV | Meaning |
|--------|-------|-------|---------|
| **[ACT] Script 02 BUG** | **164** | **$7,360,069.92** | Has TXN_DAILY records — should be in cube but isn't |
| **[BKF] Backfill-only** | **233** | **$6,585,657.53** | No TXN_DAILY records — Script 02 intentionally capped at last-txn-date |
| [UNK] Not in any partition | 0 | $0.00 | None — clean |

**BKF recency (233 accounts):**
- Median days since last transaction: 41
- Min: 35 days / Max: 105 days
- All last transacted in 2025Q4 or 2026Q1 — no stale/ancient accounts
- 0 accounts > 180 days, 0 > 365 days
- Account types: Brokerage (69, $3.1M), IRA (48, $236K), Joint (32, $1.5M), 403B (3, $1.0M), Charitable (13, $616K), + others

---

## Findings for DS/COO

**Two distinct issues — different owners:**

**1. ACT ($7.4M, 164 accounts) — Script 02 secondary filter bug**

These accounts have TXN_DAILY records (live pipeline data), so `_compute_account_end_dates()`
should forward-fill them to `global_end_date`. They ARE reaching the cube-build step but
getting dropped by a *secondary* filter in Script 02 beyond `account_end_dates`. DS/AE
need to inspect Script 02 for additional join conditions or exclusion logic that drops
ACT accounts.

**2. BKF ($6.6M, 233 accounts) — policy decision, not a bug**

Script 02 behavior is *correct by design* — backfill-only accounts cap at last-txn-date.
But these accounts are recent (median 41 days, all 2025Q4–2026Q1) and BD confirms they
hold real securities. This is an architectural choice:

- **Option 1 (accept gap):** These are no longer in the daily feed; their holdings are
  unverifiable without a silver positions source. The ~$6.6M BD gap is expected and documented.
- **Option 2 (extend forward-fill):** Join BD allocations to the cube build — if an account
  is in `silver/allocations/{date}.parquet` with `account_is_open=True` and non-zero MV,
  extend its forward-fill regardless of last-txn-date. Requires Script 02 change (AE work).

**Total addressable gap:** ACT ($7.4M) is fixable. BKF ($6.6M) requires a policy call.
Combined = $13.9M of the original $73.6M raw gap.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| 90-partition lookback for B1 identification (same as Phase 2) | DS explicitly restored this in the rewrite — produces 397 B1 accounts consistent with Phase 2 |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_b1_root_cause_rerun_ec2.md` | New — this file | Pending |

---

## Blockers

None. JSON in S3, DS unblocked.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Both S3 artifacts confirmed. B1 cleanly split: 164 ACT (Script 02 secondary filter bug,
$7.4M) and 233 BKF (backfill-only by design, $6.6M, all recent 2025Q4–2026Q1). DS can
now write the AUAVAR variance memo with full root-cause attribution. ACT requires Script 02
investigation (AE). BKF requires architectural policy decision (COO).

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Write AUAVAR variance memo** — full picture now available across Phase 1, Phase 2, and B1 root cause. Report to COO.
2. **COO policy decision** — BKF option 1 vs option 2
3. **AE investigation (if ACT confirmed actionable)** — inspect Script 02 for secondary filter dropping 164 ACT accounts

**Do NOT:**
- Run further diagnostics on this chain without DS/COO direction
