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

---

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` | Removed `total_aua` alias from book.json summary. Only `tagged_aua` written at advisor grain. |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | build_advisor_summaries: reads `tagged_aua` from book.json. build_leaderboard: reads `tagged_aua` from book.json. period_start_aua now uses D_02 timeseries tagged_aua at window start date (not D_00 managed_aua). _LEADERBOARD_ROLE_FIELDS: managed_aua removed. |
| `docs/data/gold_runner_term_definitions.md` | New DDL document. Authoritative definitions for all gold runner terms. |

---

## Blast Radius Audit (managed_aua)

Every location managed_aua appeared:

| Location | Status |
|----------|--------|
| C_08 aggregation (`detail['managed_aua'] = aua * weight`) | REMOVED in c6285ae8 |
| C_08 _build_window (`aua=('managed_aua', 'sum')`) | REMOVED in c6285ae8; now `aua=('total_aua', 'sum')` |
| D_00 leaderboard (`start_aua = groupby managed_aua`) | Still in D_00 internally BUT D_04 overrides period_start_aua using D_02 timeseries (clean source) |
| D_04 _LEADERBOARD_ROLE_FIELDS | REMOVED in 6391b96c |
| D_04 build_leaderboard read | FIXED in 52a14fc7 to read tagged_aua |
| D_04 build_advisor_summaries read | FIXED in 52a14fc7 to read tagged_aua |
| Portal types.ts / AdvisorsTab / FeeEfficiencyPanel | REMOVED by DE~B (concurrent session) |

Remaining: D_00's internal leaderboard builder still uses managed_aua for its own
`aua_growth_pct` computation. This is tolerable because D_04 overrides the advisor AUA
fields before they reach platinum. D_00's internal `aua_growth_pct` is a derived metric
that will have minor inaccuracy for multi-role advisors -- flagged for a future D_00 cleanup
to use account_performance directly for advisor AUA at all dates.

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
2. **[DS future]** Clean up D_00's internal advisor AUA computation to use
   account_performance directly (remove dependence on C_08 fee_detail for AUA).
3. **[All agents]** Reference `docs/data/gold_runner_term_definitions.md` before
   introducing any new AUA/NNA/fee field. No new field without a DDL entry.
