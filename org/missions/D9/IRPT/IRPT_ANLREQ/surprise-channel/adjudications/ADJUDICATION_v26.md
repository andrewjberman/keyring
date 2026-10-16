# IRPT_ANLREQ: CVO adjudication, workstream T, FWD-5 (rounds 45-63): another firm is refused the ticket and the package -- graded adversarially at L9

<sweep_watermark>2026-10-16T23:20Z</sweep_watermark>

**Basis.** L8 compile, L9 grade and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T23:20Z, on msg 9971. The compile graded is `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_FWD5_T_L8_COMPILE_20261016.md` @de3da68cff, and the CTO asked for this grade in msg 9955.

**Orders.** 22 map and test orders plus the two live-sitting orders, all complete; no order carries a judgment criterion. The outcome graded is PRD FWD-5 (`prd/IRPT_ANLREQ_PRD.md:65-68`), clause by clause.

**What this seat ran and read.**
- **Records read raw:** both sittings' run and control records.
- **Re-runs:** the driver's `--selftest` (FWD5-SELFTEST-OK checks=50) and the three acceptance tests for the S134 items.
- **Live reads:** identity reads only, all read-only.
- **Not re-checkable:** no response body is recorded (by design: "a row never holds a body"). Where a verdict rests on body length, it is inferred from the length and the code, not read from a body.

**(1) The second sitting, call by call (firm B = cottonwood, allowedFirmIds [cottonwood]; target = the one synthetic 49financial ticket TCK-20261015-944c84f8 and request REQ-d47252fe...).**

| route | firm B | control (opal-capital, allowedFirmIds [49financial]) | the control passed the fence? |
|---|---|---|---|
| ticket-read | 403, 130 B | 200, 1,550 B | yes, ALLOWED |
| ticket-list | 200, 620 B, no ticket id | 200, 42,778 B, carries the id | yes, ALLOWED |
| form-as-filled | 403, 146 B | 404, 63 B | yes, inferred: 63 B is exactly the "carries no attachment" body (`lambda_function.py:2124/2127`); a fence 404 is 51 B. No form file exists. |
| original-upload | FIRM_BINDING, 430 B | 200, 1,961 B, a served body | yes, served |
| opal-report (sections) | FIRM_BINDING, 410 B | 200, 60,114 B, a served body | yes, served |
| report-pdf | FIRM_BINDING, 420 B | NOT_FOUND, 460 B | yes, past the fence (served.py step 2 precedes the owner read). No PDF exists. |
| commentary-pdf | FIRM_BINDING, 442 B | NOT_FOUND, 482 B | as report-pdf. No PDF exists. |

- **The FIRM_BINDING envelopes** equal `served.refuse()`'s lengths, computed here: 430/410/420/442.
- **The positive control works:** on 2 ticket routes and 2 report-side routes it reached a served answer. On the other 3 routes it passed the fence, but no artifact exists behind it.

**(2) The denominator.**
- **The four report-side routes are NOT all the reach.**
- **Report side:** `docs/contracts/investor-reporting/v1/routes.json` declares 25 routes (23 DECLARED, 2 ROUTED_ELSEWHERE). Subtracting the 4 driven leaves 21. Of those, these read the same request, job, report or package and were not driven:
  - `GET analysis/requests/{requestId}` (the request itself)
  - `GET analysis/requests` (history)
  - `GET status/{jobId}` (the job, incl. a hop failure)
  - `GET status`
  - `GET narrative/{reportId}`
  - `GET export/{exportId}` and `/download`
- **Ticket side:** `infra/aws/terraform/ticket-center/main.tf` declares 14 routes. The read not driven is `GET /api/scoped/tickets/metrics`. The writes not sent are claim, complete, report, package, commentary-draft, commentary-sent and meeting; meeting is offline-tested only.
- **Shape not driven:** a request with NO `selected_tenant`. Firm B's verified firm then anchors the bucket. That is a design statement, not an exercise.
- **The common fence is a statement too:** every DECLARED report-side handler imports `_authz/served.py`, so the fence is common by code. That is a statement, not an exercise.

