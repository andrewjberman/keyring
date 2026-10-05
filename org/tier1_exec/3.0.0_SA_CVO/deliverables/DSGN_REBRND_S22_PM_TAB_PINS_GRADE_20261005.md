# DSGN_REBRND row S22 pins f51fb5dc and fb46d507 -- grade (3.0.0_SA_CVO, 2026-10-05 22:5xZ by `date -u`)

Pins: portal DEV f51fb5dc (Model tab cell ink) and fb46d507 (Alpha and Sector row inks), 2.0.0_SA_COO~D msg 105425,
FAST, graded after the fact. origin/DEV read fb46d507 by fetch, and both commits are its ancestors.

**Verdict: both PASS on their after-state claims, read here on the served build. The before-state numbers were not
reproduced. Neither tab is clean yet, as each commit says.**

## What was run here

The vite server on port 5174 served the worktree `portal-coo-d-r43` at fb46d507, 0 uncommitted paths before and after.
`scripts/ui-smoke.mjs /portfolio-management --fixtures r4-2-portfolio-management.json --click "Resume (3d ago)"
--click <tab> --hover-walk 200 --hover-every`, once per tab. Both clicks printed CLICKED in each run.

| tab | the pins say (after) | read here at fb46d507 |
|---|---|---|
| Model | worst cell 4.66:1; one row stays at 4.3 on hover | 12 walked; the Size-factor row's worst cell 4.66:1 at rest and 4.30:1 on hover; one header 3.77:1 at rest |
| Alpha | 1 below -> 0 | 13 walked; 0 below at rest, 0 on hover |
| Sector | Materials row 4.40 at rest, 4.33 on hover; muted cells and the header rest ink still below | 14 walked; Materials 4.40 and 4.33; two muted-cell rows 3.42 and 3.62 at rest (3.42 on hover); two headers 3.77 at rest |

- **The diffs match the words.** f51fb5dc changes four cells in `ModelTab.tsx` from black to `--palette-white` on the
  green gradient. fb46d507 changes `AlphaTab.tsx` and `SectorTab.tsx` from `--success` / `--danger` to
  `--delta-positive-hover` / `--delta-negative-hover` (index.css lines 388-389 in the band world).
- **Before-state numbers (1.99, 1.65, Alpha 1 below, 4.20, 4.14): NOT REPRODUCED.** No build of the parent commits was
  made here; they are the author's.
- **What is still below the 4.5:1 bar at this build, on these three tabs:** the Model row on hover (4.30), the Sector
  Materials row at rest and on hover (4.40, 4.33; its worst text is an indigo figure, not a red one), two Sector rows of
  muted figures (3.42, 3.62), and the sortable column headers at rest (3.77). The commits name each of these as a later
  step. So row S22's redo is in progress on these tabs, not done.
- **Sampling (row S24).** The Sector table was graded on 3 rows, one per class signature. The other rows share those
  classes; their inks were not read.

## A trap in the walk (row DSGN_REBRND-S25)

This seat's first two attempts used `--click "Resume"` and `--clicktext "Resume"`. The button's name is
"Resume (3d ago)", so each printed CLICK-FAIL or CLICKTEXT-FAIL, then carried on, clicked the tab, and printed
`7 distinct clickable elements walked ... below 4.5:1 at rest 0, on hover 0` for all three tabs. That is the empty
page (no session loaded), and it reads as a clean pass. With the session open the same walk reads 12, 13 and 14
elements and up to 5 below. The name also changes with the clock ("3d ago" today).

## The author's finding, recorded

Msg 105425: batch 2's band rung lowered row hover contrast (4.14 to 3.19 and the like) because rows carry semantic ink
on a lighter rung, and batch 2 was not redone on rows. That agrees with row S22 as filed (the red negatives on hover)
and is the author's measurement; this seat did not re-measure it.

-- 3.0.0_SA_CVO
