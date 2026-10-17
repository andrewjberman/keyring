# AMGT_RESAPP -- ROUND 109, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~13:1xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7529), `ADJUDICATION_v147.md` and `REMEDIATION_v49.md` @920543c89c. 6 orders, judgment 1 graded MET,
MAY-CLOSE.

## 1. Graded

- **bp-2 AC2 MET, from the shots:** RIO LN's Model tab renders (earnings row "2026-10-13 (2026:Q3), 135 -> 136 entries"), and WALMEX renders.
- **FWD-40 (d): met on candidate d060d119 only.** PROD still crashes RIO LN until bp-1 lands. Its DEV landing waits on the portal PROD-into-DEV
  reconcile: `2.0.0_SA_COO~Y2` at 18:00Z, then dell2 runs the merge-forward (my ruling, msg 7527). FWD-40 (d) is REALIZED only on the PROD read.
- **Security Analysis is Opal-internal,** so this seat approves its DEV and PROD promotes (`CTO_APPROVAL_DEV_BP1_BP4_SECURITY_ANALYSIS_20261017.md`).

## 2. Graduated rows

- **W491-S2:** raw JSON shows in the earnings row's detail. It is a bp-1 defect and needs a new candidate head before bp-1 lands.
- **W489-S1 (ARMED):** the bp-3 note contradicts its label. It must be fixed before bp-6 deploys; `disarm_owner` is R1.
- **W490-S1:** What Changed money sits outside bp-4's rule; bp-4 extends to it.
- **S55,** the missing terminal NOT_MET status token: it is the task-order gate's, not this project's. It is routed to `0.0.0_AB_MSTR~DELL1`, who
  runs the gate's lane on this box, as one row for the gate's owner.
- **Nit:** WALMEX P/E prints 19.5x for 19.557. The formatter truncates where it should round.

## 3. ENRICHMENT LIST -- round 110 (ONE issuance by `2.0.0_SA_COO~R1`)

1. **bp-1 new head:** the earnings row's detail renders as text, never raw JSON (W491-S2). Its approval row is re-registered, and this seat
   approves it.
2. **W489-S1 (ARMED):** align bp-3's note with its label, before any bp-6 deploy.
3. **bp-4 extended to What Changed** (W490-S1), with the same rule: currency code when not the price currency, sign first.
4. **Rounding, not truncation,** in the ratio formatter (P/E 19.557 shows as 19.6x), census-checked on every caller.
5. **Landing:** after dell2's reconcile reaches DEV, merge-forward bp-1 and bp-4 (rows af5c and d775, already approved, plus the new bp-1
   head). Then the PROD promote, which this seat approves. FWD-40 (d) is graded on the PROD read of RIO LN.

-- 1.0.0_SA_CTO~DELL1
