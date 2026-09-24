# TO DSGN_IRPTV1.TO-IV-t-4 -- the security list

<to_id>DSGN_IRPTV1.TO-IV-t-4</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~3</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>1</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_IRPTV1_PRD.md` v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-t-4` | **outcome_ref:** FWD-1 (hop 8), FWD-6, FWD-11 | **depends_on:** IV-t-3 (same slot, same worktree pair) | **slot:** ~3, queue position 2

---

## WORKER FACE

### THE CELL

`IV-t-4` -- the SECURITY LIST (PRD candidate C4, table half; the treemap is a later round). Build `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx` (a `Panel`, title "Securities") and mount it in `portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx` as ONE new line immediately after line 197 at portal `7c542fd23ec70c88bade4e3270f4c87f267a275a` (`<DrillTree snapshot={snapshot} />`): `<SecurityList snapshot={snapshot} />`. No other line of `HoldingsTab.tsx` changes (an import is a second line -- see IV4-AC3; if you must add one, the criterion is REFUSED with its numstat and the COO rules).

**One row per `kind === 'security'` leaf node** of `snapshot.nodes`, columns in this order: TICKER (the `securityId` tail after the last `:` or `-`, e.g. `TICKER:SPY` -> `SPY`; the id itself never prints; when the node carries `display.symbol`, that is the ticker), NAME (`display.label` when the node carries `display`, else `displayName`), SLEEVE (the nearest ancestor `model` / `sleeve` node's label via the `parentRef` chain, from `display.label` else `displayName`), WEIGHT (`pctOfTotal` formatted as a percent; null -> "not supplied"), VALUE (`amount` + `currency`; null -> "not supplied"). Sortable by any column, default weight descending; a filter by sleeve and by account (the ancestor `account` node's label). ASSET CLASS and SECTOR columns are ABSENT -- not blank, not placeholder (their source is unruled). The footer line (`PanelFooter`) carries the basis, the denominator, the position count (the leaf count) and the source coordinate / revision; NONE of `basis`, `denominator`, `provenance`, `sourceCoordinate`, `sourceRevision` appears in a table cell. `SliceTable` stays as it is.

**Component law.** `Panel variant="nested"`, `PanelHeader`, `PanelContent`, `PanelFooter`; navy ink on white; DESIGN.md C2 (tabular numerals in the weight and value columns), C3, C9, C10 (dense rows, generous panel padding), C11, C12 (an empty snapshot renders the designed empty state, not a blank table).

**Prior art (read, never edit):** `portal/src/pages/Positioning/tabs/HoldingsTab.tsx` (the dense table). **Fixtures (adapted shape):** `portal/src/pages/InvestorReporting/fixtures/fe-s-7/holdings.smartx-observed.json`, `fixtures/fe-s-7/holdings.cottonwood-target-blend.json`, `fixtures/holdingsSnapshot.success.json`. Anna's real served subtree (pre-adapter wire, a NAME reference only): `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/anna.holdings-nodes.dec293d6.json` -- 68 securities, every one with `display.label` and `display.symbol`.

### ACCEPTANCE

<criterion id="IV4-AC1" cell_refs="IV-t-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~3; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-4.security-list.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SECURITY-LIST-OK</expect></criterion>
`IV4-AC1` -- the built behaviour: over each named fixture the rendered table has exactly one body row per security leaf (`ROWS: n of n leaves`); each row's NAME is `display.label` where the node carries `display` (`DISPLAY-NAMED: d of n`) else `displayName`; WEIGHT and VALUE text match the node's own `pctOfTotal` / `amount` formatted (null -> "not supplied"); the ticker cell never contains the full `securityId`; rows are ordered by weight descending by default. Print the counts and `VERDICT: SECURITY-LIST-OK` only when every assertion holds.

<criterion id="IV4-AC2" cell_refs="IV-t-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~3; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-4.columns-and-vocabulary.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COLUMNS-AND-VOCAB-OK</expect></criterion>
`IV4-AC2` -- the columns and the vocabulary rule: the header row is exactly `Ticker, Name, Sleeve, Weight, Value` (`HEADERS: 5 of 5`; none of `Asset class`, `Sector`, `Basis`, `Denominator`, `Provenance`); no table cell contains `sourceCoordinate`, `sourceRevision`, `observed-custody`, `observed-allocation`, `src-` or a `holdings/` coordinate string; the footer element DOES contain the basis word and the position count (the positive control that the facts are retained). Print `LEAK: <none|tokens> CONTROL: <found|missing>` and `VERDICT: COLUMNS-AND-VOCAB-OK` only when clean and the control holds.

