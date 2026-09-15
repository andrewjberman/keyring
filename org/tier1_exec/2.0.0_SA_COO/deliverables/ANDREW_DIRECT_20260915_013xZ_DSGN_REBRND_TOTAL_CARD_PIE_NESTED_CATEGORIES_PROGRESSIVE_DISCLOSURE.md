# ANDREW-DIRECT 2026-09-15 ~01:3xZ -- DSGN_REBRND: THE TOTAL CARD BECOMES A FILLED PIE, THE THREE CATEGORY CARDS NEST INSIDE IT, AND THEIR L1 DETAIL APPEARS ON HOVER

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. It is his
review of the Total Assets card built on his ~01:2xZ word (record @11fe71294d, portal 5d52df87). It arrived while
the category colours were being moved onto data-palette tokens (1.0.0_SA_CTO 96809).

## VERBATIM AND ENTIRE

> I like it but the design isnt quite right. I think the total assets should be described as a filled in pie chart
> and the 3 smaller cards should somehow be nested inside the one main card with hover options where when you hover
> the L1 detail appears with a click through or something. It's too disconcerting to see 1 wide card and three
> smaller cards all with figures on them, there needs to be progressive disclosire for it to work.

## WHAT IT SETTLES

1. **The total is drawn as a filled pie chart** (not a donut, not a split bar), with one slice per category.
2. **The Models / SMAs / Client cards nest inside the one Total card.** There are no longer separate cards beneath
   it.
3. **Progressive disclosure.**
   - At rest, each nested category is brief.
   - On hover, its L1 detail appears, with a click-through.
   - The click-through opens the existing breakdown pop-up, which is where L2 lives.
4. **The reason is his, and it is the test:** one wide card plus three smaller cards "all with figures on them" is too
   much at once.

## HOW 2.0.0_SA_COO~D READS "OR SOMETHING", AND SAYS SO

- **At rest, each nested tile shows:**
  - its colour, name and one-line subheader;
  - its amount, at a smaller size than the total;
  - its share of the total.
- **On hover or keyboard focus, the same tile shows:**
  - its L1 bar and rows;
  - a "View breakdown" link.
  The tile keeps a fixed height, so nothing on the page moves.
- **Clicking a tile or a pie slice opens the category's pop-up.**
- **Hover is linked both ways.** Hovering a slice opens that tile's detail, and hovering a tile highlights its slice.

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote. The portal
freeze and the feature branch stand.
