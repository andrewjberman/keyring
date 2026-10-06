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
