# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 14Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 14:0xZ | DSGN_REBRND (FAST; IR lines still blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3 E3, row W3-S4 | a Global RSI class with no published period change shows no marker and no invented "no change": portal `1754d9c1` on origin DEV (ls-remote 14:06Z) | DRIVE FORWARD |
| 14:1xZ-14:2xZ | DSGN_REBRND (FAST; IR still blocked on ~P) | round 3 E3, row W3-S4 | the RSI modal says a missing reading instead of 50: portal `4a40a0ff` on origin DEV (ls-remote 14:29Z) | DRIVE FORWARD |

## W3-S4: the missing period change

- `useRSIValues` mapped an absent `change_90d` / `change_1y` / `change_3y` to 0: RSIBars drew the period marker on the
  bar's own end, and the tooltip read "(0.0)" and "Neutral". The change and previous value now stay null; RSIBars
  draws no marker and the tooltip says "<period> ago: not published" with no status.
- Fixture render (`--fixtures` rsi-summary, commodities without change_90d): HEAD drew Commodities' 90D marker on the bar
  end; the change draws none while Fixed Income keeps its real one. The tooltip is not exercised (hover).
- PartnerAnalytics.tsx (Assets Overview) still waits on 2.0.0_SA_COO~M's MDPF_SECCLASS lease reading FULL, per ~M's
  104617; it read FAST to 14:34Z at 14:06Z.

## W3-S4: the RSI modal

- `current || 50` drove the Status ("Neutral" beside an empty Current RSI; a real 0 also became 50); the trend tooltip
  read `value ?? 50`. Now `currentRsi` (null when absent): "Not published" in the secondary grey; the tooltip says
  "RSI: not published".
- Real run needed a driver: the modal opens from an SVG bar click, and a static render cannot reach the selection effect.
  A throwaway Playwright script in the scratchpad (auth stub as ui-smoke) served rsi-summary + rsi-details-equities with
  "S&P 500" at current null (the first try, "SPX Index", is not a known category member: "No indices available"),
  clicked the Equities bar, opened Full. HEAD: "Neutral"; change: "Not Published".

## Still open on W3-S4

- /advisor-intelligence Assets Overview (PartnerAnalytics.tsx), after ~M's lease reads FULL.
- ~~RSIModal's own `?? 50` / `|| 50` defaults~~ LANDED 4a40a0ff.
