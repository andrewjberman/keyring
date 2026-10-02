# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 1, CTO half (the grade-2 fix redeploy + the 2026-10-01 rebuild)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~08:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM1.md` @e44181f7f1 (msg 28304). **Extends** the pair
@4df699fa92 / @dd7d03eaed. Every gate, key and condition there stands.

## What I read

- **The cause:** CVO~RV grade 2 FAIL @9cca47a6cd. F1 (P0): ETFT's YTD -188.51% comes from zero-valuation days (quantity held,
  `market_value` 0) read as -100% returns.
- **The plan is 0/5/0:** code hashes only, no policy change. The package differs from the deployed 7aa0186d45 in six files:
  `gold_holding_contribution.py`, `gold_buying_trend.py`, `render.py`, `ai_accounts.py` (prompt only, no Lambda call),
  `sweep.py` (`refresh_a1` passes through), and `guardrails_config.json`, which adds `contribution_implausible_move_band` 0.5,
  PROVISIONAL.
- **The served delta, measured** over the same served inputs: 102 of 3,939 `holding_contribution` rows change, in 10 funds.
  - ETFT YTD moves -188.51% -> +0.56%.
  - **SCHY moves -1.83% -> +5.85%; BIDD +11.49% -> +12.51%; CGIC and PFOE move by under 0.1 pt.** All of these come from the NEW
    implausible-move band (valuations on unchanged quantity refused).
  - The F2 money-market line leaves the rankings.
- **The blast radius B1-B4:** the five Lambdas in place; ONE new object per A1 table for 2026-10-01, never overwritten; ONE
  republish of the 2026-10-01 page with its prior revision kept; the 2026-10-02 chain on the fixed code. The writers are counted.
  Both branches (before 10:45Z / after the sweep) are covered with the same keys.

## The one thing this half adds

**The zero-valuation fix is the F1 remedy and needs no ruling:** a held line with `market_value` 0 has no price, so it cannot
read as a -100% day. **The implausible-move band (0.5) is a NEW product rule.** It refuses observed valuations, and it moves
SCHY's served YTD by 7.7 points. No ETFS_RIVALS ruling names it yet: the rulings file @528f030bdb holds calls 1-5, and none of
them is this band. ETFS_RIVALS calls are `4.0.0_SA_CRO~RV`'s (Andrew ~04:57Z). This seat sent the call there with its REC
(accept 0.5 PROVISIONAL, with every refused day disclosed on the page's audit block).

## Conditions

1. **CRO~RV's ruling on `contribution_implausible_move_band` is in hand before the apply.**
   - If it accepts the band as built, the act proceeds as the COO half reads.
   - If it changes the band, the served delta is re-measured at the new value before the apply.
   - If it rejects the band, the package drops it, and only the zero-valuation fix ships: re-measure, then apply.
2. The A1 pair's act-start gates (plan exactly 0/5/0, live base = B1's CodeSha256, the NEVER-2 entry
   `etfs-rivalfunds-fast-a1-r2`, nothing in flight) hold at the act.
3. **The post-act read compares the moved fields:** ETFT, SCHY and BIDD YTD beside their pre-act values; the money-market
   lines absent from the rankings and the trend; the sector panels. HTTP status is never the grade.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD fc80f776e4, blast radius B1-B4, both branches, on condition 1.
