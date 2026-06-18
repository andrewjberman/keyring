---
name: deck-prompt
description: Author a deck-prompt (`*.deck.md`) for `/deck-gen`, shown in the chat as boxed slide cards. Two passes — (1) FLOW & LAYOUT: interview or synthesize, lay out the slides, and display them as boxed cards (slide #, title, text-format, content) for approval; (2) VARIANT: per slide, offer the archetype's design variants (A/B/C/D) so the user picks the card design. Output always renders in-chat via a deterministic renderer (byte-identical every session) and saves to deck_generation/prompts/. Use when the user says `/deck-prompt`, "make a deck prompt", "turn this doc into a deck", or "start a new deck". Pair skill: `/deck-gen` consumes the saved file.
---

# /deck-prompt — author a deck-prompt, shown in the chat

Produces a `*.deck.md` (schema: `deck_generation/PROMPT_SPEC.md`) — the input `/deck-gen`
builds from — and **always displays it in the chat as boxed slide cards**. You write content
+ structure only; never colors/fonts/layout (the bible owns those, enforced at generation).

## Non-negotiable: the prompt is shown IN THE CHAT

Every time you produce or change the prompt, render it in the chat with the deterministic
view tool — **never** just "saved to `<path>`, go look." The tool guarantees byte-identical
formatting across every session and machine (that consistency is the whole point). Run it
with the Bash tool and **paste its output verbatim into the chat inside a code block**:

```
cd deck_generation
PYTHONUTF8=1 PYTHONPATH=. python prompt_view.py prompts/<slug>.deck.md            # Pass 1 — boxed cards
PYTHONUTF8=1 PYTHONPATH=. python prompt_view.py prompts/<slug>.deck.md --pass2    # Pass 2 — variant menus, all slides
PYTHONUTF8=1 PYTHONPATH=. python prompt_view.py --variants <archetype>            # one slide's family variants
```
Add `--ascii` to any call for a pure-ASCII frame (guaranteed alignment on any terminal/locale;
the default is box-drawing). `prompt_view.py` reads the saved `.deck.md` and renders it — so
the file and the on-screen cards are always the same thing.

## The two passes

**Pass 1 — Flow & layout.** Decide the slide sequence and the *content* of each slide. The
archetype FAMILY for each slide falls out of the narrative implicitly (a title → cover; peer
concepts → panels/grid; a sequence → flow/vsteps; a head-to-head → compare; KPIs → statcards;
a close → statement; real numbers → a chart/table). The user reads copy, not archetypes — but
each card labels its archetype upper-right. Write the `.deck.md`, render the cards, get approval
on copy + flow. Adjust = edit the `.md` and re-render.

**Pass 2 — Variant (the card's design).** Only after Pass 1 is approved. For each slide, show
the variants WITHIN its family as A/B/C/D and let the user pick the visual treatment. On each
pick, change that slide's `archetype:` in the `.md` to the chosen variant and re-render. Then
hand off to `/deck-gen`.

## Step 0 — pick the mode
- A path / file(s) given, or "turn this into a deck" → **SYNTHESIZE**: read every source
  (`.docx`/`.pdf`/`.md`/`.txt`), reconcile into one narrative; if it's already slide-structured,
  keep its slide count + per-slide content (fidelity); if prose, segment into a sensible sequence.
- "new deck" / "from scratch" / no source → **INTERVIEW**: topic, audience, goal enum
  (prospect_pitch / client_recommendation / partner_intro / strategy_update / custom), topical
  flow, length, key points per beat, data, must-includes. Use `AskUserQuestion` for the discrete
  choices; keep it to a few rounds — don't over-interview. (A bare "make me a sample" → pick
  sensible defaults and proceed; don't interrogate.)

## Archetypes — the live catalog is the source of truth
Run `python -m engine.compose --catalog` (from `deck_generation/`). It prints every archetype
`/deck-gen` can render, grouped by family, with the content each `takes` + its item range. In
**Pass 1** pick the family's *primary* archetype (`cover`, `panels`, `grid`, `compare`, `list`,
`vsteps`/`flow`, `statcards`, `stat`, `statement`, `table`, or a `chart-*`); **Pass 2** swaps in
a variant. Only a name the catalog prints is valid. Vary structure — never the same family on two
consecutive slides (D10). Match the item count to the archetype's range.

## Pass 1 — build & display
1. Lay out the slides (slide 1 = a cover; vary families across the deck). Per slide capture a
   short `title:` and the content lines.
2. Write `deck_generation/prompts/<slug>.deck.md` per `PROMPT_SPEC.md`: frontmatter, one
   `## Slide N — Name` block per slide, `archetype:` = the family primary, content as `- bullets`
   (use ` | ` to split into header | body for cards/compare/stats/steps), `subtitle:`/`tag:`/
   `footer:` fields where relevant, and a `data:` line for charts/tables — **only with real
   numbers** (no data → render figures as a stat archetype instead).
3. **Run the renderer (Pass 1) and paste the boxed cards into the chat.**
4. Ask the user to approve copy + flow, or adjust. Apply edits to the `.md`, then re-render.

## Pass 2 — variant selection
1. Run `--pass2` (every slide's menu) or `--variants <archetype>` (one slide) and present each
   slide's options as A/B/C/D in the chat. The variant list comes straight from the registry, so
   it is always complete and current.
2. The user types a letter per slide; defaults stand if they "approve all." On each pick, **Edit**
   that slide's `archetype:` in the `.md` to the chosen variant name.
3. **Charts:** a chart slide's "variants" are the chart types whose `takes` matches the data shape
   (e.g. allocation → `chart-donut`/`chart-pie`; a metric over categories → `chart-column`) — offer
   those. **Table:** one variant — confirm it.
4. Re-render the Pass 1 cards so the user sees the final lineup, then hand off.

## Hand off
> Prompt: `deck_generation/prompts/<slug>.deck.md` (shown above).
> Run **`/deck-gen deck_generation/prompts/<slug>.deck.md`** to build the deck.

## Rules
- **Always render in the chat** (Pass 1 cards). Never hand back only a file path.
- **Content + structure only** — no design directives; the bible owns colors/fonts/layout.
- **Be faithful to sources**; **vary structure**; **never request a chart without real numbers**.
- Keep the `.deck.md` to the `PROMPT_SPEC.md` schema — `prompt_view.py` parses it, so writer and
  reader must agree.
