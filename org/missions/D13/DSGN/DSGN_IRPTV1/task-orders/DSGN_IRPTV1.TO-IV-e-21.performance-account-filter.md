# TO DSGN_IRPTV1.TO-IV-e-21 -- FWD-2: the account choice at rest on Performance (IVE10)

<to_id>DSGN_IRPTV1.TO-IV-e-21</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~12</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>complete</status>
<round>4</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-21` (decomp v4 @d4add46f46) | **outcome_ref:** FWD-2 | **depends_on:** -- (chain 1) | **slot:** ~12, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-21` -- the round-3 grade IVE10-AC4 FAILED (ADJUDICATION_v2 C-S15): Holdings offers "Account: All accounts" beside
the view, but Performance does not -- its accounts table sits inside the collapsed "Monthly returns and accounts".

Mount the shared `IR/tabs/holdings/AccountFilter.tsx` (READ ONLY: it already reads `HeaderSelectionContext` when its props
are absent) in `IR/tabs/reporting/ReportingTab.tsx` above the Performance headline, outside every closed disclosure: one
import and one mount line. It renders nothing without a selection, so the no-client sample view is unchanged.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

**Environment (every cell):** the portal worktree is based on DEV `8242412d` (round 3 merged). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. The header's accepted selection reaches tab bodies through `IR/header/HeaderSelectionContext.ts` (wrap a render in `HeaderSelectionContext.Provider` to exercise it). Do not start any server: dev builds run on port 5174 only, and 5174 serves the main checkout, not your worktree.

### ACCEPTANCE

<criterion id="IVE21-AC1" cell_refs="IV-e-21"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~12; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-21.performance-filter.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PERF-FILTER-OK</expect></criterion>
`IVE21-AC1` -- with a HeaderSelectionContext carrying a two-account selection and named entries, the Performance tab markup renders the account filter naming both accounts by name + masked tail with zero `acc_` substrings; the filter's change handler, given one account, calls onNarrow with that account's narrowed selection. The test prints `VERDICT: PERF-FILTER-OK` only when every arm holds.

<criterion id="IVE21-AC2" cell_refs="IV-e-21"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~12; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-21.at-rest.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: FILTER-AT-REST-OK</expect></criterion>
`IVE21-AC2` -- the filter sits outside every `<details>` element and before the headline in document order; with no provider the Performance markup carries no filter and renders without error. The test prints `VERDICT: FILTER-AT-REST-OK` only when every arm holds.

<criterion id="IVE21-AC4" cell_refs="IV-e-21" judgment="true"/>
`IVE21-AC4` -- graded at the round-4 drain by `2.0.0_SA_COO~D` on the signed-in trace (IRPT_BCKEND principal IB-rtf-3, else Andrew's walk on `localhost:5174`), per CTO 100991 -- never the CVO: an advisor narrows to one account from inside Performance without opening a disclosure (FWD-2 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE21-AC1, IVE21-AC2, IVE21-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `8242412dde9a3ef807e118f648242cf24ffe2981`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 @d4add46f46, cell `IV-e-21`.
<owned_cells>IV-e-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE21-AC1, IVE21-AC2, IVE21-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~12/DSGN_IRPTV1.TO-IV-e-21.performance-account-filter.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE21-AC1,IVE21-AC2,IVE21-AC4` BEFORE the flip. `IVE21-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s drain trace (CTO 100991).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W12-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v4 section 5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v4 -- every write path measured at portal DEV 8242412d at the cut (decomp v4 section 5).
lane: the <paths> block IS the grant; the write sets are pairwise disjoint (decomp v4 section 2).
</preflight>

Seating: slot ~12, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 12 --portal-ref 8242412dde9a3ef807e118f648242cf24ffe2981`.
