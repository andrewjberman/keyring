---
name: deck-prompt
description: Author a `*.deck.md` deck prompt for `/deck-gen` and render it in-session as boxed slide cards (the cards are the deliverable; the file is persistence). Two passes: flow and layout, then the per-slide variant (A/B/C/D). Use on `/deck-prompt`, "make a deck prompt", "turn this doc into a deck". Pair: `/deck-gen`.
---

# /deck-prompt — author a deck-prompt, rendered in the session

## THE CONTRACT — read this first; it is the whole skill

Your deliverable is the **deterministically-rendered slide cards, printed in the session** —
produced by the renderer, never by you. Every time, the loop is:

1. **You write/edit** `deck_generation/prompts/<slug>.deck.md`. This is your ONLY creative
   output: slide copy + the archetype per slide. You decide nothing about formatting.
2. **You run the renderer:**
   ```
   cd deck_generation
   PYTHONUTF8=1 PYTHONPATH=. python prompt_view.py prompts/<slug>.deck.md
   ```
   (PowerShell: `$env:PYTHONUTF8='1'; $env:PYTHONPATH='.'; python prompt_view.py prompts\<slug>.deck.md`)
3. **You present the renderer's stdout VERBATIM, in a fenced code block, as the first thing in
   your reply** — the full deck, every slide — then at most ONE line asking to approve or edit.

`prompt_view.py` is a pure function — it reads the `.deck.md` + the archetype registry and has no
randomness, clock, or network — so the **same `.deck.md` renders byte-identical cards on every
machine and every session.** That is the entire source of consistency: the formatting must come
from the tool, not from you. Add `--ascii` for a pure-ASCII frame (guaranteed alignment anywhere).

### NEVER (each of these breaks the determinism — and each has happened)
- **NEVER** hand-format, redraw, or re-type a slide card yourself. Copy the tool's stdout exactly.
- **NEVER** summarize, describe, paraphrase, or analyze the deck *instead of showing it*.
- **NEVER** say "rendered above" / "see the output" / point back at a tool result — paste the cards
  into your reply as the content.
- **NEVER** lead with commentary. The cards come first; any commentary is one line, after them.
- **NEVER** show a partial or "representative" subset — always the full deck, every slide.
- **NEVER** edit, tighten, re-wrap, or "clean up" the tool's output. It is the product as-is.
- **NEVER** make the user run a command, see a file path, or type a raw letter/archetype name.
  You run all python / PowerShell; the user sees only the rendered cards and a clickable picker.

### The markdown file is SECONDARY
The `.deck.md` is persistence + the `/deck-gen` build input. The PRIMARY output is the rendered
cards in the session. Saving the file does NOT satisfy the skill — showing the cards does.

## Step 0 — pick the mode
- A path / file(s), or "turn this into a deck" → **SYNTHESIZE**: read every source; if it is already
  slide-structured, keep its slide count + per-slide content (fidelity); if prose, segment sensibly.
- "new deck" / no source → **INTERVIEW**: topic, audience, goal enum (prospect_pitch /
  client_recommendation / partner_intro / strategy_update / custom), flow, length, key points, data,
  must-includes. `AskUserQuestion` for discrete choices; don't over-interview ("make a sample" → just proceed).

## Archetypes — the live catalog is the source of truth
Run `python -m engine.compose --catalog` (from `deck_generation/`). **Default to VARIETY, not the bare
family primary (D11).** In **Pass 1** pick each slide's best-*fitting* layout — and when a family repeats
across the deck, use a *different* variant each time (4 `compare` slides → `compare` / `compare-balance` /
`compare-venn` / `compare-convergence`; 3 `statcards` → `statcards-clean` / `statcards-delta` /
`statcards-strip`), so even a deck that never reaches Pass 2 is already varied. The **cover defaults to the
master** (`cover` — the photo cover, the best cover; D11-exempt). **Pass 2** is the per-slide refinement
picker. Only a name the catalog prints is valid. Two rules bind: never the same family on two consecutive
slides (D10), and a family repeated ≥3× must use ≥`ceil(k/2)` distinct variants (D11) — `/deck-gen` rejects
both. Charts only with real numbers.

## The two passes — each pass IS the contract loop (write/edit → render → paste cards → ask)
- **Pass 1 — flow & layout:** lay out the slides + copy; the layout falls out of the narrative
  (labeled upper-right on each card). Pick the best-fit *variant* per slide — **default to variety**:
  vary the variant on any family that repeats (D11), cover = master. Render, paste the full deck, ask to
  approve copy + flow. Edits = edit the `.md`, re-render, re-paste the full deck.
- **Pass 2 — variant (the card design), via a CLICKABLE picker (mandated standard):** only after
  Pass 1 is approved. The user picks the visual treatment of each card by *clicking between pictures*
  — never by typing. You run all python; surface only the cards + the picker.
  1. **Get the variant data:** run `... prompt_view.py prompts/<slug>.deck.md --pass2 --json` — every
     slide's family variants, each with a deterministic `preview` mock (the renderer's ASCII layout
     for that treatment: compare = two columns, compare-venn = overlapping circles, panels-formula =
     A + B = C, the chart types as icons, …).
  2. **Offer the one-click path FIRST:** a single `AskUserQuestion` — "Use the recommended design for
     every slide, or choose per slide?" with **"Accept all recommended" (Recommended, first)** and
     "Choose per slide." Accept-all → apply the recommended variant to every slide and skip to step 5.
  3. **Per slide (one `AskUserQuestion` each):** build the options from the `--json` data — each
     option's **`preview` = that variant's renderer mock pasted verbatim** (never hand-drawn), `label`
     = a plain-language name, `description` = its use-line. Put the **best-fit variant FIRST, marked
     "(Recommended)"** — it is the default, so a non-technical user can click straight through.
  4. **>4-variant families** (Cover, Statement = 5) exceed the picker's 4-option cap: present the **4
     best-fit** variants; the auto-"Other" covers the 5th. **Charts:** the variants ARE chart types —
     offer those matching the data shape. **Table:** one variant — no picker, just confirm.
  5. On each pick, **Edit** that slide's `archetype:` to the chosen variant. When all slides are set,
     **re-render and paste the full deck** (the contract), then hand off.

## Writing the .deck.md (the renderer parses it — keep to PROMPT_SPEC.md)
- Frontmatter: `deck_title`, `audience`, `goal`, `source`, `slide_count`.
- One `## Slide N — Name` block per slide; `archetype:` = the chosen best-fit variant (default to
  variety, not the bare primary; vary it on repeated families; cover = `cover`); short `title:`;
  content as `- bullets` (use ` | ` to split a bullet into header | body for cards / compare /
  stats / steps; a plain `- text` bullet is fine — **mixed paired + plain in one slide is OK and all
  render**); `subtitle:`/`tag:` (cover, statement), `footer:`/`quote:` (takeaway, pull-quote), and a
  `data:` line for charts/tables (real numbers only).

## Hand off (after Pass 2 is approved)
> Prompt saved: `deck_generation/prompts/<slug>.deck.md`
> Run **`/deck-gen deck_generation/prompts/<slug>.deck.md`** to build the deck.

## Process note
This process is **NOT commit-gated** (Andrew-direct). Iterate fast and show the rendered cards;
commit the `.deck.md` and any renderer change for persistence when convenient — never block a pass on it.
