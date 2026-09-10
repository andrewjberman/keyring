# TO IRPT_FNTEND.TO-FE-s-7 -- the Holdings tab

<to_id>IRPT_FNTEND.TO-FE-s-7</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F6; PATHS category-tree and radial rows; FIXTURES model-overlay row) | **Decomp cell:** `FE-s-7` | **outcome_ref:** FWD-5 | **depends_on:** `FE-s-3` (terminal) | **slot:** ~4, queue position 1

---

## WORKER FACE

### THE CELL

`FE-s-7` -- the Holdings tab: model-led radial drilldowns from `HoldingsSnapshot`, every slice carrying its basis and denominator.

**Tab** at `portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx`, mounted in `TabShell`'s `holdings` body:
- `HoldingsSummary.tsx`: current value (the snapshot's unique custody total), unique account count, source dates (business and as-of clocks), model coverage with its denominator.
- `DrillTree.tsx`: `CategoryViewTree` from `portal/src/components/CategoryViewTree.tsx` over the snapshot's node hierarchy (Models, SMAs, Client and every other category the hierarchy carries), colours from `portal/src/lib/modelPortfolioColors.ts` by canonical model code; breadcrumbs; the current node's children as a donut (`recharts`) with direct labels, following the presentation of `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx` and `_shared/tabs/DistributionTab.tsx` (imported patterns, not their value handling).
- `SliceTable.tsx`: the table equivalent beside every donut: node, basis, amount (signed), denominator, percent of parent, percent of total, classification partition, provenance. `pctOfParent` and `pctOfTotal` are two columns from the snapshot, never computed here.
- Rules in `tabs/holdings/slices.ts` (pure, tested): a slice's basis label is one of `observed custody`, `observed allocation`, `assigned account`, `target`; unassigned, unmapped and classification-unavailable nodes are distinct slices with those labels; a partial allocation's slices sum to the snapshot's stated total, never scaled to 100; a negative amount renders negative and is drawn as its own labelled slice, never through an absolute value; a node whose `denominator` is signed, zero or `unknown` renders the snapshot's `alternativeState` table and no donut; classification partitions (`Supervised`/`Unsupervised`, `Advised`/`Residual`) render from `node.classification` and are never merged with the basis axis; an `unknown` classification renders `unknown`; sleeve-held securities (`kind: security`) and model target constituents (`kind: target-constituent`) are different drill destinations with different headings. Summary and drill carry one `(scope, revision)` and the tab refuses to render a drill whose revision differs from the summary's. No time series.

**Fixtures** under `fixtures/fe-s-7/`, the seven cases: `holdings.smartx-observed.json`, `holdings.eclipse-assigned.json`, `holdings.cottonwood-target-blend.json`, `holdings.cash-remainder.json`, `holdings.unknown-category.json`, `holdings.duplicate-relationship.json`, `holdings.stale-overlay.json`, plus `holdings.signed-denominator.json`. Smoke maps `fixtures/smoke/fe-s-7-smartx.json`, `fe-s-7-cottonwood.json`.

**Tests** under `__tests__/fe-s-7/`: `slices.test.ts` (per fixture: the sum of rendered slice amounts equals the fixture's stated total, printing `SUM: <sum> of <total>`; the partial fixture's percents do not sum to 100; the negative position renders with its sign; the unknown-category fixture renders `unknown` and no `Client`; parent and total percents differ where the fixture says they do; the signed-denominator fixture renders the alternative state and no donut), `drill.test.ts` (security and target-constituent destinations have different headings; a drill at a revision other than the summary's is refused), `source-bounds.test.ts` (reads `tabs/holdings/**` and asserts no `Math.abs`, no `/ total`, no `* 100`, no arithmetic producing a percent, no `reduce(` producing a total).

### ACCEPTANCE

<criterion id="F7-AC1" cell_refs="FE-s-7"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F7-AC1` -- typecheck clean.

<criterion id="F7-AC2" cell_refs="FE-s-7"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7/slices.test.ts</invocation><expect>0 fail</expect></criterion>
`F7-AC2` -- eight fixtures: sums equal stated totals, partial never 100, signs kept, unknown never Client, two percents distinct, alternative state on a bad denominator (record the `SUM:` lines).

<criterion id="F7-AC3" cell_refs="FE-s-7"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7/drill.test.ts</invocation><expect>0 fail</expect></criterion>
`F7-AC3` -- securities and target constituents are different destinations; revision mismatch is refused.

<criterion id="F7-AC4" cell_refs="FE-s-7"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7/source-bounds.test.ts</invocation><expect>0 fail</expect></criterion>
`F7-AC4` -- no absolute values, no percent or total computed in the tab.

<criterion id="F7-AC5" cell_refs="FE-s-7"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/fe-s-7_holdings_smartx_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-7-smartx.json --click Holdings; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F7-AC5` -- the Holdings tab renders the SmartX fixture at the model level at 1440 (record `LOC`).

<criterion id="F7-AC6" cell_refs="FE-s-7"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/fe-s-7_holdings_cottonwood_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-7-cottonwood.json --click Holdings; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F7-AC6` -- the Cottonwood blend renders at 390 with its table equivalent.

<criterion id="F7-AC7" cell_refs="FE-s-7" judgment="true"/>
`F7-AC7` -- graded at L9 from the PNGs: targets never read as observed holdings; missing attribution is visible and not redistributed; model colours are the portal's; nothing light on the silver canvas. RECORD; NO VERDICT.

<expected_criteria>F7-AC1, F7-AC2, F7-AC3, F7-AC4, F7-AC5, F7-AC6, F7-AC7</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **Data.** Through the typed client only. Joins, reconciliation, denominators and revision-bound nodes are the counterpart's; this tab renders them and computes none. Actual custody holdings remain the total-value basis. NO LIVE VENDOR CALL; fixtures only.
- **Numbers.** No width or count value is an acceptance value.
- **Reuse.** `CategoryViewTree.tsx`, `modelPortfolioColors.ts`, the AdvisorIntelligence radial files, `StatusPanel.tsx`, `TabShell.tsx` are IMPORTED, never edited. The absolute-value shortcut in the radial precedents is NOT inherited.
- **Keys.** Built by `irKey`; a client name is never a key.
- **Colour law.** No light text or light button directly on the silver canvas.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W4-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/
portal/src/pages/InvestorReporting/fixtures/fe-s-7/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-7/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-7`.
<owned_cells>FE-s-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F7-AC1` .. `F7-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-7.holdings-tab.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F7-AC1,F7-AC2,F7-AC3,F7-AC4,F7-AC5,F7-AC6,F7-AC7` BEFORE the `complete` flip. `F7-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `holdings-tab.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
comp-blast: RUN at L5 on portal/src/components/CategoryViewTree.tsx -- SUBJECT_ABSENT_FROM_CORPUS in the served graph (vintage 2026-09-10T12:24Z) while the file exists at portal 5907cbca; blindness stated; the file is imported and never edited.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. The tab mounts into TabShell's existing `holdings` body by export name; TabShell.tsx is not edited.
</preflight>

Seating: slot ~4, queue position 1; seated when `FE-s-3` is terminal and drained, fresh worktree pair from HEAD, dev-server port 5184.
