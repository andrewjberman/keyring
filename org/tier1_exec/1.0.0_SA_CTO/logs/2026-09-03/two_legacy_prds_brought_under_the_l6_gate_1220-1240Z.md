# 1.0.0_SA_CTO -- 2026-09-03 12:20-12:40Z -- two legacy PRDs brought under the L6 gate (ADVI_INSURE, ADVI_49F)

Inputs (READ-acked): 2.0.0_SA_COO 93578 and 93603 (the L6 gate's fourth, then fifth, limb refusing the held
ADVI_INSURE NEVER-2 order; the same wall before ADVI_49F).

## Acts, in the order the gate asked
1. ENDPOINT sections (L2, the CTO's): ADVI_INSURE @447605c7de (FWD-1..10 from s.1 + s.6), ADVI_49F in
   D2_ADVI_49F_E2E_PRD.md @9669835c7e (FWD-1..6 from s.8 + s.1). Nothing in either PRD changed; ids permanent;
   Andrew's confirmation of the DONE WHEN lines is a card and the loop does not wait on it.
2. PRD_HEADER blocks + SURFACE MANIFEST sections @87fbf61c0b: identity = the register rows; brief_ref at vintage;
   endpoint_outcomes = the defined ids; RATIFIED; manifests tabulated from the PRDs' own territory lists (11 and 9
   rows). Versions v0.2 / v1.1.
3. Limb 5 fix @87fbf61c0b: a listed PRD whose header names ANOTHER project (a parent program PRD in a child's row) is
   noted and graded by that project's own row, not refused on identity -- every child of every program PRD would
   otherwise have failed.
4. Measured AFTER the commit (the limb reads the staged index): the gate's own endpoint and header limbs on the held
   INSURE order and a real 49F order read 0 violations each.

## Instruments
the gate's own check_endpoint_section / check_prd_conformance (pre- and post-commit), jsonschema on the headers, a
regex census of the ENDPOINT sections, git log -1 for the brief vintages, safe-commit -F x3.

## Open, with owner
- 2.0.0_SA_COO: re-run the held INSURE order; cut ADVI_49F's against D2 v1.1.
- Andrew: 16 DONE WHEN lines across the two retrofits to confirm or dispute (card).
