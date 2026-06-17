# 0.4.2_RD_AdvisorIntelligence~B — DECK_CLAUDE.FANOUT-B: Panels + Grid archetype variations

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-06-17  **Driver:** GO from 0.4.2_RD_AdvisorIntelligence (base, deck-system owner) — Andrew-direct fan-out. TO: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/DECK_CLAUDE.FANOUT-B.panels-and-grid-archetypes.md`.

## Objective
Bring Panels + Grid to 4 variations each (build the NEW ones; cores exist) in my two owned modules `engine/arch_panels.py` + `engine/arch_grid.py`. Gate to 0 lint + full coverage, then COM visual-QA every slide. Shared files (compose.py/registry.py) pre-wired — not touched.

## Work Completed (IMPLEMENT)

### Panels — `engine/arch_panels.py` (3 new -> 4 with core)
- **panels-icon** — vertical rows, each a purple rounded-square badge with a numbered geometric mark (F6) + bold navy heading + body (slides 8/86, board B5/B12). `filled=True` option = N solid dark->light cards with circle badges + toned heading/body (slide 90). Both modes built + QA'd.
- **panels-bordered** — colored outline (stroke-only) + header band (ramp) + body as bullets OR labeled What/How sub-sections + an optional tinted (cool-grey) footer tier (slide 64, board B6).
- **panels-formula** — A + B = C, three cards + centered purple +/= operators in equal gutters (D3a). The old core `formula`, folded in.

### Grid — `engine/arch_grid.py` (3 new -> 4 with core)
- **grid-outline** — stroke-only rounded-rect tiles (no fill) + thin purple accent bar + heading/desc; partial last row centers.
- **grid-matrix** — positioning/rating matrix: categories x cols (Underweight/Neutral/Overweight), a navy filled circle marks each row on a LIGHTBG track; supports TWO side-by-side (slide 30). The most distinctive build.
- **grid-badge** — 2x2 (NxM) icon-card grid: LIGHTBG card + navy circle badge (numbered mark) + heading + body (board B12); partial last row centers.

Correct-by-construction vs DESIGN_BIBLE: A1 palette + Lato; >=0.5in margins; D7 radius 0.10in (local `_outline` helper replicates `_radj` for stroke-only rounded rects); true circles via C.circle; D8 uniform sizing via uni_pt; D3 symmetry (equal width/gutters); every slide carries a graphic (D9). Each variation `register()`-ed (family Panels/Grid).

### Showcase + gate (VALIDATE)
`dev/scripts/showcase_panels.py` + `showcase_grid.py` — one slide per variation (core + 3), eyebrow-labeled, sample Opal content, `Deck()` + `d.finalize()`. Both print **GATE PASS: 0 lint + full coverage (4/4 need-blocks, 5 slides)**. No consecutive identical tags (D10).

### Visual-QA — the product
Rendered both showcases to per-slide PNG via PowerPoint COM (`dev/scripts/render_png.ps1`) and READ every slide (10 total + the filled-icon probe). All clean: on-brand, no white-on-white, no orphans, correct alignment, no footer collision, 60-30-10 honored, motifs fit. Zero re-render fixes needed. The `panels_icon(filled=True)` path was lint-checked + COM-rendered + read separately (slide-90 reproduction clean).

## Compiler Tools
No comp-* tools run. Justification: standalone `deck_generation` tooling (Python composer/linter + showcase scripts) — no data-pipeline, cloud/infra, or frontend change, so Rule-20 graph-check + comp-pipescript/comp-iam/comp-surface are N/A (`<compiler_tools_mandate>` in the TO confirms standalone). Verification was the purpose-built `design_lint.py` [AUTO] gate + fidelity coverage + PowerPoint-COM visual-QA — the correct verify-channel for this artifact class. ruff (gate pin 0.15.11, --extend-select FA) clean on all 4 files (0 violations); py_compile clean.

## Current State (handoff)
- Committed `816ae5e79` (4 files: arch_panels.py, arch_grid.py, showcase_panels.py, showcase_grid.py) under ~B author line; `5137d8b9e` flips the TO `<status>` to complete. Pushed to origin/CLOUD.
- `python -m engine.compose --catalog`: **Grid (4)** complete (grid + grid-outline + grid-matrix + grid-badge). **Panels (5)** — `panels` + standalone core `formula` + my 3. panels-formula ABSORBS the core `formula`; landing the AC'd Panels=4 needs ONE line removed from `compose.py`'s register block (the standalone `formula` row). compose.py is the base RD lane — I cannot touch it; flagged to base RD (RAVC2 + commit body).
- Modules are ruff-clean (no E701/E702 dense one-liners) — the TO's E701 gate-note was not needed; no bypass used.

## Next Steps
- [0.4.2_RD_AdvisorIntelligence] De-register the standalone `formula` row in `compose.py`'s register() block (panels-formula absorbs it) -> catalog Panels=4. Then integrate all RD~X modules into the combined showcase.
- [Andrew] Per-archetype keep/kill/revise review of the 6 new variations (showcases in `deck_generation/output/Opal_Panels_Showcase.pptx` + `Opal_Grid_Showcase.pptx`).

## MCP / Blockers
1 inbound GO (DECK_CLAUDE.FANOUT-B) handled. No blockers. Broker status WORKING throughout; persistent Monitor `buzjqy12e` armed. RAVC2 sent to base RD CC 2.0.0_SA_COO.
