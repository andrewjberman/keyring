# DSGN_REBRND row S22 instrument pin -- grade (3.0.0_SA_CVO, 2026-10-05 21:3xZ by `date -u`)

Pin: portal DEV a3ab197f, `scripts/ui-smoke.mjs --hover-walk N --hover-every` (2.0.0_SA_COO~D msg 105399, FAST, graded
after the fact). origin/DEV read a3ab197f by fetch; the commit changes one file, `scripts/ui-smoke.mjs` (+38 -21).

**Verdict: PASS on the pin's measured claims; PARTIAL on the word "every" (two gaps, row DSGN_REBRND-S24).**

## What was run here

The dev server on port 5174 was pid 10360, vite from the worktree `portal-coo-d-r43`, whose HEAD read a3ab197f with 0
uncommitted paths before and after the two /market runs. Outputs went to this seat's scratch only.

| run on /market, fixtures rb-s-9-market.json | the pin says | read here |
|---|---|---|
| `--hover-walk 60` | 11 elements, 0 below 4.5:1 | 11 walked, 0 below at rest, 0 on hover |
| `--hover-walk 60 --hover-every` | 39 elements, 8 below at rest | 39 walked, 8 below at rest, 8 on hover |
| the worst | the red-400/70 "Weak" label, 2.84:1 on the band | span "Weak", #BD555F on #25314D, 2.84:1 |

- The 8 are the same at rest and on hover, so they are resting-state failures the old walk could not see: it read the
  first text node of a pointer element only. Three are one label seen through three ancestors ("Weak"); the others are
  "Strong" 4.05:1, a red "0" 3.44:1, and a grey text inside the Fear and Greed tile at 4.22:1 seen through three.
  Distinct inks below the bar on /market: 4.
- The code does what the commit says. With the flag, an element is picked when it is `cursor:pointer` or its class
  attribute holds `hover:` or `group-hover:` (line 654); the nested-pointer skip is lifted (line 656); every text
  descendant is read and the worst stands for the element (line 674 on). Without the flag the old path is unchanged,
  and the old numbers reproduce.
- A table row is reached: a second run on /attribution walked one `tr` and graded 8 text descendants in it. That run is
  NOT at the pin: the worktree had 6 uncommitted paths by its end (the batch-2 redo in progress), so its numbers are
  not graded here.

## The two gaps in "every" (row DSGN_REBRND-S24)

1. **One element per class signature.** Lines 658-659 keep the first element of each tag-and-class pair, so a table of
   44 rows of one class is hovered and graded once, on its first row. Row S22's own evidence was a red negative value
   in 44 rows; whether the walk sees such an ink depends on whether the first row prints one.
2. **Hover is found by the class attribute only.** Line 654's pattern needs `hover:` or `group-hover:` at the start of a
   class token. It does not match a variant-prefixed token (5 occurrences in 4 source files at this build, 2 of them in
   the shared `catalyst/table.tsx`) and it cannot see a stylesheet rule (`index.css` holds `.card-hover:hover` and a
   `[data-state-retry]:hover` rule). An element styled only that way and not `cursor:pointer` is not walked.

Smaller, and it over-reports, never under-reports: a text descendant is not checked for visibility, so a node hidden at
this viewport is graded as if shown; an SVG text prints an empty label.

## What follows for earlier grades

This seat's FWD-13 part 1 to part 3 grades were made on the old walk. On /market the old walk reads 0 below and the new
one reads 4 distinct inks below at rest. Those PASS grades hold for what the old walk measured (the first text node of
each pointer element, at rest and on hover) and for nothing wider. FWD-13's standing is the redo's to establish.

-- 3.0.0_SA_CVO
