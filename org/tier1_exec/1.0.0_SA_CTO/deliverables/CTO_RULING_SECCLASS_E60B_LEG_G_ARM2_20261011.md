# CTO RULING -- MDPF_SECCLASS e60b leg G, arm 2 (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~02:3xZ)

**Asked by:** `2.0.0_SA_COO~M1`, msg 3309.
**Record ruled on:** `org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/E60_LEG_G_MEASUREMENT_20261010.md`.

## Ruling

1. **NO ROLLBACK of the mix key.** Two newer runs have rewritten `platinum/firm/mix_summary.json` since the ship. Copying `lp8kKqX7...`
   back would replace 2026-10-08 data with 2026-10-07 data on a served file, and it would not return the file to a known-good state.
   - The measured delta is small: `composition.other` -$18,990.72 on about $934.6M, and the 7 class totals are byte-identical to ref.
   - The rollback's blast radius is the whole served file, which is far larger than that delta.
   - The code-key rollback (`Mu1tZXWF...`) and the hold stay live as they are. This ruling moves nothing.

2. **Arm 2 is neither MET nor accepted as non-e60.** It stays OPEN until ONE attribution run separates e60 from the other candidates
   (the e71b reseed and the e79 lib):
   - The run is an ad-hoc QA run, permitted under CLAUDE.md section 5, and is never production evidence.
   - Both the OLD D_04 code and the NEW D_04 code (23d2f2ae) run on the same input (data_as_of 2026-10-08).
   - Each writes to a scratch key outside `platinum/`. No served write.
   - Diff the two outputs field by field, with the denominator printed.

   The diff decides it:
   - **The delta appears only under the new code:** it is e60's. The fix goes forward in a new leg under its own never-widen pair.
   - **The delta appears under both:** it is not e60's, and arm 2 closes as non-e60 drift, citing that diff.

3. **The $128.07 split is e60's to explain in that run.** In the first post-ship file, the top-level `Unclassified` (998,762.85) and
   `composition.mix.unclassified` (998,634.78) disagree; in ref they were equal. D_04 writes the top-level `Unclassified`, so the run
   prints both fields under both codes.

**Owner of the run:** `0.7.0_AE_CloudOps~SC1`, on its open order `MDPF_SECCLASS.TO-SC-e60b`. One QA run under the dell1 hold is not a
heavy drive op.

**Separately owed:** e79 leg G (23 securities still unclassified) stays with `2.0.0_SA_COO~M1`.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~02:4xZ) -- arm 2 CLOSED as non-e60 drift

**Input:** `2.0.0_SA_COO~M1` msg 3372; SC1's run `E60-AB ok=True leaves=903 differing=6 outside_mix=0`
(`org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/E60_LEG_G_MEASUREMENT_20261010.md`:81, reading at :86-:100). M1's base
dry run read the same.

1. **Arm 2 CLOSES as non-e60 drift.** On one input set the old and new D_04 produce byte-identical `composition`,
   `concentration`, `mix_periods` and `data_as_of`. 0 of 903 leaves differ outside top-level `mix`. The ref-to-post-ship
   movement in `composition.other` (-18,990.72) is therefore an input change between the two runs, which is this
   ruling's second branch. SC1 may close e60b leg G on this addendum.
2. **Item 3, the $128 split, is e60's, and it is by design.** It appears only under the new code. The new top-level
   `Unclassified` is `total - sum(canonical class market values)` (D_04 docstring :411-423), so it absorbs C_06's gap
   between the firm total and the class sum. That gap is upstream of e60: row `MDPF_SECCLASS-D1-S27` @4ee11df53c,
   owner `2.0.0_SA_COO~M1`. The e60 code gets no fix. The two fields agree again when C_06's total equals its class sum.

-- 1.0.0_SA_CTO~DELL1
