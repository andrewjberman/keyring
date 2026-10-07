# MDPF_SECCLASS SC10-e59-AC2 -- the firm-level Advisor Intelligence composition view, rendered on the laptop

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~16:5xZ, on `0.0.0_AB_MSTR` msg 106419 (bus 25ced3e0, from
`1.0.0_SA_CTO~DELL1`). Evidence for dell1's CVO lane, which grades. A FILE; no row is minted here. The images stay under
`tmp/ui-walk/` (gitignored) per the walker's rule; their sha256 are below.

## Answer

**Yes. On portal DEV `fc18e50b`, the firm-level view shows GLD and PHYS under Commodities with the sub-class "Metals",
and VXX under Structured with the sub-class "Hedge".**

## The render

- Build: `C:\tmp\portal-5174` at `fc18e50b`, 0 changed files (read before the walk); `http://localhost:5174` answered 200.
- Page: `http://localhost:5174/advisor-intelligence`, partner 49 Financial, tab Books, panel FIRM OVERVIEW (as of
  2026-10-05 on the page).
- Walk: `node .claude/skills/ui-walk/walk.mjs --route /advisor-intelligence --press "Books" --press "Commodities" --press "Structured"`,
  signed in as the walker; DISARM printed REFUSED. Output `tmp/ui-walk/20261007T164918Z`.

### After pressing "Commodities" (16:50:25Z)

Legend: Commodities, $1.40M, 0.1%. Panel title TOP COMMODITIES HOLDINGS. Rows as printed, ticker then sub-class:
SLV Metals 36.1%; GLD Metals 21.7%; GLDM Metals 17.6%; IAU Metals 6.8%; PSLV Metals 4.6%; DBO Oil 4.5%;
**PHYS Metals 4.1%**; PDBC Commodities 2.5%; USO Oil 2.1%; Other 0.9%.
Screenshot `shots/003--advisor-intelligence-press-Commodities.png`, 1440x4019, sha256
`57e8374afc1d3d02309bd5ae7bfee700d82ca0bc25a17ee88fc1d9ffa5e876ac`.

### After pressing "Structured" (16:50:40Z)

Legend: Structured, $25.9M, 1.3%. Panel title TOP STRUCTURED HOLDINGS. Rows as printed:
**VXX Hedge 82.1%**; a Barclays note, Hedge, 7.4%; a JPMorgan note, Hedge, 3.3%; JHQTX Hedge 1.6%; JEPI Options Income
1.3%; a BBVA note, Hedge, 1.0%; a Morgan Stanley note, Hedge, 0.9%; BMAR Hedge 0.4%; SPYI Options Income 0.4%;
Other 1.0%.
Screenshot `shots/004--advisor-intelligence-press-Structured.png`, 1440x4019, sha256
`97208c095952faa7f200a4dd85536c9f92bc989b674aaa9dfc6718b791652308`.

Both panels were read from a full-resolution crop of the screenshot, not from a reduced image.

## The served data behind the page (read directly, this seat)

`s3://opal-data-bd/platinum/firm/mix_summary.json`, LastModified 2026-10-07T05:49Z, data_as_of 2026-10-05:
- GLD: asset_class_canonical `commodities`, sub_asset_class_canonical `Metals`, class_source `etf-classifications`.
- PHYS: `commodities`, `Metals`, `etf-classifications`.
- VXX: `structured`, `Hedge`, `etf-classifications`.

## What this does not show

- It is the FIRM view. No client page and no advisor Book view was reached (the 403 of the earlier attempt,
  `MDPF_SECCLASS_SC10_E59_RENDER_ATTEMPT_20261007.md` @b207496c40). The three named clients were not rendered.
- The candidate's change is in `ConsolidatedOverviewPanel.tsx` and `composition.ts`. This seat did not establish
  which component draws the firm panel's sub-class word, so the render shows the page agrees with the served
  sub-class; it does not by itself show the changed lines drew it.

## Seen on the same page

- With Commodities or Structured selected, the quarter strip reads Q3 '26 $1.51M (or $28.4M) and $0 for Q2 '26 and
  Q1 '26.
- The Assets Overview chart above the tabs draws its axes and no bars after a press in the Books tab; it drew four
  bars on first load.

-- 3.0.0_SA_CVO
