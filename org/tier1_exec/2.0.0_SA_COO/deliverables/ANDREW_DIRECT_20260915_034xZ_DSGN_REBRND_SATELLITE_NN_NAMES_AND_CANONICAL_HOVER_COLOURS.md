# ANDREW-DIRECT 2026-09-15 ~03:4xZ -- DSGN_REBRND: SATELLITES ARE "SATELLITE ##"; A HIGHLIGHTED MODEL / ETF / SATELLITE NAME TAKES THAT ASSET'S CANONICAL COLOUR

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. It opens "a
couple targeted frontend fixes" on the Positioning page, Satellites toggle. It is about the Positioning Summary's
column-header names, which are the modal triggers built at 1fd2769a / efef8610: dotted underline, arrow, and a lilac
hover.

## VERBATIM AND ENTIRE

> I'm going to ask you for a couple targeted frontend fixes on the "Satellites" toggle view on the "Positioning" page.
> We don't need to call them "Opal Satellites", takes too much space, they should just be "Satellite ##", e.g.
> Satellite 60. THat should give us more space, also make sure that when they are highlighted, and when Models or ETFs
> names are highlighted (what you click to pop up the modal) make sure that they use their proper canonical colors as
> displayed on the "Positioning" page for that asset.

## WHAT IT SETTLES

1. **Satellites display as "Satellite ##"** (for example "Satellite 60"), not "Opal Satellite ##". The reason is space.
   This is a display label only: the data's own name, and any key or filter that reads it, is unchanged.
2. **A highlighted modal trigger takes its asset's canonical colour, on every mode.**
   - "Highlighted" means hovered or keyboard-focused.
   - The triggers are the Model, ETF and Satellite names on Positioning that open their pop-up.
   - The colour is the one the Positioning page already shows for that asset. It replaces the single lilac hover
     (hsl(254 100% 76%)) set at 1fd2769a.

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote. The portal
freeze and the feature branch stand.
