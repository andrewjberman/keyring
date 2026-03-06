# ADVI_AUAVAR: ACAT Confirmation v2 (Extended Patterns) EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 22:05
**End Time:** 22:15

---

## Objective

Re-run `diag_acat_confirmation.py` (DS commit `5dd75c6d`) on `bd-gold-layer-runner`
(`i-01003b035d2988dfb`) with three pattern extensions applied by DS:
1. `POSITION_BROAD_PATTERN` now catches `sale`, `transfer.?in`, `transfer.?out`
2. FLOW rows with non-zero units reclassify to POSITION
3. Both Section 1 target derivation and Section 2 per-account classification use
   updated logic consistently

Expected outcome per DS: most of the 376 UNKNOWN accounts shift to OLD_POS, combined
BKF-recoverable pool ~700 accounts / ~$83M.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Confirm DS commit `5dd75c6d` in origin/CLOUD | Present — no push needed |
| 2 | Upload updated script to S3 | `s3://opal-data-bd/code/diagnostics/diag_acat_confirmation.py` — 28,385 bytes (v1 was 27,900; overwrite confirmed) |
| 3 | SSM send-command (python3) | CommandId: `fb2b9a60-3b8d-49a9-9ef3-179e0ff54345` |
| 4 | Note — first attempt used `python` (not found on EC2) | CommandId `670eeeaa` — failed; fixed to `python3` |
| 5 | Poll status | `Success` (~2.5 min) |
| 6 | Verify S3 artifacts | JSON: 4,344 bytes / stdout: 9,403 bytes |

---

## Verification

```
s3://opal-data-bd/diagnostics/acat_confirmation_2026-03-02.json    4,344 bytes  (2026-03-06 17:11:09)
s3://opal-data-bd/diagnostics/acat_confirmation_2026-03-02_stdout.txt  9,403 bytes  (2026-03-06 17:11:14)
```

**SSM Command:** `fb2b9a60-3b8d-49a9-9ef3-179e0ff54345` | EXIT_CODE: 0

---

## Results

### Section 1 — Activity-Gap Target Re-Derivation (Extended Patterns)

| Metric | v1 Run | v2 Run (extended) | Delta |
|--------|--------|-------------------|-------|
| Investment-open accounts | 6,002 | 6,002 | — |
| Accts w/ recent position txn (90d) | 5,449 | **5,672** | +223 |
| Activity-gap target accounts | 715 | **465** | -250 |
| Target AUA | $89,070,388 | **$33,187,010** | -$55.9M |

**The pattern extension resolved 250 accounts at the Section 1 level.** These accounts
had Sale, Transfer In, Transfer Out records in the 90-day lookback that weren't matching
`POSITION_BROAD_PATTERN` before. With the extended pattern they now qualify as having
"recent position txns" and exit the activity-gap entirely. The gap itself shrunk from
715 to 465 accounts before Section 2 even runs.

### Section 2 — Full Transaction History Classification (465 accounts)

| Label | Count | AUA | Pct | v1 count |
|-------|-------|-----|-----|---------|
| OLD_POS (position records, predate 90d) | **386** | $26,846,938 | **83.0%** | 327 |
| UNKNOWN | 66 | $1,665,937 | 14.2% | 161 |
| NO_HISTORY (zero records) | 12 | $4,674,132 | 2.6% | 12 |
| FLOW_ONLY (no position records ever) | 1 | $3.09 | 0% | 215 |
| ACAT_ONLY | 0 | $0 | 0% | 0 |

FLOW_ONLY collapsed from 215 to 1 — the 214 accounts previously in that bucket
had non-zero unit FLOW records (Cash Withdrawal/Deposit with securities) that now
reclassify as POSITION under the updated logic.

### Section 3 — ACAT Pattern Detection

Zero explicit ACAT-labeled rows. All FLOW-type records for the remaining 466 accounts:
Dividend (1,644), Interest (193), Journal (4). Consistent with v1.

### Section 4 — OLD_POS Age Distribution (386 accounts)

| Age bucket | Count |
|------------|-------|
| 91–180d | 81 |
| 181–365d | 109 |
| 366–730d (1–2 years) | 141 |
| > 730d (2+ years) | 55 |

Median: 368 days. Mean: 413 days. Max: 1,090 days.
Zero accounts in the 0-90d window — all genuinely outside lookback.

---

## Determination

**BUY-AND-HOLD** (83.0% threshold met — was MIXED in v1 at 45.7%)

