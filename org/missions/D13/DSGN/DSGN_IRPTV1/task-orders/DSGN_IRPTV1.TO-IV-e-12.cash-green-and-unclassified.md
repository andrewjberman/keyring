# TO DSGN_IRPTV1.TO-IV-e-12 -- FWD-13 remainder: cash is green on Positioning too; an unclassified security says so

<to_id>DSGN_IRPTV1.TO-IV-e-12</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~8</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-12` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-13 | **depends_on:** IV-e-11 (chain B) | **slot:** ~8, queue position 2 of 3

---

## WORKER FACE

### THE CELL

`IV-e-12` -- PRD v0.6 candidate C18 remainder (Andrew's call C1: cash is GREEN, on Positioning too). DEV 13b5356f
already colours the Securities map, table and models dialog by the served `asset_class` (Unclassified until M emits).

**(a)** `portal/src/lib/chartColors.ts` `ASSET_CLASS.cash` becomes the fixed-income green family (a distinct green step so a
cash row stays distinguishable inside fixed income -- name the token you choose and why). Positioning is the named reader:
screenshot its holdings tab before and after; only the cash colour may change. **(b)** Investor Reporting: the treemap
legend, hover card and securities table say "Unclassified" in advisor words for a security whose served class is
unclassified or absent -- never another class's colour.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE12-AC1" cell_refs="IV-e-12"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-12.cash-green.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CASH-GREEN-OK</expect></criterion>
`IVE12-AC1` -- ASSET_CLASS.cash is a green (hue within the fixed-income family), distinct from fixedIncome; every other ASSET_CLASS key is unchanged from the base. The test prints `VERDICT: CASH-GREEN-OK` only when every arm holds.

<criterion id="IVE12-AC2" cell_refs="IV-e-12"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-12.positioning-reader.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: POSITIONING-ONLY-CASH-MOVED</expect></criterion>
`IVE12-AC2` -- the Positioning holdings colour map at the base and now differs in the cash entry only (printed diff of every class key). The test prints `VERDICT: POSITIONING-ONLY-CASH-MOVED` only when every arm holds.

<criterion id="IVE12-AC3" cell_refs="IV-e-12"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-12.unclassified.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: UNCLASSIFIED-OK</expect></criterion>
`IVE12-AC3` -- a security with no served class, and one served `unclassified`, both render the grey Unclassified colour and the word Unclassified in the legend and hover; none borrows another class. The test prints `VERDICT: UNCLASSIFIED-OK` only when every arm holds.

<criterion id="IVE12-AC4" cell_refs="IV-e-12" judgment="true"/>
`IVE12-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: equities blue, fixed income and cash green, alternatives orange, structured pink, commodities gold -- the same on Positioning and here (FWD-13 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE12-AC1, IVE12-AC2, IVE12-AC3, IVE12-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `13b5356fad4779b990e8e7a88636430204b30e42`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/lib/chartColors.ts
portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-12`.
<owned_cells>IV-e-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE12-AC1, IVE12-AC2, IVE12-AC3, IVE12-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~8/DSGN_IRPTV1.TO-IV-e-12.cash-green-and-unclassified.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE12-AC1,IVE12-AC2,IVE12-AC3,IVE12-AC4` BEFORE the flip. `IVE12-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W8-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~8, queue position 2 of 3; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 8 --portal-ref <portal_ref at the cut>`.
