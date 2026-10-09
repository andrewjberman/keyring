# TO ADVI_BILLING.TO-AB-e-6 -- E2+E3 consumer: fee_quarter v2 reads the household from the crosswalk and SMArtX rates and true-up from the silver fee statement when present; dry run only

<to_id>ADVI_BILLING.TO-AB-e-6</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~3</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-e-6` (decomposition section 3, round 2) | **outcome_ref:** FWD-1 / FWD-3 | **depends_on:** AB-e-4 (its contract), AB-e-5 (its object).

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-3`; run everything from its root. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/`.

**The cell.** `data/assets/scripts/gold/advi_billing/fee_quarter.py` (round 1; contract `org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json`)
takes the household from Black Diamond fee lines and the ADVISOR rate from BD's schedule; the PLATFORM portion has no schedule.

1. v2: the household's accounts come from the `household_crosswalk` (AB-e-5; newest `date=` partition at
   `address("advi","49financial","gold","household_crosswalk",...)`), and the object gains `household_source` = `household_crosswalk`
   (`bd_fee_lines` when it falls back). Where a silver `smartx_fee_statement` partition exists for the quarter (AB-e-4's contract), each
   account's ADVISOR and PLATFORM rates and the SmartX/Advisor true-up (shown as a named adjustment) come from it, summed over the account's
   allocations, with `schedule_claim` measured and `schedule_source` SMArtX; otherwise round 1's behaviour stands. Keep the contract's
   field set (additive only; bump `contract_version` to 0.2.0 if you add fields) so the served panel still renders.
2. Tests `data/assets/scripts/gold/advi_billing/tests/test_fee_quarter_v2.py`: fixtures only, including a test named with `crosswalk`
   (household from the crosswalk) and one named with `smartx` (rates and true-up from a synthetic silver frame).
3. A DRY run (no `--write`) for `--quarter 2026Q3 --client-key z08219260` against the real crosswalk, saving the object to
   `.scratch/advi_billing/AB_E6_DRYRUN.json` in the worktree root (gitignored; it carries client figures and is never committed).

<criterion id="AB2-6-AC1" cell_refs="AB-e-6"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-6-AC1</invocation><expect>AB2-6-AC1 PASS</expect></criterion>
`AB2-6-AC1` -- the v2 tests pass, one named *crosswalk*, one named *smartx*. Base: FAIL.

<criterion id="AB2-6-AC2" cell_refs="AB-e-6"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-6-AC2</invocation><expect>AB2-6-AC2 PASS</expect></criterion>
`AB2-6-AC2` -- the dry-run object for z08219260 conforms to the contract and takes its household from the crosswalk. Base: FAIL.

<expected_criteria>AB2-6-AC1,AB2-6-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- S3 reads only; NO S3 write (the served object stays as round 1 wrote it); no vendor call.
- **Refusal clause.** An edit outside the grant, a write the face does not name, a vendor call, a secret read, or an account
  number, name or dollar figure in a committed file is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/advi_billing/fee_quarter.py
data/assets/scripts/gold/advi_billing/tests/
org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-e-6.fee-quarter-v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 3 (round 2), cell `AB-e-6`.
<owned_cells>AB-e-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB2-6-AC1, AB2-6-AC2. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/ADVI_BILLING.TO-AB-e-6.fee-quarter-v2.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB2-6-AC1,AB2-6-AC2` BEFORE the flip.
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
checks dry-run at base: AB2-6-AC1, AB2-6-AC2 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
