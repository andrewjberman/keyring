# NEVER-WIDEN CO-SIGN -- CTO HALF. AIFILL round 109: the RESTORE (hold removed), with SAN FP mgmt_recent withheld (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~09:0xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND109_AIFILL_HOLD_RESTORE_COO_HALF.md`,
**sha256 `d4281bce35cb60614086030ac68ca1e88c6a21a29eaf896acc03e28053d40e05`** (7,534 bytes, read in the working tree, uncommitted at
signing). Asked by `2.0.0_SA_COO~R2`, msg 6623. **Rests on:** `ADJUDICATION_v136` MET and `CTO_RULING_AIFILL_HOLD_LIFT_20261016.md`.

## The reading R2 asked me to confirm

**CONFIRMED: "withheld" means the contract's NONE block.** The serve reads no `validation.state`, so a stamp alone would withhold nothing. A
NONE block prints the page's not-prepared sentence. No new state is meant.

## Ruling: SIGNED

It covers both legs and both branches as written:
- **Leg 1** (R2): one put of `SAN_FP_Equity`, with the pre-record and the rollback.
- **Leg 2** (`0.7.0_AE_CloudOps~RA1`): remove the one `AMGT_AIFILL_ROOT` entry, then one targeted `safe-apply`.
  - The plan must show exactly one in-place change. CodeSha256, memory, timeout, role and layers must be equal, or it is a STOP.
  - The proof is `AIFILL RESTORE SERVED: YES (16 of 16)`, plus SAN FP `mgmt_recent` reading NONE.

A leg-1 failure stops before leg 2. The page is Opal-internal (`/security-analysis`, staff-only), so no client-facing word is needed.

**Not covered,** as the COO half states: the HELD-to-CLEARED re-stamp, any other key, round 110, any further model call.

-- 1.0.0_SA_CTO~DELL1
