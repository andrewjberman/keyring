# NEVER-WIDEN -- CTO half: `integrations/bloomberg/pipeline/etf_daily_pull.py` BACKFILL_CAP 50 -> 62 (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~23:4xZ)

**Signs:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_COO_SECHIST_A2_BACKFILL_CAP_62_20261015.md` @62b505c131,
sha256 `f04b805e597a8cf424cb2b1ba1e4cfb5c4748e92add671cfcd97f42b6650f372`. Authority: Andrew, "Positioning ETF pull can have slight increase"
(`ANDREW_DIRECT_20261015_233xZ_DA0C_POSITIONING_PULL_SLIGHT_INCREASE.md` @3353228c01). Read at HEAD: `etf_daily_pull.py:62` `BACKFILL_CAP = 50`.

**GIVEN.**
- Only that constant moves, 50 -> 62.
- No field, security, schedule, code path or shared budget file (`bbg_budget.json`) changes; the 9-30 hold stands for everything else.
- The first run on it reads the budget ledger.
- Rollback: the constant back to 50.

-- 1.0.0_SA_CTO~DELL1
