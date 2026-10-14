# FWD-1 Positioning limb -- one read (2.0.0_SA_COO~M1, dell1, 2026-10-14 12:32Z-12:41Z)

Asked by: CTO round-24 analysis section 4 item 2 (msg 5506): render both Positioning surfaces for GLD, PHYS and VXX and compare class and sub-class with the Black Diamond page values of D1-C-S21.
Claim words: `measured` = read this session off the rendered page or the live table.

**Instrument:** `/ui-walk` (read-only walker, dormant service account armed and disarmed by the walker each run; every run printed `DISARM ... REFUSED` and `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401`), local dev build on port 5174 (portal DEV `0a06280a`),
route `/positioning`, tabs pressed by label. Walk stamps (screenshots are under `tmp/ui-walk/<stamp>/shots/`, gitignored, not committed): `20261014T123205Z` (Models), `20261014T123329Z` (Satellites, Satellite 15), `20261014T123628Z`
(Satellite 90, Satellite 50), `20261014T123906Z` (Satellites 30, 40, 60, 70, 80). Page data as of October 13th, 2026, 5:00p ET. The dev server was stopped after the walk.

## What the pages show (measured, read off the rendered screenshots)

| ticker | surface | class / sub-class shown | where |
|---|---|---|---|
| GLD | Satellites, Holdings Breakdown table | Commodities / Metals | Satellite 15 (8.06 pct), also the one Commodities tile of Satellites 30 and 50 (treemap, Commodities colour) |
| VXX | Satellites, Holdings Breakdown table | Structured / Hedge | Satellite 90 (1.75 pct); Structured tile on Satellite 50 |
| VXX | Models, Portfolio Composition treemap | Structured (pink tile, legend Structured) | Models AGG (1.6 pct); the Models Holdings Breakdown capture is cut before its Structured rows, so the sub-class is NOT read on Models |
| PHYS | both | not shown | not a tile or a row in the Models view, in Satellites 15, 30, 50 or 90 (all read); Satellites 40, 60, 70, 80 were walked and their screenshots not read for it |

## The shared list's own rows (measured, `dynamodb get-item` on `etf-classifications`, 2026-10-14 ~12:4xZ)

GLD: commodities / Metals, fund, `classified_by` seed. PHYS: commodities / Metals, fund, seed. VXX: structured / Hedge, fund, seed.

## Comparison

- **GLD:** Positioning (Satellites) = shared list = the Black Diamond page value (Commodities / Metals): EQUAL.
- **VXX:** Positioning (Satellites) = shared list = the Black Diamond page value (Structured / Hedge): EQUAL. Models shows the class (Structured) and not the sub-class in its capture.
- **PHYS:** shown on neither Positioning surface in the views read, so there is no Positioning value to compare; the shared list's row equals the Black Diamond page value (commodities / Metals).
- No difference was found on any ticker that Positioning displays.

## Not shown

That the Models Holdings Breakdown table carries VXX's sub-class (cut in the capture); that PHYS is absent from Satellites 40, 60, 70 and 80 (not read); that the pages take their class from the shared list rather than from the portal's ticker constants (`etf-categories.ts`, `HoldingsBreakdownTable.tsx`, the FWD-4 copies): the render shows equal values, it does not trace the source.