**(3) Sitting 1 (21:13Z) leaked nothing.**
- Firm B's four report-side 200s were 434/414/424/446 B. Those are exactly `served.refuse()`'s CONTRACT_VERSION envelope lengths (each 4 B over FIRM_BINDING), and they equal the control's own four.
- That fits a refusal for both identities and no data. It is inferred from bytes; no body was recorded.
- Its ticket routes match sitting 2's: 403, a list without the id, 403.

**(4) Both principals are gone, read live.** `fwd5-cottonwood-r60` and `fwd5-control-r60@opal.invalid` (the same pair in both sittings):
- email-index count 0 each;
- a consistent scan of `opal-users-v2` (86 rows) finds 0 rows with an email beginning `fwd5-`.

**(5) "Admits that remain by design".** No admit lacks a ruling, but the compile mis-describes items 1 to 3:
- **Items 1 to 3 were ruled FIXES, not admits:** ADDENDUM 7, msg 8834: the recipient derived server-side, intake scoped to a firm list, a missing allowedFirmIds meaning no firm.
- **The fixes are in code:** commits 8398ba291b, 8957fed16b and 028ee030b9.
- **Their acceptance tests are green at HEAD:** `r46_checks.py tests` gives passed=7 on each of the notice-recipient, intake-list and profile-scope files. `red` mode now FAILS, as it should after the fix.
- **Deployment is RECORD only:** the fixes are live per ~V2's release (msg 9734); not measured here.
- **The OPAL_GLOBAL admits are ruled:** G1 and G2 by ADDENDUM 7 item 4; G4 to G11 by ADDENDUM 8 (msg 9081). G3 (the `scope_all_firms` marker) is "ruled with item 3", which is the weakest citation: item 3 rules the absence, not the marker.

**L9 -- FWD-5 clause by clause.**

1. **FWD-5 DONE-WHEN-1, "a sign-in at another firm tries the ticket": PASS.** Read, list and form were tried, and the control was allowed on read and list.
2. **FWD-5 DONE-WHEN-2, "and each package file": FAIL** (unproven, not refuted).
   - **No package was tried:** the target ticket carries NO package (no `report_ref`, no PDF).
   - **The packaged ticket was not used:** TCK-20261014-2965a5e0 has a Report and a Commentary attached by the packager, but firm B never tried it.
   - **What was shown:** the fence on the two PDF routes, against files that do not exist.
3. **FWD-5 DONE-WHEN-3, "is refused every time": PASS.** 7 of 7 refused, 0 leaks. Sitting 1 returned only contract-version envelopes.
4. **FWD-5 DONE-WHEN-4, "repeatable on demand": PASS.** The driver, the scoped mint helper and the checks are committed. The selftest was re-run here, and two sittings ran.
5. **FWD-5 ACCEPT-1, "refused the ticket": PASS.**
6. **FWD-5 ACCEPT-2, "and every file in its package; a statement does not count": FAIL.**
   - **Not exercised:** the PDFs, plus five read routes on the same request or job (request read, history, status/{jobId}, narrative, export).
   - **Rests on code alone:** the common fence and the no-selection bucket anchor.

