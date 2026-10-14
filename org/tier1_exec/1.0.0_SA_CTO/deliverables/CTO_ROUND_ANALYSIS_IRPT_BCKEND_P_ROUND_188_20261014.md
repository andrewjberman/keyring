# CTO ROUND-188 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering round 187 (2026-10-14 ~01:4xZ; self-drive dell2 box)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** COO~P2 msg 7417, packet `deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_187_P_DRAIN_END_20261014.md`
@754b9f4570, and the mapping summary `deliverables/0.9.0_WK_IRPT_BCKEND~371/TRANSACTION_SOURCE_MAPPING_SUMMARY.md`. **No PRD addendum.**

## 1. What round 187 did

- IB-pr-523 built the Design B code change, offline.
- IB-pr-524 read the landed transaction sources:
  - Cottonwood can produce all 19 of 19 `account_activity_daily` columns;
  - Inflection can produce 17 of 19. `realized` and `inkind_departure_gain` are absent because no lot table has landed.

## 2. Ruling

**Inflection serves the default report with those two gain columns ABSENT, with their reason. It does not wait for a lot feed.**
- FWD-21's ACCEPT: "a figure Opal cannot produce says so in words, never blank".
- FWD-19: Andrew, "inflection is not a huge priority".
- A lot feed for Orion would be a new vendor leg. It is not asked here, and becomes a call only if a person asks for those two figures.

## 3. ENRICHMENT LIST for round 188 (ONE issuance; P2's list accepted, in order)

1. **The Design B census and packet** for the 49F function. The pair proves 0 returns partitions changed.
2. **The IR holdings class rule** (row D2-S156): the count of holdings that move per firm, then the build from ONE shared definition, then
   its pair.
3. **IB-pr-456** on Andrew's execution ID (row `f61b`).

**Queued next:** the Cottonwood and Inflection activity producers into the same shape. Cottonwood has all 19 columns; Inflection has 17,
with 2 ABSENT and named.

-- 1.0.0_SA_CTO~DELL2
