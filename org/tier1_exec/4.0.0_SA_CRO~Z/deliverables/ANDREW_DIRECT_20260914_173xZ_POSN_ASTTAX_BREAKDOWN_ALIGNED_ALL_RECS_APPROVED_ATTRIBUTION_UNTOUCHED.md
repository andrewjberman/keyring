# ANDREW-DIRECT 2026-09-14 ~17:3xZ (~1:3x PM ET) -- POSN_ASTTAX breakdown ALIGNED: "All recs approved", and Attribution is NOT touched

**Author:** 4.0.0_SA_CRO~Z (Chief Research Officer, site-Z lane)
**Channel:** Andrew at the 4.0.0_SA_CRO~Z terminal, in-session, answering the eight open items A-H of
`1.0.0_SA_CTO~Z`'s close-out breakdown v0.3 @888a9d281b s.5, put to him as cards by this seat (~17:3xZ) with
the breakdown's recommendations, one difference noted (card B: VNQ sub-asset = Real Estate; CTO rec left it as-is).
**Received:** ~17:3xZ; clock read at the commit of this file.

## VERBATIM, ENTIRE (the phrasing is the ruling)

> "All recs approved. Keep in mind that attribution, for now at least, is staying to just Equities and Fixed
> Income on asset classes, because those are the only ones Yang uses, and we stick to his layout. Eventually
> that may change, but need to keep in mind that the work we're doing here is very much contained to
> "Positioning", we do not touch "Attribution""

## THE CARDS HE ANSWERED (this seat's text, so the word binds to a known question)

| card | the call as put | rec approved |
|---|---|---|
| A | "Summed" = BD's total per ticker across the satellite's sleeves; Yang's copy NOT added on top | yes |
| B | Sub-asset labels for the rest of the 12: Metals = GLD, IAU, SLV; Hedge = VXX, VIXY, UVXY, QBER; DBC/GSG/USO/PDBC keep current (Commodities / Oil); VNQ -> ? | as listed, **and VNQ = Real Estate** (this seat's rec, approved) |
| C | Retag set = the 12; BIPC stays Equity | yes |
| D | Allow F4: three one-line guards on the Attribution page | rec was yes -- **OVERRIDDEN by his qualifier, see below** |
| E | Cut `is_hedge()` and the `bd-securities` reconciliation from this close-out | yes |
| F | Done = backend deployed + frontend built and committed behind the freeze, promote on his separate word; the labelled-zero benchmark widens the 2026-09-13 deploy approval to `yang-generate-allocation-summary` under one sign-off | yes |
| G | Alignment on this breakdown releases the worker gate; `2.0.0_SA_COO~Z` issues the cells | yes, "once A-F are answered" -- they now are |
| H | Bloomberg pull: (a) land the FUNDS edit today, first data 09-15; or (b) land it AND run a one-off pull today (download-class, his per-use word) | **(b)** -- the per-use word for the one-off pull is this "approved" |

## WHAT THIS SEAT READS, STATED AS A READING AND NOT ADJUDICATED

- **Card D is OVERRIDDEN by the qualifier, and F4 is OUT.** "All recs approved" alone would have admitted the
  three Attribution guard lines; his next sentences are later and more restrictive -- *"we do not touch
  'Attribution'"* -- and they name the exact surface F4 touches. Latest + most-restrictive binds: **round 5 has
  EIGHT cells (B1-B4, F1-F3, R1); F4 is cancelled; Attribution stays on Yang's two-class layout, Equities and
  Fixed Income, "for now at least".**
- ⚠ **THE CONSEQUENCE F4 EXISTED TO PREVENT IS NOW AN ACCEPTED STATE, and it is written down so nobody
  re-files it as a defect:** after R1 retags VXX to Structured, Attribution's hardcoded two-class list
  (`SelectionTab.tsx:321` and two siblings) will not iterate a Structured group, so VXX's row (LT 1.5%, ULT 2.0%
  in Yang's models) will not appear under either of Attribution's two class groups while its weight stays in
  the totals. Under his word that is Attribution's known state until "eventually that may change". It is
  surfaced back to him in the same reply as one line, not assumed silently.
- **Card G:** the worker gate is RELEASED by this word, on the breakdown as amended by this same word (F4
  removed). The amendment is his own, so s.4's "any deviation from s.3 comes back to Andrew" is satisfied by
  construction.
- **Card H (b):** the one-off Bloomberg ETF pull today is approved by his per-use word here. The FUNDS edit
  itself remains `1.0.0_SA_CTO~Z`-gated (deploy on this box's working tree) and subject to the CTO's in-progress
  read of what `FUNDS` feeds (fund-specific `FUND_D` history pull, manifest "funds" list -- msg 22859).
- **Card B:** VNQ `sub_asset_class` -> `Real Estate` (today `US Large Cap`; its `sector` already reads
  `Real Estate`).

## WHAT THIS RECORD DOES NOT DO

It amends no PRD, cuts no cell, signs nothing, deploys nothing. The L4 act (PRD v0.7) is `1.0.0_SA_CTO~Z`'s; the
L5/L6 cut is `2.0.0_SA_COO~Z`'s; the FUNDS edit and the one-off pull are gated and landed by whom the CTO names.

## Broadcast

Same turn, MCP to `1.0.0_SA_CTO~Z`, `0.0.0_AB_MSTR~Z`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z` (per-recipient result
in the session log).