The extended patterns resolved the MIXED verdict. 83% of activity-gap accounts
have real position records older than 90 days. These are buy-and-hold clients
whose last position transaction predates the 90-day lookback window.

---

## Key Findings for DS

**1. Pattern extension primary effect was at Section 1, not Section 2.**
The DS expected 376 UNKNOWNs to shift to OLD_POS within Section 2. What actually
happened: 250 of those accounts had Sale/Transfer In/Transfer Out activity in the
last 90 days — once the pattern caught them in Section 1, they exited the activity
gap entirely (now classified as covered). The Section 1 target dropped from 715 to
465. The remaining 386 OLD_POS accounts were genuinely inactive for >90d.

**2. Combined BKF-recoverable pool is smaller than projected, not larger.**
DS expected ~700 accounts / ~$83M. Actual outcome:
- Section 1 reduction: 250 accounts reclassified as active (now covered by regular cube)
- Remaining activity gap: 465 accounts / $33.2M
- Of those: 386 OLD_POS / $26.8M are BKF fix territory
- Combined with Phase 3 BKF (143 accounts / ~$6.6M): overlap unknown, but these are
  distinct populations (Phase 3 BKF came from the B1 "has recent txns" bucket;
  these 386 are from B2 "no recent txns" bucket). Total is likely additive: ~529
  accounts / ~$33M.

**3. BKF fix (`91b1918a`) should cover the 386 OLD_POS accounts.**
Same profile as Phase 3 BKF accounts (buy-and-hold, backfill-only records, median
last position txn 368 days ago). If these accounts appear in
`silver/allocations/2026-03-02.parquet` with `account_is_open=True`, the deployed
fix will extend them to `global_end_date` on next rebuild. Verification needed
post-rebuild — not confirmable without running a rebuild.

**4. UNKNOWN bucket is now 66 accounts / $1.7M (was 161 / $16.5M).**
Most of the previous UNKNOWNs resolved via pattern extension. Remaining 66 are
small in AUA. DS may still want to sample `unknown_sample_ids` from JSON if
these need to be classified, but they are not material to the overall sizing.

**5. FLOW_ONLY (1 account / $3.09) is negligible.**
The 215 FLOW_ONLY accounts from v1 were accounts with non-zero unit FLOW records
(Cash Withdrawal/Deposit with securities) — now correctly reclassifying as POSITION.
No positions seed feed scope required for this population.

---

## Technical Note — python vs python3

First SSM attempt used `python` (CommandId `670eeeaa`) — failed with
`/var/lib/amazon/ssm/.../script.sh: 2: python: not found`.
EC2 instance requires `python3`. Fixed in second dispatch.
**Use `python3` for all future SSM commands to `bd-gold-layer-runner`.**

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_acat_confirmation_v2_ec2.md` | New — this file | Pending |

**S3 writes:**
- `s3://opal-data-bd/diagnostics/acat_confirmation_2026-03-02.json` (overwritten, v2)
- `s3://opal-data-bd/diagnostics/acat_confirmation_2026-03-02_stdout.txt` (overwritten, v2)

---

## Blockers

None. JSON in S3 — DS unblocked.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

BUY-AND-HOLD verdict confirmed (83% OLD_POS). Extended patterns resolved the MIXED
verdict from v1 by catching 250 accounts at Section 1 (they now have "recent position
txns" under the broadened pattern). Activity gap shrunk from 715 accounts / $89M to
465 accounts / $33.2M. Remaining 386 OLD_POS accounts ($26.8M) are covered by the
BKF fix deployed at `91b1918a` — verify post-rebuild. FLOW_ONLY scope collapses to
negligible ($3). No positions seed feed engineering needed for this population.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Update variance memo with v2 numbers** — activity gap is
   $33.2M (not $89M); FLOW_ONLY population negligible; BKF fix covers ~83% of remaining
   gap; combined recoverable ~$26.8M (plus Phase 3 BKF $6.6M) on next rebuild
2. **[Andrew/COO] Authorize cube rebuild** — BKF fix is deployed (`91b1918a`);
   activating it requires a full cube rebuild run on `bd-gold-layer-runner`
3. **[0.4.0_DS_ClientPlatform] Optional: inspect UNKNOWN sample IDs (66 accounts / $1.7M)**
   from JSON if classification is needed — not material to sizing
4. **No further DT action required** until rebuild authorized or DS issues new diagnostic

**Do NOT:**
- Use `python` (not `python3`) in future SSM commands to `bd-gold-layer-runner`
- Rerun diagnostics without DS direction
- Trigger cube rebuild without explicit COO/Andrew authorization
