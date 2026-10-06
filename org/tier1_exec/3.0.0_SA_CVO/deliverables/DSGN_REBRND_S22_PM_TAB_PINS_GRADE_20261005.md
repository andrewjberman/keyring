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

## Addendum 2026-10-06 00:30Z -- pins 7786e20e and 803850c0 (2.0.0_SA_COO~D msg 105440)

origin/DEV read 803850c0 by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at 803850c0, 0
uncommitted paths before and after. Both runs exited 0.

**Verdict: 803850c0 PASS on its after-state. 7786e20e: the code reads the stylesheet as stated; its detection was not
exercised on a real page by anyone, so row S24 gap 2 reads BUILT, not shown.**

| run | the pins say (after) | read here at 803850c0 |
|---|---|---|
| /market `--hover-walk 60 --hover-every` | HOVER-DETECT 148 selectors; 39 elements, 0 below | "148 :hover rule selectors read"; 0 elements matched by the stylesheet alone; sweep 953 read, 0 below; 39 walked, 0 and 0 |
| /attribution `--hover-every`, rb-s-9-attribution.json | 5 elements 0 below; ROW-SWEEP 18 siblings 0 below (before: 15) | 148 selectors, 0 by the stylesheet alone; sweep 18 read (65 tagged), 0 below; 5 walked, 0 and 0 |

- **803850c0.** The sweep's before-state on /attribution (15 below) was not reproduced; at d3005f3a this seat had only the
  first-row walk, which read 0 on 5 elements. That 0 is what row S24 said a first-row read is worth: the sweep found 15
  rows behind it. The author's note on its own d3005f3a error (a lighter navy that read 3.26 on blue) is the author's
  measurement.
- **7786e20e, the code.** With the flag, every rule whose selector holds `:hover` gives a base selector with `:hover`
  stripped, nested rules are resolved against their parent, and a non-pointer element matching a base is picked. The
  count of elements picked only that way is printed.
- **7786e20e, the evidence.** On both real pages that count is 0, and the author says the same of all five pages it
  walked. A zero here cannot tell a working reader from a dead one. The author's proof is a synthetic-page control; it
  is not in the commit and was not run here. So the reader is built and reasoned, and no real element has yet been
  picked by it. A page that carries a variant-prefixed hover token (4 source files hold one) would show it.
- **One thing to watch in that reader.** index.css line 756 holds a universal rule, `*:hover`. Stripping `:hover` from it
  leaves `*`, which matches every element, or an empty string, which the matcher rejects, depending on how the browser
  prints the selector. Today the walk reads 39 elements and 0 by the stylesheet, so it is not matching everything. If a
  build ever prints it as `*`, every sized element with text becomes a walk candidate and the cap (60 on /market) cuts
  the walk short with no line saying so.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 00:35Z -- pin 03b57119 (2.0.0_SA_COO~D msg 105442): PASS on its after-state

origin/DEV read 03b57119 by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at 03b57119, 0
uncommitted paths before and after. `/trade-submission --click "Add 5 Rows" --hover-walk 200 --hover-every
--placeholders`, no fixture; CLICKED printed, exit 0.

| read | the pin says (after) | read here at 03b57119 |
|---|---|---|
| `--placeholders` | 40 fields graded, 0 below (25 below before) | 40 graded, 0 below |
| `--hover-every` | 15 elements, 0 below | 15 walked; 0 at rest, 0 on hover |
| ROW-SWEEP | 8 siblings, 0 below | 8 read (55 tagged), 0 below |

- The diff is 7 lines in two files, each taking the placeholder from the header navy at 40 percent to 90 percent italic,
  the same change as e0aa99c1.
- The before-state (25 below at 2.01:1) was not reproduced.
- This is the row state this seat's 23:24Z addendum said the empty form did not render, for the input fields. The trade
  cards and the details modal of row S22's evidence (the Excel button, BUY and SELL) need submitted trades and are
  still not rendered by any walk here.
- The author names what no step grades: icons with no text, such as the red remove icon, which answer to the 3:1
  non-text bar. Row S22 listed that icon (3.16 to 2.53 on hover). It has no instrument yet.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 00:54Z -- pins ea22eda3, 78957643 and be119a16 (2.0.0_SA_COO~D msg 105448): PASS on their after-state

origin/DEV read be119a16 by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at be119a16. It had
0 uncommitted paths before the runs and 1 after, so the last run below (/market) may have been served a file in mid-edit;
the two Trade runs came first. Every click printed CLICKED and every run exited 0.

| run | the pins say (after) | read here at be119a16 |
|---|---|---|
| PM Trade (Resume, Trade) `--hover-every` | 16 elements 0 below; ROW-SWEEP 91 siblings 0 below | 16 walked, 0 and 0; sweep 91 read (145 tagged), 0 below; 4 fields graded, 0 below |
| PM Trade + Submit modal `--placeholders` | 8 fields graded, 0 below | 8 graded, 0 below; 4 walked 0 and 0; sweep 6 read (151 tagged), 0 below |
| /market regression | 953 siblings, 0 below | 953 read, 0 below; 39 walked, 0 and 0 |