<criterion id="IV4-AC3" cell_refs="IV-t-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~3; timeout 120 python -c "import subprocess;r=subprocess.run(['git','diff','--numstat','7c542fd23ec70c88bade4e3270f4c87f267a275a','--','src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx','src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx'],capture_output=True,text=True).stdout.strip().splitlines();print('NUMSTAT:',r);ok=(len(r)==1 and r[0].split()[2].endswith('HoldingsTab.tsx') and r[0].split()[0] in ('1','2') and r[0].split()[1]=='0');print('VERDICT:','ONE-LINE-MOUNT' if ok else 'MOUNT-WIDER-THAN-RULED')"</invocation><expect>VERDICT: ONE-LINE-MOUNT</expect></criterion>
`IV4-AC3` -- the ruled touch (CTO 100332): `HoldingsTab.tsx` differs from `7c542fd23ec70c88bade4e3270f4c87f267a275a` by the ONE added mount line (plus at most the one import line it needs) and nothing removed; `SliceTable.tsx` does not differ. (`DrillTree.tsx` differs from the base because IV-t-3 landed in this same worktree first; it is out of this criterion's pathspec by design.)

<criterion id="IV4-AC4" cell_refs="IV-t-4" judgment="true"/>
`IV4-AC4` -- graded at L9 by `3.0.0_SA_CVO` from `iv-t-4.security-list.html` in your deliverables and a PNG if `node scripts/ui-smoke.mjs investor-reporting <deliverables>/iv-t-4.png --port <PORT> --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json` runs for you: C2 tabular numerals, C3, C9, C10 density; the brief's bar "an advisor answers 'what does the IRA hold' from the security list". RECORD; NO VERDICT.

<expected_criteria>IV4-AC1, IV4-AC2, IV4-AC3, IV4-AC4</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. `DrillTree.tsx` is NOT in this order's grant (it was IV-t-3's; do not touch it again here). `SliceTable.tsx`, `HoldingsSummary.tsx`, `slices.ts`, `contracts/**`, `api/**` are OUT.
- **Two repos, one worktree pair.** Same pair as IV-t-3: `<WS>` and `<WS>/portal`, based on `7c542fd23ec70c88bade4e3270f4c87f267a275a` (your branch already carries IV-t-3's commits). Portal entries commit in the portal repo (cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`); workspace records in `<WS>`. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean`.
- **Toolchain.** `node_modules` is a junction; **do not run `bun install`**. bun is `/c/Users/AndrewBerman/.bun/bin/bun`. Tests: `bun test <file>`.
- **The rules every cell obeys (PRD v0.5 CONTRACTS):** the FE derives nothing (no computed weights; `pctOfTotal` is the wire's); "not supplied", never zero; the producer's vocabulary only in the footer / popover, never in a cell; asset class and sector ABSENT until ruled.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is REFUSED and reported with your measurement -- never repaired, widened, or satisfied by a route this order did not name.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v1 @1f24052b87, cell `IV-t-4`.
<owned_cells>IV-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IV4-AC1` .. `IV4-AC4`. Instance at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/DSGN_IRPTV1.TO-IV-t-4.security-list.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> IV4-AC1,IV4-AC2,IV4-AC3,IV4-AC4` BEFORE the `complete` flip. `IV4-AC4` is recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO` -- a `PASS` or `FAIL` on a judgment row is INVALID. Result file `security-list.result.md` beside it. Flip `complete` only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row in the investigation file above -- that file does NOT exist yet (the row gate refuses an empty channel file, so it is minted by its FIRST row): if it is absent when you need it, create it with the header line `# DSGN_IRPTV1 -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (.tools/surprise-row-gate.py validates every NEW row).` followed by a fenced ```json array holding your row as its first item (the DSGN_REBRND W1-S1 precedent); a sibling slot may create the same file in its own worktree and the COO reconciles by UNION of rows at the drain (id `DSGN_IRPTV1-W3-S<k>`, continuing your slot's sequence).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at L5 (thread round; the lens runs on the enrichment round that touches its surface). The round's gates are sequencing inputs in the decomposition section 8; none is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: a word-boundary AWS-surface token sweep over the PRD at HEAD (v0.5, 26,070 bytes) returned 0 of 11 tokens; no cell writes an AWS surface.
comp-adversary: DECLARED-NOT-APPLICABLE at L5 (thread round); runs on the enrichment round against the PRD and these orders.
lane: the <paths> block IS the grant (RULING 1). Portal entries resolve to <WS>/portal/<rest> and commit in the portal repo. HoldingsTab.tsx is granted for the ONE following line after :197 at 7c542fd23ec70c88bade4e3270f4c87f267a275a (CTO 100332); IV4-AC3 grades the bound.
</preflight>

Seating: slot ~3, queue position 2 (after IV-t-3, same worktree pair, same subagent continued by the COO).
