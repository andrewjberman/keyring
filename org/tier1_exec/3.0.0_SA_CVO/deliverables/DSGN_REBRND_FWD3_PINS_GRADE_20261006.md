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
