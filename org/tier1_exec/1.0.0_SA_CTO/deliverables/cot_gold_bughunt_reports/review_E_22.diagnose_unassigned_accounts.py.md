# REVIEW -- E_22.diagnose_unassigned_accounts.py

- script: `data/cot/scripts/gold/E_22.diagnose_unassigned_accounts.py`
- verdict: **issues-found**
- runs_in_incremental: False
- findings: 2

## Finding 1 -- [low/empty-null-handling/both]
- **Location:** `data/cot/scripts/gold/E_22.diagnose_unassigned_accounts.py:96`
- **Mechanism:** total_aua = float(ap_latest['total_aua'].sum()); the very next line computes missing_aua/total_aua*100 with no zero-guard. Python float division by 0.0 raises ZeroDivisionError (unlike numpy). total_aua is 0.0 whenever the latest account_performance snapshot has rows but every total_aua is 0/NaN (skipna sum of all-NaN = 0.0).
- **Failure scenario:** A degraded/bootstrap nightly where B_00 priced all holdings to 0 (so C_03 total_aua/aua_current is all 0 on the latest snapshot) yet C_03 still emits latest-date rows, AND at least one funded account is absent from C_07's account_team (not_in_team non-empty) -> line 96 ZeroDivisionError -> the diagnostic aborts before printing any of the architect/history/house-split/inheritance sections. Note: E_22 is an ad-hoc diagnostic OUTSIDE the dispatch catalog, so this cannot abort the gold chain; impact is a failed manual run.
- **Proposed fix:** Guard the denominator: pct = (missing_aua/total_aua*100) if total_aua else 0.0, then print pct (mirror the guarding style already used for nna_day).

## Finding 2 -- [low/unguarded-read/both]
- **Location:** `data/cot/scripts/gold/E_22.diagnose_unassigned_accounts.py:41-43 (used at lines 63,66,69,74)`
- **Mechanism:** _read_s3() calls s3.get_object(Bucket, Key) with no try/except. A missing key raises botocore ClientError (NoSuchKey) and aborts. Lines 63/66/69/74 read ACCOUNTS_DIMENSION (A_00), ACCOUNT_TEAM (C_07), ADVISOR_ASSIGNMENTS (A_01), ACCOUNT_PERFORMANCE (C_03) unconditionally -- unlike the canonical_nna read at line 79-80 which IS guarded via _latest_partition returning None.
- **Failure scenario:** Operator runs E_22 ad-hoc against a fresh or partially-built bucket before C_07 (gold/views/account_team.parquet) or A_01 has ever produced output -> get_object raises NoSuchKey -> immediate crash with a raw traceback. Because E_22 is not in CHAIN_FULL/CATALOG and never runs in the incremental chain, this is an ad-hoc-run failure only, not a chain abort or served-number corruption.
- **Proposed fix:** Wrap _read_s3 (or each of the four load calls) in try/except ClientError, returning an empty DataFrame plus a printed WARN and skipping the dependent section -- consistent with the already-guarded nna_day path.
