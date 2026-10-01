# DSGN_REBRND -- round-2 grade on the served pages (`3.0.0_SA_CVO`, 2026-10-01 09:5xZ to 10:3xZ)

**Asked by:** `1.0.0_SA_CTO` RULINGS batch 73 item 6 and batch 74 item 7: grade FWD-2 to FWD-5, FWD-7, FWD-8 and FWD-10
to FWD-13, "with the 37 remediation rows read against what landed". FWD-1, FWD-6 and FWD-9 are person acts or were
graded in round 1 and are not graded here. **Text graded against:** PRD v0.10 @f3f726763d ENDPOINT (prd-signoff reads
ADMITTED; this seat's half was restored @86e1708ffd). **Planes read:** portal DEV HEAD `2879d65b` (= origin DEV) and
origin PROD `ba8e971f`; the three round-2 commits the CTO names (`086371dd`, `a7c4fa4f`, `0aefb3c5`) are ancestors of
both. Read-only.

**Verdict in one line: 4 of 10 outcomes grade REALIZED on their APPLIED bar (FWD-2, FWD-5, FWD-7, FWD-8), each with
one named gap; 6 are NOT REALIZED or only partly evaluated, because round 2 delivered one page (/market, pass 1) of a
page-by-page scope and stopped.** The project is not closeable on these grades; it is held on work, not only on
Andrew's side-by-side.

## How each was read

- Source census at both refs: `git grep` counts with file denominators (978 ts/tsx/css files under `src/` at DEV, 938
  at PROD). The two refs agree on every verdict below; the counts printed are DEV's (PROD differs only in size:
  recharts 41 import lines in 39 files, lucide-react 122 in 119).
- The project's own six checkers, run by this seat at the current tree.
- Two headless renders at 1440 wide on the local dev build (`scripts/ui-smoke.mjs`, stubbed session, no data
  fixtures): `/market` and `/positioning`, both read. Canvas measured `rgb(244, 246, 250)` on both, the contract's
  #F4F6FA.
- A keyboard walk this seat scripted: Tab pressed 30 or 40 times per route, the focused element's computed outline
  and box-shadow read at each stop.

## Grades

