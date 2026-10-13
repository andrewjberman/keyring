# CTO ROUND-93 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-92 L10 slug (2026-10-13 ~16:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 7080, `surprise-channel/remediations/REMEDIATION_v39.md` @063bf7a3df. Row
`IRPT_DASHBD-D2-W138-S1` (BLOCKING, INERT) asks for the endpoint card. **Prior:** round-92 analysis @a862a037f3. **No PRD addendum.**

## 1. What round 92 did

The rule (`RULE_EXCL.md` @d8a3f1fa58) was committed before the read.
- `BD_EXCLUDES_SERVED_INCOME` holds on 13 of the 23 days.
- 4 of the 7 windows re-close (accounts 2, 3, 4 and 7 of the round-90 list). 3 stay open, with 10 UNEXPLAINED days between them:
  - account 1: 6 days, up to -6.86pp;
  - account 5: 3 days, all under 0.07pp;
  - account 6: 1 day, -2.75pp.
- Negative arm: all 7 uncorrected windows miss.
- FWD-8 is met for 83 accounts and NOT REALIZED for 3.

## 2. Rulings

1. **`BD_EXCLUDES_SERVED_INCOME` is accepted as a stated reason.** Its test and its correction are one identity, as the COO says, so
   one held day proves nothing. What it measures is that, on 13 days, Black Diamond's day return differs from ours by exactly our
   income over the prior value, to within 0.01pp. That says what Black Diamond does: its day return leaves out income that ours counts
   on that day. That is a reason in FWD-8's sense, a stated cause of a disagreement, and it is the same class of statement as
   `BD_ACCRUED_INCOME`.
2. **Account 5 is decided by one number, not by its three days.** Its three UNEXPLAINED days are each under 0.07pp, which is a fifth of
   the window tolerance. Under 11b a window inside 0.35pp after its reasoned days are corrected meets the clause, and its remaining
   days are not graded one by one. The record does not print account 5's corrected-window figure. If it is inside 0.35pp, account 5 is
   met. If not, it joins the other two.
3. **The endpoint question goes to Andrew as one card**, because it changes how FWD-8's DONE WHEN reads: accept FWD-8 with accounts 1
   and 6 (and 5, if item 2 fails) named as known differences against Black Diamond that neither ledger explains, their served figures
   unchanged (round-92 ruling 2). This seat recommends yes. Open call: `dell2` list, kind fork.

## 3. ENRICHMENT LIST for round 93 (ONE issuance)

1. **Ledger leg L7**, carried (2026-10-14 11:41Z).
2. **Account 5's corrected window**: one figure, the window return after its 4 reasoned days are corrected, against 0.35pp. Read from
   the stored record. Nothing else is read.

Nothing more is cut until Andrew answers the card.

## 4. Acts only Andrew can do

The endpoint card (FWD-8 with named exceptions).

-- 1.0.0_SA_CTO~DELL2
