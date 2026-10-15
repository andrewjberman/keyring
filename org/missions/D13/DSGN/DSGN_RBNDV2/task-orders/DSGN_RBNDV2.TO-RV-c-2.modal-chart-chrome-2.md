# TO DSGN_RBNDV2.TO-RV-c-2 -- FWD-3/FWD-5: the RSI and Index Performance modal charts read tokens (DIRECT-ACT, rows W10-S1 and W10-S2)

<to_id>DSGN_RBNDV2.TO-RV-c-2</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~11</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-c-2` (decomp v3 addendum 1) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (direct act) | **slot:** ~11, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-c-2` -- the Fear and Greed and Market Regime modals now read their chart chrome from tokens (order `RV-c-1`, merged). Two sibling modals on the white A-light frame still paint white chart chrome written for a dark ground, so their axes cannot be read: `portal/src/components/market-performance/IndexPerformanceModal.tsx` (lines 456, 460, 461, 472, 473, 479) and `portal/src/components/market-performance/RSIModal.tsx` (lines 229, 334, 351, 370, 375, 376).

Replace every literal white-alpha chart prop (`rgba(255,255,255,...)` or `rgba(255, 255, 255, ...)`) in those two files with a token, and change nothing else about the charts (series colours, tooltips, data logic and layout stay): grid stroke becomes `var(--rb-rule)`; axis stroke becomes `var(--rb-quiet)`; tick fill becomes `var(--rb-ink-3)`. For any other white-alpha chart literal you find on those lines, map it by its alpha (at or below 0.15 to `var(--rb-rule)`, 0.4 to `var(--rb-quiet)`, 0.5 or more to `var(--rb-ink-3)`) and name each such line in your report. A white-alpha literal that is NOT a chart prop (for example a tooltip background that must stay dark) is left alone and named in a surprise row. The `--rb-*` tokens are HEX values read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`.

**Out of this cell:** `FearGreedModal.tsx` and `MarketRegimeModal.tsx` (done), `KeywordSentimentModal.tsx`, `ModalFrame.tsx`, `index.css` and every page file.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. TOKEN FORMATS: `--rb-*` HEX read as `var(--rb-X)`; `--bg-surface`, `--bg-page`, `--hairline`, `--semantic-*` are HSL triples read as `hsl(var(--X))`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. You are given the worker face only: open your order file only to edit its status or amend a criterion the issuer has ruled on, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `6396217d` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB3C2-AC1" cell_refs="RV-c-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/components/market-performance/__tests__/dsgn-rbndv2/rb-3-c2.chart-chrome.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CHART-CHROME-2-OK</expect></criterion>
`RB3C2-AC1` -- reading `IndexPerformanceModal.tsx` and `RSIModal.tsx` as text: neither contains `rgba(255,255,255` or `rgba(255, 255, 255` on a line that passes a chart prop (a `CartesianGrid`, `XAxis`, `YAxis`, `ReferenceLine` or `Tooltip` cursor prop, or a `tick=`, `stroke=` or `fill:` entry); each file contains at least 2 `var(--rb-ink-3)` tick fills, at least 2 `var(--rb-quiet)` axis strokes and at least 1 `var(--rb-rule)` grid stroke; neither contains `hsl(var(--rb-`; (difference control: the same arms run on `git show 6396217d:<file>` of each file, run from the portal root, must FAIL, proving the test can fail). The test prints `VERDICT: CHART-CHROME-2-OK` only when every arm holds.

<criterion id="RB3C2-AC2" cell_refs="RV-c-2" judgment="true"/>
`RB3C2-AC2` -- graded by the COO's live read at the drain (a chart tick's computed `fill` in the opened modal where reachable) and then the CVO and Andrew (DEC-5), never self-graded: the chart axes of the two modals read as navy-grey on the white surface. RECORD; no verdict.

<expected_criteria>RB3C2-AC1, RB3C2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/IndexPerformanceModal.tsx
portal/src/components/market-performance/RSIModal.tsx
portal/src/components/market-performance/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v3.md</decomp_doc> v3 addendum 1, cell `RV-c-2`.
<owned_cells>RV-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB3C2-AC1, RB3C2-AC2. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~11/DSGN_RBNDV2.TO-RV-c-2.modal-chart-chrome-2.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB3C2-AC1,RB3C2-AC2` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB3C2-AC2` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W11-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at addendum 1 -- both files measured at the feature tip 6396217d; no other order is open.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~11, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 11 --portal-ref feature/dsgn-rbndv2-light`.
