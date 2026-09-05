---
name: deck-gen
description: Generate a brand-compliant, fidelity-checked Opal .pptx from a `*.deck.md` prompt file: compose, lint against DESIGN_BIBLE.md, verify slide count and line coverage, render and QA every slide, drop on the Desktop with a report. Use on `/deck-gen <prompt.deck.md>` or "build the deck". Pair: `/deck-prompt` writes the file this consumes.
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
   deck. **Run it from `deck_generation/` with the package on the path** —
   `cd deck_generation && PYTHONPATH=. python <build_script>.py`
   (PowerShell: `$env:PYTHONPATH='.'; python <build_script>.py`). Without the path set,
   the import dies with `ModuleNotFoundError: No module named 'engine'`. There is **no
   `SLIDE_LIBRARY_PATH` to export** — compose.py loads the Slide Library from a fixed
   path. Keep build scripts beside the references in `dev/scripts/`.
   ```python
   from engine.compose import Deck, C, NAVY, PURPLE   # etc.
   d = Deck()
   d.set_cover(title, subtitle, tag)                  # reuses the master cover (F4)
   s = d.slide("panels"); C.eyebrow(s, "Header"); C.panels(s, [(h,b),(h,b),(h,b)])
   d.need(2, "header", "key phrase", ...)             # one need() per slide w/ its tokens
   ...
   report = d.finalize(out_path)                      # raises on any gate failure
   ```
   - **The archetype catalog is the single source of truth (`engine/registry.py`)** — run
     `python -m engine.compose --catalog`. For every archetype it prints the name, what it
     `takes`, the item range, the **call** (the method), and an example. Build straight from
     that — do **not** work from a remembered archetype list.
   - **Two calling conventions — the catalog's `call` column tells you which:**
     - **Core** (call shown as `C.<m>` or `d.set_cover`) → `from engine.compose import Deck, C`,
       then `C.<m>(s, ...)` (e.g. `C.panels`, `C.grid`, `C.compare`, `C.table`, `C.statcards`,
       `C.vsteps`, `C.flow`, `C.list_accent`, `C.list_sidebar`, `C.statement`, `C.stat`), or
       `d.set_cover(...)` for the cover.
     - **Family** (call shown as `archetypes.<family>.<func>`) → `from engine.archetypes.<family>
       import <func>`, then `<func>(s, ...)` — or `<func>(d, ...)` for `cover-*` variants. The
       one multi-module family is **charts**: import from its submodule, e.g.
       `from engine.archetypes.charts.scatter import chart_scatter_riskreturn`. If an import
       errors, `grep -rln "def <func>" engine/archetypes/` locates its exact module; the
       per-family `dev/scripts/showcase_<family>.py` builds are working references.
   - Use `C.eyebrow(s, "HEADER")` on every content slide. Compose a custom layout from the
     `C` primitives only when no archetype fits — keep it bible-clean.
   - **Harvested case-study primitives (2026-06-17, from the Cottonwood-vs-Goldman deck):**
     KPI/comparison row→`C.statcards([(big,label,vs,takeaway), …])` (vs/takeaway optional;
     uniform navy top-band + one big-number size; pass `x0,x1` to span a half-slide for a
     2-up); list + filled panel→`C.list_accent([(label,desc), …])` on the left **paired with**
     `C.sidebar(eyebrow,head,body)` on the right (`list_accent(panel=True)` draws row cards
     and stands alone — use it when there is no sidebar, e.g. a full-width concern list);
     feature grid→`C.grid([(head,desc), …], cols=2)` (partial last row auto-fills its width —
     no dead cell); comparison/holdings table→`C.table(headers, rows, first_col_w=…)` (navy
     header, zebra body, navy-bold first column; A1-palette fills only). Reference build that
     exercises all five: `deck_generation/dev/scripts/cw_goldman_build.py` (11 slides, 0
     violations, 10/10 coverage).
   - **Variety by default (D11).** Do NOT render the bare family primary across the deck — pick
     the best-*fitting* variant per slide, and when a family repeats, use a *different* variant each
     time (4 compares → `compare` / `compare-balance` / `compare-venn` / …; 3 statcards →
     `statcards-clean` / `statcards-delta` / `statcards-strip`). The **cover stays the master**
     (`set_cover`, the photo cover — the recommended default; it is D11-exempt). `finalize` FAILS a
     deck that uses one variant for a family it repeats ≥3× — variety is the default, not a Pass-2
     afterthought. If the `.deck.md` hands you bare primaries on a repeated family, upgrade them to
     varied best-fit variants as you build.
   - **Charts only from supplied data (F2).** If the slide has no `data:` line, render
     its figures as `C.stat` (stat-as-type), never a chart.
   - **Cover the lines (F3).** Put every content line on its slide and register it via
     `d.need(...)`. Tighten/rephrase is fine; dropping or inventing is not.

3. **Gate (automatic in `finalize`).** `finalize()` runs the [AUTO] `design_lint`
   (D1–D11, A/B/C rules — incl. D11 variant-variety) + the fidelity coverage check and
   **raises** on any violation or uncovered line. Read the message, fix the build script,
   re-run until it returns a clean report (0 violations, full coverage, slide count == prompt).
   A D11 failure means a repeated family is using one variant — swap some occurrences to
   different best-fit variants.

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
