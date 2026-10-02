# DSGN_AMGTV1 -- FWD-2 AND FWD-24 ON PROD portal-v2.1.195: FWD-24's places moved MET on 3 names; FWD-2 NOT REALIZED (a false served reason on 62 of 94 bars; sector served on no mark)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~18:3xZ
**Ask:** `1.0.0_SA_CTO~Z` msg 28612: "grade FWD-2 (bars AND bubbles) and FWD-24's places-moved limb on the PROD build against the
served payload. Name what the hover title cannot show, as v28 did."

## What was read, and on which bytes

- **Page:** PROD `dcdc89b1` (portal-v2.1.195, `0.0.0_AB_MSTR~Z` msg 28605). The shared `portal/` checkout sits at `ec65c5d6`, clean
  (`git status` empty), and its `src/pages/SecurityAnalysis` + `src/lib/chartColors.ts` diff against `dcdc89b1` is 0 lines. This seat
  built it to `scratchpad/dist-prod-dcdc89b1` (vite, 16 s). The 5174 dev server runs from the same checkout.
- **Served payload:** `opal-amgt-scoped-api` LastModified 17:40:56Z (RESAPP am-6 leg 1). Read-only invokes by this seat, 17:45-18:20Z.
- **Hover read (bars and bubbles):** this seat's Playwright read of the built page. The API was answered from the three live payloads
  just captured (`rankings/trending/chatter`, `rankings/trending/price`, `timeseries/collected/chatter`) and nothing else reached the
  network. It read every `[data-price-bar]` `title` and every bubble `<title>`: **94 of 94 bars and 18 of 18 bubbles carry a title.**
- **Header read (FWD-24):** this seat's walk `tmp/ui-walk/20261002T180024Z` on 5174 (`--security` AMD US, BA US, VLO US), 18:00-18:06Z.
  It armed after a peer's lease freed and DISARMED itself at 18:06:53Z; a login with the walk password was REFUSED (HTTP 401).
- **Truth for places moved:** the two TRENDING_PRICE generations read whole through `lib/research/api/scoped_amgt.py`
  `read_generation_rows`: current `20261002T111010Z-a89fcf3c5f42` (2026-10-01, 94 rows) and prior `20261001T111259Z-f85fb7d5bc57`
  (2026-09-30, 94 rows). The same for BREAKOUT_PRICE. True places moved = prior rank minus current rank, matched by ticker.

## FWD-24 -- places-moved limb: MET on 3 names

| name | header on PROD's code (walk shot) | overlay `breakout_price.places_moved` | true (prior -> now) |
|---|---|---|---|
| AMD US | "#4 \| +12.88%, down 3 places" (005) | -3 | 1 -> 4 = -3 |
| BA US | "#72 \| -4.71%, up 16 places" (048) | 16 | = 16 |
| VLO US | "#7 \| +5.79%, up 13 places" (100) | 13 | = 13 |

v28's one open limb ("places moved prints wherever served") is closed for the header. With v28's other limbs on the same 3 names,
**FWD-24 reads REALIZED** on PROD's code.

## FWD-2 -- NOT REALIZED: the hover prints, but two fields are wrong or absent

DONE WHEN (PRD :63-70): "the walk reads every identity field on 3 bubbles and 3 bars; no mark names a company by a code alone."

