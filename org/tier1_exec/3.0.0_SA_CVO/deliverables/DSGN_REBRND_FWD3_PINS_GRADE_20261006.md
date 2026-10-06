# DSGN_REBRND FWD-3 and R4-4 pins -- grade (3.0.0_SA_CVO, 2026-10-06 03:55Z by `date -u`)

Pins (2.0.0_SA_COO~D msgs 105466 to 105495): b0db73d1 (layer table), 2146031c (SUPERSEDED, not graded), 85e8d9a5
(its revert), 289c6f7c and 60e3e930 (U.S. Regime card and modal), 0576d88f, 9f982e97 and 97c678d3 (the gain/loss scale,
the two return badges, the type-check repair), 786c49a8 (factor-tilt bar), daf79e94 (scanner IC quintiles), 7d1ea524
(Valuation tints). origin/DEV read 7d1ea524 by fetch.

**How it was read.** COO~D's worktree had moved one commit past the tip and held 4 uncommitted files, among them
`src/index.css` and `src/lib/deltaScale.ts`, the very files under grade. So this seat made a clean checkout at 7d1ea524
(`C:/tmp/cvo-pv`, 0 uncommitted paths), built it (`vite build`, 24.9 s), and walked the build with `ui-smoke --dist`.
Two walks run earlier on COO~D's worktree are discarded.

**Verdict: PASS on what each pin claims, with three of them graded on code and tests only, as their author says.**

| pin | claim | read here at 7d1ea524 | result |
|---|---|---|---|
| 0576d88f, 9f982e97, 97c678d3 | one writer of the gain/loss scale; every rung at 4.5:1 or better; type-checks after the repair | `bun test src/lib/__tests__/`: 5 pass, 0 fail. CI: 9f982e97 **failure**, 786c49a8, daf79e94 and 7d1ea524 success (gh run list). The rung tokens are opaque (index.css 392-397) | PASS after the repair; 9f982e97 alone was a red CI commit on DEV, as the author reported |
| 289c6f7c, 60e3e930 | the Regime card's percentile bar is the one-hue ramp; the modal reads band ink | /market: 1159 siblings, 39 walked, 0 below. Modal (`--clicktext "Multi-Asset Momentum"`, CLICKED): 45 siblings, 3 walked, 0 below. The card reads `--ramp-` tokens (2 uses) | PASS. The fixture reads every percentile at 0, so only the ramp's left end is seen, as the author says |
| 85e8d9a5 | the duration ladder back on its locked hues | `PORTFOLIOS` reads orange, amber, green, blue, red (holdings-shared.tsx 20-24); /attribution 215 siblings, 0 below | PASS |
| daf79e94 | IC quintile fills a one-hue ramp, ink 5.95:1 or better, computed | `quintileUtils.ts` 75-79 map quintiles 1-5 to `--cell-ramp-1..5` (hue 221, index.css 399-403). The scanner page walks 0 below, but its quintile cells need factor data the default page does not load | PASS on code; not seen rendered |
| 786c49a8 | factor-tilt bar reads the gain/loss scale | /factor-tilts walks 0 below on 8 siblings; the page is empty without data, as the author says | PASS on code; not seen rendered |
| 7d1ea524 | Valuation tints read the gain/loss pair | /valuation walks 0 below on 50 siblings; no fixture draws a tinted cell | PASS on code; not seen rendered |
| b0db73d1 | the layer table prints the role contrasts and the denominator | `node scripts/layer-table.mjs`: band 5 of 5 pairs measured; light 2 of 5, `layer-light-strip` and `layer-light-tile` MISSING | PASS as an instrument. It measures that FWD-12's light world lacks two rungs |

- **Not reproduced:** the before-states, and the pin test's negative control (a rung set to L52 fails).
- **The S25 guard showed itself live:** a first modal attempt with a wrong click name exited 2 with HOVER-WALK-INVALID.
- **The clean checkout is left at `C:/tmp/cvo-pv`** (a portal worktree, detached at 7d1ea524, its borrowed
  `node_modules` link removed). Removing it is a recursive delete and waits on Andrew's word.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 04:02Z -- pins 4fa0312e, e568f064, 48fac2b6 (2.0.0_SA_COO~D msg 105507), and one correction

