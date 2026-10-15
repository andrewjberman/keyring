# TO DSGN_RBNDV2.TO-RV-y-1 -- FWD-3, FWD-5: the Market Overview page draws no box around a row or card, only deliberate hairlines and controls

<to_id>DSGN_RBNDV2.TO-RV-y-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~19</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>6</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-y-1` (decomp v6 @e4848abcad) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- (chain 1) | **slot:** ~19, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-y-1` -- a regression of round 2's rule that inset cards become hairline sections. Round 4's stylesheet rule (`portal/src/index.css`, the `border-white/N` selectors at about lines 593-615, written `[data-panel-surface="light"] .border-white\/N { border-color: var(--rb-rule) }`) turned every `border-white/N` class on a light surface from invisible-on-white into a visible grey line. A component that kept `border border-white/10` out of its dark-ground days is now boxed again: each Trending Topics row (`portal/src/components/market-performance/ExecutiveSummary.tsx` about line 989, class `... rounded-[4px] border border-white/10 hover:... hover:border-white/2..`) shows a grey box, which Andrew's panel design (hairline sections, no inset boxes) does not want. **The fix is a sweep of the class, not one row.**

**Scope (these files only; the stylesheet rule stays as it is):** every `.tsx` file under `portal/src/components/market-performance/` EXCEPT `SentimentGauge.tsx` (another order owns it), and the page folder `portal/src/pages/MarketPerformance/`. A measured denominator at the base: `git grep -n -E "border-white/[0-9]+" -- src/components/market-performance src/pages/MarketPerformance` from the portal root (about 70 lines in 6 files). Print it first.

**Classify every occurrence** by the element that carries it and decide, using this rule:
- KEEP (the border is deliberate and stays): a control (a `button`, `input`, `select`, `textarea`, a chip or segmented button, a dropdown trigger); a one-sided rule (`border-t`, `border-b`, `border-l`, `border-r`, `border-y`, `border-x`, a `divide-*` separator, a table row separator); a modal or panel header, footer or section hairline; a popover, menu or tooltip that floats (`absolute` or `fixed`); a focus or selected-state border.
- DROP (the border boxes a content container): a `div`, `li`, `section`, `article` or `tr` that carries the all-sides `border` class together with `border-white/N` and acts as a row, card or tile. Drop it by changing `border border-white/N` to `border border-transparent` (the 1px stays so nothing shifts) and by changing any `hover:border-white/N` on the same element to `hover:border-transparent`.
Start with the Trending Topics row in `ExecutiveSummary.tsx` (about line 989), then the rest. When a case is not clear from the rule, KEEP it and say why in the list.

**Write the list.** Create `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~19/BORDER_SWEEP_LIST.md`: one markdown table row per occurrence, columns `file | line | tag | role | decision | snippet` where `snippet` is the occurrence's trimmed source line copied exactly as it reads AFTER your change (for KEEP rows the unchanged line; for DROP rows the changed line), `decision` is `KEEP` or `DROP`, then a summary line `BEFORE <n> AFTER <m>` (the counts of `border-white/N` classes in scope before and after).

**Test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts`, reading the in-scope files as text: (a) the Trending Topics row in `ExecutiveSummary.tsx` (the line carrying `group relative px-4 py-3 mb-1`) holds no `border-white`; (b) the list file exists and every row has a role and a decision of KEEP or DROP; (c) every `border-white/N` occurrence that remains in the in-scope files appears as the `snippet` of a KEEP row; (d) no DROP row's snippet still holds `border-white`; (e) the after count is below the before count; the test PRINTS `BORDER-WHITE-BEFORE <n> BORDER-WHITE-AFTER <m>` (the before read by `git show d0cb67d0:<file>` for each in-scope file) and `VERDICT: BORDER-SWEEP-OK` only when every arm holds; the difference control runs arm (a) on the base text of `ExecutiveSummary.tsx` and it must FAIL there.

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. The design principle Andrew gave in round 5: text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `d0cb67d0` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB6Y1-AC1" cell_refs="RV-y-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~19; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: BORDER-SWEEP-OK</expect></criterion>
`RB6Y1-AC1` -- the Trending Topics row holds no `border-white`, the list file holds a role and a KEEP or DROP for every occurrence, every remaining occurrence is a KEEP row's snippet, the after count is below the before count and both print, the difference control fails on the base text, and the test prints `VERDICT: BORDER-SWEEP-OK` only when every arm holds.

<criterion id="RB6Y1-AC2" cell_refs="RV-y-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~19; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB6Y1-AC2` -- every test under `src/__tests__/dsgn-rbndv2/` passes after your edit: the summary line reads `0 fail`.

<criterion id="RB6Y1-AC3" cell_refs="RV-y-1" judgment="true"/>
`RB6Y1-AC3` -- graded by the COO's walk at the drain (one live walk of /market, rows read by computed `border-top-color` and `border-top-width`), then the CVO and Andrew (DEC-5), never self-graded: the Trending Topics rows show no box (border colour transparent), the controls (period chips, dropdowns) keep their lines. RECORD; no verdict.

<expected_criteria>RB6Y1-AC1, RB6Y1-AC2, RB6Y1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/market-performance/ExecutiveSummary.tsx
portal/src/components/market-performance/FearGreedModal.tsx
portal/src/components/market-performance/IndexPerformanceModal.tsx
portal/src/components/market-performance/KeywordSentimentModal.tsx
portal/src/components/market-performance/MarketRegimeModal.tsx
portal/src/components/market-performance/MarketRegimeIndicator.tsx
portal/src/components/market-performance/RSIModal.tsx
portal/src/components/market-performance/RSIBars.tsx
portal/src/components/market-performance/TopicCloud.tsx
portal/src/components/market-performance/EmotionalIntensityMeter.tsx
portal/src/pages/MarketPerformance/
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v6.md</decomp_doc> v6 @e4848abcad, cell `RV-y-1`.
<owned_cells>RV-y-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB6Y1-AC1, RB6Y1-AC2, RB6Y1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~19/DSGN_RBNDV2.TO-RV-y-1.border-sweep.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB6Y1-AC1,RB6Y1-AC2,RB6Y1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB6Y1-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's live read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W19-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v6 -- the paths of this cell are written by no other order of the round (disjoint write sets; `portal/src/__tests__/dsgn-rbndv2/` holds one new test file per cell); the files were read at the feature tip d0cb67d0.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~19, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 19 --portal-ref feature/dsgn-rbndv2-light`; Andrew-direct record `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md; CTO analysis ledger/ROUND_ANALYSIS.round5.md`.
