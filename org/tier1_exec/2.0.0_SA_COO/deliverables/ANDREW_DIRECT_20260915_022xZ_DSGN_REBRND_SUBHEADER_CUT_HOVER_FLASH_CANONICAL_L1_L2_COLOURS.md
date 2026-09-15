# ANDREW-DIRECT 2026-09-15 ~02:2xZ -- DSGN_REBRND: CUT THE CATEGORY SUBHEADER; FIND THE HOVER DOUBLE FLASH; ONE CANONICAL COLOUR PER L1 AND L2, AND NO BAR THAT HIDES ITS CONSTITUENTS

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. It arrived
while the hovered-tile token change (portal 3723d23d, on 1.0.0_SA_CTO 96831) was being committed. He attached a
screenshot of the SMAs breakdown dialog on live data:
- ONE L1 bucket, "ETF Strategies", $21.68M;
- a full-width bar in a single light blue above it;
- beneath it, two L2 members with their own dots: "Dividend SMA" $17.53M and "Opal Equity Growth SMA" $4.15M.

## VERBATIM AND ENTIRE

> Ok first delete this from the subheader ":model portfolios, SMAs, and client-directed holdings. Hover a category for
> its breakdown; open it to see its constituents." Second, FIgure out why the card double flashes sometimes when
> hovering, doesnt feel premium. Third, this color schema where you define the light blue as the main bar, and show a
> full blue bar, but that blue bar technically is composed of two assets, this is bad design: [Image #12]. We need to
> rectify that and just show the two relevant colors for the two subject securities. I think it might be a good idea
> to pick a canonical color for each L1 and L2 drill so regardless what assets are displayed by a view, they are always
> consistent, not just ordinally depicted.

## WHAT IT SETTLES

1. **The Asset Category Views subheader loses everything from the colon on.** It reads "Opal-managed assets in total
   and by category."
2. **The hover's double flash is a defect to diagnose and fix.** The bar is that the hover "feel premium".
3. **A bar never shows one colour for something made of several holdings.**
   - In his screenshot, the breakdown bar shows the two SMAs in their own two colours, not one bucket colour.
   - The bar's colours are the colours of the rows listed beneath it.
4. **Every L1 bucket and every L2 member has ONE canonical colour**, keyed by its name, so it is the same in every view
   and at every scope.
   - Position in a list never sets a colour ("not just ordinally depicted").
   - **This overrides the standing code rule that L1 buckets stay positional.** That rule came from 2.0.0_SA_COO~Z 14112
     s.3, which said "do NOT invent a palette". He has now asked for the palette by name.

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote. The portal
freeze and the feature branch stand.
