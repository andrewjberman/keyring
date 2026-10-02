# DSGN_AMGTV1 -- FWD-24 ON THREE NAMES: every limb met except "places moved prints wherever served" -- the overlay route drops it

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~15:0xZ
**Ask:** `1.0.0_SA_CTO~Z` msg 28538, "CVO~Z: the third name for the FWD-24 census".

## The third name -- this seat's walk `tmp/ui-walk/20261002T145316Z` (AMD US)

- **Build:** 5174 served portal `df019dba` (round 27, COO~D's dev server). It differs from PROD's tree in `ChatterBubbles.tsx`,
  `PriceBars.tsx` and `types.ts` only. The header components (`SecurityOverlay.tsx`, `HeaderCards.tsx`) are PROD's.
- **The walk:** armed 14:53Z, 47 shots, walk void no, 0 API issues. DISARMED 14:55:15Z: a login with the walk password was
  REFUSED (HTTP 401).
- **AMD's header (shot 005):**
  - "Readings of October 2nd, 2026 and October 1st, 2026 ... price: ranked October 1st, 2026 from Bloomberg (94 names)": the
    latest served day; the page computes no date.
  - "Breakout (price)" reads the breakout row, "#4 | +12.88%"; units print as served.
  - Positive control: "CHATTER (THIS MONTH) -- No articles collected for this name this month.", the designed state for a
    field the payload lacks.
  - Census: 0 `unconnected-field` findings; the only raw-code hit is the exempt folded provenance line.

With BA and VLO (walk `20261002T101105Z` on PROD-equal code, ADJUDICATION v27), every FWD-24 limb but one is met on 3 names.

## The one limb not met: "places moved prints wherever served"

| route | VLO breakout row | BA breakout row |
|---|---|---|
| `/lead-panel/rankings/breakout/price` | rank 7, **places_moved 13** | rank 72, **places_moved 16** |
| `/security/<name>/overlay` `breakout_price` | rank 7, pct_jump_pct 5.7853, **no `places_moved` key** | rank 72, -4.7122, **no `places_moved` key** |

- The rankings serve `places_moved` on 32 of 94 rows; the other 62 are null with the reason "not ranked in the previous
  generation (2026-09-30)".
- The header reads only the overlay row: `SecurityOverlay.tsx:365` `placesMovedWords(breakoutRow?.places_moved)`, printed at
  :473 as ", up N places".
- **COO~D's walk `20261002T144632Z` (14:46Z, current generation)** reads VLO's header as "BREAKOUT (PRICE) #7 | +5.79%", with no
  places moved, although 13 is served.
- On PROD the price bars print no places moved either (v26, FWD-2).

So places moved is served and printed nowhere on PROD. Round 27's AV-ze-1 (bars and bubbles carry their identity on hover)
may print it on the bars at the next promote; the header stays silent until the overlay route carries `places_moved` (producer).

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S34",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T15:00:00Z",
    "one_line": "FWD-24 on 3 names (BA, VLO, AMD): latest served day, the breakout row, units as served, a 0 unconnected-field census beside a designed-empty positive control -- all met; NOT met: 'places moved prints wherever served' -- the rankings serve places_moved (VLO 13, BA 16; 32 of 94) but the overlay route's breakout_price row carries no places_moved key, so the header (SecurityOverlay.tsx:365/:473) prints nothing ('#7 | +5.79%' for VLO), and PROD's bars print none.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "walk tmp/ui-walk/20261002T145316Z (AMD US, 5174 = df019dba, header code = PROD): shot 005 'Breakout (price) #4 | +12.88%', 'Readings of October 2nd, 2026 and October 1st, 2026'; summary 0 API issues, walk void no; DISARMED 14:55:15Z, login REFUSED 401.",
        "invoke /lead-panel/rankings/{trending,breakout}/price ~15:0xZ: places_moved non-null 32 of 94; breakout VLO 13, BA 16, AMD null.",
        "invoke /security/{VLO%20US,BA%20US}/overlay ~15:0xZ: breakout_price {rank 7, pct_jump_pct 5.7853} and {rank 72, -4.7122}, no places_moved key.",
        "portal fa529337 src/pages/SecurityAnalysis/components/SecurityOverlay.tsx:365 placesMovedWords(breakoutRow?.places_moved); :473 prints it.",
        "walk tmp/ui-walk/20261002T144632Z shot 005 (VLO): 'BREAKOUT (PRICE) #7 | +5.79%'."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-24 DONE WHEN: on 3 names walked ... 'places moved' prints wherever served; a DOM census reads 0 'not served' beside a positive control.",
    "world_is": "Every limb met on 3 names except places moved, which the overlay route does not carry and the page therefore never prints.",
    "notes": "FOR THE CTO: a producer cell (the overlay route joins places_moved onto price and breakout_price, as the rankings do) or a page cell (the header reads the rankings row)."
  }
]
```

-- 3.0.0_SA_CVO~Z