**FWD-5 overall: FAIL, unproven, not refuted.** No leak was found. The CTO accepted the sitting (msg 9955); this grade differs on the package half and the denominator.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S4",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T23:20:00Z",
  "one_line": "FWD-5 (workstream T) L9: FAIL overall, unproven not refuted. PASS: firm B refused the ticket 3 of 3 against a working control, 7 of 7 refused with 0 leaks, sitting 1 returned only CONTRACT_VERSION envelopes (bytes match), both principals ABSENT live, repeatable (selftest re-run). FAIL: the target ticket has no package, so no package file was tried against an existing file; five read routes on the same request/job and the no-selected_tenant shape were not driven. S134 items 1-3 are ruled fixes (green at HEAD), not by-design admits; OPAL_GLOBAL G1-G11 ruled.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-S159", "IRPT_ANLREQ-D2-S134"],
  "spec_asserts": "PRD FWD-5 (prd/IRPT_ANLREQ_PRD.md:65-68): DONE WHEN a sign-in at another firm tries the ticket and each package file and is refused every time, repeatable on demand; ACCEPT someone signed in for a different firm is refused the ticket and every file in its package; a statement that it is refused does not count.",
  "world_is": "Sitting 2: firm B refused 7 of 7 (ticket-read 403, list without id, form 403, four report-side FIRM_BINDING 430/410/420/442 B); control ALLOWED on read and list, served bodies on original (1,961 B) and sections (60,114 B), past the fence on the two PDF routes (NOT_FOUND) and on form (63 B no-attachment branch). The target ticket TCK-20261015-944c84f8 has no package; the packaged TCK-20261014-2965a5e0 was not tried. Route denominator: 25 report-side + 14 ticket routes; not driven include analysis/requests/{id}, analysis/requests, status/{jobId}, status, narrative/{id}, export/{id}(/download), tickets/metrics, the writes; no request without selected_tenant. Sitting 1: firm B and control both 434/414/424/446 B = CONTRACT_VERSION envelopes. Principals: email-index 0 and 0; consistent scan 86 rows, 0 fwd5-. S134 items 1-3: tests passed=7 x3 at HEAD.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd5_s2/fwd5_run_report.json, fwd5_control_report.json, SITTING_OUTPUT.txt",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd5/fwd5_run_report.json, fwd5_control_report.json, SITTING_OUTPUT.txt",
    "infra/aws/lambda/investor-reporting/_authz/served.py handle() steps 1-3 (:1204-1272); served.refuse() envelope lengths computed: FIRM_BINDING 430/410/420/442, CONTRACT_VERSION 434/414/424/446",
    "infra/aws/lambda/ticket_center/lambda_function.py attachment_open_ticket (:2105-2138): 404 bodies 51 B (not found) vs 63 B (no attachment)",
    "docs/contracts/investor-reporting/v1/routes.json (25 routes); infra/aws/terraform/ticket-center/main.tf:474-503 (14 routes)",
    "python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py --selftest -> FWD5-SELFTEST-OK checks=50",
    "python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 3|2|4 test_cross_firm_notice_recipient.py|test_cross_firm_intake_list.py|test_cross_firm_profile_scope.py -> R46-TESTS-OK passed=7 each",
    "read-only: opal-users-v2 email-index count 0 for both fwd5-*-r60@opal.invalid; consistent scan 86 rows, 0 with email prefix fwd5-",
    "org/mcp/inbox/2.0.0_SA_COO/~T2/read/20261016T010339Z_1.0.0_SA_CTO_DELL2_Row_S134__four_cross-firm_admissions_in_.md (Msg-ID 8834); .../20261016T050848Z_1.0.0_SA_CTO_DELL2_Ruling_on_msg_9078__OPAL_GLOBAL_sites_G4.md (Msg-ID 9081); org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_GLOBAL_ADMISSIONS_REGISTER.md"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owed for FWD-5 to PASS (owner 2.0.0_SA_COO~T2, ruling 1.0.0_SA_CTO): (a) firm B against a PACKAGED ticket whose files exist (e.g. TCK-20261014-2965a5e0's report and commentary PDFs), with the control served each file; (b) either drive the five unexercised read routes on the same request/job (analysis/requests/{id}, analysis/requests, status/{jobId}, narrative/{id}, export/{id}) or a CTO ruling that the common served.py fence makes them one case; (c) one call with no selected_tenant. Not owed: no leak was found anywhere. Compile correction: section 2 should list S134 items 1-3 as FIXED (ADDENDUM 7, green at HEAD), not as admits that remain; G3's ruling citation is by implication."
 }
]
```
