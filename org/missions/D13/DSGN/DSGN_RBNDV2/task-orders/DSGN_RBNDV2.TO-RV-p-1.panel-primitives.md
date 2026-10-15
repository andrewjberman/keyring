# TO DSGN_RBNDV2.TO-RV-p-1 -- FWD-3: the panel primitives in the A-light fixture, prop API unchanged

<to_id>DSGN_RBNDV2.TO-RV-p-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~3</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>1</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-p-1` (decomp v1 @b475e9badc) | **outcome_ref:** FWD-3 | **depends_on:** -- (chain 3) | **slot:** ~3, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-p-1` -- THE PANEL PRIMITIVES in the "A light" fixture (FWD-3, C-PANEL).

Edit the primitives in `portal/src/ui/components/panels/` so every panel renders the fixture's panel section, and change NO prop: every exported prop interface, every default and every call shape stays exactly as it is, because 96 page files import `Panel` and 85 import `PanelHeader` and none may be edited.

`Panel.tsx`: in EVERY variant (`chart`, `nested`, `mixed`, `heatmap`) the root is the white surface `bg-[hsl(var(--bg-surface))]` with a 1px border `border-[hsl(var(--hairline))]`, square corners (no `rounded-lg`; at most the 2px hairline radius), no shadow, and it carries the attribute `data-panel-surface="light"` (a sibling cell keys a legibility rule on that exact attribute and value). The band-valued `chart`/`mixed` surfaces and the `--bg-header` use go. Update the variant comment block to say what is now true.

`PanelHeader.tsx`: drop the navy strip (`bg-[hsl(var(--bg-header))]`, `border-white/10`, `rounded-t-[4px]`, `text-white`), the bold uppercase title and the `HelpCircle` title pattern (keep a help affordance only if a prop already drives it, as a quiet icon button on the right, not in the title). The title is the fixture's eyebrow: 11px, 700, letter-spacing 0.14em, uppercase, `--rb-ink-2`, with a 2px `--rb-accent` bottom border and 4px padding below; an optional number renders before it in `--rb-quiet` 12px; the actions slot sits on the right; the header has padding `22px 30px 16px` and a 1px `--rb-rule` rule below. Keep the existing rule that a title never overlaps its actions at high zoom (wrap, `flex-wrap`).

`PanelContent.tsx`: padding `24px 30px`, no `rounded-b-lg`, no inset box. `PanelFooter.tsx` and `SmartPanelFooter.tsx`: the source caption is 11px, uppercase, letter-spacing 0.08em, `--rb-quiet`, above a 1px `--rb-rule` rule, with margin `0 30px` and padding `10px 0 14px`; no navy footer strip. `NestedCard.tsx`, `SectionCard.tsx`, `DarkCard.tsx`: render the same white surface and hairline with no box inside a box.

The sibling cells define `--rb-*` (a token cell) and repoint `--bg-page`; build against the names. **Out of this cell:** `index.css`, every page and component outside `src/ui/components/panels/`, `PanelExamples.tsx` and the panels README.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's (DEC-1 to DEC-5 of the PRD): you reproduce the fixture and invent nothing. Colours are read from tokens (`--bg-page`, `--hairline`, `--bg-surface`, the `--rb-*` family), never typed as a literal in a component, except where this cell says a literal is the point. Charts keep their colour (C6).

**Environment (every cell):** the portal worktree is `<WS>/portal`, based on the feature branch `feature/dsgn-rbndv2-light` at `ad7c100b5c` (= origin DEV when it was cut). The fixture you build to is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md` (read it first; it carries every value you need, so do not open the board URL). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints its VERDICT line only when every arm holds. Do not start any server: dev builds run on port 5174 only and 5174 serves the main checkout, not your worktree. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11); Lato; no non-ASCII in code.

### ACCEPTANCE

<criterion id="RB1P-AC1" cell_refs="RV-p-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~3; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/panels/__tests__/dsgn-rbndv2/rb-1-p.panel.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: PANEL-LIGHT-OK</expect></criterion>
`RB1P-AC1` -- rendering `Panel` in each of its four variants with `PanelHeader` (a title, a number and one action), `PanelContent` and a footer to static markup: every variant's root carries `data-panel-surface="light"`, the `--bg-surface` ground and the `--hairline` border; no markup in any variant contains `shadow`, `rounded-lg`, `--bg-header`, `--bg-band` or an inset box (a bordered element directly inside the content wrapper); the header title element carries the 2px `--rb-accent` bottom border; the title and the action are siblings that can wrap. The test prints `VERDICT: PANEL-LIGHT-OK` only when every arm holds.

<criterion id="RB1P-AC2" cell_refs="RV-p-1"><invocation>cd <WS>/portal && git diff --name-only ad7c100b5c..HEAD -- src/pages src/components | wc -l</invocation><expect>0</expect></criterion>
`RB1P-AC2` -- no page file and no file under `src/components` differs from the branch base once your commits are in: the count printed is 0 (C-PANEL: the primitives change, no page file is edited). At the base the same command prints 0 as well, which is the control that the command measures the right surface.

<criterion id="RB1P-AC3" cell_refs="RV-p-1" judgment="true"/>
`RB1P-AC3` -- graded at the round-1 drain by Andrew's eye on `/market` (DEC-5), never self-graded and never by the CVO: the panels read as the "A light" board's panels (white, thin silver edge, eyebrow title with the violet underline, quiet source caption, no stacked dark strips, no box inside a box). RECORD; no verdict.


<expected_criteria>RB1P-AC1, RB1P-AC2, RB1P-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can. The `--rb-*` tokens and `--bg-page`'s new value are written by a sibling cell and land at the merge; build against the names.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/ui/components/panels/Panel.tsx
portal/src/ui/components/panels/PanelHeader.tsx
portal/src/ui/components/panels/PanelContent.tsx
portal/src/ui/components/panels/PanelFooter.tsx
portal/src/ui/components/panels/SmartPanelFooter.tsx
portal/src/ui/components/panels/NestedCard.tsx
portal/src/ui/components/panels/SectionCard.tsx
portal/src/ui/components/panels/DarkCard.tsx
portal/src/ui/components/panels/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP.md</decomp_doc> v1 @b475e9badc, cell `RV-p-1`.
<owned_cells>RV-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB1P-AC1, RB1P-AC2, RB1P-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~3/DSGN_RBNDV2.TO-RV-p-1.panel-primitives.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB1P-AC1,RB1P-AC2,RB1P-AC3` BEFORE the flip. `RB1P-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming Andrew's read at the drain (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v1 section 6).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v1 -- every named existing file measured present at origin DEV ad7c100b5c; the write sets are pairwise disjoint (decomp v1 section 3 and 5).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~3, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_RBNDV2 3 --portal-ref feature/dsgn-rbndv2-light`.
