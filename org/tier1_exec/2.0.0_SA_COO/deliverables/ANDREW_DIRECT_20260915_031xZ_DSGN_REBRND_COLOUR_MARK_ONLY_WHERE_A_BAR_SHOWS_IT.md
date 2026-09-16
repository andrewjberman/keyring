# ANDREW-DIRECT 2026-09-15 ~03:1xZ -- DSGN_REBRND: NO COLOUR BESIDE AN L1 CATEGORY WHEN THE BAR SHOWS L2; APPLY IT TO THE TOTAL ASSETS COMPONENT

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. These are two
consecutive messages, received while the Tax SMA brief (~03:0xZ word) was being written. They are about the Asset
Category Views breakdown dialog as it stands at portal 208848cb: the bar is drawn at L2 (the members), yet every L1
bucket header still carries its own coloured square.

## VERBATIM AND ENTIRE

> On the modal popup, there is no need to put colors next to the L1 categories, because we only show L2 color bar, so
> it is confusing.

> Keep that in mind for that Model Portfolios total assets component

## WHAT IT SETTLES

1. **In the breakdown pop-up, an L1 category carries no colour mark when the bar shows its L2 members.** A colour with
   no matching segment on screen confuses the reader.
2. **The same principle binds the Model Portfolios Total Assets component** (the one-card Asset Category Views: pie,
   tiles and their hover detail).

## HOW 2.0.0_SA_COO~D APPLIES IT, AND SAYS SO

He states the principle through one instance. This seat applies it as ONE rule across the component: **a colour mark
is a legend entry.**
- A dot or square appears ONLY beside an item drawn as a segment of the bar (or pie) on screen.
- A bucket drawn as its members has no square. Its members carry the dots.
- A bucket drawn as itself (its members carry no amounts) keeps its square.
- An item in no drawn bar has no mark: where no bar is drawn at all, or a $0 bucket.
- The tile's own mark stays, because it is the legend of its pie slice.
- The tile's L1 row dots show only when the tile's L1 bar is drawn.

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote. The portal
freeze and the feature branch stand.
