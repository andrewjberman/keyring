# DSGN_AMGTV1 round 34 -- CTO product-file review of portal 055ba370 (AV-zl-1 repairs), `1.0.0_SA_CTO~Z`, 2026-10-04 ~02:4xZ

**Ask:** `2.0.0_SA_COO~D` msg 29122. Branch `dsgn-r34-onto-dev` (worktree `C:/tmp/wk-dsgn-amgtv1-92/portal`), nested portal repo.
Close record: `round34/ROUND34_CLOSE.md` @a408efb24a.

## What I read

- **Base:** `055ba370` descends from origin/DEV `a403f466` (`merge-base --is-ancestor`, read ~02:3xZ). Against DEV it moves
  6 files, all under `src/pages/SecurityAnalysis`, +180/-70. The merge adds 0 SecurityAnalysis lines beyond ~93's `934d86d940`.
- **ChatterBubbles.tsx (FWD-21):**
  - every outside stage now refuses a slot over another bubble;
  - a third, far ring is joined to its bubble by a leader line, and leaders are tested against labels both ways (Liang-Barsky);
  - the free-slot search tries the full name before the shortened text;
  - a label sits in a `<g>` whose `<title>` carries the full served name, and only an inside label is pointer-events none.
  - **New branch:** a label with no clear slot is dropped (`null`), and its bubble keeps its hover.
- **SecurityOverlay.tsx (FWD-27 window):** the breakout move prints only with the served row's own `window_days` ("over the last
  30 days"). With no served window it prints no number. `window_days` is a required field of the served row type.
- **TimelinePanel.tsx (FWD-27 ink):** the axis text moves from `#A8B0C0` (2.18:1 on white) to the navy token. This removes one of the
  two hex literals FWD-23's note named.
- **WhatChangedPanel.tsx (FWD-27 precision):** `atRowPrecision` re-expresses the served change at the finer of the before/after
  cells' printed resolution, in the after cell's suffix. The unit scale is inferred from the ratio of the printed value to the
  served one, so a percent printed from a ratio scales correctly. A cell that prints no number keeps its text. I traced it by hand on
  a B/M suffix mix (980M -> 1.25B prints 0.270B), and it holds.
- **cscTable.ts / PeersTab.tsx (FWD-27 names):** the subject row prints the overlay `display_name` when it is non-empty, else the
  peers name.

## Measured by this seat

- **ESLint** on the 6 files at `055ba370`: rc=0, 0 errors (7 warnings, all `react-refresh/only-export-components`).
  **Positive control:** a planted `{}` type piped as WhatChangedPanel.tsx gives rc=1.
- **tsc --noEmit** on the worktree: rc=0.
- **Label drops on the fixtures:** labels34 prints 55 / 64 / 70 labels at 30 / 90 / 365, and its header says the fixtures carry
  55 / 64 / 70 names. So 0 labels are dropped there.

## Outcomes this candidate reopens (it rewrites their faces)

FWD-12 (timeline tick ink), FWD-18 and FWD-21 (the collage), FWD-23 (TimelinePanel's literals), FWD-25 (What changed's Change column),
FWD-26 (the header's period) and FWD-27. They are re-graded on the served build after the push. The close walk of 055ba370
(19/0/1) is candidate evidence until those bytes are served.

## Conditions

1. **A dropped label is invisible to labels34.** It counts labels and never compares them to bubbles, so "0 collisions" would also
   pass a collage that dropped every hard label. The served walk prints bubbles minus labels per window. A non-zero count is a FWD-21
   row and is never a pass.
2. **The DEV push** of a product-file candidate is `0.0.0_AB_MSTR~Z`'s on Andrew's word (CLAUDE.md Portal). Card 1's word named
   f9c6fa73 and its fix only, so this one needs the card COO~D placed at MSTR~Z. PROD stays gated.

## Verdict

**APPROVED** for the DEV push under conditions 1 and 2.
