# 0.4.2_RD_AdvisorIntelligence — deck_generation: structure /draw + brand-PDF assessment + analyst-deck layout harvest

**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE, DIAGNOSE

**Date:** 2026-06-17  **Driver:** Andrew-direct (standalone deck-generation tooling; continues the 2026-06-15 re-architecture). Not a hot-registry TO.

## Objective
Andrew: (1) `/draw` the current deck-build structure (knows cloud Lambdas are involved); (2) assess incorporating `opal_brand_guidelines.pdf` into the deterministic generator after an analyst's naive-prompted deck (`Opal_Cottonwood_vs_Goldman_Case_Study_Ausdal.pptx`) came out well; (3) bring her concepts/layouts into the generator + assess further enhancements.

## Work Completed

### 1. Ground-truth + /draw (EXPLORE/TRACE)
Mapped the live structure: TWO parallel build paths sharing one offline brand/index plane. **Path A** (deployed Lambda) `lambda_function -> lambda_api/handler.py -> engine.orchestrator.orchestrate_bundle` clones the 103-slide library via the `index/` data layer (intent->architect->fitter->assembler->fit-audit). **Path B** (local skills) `/deck-prompt -> *.deck.md -> /deck-gen -> engine.compose` composes from brand primitives + `design_lint` + fidelity gate. Confirmed by grep: handler calls orchestrator/skeleton/assembler and never compose/DESIGN_BIBLE; compose imports only python-pptx + design_lint, never index/orchestrator. Delivered the two-plane ASCII diagram.

### 2. Brand-PDF assessment (DIAGNOSE)
Read all 13 PDF pages: identity-only (logo 4-variants + 0.5x safe-space; 4-color palette; Lato type scale h1 48/h2 Thin 30/h3 20/body 12). NO layout/composition guidance. Its colors (`#163372/#0A1733/#C4CBDB/#5F3BE3`) + Lato are already byte-exact in BOTH `brand_spec/brand.json` (Path A) and hardcoded `compose.py` constants (Path B) -> "incorporate the PDF" is ~90% done. Extracted every fill in the analyst deck: all on-brand (she/Claude re-derived the same ramp). Conclusion: the deck looked good from Claude's LAYOUT judgment under the brand identity, not from the PDF -> the gap is layout vocabulary, validating Path B. Reframed Andrew's hypothesis and recommended investing in Path B (not the clone Lambda).

### 3. Layout harvest -> 5 new primitives (IMPLEMENT)
Reverse-engineered her 11 slides (structure + table cells via python-pptx; rendered to PNG via COM). Added to `engine/compose.py`, bible-compliant by construction:
- `C.statcards` — KPI comparison cards (big/label/vs/takeaway), uniform navy top-band + one big-number size (D8).
- `C.list_accent` (+`panel=True` row cards) + `C.sidebar` (filled panel) — the list+sidebar split.
- `C.grid` — feature tiles, left accent bar, partial last row auto-fills (fixes the human deck's empty-cell tell).
- `C.table` — navy header / zebra body / navy-bold first column, A1-palette fills only.
- `C.bar` helper — accent bars are plain RECTANGLES (rounded-rect <0.3in fails D7).

`design_lint.py` D9 refined: count `has_table` + sizable filled panels (min(w,h)>=0.6, not full-bleed) as the graphic element (aligns linter with the bible's "a colored container/panel"); `finalize()` coverage now walks table cells (fidelity must see table content). DESIGN_BIBLE D9 + `/deck-gen` SKILL.md archetype-map updated.

### 4. Fidelity proof
`deck_generation/dev/scripts/cw_goldman_build.py` rebuilds her Cottonwood-vs-Goldman deck (her real numbers, no invented data per F2) through `finalize()`: **11 slides, 0 lint violations, 10/10 coverage**. Visual-QA all 11 slides via COM render — clean after fixing 2 footer-crowding [QA] issues (slides 6, 9). Delivered to `Desktop/Opal_Cottonwood_vs_Goldman.pptx`.

## Compiler Tools
No comp-* tools run. Justification: standalone `deck_generation` tooling (Python composer/linter + Claude Code skills) — no data-pipeline, cloud/infra, or frontend change, so Rule-20 graph-check + comp-pipescript/comp-iam/comp-surface are N/A. Verification was the purpose-built `design_lint.py` [AUTO] gate + fidelity coverage + PowerPoint-COM visual render — the correct verify-channel for this artifact class. `py_compile` clean on all touched .py.

## Current State (handoff)
- Working-tree changes (UNCOMMITTED): `engine/compose.py`, `engine/design_lint.py`, `DESIGN_BIBLE.md`, `.claude/skills/deck-gen/SKILL.md`, `dev/scripts/cw_goldman_build.py`.
- Commit BLOCKED on two fronts, both matching the 2026-06-15 DT-custodial precedent: (a) all files are outside the RD portal lane; (b) `ds-commit-gate` ruff E701 on `compose.py`'s established dense one-line style (HEAD already had 20; do NOT bulk --fix per the cot-fork ruff memory). Recommend DT custodial save or Andrew clearance for a gate-note/--force bypass.
- Live Lambda UNCHANGED (still Path A clone). Re-pointing it at Path B is deferred (DT deploy).

## Next Steps / open enhancement menu (Andrew's call)
- Single brand source-of-truth (generate compose constants from brand.json) — closes the token-duplication drift.
- Encode the PDF's exact type scale incl. Lato Thin; logo auto-placement + 0.5x safe-space lint; fix dark-slide master-footer logo variant (light-on-dark).
- The "bridge" workflow: free-form Claude draft -> /deck-gen re-renders through the gates.
- Eventual: re-point the Lambda at Path B.

## MCP / Blockers
No inbound this session. No blockers. Broker status WORKING throughout; persistent Monitor `bftbi2it5` armed.
