# 0.4.2_RD_AdvisorIntelligence~C — DECK_CLAUDE.FANOUT-C: Statcards + Stat archetype variations

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-06-17  **Driver:** Andrew-direct fan-out GO (base RD dispatch, CC COO). TO: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/DECK_CLAUDE.FANOUT-C.statcards-and-stat-archetypes.md`. Lane ~C.

## Objective
Bring **Statcards** and **Stat** to 4 variations each (build the 3 NEW ones per family; cores exist), in the two modules I own exclusively — `deck_generation/engine/arch_statcards.py` + `engine/arch_stat.py`. stat-as-type only (charts deferred, F2). Gate to 0 lint + full coverage + COM visual-QA every slide.

## Work Completed (IMPLEMENT)

### arch_statcards.py — 3 new (core `C.statcards` = 4 total)
- **statcards-clean** — filled navy KPI cards, big white number + cool-grey label only, no vs-line. Uniform card width/gutter (D3), one big-number size (D8).
- **statcards-strip** — one LIGHTBG panel, 4-6 metrics evenly placed, cool-grey vertical dividers (kept off the container set so no D3/D2 interference). Compact horizontal strip.
- **statcards-delta** — LIGHTBG card + navy top-band + number + label + a geometric ISOSCELES_TRIANGLE marker (rotation 180 = down) + the change text. No red/green in palette, so direction is conveyed by orientation; marker x is **card-relative-fixed** so the triangle row keeps equal gutters (D3).

### arch_stat.py — 3 new (core `C.stat` = 4 total)
- **stat-context** — oversized hero number in a filled navy panel (number+label group vertically centered on the panel) beside a multi-line left-aligned context paragraph (C3).
- **stat-hero** — big navy filled card ("$30B+" / "10-year AUA goal", board B10) paired beside a purple-circle-bulleted list (the slide's single 10% accent; true circles, F6 geometric marks).
- **stat-stacked** — slide-51 sleeve-composition: stacked RECTANGLE segments per column, **brand ramp dark->light top->bottom** (B1) with **no purple in the ramp** (B2), % labels on tall-enough segments (ton() contrast), a vertically-centered left legend, column labels, and a cool-grey baseline divider. Buildable from shapes (F2-safe).

### showcase scripts
`dev/scripts/showcase_statcards.py` + `dev/scripts/showcase_stat.py` — one slide per variation incl. the core via `C.statcards`/`C.stat`, eyebrow-labeled with sample Opal content, distinct tags (no D10 back-to-back repeat). Each prints **GATE PASS: 0 lint + full coverage** (5 slides). `python -m engine.compose --catalog` now shows Statcards (4) + Stat (4).

## VALIDATE — gate + visual-QA
- `finalize()` [AUTO] design_lint + fidelity coverage: **0 violations, 4/4 coverage, 5 slides** on BOTH decks (gate raises otherwise, so the printed PASS is real).
- PowerPoint-COM render of all 10 slides + read each: clean after **one [QA] fix** — stat-stacked left legend wrapped/orphaned ("Fixed/income", "Alternati/ves"); widened plot-left (x 1.9->2.7) + vertically centered the legend so names sit one-line. Re-rendered: clean. Covers F4-reused (title/subtitle/tag retext landed); empty 2nd eyebrow tick on the cover is a pre-existing master-template artifact in shared `compose.py` (`set_cover`), outside my lane.
- `ds-commit-gate.sh` on all 4 files: **All checks passed** (py_compile + AST + ruff py39). Trimmed imports to used names -> no F401, no E701, no bulk --fix.

## Compiler Tools
No comp-* tools run. Justification: standalone `deck_generation` tooling (Python composer + my two family modules + showcase scripts) — no data-pipeline, cloud/infra, or frontend change, so Rule-20 graph-check + comp-pipescript/comp-iam/comp-surface are N/A. Verification was the purpose-built `design_lint.py` [AUTO] gate + `finalize()` fidelity coverage + PowerPoint-COM visual render (the correct verify-channel for this artifact class) + `ds-commit-gate.sh`. All clean.

## Files Modified / Current State (handoff)
Committed `4d33f0811` (DECK lane, ~C author), pushed to origin/CLOUD. See commit message for per-file summary.
- `deck_generation/engine/arch_statcards.py` — 3 funcs + register (Statcards family now 4).
- `deck_generation/engine/arch_stat.py` — 3 funcs + register (Stat family now 4).
- `deck_generation/dev/scripts/showcase_statcards.py`, `showcase_stat.py` — new showcase builds.
- TO flipped to `<status>complete</status>`.
- Owned ONLY my 2 modules + 2 showcase scripts; shared `compose.py`/`registry.py`/`design_lint.py` untouched (pre-wired, zero-contention). QA PNGs under `deck_generation/output/qa_statcards/` + `qa_stat/` (gitignored output dir).

## Next Steps
- [0.4.2_RD_AdvisorIntelligence] base RD integrates the new variants; per-archetype keep/kill/revise review by Andrew (the 6 new variations are designed and clean, ready to showcase).
- Cover-family (~A), Panels/Grid (~B), Compare/Flow/List (~D) modules are still empty stubs — same family-module pattern now proven end-to-end (gate + COM-QA + clean commit) by this lane.

## MCP / Blockers
Inbound: 1 GO (base RD, DECK_CLAUDE.FANOUT-C) acted on; 1 stale non-blocking CTO product-Q (49F cross-drill, 2026-06-02) surfaced to Andrew, not actioned. No blockers. Broker status WORKING throughout; persistent Monitor `bzb0io1z3` armed at load.
