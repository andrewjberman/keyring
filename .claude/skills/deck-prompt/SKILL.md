---
name: deck-prompt
description: Author a structured deck-prompt file (`*.deck.md`) that `/deck-gen` turns into an Opal PowerPoint. Two modes — (1) SYNTHESIZE from existing material (a document, or a cache of several files) into the canonical prompt format; (2) NEW FROM SCRATCH via a short interview (what the deck is about, audience, topical flow, how many slides) and then draft the prompt. Output conforms to deck_generation/PROMPT_SPEC.md and ends by instructing the user to run `/deck-gen <file>`. Use when the user says `/deck-prompt`, wants to "make a deck prompt", "turn this doc into a deck", or "start a new deck". Pair skill: `/deck-gen` consumes what this writes.
---

# /deck-prompt — author a deck-prompt file

Produces a `*.deck.md` (see `deck_generation/PROMPT_SPEC.md`) — the structured,
consistent input `/deck-gen` builds from. Read `PROMPT_SPEC.md` first; it is the schema.
You write content + structure only — **never** colors/fonts/layout (those live in
`DESIGN_BIBLE.md` and are enforced at generation).

## Step 0 — pick the mode

- **A path / file(s) given, or "turn this into a deck"** → **SYNTHESIZE** (Step A).
- **"new deck", "from scratch", or no source** → **INTERVIEW** (Step B).
- Ambiguous → ask which.

## Archetypes — the live catalog is the source of truth

**Before picking any `archetype:`, run `python -m engine.compose --catalog` (from
`deck_generation/`).** It is the single source of truth (`engine/registry.py`) and prints
every archetype `/deck-gen` can render — name, one-line purpose, the content it `takes`,
its item-count range, and an example — grouped by family (~50 across Cover · Panels · Grid ·
List · Compare · Flow · Statcards · Stat · Statement · Table · Charts). **Never work from a
remembered list** — the set grows, and only a name the catalog prints is valid (an unlisted
archetype is rejected by `/deck-gen`). Choose the archetype whose `takes` contract matches
the slide's content and keep the item count inside its printed range.

## Step A — Synthesize from material

1. **Read every source** (`.docx` via python-docx, `.pdf` via the pdf path, `.md`/`.txt`
   directly). For a cache of files, read all and reconcile into one narrative.
2. **Extract the slide structure.** If the source is already slide-structured (e.g.
   "Slide 1 / Title / Visual / Key points"), preserve its slide count and per-slide
   content exactly — that is the author's intent (fidelity). If it's prose, segment it
   into a sensible slide sequence.
3. **Per slide, capture** a short `title`, the content lines (bullets / quotes / key
   messages — everything that must appear), and the author's **visual intent** if stated
   ("3-column visual", "big arrow", "large centered graphic") → map to an `archetype:`.
4. **Choose archetypes** from the live catalog (see the box above — `--catalog`). **Vary
   them** — never the same archetype on two consecutive slides (D10). Match structure to
   subject: process/sequence → `flow` or `vsteps`; peer concepts/features → `panels` or
   `grid`; a head-to-head → `compare` (or a `compare-*` variant); KPIs/metrics →
   `statcards`; a section break or close → `statement`; real numbers → the `chart-*`
   family. If no archetype fits, give `intent:` prose and let `/deck-gen` pick the form.
5. **Charts:** only emit a `data:` chart line if the source gives real, representative
   numbers. Otherwise leave figures as content (they'll render as stat-as-type).
6. Write the `*.deck.md` per the spec.

## Step B — New from scratch (interview)

Run a short interview, then draft. Cover, at minimum:
1. **Topic** — what is the deck about? (one or two sentences)
2. **Audience** — who's it for? (prospects / clients / partners / internal)
3. **Goal** — the enum: prospect_pitch / client_recommendation / partner_intro /
   strategy_update / custom.
4. **Topical flow** — the sections/beats in order (the narrative arc).
5. **Length** — how many slides (or "you suggest" → propose a count from the flow).
6. **Key points per section** — the must-say content for each beat.
7. **Data** — any real stats/figures to feature? (only these become charts/stats.)
8. **Must-includes** — quotes, taglines, a required closing.

Use `AskUserQuestion` for the discrete choices (audience, goal, length) and free text for
the rest; keep it to a few rounds, don't over-interview. Then:
- Draft a slide-by-slide outline (title + content + archetype per slide), **varying the
  archetypes** and matching structure to subject. Briefly show the outline for a sanity
  check if the user wants, then write the `*.deck.md`.

## Step C — Write the file + hand off (both modes)

1. **Validate** against `PROMPT_SPEC.md`: one `## Slide N — Name` block per slide; every
   non-cover slide has a short `title:`; no two consecutive `archetype:` the same; charts
   only where `data:` is present; first slide is `cover`.
2. **Save** to `deck_generation/prompts/<slug>.deck.md` (create the dir if needed). Add
   the provenance footer comment (source / interview, reviewed flag).
3. **Hand off** — tell the user exactly:
   > Prompt written: `deck_generation/prompts/<slug>.deck.md`
   > Review/edit it, then run **`/deck-gen deck_generation/prompts/<slug>.deck.md`** to build the deck.

## Rules
- Output is **content + structure only**. No design directives — the bible owns those.
- **Be faithful to sources** — preserve an author's slide count and per-slide content; do
  not drop or invent. When inventing (scratch mode), make the content true to the brief.
- **Vary structure** so `/deck-gen` won't reject consecutive-repeat formats.
- Never request a chart without real numbers.
