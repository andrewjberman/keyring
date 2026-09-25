# TO DSGN_IRPTV1.TO-IV-e-10 -- FWD-2 as amended: accounts are chosen next to the view they narrow (Holdings, Performance)

<to_id>DSGN_IRPTV1.TO-IV-e-10</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~7</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-10` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-2 | **depends_on:** IV-e-9 (chain A) | **slot:** ~7, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-10` -- PRD v0.6 candidate C16. The header no longer carries account chips (DEV 93b28880). Put the account
choice next to the view it narrows:

**(a) Holdings.** An account filter above the drill in `IR/tabs/holdings/HoldingsTab.tsx` (ONE mount line + at most one
import: a ruled touch on an M-written file). Options are the accepted selection's accounts by directory name + masked tail
(reuse `IR/header/IdentityCard.tsx`'s `fetchIdentityCardData` / `overWhatFor` shapes; never an `acc_` id); choosing one
narrows through the existing server-accepted selection path (`narrowToOneAccount` / `restoreFullSelection` in
`IdentityCard.tsx`), "All accounts" restores.

**(b) Performance.** `IR/tabs/reporting/AccountsTable.tsx` rows become the filter: clicking an account narrows the same way;
the uncovered-account row stays a row with its reason.

The Analysis input's account choice is `IV-e-14`'s, not this order's.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE10-AC1" cell_refs="IV-e-10"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-10.holdings-filter.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: HOLDINGS-FILTER-OK</expect></criterion>
`IVE10-AC1` -- the filter lists the selection's accounts by name + masked tail with zero `acc_` substrings in the markup; choosing one calls the narrowing path with exactly that account; "All accounts" restores the full set. The test prints `VERDICT: HOLDINGS-FILTER-OK` only when every arm holds.

<criterion id="IVE10-AC2" cell_refs="IV-e-10"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-10.accounts-table-filter.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ACCOUNTS-TABLE-FILTER-OK</expect></criterion>
`IVE10-AC2` -- an AccountsTable row click narrows through the same path; the uncovered-account row stays a row with its reason; no id prints. The test prints `VERDICT: ACCOUNTS-TABLE-FILTER-OK` only when every arm holds.

<criterion id="IVE10-AC3" cell_refs="IV-e-10"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-10.ruled-touch.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: RULED-TOUCH-OK</expect></criterion>
`IVE10-AC3` -- `HoldingsTab.tsx` differs from `13b5356fad4779b990e8e7a88636430204b30e42` by at most two added lines (one mount, one import), nothing removed. The test prints `VERDICT: RULED-TOUCH-OK` only when every arm holds.

<criterion id="IVE10-AC4" cell_refs="IV-e-10" judgment="true"/>
`IVE10-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: an advisor narrows to one account from inside Holdings and Performance without scrolling to the top (FWD-2 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE10-AC1, IVE10-AC2, IVE10-AC3, IVE10-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/tabs/holdings/AccountFilter.tsx
portal/src/pages/InvestorReporting/tabs/reporting/AccountsTable.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-10`.
<owned_cells>IV-e-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE10-AC1, IVE10-AC2, IVE10-AC3, IVE10-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~7/DSGN_IRPTV1.TO-IV-e-10.accounts-in-the-view.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE10-AC1,IVE10-AC2,IVE10-AC3,IVE10-AC4` BEFORE the flip. `IVE10-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W7-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~7, queue position 2 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 7 --portal-ref <portal_ref at the cut>`.
