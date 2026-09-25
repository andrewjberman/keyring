# TO DSGN_IRPTV1.TO-IV-e-30 -- the Cottonwood client drill colours cash and other by the tenant palette: thread the layout through CanonicalBookView and its callers (DIRECT-ACT, row W19-S1)

<to_id>DSGN_IRPTV1.TO-IV-e-30</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~20</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>pending</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-30` (decomp v4 addendum 4) | **outcome_ref:** FWD-13 (its reader: the Advisor Intelligence page) | **depends_on:** IV-e-29 (merged, local DEV b997c9e5) | **slot:** ~20, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-30` -- row `DSGN_IRPTV1-W19-S1` (ARMED). IV-e-29 gave `ConsolidatedOverviewPanel`
(`src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx`) an optional `tenantLayout` prop: when
supplied, every legend and donut colour resolves through `tenantLayout.assetClasses.colorPalette` keyed by the served class
(Cottonwood: `cash` -> `ASSET_CLASS.cash`, `other` -> `PALETTE.purple600`), else the MIX_PIE colour. But its only product
caller, `_shared/panels/CanonicalBookView.tsx` (line ~97), does not pass it, so Cottonwood's real client drill still
colours cash in the MIX_PIE amber. Read `git -C <WS>/portal show b997c9e5 --stat` and the two files first.

**The change.** (a) `CanonicalBookView` takes an optional `tenantLayout?: TenantLayoutConfig` prop and forwards it to
`ConsolidatedOverviewPanel`. (b) Every caller passes it: `_shared/AdvisorBookView.tsx` (~1086) passes the `tenantLayout`
it already holds (`useTenantLayout(firmId, firmOverride)`, ~379); `_shared/tabs/ClientsTab.tsx` (~812) passes
`dataSourceLayout` (`useTenantLayout(firmId, firmOverride)`, ~151 -- the firm being viewed); `_shared/AdvisorBookClientDetail.tsx`
(~171) has no firm id, so it takes its own optional `tenantLayout` prop, forwards it, and its two callers
(`AdvisorBookView.tsx` ~930, `ClientsTab.tsx` ~730) pass the same layouts as above. Strictly additive: an omitted prop
keeps today's behaviour. Nothing else changes.

**The rules:** the FE derives nothing; colour is keyed by the served class, never a label substring or a guess.

**Environment:** the portal worktree is based on local DEV `b997c9e5`. The tests live in the existing
`portal/src/pages/AdvisorIntelligence/__tests__/cot-other/` (reuse `discover-layouts.ts` and the render approach of `cot-drill-legend.test.ts`; never type a
firm token). Write each criterion's test from its text; it prints the VERDICT only when every arm holds. Do not start any
server (dev builds run on port 5174 only, serving the main checkout). The PROD promotion is NOT yours.

### ACCEPTANCE

<criterion id="IVE30-AC1" cell_refs="IV-e-30"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-20/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~20; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-drill-thread.render.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: DRILL-THREAD-OK</expect></criterion>
`IVE30-AC1` -- `CanonicalBookView` rendered with the Cottonwood layout (discovered from disk) and a composition carrying `cash` and `other` forwards the layout to `ConsolidatedOverviewPanel`: the legend's Cash entry carries `ASSET_CLASS.cash` and its Other entry `PALETTE.purple600`; the same render WITHOUT the layout prop gives the Cash entry the MIX_PIE colour (`mixPieColor('cash')`), the difference-control arm. The test prints `VERDICT: DRILL-THREAD-OK` only when every arm holds.

<criterion id="IVE30-AC2" cell_refs="IV-e-30"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-20/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~20; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-drill-thread.callsites.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CALLSITES-THREADED-OK</expect></criterion>
`IVE30-AC2` -- a scan of every `.tsx` file under `src/pages/AdvisorIntelligence/` (tests excluded) finds every JSX use of `<CanonicalBookView` and of `<AdvisorBookClientDetail`, prints the count of each (the denominator), and finds a `tenantLayout=` attribute on every one; `AdvisorBookClientDetail` forwards the prop it receives to its `<CanonicalBookView`. The test prints `VERDICT: CALLSITES-THREADED-OK` only when every arm holds.

<criterion id="IVE30-AC3" cell_refs="IV-e-30" judgment="true"/>
`IVE30-AC3` -- graded by `2.0.0_SA_COO~D` at the drain on the running page (localhost:5174, Advisor Intelligence, Cottonwood, one client drill): the donut and legend show Cash in the asset-class cash green and Other in purple. RECORD; never self-graded.

<expected_criteria>IVE30-AC1, IVE30-AC2, IVE30-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `pages/InvestorReporting/**`,
  `contracts/**`, `api/**`, `src/lib/**` and every other page are OUT.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `b997c9e5c3b8071fc317f8e56cbef5105197637e`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/AdvisorIntelligence/_shared/panels/CanonicalBookView.tsx
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookClientDetail.tsx
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx
portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx
portal/src/pages/AdvisorIntelligence/__tests__/cot-other/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 addendum 4, cell `IV-e-30`.
<owned_cells>IV-e-30</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE30-AC1, IVE30-AC2, IVE30-AC3. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~20/DSGN_IRPTV1.TO-IV-e-30.ai-drill-tenant-thread.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE30-AC1,IVE30-AC2,IVE30-AC3` BEFORE the flip. `IVE30-AC3` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s look at the running page at the drain.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W20-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at the addendum -- the call sites measured at portal local DEV b997c9e5 (CanonicalBookView.tsx:97 passes no tenantLayout; callers AdvisorBookView.tsx:1086, ClientsTab.tsx:812, AdvisorBookClientDetail.tsx:171; AdvisorBookClientDetail callers AdvisorBookView.tsx:930, ClientsTab.tsx:730).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~20, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 20 --portal-ref b997c9e5c3b8071fc317f8e56cbef5105197637e`.
