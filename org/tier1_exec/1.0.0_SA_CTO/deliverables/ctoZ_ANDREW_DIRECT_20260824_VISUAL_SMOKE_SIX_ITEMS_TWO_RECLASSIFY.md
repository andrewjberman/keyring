# ANDREW-DIRECT 2026-08-24 ~23:20Z -- THE VISUAL SMOKE: SIX ITEMS, AND TWO OF THEM RECLASSIFY ON MEASUREMENT

**Seat:** `1.0.0_SA_CTO~Z` (site Z) · **Surface:** the CTO~Z terminal, after he smoked
`localhost:5175/positioning` against tonight's 23:00:45Z publish · **Recorded + broadcast same turn**
(5758-5763, 6/6 DELIVERED).

## HIS WORD, VERBATIM AND COMPLETE

> *"I just visual smoked, it's off to a decent start but still no data for DIVZ and IDVZ. Also no
> performance data for PFDE or PFOE. Additionally kind of patchy response on yield column, have most
> of it but missing key ones like Amazon AMZN for example. Also don't need "# of ETFs" on frontend,
> should be "# of Securities". Also still need to figure out GICS + order by canonical Sector/GICS
> ordering (see how the frontend handles it in "Portfolio Management" (Yang was very adamant on how
> secrots should be ordered), then this order should be lighter to darker in color on the "Sub-Asset"
> Field."*

## MEASURED ON THE LIVE SERVED PAYLOAD BEFORE ROUTING -- denominator 114 holding rows, 2 funds

| # | his item | measured | classification | owner |
|---|---|---|---|---|
| 1 | no data for DIVZ/IDVZ | `holdings_status: book_only`, `num_holdings: 0`; **book-level yield/cost/beta/aum PRESENT** | **EXPECTED** -- T-1 = Friday; resolves at tomorrow's 13:00Z fire. **"No HOLDINGS", not "no data"** | none |
| 2 | no performance for PFDE/PFOE | `1D` **109/114**; `WTD MTD 1M QTD 1Q YTD 1Y` **0/114 each** | **REAL DATA GAP, total not patchy.** Producer computes one day only; `history_topup` not feeding period returns | DS~Z (build) |
| 3 | yield patchy, AMZN missing | **80/114 populated (70%)**; nulls = AMZN BA AMD MNST SNDK PLTR CIEN INTC CNC TSLA INCY ANET; populated = NVDA 0.47 AAPL 0.35 MSFT 0.75 AVGO 0.71 GOOGL 0.26 | **RECLASSIFIES -- likely CORRECT nulls** (non-payers), and the defect is that a correct null renders identically to a failed fetch | read first, then DE~Z **or** DS~Z |
| 4 | "# of ETFs" -> "# of Securities" | -- | label change | DE~Z |
| 5 | GICS + canonical sector order | `sub_asset_class` is **already GICS**: 10 of 11 sectors + Cash + **1 `None`** (`2602335D` / TPG Inc). Real Estate absent from today's data only | **ORDERING + industry-group sub-level**, not a vocabulary change | DE~Z + DS~Z |
| 6 | light->dark colour on Sub-Asset | -- | **REOPENS colour, and does NOT contradict DE~Z's ruling** (below) | DE~Z |

## THE TWO ITEMS THAT RECLASSIFY, AND WHY IT MATTERS OPERATIONALLY

### Item 3 -- one symptom, two opposite remedies

The null set is dominated by companies that do not pay a dividend and the populated set carries
plausible yields for known payers. **His own example -- AMZN -- is the canonical non-payer.**

⛔ **I did NOT assert that from memory, and nobody should.** It is one Bloomberg field read
(`EQY_DVD_YLD_IND_NET`) on three or four of the null names, and it **assigns the work**:

- **correct nulls** -> the remedy is a **DISPLAY CONVENTION** (a dash meaning *does not pay* vs blank
  meaning *unknown*) -- **DE~Z's plane**
- **actually missing** -> a **pull gap** -- **DS~Z's plane**

**Two opposite remedies behind one symptom, so the read comes first and the rest waits on it.**
This is tonight's recurring class arriving on the serving surface in front of him: **a null quietly
becoming a value.**

### Item 6 -- his instruction does not overturn DE~Z's ruling; it is outside what they ruled on

DE~Z ruled against **CATEGORICAL colour over ~24 UNORDERED values against an 8-slot palette**, and
that reasoning holds. He specified a **SEQUENTIAL RAMP OVER AN ORDERED AXIS** -- a different
encoding, which handles many values *precisely because the order carries the meaning*. Their 4-site
blast radius and the `getSubAssetTextColor` 8-entry allowlist remain the live build constraints.

**Recording it this way deliberately: "he reversed DE~Z" would be wrong and would teach the next
seat that a well-argued determination gets overruled on taste.** It did not; the question changed.

## A ZERO OF MINE THAT MUST NOT BE READ AS ABSENCE

`comp-find -i "SECTOR_ORDER|sectorOrder|SECTOR_SEQUENCE|canonicalSector"` over `portal/src` =
**0 hits across 415 files.** **He states Portfolio Management already handles sector ordering -- so
my PATTERN missed it, not the estate.** Flagged to DE~Z in those words. Reuse what PM does
(build-ladder rung 2); do not re-coin an ordering.

## SEQUENCING

Items **4, 5, 6** are frontend-only and run in parallel with the provenance/conventions deploy work
targeting 13:00Z. Item **2** is a producer build. Item **3** is a one-field read that assigns its own
owner. Item **1** needs nothing.
