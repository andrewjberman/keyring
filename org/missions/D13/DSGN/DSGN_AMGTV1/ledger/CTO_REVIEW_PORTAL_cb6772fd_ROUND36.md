# DSGN_AMGTV1 round 36 -- CTO product-file review of portal `cb6772fd` (1.0.0_SA_CTO~Z, 2026-10-04 ~23:5xZ) -- APPROVED for DEV

**Ask:** `2.0.0_SA_COO~D` msg 29313 (it reached this seat as OFFER-EXHAUSTED and was read late, ~23:4xZ). The close is
`deliverables/2.0.0_SA_COO~D/round36/ROUND36_CLOSE.md` @99e9b46b5a.

## What I read

- **Surface:** 6 files against DEV, +295/-1394.
  - 3 product files: `ChatterBubbles.tsx` +168, `TimelinePanel.tsx` +6, `model/WhatChangedPanel.tsx` +5.
  - The rest is the instrument (`scripts/ui-contract-check.mjs`, `ui-measure.mjs`) and the fixture swap to the windowed chatter
    shape. The swap accounts for most of the -1394.
  - It does not touch `ModelTab.tsx` or `modelSheet.ts`, the CORPUS second-writer file.
- **DEV moved:** origin/DEV `3173c186` is 2 commits past the candidate's base. They touch AdvisorIntelligence, InvestorReporting
  and a PageEnd test (0 SecurityAnalysis files), and the trial merge (`git merge-tree`) is CLEAN.
- **The issuer's evidence:**
  - battery29 ALL PASS; repairs36 5/5; the round 34-35 checks are full.
  - The FWD-20 render instrument reads **76 PASS / 0 FAIL** on the candidate against 6 band FAILs pre-redesign, and its plants
    behave.
  - Close walk 21/1/1: round 35's tooltip FAIL now PASSes 3 of 3. BA's "-100.0%" is a real move to zero, as before. The ERROR is
    the known control gap.

## Verdict

**APPROVED for the DEV push.** Re-merge onto the current origin/DEV and re-run battery29 on the merge. The push takes Andrew's word
(CLAUDE.md Portal); `0.0.0_AB_MSTR~Z` pushes.

## Rulings on the close's section 4

1. **Round-35 condition 3 (PROD waits for RESAPP aq-5) is MET in substance.** aq-5's code leg landed at 21:41Z. The function now
   runs CORPUS al-5's build `2rFeF57l` (22:42Z), which carries round 67. AMD's served cloud no longer lists "amd". The aq-5 order
   still reads `pending` because its entry carries the aq-6 leg; that is bookkeeping, not a served gap. A PROD promote is still a
   separate act on Andrew's word.
2. **Round 37 cuts NO new page cells.**
   - The census items stay uncut: `RankedChart.tsx`'s 10px ticks (not mounted on the list state, so no served effect) and
     PanelContent's `rounded-b-lg` (the estate's shared component, outside DSGN's surface).
   - What remains is GRADING on the served build after the DEV push: the 7 outcomes round 34 reopened, plus rounds 35-36's
     outcomes.
   - DSGN FWD-1 remains Andrew's signed-in read.
