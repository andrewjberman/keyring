# TO DSGN_IRPTV1.TO-IV-e-5 -- FWD-6 L1: allocation bars with the per-account matrix, and the treemap

<to_id>DSGN_IRPTV1.TO-IV-e-5</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~6</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>2</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-5` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-6 | **depends_on:** -- (chain C, alone) | **slot:** ~6, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-5` -- FWD-6's L1 and the treemap (PRD candidate C5 + C4's remainder; ROUND_ANALYSIS item 5; brief O5, CONCEPTS section 2.2). Build TWO new components under `portal/src/pages/InvestorReporting/tabs/holdings/` and mount them in `HoldingsTab.tsx` (CTO ruled touch T3: two added mount lines + at most two import lines, nothing removed).

**(a) `AllocationBars.tsx` -- L1.** One horizontal bar per L0 category (the snapshot's top-level categories under the root, labelled `display.label` else `displayName`, the Models / SMAs / Client triad the producer carries), length = the category's `pctOfTotal` (the wire's, never computed), the amount beside it (`amount` + `currency`, "not supplied" when null); an "expand" affordance per bar that reveals the PER-ACCOUNT MATRIX: one row per `account` node (label = `display.label` else `displayName` + masked tail), one column per category, each cell = the amount of that category's node beneath that account when the tree carries one, else "--" (never a sum, never a computed split; print nothing you did not read). The Positioning summary's frozen-header pattern (`pages/Positioning/panels/PositioningSummary.tsx`, read only) is the shape. `Panel variant="nested"`, `PanelHeader` "Allocation", `PanelContent`, a `PanelFooter` carrying basis + denominator + provenance (never in a cell).

**(b) `HoldingsTreemap.tsx` -- the L2 treemap.** Over the `security` leaves: size = `pctOfTotal`, colour = the nearest `model`/`sleeve` ancestor's label (the same ancestor rule `SecurityList.tsx` uses; a small deliberate duplicate is fine, `slices.ts` is out of grant), hover = ticker (`display.symbol` else "not supplied" -- NEVER a split id, the C-S12 rule), name, value, weight. Use the chart library the portal already renders treemaps with (`pages/Positioning/tabs/HoldingsTab.tsx`, read only, is the prior art; recharts' `Treemap` if that is what it uses). No asset class / sector anywhere. `Panel`, `PanelHeader` "Securities map", `PanelFooter`.

**(c) The mounts in `HoldingsTab.tsx`:** `<AllocationBars snapshot={snapshot} />` on its own line directly ABOVE the `<DrillTree snapshot={snapshot} />` line (find it by the element text and print the line; order: Summary, Allocation, Hero, Treemap, SecurityList) and `<HoldingsTreemap snapshot={snapshot} />` on its own line directly ABOVE `<SecurityList snapshot={snapshot} />`; the two imports. Nothing removed.

**Fixtures:** discover `fixtures/fe-s-7/holdings.*.json` from disk (the naming-gate rule); `fixtures/holdingsSnapshot.success.json`.

### ACCEPTANCE

<criterion id="IVE5-AC1" cell_refs="IV-e-5"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~6; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-5.allocation-bars.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: BARS-AND-MATRIX-OK</expect></criterion>
`IVE5-AC1` -- the built behaviour over each fixture: one bar per top-level category (`BARS: n of n`), each bar's width attribute / text equals the category's own `pctOfTotal` formatted and its amount text the node's own `amount` (print `COMPUTED: 0`), the matrix has one row per account node and one column per category with cells equal to the wire amounts where a node exists and "--" elsewhere (`MATRIX: r x c, filled f, dashes d`); no cell contains `basis`, `denominator`, `provenance` or a source coordinate; the footer does (positive control). `VERDICT: BARS-AND-MATRIX-OK` only when all hold.

<criterion id="IVE5-AC2" cell_refs="IV-e-5"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~6; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-5.treemap.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: TREEMAP-OK</expect></criterion>
`IVE5-AC2` -- the treemap's data derivation (the pure function you export, no chart rendering in the assertion): one node per security leaf (`NODES: n of n leaves`), size = `pctOfTotal` (null leaves excluded and counted: `EXCLUDED-NULL-WEIGHT: k`), group = the nearest model/sleeve label, the hover label's ticker = `display.symbol` when present else "not supplied" with NO substring of `securityId` (the C-S12 rule as a negative arm) and a PLANTED symbol printed as the positive control. `VERDICT: TREEMAP-OK` only when all hold.

<criterion id="IVE5-AC3" cell_refs="IV-e-5"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~6; timeout 120 python -c "import subprocess;b='895752676a45e83dc252d4253aebc5fa316a229e';f='src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx';n=subprocess.run(['git','diff','--numstat',b,'--',f,'src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx','src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx','src/pages/InvestorReporting/tabs/holdings/HoldingsSummary.tsx'],capture_output=True,text=True).stdout.strip().splitlines();d=subprocess.run(['git','diff','-U0',b,'--',f],capture_output=True,text=True).stdout;ch=[l for l in d.splitlines() if (l.startswith('+') or l.startswith('-')) and not l.startswith('+++') and not l.startswith('---')];other=[l for l in ch if not l[1:].lstrip().startswith('import ') and 'AllocationBars' not in l and 'HoldingsTreemap' not in l];print('NUMSTAT:',n);print('CHANGED:',len(ch),'OUTSIDE:',other);ok=(len(n)==1 and n[0].split()[2].endswith('HoldingsTab.tsx') and n[0].split()[1]=='0' and int(n[0].split()[0])<=4 and not other);print('VERDICT:','TWO-MOUNTS-ONLY' if ok else 'TOUCH-WIDER-THAN-RULED')"</invocation><expect>VERDICT: TWO-MOUNTS-ONLY</expect></criterion>
`IVE5-AC3` -- the ruled touch T3: `HoldingsTab.tsx` differs from `895752676a45e83dc252d4253aebc5fa316a229e` by at most four added lines (two mounts, up to two imports), nothing removed, every changed line a mount or an import; `DrillTree.tsx`, `SecurityList.tsx`, `HoldingsSummary.tsx` untouched.

<criterion id="IVE5-AC4" cell_refs="IV-e-5" judgment="true"/>
`IVE5-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the static markup (`iv-e-5.allocation.html`, `iv-e-5.treemap.html`) and the smoke PNG if IV-e-2's fixture renders it: an advisor who has used Positioning recognises the bars, the frozen matrix and the treemap without explanation (brief Part III); C2 tabular numerals, C3, C6 (the data colours keep their chroma; the chrome is quiet), C10. RECORD; NO VERDICT.

<expected_criteria>IVE5-AC1, IVE5-AC2, IVE5-AC3, IVE5-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `DrillTree.tsx`, `SecurityList.tsx`, `HoldingsSummary.tsx`, `SliceTable.tsx`, `slices.ts` (read only), `components/**` (DSGN_REBRND's / Positioning's), `contracts/**`, `api/**` are OUT.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `895752676a45e83dc252d4253aebc5fa316a229e`). Same commit discipline. Never push, merge, rebase, `checkout --`, `clean`.
- **The rules:** the FE derives nothing -- every width, amount and weight is the node's own field; no sum, no computed split; ids never print; asset class / sector absent; "not supplied" / "--" never zero.
- **Refusal clause.** As every order. **Your queue:** this order only; then the pair ends.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-5`.
<owned_cells>IV-e-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE5-AC1` .. `IVE5-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~6/DSGN_IRPTV1.TO-IV-e-5.holdings-l1-and-treemap.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> IVE5-AC1,IVE5-AC2,IVE5-AC3,IVE5-AC4` BEFORE the flip. `IVE5-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `holdings-l1-and-treemap.result.md`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W6-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register; none owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands.
comp-adversary: RUN at L5 v2 on the PRD (9/9 commits verified; 6 paths, 5 stable, 1 flagged).
lane: the <paths> block IS the grant. HoldingsTab.tsx (M-written) admitted for two mount lines + two imports (CTO touch T3).
</preflight>

Seating: slot ~6, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 6`.
