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

## ADDENDUM 1 (2026-10-11 ~15:2xZ) -- the post-act read: Branch A, NOT a STOP. Row D1-S5: the av-2 surface is held from PROD until two fixes.

`2.0.0_SA_COO~C1` msg 3941, evidence `deliverables/2.0.0_SA_COO~C1/evidence/r46_av4_post_act_20261011.md` @21e3d2303f. Live `VNcX9ntm`:
`team_sheet` equals stored /12 on 95 of 95; four names 4 of 4 EQUAL; unmapped 0 (FIGURE 3,381 = Bloomberg 482 + team 2,899).

**Condition 2 is MET in intent; the pixel instrument was over-strict, and this seat wrote it.** The PROD-built page differs on 67 of 86 shots.
Every differing region is one of:
- the per-request clock line;
- a 1-px hairline;
- the lead panel's daily chatter (live data);
- ONE content change: SAN FP's name "Banco Santander S.A." to "Sanofi".

The name change is `AMGT-ff-4`'s signed, intended effect, carried by the same redeploy (its CTO half @c53a86ef41). The Model tab's rows area is
EQUAL on all three names, and that is the surface the condition protects. **Not a STOP; no rollback.** The lesson for the next such condition:
the instrument is a region diff with the known-moving lines masked and a content diff of text, not whole-page pixels.

## Row D1-S5 -- the DEV Model tab reads worse for the 32 own-workbook names. HOLD av-2 from any PROD promote; two fixes FIRST.

On DEV, 1,348 of 3,381 FIGURE rows (40%) are labelled by raw field codes (`BEST_EBIT`, `IS_ADJUSTED_OPERATING_INCOME`), and 72% of team float
cells print more than 4 decimals. The ruling was built as written. So the rule is incomplete, not the build, and both fixes are this seat's
to state:
1. **A row labelled by a Bloomberg field code is MARKET DATA, not team judgment.** It is the sheet's own data-feed block. Under round-45
   ADDENDUM 1 precedence it is Bloomberg's:
   - Where the served block carries the field, it shows the Bloomberg figure.
   - It is ALWAYS labelled by the field's human name from the vendor's own field dictionary (Bloomberg's field description), never by the
     code.
   - This is NOT the refused label map: it is the vendor's definition of its own mnemonic, one source, not a hand-kept second truth.
   - A code the dictionary cannot name renders "data-feed field <CODE>" with the why. Close: 0 raw codes as labels, with the denominator.
2. **Display follows the cell's OWN number format; storage stays verbatim.** "As the workbook saved it" means the value AND the format the analyst
   sees.
   - The write captures each value's Excel `number_format` (a method /13 field, its own pair).
   - The page renders by that format, and the title keeps the full stored value.
   - Close: 0 cells print beyond their format's decimals, and a percent-formatted cell renders as a percent.

**Until both land, av-2's Model-tab change does not reach PROD.** PROD promotion is Andrew's call `e7f2`. Because a DEV-to-PROD promote carries
everything on DEV, this hold is stated on that call, so his choice is informed: promote with av-2 reverted for the promote, or wait for the
fix. These are round 47's first two cells.

-- 1.0.0_SA_CTO~DELL1
