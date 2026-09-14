# ANDREW-DIRECT 2026-09-14 ~19:0xZ -- DSGN_REBRND /market: PASS 1 CONFIRMED; FIVE MORE REQUESTS (F&G gradient, header overlap on zoom, tooltips solid indigo, regime status as change, smooth sidebar collapse)

**Terminal:** `2.0.0_SA_COO~D`, in the interactive round-2 mode (record @78ff363894). **Recorded by:**
`2.0.0_SA_COO~D`, in the same turn. PRD v0.7's R17 acceptance requires his confirmation to be recorded, and it is
recorded here.

## VERBATIM AND ENTIRE

> This is all good, now five more requests for this page: 1.) the Fear & Greed Modal should have the original color
> gradient on the chart element; it was changed to a Blue Gradient, that is not necessary. 2.) The panel title rows need
> to not overlap even when users zoom in (ctrl & +) [Image #7], depicted in the image #7. 3.) Tooltips need
> consolidation in style. They should all have the smae look as we have in the helper tip, solid indigo no outlines,
> attached: [three screenshots] 4.) The U.S. Regime tooltips need to have a differnet convention on the "Status", it
> should be what has changed over the last Period, e.g. "Flattening" versus "Flat", or "Decreasing" (for Correlation)
> if the number is lower, etc. 5.) In the sidebar, we need a smoother action when the sidebar is closing. Currently,
> when the sidebar is collapsing from its expanded state, the icons all jumble together during the closing, that should
> be cleaned up for a smooth transition.

The three screenshots, from his `Pictures\Screenshots`:
- 150516: the HelperTip, solid indigo with no outline, which is the target look;
- 150506: the heatmap cell tooltip, dark with a 2px indigo outline;
- 150453: the Global RSI bar tooltip, dark with an outline.

## WHAT IT SETTLES

- **`/market` PASS 1 IS CONFIRMED:** "This is all good". That covers the portal commit @0aefb3c5 on
  `feature/d13-visual-elevation`: the named layers, the hover wash-out fixed, the heatmap row layers, the drill-down
  cards, the cloud's yellow family, and the delta tokens.
- **THE TOOLTIP QUESTION THAT WAS OPEN AT HIM IS ANSWERED.** Every tooltip takes the HelperTip look: solid indigo, no
  outline. His earlier "three types that vary slightly" are consolidated to one look. The state rule then binds the ink
  inside it: text follows its current background, which is indigo.
- **THE FEAR & GREED CHART TAKES ITS ORIGINAL GRADIENT.** RB-s-4's single-hue ramp is set aside for it, as the Daily
  Cloud's was at ~18:5xZ: "it was changed to a Blue Gradient, that is not necessary".
- **The U.S. Regime tooltip "Status" describes the CHANGE over the selected period**, for example "Flattening" rather
  than "Flat", and "Decreasing" for a lower correlation.
- **No panel title row may overlap its actions at any zoom.**
- **The sidebar's collapse is a smooth transition,** with no jumbling of icons mid-animation.

## WHAT IT DOES NOT SETTLE

- The sidebar's wider treatment: keep the current one, or revert to DEV. That remains his later call.
- Anything beyond `/market`, except where a shared component carries the fix, which the pass record will state.
