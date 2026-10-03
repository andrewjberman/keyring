# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 10Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 09:5xZ-10:1xZ | DSGN_REBRND (FAST; IR lines still blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3, Next 4c | ETFs and Satellites walked with the widened limb; the Satellites footer date fixed: portal `46aeea17` on origin DEV (ls-remote 10:10Z) | DRIVE FORWARD |

## 4c -- ETFs and Satellites

- Walk `20261003T095441Z` (signed in, 5174, `--press ETFs --press Satellites --contrast-table`): ETFs 86 pairs (20
  text groups), Satellites 112 pairs (30 text groups), 0 under their bar on both.
- `format:dates` on Satellites: both footers wrote the ISO date ("holdings as of 2026-10-03") beside the page end's
  long form. The `2026-09-22` in the finding is the check's own label for the ISO pattern, not a page date. Fix:
  formatPanelTimestamp in PositioningSummary.tsx and HoldingsTab.tsx. Pin `footer-date-format.test.ts`. Typecheck
  rc=0, eslint 0 errors, Positioning tests 5 pass.
- After-walk `20261003T100559Z`: no date finding; the footer reads "Source: Black Diamond, holdings as of October
  3rd, 2026, 5:00p ET" (cropped and looked at).
- Walker: the older `design:contrast` check read every treemap tile label against the panel behind the chart (32-60
  false hits per view). It now reads the tile `rect` fill as the text limb does: 4 hits remain, all the satellite
  dialog's gradient header (a background-image ground; parked).

## Parked (STATUS 4c, owner this seat)

- `dateUtils.create5pmETDate` decides DST from the runtime's zone: under TZ=UTC a summer date reads "6:00p ET"
  (2026-10-03), while a winter date reads 5:00p. Found when the first pin draft failed under bun test.
- Satellite 90's labels run past the Summary's right edge at 1440 px.
- The old contrast check cannot read a gradient/background-image ground.
