# ANDREW-DIRECT 2026-09-14 ~19:4xZ-~19:5xZ -- DSGN_REBRND: NO THICK OUTLINE ON SELECTION; NO WHITE OUTLINE ON THE SIDEBAR'S ACTIVE ITEM; THE OUTLINE AND CONTAINER-GRADIENT POLICIES GO PORTAL-WIDE, STARTING WITH ADVISOR INTELLIGENCE; THEN /philosophy's 10-YEAR ASSUMPTIONS; THEN LAYERING AND TOOLTIPS UNIFIED

**Terminal:** `2.0.0_SA_COO~D`, in the page-by-page mode (record @ff6f00d0b0). **Recorded by:** `2.0.0_SA_COO~D`, in the
same turn. These are three consecutive messages.

## VERBATIM AND ENTIRE

**~19:4xZ, with three screenshots (the Peers tab, the Quarterly toggle, the Select Partner dropdown):**
> While we're here, there is a thick outline pattern that I have noticed appear on certain components, namely
> dropdowns and tab headers, but it may be elsewhere that I have yet to notice as well; we should not be using this
> thick/pointer outline when a component is selected, images attached showing examples: [three screenshots]

**~19:5xZ, with a screenshot of the sidebar's active item:**
> Also while we're here, that little white outline (pictured) [Image #8] in the sidebar is not necessary, please take
> that out.

**~19:5xZ:**
> Ok also these policies on outlines and container color gradient should be instituted across the entire portal
> frontend. Start with Advisor Intelligence and instituting it wide, which it seems like you may be doing already in
> terms of the src\main.tsx. THen we can get into the same process for the layering in the "10-Year Assumptions" panel
> on the /philosophy page (fixing both layering of row color as we did in PerformanceHeatMap on /market page) as well
> as highlighting. That layering issue should also be unified across the portal, then finally unifying the tooltips in
> the indigo as designed across the portal.

## WHAT IT SETTLES

1. **No thick or pointer outline on selection.** The focus ring draws for keyboard focus only: input modality in
   `main.tsx`, with the ring scoped in `index.css`, portal @ the focus-ring commit. It is portal-wide by construction.
2. **The sidebar's active item loses its white left rule.** This reverses the RB-s-5 Amendment 1 detail that kept it
   for SC 1.4.11. The state is now carried by the fill, the bold white label and the full-white icon. The contract
   (C8) and the issuer checker change with it.
3. **The outline and container-gradient policies are PORTAL-WIDE**, starting with Advisor Intelligence. The named
   layers move from a per-page opt-in to the whole portal.
   - This supersedes the page-level surface scope's per-page opt-in, which the PRD v0.6 preamble wrote as a migration
     switch retired when the last page opts in: his word opts every page in at once.
   - The /market-only sentiment restore (the Fear & Greed gradient) stays /market-only, because his words for it
     named that chart.
4. **The order after that:**
   1. /philosophy's "10-Year Assumptions" panel: row layering as in PerformanceHeatMap, plus the highlight states;
   2. that layering unified across the portal;
   3. the indigo tooltips unified across the portal.

## WHAT IT DOES NOT SETTLE

- **The manual close.** It remains his (@ff6f00d0b0).
- **The sidebar's keep-or-revert-to-DEV question.** The edits so far are approved; this removes one detail.
- **The portal freeze and the feature-branch confinement.** Both are unchanged.
