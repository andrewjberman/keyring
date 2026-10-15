# TO DSGN_RBNDV2.TO-RV-x-4 -- FWD-3, FWD-5: the Fear and Greed dial and its text read on white, and a component tile tints on hover

<to_id>DSGN_RBNDV2.TO-RV-x-4</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~16</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>5</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-x-4` (decomp v5 @f4c4268583) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (chain 4) | **slot:** ~16, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-x-4` -- two defects Andrew measured, in two files.

(1) **The Fear and Greed panel's dial and text are white on white** (Andrew: "Dial on Fear and Greed meter is invisible as well as all text here is white and not legible on white background"). The panel draws `portal/src/components/market-performance/EmotionalIntensityMeter.tsx`, whose SVG carries literal whites the stylesheet rule cannot reach: the gauge track `stroke="rgba(255,255,255,0.1)"` (about line 215), the needle shaft `stroke="white"` and tip `fill="white"` (about lines 244-251), the centre hub `fill="white"` (about line 256), the Fear and Greed end labels `fill="white"` with `opacity="0.5"` (about lines 264-292), the value text `fill="white"`, and a label `fill="rgba(255,255,255,0.7)"` (about line 326). Read the whole file and replace EVERY literal white: the track `rgba(10, 23, 51, 0.08)`; the needle shaft, tip and hub `var(--rb-ink)`; the Fear and Greed end labels `var(--rb-ink-3)` with the `opacity` attribute removed (full opacity); the value text and the other labels `var(--rb-ink)` or `var(--rb-ink-3)` as the original weight suggests (primary figure ink, secondary label ink-3). Leave the coloured gauge track and its gradient untouched.

(2) **Component Indicators tiles need an indigo hover.** In `portal/src/components/market-performance/FearGreedModal.tsx` the component tile (about lines 265-272) reads `hover:border-white/20` when not selected. Andrew: "Hover over 'Component Indicators' should change color to indigo with transparent shade, full opacity indigo shade on selection is correct in current state." Replace `hover:border-white/20` with `hover:bg-[hsl(var(--primary))]/10` (an indigo tint at 10 percent on hover) and leave the selected state `bg-[hsl(var(--primary))]/20 border-2 border-[hsl(var(--primary))]` exactly as it is.

Do not change any other colour, chart or data code.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. The design principle Andrew gave for this round: text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `7f8731df` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB5X4-AC1" cell_refs="RV-x-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~16; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-5-x4.fear-greed.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: FEAR-GREED-OK</expect></criterion>
`RB5X4-AC1` -- `EmotionalIntensityMeter.tsx` holds no `stroke="white"`, no `fill="white"` and no `rgba(255,255,255`, `FearGreedModal.tsx` carries `hover:bg-[hsl(var(--primary))]/10` and no `hover:border-white/20` and keeps the selected-state classes; the before and after counts of white literals in `EmotionalIntensityMeter.tsx` print (`GAUGE-WHITE-BEFORE <n> GAUGE-WHITE-AFTER <m>`, the base read by `git show 7f8731df:src/components/market-performance/EmotionalIntensityMeter.tsx`); the difference control fails on the base text; the test prints `VERDICT: FEAR-GREED-OK` only when every arm holds.

<criterion id="RB5X4-AC2" cell_refs="RV-x-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~16; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB5X4-AC2` -- every test under `src/__tests__/dsgn-rbndv2/` passes after your edit: the summary line reads `0 fail`.

<criterion id="RB5X4-AC3" cell_refs="RV-x-4" judgment="true"/>
`RB5X4-AC3` -- graded by the COO's live read at the drain, then the CVO and Andrew (DEC-5), never self-graded: in the Fear and Greed panel the needle and hub are dark and visible and the value and end labels read dark on the white ground; hovering a Component Indicators tile in the modal shows an indigo tint. RECORD; no verdict.

<expected_criteria>RB5X4-AC1, RB5X4-AC2, RB5X4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/EmotionalIntensityMeter.tsx
portal/src/components/market-performance/FearGreedModal.tsx
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v5.md</decomp_doc> v5 @f4c4268583, cell `RV-x-4`.
<owned_cells>RV-x-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB5X4-AC1, RB5X4-AC2, RB5X4-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~16/DSGN_RBNDV2.TO-RV-x-4.fear-greed.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB5X4-AC1,RB5X4-AC2,RB5X4-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB5X4-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W16-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v5 -- the paths of this cell are written by no other order of the round (disjoint write sets; `portal/src/__tests__/dsgn-rbndv2/` holds one new test file per cell); the files were read at the feature tip 7f8731df.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~16, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 16 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md`.