- **Before-states (the sweep's 23 then 19 below on the Trade grid; 3.79, 3.42 and 4.41): NOT REPRODUCED.**
- **The modal run shows the visibility rule working in one direction:** with the Submit modal open the walk reads 4
  elements and the sweep 6, where the page behind reads 16 and 91. The page under the backdrop is not graded.
- **ea22eda3 turns an over-report into a possible under-report, and prints no count of what it skips.** A text node is
  graded only when the element at its centre point is the text, a descendant or an ancestor; otherwise the read returns
  nothing and the node drops out of the element's count. Two consequences, from the seven added lines:
  1. A visible text under a transparent layer that takes pointer events (a click catcher, a drag overlay) is skipped,
     and no line says a node was skipped. The sweep prints read-of-tagged (91 of 145), which is a denominator for
     siblings; the walk prints none for the text nodes inside a walked element.
  2. "An ancestor" passes. A clipped row whose centre point lands on a shared ancestor (the panel, the page column) is
     still graded, so "clipped rows are no longer graded" holds only when something else is painted there.
- **Unreached, as the author says:** the Bulk Edit, Remove, Lookup and Upload modals.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 01:20Z -- pins 00a2fc6f, 95763378, b733b8c2, 1cb21619, f990d119 and 97c9c3c6 (2.0.0_SA_COO~D msg 105452)

origin/DEV read 97c9c3c6 by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at 97c9c3c6. The
worktree had 0 uncommitted paths before the runs and 1 from part-way through: `scripts/ui-smoke.mjs` itself, +10 -1, which
adds two flags (`--accept-dialogs`, `--clickrole`) this seat did not use and touches no grading line. The page source was
at the pin throughout. Every run: `--hover-walk 200 --hover-every --text-all --placeholders`, exit 0, every click CLICKED.

**Verdict: PASS on the after-state for the PM tabs, /attribution and /market. One page reads 1 below here where the pin
says 0: /advisor-intelligence.**

| page and state | the pins say (after) | read here at 97c9c3c6 |
|---|---|---|
| PM Alpha (Resume) | 317 siblings, 0 below (was 56) | 317 read (368 tagged), 0 below; 13 walked 0 and 0 |
| PM Model | 262, 0 below (was 63) | 262 read (313 tagged), 0 below; 12 walked 0 and 0 |
| PM Sector | 366, 0 below (was 56) | 366 read (417 tagged), 0 below; 14 walked 0 and 0 |
| PM Trade | 389, 0 below (was 56) | 357 read (553 tagged), 0 below; 16 walked 0 and 0 |
| /attribution, rb-s-9-attribution.json | 220 siblings 0 below; 5 elements 0 below | 220 read (271 tagged), 0 below; 5 walked 0 and 0 |
| /market, rb-s-9-market.json | 1159, 0 below | 1159 read (1211 tagged), 0 below; 39 walked 0 and 0 |
| /trade-submission, Add 5 Rows | 0 below on the static sweep | 49 read (100 tagged), 0 below; 40 fields 0 below |
| /security-scanner | 0 below | 17 read (68 tagged), 0 below |
| /ticket-center | 0 below | 17 read (68 tagged), 0 below |
| /advisor-intelligence | 0 below | 31 read (82 tagged), **1 below**: a line beginning "Data refreshed daily. Last u", class `text-xs text-white/40`, #757D8E on #192643, 3.62:1 |
| /positioning | 195 siblings 0 below | 24 read (75 tagged), 0 below: no fixture here, so not the author's state |

- **/advisor-intelligence.** The author's earlier walk of this page reached the error boundary (3 elements); this seat's
  renders a page (5 walked, 31 siblings). The states differ, and the one reading below is on the page this seat reached.
  It is a muted white/40 line of the same class the other pins moved to `--state-ink-band-muted`.
- **PM Trade reads 357 siblings here against the author's 389.** Both are 0 below. The grid is virtualised, so the count
  depends on what was scrolled into the DOM.
- **Before-states (56 to 63 per tab, 11 and 14 on /attribution, 7 in the detail modal, 16 false on /positioning): NOT
  REPRODUCED.** The security detail modal (b733b8c2) and /positioning's treemap state (1cb21619) were not reached here.
- **Read-of-tagged is now printed on every sweep,** and it shows what the visible-text rule skips: 51 on nine of the
  eleven reads, 52 on /market and 196 on PM Trade. A constant 51 across pages of different sizes is most likely the app shell
  (the sidebar's labels); the walk does not say which nodes they are.
- **1cb21619 changes what "ground" means** to the paint stack at the text's centre, SVG fills included. It was read as
  code only. Its named regression counts (/market 1159 and 0) reproduce.
- **Not swept, as the author says:** the Bulk Edit, Remove, Lookup and Upload modals; History; the detail modal's
  factor tables; non-text icons.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 01:31Z -- pins aebfd7c9, d68827f7 and 90dc443d (2.0.0_SA_COO~D msg 105457): PASS

origin/DEV read 90dc443d by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at 90dc443d, 0
uncommitted paths before and after. Every run exited 0.

| what | the pins say | read here at 90dc443d |
|---|---|---|
| `node scripts/ui-smoke-hover-control.cjs` | flat, nested and descendant hover rules detected; a plain element and `*:hover` not; CONTROL-PASS | `{"rules":3,"flat":true,"nested":true,"child":true,"never":false} CONTROL-PASS`, exit 0 |
| /advisor-intelligence, no fixture | 31 siblings (82 tagged), 0 below | 31 read (82 tagged), 0 below; 5 walked 0 and 0; 45 reads skipped as not visible |
| /attribution, rb-s-9-attribution.json | 220 -> 215 siblings, 0 below | 215 read (271 tagged), 0 below; 5 walked 0 and 0; 46 skipped |
| PM Upload modal, `--accept-dialogs --click "Upload Portfolio"` | 14 siblings 0 below; 3 elements 0 and 0 | DIALOG-ACCEPTED, CLICKED; 14 read (201 tagged), 0 below; 3 walked 0 and 0; 1 field 0 below; 201 skipped behind the modal |

- **Row S24 gap 2 now has its control, committed and run here.** The reader picks up a flat rule, a nested media rule and
  a descendant rule on a synthetic page and does not pick a plain element. No real page element has been picked by the
  stylesheet alone yet (0 on all three runs here); the control is what shows the reader works. Gap 2 reads REMEDIED on
  that evidence.
- **The universal-rule worry is answered.** The control's `never` case is false, and the author states the browser
  prints `*:hover` as `:hover`, whose stripped base is empty and dropped, with a literal `*` guarded as well.
- **The skip count is printed** (VISIBILITY-SKIPPED), which answers this seat's note 1 of the ea22eda3 read. The ancestor
  case is narrowed to text that ignores pointer events, which answers note 2; /attribution's sweep went from 220 to 215.
- **d68827f7** fixes the one line this seat read below on /advisor-intelligence, on all four partner pages. Read here on
  the page this seat reaches; the other three partner pages were not rendered.
- **90dc443d.** The before-states (3.62 and 2.77) were not reproduced.
- **A finding the author reports and this seat did not measure:** `--state-disabled-ink-band` reads 4.31:1 on #25314D.
  That is the same class as row DSGN_REBRND-S20 (the band's disabled ink measured on one ground only), on a third
  ground. The token table is the CTO's.
- **Also reported, not checked here:** Bulk Edit, Remove, Lookup and Version History have no opener anywhere in `src`.
  If so they are unreachable code, and no walk can or need grade them.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 01:47Z -- pins 7c66142a, 7c2fef18 and 560f165f (2.0.0_SA_COO~D msg 105459): PASS on their after-state

origin/DEV read 560f165f by fetch. The vite server on port 5174 served the worktree `portal-coo-d-r43` at 560f165f, 0
uncommitted paths before and after. Every run: `--hover-walk 200 --hover-every --text-all --placeholders`, exit 0.

| page and state | the pins say (after) | read here at 560f165f |
|---|---|---|
| /data-refresh | 44 siblings 0 below; 12 elements 0 and 0 | 44 read (95 tagged), 0 below; 12 walked 0 and 0; 41 skipped |
| /trade-submission | 36 siblings 0 below | 36 read (87 tagged), 0 below; 14 walked 0 and 0; 5 fields 0 below |
| /investor-reporting | 2 fields 0 below | 2 fields graded, 0 below; 26 read (78 tagged), 0 below; 4 walked 0 and 0 |
| PM History (Resume, History) | 197 siblings 0 below | 197 read (248 tagged), 0 below; 7 walked 0 and 0 |
| PM Submit modal (Resume, Trade, Submit) | 21 siblings 0 below; 8 fields 0 below | 21 read (574 tagged), 0 below; 8 fields 0 below; 646 skipped behind the modal |

- **Before-states (1.98, 3.62, 4.25, 4.44 to 4.49; 11 and 6 on /data-refresh): NOT REPRODUCED.**
- **560f165f changes a shared component.** `SearchSelect`'s disabled state takes `--state-disabled-ink-light` (index.css
  line 404: #56688F, stated 5.57:1 on white) with no opacity. The commit says only the disabled state changed. Read here on
  /investor-reporting, where the client search is disabled while the directory loads; no other page that uses the
  component was rendered in a disabled state.
- **The route sweep (18 default shells, 13 clean) is the author's.** This seat walked the five states above and not the
  18. Two items the author names and did not edit, each with an owner: /portfolios "Last Qtr" at 4.49:1 (inside
  4.0.0_SA_CRO's lease) and /login (outside the commission).

-- 3.0.0_SA_CVO
