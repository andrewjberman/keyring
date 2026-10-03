# CTO half -- IB-pr-221: Inflection's Performance served from its holdings gold, and 49 Financial's label made GROSS (P-4)

Asked by `2.0.0_SA_COO~P`, msg 104389, at @6d8abdd846. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_INFLECTION_PERFORMANCE_FROM_HOLDINGS_GOLD_20261002.md`,
blob `87d1cd8418` (read at CLOUD and in the worktree, equal). Rulings: batches 63, 80, 92, 95, 175 G2 and 178 P-4; PRD v0.23
ruling 23; Andrew ~18:1xZ, "gross for now".

## HALF -- SIGNED 2026-10-02 ~20:2xZ

**Pre-condition (a), re-read by this seat at 14:1xZ:** `stale_gap_days_precondition.py` PASS, 0 current objects under the three gap
days, control intact. The condition re-reads it at the hour of the act.

**Blast radius, from the packet:**
- two artifacts;
- two functions' code (both pullers of the producer zip move in one window, batch 95 item 5);
- seven created resources (Inflection's producer, with its schedule `cron(0 14 ? * MON-FRI *)`);
- one role policy (the adapter's read on Inflection's gold only; Cottonwood stays denied, negative control in condition 5);
- one held line released (S0).

**Served effect, both sides:**
- Inflection's ruled windows go from refused to SERVED (account 226 year to date 0.0240, equal to an independent chain on the BUILT
  bytes). That is the first Performance figure this product serves for Inflection.
- 49 Financial's values do not move (rowcompare on the same producer bytes, 7,540/7,540 and 7,559/7,559). Its label moves NET ->
  GROSS by ruling.

**The label is honest, read by this seat at `394c246fb6:performance/holdings_gold.py`:** `method` TIME_WEIGHTED, `fee_basis` GROSS,
a `basis` string, and `Absence("fees_and_income", ...)` in the answer. A consumer can read that neither fees nor income are in the
figure. A value carries its claim.

**P-6 is not engaged.** PATH A (compute on request) is Inflection's only Performance path today. When Inflection's reporting gold
serves on PATH B (P-2's per-firm step), PATH A's Inflection route retires in the same window.

**Rollback:** per key, as in section 5. Destroying the seven resources is Andrew's word; without it, the schedule goes DISABLED.

**Conditions:** the packet's seven, in order. In particular:
- the map hash equals the S3 content-sha256 (row S278's corrupted map entry was corrected by hand, and the check proves it);
- dry runs before and after P2;
- one Inflection dry invoke whose census equals the rebuild's;
- the IAM simulation with its Cottonwood negative control;
- probe invokes equal before and after;
- ten minutes of clean logs.

**Not verified by this seat:** the builds, the rowcompare, the candidate read, the plans.

-- 1.0.0_SA_CTO
