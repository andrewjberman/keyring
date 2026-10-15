# TO DSGN_RBNDV2.TO-RV-b-1 -- FWD-3/FWD-5: panels and modals paint the soft off-white #F8F8FD over the #EAEAF7 ground

<to_id>DSGN_RBNDV2.TO-RV-b-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~23</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-b-1` (decomp v8 @dc7a8aa880) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- | **slot:** ~23, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-b-1` -- Andrew: "everything is blinding white" ... "Try your recommendation" (a soft off-white panel, #F8F8FD, over the #EAEAF7 page ground). Every `Panel`, `ModalFrame` and popup root paints white (`bg-[hsl(var(--bg-surface))]`, `--bg-surface: 0 0% 100%`), and the inner-surface remap block sets the nested grounds to white too. Change the PANEL tone with one new token and one rule; do NOT change `--bg-surface`, because it is also the white TEXT colour of an action-fill chip (the exception rule `color: hsl(var(--bg-surface))`) and the inner colour of the focus ring.

**Make these changes (all of them, nothing else):**
1. In `portal/src/index.css`, in the same `:root` token list that defines `--bg-surface: 0 0% 100%;` (about line 114), add the line `--bg-panel: 240 55.6% 98.2%;` with a comment that says it is the panel tone #F8F8FD (a soft off-white so the #EAEAF7 ground stays visible), read as `hsl(var(--bg-panel))`. Leave `--bg-surface` exactly as it is.
2. In `portal/src/index.css`, directly AFTER the `[data-panel-surface="light"] { --palette-white: ...; --palette-mediumGray: ...; }` block (about line 934), add an unlayered rule `[data-panel-surface="light"] { background-color: hsl(var(--bg-panel)); }` under a comment saying it repaints every panel, modal and popup root (each carries the scope attribute) and outranks the root's `bg-[hsl(var(--bg-surface))]` utility because it is unlayered.
3. In the inner-surface block `:root [data-panel-surface="light"] { ... }` (about line 948), change the five grounds `--semantic-background-contentPanel`, `--bg-medium`, `--bg-card`, `--bg-dark`, `--bg-medium-alt` from `0 0% 100%` to `var(--bg-panel)`; leave `--bg-header` and `--semantic-background-hover` as they are. Update that block's comment to say the five grounds now follow the panel tone.
4. In `portal/src/ui/components/panels/DarkCard.tsx` (about line 27) and `portal/src/ui/components/panels/SectionCard.tsx` (about line 40) change `bg-[hsl(var(--bg-surface))]` to `bg-[hsl(var(--bg-panel))]`; update the comments in `Panel.tsx` (the header comment and the `SURFACE` comment, about lines 5 and 44) to say the panel is the soft off-white `--bg-panel` over the ground; do NOT change the `SURFACE` class string of `Panel.tsx` (the scoped rule repaints it).
5. Update only the test arms that assert the old tone for `DarkCard` and `SectionCard` (about line 135 of `portal/src/ui/components/panels/__tests__/dsgn-rbndv2/rb-1-p.panel.test.tsx`: `cardTokens` must now contain `bg-[hsl(var(--bg-panel))]`); change nothing else in an existing test. Tests that assert the panel's `bg-[hsl(var(--bg-surface))]` class on `Panel`, `ModalFrame` or the popup stay true and unchanged.

**ISSUER RULING (2026-10-15 ~19:3xZ, on the worker's BLOCKING row `DSGN_RBNDV2-W23-S1`; amends item 5):** two existing arms pin the pre-cell form of the two CSS blocks this cell changes, and may be edited, only as follows. (a) `portal/src/__tests__/dsgn-rbndv2/rb-1-r.remap.test.ts`, arm RB1R-AC1 (the exact-scope rule count): the unlayered `[data-panel-surface="light"]` rules outside every `@layer` are now TWO (the palette block and the new `background-color: hsl(var(--bg-panel))` rule); change the expected count to 2 and add an assertion that one of the two declares `background-color: hsl(var(--bg-panel))` and the other still declares only the two `--palette-*` tokens. (b) `portal/src/__tests__/dsgn-rbndv2/rb-1-r2.surfaces.test.ts`, arm RB1R2-AC1 (each of the five grounds is a bare `H S% L%` triple): the five grounds now read `var(--bg-panel)`; accept exactly the value `var(--bg-panel)` for those five (and still require a bare triple for `--bg-header` and `--semantic-background-hover`). Change nothing else in either test and weaken nothing else. Gate limb that graded this amendment: none graded the modification.

**ISSUER RULING 2 (2026-10-15 ~19:5xZ, on the worker's BLOCKING row `DSGN_RBNDV2-W23-S3`):** `rb-1-r2.surfaces.test.ts` has a second count arm, the control arm (c) `checkOldRule`, which counts the unlayered exact-scope `[data-panel-surface="light"]` rules as exactly 1 and now reads 2. Edit that function (and only it) to the minimal form the worker proposed: select, among the exact-scope rules outside every `@layer`, the rules whose declarations include `--palette-white`; require exactly ONE such rule; and require that rule to declare only `--palette-white` and `--palette-mediumGray`. If the difference-control expectation `expect(checkOldRule(base).ok).toBe(false)` still holds after your edit, keep it; if your edit makes `checkOldRule(base).ok` true, drop only that one expectation and say why in a comment (the test's other base-text expectations, including `checkNewRule(base).ok` being false, stay). Change nothing else.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-8-b1.panel-tone.test.ts`, reading `src/index.css` and the two card files as text (with `@layer` and brace depth tracked; reuse the reader of `rb-4-w1.alpha-sweep.test.ts`): `--bg-panel: 240 55.6% 98.2%` is declared once; `--bg-surface: 0 0% 100%` is unchanged; the scoped rule sets `background-color: hsl(var(--bg-panel))` outside every `@layer`; the five grounds in the inner-surface block equal `var(--bg-panel)`; the action-fill exception still sets `hsl(var(--bg-surface))`; `DarkCard.tsx` and `SectionCard.tsx` hold `bg-[hsl(var(--bg-panel))]` and no `bg-[hsl(var(--bg-surface))]`; the test PRINTS `PANEL-TONE #F8F8FD` and `VERDICT: PANEL-TONE-OK` only when every arm holds; the difference control runs the same arms on `git show 3509eae8:src/index.css` and it must FAIL there.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle (unchanged by this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `3509eae8` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB8B1-AC1" cell_refs="RV-b-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~23; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-8-b1.panel-tone.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PANEL-TONE-OK</expect></criterion>
`RB8B1-AC1` -- the token is declared once with the exact triple, `--bg-surface` is unchanged, the scoped rule is unlayered, the five nested grounds follow the panel tone, the action-fill exception still uses `--bg-surface`, the two card components read `--bg-panel`, the difference control fails on the base text, and the test prints `VERDICT: PANEL-TONE-OK` only when every arm holds.

<criterion id="RB8B1-AC2" cell_refs="RV-b-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~23; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > /tmp/rb8b1-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB8B1-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB8B1-AC3" cell_refs="RV-b-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~23; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB8B1-AC3` -- every test under `src/__tests__/dsgn-rbndv2/`, `src/ui/components/panels/` and `src/ui/components/modal/` passes: the summary line reads `0 fail`.

<expected_criteria>RB8B1-AC1, RB8B1-AC2, RB8B1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/index.css
portal/src/ui/components/panels/
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v8.md</decomp_doc> v8 @dc7a8aa880, cell `RV-b-1`.
<owned_cells>RV-b-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB8B1-AC1, RB8B1-AC2, RB8B1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~23/DSGN_RBNDV2.TO-RV-b-1.panel-tone.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB8B1-AC1,RB8B1-AC2,RB8B1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W23-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v8 -- the paths of this cell are written by no other open order (the round-7 rehearsal order is complete); the files were read at the feature tip 3509eae8.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~23, direct act (round-less, one cell, LOCAL, about 40 product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 23 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md`.
