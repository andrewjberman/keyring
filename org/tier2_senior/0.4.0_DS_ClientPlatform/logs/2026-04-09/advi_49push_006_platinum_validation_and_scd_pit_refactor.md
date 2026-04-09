# ADVI_49PUSH.006 -- Platinum Validation + D_02/D_04 SCD PIT Refactor

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-09
**Project:** ADVI_49PUSH (Phase 1 platinum layer)
**Status:** All fixes committed on CLOUD. Awaiting AE re-upload + gold chain re-run for final validation.

---

## Summary

Started as a routine platinum-output validation task (TO ADVI_49PUSH.006). Quickly turned into an end-to-end investigation and refactor of the advisor book-building logic across `C_08`, `D_00`, `D_02`, and `D_04`. Final state: advisor books are now built from the SCD with point-in-time team membership, full-credit AUA for every tagged advisor, and a proper fee-earning / non-fee-earning decomposition with implied revenue.

The `$12M firm-vs-advisor gap` we were chasing was a red herring -- it was a stale-D_02 artifact from a silent crash. Digging into it surfaced three real issues that were all fixed this session.

---

## Commits shipped (CLOUD branch)

| SHA | Change |
|-----|---|
| `45943f6f` | docs: initial ADVI_49PUSH.006 validation report (5/6 pass) |
| `9f805593` | first attempt to fix firm vs advisor gap -- clients_tab whitelist filter (wrong, over-corrected) |
| `5437b1c2` | revert clients_tab filter; document structural gap theory (also wrong theory) |
| `862db05d` | D_00: read `account_performance` instead of `client_performance` -- align data source with D_02 |
| `a1ea51f5` | D_02: drop `nna` / `num_positions` from column list (C_03 schema didn't have them -- this was the real silent crash) |
| `52f13077` | D_04: revert fee_efficiency field transform (C_08 repo version was already correct) |
| `13a013e8` | D_02, D_04: delete stale advisor entity files between runs (prevent orphan book.json double-count) |
| `8ff74fdb` | D_02: build books for all 5 roles, not just architect -- initial multi-role version (too permissive) |
| `517adcf6` | D_02: PIT team membership via SCD + 08b current-period name overlay; drop meaningless `sum(advisor AUA)` check |
| `a3e620d4` | D_02, D_04: fee-earning decomposition per advisor (`tagged`, `fee_earning`, `non_fee_earning`, `implied_annual_revenue`, `avg_fee_bps_earned`) |

---

## Investigation flow

### Step 1 -- Initial validation (.006)

Ran the 6 requirements from the TO against `s3://opal-data-bd/platinum/`. Found:

- REQ 1-4, REQ 6: PASS (firm files, advisor spot-check, client spot-check, account spot-check, timeseries spot-check)
- **REQ 5 (number consistency): FAIL** -- `sum(advisor books) = $1,629.9M` vs `firm headline = $1,617.9M`, a $12M gap

Report committed at `45943f6f`, COO notified.

### Step 2 -- False start: ghost exclusion filter

First theory: ghost/insurance accounts were being counted in advisor books but excluded from the firm headline. Implemented a `clients_tab` whitelist filter in `D_04.build_advisor_summaries()` -- only keep clients that appear in `clients_tab`. Result: **$27.5M under** (over-corrected, by a lot). Reverted.

Why it over-corrected: the `unknown` advisor had 138 entries with `acct_*` format keys ($25.2M) that couldn't match any relationship-format key in `clients_tab`. Those weren't ghost accounts -- they were orphan accounts that D_02 had bucketed into a fake "unknown" advisor. Filtering them out dropped legit AUA.

### Step 3 -- Second theory: data source mismatch

Dug into D_00 vs D_02 input grain:

- **D_00** (`build_clients_tab`) reads `client_performance.parquet` (C_02), which is at relationship grain and built from C_00 that drops orphan accounts (no relationship_id).
- **D_02** (`build_advisor_books`) reads `account_performance.parquet` (C_03), which is at account grain and keeps all rows including orphans.

Patched D_00 to read `account_performance` and aggregate to relationship grain itself (commit `862db05d`). This aligned the data source.

AE re-ran -- **gap unchanged at $12M**. Theory wrong.

### Step 4 -- Real root cause: D_02 silent crash + stale output

Compared timestamps on S3:

```
gold/artifacts/clients_tab.json                  2026-04-08 21:27  <- fresh
gold/entities/advisors/kyle_sims/book.json       2026-04-09 09:03  <- fresh
gold/entities/advisors/49f_house/book.json       2026-04-07 11:48  <- STALE (2 days old)
```

D_02 hadn't rewritten `49f_house/book.json` in the latest run. But D_04 was reading it and propagating to platinum. Why didn't D_02 write it? Because D_02 was **crashing silently**:

- D_02's load requested columns `['nna', 'num_positions']` from `account_performance.parquet`
- C_03 does NOT produce those columns (the schema has `daily_inflow`, `daily_outflow`, `cum_inflows`, `cum_outflows`, no `nna`)
- Reading with an invalid column list raises `ArrowInvalid`
- D_02 exited mid-run, but the `49f_house/*.json` files from April 7 remained on S3
- D_04 discovered all existing advisor directories and built platinum summaries from each, including the stale ones
- The $12M gap was just AUA movement between April 7 and April 9 across the 4 stale advisor directories

**Fix:** commit `a1ea51f5` removed `nna`/`num_positions` from the load column list; compute `nna` inline as `cum_inflows - cum_outflows`; default `num_positions` to 0.

**Also fix:** commit `13a013e8` added stale-file cleanup in both D_02 (before writing `gold/entities/advisors/`) and D_04 (before writing `platinum/advisors/`). Any directory not in the current write set gets deleted.

### Step 5 -- DE finding: only architects had books

After fixing D_02's crash, DE (0.4.0_DE) found that the Books tab was broken for ~98 of 155 advisors in the leaderboard. Root cause: `D_02.build_advisor_books` iterated only `latest_snap['architect'].unique()`. Implementors, consultants, local_ops, and additional_advisors never got a `book.json` at all. Clicking any non-architect advisor in the portal silently fell back to N1.

**Fix:** commit `8ff74fdb` rewrote `build_advisor_books` to iterate unique advisors across all 5 role columns with an OR filter (`acct[role_mask]` where `role_mask` is OR across all 5 roles). Added `Unassigned` sentinel filter. Also rewrote `build_advisor_timeseries` with a multi-role melt + dedupe.

But this was still wrong, because...

### Step 6 -- Andrew's clarification on time-awareness

The commit `8ff74fdb` applied the `account_team` snapshot as a uniform override across all historical dates, which meant historical NNA/growth calculations credited the CURRENT team to events that happened when a different team was on the account. Andrew flagged:

> If Travis was listed as an architect on a 20m account ABC between Jan 2025 and Jan 2026, but in Feb 2026 Chase became Architect and travis is no longer on that account, then 20m should not be ascribed to travis post-Feb 2026.

**Fix:** commit `517adcf6` replaced the uniform override with a point-in-time (PIT) join against `advisor_assignments_history` (the SCD). For each `(account_id, date)` pair in `acct`, the join finds the SCD record where `effective_date <= date <= end_date` and uses that record's team. Historical dates now use the team active at that date.

Hybrid overlay: `account_team` (08b-resolved names) is applied as a **name-only** override to rows in the CURRENT SCD record. This preserves 08b resolution (e.g. mapping "Unassigned" → "Travis Penfield") for the current period but does not overwrite historical records.

Also dropped the `sum(advisor_aua)` vs firm check -- Andrew pointed out that summing advisor books is meaningless under the multi-role full-credit model, because the same account is credited to every tagged advisor by design.

### Step 7 -- Andrew's clarification on fee-earning vs non-fee-earning

With the PIT join in place, Travis's "tagged book" came out to $426.8M (514 accounts where he has any role). But his C_08 fee-weighted AUA was only $149M. Andrew asked for both numbers, per advisor, with a cleaner methodology than "equivalent solo-advisor AUA":

> in terms of taking the advisor split pct * account fee * account aua and getting fee-paying book-wide average bps charge

**Fix:** commit `a3e620d4` added the fee-earning decomposition per advisor:

- Extended `build_team_pit` to also return the 5 `*_split_pct` columns from the SCD
- Added `build_fee_bps_pit` -- parallel PIT join against `fee_rate_history` for per-date `fee_bps`
- `acct` rows now carry team, splits, and fee_bps all time-aware
- In `build_advisor_books`, for each advisor on the latest date:
  - `advisor_splits[account]` = sum of split_pct across all their roles on that account
  - `tagged_aua` = sum of full AUA for all tagged accounts
  - `fee_earning_aua` = sum where `advisor_splits > 0`
  - `non_fee_earning_aua` = sum where `advisor_splits == 0`
  - `implied_annual_revenue` = `sum(aua * fee_bps/10000 * splits/100)`
  - `avg_fee_bps_earned` = `revenue / fee_earning_aua * 10000`
- Both D_02 `book.json.summary` and D_04 `platinum/advisors/*/summary.json` `book` section carry the new fields

The SCD splits are authoritative for fee attribution (08b resolves names only, not splits).

---

## Travis Penfield validation table

Locally verified against current account_team + SCD + fee_rate_history:

| Metric | Value | Source |
|---|---|---|
| `tagged_aua` | $427,342,669 (514 accts) | full AUA, any role tag |
| `fee_earning_aua` | $342,613,278 (221 accts) | full AUA, any positive split |
| `non_fee_earning_aua` | $84,729,391 (293 accts) | full AUA, all splits = 0 |
| `implied_annual_revenue` | $1,136,099 / yr | sum(aua × bps × total_split) |
| `avg_fee_bps_earned` | 33.16 bps | effective book-wide rate |

Progression of how we computed Travis across this session (for reference):

- **$149M** -- C_08 split-weighted `managed_aua`
- **$319M** -- `account_performance.architect` BD-native (pre-08b)
- **$395M** -- `account_team.architect` 08b-resolved (architect-only, old D_02 behavior)
- **$426M** -- `account_team` any-role (514 accts, all 5 role columns)
- **$426.8M** -- SCD PIT + 08b current-record name overlay (509 accts, 5 excluded because no current SCD record)
- **$427.3M** -- account_team any-role on latest date (current fix, matches exactly)

The 5-account gap between SCD-PIT and account_team-only is accounts present in account_team but with no current SCD record -- these get dropped by the PIT join. Total impact ~$0.5M, not material. Left as a known edge case.

---

## Side issues surfaced and resolved

### 1. Stale C_08 deployment (deprecated field names)
Deployed `C_08.advisor_fee_efficiency.py` on the gold runner was 27,376 bytes from April 7 and emitted deprecated field names (`managed_aua`, `implied_revenue`, `fee_yield_bps`, `efficiency_ratio`). Repo version was 28,896 bytes with correct names (`aua`, `commission`, `fee_bps_weighted`, `efficiency_pctile`).

DE hit this first as "Books tab fee efficiency scatter all dots at 50th percentile" -- the scatter was reading `efficiency_pctile` which didn't exist in the deployed output, defaulting to 50 and rendering all dots yellow. Told AE to include C_08 in the next upload; told DE to keep the `as any` workarounds in place until the re-run lands, then revert.

Audited C_08's calculations line-by-line: `managed_aua = aua_current * split_pct/100`, `implied_daily_fee = aua * fee_bps/10000/252 * weight`, `efficiency_pctile = rank(commission/nna, pct=True) * 100`. All sound. The only issue was a stale deploy.

### 2. 401s on opalinvest.dev (separate thread from COO)
COO asked for help debugging 401s. Ran `comp-routes trace getPlatinumFirmDashboard`, `comp-platinum tab-audit`, and direct S3 inspection. Confirmed:
- Platinum S3 paths exist and route correctly
- `shared-advisor-router` Lambda@Edge correctly maps `/api/scoped/advisor-intelligence/platinum/*` to `/platinum/*` at line 124 of `index.mjs`
- Advisor/client `summary.json` intentionally returns 403 from the router; the routes go through `opal-partners-data` Lambda for pseudonymization (lines 1363-1370)
- Both Lambda artifacts were freshly deployed (2026-04-08 20:34-20:35)
- `comp-routes` parser has a cosmetic bug: shows S3 key as `gold/artifacts/platinum/...` for platinum paths when the actual Lambda code strips the prefix correctly. **Not a routing bug, a comp-tool display bug.** Flagged to COO.

Concluded the 401 was a real auth issue, not a data/path problem. Handed back to DT.

### 3. Meaningless `sum(advisor_aua)` check
Under the multi-role full-credit model, summing advisor books is garbage: the same account is credited to every tagged role-holder, so `sum(books) ≈ 3.3x firm`. Removed:
- `total_aua_sum` accumulator in `build_advisor_summaries`
- The return tuple `(written, total_aua_sum)` -- now just returns `written`
- `advisor_aua_sum` parameter in `_verify_consistency`
- The ratio check log output

The consistency check now just logs the firm headline from D_00 clients_tab and the advisor book count. There is no invariant to verify at the advisor-sum level.

---

## Files touched

**Gold scripts:**
- `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` -- read `account_performance`, aggregate to relationship grain inline (`862db05d`)
- `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` -- silent crash fix, stale cleanup, multi-role iteration, SCD PIT join, fee-earning decomposition (`a1ea51f5`, `13a013e8`, `8ff74fdb`, `517adcf6`, `a3e620d4`)
- `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` -- stale cleanup, consistency check cleanup, field passthrough for new metrics (`13a013e8`, `517adcf6`, `a3e620d4`)

**Briefs:**
- `docs/briefs/ADVI_49PUSH_P1_validation_report.md` -- initial .006 validation report (`45943f6f`)

---

## Pending

1. **AE (0.6.0) re-upload and re-run** -- `C_08`, `D_00`, `D_02`, `D_04` need to go to `s3://opal-data-bd/code/gold/` and the downstream chain (`D_00 D_01 D_02 D_03 D_04`) needs to re-run on the gold runner. I've sent AE the full context across multiple messages; latest READY ping at `20260409T143521Z`.
2. **Re-validate the 6 requirements** after the re-run
3. **Verify new book fields land correctly** in `platinum/advisors/*/summary.json` and confirm Travis's numbers match local calc ($427M / $343M / $85M / $1.14M / 33.2 bps)
4. **DE (0.4.0_DE) revert `as any` casts** in `FeeEfficiencyPanel.tsx` and `types.ts` once C_08's portal-contract field names are deployed
5. **Frontend design decision** -- Books tab should be updated to surface `tagged_aua`, `fee_earning_aua`, `non_fee_earning_aua`, `implied_annual_revenue`, `avg_fee_bps_earned` per advisor. Currently those fields exist in the platinum output but the portal hasn't been wired to read them. Task for DE/RD.

---

## Lessons learned / durable observations

- **Silent crashes that preserve stale files are the hardest to catch.** D_02 was crashing on a missing column, but because `gold/entities/advisors/` wasn't cleaned, D_04 happily read the stale files from 2 days prior. Added stale-file cleanup in both D_02 and D_04 as a durable fix.
- **`sum(advisor books)` is not a valid invariant under multi-role attribution.** Any consistency check that sums advisor-level totals and compares to firm totals will be wrong by design. The right invariants are per-advisor internal consistency.
- **SCD PIT is the only correct way to track historical team membership.** Using any snapshot (even account_team with 08b resolution) propagates current state backwards in time incorrectly.
- **08b resolution writes to `account_team` but NOT to the SCD.** When the SCD's current record has a raw BD value like "Unassigned" and account_team says "Travis Penfield", the hybrid model applies the override to the current SCD record only. Prior SCD records keep their raw values.
- **Fee splits are authoritative from the SCD; names are authoritative from account_team (for current period).** Never override splits with account_team values.
- **`comp-routes` has a parser bug** for platinum path resolution -- displays `gold/artifacts/platinum/...` when the actual Lambda code resolves to `/platinum/...`. Not a routing bug, but confusing if you trust the tool output. Flagged.
