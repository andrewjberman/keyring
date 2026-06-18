# DECK_CLAUDE Pass-2 preview cards -- data/numbers family (Charts 13 + Statcards 4 + Stat 4)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**agent:** 0.4.2_RD_AdvisorIntelligence~C
**window:** session start (fresh ~C lane) -> now. GO from ~A relaying Andrew-direct task: draw the
data-viz Pass-2 preview cards as legible 56-wide thumbnails (tiny icon-mocks rejected). Andrew
approved each family himself.

## What shipped (all Andrew-approved, committed, --pass2 verified aligned+filled)

21 preview cards in `deck_generation/archetype_previews/`, one family/turn:
1. **Composition (3)** -- chart-pie (radial-slice pie + share legend), chart-donut-center (heavy
   highlight arc + inner ring around center hero value + `>` legend mark), chart-treemap (nested
   proportional rects). Fixed the donut's `International17%` flaw via a 21-wide legend label field.
2. **Lines/areas (3)** -- chart-line-rolling (line + dashed ref + series legend), chart-line-
   timeseries (multi-series), chart-area-stacked (true rising stacked-area contour, computed band grid).
3. **Bars/columns (4)** -- chart-column, chart-column-cme (`###` ret/`:::` vol + keyed legend),
   chart-bar-diverging (signed about zero), chart-waterfall (floating bridge).
4. **Analytical (3)** -- chart-scatter-riskreturn (`o` model / `<>` benchmark), chart-quartile-peers
   (box-whisker per period + markers at varying quartiles), chart-heatmap (`###`/`:::`/`...` density grid).
5. **Statcards (4)** -- statcards (big/label/vs/takeaway), statcards-clean, statcards-strip (5-across),
   statcards-delta (`^`/`v` + change).
6. **Stat (4)** -- stat (giant centered hero), stat-context (hero + prose), stat-hero (card + bullets),
   stat-stacked (stacked composition columns + segment legend).

Cards built via a grid-placement helper (every interior padded to exactly 54 -> card `|`+54+`|` = 56);
legend label fields sized so common labels clear values (the `International17%` collision class). Where
the renderer only fills `$N`/`$Nb` (statcards vs/takeaway, delta dir), used static structure hints
matching the existing `statcards.txt` `vs.` convention.

## chart-area-stacked engine (Andrew-direct: "fix the actual slide too")

Ground-truthed the real archetype, not the preview: composed a slide via `engine/archetypes/charts/
series.py:chart_area_stacked` -> emits `<c:areaChart grouping="stacked">` w/ 3 solid-filled series;
COM-rendered to PNG = a true filled stacked area. **No engine bug.** Andrew wanted the showcase DEMO to
read as cumulative growth, so changed `dev/scripts/showcase_charts_series.py` area data from
100%-allocation (flat top) -> cumulative $B growth (rising surface); gate PASS 0-lint/full-coverage,
COM-rendered OK. Render evidence dropped to Desktop (area_stacked_ACTUAL/CUMULATIVE_render.png).

## MCP traffic

~8 significant: GO received (~A, Andrew-direct); 3 SAVE/CC -> ~A+base per family batch; 3 verify+commit-
nudge from ~A (all 17 cards verified great, asked me to commit -- did); ACKs both ways. All RAVC loops
closed. ~A owns the renderer/convention; flagged 2 non-blocking open items back to them.

## Compiler Tools

| Tool | Result | Note |
|------|--------|------|
| comp-* | N/A | Deck-generation ASCII preview-card work -- not a portal component / data / infra change, so the comp-transform/comp-* surface doesn't apply. RD minimum (`comp-transform fields`) is for portal data components. |
| deck `prompt_view.py --pass2 --json` | PASS x6 families | the canonical fill renderer; verified every card aligned+filled with real deck data (scratch test decks). |
| PowerPoint COM export | PASS | rendered chart-area-stacked actual + cumulative to PNG for ground-truth (verify-against-artifact, not XML self-report). |
| `engine.compose --catalog` | PASS | read each archetype's content-contract to match drawings to real purpose. |
| safe-commit.sh (+ ds-gate/surface-check) | PASS x5 | surface-check OK every commit (0 critical surfaces); ~C author, explicit pathspec. |

What worked: grid-placement builder made 56-wide alignment deterministic (vs hand-counting drift);
COM render caught that the "broken" area-stacked was actually fine. What failed: nothing landed broken;
several width/gap iterations before each family rendered clean. Gap found: `slide_fields` only fills
`$N`/`$Nb` -> statcards vs/takeaway + delta direction can't field-fill (routed to ~A as optional
$Nc/$Nd extension).

## Current State (zero-context handoff)

- CLOUD HEAD includes my 5 commits: efd921a4c (10 cards) + 6c18c7e69 (showcase demo) + 11a4dad20
  (analytical 3) + 212e20420 (statcards 4) + 15ffde548 (stat 4). All local-only (RD cannot push;
  base integrates from commits).
- All 21 cards live in `deck_generation/archetype_previews/<arch>.txt`, hand-source, 56-wide, render
  via `PYTHONPATH=. python prompt_view.py <deck> --pass2`. chart-donut remains ~A's reference.
- Scratch left untracked (regenerable, `_`-prefixed): `prompts/_preview_test_{composition,lines,bars,
  analytical,statcards,stat}.deck.md` (QA fixtures) + `deck_generation/.qa_tmp/` (render PNGs/pptx).
- Nothing blocked. All assigned families complete + approved. Broker IDLE after this log.

## Next Steps

- None self-owned. React to: any keep/kill/revise on the 21 cards from Andrew / base
  [0.4.2_RD_AdvisorIntelligence]; the 2 optional items flagged to [~A] (heatmap generic-header tighten;
  $Nc/$Nd field extension for statcards vs/takeaway+delta) are their renderer call.
