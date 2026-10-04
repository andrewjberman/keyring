# DSGN_AMGTV1 round 35 -- CTO product-file review of portal `d60a0f90` (1.0.0_SA_CTO~Z, 2026-10-04 ~21:4xZ)

**Ask:** `2.0.0_SA_COO~D` msg 29252; close `deliverables/2.0.0_SA_COO~D/round35/ROUND35_CLOSE.md` @9e5820652c.
**Candidate:** portal `d60a0f90` on `dsgn-r35-onto-dev` (worktree `C:/tmp/wk-dsgn-amgtv1-92/portal`). It is DEV `2c792c27` (which
carries 055ba370) plus AV-zm-1/2/3.

## What I read

- **Surface:** `git diff origin/DEV...d60a0f90` touches 12 files, all under `src/pages/SecurityAnalysis/`, +200/-31. Nothing outside.
- **`TimelineWordCloud.tsx` (new, 108 lines):** presentation only.
  - It draws the served terms in served order, never re-sorted.
  - Size maps linearly from the served counts, and a larger count is never smaller.
  - It uses ONE data hue (`PALETTE.blue600`) with no sentiment colour. Text is 11px and up, and there is no light or ghost text.
  - It has three designed states (`terms` / `empty` with the served reason verbatim / `absent`) and no clock or randomness.
  - It fits the portal colour law and C-PRESENTATION-ONLY.
- **The wording diffs** replace "not carried on this payload" with "not in this security's data" (FWD-27, no system word on the
  face). `TimelinePanel.tsx` adds 4 lines: the optional `word_cloud` type and the mount.
- **The issuer's evidence:** battery29 ALL PASS (tsc 0, eslint 0), changed35 5/5, payload35 4/4 and cloud35 5/5, with the round-34
  checks still 4/4. The close walk read 20 PASS / 2 FAIL / 1 ERROR. I accept both FAIL grades as the issuer read them:
  - BA's "-100.0%" is a real move to zero (0.005 -> 0.0), not an equal print, so the probe over-matched;
  - the tooltip's fallback headline is pre-existing and outside these cells, and it goes to round 36.
- **DEV has moved:** origin/DEV is `aa373a83`, 2 commits past the candidate's base. Those commits touch Attribution, CMA,
  FactorTilts, Macroeconomics and a PageEnd test, which is 0 files under `src/pages/SecurityAnalysis/`.
- **Upstream dependency:** AMD's served cloud still carries "amd" (18). The own-ticker exclusion is RESAPP aq-1, which is drained
  but not deployed (aq-5 is pending with AE~A). The page only shows what the route serves.

## Verdict

**APPROVED for the DEV push**, under these conditions:
1. Merge onto the current origin/DEV in a scratch worktree, then re-run battery29 and the round-35 checks on the merge before the
   push (DEV moved twice today during this project's pushes).
2. The push takes Andrew's word (CLAUDE.md Portal: product file); `0.0.0_AB_MSTR~Z` pushes.
3. **PROD:** the word cloud is promoted only after RESAPP aq-5 is deployed, so PROD never shows a company's own ticker in its own
   cloud (FWD-39). DEV may show it meanwhile.
4. The round-36 list in the close's section 4 stands as the issuer named it, plus the FWD-5 tooltip.
