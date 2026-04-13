# 0.4.0_DS_ClientPlatform -- ADVI_PROFAU.001 Session Log

**Date:** 2026-04-13 (EDT)
**TO:** ADVI_PROFAU.001 -- DS profile/book data-gap audit
**Status:** complete

## Objective

Produce a structured audit response covering 7 backend data gaps surfaced from the advisor-profile/book number-tie audit. Apply EXISTS-UPSTREAM first framing: can we work with existing tables? Labels: EXISTS-UPSTREAM / COLUMN-ADD / NEW-ARTIFACT / DEPRECATED.

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 | comp-pipescript | `comp-pipescript io D_00c` | D_00c reads 8 tables, writes EMPLOYEE_LEADERBOARD only |
| 1 | comp-pipescript | `comp-pipescript io D_04` | 20 reads (incl. client_detail_key, advisor_book_key, EMPLOYEE_LEADERBOARD); 21 platinum terminal writes |
| 1 | comp-trace | `comp-trace employee_leaderboard --direction both --all` | D_00c -> employee_leaderboard.json -> D_04 -> leaderboard.json (terminal) |
| 1 | comp-transform | `comp-transform schema-check AdvisorBookView` | 19/3/13-unused on PlatinumAdvisorSummary; 13/5/6-unused on PlatinumClientSummary; 6/3/1-unused on PlatinumAccountSummary. All rendered fields match types. |
| 1 | comp-transform | `comp-transform schema-check AdvisorPublicProfile` | 13/1/12-unused on AdvisorDrilldownSummary. SCHEMA MISMATCH: timeseriesResp at L1166/L1164 not declared on type. |
| 2 | Grep | `capital_gains_ttm|cost_basis_by_year|top_gain_positions` in gold/ | LIVE in D_02 (per-client) and D_00 (per-client). D_04 line 1959 capital_gains_ttm is in CLIENT summary builder (~1920), NOT advisor summary builder (491-521). Absent from advisor-level platinum output. |
| 2 | Grep | `is_fee_paying` in gold/ | D_00c lines 647-829 (leaderboard path only). Zero matches in D_02. Not on AdvisorClient type. |
| 2 | Grep | `fee_summary` in gold/ | D_02 line 778 `_build_fee_summary_by_role` for L2; D_02 line 811 `_build_fee_summary_by_account` for L3. D_04 line 516: emitted in advisor summary. D_04 line 687: emitted in client summary. LIVE. |
| 2 | Grep | `total_market_value` in gold/ | C_05 line 242: computed. D_04 line 888: emitted in `platinum/accounts/{*}/summary.json`. LIVE. |
| 2 | Grep | `fee_earning_aua` in D_02 | Line 960: `fee_earning_mask = total_split_pct > 0` — no is_billable gate. Confirmed divergence from D_00c W6-005 canonical (`billable AND split_pct > 0`). |
| 2 | Read | D_04 lines 491-521 (advisor summary builder) | Emits book.{fee_earning_aua, non_fee_earning_aua, tagged_aua, fee_earning_account_count, non_fee_earning_account_count, implied_annual_revenue, avg_fee_bps_earned} + top-level role_breakdown. MISSING from PlatinumAdvisorSummary type. |
| 2 | Read | api/endpoints/advisor-intelligence.ts 711-734 | `getPlatinumAdvisorDrilldownSummary` reads platinum/advisors/{id}/summary.json, flattens book.* fields. fee_earning_aua sourced from D_02 (stale filter). |

## Output Produced

`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/profau_gap_audit_response.md`

## Gap Labels Summary

| Q | Label | Evidence |
|---|---|---|
| Q1 — L2 capital gains / cost basis | COLUMN-ADD | D_02 per-client data in detail.json; D_04 advisor builder (491-521) does not aggregate |
| Q2 — per-client is_fee_paying flag | COLUMN-ADD | A_02 loaded by D_02; not joined to client list; AdvisorClient has no fee flag |
| Q3 — fee_earning_aua reconciliation | COLUMN-ADD | D_02 line 960: total_split_pct>0 (no billability gate) vs D_00c billable AND split_pct>0 |
| Q4 — PlatinumClientSummary.fee_summary | EXISTS-UPSTREAM | D_04 line 687 LIVE, type declared, no frontend consumer at L3 |
| Q5 — PlatinumAccountSummary.total_market_value | EXISTS-UPSTREAM | D_04 line 888 LIVE, type declared, no frontend consumer at L4 |
| Q6 — PlatinumAdvisorSummary type drift | EXISTS-UPSTREAM | D_04 emits full shape; type.book missing 7 fee/tagged fields + role_breakdown |
| Q7 — fee_earning_aua canonical pick | COLUMN-ADD | sum(role.fee_paying.aua) from leaderboard is canonical (W6-005 verified); D_02 filter fix aligns |

## No NEW-ARTIFACT labels — all 7 gaps addressable from existing Group A-D tables.

## Files Modified

| File | Change |
|---|---|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/profau_gap_audit_response.md` | Created — Q1-Q7 audit response |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_PROFAU.001.ds-profile-book-data-gap-audit.md` | Status: pending -> complete |
| `org/compiler-tools-log.md` | Appended ADVI_PROFAU.001 session entry |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-13/profau_001_data_gap_audit.md` | This log |

## Next Steps

- **[0.4.0_DE_ClientPlatform]** Response doc at `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/profau_gap_audit_response.md`. Q4, Q5, Q6 are pure DE work (type fix + render one-liners). Q2 + Q1 will be unblocked after DS ADVI_PROFAU.002 + .003. Recommend opening .004 (type fix) and .005 (frontend renders) in parallel with DS .002.
- **[0.4.0_DS_ClientPlatform]** ADVI_PROFAU.002: D_02 line 960 `fee_earning_mask` filter fix (add `is_billable` gate). Covers Q2 partial + Q3 + Q7. One-liner + incremental D_02+D_04 run.
- **[0.4.0_DS_ClientPlatform]** ADVI_PROFAU.003: D_04 advisor summary book-level tax aggregation. Covers Q1.
