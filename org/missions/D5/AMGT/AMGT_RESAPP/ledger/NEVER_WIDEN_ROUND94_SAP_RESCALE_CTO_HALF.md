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
