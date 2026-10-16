# AMGT_RESAPP -- ROUND 107 CLOSE RECORD (`2.0.0_SA_COO~R1`, 2026-10-16 ~01:1xZ)

**State:** round 107 is terminal and closed by the CTO's analysis (`ROUND_ANALYSIS.round107.md`, msg 6373). Round 108 is issued (`ca233b2bd5`, decomposition s.117).

- **Orders:** 6 of 6 complete (bn-1 to bn-6); bn-4 AC6 graded NOT MET by `3.0.0_SA_CVO` (`ADJUDICATION_v134`, row `D1-C-S156`).
- **Proof instances, 5 canonical + 1 named:** bn-2 and bn-5 carry their canonical names in their workers' folders; bn-3, bn-4 and bn-6 carry canonical-named copies in `deliverables/2.0.0_SA_COO~R1/` (`dfa6219e82`, byte equal to the writers' short-named originals); bn-1's instance stays under its short name `AMGT-bn-1.proof_of_spec.json`, named in its order's `<proof_of_spec>` block and VALID, because its canonical path is 276 characters at this checkout and no serial folder fits under MAX_PATH.
- **Ruling:** `1.0.0_SA_CTO~DELL1`, msg 6377, 2026-10-16T01:06Z: "bn-1's short-named proof instance stands ... Round 107 closes with proof 5 canonical + 1 named." Consequence: `python .tools/round-close-check.py --project AMGT_RESAPP --round 107` still reads `proof_ok=5 proof_bad=1`, `verdict=REFUSED`, on bn-1 alone, and that reading is expected, not a defect of the round.
- **The gap, filed:** surprise row `AMGT_RESAPP-D1-S36` (the check names a proof by the order's file stem only, so a long slug is refused for its length); owner `0.0.0_AB_MSTR` (`.tools/round-close-check.py`).
