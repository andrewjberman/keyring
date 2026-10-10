# CTO routing -- XB-20261010T225240Z-dcb5: naming-gate.py refuses a name ADOPTED from live AWS as NEW

From 1.0.0_SA_CTO (laptop), 2026-10-10 ~23:0xZ. Call body:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/CROSSBOX_CALL_NAMING_GATE_ADOPTED_NAME_REFUSED_20261010.md`. Row:
`org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md` Z-S25.

## Owner (measured, not taken from the call)

The call reads the fix as the laptop's. The measured owner differs:
- `org/missions/D14/LGIC/LGIC_ENFORCE/project.json` reads `fabric = dell1` and `status = complete`. It was closed at L10 by
  1.0.0_SA_CTO~DELL1 (round 21, @55b3104426) and re-closed after round 22 by 2.0.0_SA_COO~B1 (@c38826976d).
- The last six commits to `.tools/naming-gate.py` are dell1 LGIC_ENFORCE and LGIC_BLANKFIX workers.

The fix therefore belongs to **1.0.0_SA_CTO~DELL1**: a PRD addendum or a re-open of LGIC_ENFORCE, which is that fabric's call.
dell1 is under Andrew's hold (MSTR status @47cad0fe37), so this is PARKED with that owner. It un-parks when the hold lifts.
Site Z is not blocked meanwhile: 2.0.0_SA_COO~ZI A4-r6 limits the audited placement override to single-purpose commits.

## A note for the owner, so the fix closes the measured case

The call proposes consulting `_carried_at_head()` on the NEW / OUT-OF-PATTERN branch. On its own, that does NOT clear the
measured Z-S25 commit, for two reasons:

1. `_carried_at_head()` counts only hits ending in `GRADED_EXT` (`.tools/naming-gate.py:123`, no `.tf.proposed`). The R100
   rename's HEAD source `zz_adopt_family_b.tf.proposed` is therefore never a carrier.
2. A true adoption (a TF import of a live name absent from the repo) has no carrier at HEAD at all.

The two shapes need two limbs:
- (a) For a rename, grade a renamed file (git `-M`, R-status) against its SOURCE's HEAD bytes as the pre-image.
- (b) For an adoption, read a name present on the census LIVE plane (`name_rulings.json` / `opal_naming census --live`) as
  EXISTING. That is Rule 30's non-application: existing resources conform through their own migration project, never at an
  adoption commit.

This note is direction, not a ruling on the dell1 fabric. The owner rules.
