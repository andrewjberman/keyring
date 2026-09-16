# ANDREW-DIRECT 2026-09-15 ~02:1xZ (2026-09-14 ~10:1x PM ET) -- a class no displayed book holds shows no row anywhere; the Satellites mode still renders broken

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in-session, with two screenshots of the POSN view on `localhost:5173`
(portal `dd1d33c6`). **Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## HIS WORDS -- VERBATIM AND ENTIRE

> "We are now seeing this [Image #2] wwhich is great that we can now establish the structured asset class and everything
> displays right in the models view. The one issue I have with it, is if none of the models/ETFs/satellites have a given
> asset class (e.g. Alternatives) then no Alternatives row should be shown. In the context of the Models view, becuase
> there is Structured exposure, but no Commodities or Alternatives Exposure, that means that commodities and alternatives
> weights should not appear in that colored bar section of the characteristics. With that said, the Satellites section is
> still broken; not displaying data [Image #3] showing all the floats in this case. and no characteristics or performance
> in the "Holdings Breakdown" panel."

Screenshots: `Screenshot 2026-09-14 221346.png` (Image #2, Models mode, Portfolio view, details expanded),
`Screenshot 2026-09-14 221235.png` (Image #3, Satellites mode).

## READING -- stated narrowly

1. **Confirmed (his):** the Models mode now shows Structured (Long-Term 1.5%, Ultra Long-Term 2%) and displays right.
2. **Requirement (his), widening the legend ruling of ~00:4xZ (record @85621749e2):** a class that no book in the view
   holds shows NO ROW -- not in the legend, and not in the expanded details' coloured ASSET CLASS rows (Image #2 shows
   `Commodities (%)` and `Alternatives (%)` rows of all zeros under `ASSET CLASS (5)`). "The view" is read as the books
   the current mode displays (his example is the Models view); order and colour of the classes that ARE shown are unchanged.
3. **Report (his):** the Satellites mode is still broken -- the summary labels print raw floats, the bars do not render
   the full book, and the Holdings Breakdown panel shows no characteristics and no performance. Causes, pinned in the
   portal code and the served data, are in the rows filed on the POSN channel that cite this record.
4. Scope: Positioning page only (PRD v0.8 `C-POSITIONING-ONLY`). Mid-round the decomposition is frozen; findings go to the
   surprise channel and into the round-5 analysis the COO recuts from.
