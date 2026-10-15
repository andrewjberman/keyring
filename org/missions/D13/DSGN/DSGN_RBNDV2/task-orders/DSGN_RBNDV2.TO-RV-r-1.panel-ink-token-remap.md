# TO DSGN_RBNDV2.TO-RV-r-1 -- FWD-3/FWD-1: controls inside a light panel read navy, not pale (DIRECT-ACT, surprise row S2)

<to_id>DSGN_RBNDV2.TO-RV-r-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~5</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-r-1` (decomp v1 addendum 1) | **outcome_ref:** FWD-3, FWD-1 | **depends_on:** -- (direct act) | **slot:** ~5, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-r-1` -- on `/market`, inside the white panels, the shared `Segmented` period chips and `Button` ground-`band` variants read pale. `portal/src/ui/components/Controls.tsx` spells the band-ground ink as `text-[hsl(var(--palette-white))]` (active chip, secondary and ghost buttons) and `text-[hsl(var(--palette-mediumGray))]` (idle chip); the theme defines `--palette-white: 222 38% 93%` and `--palette-mediumGray: 220 18% 71%` at `:root` (`portal/design/themes/opal-capital.css`). A white panel (it now carries `data-panel-surface="light"` on its root) makes both unreadable.

Add ONE unlayered rule block to `portal/src/index.css` (outside every `@layer`, next to the existing `[data-panel-surface="light"]` legibility rules the tokens cell added): selector exactly `[data-panel-surface="light"]`, declaring only `--palette-white` as the `H S% L%` triple of the navy ink `#0A1733` and `--palette-mediumGray` as the triple of the quiet ink `#4A5878`, the same triple format as the theme (`220 18% 71%`; integer or two-decimal percentages are fine if they resolve within 1/255 per channel). A custom property set on the panel root is inherited by every control inside it, so nothing else needs to move. Do not edit `Controls.tsx`, the theme file, the legibility rules already in `index.css`, or any page file.

**Out of this cell:** every file except `portal/src/index.css` and your test.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. Colours stay token-defined; no shadow; radii 2/3/4px only (`portal/DESIGN.md` C11); no non-ASCII in code.

**Environment:** the portal worktree is `<WS>/portal`, based on the feature branch `feature/dsgn-rbndv2-light` at `d2a3c2fe`. The fixture's inks are in `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md`. The criterion's test file does not exist at the base: you write it from the criterion's text, and it prints its VERDICT line only when every arm holds. Do not start any server.

### ACCEPTANCE

<criterion id="RB1R-AC1" cell_refs="RV-r-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~5; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-1-r.remap.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PALETTE-REMAP-OK</expect></criterion>
`RB1R-AC1` -- reading `src/index.css` as text with brace depth and `@layer` nesting tracked: a rule whose selector is exactly `[data-panel-surface="light"]` exists OUTSIDE every `@layer`; it declares `--palette-white` and `--palette-mediumGray` as HSL triples that resolve to `#0A1733` and `#4A5878` (each channel within 1/255) and declares nothing else; (difference control: the same text checks run against `git show d2a3c2fe:portal/src/index.css` report the rule absent, proving the test can fail). The test prints `VERDICT: PALETTE-REMAP-OK` only when every arm holds.

<criterion id="RB1R-AC2" cell_refs="RV-r-1" judgment="true"/>
`RB1R-AC2` -- graded at the round-1 close run by `2.0.0_SA_COO~RB` on the headless `/market` render, and then by Andrew's eye (DEC-5), never self-graded and never by the CVO: the Period chips and the panel-header buttons read as navy ink on the white panel. RECORD; no verdict.

<expected_criteria>RB1R-AC1, RB1R-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/index.css
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP.md</decomp_doc> v1 addendum 1, cell `RV-r-1`.
<owned_cells>RV-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB1R-AC1, RB1R-AC2. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~5/DSGN_RBNDV2.TO-RV-r-1.panel-ink-token-remap.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB1R-AC1,RB1R-AC2` BEFORE the flip. `RB1R-AC2` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~RB`'s close run and Andrew's read (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at the addendum -- `src/index.css` is written by no other cell now open (the tokens cell is merged at 80d45ff8; the heat cell does not write it).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~5, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_RBNDV2 5 --portal-ref feature/dsgn-rbndv2-light`.
