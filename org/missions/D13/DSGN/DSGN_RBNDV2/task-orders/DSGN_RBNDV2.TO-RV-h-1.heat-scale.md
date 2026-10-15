# TO DSGN_RBNDV2.TO-RV-h-1 -- FWD-4: one white-to-silver heat scale, every heat map pointed at it

<to_id>DSGN_RBNDV2.TO-RV-h-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~4</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>1</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-h-1` (decomp v1 @b475e9badc) | **outcome_ref:** FWD-4 | **depends_on:** -- (chain 4) | **slot:** ~4, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-h-1` -- THE ONE WHITE-TO-SILVER HEAT SCALE and every heat map pointed at it (FWD-4, C-HEAT).

Create `portal/src/lib/heatScale.ts`: the ONE definition of the heat colour, a white end `#FFFFFF` and a silver end you choose, and `heatColor(t: number): string` returning a hex colour for t clamped to 0..1 (0 = white = lowest, 1 = silver = highest), plus the two end constants exported. Choose the silver end so that (i) white against the silver end holds a contrast ratio of at least 3.0 (WCAG relative luminance), and (ii) navy ink `#0A1733` on the silver end holds at least 4.5, so dark cell text stays readable on the darkest cell; interpolate in a way that makes lightness strictly decreasing with t so a reader tells high from low at a glance. The blue scale is gone from every heat map.

Point each heat map at it, replacing its own blue colour logic and keeping its data logic, thresholds, bins and text exactly as they are: `portal/src/components/BenchmarkHeatmap.tsx`, `portal/src/components/PerformanceHeatMap.tsx`, `portal/src/pages/InvestorReporting/tabs/reporting/ReturnsHeatmap.tsx`, `portal/src/pages/Macroeconomics/panels/MacroHeatmap.tsx`, `portal/src/pages/Macroeconomics/utils/percentileColor.ts`, `portal/src/pages/Valuation/panels/ValuationSummaryPanel.tsx`, `portal/src/pages/Correlation/components/CorrelationMatrix.tsx` and `portal/src/pages/Correlation/Correlation.tsx` (the Correlation page's heat cells). A name search (brief F10) found these and is not exhaustive: read each file, change only where it colours a heat cell, and if a heat map elsewhere in `src/` also uses a blue scale, name its file in a surprise row and leave it (it is a wall: not in your `<paths>`). Where a file colours a heat cell as diverging (positive vs negative), keep the sign semantics of the data and shade magnitude by the scale; do not invent a new hue. Cell text stays navy ink.

**Out of this cell:** `index.css`, the panel primitives, the sidebar, and `--ramp-*` / the sentiment scale (an ordered-scale ramp for other charts; the round-3 walk reads it).

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's (DEC-1 to DEC-5 of the PRD): you reproduce the fixture and invent nothing. Colours are read from tokens (`--bg-page`, `--hairline`, `--bg-surface`, the `--rb-*` family), never typed as a literal in a component, except where this cell says a literal is the point. Charts keep their colour (C6).

**Environment (every cell):** the portal worktree is `<WS>/portal`, based on the feature branch `feature/dsgn-rbndv2-light` at `ad7c100b5c` (= origin DEV when it was cut). The fixture you build to is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md` (read it first; it carries every value you need, so do not open the board URL). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints its VERDICT line only when every arm holds. Do not start any server: dev builds run on port 5174 only and 5174 serves the main checkout, not your worktree. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11); Lato; no non-ASCII in code.

### ACCEPTANCE

<criterion id="RB1H-AC1" cell_refs="RV-h-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~4; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/lib/__tests__/dsgn-rbndv2/rb-1-h.scale.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: HEAT-SCALE-OK</expect></criterion>
`RB1H-AC1` -- `heatColor(0)` is `#FFFFFF`; the silver end differs from white by a WCAG contrast ratio of at least 3.0 and navy `#0A1733` on it holds at least 4.5; across `heatColor(i/10)` for i in 0..10 the relative luminance is strictly decreasing; values below 0 and above 1 clamp to the ends (difference control: a deliberately reversed copy of the function inside the test must FAIL the monotonic arm, proving the arm can fail). The test prints `VERDICT: HEAT-SCALE-OK` only when every arm holds.

<criterion id="RB1H-AC2" cell_refs="RV-h-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~4; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/lib/__tests__/dsgn-rbndv2/rb-1-h.readers.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: HEAT-READERS-OK</expect></criterion>
`RB1H-AC2` -- reading the eight heat files as text: each imports from `heatScale` (or `@/lib/heatScale`) and calls `heatColor`, and none still defines the blue heat colours it held at the base (the test lists, per file, the blue literals or blue class names that the base file coloured heat cells with, taken from `git show ad7c100b5c:portal/<file>` in `<WS>/portal`, and asserts each is absent now; difference control: the same absence check run against the base text must FAIL for every file, proving it can fail). The test prints `VERDICT: HEAT-READERS-OK` only when every arm holds.

<criterion id="RB1H-AC3" cell_refs="RV-h-1" judgment="true"/>
`RB1H-AC3` -- graded at the round-1 drain by Andrew's eye on `/market` and the heat maps he opens (DEC-5), never self-graded and never by the CVO: a reader tells high from low at a glance and no heat map is left in the blue scale. RECORD; no verdict.


<expected_criteria>RB1H-AC1, RB1H-AC2, RB1H-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can. This cell's write set spans page files because C-HEAT says each heat map is pointed at the scale; it is not a loosening of C-PANEL.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/lib/heatScale.ts
portal/src/lib/__tests__/dsgn-rbndv2/
portal/src/components/BenchmarkHeatmap.tsx
portal/src/components/PerformanceHeatMap.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReturnsHeatmap.tsx
portal/src/pages/Macroeconomics/panels/MacroHeatmap.tsx
portal/src/pages/Macroeconomics/utils/percentileColor.ts
portal/src/pages/Valuation/panels/ValuationSummaryPanel.tsx
portal/src/pages/Correlation/components/CorrelationMatrix.tsx
portal/src/pages/Correlation/Correlation.tsx
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP.md</decomp_doc> v1 @b475e9badc, cell `RV-h-1`.
<owned_cells>RV-h-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB1H-AC1, RB1H-AC2, RB1H-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~4/DSGN_RBNDV2.TO-RV-h-1.heat-scale.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB1H-AC1,RB1H-AC2,RB1H-AC3` BEFORE the flip. `RB1H-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming Andrew's read at the drain (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v1 section 6).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v1 -- every named existing file measured present at origin DEV ad7c100b5c; the write sets are pairwise disjoint (decomp v1 section 3 and 5).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~4, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_RBNDV2 4 --portal-ref feature/dsgn-rbndv2-light`.
