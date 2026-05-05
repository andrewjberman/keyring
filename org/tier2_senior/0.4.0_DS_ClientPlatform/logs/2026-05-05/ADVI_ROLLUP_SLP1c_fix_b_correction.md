# Session Log — ADVI_ROLLUP.SL-P1c Fix B Correction Ship

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-05
**Task Order:** ADVI_ROLLUP.SL-P1c.b01-denominator-fix
**Status:** SHIPPED — RAVC3 to CTO + COO sent; awaiting AE SLEEVE_SHADOW_DISABLE unset

---

## Summary

Implemented SL-P1c Fix B correction in `B_01.holdings_lots.py` per CTO RAVC2 ratification
(received end of 2026-05-04 session). Root cause analysis was completed in prior session
(`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-04/ADVI_ROLLUP_SLP1c_shadow_root_cause.md`).

Change: revert `non_cash_target_mv` formula to `max(account_mv - cash_mv, 0.0)`, removing
the FIFO-subtract overcorrection introduced by Fix B. `fifo_mv_by_acct` dict and
`fifo_covered_mv` retained per CTO condition #5. SL-P1b denominator fix preserved.

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| ds-commit-gate | B_01.holdings_lots.py | PASS — py_compile + AST + ruff all exit 0 |
| comp-pipescript deployed | B_01 | MATCH (S3 ETag current 2026-05-05) |

---

## Code Change

**File:** `data/black_diamond/scripts/gold/B_01.holdings_lots.py`

**Lines 948-952 (comment — before):**
```
# SL-P1c Fix B: per-account FIFO-covered MV used to compute uncovered apportionment base.
# Prevents non-vetoed lots from receiving the full account_mv when FIFO already covers most
# of the account (root cause of SL-P1b ITERATE: total_unit_cost denominator included vetoed
# positions, deflating surviving lot weights to their fractional share of non_cash_target_mv).
```

**Lines 948-952 (comment — after):**
```
# SL-P1c Fix B (corrected 2026-05-05): fifo_mv_by_acct retained for observability / future use.
# non_cash_target_mv reverts to full non-cash MV (account_mv - cash_mv); the FIFO-subtract
# formula overcorrected when HLOT2b reopen lots made fifo_covered_mv ≈ full account non-cash MV,
# leaving non_cash_target_mv ≈ 0 for 98% of sleeve accounts and suppressing the shadow entirely.
# The SL-P1b denominator fix (non-vetoed-only total_unit_cost) is preserved and still correct.
```

**Line 977 (before):**
```python
fifo_covered_mv = fifo_mv_by_acct.get(acct_id, 0.0)
non_cash_target_mv = max(account_mv - cash_mv - fifo_covered_mv, 0.0)
```

**Lines 977-978 (after):**
```python
fifo_covered_mv = fifo_mv_by_acct.get(acct_id, 0.0)  # noqa: F841 -- retained for observability
non_cash_target_mv = max(account_mv - cash_mv, 0.0)
```

**Lines 1000-1004 (comment — before):**
```
# Non-cash: Path 3 cost-basis apportionment (SL-P1c Fix B).
# Filter to non-vetoed positions BEFORE computing total_unit_cost so that
# the denominator only reflects positions that will actually produce lots.
# non_cash_target_mv is the uncovered portion (account_mv - cash_mv - fifo_covered_mv),
# so vetoed positions correctly receive zero MV allocation.
```

**Lines 1001-1004 (comment — after):**
```
# Non-cash: Path 3 cost-basis apportionment (SL-P1c Fix B, corrected).
# non_cash_target_mv = full non-cash MV (account_mv - cash_mv).
# Denominator uses non-vetoed positions only (total_unit_cost from grp_nc_pass),
# so FIFO-covered lots contribute zero weight without shrinking the apportionment target.
```

---

## Deploy Cycle

| Step | Result |
|------|--------|
| Pre-commit gate | PASS — all 3 checks exit 0 |
| safe-commit.sh | Contamination abort on first attempt (docs/architecture/INFLEC_FE_BACKEND_WIRING.md + org/projects/ADVI_INFLFE.json staged by another agent). Unstaged extras via `git reset HEAD --`, clean commit on second attempt. |
| Commit | `e3463bffa` — fix(B_01): SL-P1c Fix B correction |
| Push | origin/CLOUD — f6ea12221..e3463bffa |
| S3 upload | s3://opal-data-bd/code/gold/B_01.holdings_lots.py (147.3 KiB) |
| comp-pipescript deployed | MATCH |
| RAVC3 to CTO | Sent 20260505T130444Z |
| RAVC3 to COO | Sent 20260505T130453Z |

---

## Also This Session: AUDIT-001 ORANGE Verification Accepted (COO RAVC4)

COO RAVC4 received confirming AUDIT-001 findings from prior session accepted:

| Cell | Final verdict |
|---|---|
| header_metrics.total.fee_earning_account_count | ORANGE — field name mismatch; shows 0 at firm level |
| concentration_risk | Reclassified RED-(c) upstream INF_B_01 pricing gap |
| clients_tab L3 summary.tax | GREEN — FE reads raw.summary?.tax correctly |
| leaderboard.role_breakdown | GREEN |
| fee_earning_aua / non_fee_earning_aua | GREEN |

Account_id int64 mismatch finding logged as addendum to AUDIT-002 scope.

---

## Acceptance Criteria Status

| AC | Status | Notes |
|----|--------|-------|
| AC#1: Pre-commit gate clean | DONE | ds-commit-gate exit 0 |
| AC#2: Jones z0817905851 shadow MV = cash-only | PENDING | First nightly post-unset |
| AC#3: 3 pure-sleeve within 2% | PENDING | First nightly post-unset |
| AC#4: Cohort stability ±5 across 3 dates | PENDING | 3 nightly emissions needed |
| AC#5: Open MV per nightly assertion | PENDING | 3 nightly emissions needed |
| AC#6: 3 consecutive clean nightly emissions | PENDING | AE must unset SLEEVE_SHADOW_DISABLE first |
| AC#7: No regression to canonical holdings_lots | N/A | Shadow is separate artifact |
| AC#8: RAVC4 to COO | PENDING | After AC#6 gate passes |
| AC#9: Session log | COMPLETE | This document |

---

## Carry-forwards

1. **AE SLEEVE_SHADOW_DISABLE unset** — COO to dispatch AE 0.6.0/0.7.0; gates 3-nightly observation.
2. **AC#2-6 validation** — Monitor nightly emissions after unset; RAVC4 to COO on AC#6 close.
3. **ADVI_BFIX4 TO-2** — Gated on Andrew B1 ruling; do NOT proceed.
