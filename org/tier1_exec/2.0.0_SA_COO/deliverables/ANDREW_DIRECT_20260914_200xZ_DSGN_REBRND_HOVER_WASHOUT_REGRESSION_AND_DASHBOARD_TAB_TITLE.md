# ANDREW-DIRECT 2026-09-14 ~20:0xZ -- DSGN_REBRND: THE HOVER WASH-OUT CAME BACK (Trending Topics, Top/Bottom Performers, PerformanceHeatMap); THE DASHBOARD TAB READS "Opal Capital | Dashboard"

**Terminal:** `2.0.0_SA_COO~D`, in the page-by-page mode (record @ff6f00d0b0). **Recorded by:** `2.0.0_SA_COO~D`, in the
same turn. These are two consecutive messages, received mid-turn while the portal-wide move (record @5a707c0b43) was
uncommitted on the feature branch.

## VERBATIM AND ENTIRE

**~20:0xZ, with a screenshot of the Bullish Drivers card on hover (near-white ground, white text):**
> Also just noticed that on these Card elements in Trending Topics we still are not properly converting the text to
> dark, so it gets washed out as you can see  [Image #9]. This is effecting multiple other card elements across
> Top/Bottom Performers, the PerformanceHeatMap, and others, so it seems like maybe something regressed during an
> edit.

**~20:0xZ:**
> Also while we're here, the dashboard should mirror the tab structure as the website. The website appears in tab as
> "Opal Capital | Investment Platform". The dashboard tab should read as "Opal Capital | Dashboard".

## WHAT IT SETTLES

1. **The wash-out is a regression, and it is this seat's.**
   - Moving the named layers from the per-page attribute to `:root` (the portal-wide word, @5a707c0b43) lost the
     cascade to `design/themes/opal-capital.css`.
   - That theme sets `--semantic-background-hover: 218 21% 93%` under `:root[data-theme="opal-capital"]`. That
     selector's specificity is 0,2,0, which beats a bare `:root` at 0,1,0. So the hover rung went back to near-white
     under white ink.
   - The per-page attribute had worked only because it sat on a descendant element.
   - The remedy puts the layer block on `body`: a declaration there overrides what `html` carries for every
     descendant, whatever the selector weight or load order.
   - His sentence names no new state rule. It is FWD-13 ("text follows its current background") failing on the ground
     it already governs, so the fix restores the dark-rung hover rather than flipping the ink.
2. **The browser tab title is "Opal Capital | Dashboard"** (portal `index.html` `<title>`), mirroring the website's
   "Opal Capital | Investment Platform". Nothing else in the portal sets `document.title`.

## WHAT IT DOES NOT SETTLE

It says nothing about the manual close, the sidebar keep-or-revert-to-DEV call, or a promote. The portal freeze and the
feature branch stand.
