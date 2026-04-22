# Session Log: AUAGAP.001 RCA Investigation

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-22
**Task Order:** ADVI_STAUDT.AUAGAP.001
**Status:** Complete. RCA committed bb823bf8. CTO+COO notified.

---

## Investigation Summary

Investigated 49F portal AUA Q1-Q3 2025 regression (~70% drop, $1.4B -> $300M).

### What I investigated

1. canonical_prices coverage and values for Q1-Q3 2025 — confirmed clean
2. positions_cube vs canonical/holdings account counts for 2025-03-31
3. accounts_dimension closed_date distribution
4. alive_cache filter behavior (silver/allocations start date)
5. B_00.canonical_holdings.py code: reconcile_date(), build_persistent_rps_accts(),
   BFIX1+BFIX2 mechanism, units>0 filter, admitted_accts scope

### What I found (base DS)

- positions_cube 2025-03-31: 5,595 accounts vs canonical/holdings 2025-03-31: 2,057 accounts
- 3,538 missing accounts hold valid-priced equities — not a pricing issue
- Closed accounts: only 374 — cannot explain 3,538
- alive_cache filter: skipped (empty set = falsy; silver/allocations has no 2025 data)
- build_persistent_rps_accts() uses sorted_dates[-7:] = last 7 globally (April 2026 dates)
- This static ~5,450-account set is applied to ALL historical target dates
- bd_stale fires on accounts in the 2026 set but absent from 2025 RPS
- BFIX2 does NOT rescue: admitted_accts computed before units>0 filter

**My initial hypothesis (partially correct):** Schwab RPS universe grew from 2025 to 2026,
causing temporal mismatch. Correct mechanism direction, wrong specific cause.

### DS~D's finding (confirmed precise root cause)

Direct S3 inspection of 2025 Schwab RPS partitions: account IDs are ANON_<hash> format
(anonymized test data), not real 10-digit Schwab account numbers. Only 1 of 3,931 RPS
rows maps via schwab_to_bd. schwab_df has 1 account. schwab_persistent_accts (2026)
marks ~5,450 accounts is_schwab_covered=True but has_schwab=False -> bd_stale -> $934M
dropped on 2025-01-02 alone.

---

## Root Cause (Final)

**ANON_* account IDs in Schwab RPS S3 partitions from 2025-01-02 onward (test data
written to production S3 bucket). prepare_schwab_partition() maps 1/3,931 rows.
Combined with BFIX1's global schwab_persistent_accts, all ~5,449 accounts with real BD
positions are classified bd_stale and dropped from canonical/holdings.**

---

## Files Committed

- `data/black_diamond/diagnostics/aua25q_rca.md` — initial RCA (commit 43c7e5db)
- `data/black_diamond/diagnostics/aua25q_rca.md` — revised with DS~D finding (commit bb823bf8)
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.AUAGAP.001.ds-canonical-prices-q1q3-2025-audit.md` — status: complete

---

## MCPs Fired

- 20260422T123504Z — CTO: initial RCA (bd_stale temporal scope hypothesis)
- 20260422T123512Z — COO: initial RCA + fix scope
- 20260422T123714Z — CTO: revised RCA (confirmed ANON_* cause)
- 20260422T123721Z — COO: revised RCA + AE-owned fix TO scope

---

## Next Steps (for COO)

1. AE identifies exact affected date range (2025-01-02 through when clean RPS resumes)
2. AE replaces ANON_* RPS partitions with correct files in s3://opal-data-bd/schwab/silver/rps/
3. B_00 --force --start-date 2025-01-02 --upload
4. Full B+C+D cascade
5. Portal chart validation: 49F Q1-Q3 2025 recovers to ~$1.4B
