# TO DSGN_RBNDV2.TO-RV-i-1 -- FWD-3: the inset cards of Trending Topics and Top/Bottom Performers become hairline sections, at the primitives

<to_id>DSGN_RBNDV2.TO-RV-i-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~9</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>2</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-i-1` (decomp v2 @95d724679e) | **outcome_ref:** FWD-3 | **depends_on:** -- (chain 2) | **slot:** ~9, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-i-1` -- THE INSET CARDS BECOME HAIRLINE SECTIONS (FWD-3, C-PANEL "no box inside a box"; CVO grade `RB1P-AC3` NOT MET on this one clause).

On `/market`, Trending Topics and Top/Bottom Performers each frame two bordered inset cards with a coloured left bar inside the white panel (Bullish/Bearish Drivers, Top/Bottom Performers). They are built from the primitives `NestedCard` (`portal/src/ui/components/panels/NestedCard.tsx`: `bg-[hsl(var(--bg-surface))] border border-[hsl(var(--hairline))] p-4`, an absolutely positioned `w-1` accent bar when `accentColor` is set) inside `PanelGrid` (`PanelGrid.tsx`: a `grid` with `xl:grid-cols-2` and a gap). Fix it AT THE PRIMITIVES, so no page file is edited (the CTO's round-1 analysis named a per-file edit; the issuer rules the primitive cheaper and wider, and `NestedCard` has two real users, `ExecutiveSummary.tsx` and `AdvisorPublicProfile.tsx`):

- `NestedCard` renders a SECTION, not a box: no border box, no fill, no left accent bar, no radius; it keeps its props (`children`, `accentColor`, `className`) so every caller compiles unchanged, `accentColor` is still accepted and now only sets a data attribute (`data-accent`) and no visual. It carries `data-panel-surface="light"` is NOT needed (it sits inside a panel that already does).
- Sections are separated by hairlines in `var(--rb-rule)`: a 1px top rule on a section that follows another in a stacked layout, and a 1px vertical rule between the two columns of a 2-column `PanelGrid` at the `xl` breakpoint; implement this in `PanelGrid` (for example `xl:divide-x` with the rule colour, and horizontal `divide-y` below `xl`) and in `NestedCard` padding, so a `NestedCard` outside a `PanelGrid` is still a clean section.
- `SectionCard.tsx` and `DarkCard.tsx` are NOT touched.

**Out of this cell:** every file outside `portal/src/ui/components/panels/` (NestedCard, PanelGrid and your tests), `ExecutiveSummary.tsx` (read only: the proof of use), `PanelExamples.tsx` and the panels README.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's: you reproduce the fixture and invent nothing. TOKEN FORMATS (a defect in round 1 came from mixing them): the `--rb-*` tokens (`--rb-rule`, `--rb-row-rule`, `--rb-ink`, `--rb-ink-2`, `--rb-ink-3`, `--rb-quiet`, `--rb-accent`) are HEX values, so you read them as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`; `--bg-surface`, `--bg-page`, `--hairline` and the `--semantic-*` tokens are HSL triples, so you read them as `hsl(var(--X))`. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11), no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. You are given the worker face only: open your order file only to edit its status or amend a criterion the issuer has ruled on, and do NOT read anything below its `## RECORD FACE` line.

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `adc70061` (the difference-control base). The fixture is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md`; read it first. Round 1 is merged on the branch: the `--rb-*` tokens, the ground `#EAEAF7`, the white panel primitives, and two scoped rules keyed on `data-panel-surface="light"` (text-white idioms resolve to navy ink; the old dark surface tokens resolve to white and silver). An element carrying `data-panel-surface="light"` therefore reads as a light surface for everything inside it. Do not start any server.

### ACCEPTANCE

<criterion id="RB2I1-AC1" cell_refs="RV-i-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~9; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/panels/__tests__/dsgn-rbndv2/rb-2-i1.sections.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: SECTIONS-OK</expect></criterion>
`RB2I1-AC1` -- rendering `NestedCard` (with and without `accentColor`) and a 2-column `PanelGrid` holding two `NestedCard`s to static markup: no `NestedCard` element carries `border` on four sides, a `bg-` fill class, `rounded`, or an absolutely positioned bar (no element with `absolute` and `w-1`); `accentColor` leaves a `data-accent` attribute and no visual class; the `PanelGrid` markup carries a divider class keyed on the `--rb-rule` token written as `var(--rb-rule)` (and the text `hsl(var(--rb-` appears in neither file); the prop interfaces still export `NestedCardProps` with `children`, `accentColor`, `className` and `PanelGridProps` with `cols`, `gap`, `children`, `className` (difference control: the same arms run on `git show adc70061:src/ui/components/panels/NestedCard.tsx` from the portal root must FAIL the no-fill arm, proving the test can fail). The test prints `VERDICT: SECTIONS-OK` only when every arm holds.

<criterion id="RB2I1-AC2" cell_refs="RV-i-1"><invocation>cd <WS>/portal && git diff --name-only adc70061..HEAD -- src/pages src/components | wc -l</invocation><expect>0</expect></criterion>
`RB2I1-AC2` -- no page file and no file under `src/components` differs from the branch base once your commits are in: the count printed is 0 (the fix is at the primitives). At the base the same command prints 0, which is the control that it measures the right surface.

<criterion id="RB2I1-AC3" cell_refs="RV-i-1" judgment="true"/>
`RB2I1-AC3` -- graded by the COO's close walk of `/market` and then the CVO and Andrew (DEC-5), never self-graded: Trending Topics and Top/Bottom Performers read as hairline-divided sections with no bordered inset card and no coloured left bar. RECORD; no verdict.


<expected_criteria>RB2I1-AC1, RB2I1-AC2, RB2I1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/ui/components/panels/NestedCard.tsx
portal/src/ui/components/panels/PanelGrid.tsx
portal/src/ui/components/panels/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v2.md</decomp_doc> v2 @95d724679e, cell `RV-i-1`.
<owned_cells>RV-i-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB2I1-AC1, RB2I1-AC2, RB2I1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~9/DSGN_RBNDV2.TO-RV-i-1.hairline-sections.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB2I1-AC1,RB2I1-AC2,RB2I1-AC3` BEFORE the flip, run from inside your worktree. `RB2I1-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's close walk and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W9-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v2 -- every named existing file measured present at the feature branch adc70061; write sets are pairwise disjoint (decomp v2 section 3).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~9, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 9 --portal-ref feature/dsgn-rbndv2-light`.