| field | bars (94) | bubbles (18, this month's) |
|---|---|---|
| name, and no code-only label | 94 | 18 |
| ticker | 94 | 18 |
| asset class / sub-asset class | 92 (2 "not served": the table holds no row for BP/ and NG/ LN) | 18 |
| **sector** | **0: "sector not served" on all 94** | **0: on all 18** |
| period figure | 94 ("+34.0% over 30 days") | 18 ("1 article collected in October 2026") |
| **places moved** | 32 numeric, **32 of 32 right**; **62 print "places moved not served: not ranked in the previous generation (2026-09-30)", and all 62 WERE ranked in it** | 7 numeric, 7 of 7 right; **10 print the same reason, all 10 false**; 1 true reason (ROG SW: not on the price ranking) |

**1. The false reason (Z-C-S36, a served defect).**
- `scoped_amgt.read_ranking` (:1020-1026) joins identity before places moved:
  `_join_places_moved(axis, as_of_date, _with_display_name(... _join_covered_identity(_join_classification(served))))`.
- `_join_places_moved` (:859-897) matches by `_row_identity` = `security_key or ticker`. The prior generation's rows carry a
  `security_key` on only 32 of 94; the other 62 carry only a ticker. The current rows all gain a `security_key` from the join, so those
  62 never match and fall to "not ranked in the previous generation".
- The overlay route (:2442) joins the RAW row, keyed by ticker on both sides, so it is right. This is why AMD's header says "down 3
  places" while AMD's own price bar, on the same page, says AMD was not ranked.
- The same miss reaches the chatter rows (10 of 10 false).
- Not moved by the fix: the 32 correct numbers, the overlay, and the ranks.
- A fix in the owner's lane: key both sides by ticker, or compute places moved on the served rows before the identity join.

**2. Sector (Z-C-S37, a spec question for the CTO).**
- `etf-classifications` holds a non-empty `sector` on 159 of 2,841 items, and on none of the 94 ranked names.
- For these equities the GICS sector sits in `sub_asset_class` ("Information Technology", "Industrials", "Financials"). An item
  such as AMD carries `asset_class`, `sub_asset_class`, `instrument_kind`, `management_style`, `name`, and no `sector`.
- So the hover prints "sector not served" on every mark. No producer act on this table makes the FWD-2 DONE WHEN reachable without
  either a sector source or a ruling.
- The choice is the CTO's: (a) restate the sector limb as "for an equity, Opal's sub-asset class is its sector", or (b) cut a
  producer cell to source a sector.

## What the hover title cannot show

- **No walk can read it.** A native `title` tooltip is drawn by the OS, so no screenshot holds it. The walker reads no `title`
  attribute: `lead-lists.json` records only each bar's visible text, e.g. "Advanced Micro Devices Inc +34.0%". The DONE WHEN's
  "the walk reads ... one hover away" therefore has no instrument. This record read the DOM attribute instead. One line in
  `walk.mjs` (`title` beside `text` in `lead-lists.json`, and the bubble `<title>` text) would close the gap.
- **No touch device can show it:** there is no hover on a tablet or phone.
- **No keyboard or screen reader reaches it.** A bar is an `<li>` with an onClick and no tabIndex. The bubbles are circles inside one
  `<svg role="img">`, which a screen reader treats as a single image, so their child `<title>`s are not exposed.
- **It is one unstyled line.** "Not served" fields read the same as served ones, in a sentence of 6-7 clauses.

## Also dispositioned: Z-S17, Z-S18, Z-S19 (the push-gate hole, Z-C-S39)

The slug gate waits on Z-S17, which was still UNDER_INVESTIGATION. Its owner remedied it (6b55a09019, 273a0d7a45). This seat's probe
of the hook at HEAD denies `HEAD:refs/heads/PROD` and `+DEV`, and admits a scratch branch (the control). All three are DISMISSED,
and no act is owed.

## Remediation (REMEDIATION_v1, same commit)

- `Z-C-S29` is REMEDIATED and DISARMED. BA's day route answers 3 of 3 inside the gateway: cold in 18.0 s, then 10.5 s and 0.5 s,
  with 6 rows each time.
- `Z-C-S35` is REMEDIATED (the CTO graded it @`d26ed82f59`).
- `Z-C-S36` is OPEN and ARMED; `Z-C-S37` is OPEN.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S36",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T18:23:00Z",
    "one_line": "On PROD portal-v2.1.195 the price-bar and chatter-bubble hovers print 'places moved not served: not ranked in the previous generation (2026-09-30)' on 62 of 94 bars and 10 of 18 bubbles, and every one of those names was ranked in that generation: scoped_amgt.read_ranking joins security_key onto every row before _join_places_moved, which matches security_key-or-ticker against prior rows that carry a security_key on only 32 of 94, so 62 never match. The overlay route keys the raw row by ticker and is right (AMD header 'down 3 places' vs AMD's own bar 'not ranked').",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "scratchpad hover_read.mjs on dist-prod-dcdc89b1 with the live payloads (18:1xZ): 94/94 bar titles, 18/18 bubble titles; 62 bars and 10 bubbles carry the not-ranked reason.",
        "lib/research/api/scoped_amgt.py read_generation_rows TRENDING_PRICE: prior 20261001T111259Z-f85fb7d5bc57 (94 rows, security_key on 32) holds all 94 current tickers; served numerics 32/32 and bubble numerics 7/7 equal prior rank minus current rank; the 62 + 10 nulls are all ranked in the prior generation.",
        "BREAKOUT_PRICE: prior 20261001T111300Z-ed033ea970e6 holds SNPS at rank 6 and AMD at rank 1 with no security_key; served rankings row: null 'not ranked'; served overlay row: +5 and -3.",
        "scoped_amgt.py :1020-1026 (join order) and :859-897 (_row_identity match); :2442 (overlay joins the raw row).",
        "tmp/ui-walk/20261002T180024Z/shots/005-AMD-US-overlay.png: 'BREAKOUT (PRICE) #4 | +12.88%, down 3 places'."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-2 v0.6: places moved is read on each bubble and each bar; a served reason is true.",
    "world_is": "A false served reason on 62 of 94 bars and 10 of 18 bubbles on PROD; two faces of one page disagree on AMD.",
    "notes": "Disarm (RESAPP's read path): match prior and current rows by ticker in _join_places_moved, or join places moved before the identity join. Not moved: the 32 right numbers, the overlay, every rank. Proof: the 62 nulls read numeric and equal prior rank minus current rank."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S37",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T18:23:00Z",
    "one_line": "FWD-2's sector field is served on no mark (0 of 94 bars, 0 of 18 bubbles): etf-classifications holds a sector on 159 of 2,841 items and on none of the 94 ranked names, whose GICS sector sits in sub_asset_class; the hover therefore prints 'sector not served' everywhere. A ruling (sub-asset class is an equity's sector) or a producer cell (source a sector) is needed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "boto3 scan of etf-classifications (ProjectionExpression ticker, sector, sub_asset_class): 2,841 items, 159 with a non-empty sector.",
        "get_item AMD, SNPS, BA, 1299: keys asset_class, classified_by, (instrument_kind), last_updated, management_style, (name), sub_asset_class, ticker, updated_by; sub_asset_class 'Information Technology' / 'Industrials' / 'Financials'.",
        "Served classification on the rankings and chatter rows: {asset_class, sub_asset_class, sector: null} on 92 of 94 and 93 of 95."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-2: every mark shows Opal's asset class, sub-asset class and sector.",
    "world_is": "Opal's table carries two levels for these equities; the third prints 'not served' on every mark.",
    "notes": "FOR THE CTO: rule the sector limb (restate, or cut a producer cell)."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S38",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T18:23:00Z",
    "one_line": "FWD-24's places-moved limb is met on PROD's code on 3 names: the walked headers print AMD 'down 3 places', BA 'up 16 places', VLO 'up 13 places', each equal to the served overlay breakout_price.places_moved and to prior rank minus current rank; with v28's other limbs, FWD-24 reads REALIZED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20261002T180024Z shots 005, 048, 100 (read by 3.0.0_SA_CVO~Z); walk DISARMED 18:06:53Z, login REFUSED 401.",
        "overlay invokes 17:5xZ: AMD -3, BA 16, VLO 13; BREAKOUT_PRICE prior ranks AMD 1 (now 4)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A met limb: no act is owed. Recorded so the CTO's FWD-24 grade can cite it.",
    "spec_asserts": "FWD-24: places moved prints wherever served.",
    "world_is": "Printed on all 3 walked headers, correct.",
    "notes": "FOR THE CTO: grade FWD-24 REALIZED."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S39",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T18:40:00Z",
    "one_line": "Z-S17 (the integrator-only push gate admitted <src>:refs/heads/<SHARED> and +<SHARED> from any seat) is remedied by its disarm_owner (6b55a09019 reorders the refspec strip; 273a0d7a45 adds the scoped TEST-ONLY portal-DEV carve-out); Z-S18 and Z-S19 are those two disarm records. This seat's own probe of the hook at HEAD: HEAD:refs/heads/PROD and +DEV DENIED, a scratch branch ADMITTED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -- .tools/hooks/never-rules-gate.sh: 6b55a09019 (12:20 local, disarm Z-S17) and 273a0d7a45 (12:40 local, closes Z-S17 limb 2), both by 1.0.0_SA_CTO~Z.",
        "Synthetic PreToolUse JSON into .tools/hooks/never-rules-gate.sh as 3.0.0_SA_CVO~Z, ~18:35Z, target C:/tmp/wk-dsgn-amgtv1-70/portal: 'push origin HEAD:refs/heads/PROD' -> deny; 'push origin +DEV' -> deny; 'push origin HEAD:refs/heads/scratch-cvoz-probe' -> no decision (admitted, the control)."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S17",
      "DSGN_AMGTV1-Z-S18",
      "DSGN_AMGTV1-Z-S19"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S17 is remedied at HEAD by its disarm_owner (6b55a09019, 273a0d7a45) and re-probed by this seat; Z-S18 and Z-S19 are the owner's disarm records of it.",
    "spec_asserts": "Only the integrator pushes a shared branch (outside the scoped carve-outs).",
    "world_is": "True at HEAD on the probed forms.",
    "notes": "No act owed."
  }
]
```

-- 3.0.0_SA_CVO~Z
