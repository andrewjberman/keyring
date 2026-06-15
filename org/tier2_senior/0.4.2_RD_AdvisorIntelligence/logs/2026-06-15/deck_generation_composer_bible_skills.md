# 0.4.2_RD_AdvisorIntelligence — deck_generation re-architecture: brand-derivative composer, design bible, linter, /deck-prompt + /deck-gen skills

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE

**Date:** 2026-06-15  **Window:** session 2026-06-15 (prior log 2026-06-03; this is a fresh Andrew-direct session)
**Driver:** Andrew-direct (not a registered hot-project TO; standalone deck-generation tooling request)

## Objective

Andrew asked to (1) establish the existing `deck_generation` Lambda's state and access, then test it on new source material (Jim's "Evolution of Advisor Economics and Mobility" .docx); (2) when whole-slide cloning produced fabricated charts/ghost-text, RE-ARCHITECT the generator; (3) codify design rules into a persistent "bible"; (4) build two user skills to run the pipeline.

## Work Completed

### 1. Live-state verification of the existing Lambda
- `deck-generation` Lambda is LIVE (Active, py3.12, 1024MB/120s, Function URL AWS_IAM). Verified all read endpoints + full write path (POST / -> PPTX -> presigned URL) against live AWS. Access = `awscurl` IAM-signed. Slide-library artifact present at `s3://opal-313476888478-lambda-artifacts/deck-generation-pipeline/slide-library.pptx`.

### 2. Category-error diagnosis (DIAGNOSE)
- V1 whole-slide cloning fuses design WITH data: cloning a library "canonical slide" inherits its embedded charts (fabricated numbers, e.g. 1.6M->1.8M), radials, stat callouts, and off-topic copy ("Bottom Line: DIZ..."). Text-only inspection was BLIND to this; only a visual render exposed it. Andrew reframed it as a category error: abstract the BRAND (tokens, layout grammar), do NOT reuse the components.

### 3. Brand-derivative composer (IMPLEMENT)
- Built a from-primitives composer: locked brand hexes + 60-30-10 + Lato, charts ONLY from supplied data, library used as a STYLE reference (master cover reuse) not a component source.
- Iterated through design feedback into a primitive library + archetypes: cover (master reuse), panels, flow (chevrons), compare, fork, vsteps, formula, statement, stat-as-type, hub/orbit/convergence/nested/ascending motifs.
- Jim's 13-slide deck rebuilt at 100% fidelity (13 slides = source, 87/87 authored lines covered, 0 design-lint violations). Desktop artifacts v2->v5 produced for smoke at each stage.

### 4. DESIGN_BIBLE.md (the persistent rule-set)
- `deck_generation/DESIGN_BIBLE.md` — every rule tagged [AUTO] (machine-linted, fails build), [QA] (visual render pass), or [CONTENT] (fidelity). Governing principle "Fundamentals before flourish." Rules cover brand tokens, dark->light color law, no-wrap large text, true circles, text-centered-in-container, symmetry incl. interstitial spacing, fixed corner radius, one-graphic-per-slide, no-consecutive-repeat-format, group-uniform text sizing, margins, eyebrow-tick centering. Andrew co-authored (corner radius / eyebrow tick / geometric-marks-only rulings).

### 5. design_lint.py (the [AUTO] enforcement)
- `deck_generation/engine/design_lint.py` — lints a built Presentation against the [AUTO] rules; returns (slide, rule, msg) violations. Refined iteratively as it surfaced real defects (inconsistent radii, off-center labels, margin breaches) and false positives (field-exemption, single-operator C1 skip, large-body-sentence skip, cover-skip).

### 6. engine/compose.py + the two skills
- `deck_generation/engine/compose.py` — the standing library: `Deck` class (master-cover reuse, archetype tracking, `finalize()` = lint + fidelity gate, RAISES on failure) + `C` primitives, all bible-compliant by construction. Smoke-tested: 3 slides, 0 violations, 2/2 coverage, renders clean.
- `deck_generation/PROMPT_SPEC.md` — the `*.deck.md` contract (content+structure only; design is the bible's job).
- `.claude/skills/deck-prompt/` — synthesizes a prompt file from source(s) OR via interview. `.claude/skills/deck-gen/` — consumes the prompt -> gated build -> Desktop. Both registered + visible.
- Dry-ran /deck-prompt on Jim's .docx -> `deck_generation/prompts/advisor-economics-and-mobility.deck.md` (13 slides, validated: cover-first, all titled, no consecutive-repeat archetypes).

## Compiler Tools

No comp-* tools were run this session. Justification: this was standalone `deck_generation` tooling (Python composer + linter + Claude Code skills) with NO data-pipeline, cloud/infra, or frontend change — Rule-20 graph-check and comp-pipescript/comp-iam/comp-surface gates are N/A. Verification was done by the purpose-built `design_lint.py` (the deck pipeline's own gate) + PowerPoint-COM visual render, the correct verify-channel for this artifact class.

## Current State (handoff)

- **All artifacts are UNCOMMITTED working-tree changes** (no git commit made this session except this log). New files:
  - `deck_generation/DESIGN_BIBLE.md`, `deck_generation/PROMPT_SPEC.md`
  - `deck_generation/engine/compose.py`, `deck_generation/engine/design_lint.py`
  - `deck_generation/prompts/advisor-economics-and-mobility.deck.md`
  - `.claude/skills/deck-gen/SKILL.md`, `.claude/skills/deck-prompt/SKILL.md`
  - working scripts under `.runtmp/` (brand_deck_v4.py = reference 13-slide build; brand_motifs.py; brand_compose_v3.py)
- **Live Lambda `deck-generation` is UNCHANGED** — still V1 clone behavior. The new composer is local-only; re-pointing the Lambda at it is a deferred, separate deploy (would need the new engine packaged + Terraform per CLAUDE.md deploy rules).
- **Render path:** PowerPoint COM automation in PowerShell (LibreOffice/poppler NOT installed on this Windows host). `$ppt=New-Object -ComObject PowerPoint.Application; $pres.Export($dir,"PNG",w,h)`.
- Memory updated: `memory/project_deck_generation_brand_derivative_composer.md` (+ MEMORY.md pointer).

## Next Steps

- Andrew to smoke the v5 deck + the /deck-prompt output; then run `/deck-gen deck_generation/prompts/advisor-economics-and-mobility.deck.md` to see the full hand-off.
- Commit the deck_generation engine + skills (ds-commit-gate applies to the .py files) once approved — they pass `from __future__ import annotations`; confirm ruff-clean before commit.
- Future: re-point the live `deck-generation` Lambda at the new composer (packaged engine + Terraform), and expand the container/motif library per ongoing design feedback.

## MCP / Blockers

- MCP: 1 inbound at session start (2.0.0_SA_COO RAVC3 standby clearance — acknowledged, no action required); heartbeats throughout. No blockers.
