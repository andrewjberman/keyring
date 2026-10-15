# TO DSGN_RBNDV2.TO-RV-x-1 -- FWD-3, FWD-5: text on an indigo tooltip or a coloured tile stays white inside a light surface

<to_id>DSGN_RBNDV2.TO-RV-x-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~13</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>5</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-x-1` (decomp v5 @f4c4268583) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (chain 1) | **slot:** ~13, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-x-1` -- the light-surface legibility rule in `portal/src/index.css` (the block "DSGN_RBNDV2 RB-t-1 / RV-w-1 -- THE ONE LEGIBILITY RULE FOR A LIGHT PANEL", with the action-fill exception as its LAST rule) maps every `text-white`, `text-white/N`, `border-white/N` and `bg-white/N` class to ink, rule or no fill inside `[data-panel-surface="light"]`. That is right on a white ground and wrong on a coloured one. Measured on the live build: every chart tooltip in a panel or modal (the shared `DataTooltip`, the Daily Cloud hover tooltip, the Fear and Greed methodology popover) is a solid indigo box (class `bg-[hsl(var(--palette-indigo))]`) whose text classes `text-white` and `text-white/85` the rule turns navy, so it reads black on indigo (Andrew: "black on indigo tooltip doesn't make sense visually"; the tooltip text must be all white). The Trending Topics tile arrow (a `text-white` icon on a green or red gradient tile) is turned navy the same way (Andrew: "the trend arrow should be white"); that tile carries the marker attribute `data-ink="on-fill"`, added by another cell.

**Add ONE block to `portal/src/index.css`, directly AFTER the action-fill exception rule** (the one setting `color: hsl(var(--bg-surface))`), unlayered, under a comment that says what is true. For each class in this set (`text-white`; `text-white/N`, `border-white/N` and `bg-white/N` for every N in 5, 10, 15, ..., 95 (19 values)) write a rule whose selector list holds BOTH contexts, each beginning with the scope attribute:
- `[data-panel-surface="light"] .bg-\[hsl\(var\(--palette-indigo\)\)\] <class>` and `[data-panel-surface="light"] [data-ink="on-fill"] <class>` (a descendant of an indigo-filled box, or of an element marked `data-ink="on-fill"`);
- the class is written as an exact class selector with the slash escaped, e.g. `.text-white\/85`;
- declarations: `text-white` -> `color: #fff`; `text-white/N` -> `color: rgb(255 255 255 / A)`; `border-white/N` -> `border-color: rgb(255 255 255 / A)`; `bg-white/N` -> `background-color: rgb(255 255 255 / A)`; where A is `String(N / 100)` as JavaScript prints it (5 -> 0.05, 10 -> 0.1, 15 -> 0.15, 20 -> 0.2, ... 85 -> 0.85, 95 -> 0.95).
Each context adds one level of specificity over the base rule, so these win by specificity and order. Do not touch any other rule, token, chart colour or the `.dark-band` rules.

**Tests.** Write `portal/src/__tests__/dsgn-rbndv2/rb-5-x1.on-fill.test.ts`, reading `src/index.css` as text with `@layer` and brace depth tracked (reuse the reader of `rb-4-w1.alpha-sweep.test.ts`): every class in the set has the rule in BOTH contexts, outside every `@layer`, with the exact declaration; the block sits after the action-fill exception; no text contains `hsl(var(--rb-`; the test PRINTS `ON-FILL-SELECTORS <n>` (the count of selectors in the block) and `VERDICT: ON-FILL-OK` only when every arm holds; the difference control runs the same arms on `git show 7f8731df:src/index.css` (from the portal root) and they must FAIL there. `rb-4-w1.alpha-sweep.test.ts` and `rb-1-t.tokens.test.ts` must still pass: amend only an arm that the new block makes wrong (for instance a count that now includes the new selectors), and say so in your report.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. The design principle Andrew gave for this round: text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `7f8731df` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB5X1-AC1" cell_refs="RV-x-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~13; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-5-x1.on-fill.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ON-FILL-OK</expect></criterion>
`RB5X1-AC1` -- reading `src/index.css` as text, every class of the set has the exact rule in both contexts after the action-fill exception, none inside an `@layer`, the difference control fails on the base text, and the test prints `VERDICT: ON-FILL-OK` only when every arm holds.

<criterion id="RB5X1-AC2" cell_refs="RV-x-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~13; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB5X1-AC2` -- every test under `src/__tests__/dsgn-rbndv2/` passes after your edit: the summary line reads `0 fail`.

<criterion id="RB5X1-AC3" cell_refs="RV-x-1" judgment="true"/>
`RB5X1-AC3` -- graded by the COO's live read at the drain, then the CVO and Andrew (DEC-5), never self-graded: the computed text colour of the tooltip text is white in the Index Performance history modal, the Global RSI panel and the Daily Cloud panel. RECORD; no verdict.

<expected_criteria>RB5X1-AC1, RB5X1-AC2, RB5X1-AC3</expected_criteria>

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
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v5.md</decomp_doc> v5 @f4c4268583, cell `RV-x-1`.
<owned_cells>RV-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB5X1-AC1, RB5X1-AC2, RB5X1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~13/DSGN_RBNDV2.TO-RV-x-1.on-fill-ink.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB5X1-AC1,RB5X1-AC2,RB5X1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB5X1-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W13-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v5 -- the paths of this cell are written by no other order of the round (disjoint write sets; `portal/src/__tests__/dsgn-rbndv2/` holds one new test file per cell); the files were read at the feature tip 7f8731df.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~13, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 13 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md`.
