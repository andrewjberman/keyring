# TO ADVI_BILLING.TO-AB-e-4 -- E2 content: the SMArtX fee-statement parser -- bronze workbook to silver smartx_fee_statement, with its contract, on a synthetic workbook

<to_id>ADVI_BILLING.TO-AB-e-4</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~3</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-e-4` (decomposition section 3, round 2) | **outcome_ref:** FWD-1 / FWD-3 (E2 content) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-3`; run everything from its root. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/`.

**The cell.** SMArtX bills 49 Financial in advance, one row per account allocation (sleeve). Its quarterly export (one header row)
carries 33 columns, measured by the issuer, including: `AllocationID`, `Brokerage Account Number`, `Sleeve Type`, `Model Name`,
`Fee Period Start`, `Fee Period End`, `SmartX Prior Quarter Estimate`, `SmartX Prior Quarter Actual`, `SmartX True-Up`,
`Advisor Prior Quarter Estimate`, `Advisor Prior Quarter Actual`, `Advisor True-Up`, `UMA Fee Rate`, `APM Fee Rate`, `Model Fee Rate`,
`Advisor Fee Rate`, `Client Fee Rate`, `Current Period Estimate Valuation`, `Days in Period`, `Days in Year`, `Net SmartX Fee`,
`Net Advisor Fee`, `Fee Debit`. Fee = valuation x rate x Days in Period / Days in Year (251 trading days); `Fee Debit` = Net SmartX + Net
Advisor and carries the prior-quarter true-up. A Q3 "Deficit Report" variant puts the same layout on a sheet named like
`49F Q3-26 Deficit Details`. No real file is in Opal yet (another cell builds the landing path).

1. `data/assets/scripts/silver/advi_billing/smartx_fee_statement.py`: reads a workbook (a local path or the bronze key
   `address("smartx","49financial","bronze","fee_statement","quarter=<q>","<file>.xlsx")`), finds the header row by these names
   (tolerant of case/whitespace and of extra columns), normalizes names to snake_case, types money/rates/dates, pads
   `Brokerage Account Number` to 10 digits, and writes (only with `--write`) parquet to
   `address("advi","49financial","silver","smartx_fee_statement","quarter=<q>","data.parquet")`. Use `openpyxl` or `pandas` if already
   installed; install nothing.
2. `org/standards/ADVI_BILLING_SMARTX_FEE_STATEMENT_CONTRACT.json` (version 0.1.0): `source_columns` (a list of the source names above,
   each with its silver name, type and meaning), the silver builder address string, and the rule that rates are annual fractions.
3. Tests `data/assets/scripts/silver/advi_billing/tests/test_smartx_fee_statement.py`: build a SYNTHETIC workbook in a temp dir with
   those columns and invented values (two allocations of one account; one true-up), and a test named with `parses` asserting the typed
   rows, the padding and the fee formula on the synthetic values. No S3 write in tests.

<criterion id="AB2-4-AC1" cell_refs="AB-e-4"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-4-AC1</invocation><expect>AB2-4-AC1 PASS</expect></criterion>
`AB2-4-AC1` -- the parser tests pass, one named *parses*. Base: FAIL.

<criterion id="AB2-4-AC2" cell_refs="AB-e-4"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-4-AC2</invocation><expect>AB2-4-AC2 PASS</expect></criterion>
`AB2-4-AC2` -- the contract lists every measured source column and carries the silver builder address. Base: FAIL.

<expected_criteria>AB2-4-AC1,AB2-4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- No S3 write; no real client file; no vendor call.
- **Refusal clause.** An edit outside the grant, a write the face does not name, a vendor call, a secret read, or an account
  number, name or dollar figure in a committed file is a defect: stop and file a row.

<paths>
data/assets/scripts/silver/advi_billing/
org/standards/ADVI_BILLING_SMARTX_FEE_STATEMENT_CONTRACT.json
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-e-4.smartx-fee-statement-parser.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 3 (round 2), cell `AB-e-4`.
<owned_cells>AB-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB2-4-AC1, AB2-4-AC2. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/ADVI_BILLING.TO-AB-e-4.smartx-fee-statement-parser.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB2-4-AC1,AB2-4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what the cell measured (counts, classes, masked ids only), and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- code only; no served key or route moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role is created or changed in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: enrichment cell; no served claim is graded here.
checks dry-run at base: AB2-4-AC1, AB2-4-AC2 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
