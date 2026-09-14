# ANDREW-DIRECT 2026-09-14 ~20:1xZ -- DSGN_REBRND: THE LAST EDITS BEFORE CLOSE -- THE SECURITY SCANNER BREAK; NO WHITE BLOCK INSIDE A CARD; NO "NO DATA" CARD WHILE LOADING

**Terminal:** `2.0.0_SA_COO~D`, in the page-by-page mode (record @ff6f00d0b0). **Recorded by:** `2.0.0_SA_COO~D`, in the
same turn. One message, with two screenshots.

## VERBATIM AND ENTIRE

> There are only a couple edits remaining and I think we can close down this project. 1.) [Image #10] It seems like
> the Security Scanner is broken somehow, need to understand if that is from us or otherwise how that happened. I
> also do not like his format where we superimpose a large white block inside a card, it is not the right
> coloring/presentation; it should be displayed as a soft card on the lighter color, like how we do the cards that sit
> in "Trending Topics". 2.) [Image #11] This white block card design appears several times throughout the portal.
> I've seen it in "Top/Bottom Performers" as well before it realizes it has data, i believe that same design appears
> in Macroeconomics as well. 3.) With regard to these "No data available" cards, it is not appropriate for them to
> come up by default at load, because what happens is that we do have the data and we end up flashing some ephemeral
> card about not having data while the load is occurring so it becomes a flash of bad ui card for a second or two
> before the actual information populates. I have seen this same behavior in the "Account Distribution" bell curve
> chart element in the "Model Portfolios" page; we need to stop using that pattern wherever it appears.

Image #10 shows the Security Scanner's Factor Bank panel. Its body holds a white block reading "The factor list could
not be loaded. Cause: API request failed: 403 Forbidden - {"message":"Forbidden"}". Image #11 shows Portfolio
Management's Alpha Decomposition panel, whose body holds a white block reading "No alpha factor attribution for this
portfolio yet."

## WHAT IT SETTLES

1. **Close is in sight.** "There are only a couple edits remaining and I think we can close down this project." The
   close itself stays his manual act (record @ff6f00d0b0); this sentence does not perform it.
2. **The Security Scanner break is diagnosed and explained: ours, or otherwise, and how.**
3. **No white block inside a card.** A state inside a dark panel (empty, error or loading) is a SOFT CARD on the
   lighter rung, like the Trending Topics cards: the tile rung, a faint hairline and light ink. This applies wherever
   the pattern appears, and he names the Security Scanner, Top/Bottom Performers, Macroeconomics and Alpha
   Decomposition.
4. **No "no data" card while a load is in flight.** An empty state shows only once the load has finished and found
   nothing. While the data is still arriving, the panel shows its loading state. He names the Account Distribution
   bell curve on Model Portfolios, and the rule applies "wherever it appears".

## WHAT IT DOES NOT SETTLE

It does not authorize a promote, and it does not perform the manual close. The portal freeze and the feature branch
stand.