**Correction to the table above.** The /valuation and /factor-tilts rows: this seat walked `/valuation`, which is not a
route; the app's routes are `/valuations`, `/correlations`, `/macro` and `/factor-tilts` (App.tsx 118-121). The
`/valuation` reading (50 siblings) was the app's fallback page, the same count `/correlation` and `/macroeconomics`
gave. The /factor-tilts row stands. The Valuation pin's verdict does not move: it was graded on code and tests.

Read on the same clean checkout, now at 48fac2b6 (0 uncommitted paths), rebuilt (19.9 s), walked with `--dist`
(port 5174 is in Andrew's use and was not touched).

| pin | claim | read here at 48fac2b6 | result |
|---|---|---|---|
| 4fa0312e | correlation matrix on the neutral sign pair, opaque, ink 4.5:1 | CI by commit: CI - Build & Validate=completed/success. /correlations walks 9 siblings, 0 below; no correlation data loads, so no matrix cell is drawn | PASS on code and tests; not rendered |
| e568f064 | factor-tilt bar and Valuation tints move to the sign pair | CI success. /factor-tilts 8 siblings and /valuations 9 siblings, 0 below, both empty without data | PASS on code and tests; not rendered |
| 48fac2b6 | Macro percentile heatmap on the one-hue ordered ramp | CI success. /macro 13 siblings, 4 walked, 0 below; no heatmap cell drawn | PASS on code and tests; not rendered |

- `bun test src/lib/__tests__/` at 48fac2b6: 7 pass, 0 fail (the pin tests that require 4.5:1 on every rung).
- All three are FAST pins with no fixture that draws their cells. What is graded here is the token values, the tests and
  CI. Whether any of these pages reads right with data is not established by anyone yet.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 04:26Z -- pins 7e5df8d3, bacc2a22, 6d25ecc9 (2.0.0_SA_COO~D msg 105524): PASS on code, not rendered

Read from origin/DEV 6d25ecc9 by `git show` and `gh run list --commit`; no build or walk this time (none of the three
draws without data, port 5174 is in Andrew's use, and this seat's clean checkout was deleted on his word).

| pin | claim | read here | result |
|---|---|---|---|
| 7e5df8d3 | remove QUARTILE_PALETTE, no importer | CI success. `git grep` at 6d25ecc9 over src: 0 files import it; PEERS_QUARTILE_BANDS stays | PASS |
| bacc2a22 | client Top 9 on one hue, lightness by rank, 10.9 to 3.68:1 on the panel body | CI success. The nine hexes (ClientListPanel.tsx) compute 10.90 down to 3.68:1 on #192643, as stated; 12.90 to 4.36 on #0A1733; 9.39 to 3.17 on #25314D, so rank 9 clears the 3:1 non-text bar on all three | PASS on code. The constant keeps the name `VBGYOR_TOP9` for a ramp that is no longer violet-to-red |
| 6d25ecc9 | one PERCENTILE_RAMP for percentile lines and markers; RISK_CONTRIBUTION_GRADIENT removed | CI in progress at this read. PERCENTILE_RAMP (chartColors.ts 705-711) reuses the Top 9 steps 9, 7, 5, 3 and 1, p10 darkest; `git grep`: 0 importers of the removed gradient | PASS on code; CI and the pin test (bun 7 pass, the author's) not read to completion here |

Not converted, as the author says: the Macro time-series band fills and lines (direction-aware), a later row.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 04:52Z -- pins 8ce292c7, ac3b018e, 79bad192 (2.0.0_SA_COO~D msg 105529): PASS; the instruments reproduce

Read on a `git archive` extract of origin/DEV 79bad192 (src, design, the two scripts; this seat's scratch, no git, no build).

| pin | claim | read here | result |
|---|---|---|---|
| 8ce292c7 | NNA outflow/inflow percentile lines on the gain/loss pair, near-zero lightest, 4.5:1 on the panel body | CI success. `bun test src/lib/__tests__/deltaScale.test.ts`: 8 pass, 0 fail. NNA_PERCENTILE_LINES (chartColors.ts 718-721): rose for outflow, mint for inflow, p25 lightest on each side | PASS on code and tests; not rendered |
| ac3b018e | overlay census: 580 translucent-white backgrounds in 117 of 596 files (REST 387, HOVER 187, ODD 6) | the same five numbers; two runs byte-identical | REPRODUCES |
| 79bad192 | layer-table --containers: 24 tokens, the shared values, one hover=surface collision | 24 tokens; in the band world `bg-hover-light` = `bg-surface` = `card` = #1E2D4D; two runs byte-identical. The base table still reads light 2 of 5 pairs measured, `layer-light-strip` and `layer-light-tile` missing | REPRODUCES. CI was in progress at this read |

- The two instruments count source files differently: the overlay census reads 596 files, the container census 597. Each
  prints its own rule; neither is wrong, and a reader comparing them should not expect one denominator.
- As the author says, these are findings, not outcomes: FWD-12 is not realized while the light world lacks two rungs.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 05:00Z -- pins f93820fe, cc9224f3 (2.0.0_SA_COO~D msg 105531): PASS as tokens; FWD-12 not realized

Read on a `git archive` extract of origin/DEV cc9224f3 (src, design, the instruments; this seat's scratch).

| pin | claim | read here | result |
|---|---|---|---|
| f93820fe | four light rungs at the band ratios 1.18 / 1.22 / 1.24 / 1.18, opaque, under the 1.9:1 cap; light table 5 of 5 | CI success. `bun test` layerLight + deltaScale: 10 pass, 0 fail. `layer-table.mjs`: strip #EAECF1, tile #D1D7E1, hover #B9C2D1, selected #A8B3C6; pairs 1.08, 1.18, 1.22, 1.24, 1.18; "light 5 pairs (5 measured)", "WITHOUT A DECLARED RUNG: none" | PASS as tokens |
| cc9224f3 | the hover=surface collision gone | `--containers`: `bg-hover-light` now #2F426A in both worlds, sharing with `layer-hover` and `state-hover-band`, no longer with `bg-surface` (#1E2D4D band). CI in progress at this read | PASS as a token change |

- **Nothing consumes the new rungs yet.** Over src the four names appear only in `index.css` (their declarations) and the
  pin test; no component reads them. So no rendered surface changed, as the author says, and FWD-12 is not realized
  until pages move onto them.
- `bg-hover-light` reads the same value in both worlds because it is declared once; the container census prints that
  limit itself.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 05:23Z -- pins 6f8b78a1, 48472ff4 (2.0.0_SA_COO~D msg 105532): PASS; and a miss of this seat's

**A miss in this seat's daf79e94 row above.** It passed the scanner quintile ramp "on code" from the token mapping alone.
At that build `--cell-ramp-5` (221 34% 18%) had the same lightness as `--layer-body` (221 45% 18%), so the lowest quintile
cell read as no fill. This seat checked that each quintile maps to a rung and did not check the rungs against the ground
they sit on. The author found it by drawing a swatch sheet.

Read on a `git archive` extract of origin/DEV 48472ff4, built in this seat's scratch (`vite build`, 8.8 s; the borrowed
`node_modules` link removed after), walked with `ui-smoke --dist`.

| pin | claim | read here | result |
|---|---|---|---|
| 6f8b78a1 | ramp lifted to L 45..26; rung 5 at 1.31:1 from the body; pins read the theme's band ink #E6EAF4 | CI success. index.css 406-410: `--cell-ramp-1..5` at L 45, 40, 35, 30, 26 against `--layer-body` L 18 (line 374). `bun test src/lib/__tests__/`: 11 pass, 0 fail | PASS |
| 48472ff4 | /attribution tilt bars and TILT column on the sign pair; return inks on the delta ink; 0 below over 215 + 5 | /attribution with rb-s-9-attribution.json: 215 siblings (271 tagged), 0 below; 5 walked, 0 and 0. The screenshot shows the under-weight bar in amber and the over-weight bar in blue, neither red nor green; returns print in light green | PASS on the drawn page. CI was in progress at this read |

- Not seen, as the author says: the SelectionTab tab.
- The extract skipped two unrelated symlinks under etl/ (they point at a Linux path); the portal build does not read them.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 05:43Z -- pins 02027f7c, b0051830 (2.0.0_SA_COO~D msg 105534): PASS on code; the drawn count not reproduced

Read on a `git archive` extract of origin/DEV b0051830, built in this seat's scratch (9.5 s, the borrowed link removed
after), walked with `ui-smoke --dist`.

| pin | claim | read here | result |
|---|---|---|---|
| 02027f7c | /positioning HoldingsTab return and effect inks on the delta ink; drawn: 195 siblings and 11 hover elements, 0 below | CI success. The diff adds 18 delta-ink lines; 9 `text-green/red-300/400` remain in the file, which the author names as header labels and a badge. This seat's walk of /positioning, with no fixture and with `cross_firm_positioning_49f.json`, reaches 24 siblings and 7 elements, 0 below, in the default view and after `--click "Performance"` (CLICKED): the page renders without holdings rows, so the sign inks were not drawn here | PASS on code. The author's 195-sibling state was not reproduced: this seat does not have the fixture that fills the page |
| b0051830 | Advisor Intelligence growth and NNA signs on the delta ink; static only | CI in progress at this read. 28 sites changed across PartnerAnalytics and AdvisorsTab per the diff stat; alpha-tinted inks and chart strokes left as stated | PASS on code; not rendered |

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 06:12Z -- pins defda8b1, e0ff23a9, 0404c8e0 (2.0.0_SA_COO~D msg 105535): PASS on code, static only

Read from origin/DEV 0404c8e0 by `git show` and `gh run list --commit`. None of the three is drawn by any fixture.

| pin | claim | read here | result |
|---|---|---|---|
| defda8b1 | the Distribution strip dots match the ramp lines; NNA signs on the delta ink, above/below on the sign pair; TaxCostBasis gain/loss on the delta ink | CI success; the diff stat matches (2 files, 21 lines each way) | PASS on code |
| e0ff23a9 | FactorTilts R2 and alpha, Overview pct-change on the delta ink | CI success; 2 files, 4 lines | PASS on code |
| 0404c8e0 | flow signs, factor tilt on the sign pair, strip repair, BenchmarkHeatmap tooltip label -400 to -200, "computed about 6:1" | CI had not started at this read. The tooltip change is emerald/red/yellow-400 to emerald/rose/yellow-200. The tooltip's ground is not set in BenchmarkHeatmap.tsx, so this seat could not read it. On indigo grounds the new inks compute 4.46 to 9.82:1: rose-200 is 4.46 on #4F46E5 (indigo-600) and 5.60 on #4338CA (indigo-700); the old red-400 was 2.27 to 4.13 on the same four | PASS on code. "About 6:1" holds on indigo-700 or darker; on indigo-600 rose-200 sits just under 4.5. The ground decides it |

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 06:34Z -- pins 4f836795, 75ff922c (2.0.0_SA_COO~D msg 105538): PASS on the author's renders; not redrawn here

The two pages were drawn by the author from fixtures built from the response types. The fixtures are scratch and not on
disk where this seat can read them (`.frontend-dev/testing/` and `.frontend-dev/fixtures/` hold neither), so this seat
graded the code, CI and the author's committed screenshots (@c3ce66038d), not a render of its own.

| pin | claim | read here | result |
|---|---|---|---|
| 4f836795 | /macro heat reads as one blue hue, dark low, light high; stale legend labels and a 2.3:1 indigo hover link fixed; re-walk 109 siblings, 12 elements, 0 below | CI success. `MACRO_AFTER_hover_fix.png` shows the heatmap in one blue hue and the five legend labels in the muted band ink | PASS on the author's render. **The before evidence is missing:** `MACRO_V3_FIRST_LOOK.png` and `MACRO_AFTER_hover_fix.png` are byte-identical (sha256 37a85fb90a8c..), both showing the fixed state |
| 75ff922c | /correlations legend and caption match the sign-pair matrix: 7 swatches, "blue / neutral to amber" | CI in progress at this read. `CORRELATION_LEGEND_AFTER.png` shows seven swatches (three blue, one neutral, three amber) labelled 0.6 to 1.0 down to -1.0 to -0.6, and the caption reads blue for positive, neutral to amber for low or negative | PASS on the author's render |

- A visual note, not a failure: at legend size the five /macro swatches read close to one another; the difference is
  clear in the cells, less so in the legend.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 07:00Z -- pins 8cc3b769, 33db2f95, 5e31a702 (2.0.0_SA_COO~D msg 105544): PASS; one finding (row DSGN_REBRND-S27)

The author's fixtures are again scratch and not on disk here, so these are graded on code, CI, the pin tests on a
`git archive` extract of 5e31a702, and the author's screenshots (each a distinct file this time).

| pin | claim | read here | result |
|---|---|---|---|
| 8cc3b769 | /valuations gains a colour key; the Expand link at 3.77:1 fixed | CI success; 2 files, 3 lines | PASS on code and the author's render |
| 33db2f95 | /factor-tilts chips on the sign pair; six abbreviation labels at 3.6:1 fixed | CI success; 2 files | PASS on code and the author's render |
| 5e31a702 | the sign pair re-cut out of the status hues into the data family: cyan 191, violet-magenta 300, declared in the theme | CI success. `bun test src/lib/__tests__/`: the colour tests pass (10); one unrelated test file fails only because the extract has no path aliases (`@/lib/dateUtils`). index.css 412-419 and the theme's `--data-sign-negative` (300 55% 58%) read as stated. The author's `CORRELATION_AFTER_SIGN_RECUT.png` shows cyan positives, violet negatives, navy near zero, and a matching seven-swatch key | PASS |

**Finding, from the author's own screenshot (row DSGN_REBRND-S27):** on /correlations the row labels sit one row below their cells.
The first row of cells (Cash's column, value -0.68) has no label beside it, every label from "Gov/Credit 1-3Y" down sits
half a row to a row lower than its cells, and the last label, "EM", has no row beside it. This seat read it in the PNG
only; it did not draw the page.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 07:09Z -- pin caf131c7 (2.0.0_SA_COO~D msg 105545): PASS on code, tests and the author's renders

| read | result |
|---|---|
| CI | in progress at this read |
| `bun test` deltaScale + layerLight on a `git archive` extract of caf131c7 (with the repo's tsconfig, so the `@/` paths resolve) | 11 pass, 0 fail |
| the author's three screenshots | three distinct files (sha256 ea26a30c.., f56e37f3.., b4ff3257..) |
| `MACRO_MODAL_AFTER_unemployment.png` | Unemployment, where high is bad: the band above the median is the loss hue, below it the gain hue; the 75th and 90th lines rose, the 10th and 25th mint; the percentile (99.2) and the vs-median figure in the loss ink; the header ticker and description read in the muted band ink |

The direction rule reads right on the one indicator this seat looked at (a bad-high series). The GDP render, the good-high
case, was not opened here. The fixture is the author's and not on disk here.

A small note from the same render: the modal's subtitle reads "Growth -- Percentage of the labor force that is jobless",
which names Unemployment's category as Growth. That is the fixture's category field or the page's mapping; it was not
read further.

-- 3.0.0_SA_CVO

## Addendum 2026-10-06 08:18Z -- pins eab83fd5, 1c86adbe, 14dcce76, 4ca437eb (2.0.0_SA_COO~D msg 105549): /market as the first light page

Built from a `git archive` extract of origin/DEV 4ca437eb in this seat's scratch (18.0 s; the borrowed link removed after),
walked with `ui-smoke --dist`.

**Verdict: PASS on every surface the walk reads, on /market and on seven other pages that share the rewritten components.
One defect the walk does not reach: the indigo tooltips on /market became unreadable in the light world (row DSGN_REBRND-S28, ARMED).
One question for Andrew: the Daily Cloud's excepted colours on white.**

| read | result |
|---|---|
| CI | 4ca437eb, 14dcce76 and eab83fd5 success; 1c86adbe (DESIGN.md only) has no run |
| `bun test` over src/lib and src/ui/components tests | 28 pass, 0 fail |
| /market, rb-s-9-market.json | 1159 siblings, 39 walked, 0 below; the screenshot shows white panels, light strips, navy ink |
| the regime modal | 45 siblings, 3 walked, 0 below |
| shared-component regression: /attribution, PM Sector, /trade-submission with rows, /data-refresh, /investor-reporting, /advisor-intelligence | every count equals this seat's earlier reads (215, 366, 49 and 40 fields, 44, 26, 31), 0 below. The band pages did not move |

**Row DSGN_REBRND-S28, the tooltips.** The idiom rewrite turned white tooltip text into the role inks, and the light scope makes the
role inks navy. Two tooltips on /market keep their solid indigo ground (#5F3BE3): the Daily Cloud word tooltip now prints
`--ink-1`, 1.87:1 in the light world (it was white, 5.41:1 on the band), and the Fear and Greed component tooltip prints
`--ink-3`, 1.32:1. The walk did not see them: they open on hovering an SVG word or a gauge component, which the walk does
not hover.

**For Andrew, not a defect against the spec:** the Daily Cloud keeps its colours by his 2026-09-14 exception. On the
band they read; on white its yellow and green words compute about 1.5 to 2.5:1 (yellow-400 1.53, yellow-500 1.92, lime
1.98, green 2.28, emerald 2.54; red 3.76). Whether the exception holds on a light page is his to say. The walk skipped
these words (49 reads not visible at their centre).

DESIGN.md C7 and C3.1 (eab83fd5, 1c86adbe) are contract edits; this seat read them as contract changes and did not
grade them against anything.

-- 3.0.0_SA_CVO
