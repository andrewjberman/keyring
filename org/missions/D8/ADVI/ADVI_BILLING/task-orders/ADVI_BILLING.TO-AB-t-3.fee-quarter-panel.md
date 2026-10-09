# TO ADVI_BILLING.TO-AB-t-3 -- FWD-1 hop 4: the advisor's quarter-fee panel -- one household's fee for one billed quarter, how it was worked out, and how it compares with what Schwab took -- built against the seam contract's fixture

<to_id>ADVI_BILLING.TO-AB-t-3</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~2</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-t-3` (decomposition section 2) | **outcome_ref:** FWD-1 | **depends_on:** none (the contract is fixed in the decomposition).

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-2`; the portal inside it is `C:/dev/wk-advi-billing-2/portal`, provisioned at portal
`DEV` `2d42e9b7`. Run workspace commands from the worktree root and `bun` commands from `portal/`. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~2/`.

**The cell.** An advisor at 49 Financial opens a household (`/advisor-intelligence` -> `_partners/49financial/index.tsx` ->
`_shared/AdvisorBookClientDetail.tsx`) and must be able to answer "why is my fee this number?" for one billed quarter. Build the
panel that shows it. It goes BELOW the existing panels and replaces nothing: the existing `tabs/FeeSummaryPanel.tsx` shows the
running fee rate and advisor split, not a billed quarter, and stays as it is.

- **Files you write (and nothing else under `portal/`):**
  - `portal/src/api/endpoints/advi-billing.ts`: the `FeeQuarter` TypeScript type (the contract below, field for field) and
    `getFeeQuarter(clientKey: string, quarter: string, firmOverride?: string)` calling
    `/api/scoped/partners/books/relationship/${clientKey}/fee-quarter/${quarter}` exactly as `getPlatinumClientSummary` in
    `portal/src/api/endpoints/advisor-intelligence.ts:1033-1040` calls its route (same `apiRequest`, same `firmId` rule).
  - `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.tsx`: a presentational component `AdvisorBookFeePanel`
    taking `{ data: FeeQuarter }` (a thin wrapper that fetches may live in the same file; the hookup into
    `AdvisorBookClientDetail.tsx` is NOT yours -- the issuer adds that one line at the merge; name it in your report).
  - `portal/src/pages/AdvisorIntelligence/_shared/__fixtures__/adviBillingFeeQuarter.json`: an example object of the contract,
    with invented values (no real client data): 2 accounts, `billing_convention` ADVANCE, one component MATCH, one DIFFERS with a
    reason, one NO_DEBIT, `steps` of at least 3 lines.
  - `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.test.tsx`: a `bun test` that server-renders the panel
    (`react-dom/server` `renderToStaticMarkup`) on the fixture and asserts the household fee, each account line, every
    `reconcile_class` label, the DIFFERS reason and every `steps` line appear.
- **What the panel shows:** the quarter and period; household billable value, computed fee, debited fee and the agreement label
  (MATCH "Matches Schwab", DIFFERS "Differs from Schwab" + the reason, NO_DEBIT "No Schwab debit found"); per account: value
  charged on, the schedule (rate as bps), days in period / days in year, flow adjustment and exclusions when non-zero, then the two
  components (Advisor fee / Platform fee) computed vs debited; the `steps` lines; and a source note from each `*_claim` + source
  ("Rates from SMArtX statement (measured)"). Use the page's own kit: `Panel`, `PanelHeader`, `PanelContent` from
  `@/ui/components/panels`, `formatCurrency` from `@/lib/universalNumberFormatter`, `HelperTip` as `FeeSummaryPanel.tsx` does.
  The portal's colour law: light canvas, white hairline panels, navy ink; no light text on light fills.
- **The contract (field for field; `org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json` is being written in parallel and will
  carry the same fields):**
  ```
  contract_version ("0.1.0"), firm ("49financial"), relationship_id, client_key, quarter ("2026Q3"),
  billing_convention (ADVANCE|ARREARS|UNRESOLVED), billing_convention_claim (measured|inferred|held|absent),
  period_start, period_end, valuation_date, as_of,
  accounts[]: { account_id, billable_value, value_source, schedule{label,rate_type,basis_points,flat_fee,tiers[]},
                schedule_claim, schedule_source, flow_adjustment, flows_in_period[], excluded_value, exclusion_reason,
                days_in_period, days_in_year,
                components[]: { portion (ADVISOR|PLATFORM), rate, debit_code (TPFEE|SMFEE), computed_fee, debited_fee,
                                debit_date, difference, reconcile_class (MATCH|DIFFERS|NO_DEBIT), difference_reason } },
  household: { billable_value, computed_fee, debited_fee, difference, reconcile_class, difference_reason },
  steps[] (strings)
  ```
  Rules: `difference_reason` is a non-empty string on DIFFERS and null otherwise; each account carries exactly one ADVISOR
  (TPFEE) and one PLATFORM (SMFEE) component; a NO_DEBIT component has `debit_date` null.

<criterion id="AB1-3-AC1" cell_refs="AB-t-3"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-3-AC1</invocation><expect>AB1-3-AC1 PASS</expect></criterion>
`AB1-3-AC1` -- the panel's `bun test` passes on the fixture. Base: FAIL.

<criterion id="AB1-3-AC2" cell_refs="AB-t-3"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-3-AC2</invocation><expect>AB1-3-AC2 PASS</expect></criterion>
`AB1-3-AC2` -- the fixture conforms to the seam contract (the same validator the gold object is graded by). Base: FAIL.

<criterion id="AB1-3-AC3" cell_refs="AB-t-3" judgment="true"/>
`AB1-3-AC3` -- JUDGMENT (graded by `3.0.0_SA_CVO` at L9 on the issuer's real-run screenshot): an advisor can answer "why is my
fee this number?" from the panel alone.

<expected_criteria>AB1-3-AC1,AB1-3-AC2,AB1-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited -- in particular `AdvisorBookClientDetail.tsx`,
  `FeeSummaryPanel.tsx`, `advisor-intelligence.ts` and every shared kit file.
- **No new dependency** (no `bun add`, no package download); no push of any branch; no AWS call.
- **Refusal clause.** An edit outside the grant, a new package, real client data in the fixture, or a push is a defect: stop and
  file a row.

<paths>
portal/src/api/endpoints/advi-billing.ts
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.tsx
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.test.tsx
portal/src/pages/AdvisorIntelligence/_shared/__fixtures__/adviBillingFeeQuarter.json
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~2/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-t-3.fee-quarter-panel.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 2 (round 1), cell `AB-t-3`.
<owned_cells>AB-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB1-3-AC1, AB1-3-AC2, AB1-3-AC3 (judgment: record it `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming
3.0.0_SA_CVO). The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~2/ADVI_BILLING.TO-AB-t-3.fee-quarter-panel.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB1-3-AC1,AB1-3-AC2,AB1-3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the portal commit hash (on your portal worktree branch) and workspace commit hash, each criterion's last line, the
hookup line the issuer must add to `AdvisorBookClientDetail.tsx` (file, line, text), and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- four NEW portal files; 0 existing files edited; the page changes only at the issuer's one-line hookup.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS surface.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: the panel calls a route AB-t-2 plans; no route is touched here.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: thread round; the lens runs on the enrichment round that touches its surface.
checks dry-run at base: AB1-3-AC1/AC2 FAIL as expected.
client-facing: the 49 Financial partner page is client-facing; DEV only, PROD waits on Andrew's word (CLAUDE.md push law, d92d08c448).
lane: the <paths> block IS the grant.
</preflight>
