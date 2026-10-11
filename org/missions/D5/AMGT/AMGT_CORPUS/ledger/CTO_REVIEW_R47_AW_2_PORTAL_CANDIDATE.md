# CTO review -- AMGT_CORPUS round 47, `CRPS-aw-2` / `aw-11` portal candidate (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~17:0xZ)

**Candidate:** nested portal branch `wk-AMGT_CORPUS-47-2-portal`, ab55a2ea then 05a49a016d, on DEV cb76f857: `modelSheet.ts` +223,
`ModelTab.tsx` +27/-14, `types.ts` +4. Asked by `2.0.0_SA_COO~C1` msg 4023. The issuer re-ran on the merged bytes: aw2 5 of 5, control 2 of 2;
tabs harness rc 0; typecheck rc 0.

**Verdict: APPROVED for portal DEV.**
- **D1-S5 fix 1 (labels):** a code row prints its served label in words, with the code and the why or cite in the title. A FactSet row's cell
  says "FactSet, via team model". The census counts `held` / `measured` / `factset_line` / `bloomberg_line` / `raw`, and `raw` is the number
  FWD-20's close needs at 0.
- **D1-S5 fix 2 (formats):** `formatTeamValue` prints a team value by its own Excel number format:
  - placeholder decimals, the thousands comma, percent;
  - the negative section without an added minus, and the zero section;
  - quoted literals, with `[...]` tags and padding dropped.
  A `General` or absent format prints at most 4 decimals with trailing zeros stripped. The FULL stored value always rides the title, so
  nothing is lost; the display is the workbook's own.
- **Inert without /13:** `format` and the label fields are optional, so a payload captured before /13 renders as today. Landing on DEV before
  the lib half is served is therefore safe, and the issuer may land it now or with the write. PROD stays with Andrew's `e7f2`, and this change is
  what lifts the av-2 hold once FWD-20's DEV census reads `raw` 0.
- **Row D1-S7** (round 46's header test misclassed about 190 rows on CLX, ML FP and BABA; remedied in aw-1): noted. The round-47 census re-prints
  the class totals so the round-46 counts are corrected, not carried.

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 2 review (2026-10-11 ~19:4xZ) -- `de1d1c955f`, +10 -1, `modelSheet.ts`: APPROVED for DEV

On a master-class team sheet, a FIGURE row the Bloomberg-first precedence did not fill now says exactly "The research team keeps no workbook
for this company; this row is from the team's template." (`MASTER_TEAM_ROW_WHY`). Own-workbook names keep their sentence. This is the render
half of the aw-3 CTO half's point 1, built as worded. Checks: aw2 6 of 6, control 2 of 2, tabs harness rc 0, typecheck rc 0. It lands on DEV
on top of 9ca634c6ea. PROD stays with Andrew's `e7f2`.
