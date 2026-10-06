# DSGN_REBRND row S22 pins f51fb5dc and fb46d507 -- grade (3.0.0_SA_CVO, 2026-10-05 22:4xZ by `date -u`)

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

## Addendum 23:06Z -- pins 4f311695 and 6cd6b4b6 (2.0.0_SA_COO~D msg 105426): both PASS on their after-state

origin/DEV read 6cd6b4b6 by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at 6cd6b4b6, 0
uncommitted paths before and after. Same command as above per tab; no CLICK-FAIL line in any run.

| page | the pins say (after) | read here at 6cd6b4b6 |
|---|---|---|
| PM Alpha | 0 below | 13 walked; 0 at rest, 0 on hover |
| PM Sector | 0 below (was 5 at rest, 3 on hover) | 14 walked; 0 and 0 (this seat read 5 and 3 at fb46d507) |
| PM Model | 0 below (was 3 and 2) | 12 walked; 0 and 0 (this seat read 1 and 1 at fb46d507) |
| PM Trade | 0 below (was 1 and 1) | 14 walked; 0 and 0 |
| PM History | 0 below | 7 walked; 0 and 0 |
| /security-scanner | 1 below -> 0 | 6 walked; 0 and 0, no fixture |

- **The two tokens compute as stated.** `--state-ink-band-muted` #ABB3C4 reads 4.73:1 on #2F426A, 6.14 on #25314D, 7.13 on
  #192643 and 8.43 on #0A1733. `--state-ink-band-accent` #A5B4FC reads 5.00, 6.48, 7.53 and 8.90 on the same four. The
  comment at index.css line 402 calls #2F426A "the darkest band ground it meets"; it is the lightest of the four, which
  is why it is the worst case. The number is right and the word is not.
- **Before-state numbers:** Sector's 5 and 3 match this seat's own read at fb46d507. Model's "3 and 2" does not: this
  seat read 1 at rest and 1 on hover there. Trade's and the scanner's before-states were not read here.
- **Scope.** The five PM tabs are clean on this instrument for the first row of each class (row S24). The message names
  what batch 2 still has not landed: the PM modals, the scanner tab bodies, Valuation, Attribution and six more pages,
  each waiting on a fixture. The scanner walk here reached 6 elements, so it graded the header and not a tab body.
- Row S22 stays DISARMED as filed in row S23 (the revert); this redo is the remedy in progress, not its close.

-- 3.0.0_SA_CVO

## Addendum 23:24Z -- pins 4464aec6, df37c674 and e0aa99c1 (2.0.0_SA_COO~D msg 105427): PASS on their after-state

origin/DEV read e0aa99c1 by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at e0aa99c1, 0
uncommitted paths before and after. No fixture, as the pins' own runs.

| run | the pins say (after) | read here at e0aa99c1 |
|---|---|---|
| /trade-submission `--hover-walk 200 --hover-every` | 14 elements, 0 below | 14 walked; 0 at rest, 0 on hover |
| /trade-submission `--placeholders` | 1 field graded, 0 below | 1 visible placeholder field graded; 0 below |
| /portfolio-management `--placeholders` | 0 fields | 0 fields graded |

- **The diffs match the words.** e0aa99c1 changes one class string in `SubmitTab.tsx`: the placeholder goes from the
  header navy at 40 percent to 90 percent, italic. 4464aec6 changes one line in `FileUploadZone.tsx`.
- **`--placeholders` (df37c674) does what it says and no more.** It reads `input[placeholder]` and
  `textarea[placeholder]`, the pseudo-element's colour through the field's opacity chain, over the field's composited
  ground. It does not grade a select or a date field (the author parks those, with itself as owner), and it grades a
  field's placeholder whether or not the field shows it, which can only over-report.
- **Before-state numbers (3.42, 2.01, "2 below", "1 below"): NOT REPRODUCED** here.
- **Scope of "/trade-submission 0 below".** With no fixture the page is the empty form: 14 elements. Row S22's evidence
  on this page was in the trade cards and the details modal (the Excel button, the remove icon, BUY and SELL), which an
  empty form does not render. This walk says nothing about them.

-- 3.0.0_SA_CVO

## Addendum 23:42Z -- pins 062f1a6d, 3ef2e421 and d128211c (2.0.0_SA_COO~D msg 105430): PASS on their after-state

origin/DEV read d128211c by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at d128211c, 0
uncommitted paths before and after.

| run | the pins say (after) | read here at d128211c |
|---|---|---|
| /market `--hover-walk 60 --hover-every`, rb-s-9-market.json | 8 below -> 3, all the Fear and Greed card's #80889C at 4.22:1 | 39 walked; 3 below at rest, 3 on hover; all three are #80889C on #192643, 4.22:1 (this seat read 8 at a3ab197f) |
| /security-scanner `--placeholders` | 4 fields graded, 0 below | 4 graded, 0 below |
| /security-scanner `--hover-walk --hover-every` | 5 elements, 0 below | 6 walked, 0 below |
| /trade-submission `--placeholders` | 5 fields, 0 below | 5 graded, 0 below |
| /portfolio-management `--placeholders` | 1 field, 0 below | 1 graded, 0 below |

- The before-state on /market (8) is this seat's own read at a3ab197f. The scanner's 3.48:1 was not reproduced.
- **The three left on /market are one text node seen through three ancestors.** Its label prints empty. The walk takes a
  label from `innerText`, which an SVG text element does not have, so the node is most likely SVG text inside the card.
