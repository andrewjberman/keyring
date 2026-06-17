# 0.4.2_RD_AdvisorIntelligence~A — DECK_CLAUDE.FANOUT-A: Cover + Statement archetype variations

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-06-17  **Driver:** Andrew-direct fan-out via base RD (0.4.2_RD_AdvisorIntelligence).
TO: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/DECK_CLAUDE.FANOUT-A.cover-and-statement-archetypes.md`.

## Objective
Build 4 Cover + 4 Statement/Mood archetype variations as bible-compliant, registered, gate-clean
archetypes in MY two pre-wired module files only (`engine/arch_cover.py`, `engine/arch_statement.py`),
grounded in the Opal master designs. Andrew LOCKED the cover refs to the blocked-graphic mosaics
(master slides 1 / 14 / 60 + analyst B1). compose.py / registry.py are pre-wired (zero-contention) --
do not touch. Gate each showcase to 0 lint + full coverage, then PowerPoint-COM visual-QA every slide.

## Work Completed

### 1. Grounding (read-first)
Read DESIGN_BIBLE.md (law), master-slide-archetype-map.md (my targets + slide refs), compose.py
primitives (`C.circle/rrect/ring/osh/banner/text`, `ramp`, `uni_pt`, `Deck`/`finalize`), the
design_lint [AUTO] rules, and registry.register() -- composed correct-by-construction against them.

### 2. Cover family (`engine/arch_cover.py`) -- 4 variations
Shared `_mosaic()` helper reproduces the Opal blocked-graphic mosaic GEOMETRICALLY: an n x n grid of
equal cells (color blocks / true circles via `C.circle` / single-corner half-rounds via
`ROUND_1_RECTANGLE`), ramped dark->light by column (B1), exactly one purple accent cell (B2), with a
concentric ring overlay. Every cell filled so each row is an equal-width / equal-gutter group (D3-clean).
- **cover-mosaic** -- title left + mosaic right (master 1 / B1).
- **cover-mosaic-left** -- mosaic left + centered section title right (master 14 "OCIO SERVICES").
- **cover-minimal** -- type-forward, big title + one restrained geometric accent cluster (the D9 graphic).
- **cover-divider** -- dark (midnight) section break + mosaic + large centered white title (master 60).

### 3. Statement / Mood family (`engine/arch_statement.py`) -- 4 variations
- **statement-fullcolor** -- full-bleed purple field + big white statement + white ring motif (master 98).
- **statement-dark** -- midnight cinematic, concentric rings + purple accent dot + big white line (master 80).
- **statement-quote** -- purple quote-mark badge (chr(0x201C), no non-ASCII in source) + centered quote + attribution.
- **statement-bignum** -- giant stat-as-mood number + accent dot + context line.
All 8 register() under family Cover / Statement; catalog now exposes them (`--catalog`).

### 4. Two design footguns caught + fixed
- **D3 unequal-gutter (cover-minimal):** the accent cluster used `ramp(3)`, whose 3rd color is COOLGREY --
  a NEUTRAL the linter excludes from containers -> a gap in the row -> unequal gutters. Fixed by using
  all-non-neutral ramp colors `[NAVY, MEDBLUE, MUTED]` so every block counts as a container. (Same reason
  the mosaics passed untouched: their excluded COOLGREY column is the LAST column, leaving cols 0-2 contiguous.)
- **Visual:** cover-minimal subtitle now positioned relative to the title bottom (`yb`) -- robust for
  multi-line titles + tighter composition. Showcase slide-2 kicker changed off "Opal Capital" (it
  duplicated the wordmark) to "Firm Overview".

### 5. Gate + visual-QA (the product)
`showcase_cover.py` + `showcase_statement.py` -- one slide per variation, Opal-flavored sample content,
both print **GATE PASS: 5 slides, 0 lint violations, full coverage**. Rendered every slide to PNG via
PowerPoint COM (`render_png.ps1`) and READ all 8 variation slides: on-brand, true circles, A4 contrast
(white/cool-grey on dark + purple fields), no white-on-white, no footer collision, 60-30-10 balanced.
The dark mosaic (cover-divider) uses a brighter ramp (skips midnight) so it stays visible on the dark field.

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| comp-surface-check | auto-run by safe-commit on the 5 changed files | PASS (0 critical surfaces touched) |

Justification: standalone `deck_generation` tooling (Python composer/linter + showcase scripts) -- no
data-pipeline, cloud/infra, or frontend change, so Rule-20 graph-check + comp-pipescript/comp-iam are
N/A. The purpose-built verify-channel for this artifact class is the `design_lint.py` [AUTO] gate +
fidelity coverage + PowerPoint-COM visual render -- all run + clean. py_compile clean; ruff
(--extend-select FA) 0 violations on all 4 .py (conditionals as indented blocks -> no E701 -> no
gate-note/bypass needed). page_inventory.xml not touched (this is deck tooling, not the AdvisorIntelligence portal page).

## Current State (handoff)
- Committed `340cc53ab` (DECK lane, ~A author line): arch_cover.py, arch_statement.py, showcase_cover.py,
  showcase_statement.py, render_png.ps1. Scoped to MY files only -- siblings' concurrent ~B/~D module
  work (arch_compare/flow/grid/list/panels + their showcases) left untouched.
- At HEAD 23ee1786f base, in sync with origin/CLOUD (0/0) before commit; 3a1fad6e2 (the wired stubs) in
  history. RD cannot push -- base RD / DT carries the push + the combined-showcase integration.
- Decks for review on disk: `deck_generation/output/Opal_Cover_Showcase.pptx`,
  `Opal_Statement_Showcase.pptx` (+ PNGs under output/qa_cover, output/qa_statement).

## MCP / Blockers
GO received + ACK'd; RAVC2 report sent to base RD (0.4.2_RD_AdvisorIntelligence) CC 2.0.0_SA_COO on
completion. No blockers. Persistent Monitor `buhz8mnxu` armed; broker status WORKING throughout.
