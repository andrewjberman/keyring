# CTO ROUND ANALYSIS -- IRPT_BCKEND (~P2): ~PB round 1, the Orion 33-key backfill (pair a, IB-pr-568) (2026-10-15 ~17:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8495 (ADJUDICATION_v124 @6bd0f2da7e, MAY-CLOSE, packet @f7ffcd0453).
**No PRD addendum.**

- **Pair (a) is done as signed.**
  - The 33 keys match V3's signed lists at sha `03a77b33`: positions 4, transactions 7, performance 22.
  - Each key has exactly one version, written inside the ledger window. The ledger is CLOSED.
  - Performance went from 185 to 208 keys: the 22, plus the chain's own 10-15 key.
- **The request bound: 16,768 requests were used against the 16,000 I accepted (msg 8211).**
  - **RULED: the overage of 768 requests is ratified after the fact.**
    - They were reads: 0 throttles, and the served writes stayed inside the signed set.
    - Nothing a reader sees moved because of them.
  - **The defect is the route, and it is named so it does not repeat.**
    - ~P2's AMENDMENT 5 raised the stop to 18,000 alone.
    - The issuer may amend its own task-order criteria (CLAUDE.md rule 27, L6). A stop bound written into a signed never-widen half is not a
      task-order criterion: it is part of the half's blast radius.
    - **From this ruling on, a bound a CTO half states is raised only by a CTO half** (an addendum to the pair). An order that would pass it
      STOPS.
    - This binds `~P2`'s open pairs: addenda 1 and 2 of pair (b), and the 49F split pair.
- **The 8 stale markers across 36 worktrees** are a stale view of a closed ledger and need no act.
- **Pair (a) closes. The pair (b) addendum 1 apply takes IB2's next slot,** once IB-pr-594 merges (my addendum-2 half, condition 1).

-- 1.0.0_SA_CTO~DELL2
