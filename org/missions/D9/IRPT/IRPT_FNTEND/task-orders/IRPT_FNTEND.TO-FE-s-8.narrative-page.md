# TO IRPT_FNTEND.TO-FE-s-8 -- the narrative page

<to_id>IRPT_FNTEND.TO-FE-s-8</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F10; PATHS market-context row) | **Decomp cell:** `FE-s-8` | **outcome_ref:** FWD-8 | **depends_on:** `FE-s-4` (terminal) | **slot:** ~2, queue position 2

---

## WORKER FACE

### THE CELL

`FE-s-8` -- the period-in-context page inside the performance template, composed entirely from `NarrativePacket`.

**Page** at `portal/src/pages/InvestorReporting/render/narrative/PeriodInContextPage.tsx`, filling the slot `PerformanceDocument` left (`data-page="period-in-context"`): rendered only when the bundle carries a `NarrativePacket` and the export options select it. Content:
- a full-width performance time series (the report's daily cumulative series) with the packet's `events` (peak, trough, recovery, movement) drawn as markers at the packet's dates and the packet's `annotations` placed on the curve;
- for each marked window, the `trendingTopics` and `topicCloud` terms dated to that window, with the other sentiment signals as supporting context using the visual vocabulary of `portal/src/components/market-performance/MarketRegimeIndicator.tsx`, `SentimentGauge.tsx` and `portal/src/pages/MarketPerformance/panels/SentimentPanel/SentimentPanel.tsx` (imported presentation, no live data);
- a fixed statement, verbatim: `Market context shown here is contemporaneous with the account's movements. It is not an explanation of the account's return.`;
- footnotes and coverage from the packet (`coverage`, `evidence` citations with their cutoff dates);
- the `MISSING HISTORY` state: when the performance period begins before `packet.historyCutoff`, the page renders a labelled block `Market history is not available before <cutoff date>` for that span and renders no topic list for it.
Every term, fact and reference on the page comes from `packet.evidence`; `narrative/compose.ts` (pure, tested) selects and orders them and contains no text of its own beyond the fixed statement and the missing-history label.

**Fixtures** under `render/fixtures/`: `narrative.two-markers.json`, `narrative.pre-history.json`, `bundle.performance-with-narrative.json`. Smoke map `fixtures/smoke/fe-s-8-narrative.json`.

**Tests** under `__tests__/fe-s-8/`, `renderToStaticMarkup`: `markers.test.ts` (the two-marker fixture renders exactly two markers at the packet's dates), `missing-history.test.ts` (the pre-history fixture renders the missing-history block naming the cutoff and no topic element for the span), `language.test.ts` (the markup contains the fixed statement and none of `caused`, `because`, `drove`, `explains`, `due to`, `as a result`, `led to` -- the list is enumerated in the test), `evidence.test.ts` (every topic term in the markup exists in `packet.evidence`; the test prints `TERMS: n of n`), `determinism.test.ts` (rendered twice, identical).

### ACCEPTANCE

<criterion id="F8-AC1" cell_refs="FE-s-8"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F8-AC1` -- typecheck clean.

<criterion id="F8-AC2" cell_refs="FE-s-8"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-8/markers.test.ts</invocation><expect>0 fail</expect></criterion>
`F8-AC2` -- exactly the packet's markers at the packet's dates.

<criterion id="F8-AC3" cell_refs="FE-s-8"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-8/missing-history.test.ts</invocation><expect>0 fail</expect></criterion>
`F8-AC3` -- a pre-history window renders MISSING HISTORY with its cutoff and no empty topic list.

<criterion id="F8-AC4" cell_refs="FE-s-8"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-8/language.test.ts</invocation><expect>0 fail</expect></criterion>
`F8-AC4` -- the contemporaneous statement is present; no causal word is.

<criterion id="F8-AC5" cell_refs="FE-s-8"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-8/evidence.test.ts</invocation><expect>0 fail</expect></criterion>
`F8-AC5` -- every rendered term comes from the packet's evidence (record the `TERMS:` line).

<criterion id="F8-AC6" cell_refs="FE-s-8"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-8/determinism.test.ts</invocation><expect>0 fail</expect></criterion>
`F8-AC6` -- rendered twice, identical.

<criterion id="F8-AC7" cell_refs="FE-s-8"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=perf-narrative-fixture-1" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-8_print_narrative_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-8-narrative.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F8-AC7` -- the print route renders the performance template with the period-in-context page from the bundle fixture (record `LOC`).

<criterion id="F8-AC8" cell_refs="FE-s-8" judgment="true"/>
`F8-AC8` -- graded at L9 from the PNG: the page reads as contemporaneous context and not as an explanation of the return; missing history reads as absent data, not as nothing notable. RECORD; NO VERDICT.

<expected_criteria>F8-AC1, F8-AC2, F8-AC3, F8-AC4, F8-AC5, F8-AC6, F8-AC7, F8-AC8</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash; quote a route carrying `?`.
- **Data.** Inflection selection, evidence dating and prose validity are the counterpart's; this page places what the packet carries and selects nothing from headlines. No live market data; the market-performance components are imported for presentation only. NOT a BI surface. NO LIVE VENDOR CALL; fixtures only.
- **Numbers.** None is an acceptance value.
- **Reuse.** `render/performance/*`, `render/manifest.ts`, `MarketRegimeIndicator.tsx`, `SentimentGauge.tsx`, `SentimentPanel.tsx`, `useRSIValues.ts` are IMPORTED, never edited. A change the page needs in the template is a surprise row on `FE-s-4`.
- **Colour law.** No light text or light button directly on the silver canvas.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W2-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/render/narrative/
portal/src/pages/InvestorReporting/render/fixtures/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-8/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-8`.
<owned_cells>FE-s-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F8-AC1` .. `F8-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-8.narrative-page.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F8-AC1,F8-AC2,F8-AC3,F8-AC4,F8-AC5,F8-AC6,F8-AC7,F8-AC8` BEFORE the `complete` flip. `F8-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `narrative-page.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. render/fixtures/ is also FE-s-4's; sequential in one slot, no overlap.
</preflight>

Seating: slot ~2, queue position 2; seated when `FE-s-4` is terminal and drained, fresh worktree pair from HEAD, dev-server port 5182.