| # | outcome (bar) | read | grade |
|---|---|---|---|
| FWD-2 | figures in the firm's typeface (APPLIED) | `font-mono`: 1 occurrence in 1 file, down from 222 at the cut; the one is `src/lib/designTokens.ts:158`, a `dataValue` token no other file references; `tabular-nums` 135 occurrences; Lato self-hosted (`public/fonts/lato-regular-400.woff2`, `lato-semibold-600.woff2`, `OFL.txt` beside them); both renders show Lato figures | **REALIZED**, one gap: the 700 weight is the SemiBold face (row W1-S8, open on Andrew's word). The before/after pixel alignment of figure columns was not re-measured |
| FWD-3 | every ordered scale one hue ramped (APPLIED) | `rb4-canon-check.py`: CANON-INTACT; the `/positioning` control renders UST, ST, INT, LT, ULT in the five locked hues, in order (Andrew-direct 2026-09-11, the ladder is canon); ramp declarations 10 across 1 hue; sentiment tokens 12, 6 off the ramp, which is the Fear and Greed gradient's named exception; `getRSIColor` still carries the Global RSI value bands and the `/market` render shows them in chartreuse | **NOT REALIZED**: one ordered scale is known off-ramp (Global RSI, row S3) and no census of ordered scales with a printed denominator exists for round 2 |
| FWD-4 | one persistent action per view, a closed identity set (APPLIED) | `rb5-accent-check.py`: ACCENTS-RESTORED, 7 of 7 sites; on both renders the accent appears only on identity carriers (title bar, subtext, active tab or sidebar item, avatar); segmented controls and tabs mark the active option by weight and rule; neither view has a primary action and neither shows an accent posing as one | **PARTLY EVALUATED, no defect found**: the accent's pixel share per route and the three-route counterexample walk were not measured |
| FWD-5 | focus visible everywhere (APPLIED) | `outline: none !important`: 0 in `src/`; keyboard walk: `/market` 40 of 40 stops paint a ring, `/positioning` 30 of 30, `/portfolios` 39 of 40 (one stop lands on the document body); the ring is a 2px white inner and 4px indigo `rgb(95, 59, 227)` outer shadow, visible in the walk's screenshot; `DESIGN.md` defines `focus-ring` and `focus-ring-on-band` | **REALIZED** on three routes, one gap: the drop zones on `/data-refresh` and `/trade-submission` carry no `tabIndex` (row W3-S6, open), so those controls cannot be reached by keyboard at all |
| FWD-7 | status and data colour are two systems (APPLIED) | `src/index.css`: 7 `--chart-*` declarations, 0 aliased to a status variable; token file: 23 data hex tokens, 4 status hex tokens, 0 shared values; the literals `#2DCE89` and `#F5365C` appear 0 times in `src/` | **REALIZED**, one gap: `--sentiment-extreme-greed: var(--success)` is one data-family property aliased to a status variable, inside the Fear and Greed exception. The exception was granted under FWD-3; FWD-7's text has no line for it |
| FWD-8 | one rendering system (APPLIED) | import census: recharts 43 import lines in 41 files; apexcharts 0; @nivo 0; @visx 2 lines in 1 file (the word cloud, the PRD's named exception); lucide-react 126 in 123; @phosphor-icons 0; framer-motion 0; motion 2 in 2; `package.json` carries exactly recharts, the two @visx packages, lucide-react and motion; `vite.config.ts` no longer names the two removed chunk entries | **REALIZED** on the census. Two charts side by side on a populated screen were not compared by eye |
| FWD-10 | the work fills the screen; a short page ends on purpose (APPLIED) | `DESIGN.md` has no page-terminator clause (0 mentions; row W1-S29, open); no populated fixture was rendered, and the PRD forbids grading density on an unpopulated route | **NOT REALIZED** on the end-of-page limb; density NOT_EVALUATED |
| FWD-11 | four designed states, every panel uses one (APPLIED) | `src/ui/components/states/PanelStates.tsx` and `EmptyState.tsx` exist; both renders show empty sentences and loading skeletons inside panels and nothing painted on the bare canvas; `rb10-state-census.py`: RAW-REMAIN, 2 rendered raw strings in 2 of 379 files; 32 `animate-spin` occurrences and 4 `Loading...` literals remain (row W3-S5); the no-permission wiring (W3-S1) and the error-versus-empty rule (W3-S4) were not exercised | **NOT REALIZED** in full: the states exist and render; the census is not at zero and two of the four states were not exercised |
| FWD-12 | every surface resolves to a named layer, both worlds (APPLIED, page by page) | one page delivered: `/market`, pass 1 (`0aefb3c5`); its render shows title strip, body and tile as three distinct rungs; `rb7-contract-check.py inversion`: 8 of 8 required clauses carried by `DESIGN.md`; `bg-white/NN` overlays: 512 in 133 files across `src/`, 32 of them in 7 files of the `/market` components | **REALIZED for one page's first pass; NOT REALIZED for the product.** The delivered page still carries 32 overlays that the proof wants mapped to a rung or enumerated |
| FWD-13 | ink follows the current state's ground (APPLIED, page by page) | no per-role state-token family was found in `src/index.css` by name; no contrast table was computed by this seat; rows W2-S8 and W1-S11 (three canon hexes below the 3:1 floor on white; no accent meets 4.5:1 both ways) are open rulings | **NOT_EVALUATED**, with two open contrast rulings that bound it |

## The 37 remediation rows, read against what landed

Five rows closed in place by their clocks (co-committed in `REMEDIATION_v1.md`), each on a read above:

| row | what landed |
|---|---|
| W2-S2 | `vite.config.ts` no longer carries the apexcharts and nivo chunk entries; neither package is a dependency |
| W1-S37 | the two gain/loss hex literals appear 0 times in `src/` |
| W2-S1 (ARMED) | PRD v0.10 FWD-8 rules the word cloud the one named exception; the census reads exactly that |
| W1-S22 | `DESIGN.md` defines the ring token and records the two-layer ring (C11) as the portal's own |
| C-S13 (ARMED) | the governing PRD is v0.10 on CLOUD, ADMITTED with both halves current; round 2 ran on it |

Read and still true today (stay OPEN): S3 (Global RSI bands); W1-S14 (the ladder's hexes are literals in three
writers, with no shared symbol); W1-S16 (`aum.ts` still keys on the five earlier model names); W1-S8 (Lato 700);
W1-S29 (no terminator clause); W1-S36 (`shadow-lg` 36 times in 24 files); W2-S15 and W1-S24 ("silver" 50 times in
31 files of `src/`); W3-S5 (bare spinners); W3-S6 (drop zones). 10 rows.

Not read at this grade (stay OPEN, unverified either way): W3-S1, W3-S3, W3-S4, W1-S20 (its ruling half is in the
PRD's FWD-4 text; the `/portfolio-management` half was not read), W2-S11, W1-S4, W2-S9, W1-S3, W1-S25, W1-S34,
W2-S8, W1-S11, C-S11, C-S12, C-S14. 15 rows.

The seven issuer rows about round 1's checkers and order faces (W1-S6, W1-S12, W1-S17, W1-S18, W1-S35, W1-S21,
W1-S23) bind the next issuance and nothing else. No order has been cut since; they are one class and stay OPEN until
an issuer either cuts again under them or the project stops issuing. One of them has a present cost: see Q2.

Denominator: 5 closed + 10 still true + 15 unread + 7 issuer rows = 37 rows; 5 closed, 32 open.

## Observations from the renders (not grades)

- **O-1, Global RSI on `/market` with no data.** The three bars draw with a "90D" label overprinting each bar's end
  and a third label clipped at the panel's top edge. A no-data state that draws bars is also a question for FWD-11.
- **O-2, Fear and Greed.** The helper line under the dial ("Click panel for detailed component breakdown") renders
  at a size that cannot be read at 1440 wide.
- **O-3, `/positioning` column headers** are underlined links, an idiom the brief listed as a defect (IV.9). That
  page has not had its round-2 pass.
- **O-4, a focused "LONG-TERM" header** turns blue on the dark band at the walk's last stop. Whether blue on that
  rung meets the contract's contrast bar is FWD-13's question and was not computed.

## What you should have asked but did not

- **Q1. The PRD's FWD-3 text still calls the `/positioning` five-hue control "the named positive case" of a
  one-hue ramp.** Andrew ruled on 2026-09-11 that all five hues are canon and locked. The contract and the checker
  carry the ruling; the ENDPOINT's wording does not. A grader reading the ENDPOINT alone would fail the canon ladder.
  An ENDPOINT wording change re-opens the ratified-text half; it is one sentence and it should be made before the
  next person reads this outcome.
- **Q2. Two of the project's own checkers now answer the wrong question.** `rb4-ramp-check.py` prints
  RAINBOW-REMAINS on the tree Andrew approved, because it predates the Fear and Greed exception; `rb7-contract-check.py`
  with no argument exits on a usage error where an earlier order ran it bare. A checker that reads red on the
  accepted state teaches the next seat to ignore it.
- **Q3. Round 2 has no record in the project's folder.** `ledger/` holds round 1's step log only; `deliverables/`
  holds one Andrew-direct record. Ten PRD versions and a page pass exist only as commits. The closure census could
  not find the round-1 analysis for the same reason. If the project is held, the hold should name where round 2's
  state lives.
- **Q4. The `/frontend-dev` skill still teaches the retired canvas.** Its first paragraph says the page canvas is
  light silver at 81 percent lightness; the render measures #F4F6FA and the script's own output cites the contract.
  FWD-1's constraint is that the old law is rewritten in place, never left standing beside the new one. That file and
  the 50 "silver" mentions in `src/` are where it still stands.

## Not verified by this seat

Any populated render; the accent's pixel share; contrast ratios; the no-permission and error states; `/data-refresh`
and `/trade-submission` in a browser; PROD as served through the CDN (the PROD ref's source was read, not the built
bundle).

-- 3.0.0_SA_CVO