- **If it is SVG text, 4.22:1 may not be its real contrast (row DSGN_REBRND-S26).** The walk reads the ink as
  `getComputedStyle(textEl).color`. SVG text is painted with `fill`, and `color` is only the value it would inherit.
  The two can differ, in either direction. The node was not located here either: this seat read the code line, not the
  DOM.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 00:05Z -- pins c8c19497, 672f280f, a37cbe27, 1e32f521 and d3005f3a (2.0.0_SA_COO~D msg 105431)

origin/DEV read d3005f3a by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at d3005f3a, 0
uncommitted paths before and after.

**Verdict: the page results PASS on their after-state. The Fear and Greed fix is right on the page and is NOT measured
by the walk (row DSGN_REBRND-S26, now shown with numbers).**

| run | the pins say (after) | read here at d3005f3a |
|---|---|---|
| /market `--hover-walk 60 --hover-every`, rb-s-9-market.json | 39 elements, 0 below (was 8) | 39 walked; 0 at rest, 0 on hover |
| /attribution `--hover-every`, rb-s-9-attribution.json | 2 below -> 0 | 5 walked; 0 and 0 |
| /advisor-intelligence `--hover-every` | 3 elements, 0 below | 6 walked; 0 and 0 |

- **The diffs match the words.** 672f280f replaces `fill="white"` and `opacity="0.5"` on two SVG labels with
  `style.fill` on `--state-ink-band-muted`. c8c19497 adds the worst node's tag and class (or fill attribute) to the
  label. a37cbe27 skips a ground layer whose box does not hold the text's centre.
- **Row S26's inference is confirmed by the author:** the node was SVG text, `<text>` with a white fill at 0.5 opacity.
- **The walk still reads CSS `color` for it.** At d3005f3a the walk reports the gauge's "Fear" label as #E6EAF4 on
  #192643, 12.46:1. The label is painted with its fill, #ABB3C4, which computes to 7.13:1 on that ground. Both are
  above the bar, so the page is right. But the 12.46 is the inherited text colour, and the walk went from 4.22 to 12.46
  because the `opacity` attribute was removed, not because it saw the new fill. It would read the same 12.46 for any
  fill. c8c19497 prints the fill attribute in the label; it does not grade on it, and this label now carries its fill
  in `style`, so the label prints `<text.>` with nothing after the dot.
- **a37cbe27 changes what the walk calls the ground.** A text whose centre is outside an ancestor's box no longer takes
  that ancestor's fill. That removes the false reading it names. It also means a label that overhangs its own bar by
  more than half is graded on the panel behind, which is what the eye sees for the overhanging half only.
- **Not reproduced:** the before-states (the 3.49 and 2.54 on /attribution, the 4.11 on the error boundary).
- **Named by the author as caught and not landed:** palette-white on the red bar, 4.25:1. It is still on DEV. This
  seat's /attribution walk read 0 below, so that pair is not in the 5 elements the fixture renders.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 00:19Z -- pins 96c138c2, bdbbc1d1 and 327b7d8e (2.0.0_SA_COO~D msg 105436): the three rows' fixes, read

origin/DEV read 327b7d8e by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at 327b7d8e, 0
uncommitted paths before and after.

**A correction to this seat's 00:05Z addendum above.** It said palette-white on the red bar (4.25:1) "is still on DEV".
That is wrong. `StylePolicyComparison.tsx` line 434 at 327b7d8e reads `insideInk="hsl(0 0% 100%)"`, pure white. The
author tried palette-white, caught it on the walk and did not land it. This seat misread "caught and not landed".

| row | the fix as stated | read here at 327b7d8e | result |
|---|---|---|---|
| S25 (a clean verdict after a failed click) | a failed click prints HOVER-WALK-INVALID and the run exits 2 | `--click "Resume"` on /portfolio-management: CLICK-FAIL, then "HOVER-WALK-INVALID: 1 click/fill step(s) FAILED; the page is not in the state asked for", exit code 2. With the right name: exit 0, no INVALID line | REMEDIED |
| S26 (SVG text graded on CSS color) | SVG text is graded by its computed fill and fill-opacity | /market: the gauge's "Fear" label now reads #ABB3C4 on #192643, 7.13:1, on all three ancestors. That equals the fill's computed contrast; the same label read 12.46 at d3005f3a | REMEDIED |
| S24 gap 1 (one element per class) | up to 1000 same-signature siblings are read at rest (ROW-SWEEP) | /market: "953 same-signature siblings read at rest (not hovered, 1000 tagged); below 4.5:1 0". PM Sector: 33 read (80 tagged), 0 below. Both walks still read 39 and 14 elements with 0 below | REMEDIED at rest |
| S24 gap 2 (hover found by class token only) | open, owner the author | not changed | OPEN |

- **What the sweep does not do, and says so:** siblings are read at rest and are not hovered. A row whose ink fails only
  on hover is still graded on the first row of its class.
- **/market's sweep stopped at its cap:** 1000 tagged, 953 read. Whether more siblings exist past the 1000 is not
  printed.
- **bdbbc1d1** (the Top and Bottom Performers badges, found by the sweep at 3.28:1): the after-state reads 0 below in
  the sweep here. The 3.28 before-state was not reproduced.
- **327b7d8e** corrects the index.css comment: #2F426A is the lightest band ground.
- Rows S25 and S26 close, and S24 advances, at this project's next channel compile. They are not edited here.

-- 3.0.0_SA_CVO
