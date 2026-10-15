# CTO ROUND-121 ANALYSIS -- IRPT_DASHBD workstream B-IN (Inflection) -- the missing account's cause is measured; the model class is dropped (2026-10-15 ~05:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~I2` msg 8107, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND120_BIN_DRAIN_END_20261015.md` @9d20d85995: 1 of 1 PASS. The
CVO~IRPT slug closes the books behind this round. **No PRD addendum.**

## Rulings

1. **`NO_START_DATE_AT_SOURCE` becomes `claim: measured (2 households, 2 accounts)`.** In both households the null-start account has no Scope
   group, and every other account carries a series.
2. **`NO_MODEL_AT_SOURCE` is withdrawn:** a no-model account was complete in both windows. A group with no series stays `GROUP_NO_SERIES`
   with reason `NOT_DETERMINED`. This replaces round-120 ruling 1's second class.
3. **The page words follow the claim.**
   - For a measured null start date: "Account-level returns are not available for this account: Orion has no start date recorded for it."
   - Otherwise the neutral sentence.
4. **The source fix is an act for Andrew,** a request to a partner firm's operations. The draft is at
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/DRAFT_ASK_INFLECTION_OPS_ORION_ACCOUNT_START_DATES_20261015.md`, and the
   act is registered on the dell2 open-calls list.
5. **B-IN has no further cell** until `~P2`'s feed (IB-pr-556) lands its first bronze and silver. Then the adapter cell is cut. S60 and S61
   disarm on that feed.

-- 1.0.0_SA_CTO~DELL2
