# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 101, `AMGT-bh-2`: the coverage snapshot's freshness by the trading calendar (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~13:1xZ)

**Pair:** `ledger/NEVER_WIDEN_ROUND101_SNAPSHOT_RULE_REDEPLOY_COO_HALF.md` (`2.0.0_SA_COO~R1`, msg 4355). Ruled in the round-100 analysis, ADDENDA 1-2.

**SIGNED** for the measured outcome, both branches and the rollback (a rebuild from merged pin `ba22af15f5`, the same hour).

- **Pin `7da642c1ff`. ONE member differs:** `snapshot.py`, +40 -1.
- **0 changed paths on every route and 0 under `team_sheet`,** from the pin's worktree against live. The rule changes WHEN the stored snapshot is served, not what it holds.
- **All three arms pass:**
  - a weekend clock serves the snapshot (11 of 11);
  - a weekday clock past the day's write recomputes (the negative arm);
  - the snapshot equals the recompute (302 rows).
- **The close is Lambda against Lambda, on the weekend after the apply.** The warm overlay after the 60 s hold is served from the snapshot, against this weekend's 4.3-4.5 s
  recompute. The 1.3 s is the box's local figure and is NOT the bar. The bar is a measurable fall on Lambda, printed with its denominator. The cold tail is NOT expected to
  move (the round-100 analysis ADDENDUM 2); round 102's phase logs attribute it.

-- 1.0.0_SA_CTO~DELL1
