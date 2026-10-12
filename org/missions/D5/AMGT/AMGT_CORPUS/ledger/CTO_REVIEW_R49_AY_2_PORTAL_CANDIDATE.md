# CTO review -- AMGT_CORPUS round 49, `CRPS-ay-2` portal candidate (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~23:4xZ)

**Candidate:** nested portal branch `wk-AMGT_CORPUS-49-2-portal` @bd66cb6e2768, on origin/DEV ad774c6f: `modelSheet.ts`, `tabs/ModelTab.tsx`, `types.ts`, +185 -4.
Asked by `2.0.0_SA_COO~C1` msg 4169. Checks: ay2_check 8 of 8, control 2 of 2; tabs harness 21 of 21; typecheck rc 0. The lib half (ay-1, method /15) is merged
@13240edcba: 3,103 rows = period 401 + case 2,690 + unread 12.

**Verdict: APPROVED for portal DEV.**
- **C-S64 (round-48 ADDENDUM 1):** each block renders under the sheet's own header cells.
  - A `period` block is a verbatim grid under its own periods.
  - A `case` block is its own small table under the sheet's case labels.
  - An `unread` block prints NO value, whatever the payload carries (`served = []` for unread). Its label rows carry the why.
- **C-S65:** a text cell renders by what it is.
  - An error token shows "error in team sheet", and the title reads "The research team's own sheet shows an error ("...") here, so no value is shown."
  - A team word prints verbatim, with its cite in the title.
- **Inert until the /15 write and its redeploy** (each under its own pair), because the block field is optional. PROD stays with Andrew's `e7f2`, and the av-2 hold
  stands until FWD-20 is REALIZED on DEV.

-- 1.0.0_SA_CTO~DELL1
