# TO DSGN_RBNDV2.TO-RV-c-1 -- FWD-3/FWD-5: the modal chart ticks read a token and the Market Regime footer stops clipping (CVO grade of RB2M4-AC3)

<to_id>DSGN_RBNDV2.TO-RV-c-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~10</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-c-1` (decomp v3 @74ed99710a) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (chain 1) | **slot:** ~10, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-c-1` -- the Fear and Greed and the Market Regime modals now sit on the white A-light frame, but their charts still paint white chrome that was written for a dark ground: the CVO graded `RB2M4-AC3` NOT MET because the axes cannot be read.

**Part 1, the chart chrome.** Replace every literal white chart prop in the two files with a token, and change nothing else about the charts (series colours, tooltips, data logic and layout stay):

- `portal/src/components/market-performance/FearGreedModal.tsx`: lines 401 and 885 (`<CartesianGrid ... stroke="rgba(255,255,255,0.1)" />`), lines 405, 423, 889 and 907 (axis `stroke="rgba(255,255,255,0.4)"`), lines 406, 424, 890 and 908 (`tick={{ fill: 'rgba(255,255,255,0.6)', fontSize: 11 }}`).
- `portal/src/components/market-performance/MarketRegimeModal.tsx`: line 606 (grid), lines 610 and 625 (axis stroke), lines 611 and 626 (tick fill).
- The mapping: grid stroke becomes `var(--rb-rule)`; axis stroke becomes `var(--rb-quiet)`; tick fill becomes `var(--rb-ink-3)`. The `--rb-*` tokens are HEX values read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`. (A recharts prop given the string `var(--rb-ink-3)` sets an SVG attribute that the browser resolves; do not wrap it.)

**Part 2, the footer clip.** `portal/src/components/market-performance/MarketRegimeModal.tsx:484` passes `className="w-[1280px] max-w-[95vw] max-h-[72vh]"` to `ModalFrame`; the `max-h-[72vh]` caps the surface below the frame's own `max-h-[calc(100vh_-_2rem)]`, so the body scrolls inside a smaller box and the bottom row of the signal selector (Momentum, Volatility, Correlation, Yield Curve) sits half behind the footer at 1440 x 900. Remove `max-h-[72vh]` from that className and keep the width classes. Do not edit `ModalFrame.tsx`.

**Out of this cell:** the other three market modals (`RSIModal`, `IndexPerformanceModal`, `KeywordSentimentModal`: if one holds the same literal white chart props, name its file and the line numbers in a surprise row and leave it, a wall), `ModalFrame.tsx`, `index.css` and every page file.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. TOKEN FORMATS: `--rb-*` HEX read as `var(--rb-X)`; `--bg-surface`, `--bg-page`, `--hairline`, `--semantic-*` are HSL triples read as `hsl(var(--X))`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. You are given the worker face only: open your order file only to edit its status or amend a criterion the issuer has ruled on, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `826551e2` (the difference-control base). Round 1 and round 2 are merged on the branch: the `--rb-*` tokens, the white panels, the shared `ModalFrame` (each modal's surface carries `data-panel-surface="light"`) and the scoped rules keyed on it. Do not start any server.

### ACCEPTANCE

<criterion id="RB3C1-AC1" cell_refs="RV-c-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/components/market-performance/__tests__/dsgn-rbndv2/rb-3-c1.chart-chrome.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CHART-CHROME-OK</expect></criterion>
`RB3C1-AC1` -- reading `FearGreedModal.tsx` and `MarketRegimeModal.tsx` as text: neither contains `rgba(255,255,255,0.1)`, `rgba(255,255,255,0.4)` or `rgba(255,255,255,0.6)` in a chart prop; the count of `var(--rb-ink-3)` tick fills is at least 4 in `FearGreedModal.tsx` and 2 in `MarketRegimeModal.tsx`, the count of `var(--rb-quiet)` axis strokes is at least 4 and 2, and the count of `var(--rb-rule)` grid strokes is at least 2 and 1; neither file contains `hsl(var(--rb-`; `MarketRegimeModal.tsx` contains no `max-h-[72vh]` and still contains `max-w-[95vw]`; (difference control: the same arms run on `git show 826551e2:<file>` of each file, run from the portal root, must FAIL, proving the test can fail). The test prints `VERDICT: CHART-CHROME-OK` only when every arm holds.

<criterion id="RB3C1-AC2" cell_refs="RV-c-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/components/market-performance/__tests__/dsgn-rbndv2/rb-3-c1.bound.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CHART-BOUND-OK</expect></criterion>
`RB3C1-AC2` -- for each of the two files, `git diff --numstat 826551e2 -- <file>` (run by the test in the portal root with `execSync`) shows insertions plus deletions of at most 40 lines, and the file still contains at least its base count of `useState`, `useEffect`, `onClick` and `onSubmit` tokens (the behaviour-preserved bound); the test reports EVERY file before it fails. The test prints `VERDICT: CHART-BOUND-OK` only when every arm holds.

<criterion id="RB3C1-AC3" cell_refs="RV-c-1" judgment="true"/>
`RB3C1-AC3` -- graded by the COO's live read at the drain (a chart tick's computed `fill` in each of the two opened modals, and the Market Regime signal row's bottom edge above the footer's top edge), then the CVO and Andrew (DEC-5), never self-graded: the chart axes read as navy-grey on the white surface and the signal row is fully visible. RECORD; no verdict.

<expected_criteria>RB3C1-AC1, RB3C1-AC2, RB3C1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/FearGreedModal.tsx
portal/src/components/market-performance/MarketRegimeModal.tsx
portal/src/components/market-performance/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v3.md</decomp_doc> v3 @74ed99710a, cell `RV-c-1`.
<owned_cells>RV-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB3C1-AC1, RB3C1-AC2, RB3C1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~10/DSGN_RBNDV2.TO-RV-c-1.modal-chart-chrome.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB3C1-AC1,RB3C1-AC2,RB3C1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB3C1-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W10-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 -- both files measured at the feature tip 826551e2: the literal white lines and the max-h cap named above; no other order is open.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~10, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 10 --portal-ref feature/dsgn-rbndv2-light`.
