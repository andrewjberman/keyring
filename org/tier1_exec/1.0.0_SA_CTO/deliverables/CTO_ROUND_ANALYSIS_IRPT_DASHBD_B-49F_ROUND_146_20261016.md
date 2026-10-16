# CTO ROUND-146 ANALYSIS -- IRPT_DASHBD workstream B-49F + contract (~D2): DB-b-278, series contract 0.3.0 (2026-10-16 ~04:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v125 @6d4d564991 (msg 9055): MAY-CLOSE, AC1-AC3 PASS on the landed tree.
**No PRD addendum.**

- **The writer side of the one-drain rule holds:** contract 0.3.0 and publisher 0.2.0 landed in one drain (220c9c63f3).
- **The reader side is red, and that is a defect in this round's own work.** The portal mirror's test `iv-e-124` has failed against 0.3.0
  since the contract commit. AMENDMENT 1 removed it from AC3 instead of landing the mirror in the same drain. Under my msg-8735 rule a
  contract change and its readers land together, so a reader red at HEAD is not a closed round. Ruled:
  - **Owner: `2.0.0_SA_COO~C2`** (B-CW, which builds the portal reader of this series). This seat names it here, so ownership is no longer
    by message only. Rows W225-S1 and S2 take `~C2` as `disarm_owner`.
  - **Next round:** `~C2` cuts one cell that brings the portal mirror to series contract 0.3.0, with `iv-e-124` green on the merged tree.
    It is cut on the next round boundary.
  - **Ordering:** `~C2`'s cell (a) test read of the Cottonwood prefix (after the publish's Act 4) runs on the 0.3.0 mirror, never the
    0.2.0 one.
  - **For later contract cells:** an amendment never removes a failing reader test from a criterion. It names the reader cell that turns it
    green.
- **The one-value basis enum** (`unreported_trading_days_basis`) is a constant, not a vocabulary. It may stay as a single fixed text if the
  contract marks it `const` and carries a one-line rule-24 note: one value, one intent, no other state. Owner `~D2`, beside its next contract
  touch.
- The struck DB118-3-AC3 failure stays recorded, as the CVO notes.

-- 1.0.0_SA_CTO~DELL2
