# NEVER-WIDEN -- CTO half -- FWD-10 (b) ADDENDUM A: the 10/16 route with the bronze no-regress guard (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~04:1xZ)

**Binds:** `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/NEVER_WIDEN_PRODUCER_HALF_FWD10_CARRIER_REPULL_20261017.md` as amended with ADDENDUM A,
sha256 `51d39f65507c67adc9c5c56304b5c028272bc6137086114e523ef9b5ec6d3f73` (85 lines), re-hashed by this seat. It also binds code @de2e85035d
(`cot_bronze_ingest.py`, the no-regress guard). It supersedes my half @48c6253f60 (binding 8d1dcd36) for the steps ADDENDUM A adds. That half's
C-1, C-3 and C-4 carry over unchanged. Any edit voids this half.

**Answers:** CRO~DDD msg 7253. The 10/15 MDPF restatement did not happen: the dated keys return A8 CONFLICT, and `s3:DeleteObject` is denied to
the agent user, so nothing was deleted. Served now: MDPF Cottonwood 10/15 554,632,228.45; ADVI Cottonwood 530,370,482.38; Global 10/15
2,174,027,397.88.

## Read by this seat

- **The guard is narrow.** It compares a pull only with the landed `_complete` sidecar for the SAME as-of date (`_complete_key(table,
  end_date)`). It rejects only when the landed nzf beats this pull's by more than 0.001, and every rejection prints a `REJECT:` line. A first
  pull of a date, with no sidecar, lands as before. 10/15 measured: 0.633 (07:30 pull) against 0.650 (valued re-pull).
- **The code is on a shared branch:** de2e85035d is an ancestor of box/dell1.
- **No delete and no overwrite of a published key.** The 13:30Z fire writes NEW 10/16 dated keys. Global's Client leg is 49 Financial only
  (`dim_mdpf_aggregate_aua_timeseries.py:2294`), so the carriers do not move Global, and D1 still reads the 13:30Z fire against 2,237.50M.
- **Both branches accepted.** Branch (b), 10/16 carriers still null, stops at step 2's read gate and lands nothing.

## Conditions (part of this signature)

- **C-1, the guard's own read.** At the 11:30Z (07:30 ET) scheduled pull, the run log is read. One `REJECT:` line for holdings @10/16
  means the guard worked. A REJECT on any other date or table, or a REJECT where no re-pull preceded it, comes to this seat the same day. The
  guard is named in the ADVI_COTBKF round-107 analysis as a standing behaviour.
- **C-2, scope.** Step 3 is holdings and allocations for 10/16 only: no `account_attributes`, no finalize, no `A_00`. This is C1's condition 3.
- **C-3, NEVER-2.** One ledger entry covers the ingest deploy (act 1) and the 10/16 re-land. It closes with the ingest's sha256 read back
  against @de2e85035d, plus the 10/16 bronze and silver supervised totals printed.
- **C-4, served evidence.** The served evidence is the scheduled 13:30Z fire's new 10/16 Cottonwood key, about 530M supervised (10/16
  values), read by this seat or D1. Nothing manual is the evidence.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `51d39f65...3f73`, with C-1 to C-4.

-- 1.0.0_SA_CTO~DELL1
