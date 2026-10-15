# TO DSGN_RBNDV2.TO-RV-t-1 -- FWD-2/FWD-3: the #EAEAF7 ground at its source, the --rb tokens and the one panel legibility rule

<to_id>DSGN_RBNDV2.TO-RV-t-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~1</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>1</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-t-1` (decomp v1 @b475e9badc) | **outcome_ref:** FWD-2, FWD-3 | **depends_on:** -- (chain 1) | **slot:** ~1, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-t-1` -- THE TOKENS AND THE ONE LEGIBILITY RULE (FWD-2, FWD-3; surprise row `DSGN_RBNDV2-S1`).

(a) The portal canvas becomes `#EAEAF7` AT ITS SOURCE. `portal/src/index.css` names `portal/design/brands/opal-capital.json` (the `canvas` palette entry) as the one writer and `portal/design/themes/opal-capital.css` (`--palette-canvas`, currently `220 37.5% 96.86%` = `#F4F6FA`) as its generated output: edit the JSON, regenerate the theme with the repo's own generator (the theme file's header names it; find it, run it, and do not hand-edit the generated file alone), so `--palette-canvas` resolves to `rgb(234, 234, 247)`. `--bg-page` and `--background` already follow it. Update only the `index.css` comments that sit inside a block you edit and that call the canvas `#F4F6FA`.

(b) Add exactly these seven hex-valued custom properties to the `:root` block of `portal/src/index.css`: `--rb-rule: #E3E7EF`, `--rb-row-rule: #EEF1F6`, `--rb-ink: #0A1733`, `--rb-ink-2: #163372`, `--rb-ink-3: #4A5878`, `--rb-quiet: #6B7590`, `--rb-accent: #5F3BE3`. Two sibling cells (the sidebar and the panel primitives) build against these NAMES and the existing `--bg-page`, `--hairline`, `--bg-surface`; the merge lands your cell first.

(c) ONE legibility rule. The panel primitive (a sibling cell) puts `data-panel-surface="light"` on every panel root and turns every panel variant white. Page bodies written for the old dark container use `text-white`, `text-white/N`, `border-white/N` and `bg-white/N`, which read invisible on white (140, 92 and 96 page files respectively). Write ONE rule block in `portal/src/index.css`, OUTSIDE every `@layer` (Tailwind v4 utilities live in a native layer and a layered rule loses; see the existing unlayered `.dark-band [data-panel-state]` rule near the end of the file for the precedent), whose every selector begins with `[data-panel-surface="light"]` and which makes, inside that scope only: `text-white` and `text-white/N` resolve to `var(--rb-ink)`; `border-white/N` resolve to `var(--rb-rule)`; `bg-white/N` resolve to no fill (`transparent`). Do not touch the `.dark-band` scope, any chart colour, or anything outside the attribute scope.

**Out of this cell:** the sidebar, the panel files, every heat colour, and every page file.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's (DEC-1 to DEC-5 of the PRD): you reproduce the fixture and invent nothing. Colours are read from tokens (`--bg-page`, `--hairline`, `--bg-surface`, the `--rb-*` family), never typed as a literal in a component, except where this cell says a literal is the point. Charts keep their colour (C6).

**Environment (every cell):** the portal worktree is `<WS>/portal`, based on the feature branch `feature/dsgn-rbndv2-light` at `ad7c100b5c` (= origin DEV when it was cut). The fixture you build to is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md` (read it first; it carries every value you need, so do not open the board URL). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints its VERDICT line only when every arm holds. Do not start any server: dev builds run on port 5174 only and 5174 serves the main checkout, not your worktree. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11); Lato; no non-ASCII in code.

### ACCEPTANCE

<criterion id="RB1T-AC1" cell_refs="RV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~1; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-1-t.tokens.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: TOKENS-OK</expect></criterion>
`RB1T-AC1` -- reading `src/index.css` as text, the seven `--rb-*` properties are present in `:root` with exactly the seven hex values above; the legibility rule exists OUTSIDE every `@layer` block (the test tracks brace depth and `@layer` nesting); every selector of that rule begins with `[data-panel-surface="light"]` (difference control: the test also asserts that no selector in the rule targets `text-white` without that prefix); and the rule sets `color` for the `text-white` family to `var(--rb-ink)`. The test prints `VERDICT: TOKENS-OK` only when every arm holds.

<criterion id="RB1T-AC2" cell_refs="RV-t-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~1; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-1-t.canvas.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CANVAS-SOURCE-OK</expect></criterion>
`RB1T-AC2` -- the canvas in `design/brands/opal-capital.json` and `--palette-canvas` in `design/themes/opal-capital.css` BOTH resolve to `#EAEAF7` (each channel within 1/255 of 234, 234, 247) and neither still holds the `#F4F6FA` value as the canvas (difference control: the same test run against `git show ad7c100b5c:portal/design/themes/opal-capital.css` content must report the old value, proving the test can fail). The test prints `VERDICT: CANVAS-SOURCE-OK` only when every arm holds.


<expected_criteria>RB1T-AC1, RB1T-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can. The generator the theme header names is run, not edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/design/brands/opal-capital.json
portal/design/themes/opal-capital.css
portal/src/index.css
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP.md</decomp_doc> v1 @b475e9badc, cell `RV-t-1`.
<owned_cells>RV-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB1T-AC1, RB1T-AC2. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~1/DSGN_RBNDV2.TO-RV-t-1.tokens-and-ink-rule.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB1T-AC1,RB1T-AC2` BEFORE the flip. No judgment criterion on this cell.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v1 section 6).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v1 -- every named existing file measured present at origin DEV ad7c100b5c; the write sets are pairwise disjoint (decomp v1 section 3 and 5).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~1, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_RBNDV2 1 --portal-ref feature/dsgn-rbndv2-light`.
