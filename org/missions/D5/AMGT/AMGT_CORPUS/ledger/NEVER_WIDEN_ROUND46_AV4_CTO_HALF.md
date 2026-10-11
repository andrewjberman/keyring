# NEVER-WIDEN co-sign -- CTO half: AMGT_CORPUS round 46, `CRPS-av-4` leg p, the served effect of /12 (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~13:2xZ)

**Pair:** `deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND46_AV4_LEGP_SERVED_EFFECT.md` @148053efdb (COO half SIGNED, msg 3883). Blobs admitted:
`dossier.py` dc2ce428d015, `team_sheet.py` 6761f09d15f0, `scoped_amgt.py` 0662ef5b08de. The redeploy itself is AMGT_RESAPP's `ff-4`, under
its own pair, admitted by blob over the build's closure. This half signs the SERVED EFFECT of these modules.

**SIGNED** for branches A to C and the per-key rollback (the kept AMGT_RESAPP package; no store object written or deleted by leg p), on two
conditions.

## Read

- **Additive:** after p, `model.team_sheet` gains the five keys, and the six round-44 keys are unchanged. Branch C STOPs on ANY other served
  dossier field moving (except an input named at leg v), or on a name serving a field unequal to its stored /12.
- **The PROD page is not touched.** The API is shared, but portal PROD runs the old Model tab, which reads the six keys and ignores
  unknown ones. So PROD renders what it rendered until a `/prod-deploy`, which is Andrew's open call `e7f2` for the portal at large.
  DEV renders the new rows (portal `f00c7b8ee8`, CI 38142372462 success).
- **The text-cell condition is met:** `av2_check` arm b5, 5 of 5. An error cell renders as a why, never as a value.

## Conditions

1. **av-3's leg v reads Branch A on the WRITTEN /12 objects BEFORE ff-4's GO.** A Branch-B name (a failed write) keeps serving /11 by the
   pick rule and is listed. A Branch-C read stops the GO.
2. **The post-act read includes ONE name from each class** (`own_new`, `own_model`, `master_absent`) read through portal PROD's built page
   as well as DEV's, showing PROD unchanged in pixels, not only by reasoning. If PROD changes, that is a STOP and the AMGT_RESAPP
   rollback applies.

-- 1.0.0_SA_CTO~DELL1
