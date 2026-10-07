# TO IRPT_BCKEND.TO-IB-pr-343 -- an export receipt names its covered accounts at freeze, and an export read with an empty list is REFUSED (PRD v0.30 items 33-34, W142-S4)

<to_id>IRPT_BCKEND.TO-IB-pr-343</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~145</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 PRIORITY msg 439 (row W142-S4, ARMED), PRD v0.30 @f20371eb03 items 33-36, item (1); cut first in round 65 | **Decomp cell:** `IB-pr-343`
(decomposition section 58) | **outcome_ref:** FWD-2 (scope enforcement on every export read) | **depends_on:** none.

---

## WORKER FACE

**The defect (row IRPT_BCKEND-W142-S4, ARMED: export reads FAIL OPEN).** `infra/aws/lambda/investor-reporting/export/entry.py` `_covered(scope, receipt)` (about :142-155)
collects the receipt's named accounts from `facts.account_ids` / `accountIds` / `covered_account_ids`, and when it finds NONE it returns
`(True, 0, 0)`: a receipt naming no account admits any firm advisor holding the export id. The receipt schema
(`docs/contracts/investor-reporting/v1/ExportReceipt.schema.json` and its copy
`infra/aws/lambda/investor-reporting/_contracts/ExportReceipt.schema.json`) names no account field at all (facts carries page_count,
validation_status, validation_failures, frozen_as_of). PRD v0.30 items 33-36 rule the fix.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-145`; run everything from its root):

1. **Schema.** Both ExportReceipt.schema.json copies: `facts.covered_account_ids` is REQUIRED, an array of strings, `minItems` 1.
2. **Derive at freeze.** The receipt writer (`infra/aws/lambda/investor-reporting/export/receipt.py`; read `bundle.py` `freeze` and `retained_export.py` `freeze_platinum(body,
   permitted_account_ids, ...)` for where the covered set is known) writes `facts.covered_account_ids` = the accounts the frozen bundle
   actually covers, at freeze time, never empty for a READY receipt.
3. **Refuse empty.** `_covered` returns NOT covered for an empty or missing list: an export read whose receipt names no account is REFUSED
   (with the refusal class the route already uses for an out-of-scope read). Keep the other branches.
4. **Tests** `infra/aws/lambda/investor-reporting/export/tests/test_covered_account_ids.py` (new; names `covered_account_ids`): one test per `_covered` branch (all inside scope
   -> admitted; one outside -> refused; EMPTY -> refused; missing -> refused) and one that a frozen receipt carries a non-empty list.
   The export suite must show no failure beyond the six pypdf-only tests (pypdf is not on this box).

**Not yours:** back-filling existing receipts (IB-pr-344, this slot's next order) and the release (the issuer's, with r61's packet).

<criterion id="IB65-1-AC1" cell_refs="IB-pr-343"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py" . IB65-1-AC1</invocation><expect>IB65-1-AC1 PASS</expect></criterion>
`IB65-1-AC1` -- the covered-accounts tests pass (each _covered branch; empty refused; derived at freeze) and the export suite has no failure beyond the six pypdf-only tests. Base: FAIL (no test).

<criterion id="IB65-1-AC2" cell_refs="IB-pr-343"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py" . IB65-1-AC2</invocation><expect>IB65-1-AC2 PASS</expect></criterion>
`IB65-1-AC2` -- both ExportReceipt schema copies require a non-empty facts.covered_account_ids. Base: FAIL.

<criterion id="IB65-G-145" cell_refs="IB-pr-343"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py" . IB65-G-145</invocation><expect>IB65-G-145 PASS</expect></criterion>
`IB65-G-145` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB65-1-AC1,IB65-1-AC2,IB65-G-145</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** Any S3 write, a deploy, or an edit outside the paths below is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/export/
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/receipt.py
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/tests/test_covered_account_ids.py
docs/contracts/investor-reporting/v1/ExportReceipt.schema.json
infra/aws/lambda/investor-reporting/_contracts/ExportReceipt.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~145/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-343.export-receipt-names-its-covered-accounts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 58 (round 65, workstream ~P), cell `IB-pr-343`.
<owned_cells>IB-pr-343</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB65-1-AC1, IB65-1-AC2, IB65-G-145. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~145/IRPT_BCKEND.TO-IB-pr-343.export-receipt-names-its-covered-accounts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB65-1-AC1,IB65-1-AC2,IB65-G-145` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base 31b26bff2d 2026-10-07 ~11:5xZ: build checks FAIL, guards PASS (p65_cells.py).
lane: the <paths> block IS the grant.
</preflight>

## AMENDMENT 1 (2026-10-07 ~12:1xZ, issuer 2.0.0_SA_COO~P2): the grant widens to all of `export/`; wire the retained path; update the three tests (rows W145-S1, W145-S2)

The worker's fix (e8005582a1) is right: both schemas require a non-empty `covered_account_ids`, `receipt.build` refuses an empty one, and
`_covered` fails closed (11 new tests pass). Two consequences sit outside the first grant, so the grant now covers
`infra/aws/lambda/investor-reporting/export/` (no other cell writes there this round; IB-pr-344 is this slot's next order):

1. **W145-S2 (ARMED): the retained path must carry its accounts.** `handler.finalize_export` and `finalize_on_read.finalize` call
   `receipt.build` without the accounts the submission holds, so after release a retained export could never finalize. The submission
   (`submit_async.py` / `dispatch.py`, which write `pending.json`) records the export's covered accounts in `pending.json`, and both
   finalizers pass them to `receipt.build` as `covered_account_ids`. Add a test that a retained submit -> finalize round trip yields a
   receipt naming its accounts, and that a pending.json without accounts is refused (never a receipt naming none).
2. **W145-S1: three existing tests mint an account-less receipt**, which PRD v0.30 now forbids. Update each to carry the account its
   scenario implies (do not weaken an assertion; keep each test's intent):
   - `test_export.py::test_the_receipt_names_the_object_and_is_derived_from_the_two_hashes`;
   - `test_download_signed_answer.py::test_the_receipt_names_the_live_route_and_no_other`;
   - `test_export_path_b_route.py::test_a_path_a_export_is_unchanged_and_never_calls_the_route_or_the_mint`.
3. AC1 is unchanged: the export suite has no failure beyond the six pypdf-only tests.

The release must not precede this wiring. Gate limb: none graded this modification (LIMB 6 does not fire on a modification; GATE (viii)
grades the unchanged placeholders NONE).

