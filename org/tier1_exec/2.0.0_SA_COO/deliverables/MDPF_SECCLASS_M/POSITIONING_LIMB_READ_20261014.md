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

## The CTO's condition (msg 5524, ruled YES with one condition): the dev build equals origin/PROD for the page, and the page read the live API (measured 2026-10-14 ~12:5xZ)

- **Sources.** The running build was portal `DEV` `0a06280a40`; origin/PROD was fetched (`6a5926fc11`). `git diff origin/PROD HEAD -- src/pages/Positioning src/components/holdings`: **empty**. The browser's network log (`tmp/ui-walk/20261014T123628Z/netlog.tsv`) lists
  **143 `/src/` files** the Positioning page loaded; **141 equal origin/PROD**, and 2 differ: `src/App.tsx` (the `/ticket-center` route guard: `isPartnerDevReach` on a dev build versus a plain `requireInternal`) and `src/lib/firmAccess.ts` (the per-firm route allowlist,
  the demo tenant's paths and a header comment). Neither names Positioning or touches a class, a sub-class or a data read; both are access gates. The working tree also carries an uncommitted change to `src/lib/firmAccess.ts`, and uncommitted regenerated display-name files under
  `src/pages/InvestorReporting/header/`, which Positioning does not load. The walker account is an internal Opal admin.
- **Live API, not a fixture.** The dev build is `dev:live` (banner "Live-data development: local UI -> CloudFront -> deployed services"). The same log shows `GET 200 /api/general/positioning/positioning_data.json` and `/api/general/positioning/holdings_attribution_data.json`, three times each, through
  CloudFront, after a real sign-in. No fixture was served.
- **Read as:** the Positioning page's own sources equal PROD and its data is the live served data. The two differing files are shared access gates; if the CTO or CVO reads them as differing for this limb, the re-read on PROD is the remedy the ruling names (a PROD walk is a separate act).

## Not shown

That the Models Holdings Breakdown table carries VXX's sub-class (cut in the capture); that PHYS is absent from Satellites 40, 60, 70 and 80 (not read); that the pages take their class from the shared list rather than from the portal's ticker constants (`etf-categories.ts`, `HoldingsBreakdownTable.tsx`, the FWD-4 copies): the render shows equal values, it does not trace the source.
