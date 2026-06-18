---
name: deck-prompt
description: Author a deck-prompt (`*.deck.md`) for `/deck-gen` and render it IN THE SESSION as boxed slide cards. The rendered cards (slide #, title, text-format, content) — printed in the chat by the deterministic tool `prompt_view.py` — are the deliverable; the `.deck.md` is just persistence. Two passes — (1) FLOW & LAYOUT: lay out the slides + copy, render the cards, approve; (2) VARIANT: per slide pick the card design (A/B/C/D). Use when the user says `/deck-prompt`, "make a deck prompt", "turn this doc into a deck", or "start a new deck". Pair skill: `/deck-gen` consumes the saved file.
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
Run `python -m engine.compose --catalog` (from `deck_generation/`). In **Pass 1** pick each slide's
FAMILY primary (`cover`, `panels`, `grid`, `compare`, `list`, `vsteps`/`flow`, `statcards`, `stat`,
`statement`, `table`, or a `chart-*`); **Pass 2** swaps in a variant. Only a name the catalog prints
is valid. Vary families — never the same family on two consecutive slides (D10). Charts only with real numbers.

## The two passes — each pass IS the contract loop (write/edit → render → paste cards → ask)
- **Pass 1 — flow & layout:** lay out the slides + copy; the family falls out of the narrative
  (labeled upper-right on each card). Render, paste the full deck, ask to approve copy + flow. Edits =
  edit the `.md`, re-render, re-paste the full deck.
- **Pass 2 — variant (card design):** only after Pass 1 is approved. Show each slide's family
  variants as **VISUAL layout mocks** — the renderer draws each variant's treatment (e.g. compare =
  two columns vs compare-venn = overlapping circles vs compare-balance = beam/fulcrum), so the user
  picks between *pictures* labeled A/B/C/D, not a list of names. Run
  `... prompt_view.py prompts/<slug>.deck.md --pass2` (all slides) or
  `... prompt_view.py --variants <archetype>` (one); paste its output verbatim, same contract as Pass 1.
  User picks a letter per slide; **Edit** that slide's `archetype:` to the chosen variant; re-render +
  re-paste the full deck. Charts: the variants ARE the chart types — offer those matching the data
  shape; Table: one variant — confirm.

## Writing the .deck.md (the renderer parses it — keep to PROMPT_SPEC.md)
- Frontmatter: `deck_title`, `audience`, `goal`, `source`, `slide_count`.
- One `## Slide N — Name` block per slide; `archetype:` = the family primary; short `title:`;
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
