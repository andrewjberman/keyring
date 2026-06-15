---
name: deck-gen
description: Generate a brand-compliant, fidelity-checked Opal PowerPoint (.pptx) from a deck-prompt file (`*.deck.md`). Runs the brand-derivative composer (engine/compose.py) — compose from primitives, enforce DESIGN_BIBLE.md via the [AUTO] linter, verify slide-count + line-coverage fidelity, render to images via PowerPoint COM, visually QA every slide, and drop the deck on the Desktop with a report. Use when the user says `/deck-gen <prompt.deck.md>`, asks to "generate/build the deck" from a prompt, or to turn a `*.deck.md` into slides. Pair skill: `/deck-prompt` writes the prompt file this consumes.
---

# /deck-gen — build a deck from a prompt file

Turns a `*.deck.md` (see `deck_generation/PROMPT_SPEC.md`) into a finished `.pptx`,
gated by the design bible and the fidelity contract. **You drive the composer; the
gates decide whether it ships.**

**Input:** a path to a `*.deck.md`. If none given, ask for one (or suggest `/deck-prompt`
to create one). Read `deck_generation/DESIGN_BIBLE.md` and `PROMPT_SPEC.md` first — they
are law.

## Process

1. **Parse the prompt.** Read the `*.deck.md`: deck meta (title/audience/goal) + the
   ordered `## Slide N` blocks. The block count is the target slide count. For each
   slide capture its `archetype`, `title`, and every content line (bullets, subtitle,
   footer, quote) — these are the **fidelity tokens** the output must cover.

2. **Compose.** Write a short build script that imports the library and lays out the
   deck. Work in `cd deck_generation` with `export SLIDE_LIBRARY_PATH=...` set.
   ```python
   from engine.compose import Deck, C, NAVY, PURPLE   # etc.
   d = Deck()
   d.set_cover(title, subtitle, tag)                  # reuses the master cover (F4)
   s = d.slide("panels"); C.eyebrow(s, "Header"); C.panels(s, [(h,b),(h,b),(h,b)])
   d.need(2, "header", "key phrase", ...)             # one need() per slide w/ its tokens
   ...
   report = d.finalize(out_path)                      # raises on any gate failure
   ```
   - **Map archetype → primitive:** cover→`set_cover`; panels→`C.panels`; flow→`C.flow`;
     compare→`C.compare`; fork→ two tiles + an OR `C.circle`; vsteps→`C.vsteps`;
     formula→`C.formula`; statement→`C.statement` (dark slide); stat-row→`C.stat` ×N;
     thesis-stat→ text + `C.stat`; rows→ labelled rows. Use `C.eyebrow` on every content
     slide. Compose custom layouts from primitives when an archetype doesn't fit — but
     keep it bible-clean.
   - **Charts only from supplied data (F2).** If the slide has no `data:` line, render
     its figures as `C.stat` (stat-as-type), never a chart.
   - **Cover the lines (F3).** Put every content line on its slide and register it via
     `d.need(...)`. Tighten/rephrase is fine; dropping or inventing is not.

3. **Gate (automatic in `finalize`).** `finalize()` runs the [AUTO] `design_lint`
   (D1–D10, A/B/C rules) + the fidelity coverage check and **raises** on any violation
   or uncovered line. Read the message, fix the build script, re-run until it returns
   a clean report (0 violations, full coverage, slide count == prompt).

4. **Render + visual QA (the [QA] gate).** Render every slide to PNG via PowerPoint COM
   and inspect each against the bible's [QA] rules (60-30-10, white-on-white, body
   orphans, grid alignment, space utilization, motif-fits-subject, no two consecutive
   identical formats, restraint). Assume there are problems; fix and re-render until a
   full pass is clean.
   ```powershell
   $ppt = New-Object -ComObject PowerPoint.Application
   $pres = $ppt.Presentations.Open($src,$true,$false,$false)
   $pres.Export($outdir,"PNG",1500,844); $pres.Close(); $ppt.Quit()
   ```
   Then Read the PNGs and look. (LibreOffice/poppler are NOT installed here — COM is the
   render path.)

5. **Deliver.** Copy the final `.pptx` to the Desktop. Report: slide count vs prompt,
   `LINT: 0 violations`, coverage `N/N`, and a one-line note on any [QA] fixes made.

## Rules (non-negotiable)
- **The gates are the product.** Never hand the user a deck that didn't pass `finalize`
  clean AND a visual-QA pass. A deck that breaks an [AUTO] rule cannot be saved.
- **Fidelity is exact** — same slide count as the prompt, every content line covered, no
  invented data or charts.
- **Design is the bible's job, not the prompt's** — never read colors/fonts/layout from
  the prompt; they come from `DESIGN_BIBLE.md` and are linted.
- Reference build that exercises the whole pipeline: `.runtmp/brand_deck_v4.py`
  (Jim's advisor deck; 13 slides, 0 violations, 87/87 coverage).
