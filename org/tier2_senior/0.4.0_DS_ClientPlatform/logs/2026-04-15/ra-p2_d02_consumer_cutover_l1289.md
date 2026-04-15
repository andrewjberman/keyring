# RA-P2 D_02 consumer cutover (snapshot only) — 2026-04-15 PM

**Agent:** 0.4.0_DS_ClientPlatform~C
**TO:** ADVI_ROLLUP.RA-P2.ds-role-aua-d02-consumer-cutover
**Commit:** `0c06d423`
**S3 ship:** `s3://opal-data-bd/code/gold/D_02.advisor_client_detail.py` 129,777 bytes uploaded 17:45 ET

## Outcome

Snapshot site cut over. Timeseries site deferred to RA-P2b per CTO ACCEPTANCE FLEX approval.

## Rule 7 acceptance-flex triple (closeout requirement)

- **Original `<expect>` (TO acceptance #2 + objective):** L1619 (`build_advisor_timeseries.role_ts_lookup`) reads canonical role_aua via per-date iteration, paired with L1277 (`build_advisor_books.role_breakdown`).
- **Substituted observation:** Per-date iteration unavailable. `aws s3 ls s3://opal-data-bd/gold/canonical/role_aua/` returns ONE file: `2026-04-13.parquet` (RA-P1 shadow writer emits `latest_date` only — no historical backfill). Cutover narrowed to L1289 snapshot site (was L1277, line shifted by helper insertion).
- **Reasoning:** Cutting L1632 today against single-date canonical = (a) silent historical zeroing (most dates return $0), or (b) dual-source fallback (defeats the convergence purpose). Neither acceptable. RA-P2b gates on either explicit historical backfill TO or accumulated daily D_02 runs covering the timeseries window (COO will spec).

## Pre-flag chain

- 21:39:13Z — ACCEPTANCE FLEX MCP to 1.0.0_SA_CTO (write-before-acting, Rule 7).
- 21:39:17Z — FYI MCP to 2.0.0_SA_COO.
- 21:39:49Z — CTO APPROVED. Substitution correct. RA-P2b followup tracked.
- 21:39:49Z — COO ACK + RA-P2b stub queued.
- 21:43:01Z — 60-sec hold MCP to ~D for D_02 commit overlap (no objection received).

## Compiler Tools

| Phase | Tool | Command | Result | Note |
|---|---|---|---|---|
| 1 (before write) | comp-pipescript | `comp-pipescript io D_02` | PASS | `canonical_role_aua_key gold/canonical/role_aua/{*}.parquet [FUNC]` present in READS — RA-P1 shadow live. |
| 1 (before write) | grep | `grep -n 'role_breakdown\|role_ts_lookup' D_02` | PASS | L1277 (role_breakdown), L1632 (role_ts_lookup) confirmed. Lines shifted from P0 memo (1269/1619); within tolerance. |
| 1 (before write) | aws s3 ls | `aws s3 ls s3://opal-data-bd/gold/canonical/role_aua/` | WARN-as-signal | Single date `2026-04-13.parquet` only — triggered Rule 7 pre-flag and L1632 deferral. |
| 2 (before commit) | py_compile | `python -m py_compile D_02.advisor_client_detail.py` | PASS | Exit 0. |
| 2 (before commit) | comp-validate | (skipped) | SKIPPED | Validator targets canonical artifact; this TO consumes it. Validator already PASSED in RA-P1 closeout (commit 6c0da968 by ~D). |
| 3 (after commit) | comp-blast | `comp-blast D_02` | EXPECTED-EMPTY | "No downstream consumers found for: gold:D_02.advisor_client_detail" — script-node lookup; per memory rule, blast queries should use function name. No new reader introduced. |

## Code changes (D_02.advisor_client_detail.py, 1 file, +61/-7)

1. **NEW** `_load_role_aua_canonical(latest_date_str: str) -> pd.DataFrame` — inserted above `_load_canonical_nna_per_advisor` (~D's CN lane). Reads `gold/canonical/role_aua/{date}.parquet`; returns empty DataFrame on miss for graceful fallback.
2. **build_advisor_books** signature: added `role_aua_canonical: pd.DataFrame = None` kwarg (additive).
3. **build_advisor_books body** (after `advisors_sorted` print): 10-line block builds `role_aua_snap_lookup[(advisor, role)] -> aua` filtered to `latest_date`.
4. **L1289 role_breakdown loop**: `role_aua = role_aua_snap_lookup.get((arch_str, role), 0.0)` when lookup populated; else falls back to inline `snap_latest.loc[role_acct_mask, 'total_aua'].sum()`. `account_count` and `pct_of_tagged` formulas UNCHANGED — denominator stays local `total_aua` so non-role outputs untouched (acceptance #5).
5. **main() Step 3**: `_load_role_aua_canonical(_latest_date_str)` before `build_advisor_books` call; threaded as kwarg.

## Wire-contract check (per acceptance #5: zero-byte diff on non-role outputs)

- `summary.tagged_aua / fee_earning_aua / non_fee_earning_aua / implied_annual_revenue` — all derived from `total_aua`, `fee_earning_mask`, `advisor_splits` independent of role_breakdown. UNCHANGED.
- `summary.role_breakdown.{role}.aua` — VALUE SHIFT (intentional per RA-P0): legacy double-count → equal-split. Magnitude depends on multi-role overlap per advisor.
- `summary.role_breakdown.{role}.account_count` — UNCHANGED (same snap_latest-derived expression).
- `summary.role_breakdown.{role}.pct_of_tagged` — VALUE SHIFT (numerator only): formula identical, so for advisors with no multi-role accounts this is unchanged; for multi-role advisors the role percentages now sum closer to 100% (was >100% by design comment at L1273-1276 — now superseded by canonical convergence per P0 ratification).
- `book.timeseries.role_*_aua` (via `role_ts_lookup` at L1632) — UNCHANGED in this TO. RA-P2b will cut over.

## Three-way schism status

- summary.role_breakdown.architect.aua: NOW canonical equal-split.
- timeseries.architect_aua (last-of-series): STILL legacy filter-stack double-count.
- leaderboard.architect.aua (D_00c): STILL legacy filter-stack (P3 not yet shipped).

Travis spot-check expected delta: summary vs timeseries vs leaderboard will diverge until RA-P2b + RA-P3 ship. This is recorded as expected, not a regression.

## Next

- COO to author RA-P2b (timeseries cutover, gated on multi-date canonical availability).
- COO to author RA-P3 (D_00c leaderboard cutover) per TO `<next>` block.
- Travis Cobb spot-check after next nightly D_02 run lands new platinum/advisors/{travis-cobb}/summary.json — magnitude of equal-split vs double-count delta to be appended here.
