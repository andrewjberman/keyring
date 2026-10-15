# TO DSGN_RBNDV2.TO-RV-x-3 -- FWD-3, FWD-5: the Global RSI panel reads on white and its modal copy and dropdown are right

<to_id>DSGN_RBNDV2.TO-RV-x-3</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~15</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>5</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-x-3` (decomp v5 @f4c4268583) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (chain 3) | **slot:** ~15, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-x-3` -- three defects Andrew measured in the Global RSI panel and its modal, all in two files.

(1) **The panel's chart labels are white on white** (Andrew: "RSI panel labels with white on white are illegible"). `portal/src/components/market-performance/RSIBars.tsx` draws literal whites that the stylesheet rule cannot reach (they are SVG and chart props, not classes): the previous-day marker (about lines 112-135: `stroke="white"` on the dashed line, `fill="rgba(255,255,255,0.8)"` on the triangle, `fill="rgba(255,255,255,0.7)"` on the period label text), the x-axis tick `fill: 'rgba(255,255,255,0.5)'` and `axisLine` stroke `rgba(255,255,255,0.1)` (about lines 255-262), the y-axis category tick `fill: 'rgba(255,255,255,0.8)'` (about line 267), the tooltip cursor `fill: 'rgba(255,255,255,0.05)'` (about line 287) and each bar cell's `stroke="rgba(255,255,255,0.15)"` (about line 310). Replace each: the dashed marker line and the triangle sit over a coloured bar, so they read `var(--rb-ink)`; the period label text `var(--rb-ink-3)`; the x-axis tick `var(--rb-ink-3)` and its axis line `var(--rb-rule)`; the y-axis category tick `var(--rb-ink)`; the cursor `rgba(10, 23, 51, 0.05)`; the cell stroke `rgba(10, 23, 51, 0.15)`. Leave the bar glow filter and the red and green reference lines (30 and 70) as they are.

(2) **A value reads in capitals.** In `portal/src/components/market-performance/RSIModal.tsx`, the Trend stat in the Full view (about lines 1051-1070) prints `COOLING DOWN` (and a sibling value for a rising trend, and a neutral value, spelled in capitals the same way). Andrew: "'Trend' value on RSI Modal Popup in 'Full' toggle view should be proper capitalized". Change every Trend value string to title case ('Cooling Down', 'Heating Up', and the neutral value in the same style) and remove any `uppercase` class or `toUpperCase` call that capitalises the VALUE (the small stat LABELS such as "Trend" keep their own styling).

(3) **The Asset Class dropdown is too narrow.** In `RSIModal.tsx`, the first `<select>` of the controls row (about lines 946-962, `Asset Class:`) lets its caret sit on top of the value "Fixed Income". Give that select `pr-9` and `min-w-[10rem]` (keep its other classes) so the caret has its own room; give the Category select beside it the same `pr-9`.

Do not change any other colour, chart or data code.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. The design principle Andrew gave for this round: text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `7f8731df` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB5X3-AC1" cell_refs="RV-x-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~15; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-5-x3.rsi-ink.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: RSI-INK-OK</expect></criterion>
`RB5X3-AC1` -- `RSIBars.tsx` holds no `rgba(255,255,255` and no `stroke="white"`, `RSIModal.tsx` holds `Cooling Down` and no `COOLING DOWN`, and the Asset Class select carries `pr-9` and `min-w-[10rem]`; the before and after counts of white literals in `RSIBars.tsx` print (`RSI-WHITE-BEFORE <n> RSI-WHITE-AFTER <m>`, the base read by `git show 7f8731df:src/components/market-performance/RSIBars.tsx`); the difference control fails on the base text; the test prints `VERDICT: RSI-INK-OK` only when every arm holds.

<criterion id="RB5X3-AC2" cell_refs="RV-x-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~15; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB5X3-AC2` -- every test under `src/__tests__/dsgn-rbndv2/` passes after your edit: the summary line reads `0 fail`.

<criterion id="RB5X3-AC3" cell_refs="RV-x-3" judgment="true"/>
`RB5X3-AC3` -- graded by the COO's live read at the drain, then the CVO and Andrew (DEC-5), never self-graded: in the Global RSI panel the axis labels and marker read dark on the white ground; in the RSI modal Full view the Trend value is title case and the Asset Class select has room beside its caret. RECORD; no verdict.

<expected_criteria>RB5X3-AC1, RB5X3-AC2, RB5X3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/RSIBars.tsx
portal/src/components/market-performance/RSIModal.tsx
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v5.md</decomp_doc> v5 @f4c4268583, cell `RV-x-3`.
<owned_cells>RV-x-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB5X3-AC1, RB5X3-AC2, RB5X3-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~15/DSGN_RBNDV2.TO-RV-x-3.rsi-ink.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB5X3-AC1,RB5X3-AC2,RB5X3-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB5X3-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W15-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v5 -- the paths of this cell are written by no other order of the round (disjoint write sets; `portal/src/__tests__/dsgn-rbndv2/` holds one new test file per cell); the files were read at the feature tip 7f8731df.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~15, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 15 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md`.
