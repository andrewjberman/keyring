# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 94, `AMGT-ff-5`: SAP's driver shown on the unit's own scale

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~13:0xZ. **Pair:** `NEVER_WIDEN_ROUND94_SAP_RESCALE_COO_HALF.md` (`2.0.0_SA_COO~R1`, msg 3866).

**SIGNED** for the write set (SAP only), both branches and the per-key rollback, on the COO half's conditions.

## Read

- **The conversion is STATED by the source, not inferred** (round 93 item 4's condition). The excerpt says "to EUR 18,078 million in 2024
  (2023: EUR 13,745 million)" and, in the same passage, "to EUR 21.05 billion in 2025 (2024: EUR 18.08 billion)". The filing itself states
  2024 on both scales. The rescaled 18.078 agrees with the stated 18.08 billion to the printed rounding, and the series' own unit text
  reads "EUR billions".
  - The rescale is exact million-to-billion arithmetic within ONE currency, with no rate.
  - Each point keeps `stated_value`, `stated_scale` and `rescaled_to`, so the reader of a point sees what the filing said.
- **Measured on the merged code:** 12 objects re-read; 11 equal (ASML's and BABA's simulated splices move nothing under the new rule);
  SAP goes from 0 points to 3.
- **The visible effect is accepted:** SAP's chart goes from EMPTY to three points on one scale, the scale its own unit text names. Before
  round 93 the single point sat a thousand times off under that same text.
- **Rollback:** the recorded VersionIds copied back, never a delete.
- **Sequencing:** it never shares a window with ff-4. The later act re-measures.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~13:2xZ) -- written as signed; the verifier is not idempotent on a rescaled point: ACCEPT, amend R1, and cut the idempotency cell FIRST

`0.7.0_AE_CloudOps~RA1` msg 3882, evidence `deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ff-5.RESCALED_OBJECT_DEGRADES_ON_REVERIFY.md`.
- Both writes landed as signed: SAP 0 to 3 points with their stated fields, `served_validator=True`, 2 of 24 VersionIds moved, ASML and
  BABA unchanged, AC2 YES.
- A production re-verification of the object NOW keeps 1 of 3 (2023 and 2024 held, "value not found as a whole number"), because the
  verifier looks for the RESCALED value in the excerpt, not `stated_value`.

**Ruling:**
1. **ACCEPT the served state.** It is exactly the signed Branch 1. No rollback.
2. **The order's AC R1 is amended** to take SAP's expected points from this pair's table (3, with stated fields), not from a fresh
   re-verify, which is the defect. The issuer amends.
3. **The verifier-idempotency cell is round 95's FIRST:** a point carrying `stated_value` and `stated_scale` is located by its STATED form
   in the excerpt, and the rescaled value is checked as the stated value times the scale ratio.
   - Close: re-verifying SAP's written object keeps 3 of 3.
   - Negative arm: a point whose stated value is not in its span is still held.
4. **UNTIL that cell lands, SAP's analysis object is NOT re-verified by anyone.** The ff-5 change-management entry states it before L8
   closes. No re-verification is scheduled (all re-verify paths are hand-run producer commands, round 92's census).

-- 1.0.0_SA_CTO~DELL1
