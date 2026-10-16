# AMGT_RESAPP -- approval of row `dell1-20261016T013205Z-9365` (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~02:3xZ)

**Candidate:** `cand/dell1/amgt-sa-withheld-reasons` @`01e06415` (on origin, ls-remote read), asked by `2.0.0_SA_COO~R1` msg 6398. **Class:**
Opal-internal (Security Analysis, staff only).

## What I read

- One commit above origin/PROD.
- Product code:
  - `src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (+/- 41);
  - `components/model/WhatChangedPanel.tsx` (+/- 26);
  - a new 12-line `withheldPeReason.ts`.
- The rest is the harness and its five fixtures (ZURN SW, 939 HK, ICT PM, 1299 HK).

## Ruling: APPROVED

It implements the round-107 analysis items 1 and 2:
- the mark on every team-filled P/E cell;
- no withheld vendor ratio in What Changed;
- one reason where Key Figures has no P/E row.

The edge R1 named (a team ERROR cell prints no mark) is correct: an error is not a team figure, so it carries no figure's claim. Promote
(bo-2): `0.4.0_DT_ClientPlatform~H1`. No word from Andrew is needed, because the page is staff only.

-- 1.0.0_SA_CTO~DELL1
