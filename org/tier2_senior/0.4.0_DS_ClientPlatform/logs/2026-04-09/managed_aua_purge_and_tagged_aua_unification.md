# managed_aua Purge + tagged_aua Naming Unification

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-04-09
**Status:** COMPLETE. All changes committed, uploaded to S3, gold run pending.

---

## What Happened

Andrew identified that `managed_aua` (split-weighted AUA, i.e. `aua_current * split_pct/100`)
was appearing in `period_start_aua` in the platinum leaderboard. This produced absurd numbers:
Travis Penfield's QTD `period_start_aua` was $147.78M (split-weighted) against a current
`total_aua` of $412.77M (tagged). The methodology mismatch made rank delta meaningless.

Andrew's explicit rule: the only valid advisor AUA number is `tagged_aua` -- all accounts
where the advisor is tagged in any role, full AUA, no weighting, no split fractions.
`managed_aua` was a Claude hallucination that was never agreed to and should never have existed.

---

## Canonical Term Definitions (explicit per Andrew)

| Term | Grain | Definition |
|------|-------|------------|
| `total_aua` | Account or relationship | Raw AUA of one account/relationship. Atomic fact from BD silver. Never used at advisor grain. |
| `tagged_aua` | Advisor | Sum of full account AUAs for all accounts where advisor appears in any of 5 roles, deduplicated at account level. THE advisor AUA number. |
| `fee_earning_aua` | Advisor | Subset of tagged_aua: accounts where advisor has split_pct > 0. For fee attribution analysis only. |
| `non_fee_earning_aua` | Advisor | tagged_aua - fee_earning_aua. |
| `nna` | Account/advisor/firm | inflows - outflows (transaction-classified). Never aua_residual. |
| `managed_aua` | DEAD | aua_current * split_pct/100. Removed. Never reintroduce. |

Full DDL written to: `docs/data/gold_runner_term_definitions.md`

---

## Commits This Work

| SHA | Change |
|-----|--------|
| `6391b96c` | D_04: period_start_aua uses D_02 timeseries tagged_aua; managed_aua removed from _LEADERBOARD_ROLE_FIELDS |
| `52a14fc7` | D_02: remove total_aua alias from book.json summary (tagged_aua only); D_04: read tagged_aua from book.json |

Prior session cleanup (already in CLOUD):
| `c6285ae8` | C_08: managed_aua removed from aggregation, total_aua used throughout internally |
| `d79ad9e7` | C_08: efficiency pctile ranking fix (separate but same session) |
| `c0d8f244` | Full purge across all gold scripts (Andrew directive): C_08 remaining refs, D_00 latest_aua/start_aua/aua_growth_pct/role_breakdown, D_02 _build_fee_summary_by_role, E_20 validation checks |

---

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` | Removed `total_aua` alias from book.json summary (52a14fc7). _build_fee_summary_by_role: managed_aua → total_aua (c0d8f244). |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | build_advisor_summaries: reads `tagged_aua` from book.json. build_leaderboard: reads `tagged_aua`. period_start_aua uses D_02 timeseries tagged_aua. _LEADERBOARD_ROLE_FIELDS: managed_aua removed (6391b96c, 52a14fc7). |
| `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` | latest_aua, start_aua, aua_growth_pct, role_detail, role_breakdown output: all managed_aua removed (c0d8f244). D_00 is fully clean. |
| `data/black_diamond/scripts/gold/C_08.advisor_fee_efficiency.py` | aua_current*weight computation removed. Aggregation: total_aua only. fee_bps_weighted denominator: total_aua. effective_split_pct removed (c6285ae8, c0d8f244). |
| `data/black_diamond/scripts/gold/E_20.cross_script_validation.py` | C_08 check: managed_aua → total_aua. Result key C_08.total_managed_aua → C_08.total_aua (c0d8f244). |
| `docs/data/gold_runner_term_definitions.md` | New DDL document. Authoritative definitions for all gold runner terms. |

---

## Blast Radius Audit (managed_aua)

Every location managed_aua appeared:

| Location | Status |
|----------|--------|
| C_08 aggregation (`detail['managed_aua'] = aua * weight`) | REMOVED in c6285ae8 |
| C_08 _build_window (`aua=('managed_aua', 'sum')`) | REMOVED in c6285ae8; now `aua=('total_aua', 'sum')` |
| D_00 leaderboard (`start_aua = groupby managed_aua`) | REMOVED in c0d8f244. D_00 is fully clean. |
| D_04 _LEADERBOARD_ROLE_FIELDS | REMOVED in 6391b96c |
| D_04 build_leaderboard read | FIXED in 52a14fc7 to read tagged_aua |
| D_04 build_advisor_summaries read | FIXED in 52a14fc7 to read tagged_aua |
| D_02 _build_fee_summary_by_role | FIXED in c0d8f244: managed_aua → total_aua |
| E_20 C_08.total_managed_aua validation check | FIXED in c0d8f244: → C_08.total_aua |
| Portal types.ts / AdvisorsTab / FeeEfficiencyPanel | REMOVED by DE~B (concurrent session) |

Remaining: none. All five gold scripts (C_08, D_00, D_02, D_04, E_20) confirmed clean
by grep on 2026-04-09. D_04 has three comment-only references ("# Replaces D_00's managed_aua")
that are explanatory annotations, not functional code.

*(Note: This log originally stated D_00 still had managed_aua in aua_growth_pct. This was
stale — c0d8f244, committed 9 minutes prior, had already cleaned D_00. Corrected on
2026-04-09 by 1.0.0_SA_CTO commit validation.)*

---

## C_08 Deduplication Note (discussed with Andrew)

C_08's `total_aua` per (advisor, role, date) sums `aua_current` per role.
If advisor holds 2 roles on same account, that account is counted twice.
This only affects `fee_efficiency.json aua` display -- not the leaderboard.

The leaderboard uses D_02's deduplicated tagged_aua (correct).
The fee efficiency panel's AUA is slightly overcounted for multi-role advisors.
Andrew accepted this for now -- fee efficiency panel AUA is "AUA across fee-bearing roles"
which is a valid framing for that specific context.

---

## S3 Uploads

| Script | S3 Key | Commit |
|--------|--------|--------|
| D_02.advisor_client_detail.py | code/gold/D_02.advisor_client_detail.py | 52a14fc7 |
| D_04.client_portal_summary.py | code/gold/D_04.client_portal_summary.py | 52a14fc7 (also 6391b96c) |

Gold run: pending marker written (instance was already running; will pick up on next cycle).

---

## Next Steps

1. **[DS post-run]** Verify platinum leaderboard period_start_aua for Travis:
   should be ~$408M+ (tagged AUA at April 1), not ~$148M.
2. ~~**[DS future]** Clean up D_00's internal advisor AUA computation~~ — DONE in c0d8f244.
3. **[All agents]** Reference `docs/data/gold_runner_term_definitions.md` before
   introducing any new AUA/NNA/fee field. No new field without a DDL entry.
