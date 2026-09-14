# ANDREW-DIRECT 2026-09-14 ~19:5xZ (~3:5x PM ET) -- Structured is a pink base; every volatility / options / overlay asset groups there, whatever its prior home

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in-session, answering this seat's note that the portal's existing `Hedge`
sub-asset colour sits in the Fixed Income green gradient while PRD v0.7 files Hedge under Structured.
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## HIS WORDS -- VERBATIM AND ENTIRE

> "Yeah "Structured" is going to be a pink base, as all volatility/options/overlay etc assets will be grouped into there,
> regardless if its a Fixed Income or an Equity Hedge or etc."

## READING -- stated narrowly

1. **Colour:** Structured is a PINK base, and its sub-assets render in the pink family. The portal's existing
   `SUB_ASSET_COLORS` keys that belong to Structured -- `Hedge` (today `PALETTE.green900`, inside the Fixed Income gradient)
   and `Volatility` (today `PALETTE.blue900`, inside the Equity gradient) -- move into the pink family. This resolves F1's
   refused criterion `V5-AC2` (`TO-V5-1`): the key cannot be "added" because it exists; per this word it is RE-BOUND.
2. **Membership:** "all volatility/options/overlay etc assets will be grouped into there, regardless if its a Fixed Income
   or an Equity Hedge". PRD v0.7 `C-RETAG-SET` has 4 Structured members, all derived from `sub_asset_class == Volatility`
   (VXX, VIXY, UVXY, QBER -- QBER is today `fixed_income`, which his "regardless if its a Fixed Income" confirms). Whether
   his word reaches FURTHER rows (options / overlay / hedged sub-assets not labelled `Volatility`) is MEASURED against the
   served table before any ruling on the set; see the census below.
3. **Spec basis:** v0.7 already binds `Hedge` as a `sub_asset_class` under `Structured` (`C-SUB-ASSET`) and Structured as pink
   (`C-COLOURS`). A Hedge swatch in the Fixed Income green contradicts that; re-binding it is within v0.7 and needs no PRD
   bump. A change to the retag MEMBERSHIP would be a different matter (spec-level).

## THE CENSUS -- does his word reach beyond the four `Volatility` rows?

`dynamodb scan etf-classifications`, projection ticker / asset_class / sub_asset_class / name, 2026-09-14 ~19:5xZ:
**285 rows read, Count 285 = ScannedCount 285, no LastEvaluatedKey** (one page, whole table); negative control
`ZZZ_NOSUCH` 0. **31 distinct `sub_asset_class` values.**

- **No sub-asset is named for options, overlay, buffer, collar or hedge.** The only volatility-shaped value is
  `Volatility`, on exactly 4 rows -- VXX, VIXY, UVXY, QBER -- all already in `C-RETAG-SET` as Structured.
- **By NAME, one genuine candidate outside the four:** `JEPI` -- JPMorgan Equity Premium Income ETF, served
  `equity / US Large Cap`, an equity book with an options (call-writing) overlay. Whether "options/overlay" reaches it is
  put to Andrew; not ruled here.
- **A name that must NOT be pulled in:** sub-asset `Structured Credit` (JAAA, a AAA CLO ETF; LONZ, senior loans) is Fixed
  Income credit, not options or volatility; the shared word "Structured" is a collision, not a membership signal.
- The remaining pattern hits matched on "income" or "protected" (DIVZ, IDVZ, DFCF, DFSD, VNLA, JPST, VTIP) or on
  infrastructure (BIPC, already ruled Equity) and carry no options exposure by their served classification.

**Does JEPI reach the Positioning page at all?** No. 0 occurrences in the Cottonwood satellite components
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_SOURCE_SATELLITE_COMPONENTS_20260911.md`, the 25-ticker necessary-data file
U4 parsed with GLD and VXX present) and 0 in Yang's served `positioning_data.json` (`data_as_of 2026-09-11`; controls in the
same read: VXX 5 occurrences, GLD 0, `ZZZ_NOSUCH` 0). So its classification changes nothing the page serves today. The
retag set stays the twelve unless Andrew moves JEPI.

## THE COLOUR SURFACE -- F1's branch (`portal` @`c475e31e70`, `src/lib/chartColors.ts`)

- `SUB_ASSET_COLORS` (`:288`): `'Hedge'` = `PALETTE.green900` at `:298`, inside the "Fixed Income -- Green gradient" block;
  `'Volatility'` = `PALETTE.blue900` at `:311`, inside the "Equity -- Blue gradient" block. **Both move into the pink
  family per this word.**
- `PALETTE` carries only two pinks: `pink500` (`:61`, the Structured class base, `ASSET_CLASS.structured` `:119`) and
  `pink600` (`:62`). The file's own convention keeps a class base out of its sub-asset gradient ("base is green-500, avoid
  re-using it"), so a pink sub-asset gradient needs pink tokens beyond `pink500`.
- Two other maps name volatility-shaped keys and are OUT of scope: `MIX_PIE` (`:407`, `structured_notes` orange) and
  `RISK_FACTOR_COLORS` (`:488`, a risk FACTOR named Volatility, amber). The Positioning page imports neither
  (`HoldingsTab.tsx` takes `PALETTE, ASSET_CLASS, SUB_ASSET_COLORS, getSubAssetTextColor, PERF`; `PositioningSummary.tsx`
  takes `ASSET_CLASS, PALETTE`; `bookSet.ts` takes `PALETTE`).

## ROUTED

`2.0.0_SA_COO~Z` (issuer of `TO-V5-1`): `V5-AC2` is resolvable within v0.7 -- `Hedge` and `Volatility` are RE-BOUND into the
pink family on tokens distinct from the `pink500` base, minting pink tokens as needed. No retag-set change.
