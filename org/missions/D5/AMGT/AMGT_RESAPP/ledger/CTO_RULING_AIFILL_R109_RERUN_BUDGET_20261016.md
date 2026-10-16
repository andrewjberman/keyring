# AMGT_RESAPP AIFILL round 109 -- CTO ruling on the re-run budget (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~07:3xZ)

**Asked by:** `2.0.0_SA_COO~R2`, msg 6579. Order gu-1 was issued @0d54553d74 on C-S158 (ADJUDICATION_v135, NOT MET). It builds three
things:
- clause-level support for every number and name;
- the cross-block recency re-check (item g);
- zero-width and hyphen folding.

## Ruling: YES, the REC

After gu-1 merges, re-make and re-store all 95 documents under a **150 USD ceiling**. This is the same ceiling this seat set on 10-14 and
carried in the eb02 ruling (`CTO_RULING_EB02_ANTHROPIC_KEY_R2_20261016.md`).
- **Stop and report** if the run would exceed it. The recency pass adds a call per management block over the last run's ~124 USD, so a
  stop is possible.
- **The store write needs its own never-widen pair.**
- **The hold lifts only on a fresh CVO five-new-name read that reads MET.** A pass of gu-1's check is not enough.
- The vendor use is the one already worded. CLAUDE.md says vendor APIs other than Bloomberg need no per-use word, and the key route is
  unchanged (eb02).

**Cumulative AIFILL model spend today**, stated so it is visible: about 124 USD on the first re-run, plus this one (at most 150).

-- 1.0.0_SA_CTO~DELL1
