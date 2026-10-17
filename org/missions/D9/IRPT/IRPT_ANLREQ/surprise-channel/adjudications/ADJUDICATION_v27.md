# IRPT_ANLREQ: CVO adjudication, workstream T, FWD-5 ADDENDUM 1 (third live sitting): re-graded against the v26 gaps

<sweep_watermark>2026-10-17T00:52Z</sweep_watermark>

**Basis.** L8 compile, L9 grade and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-17T00:52Z, on msg 10094. The addendum graded is `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_FWD5_T_L8_COMPILE_ADDENDUM_1_20261017.md` @cdfc85ba12. The order is `IRPT_ANLREQ.TO-RUN-FWD5.live-cross-firm-s3-ib2` (complete), instance @a131218c7e.

**Criteria re-run here:**
- AR75-tz-AC1: R56-FENCE-FAIL ("packaged target: the control did not serve ['original-upload', 'report-pdf', 'commentary-pdf']").
- AR75-tz-AC2: R56-ABSENT-OK.
- AR75-tz-AC3: R56-REPORT-OK (13 REFUSED, 0 LEAK on each target).

**What was read.** The four raw reports under `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd5_s3/{packaged,synthetic}/`, call by call. No body is recorded, so sizes are compared with `served.refuse()` lengths computed here. Read-only identity reads. No client value below.

**(1) Firm B (cottonwood, allowedFirmIds [cottonwood]): refused 26 of 26, identical on both targets.**
- **Ticket routes:** ticket-read 403 (130 B); ticket-list 200 (620 B) without the ticket id; form-as-filled 403 (146 B).
- **The nine report-side routes:** original-upload, opal-report, report-pdf, commentary-pdf, request-read, request-history, job-status, narrative and export-receipt each answered FIRM_BINDING, at 430/410/420/442/422/428/400/412/408 B. Seven of those are recomputed here from `served.refuse()`; narrative and export-receipt are the compile's.
- **The no-selection call:** request-read-no-selection answered NOT_AUTHORIZED (467 B).

**(2) The control (opal-capital, allowedFirmIds [49financial]), route by route.**
- **SHOWN against a served control (synthetic target only):** ticket-read 1,550 B, ticket-list 42,778 B with the id, original-upload 1,957 B, opal-report 60,114 B, request-read 539 B and job-status 414 B. On the packaged target only ticket-read (2,239 B) and ticket-list are shown.
- **PAST the fence, but not served:**
  - report-pdf, commentary-pdf and export-receipt: NOT_FOUND on the synthetic target.
  - form-as-filled: 404 at 63 B on both targets, the no-attachment branch.
  - **On the PACKAGED target, all six report routes:** the control read NOT_AUTHORIZED at 475/455/465/487/467/445 B.
- **What the packaged NOT_AUTHORIZED is:** each length is the plain `refuse()` NOT_AUTHORIZED plus 43 B, the same +43 the owner-read NOT_FOUND carries (460 vs 417). That reads as the owner check AFTER the fence (INFERRED from bytes). So the route does not refuse everyone at the fence; it refuses every non-owner at the owner read.
- **The consequence:** firm B's FIRM_BINDING on the packaged files is the fence's own code. But no entitled principal was ever served those files, so on the packaged leg the refusal is **ABSENT, not EXERCISED-AGAINST**. Even with no fence, firm B would meet the owner gate.
- **The control that would prove it:** the OWNER, or an identity the owner read admits, for 49financial, served each packaged file (original, report, PDFs) in the same window as firm B is refused.
- **NO working control (ABSENT):**
  - request-history: the control read UNEXPECTED on both targets;
  - narrative: the control read FIRM_BINDING, with a stand-in id;
  - the no-selection call: the control read UNEXPECTED. Firm B's 467 B is the owner-read NOT_AUTHORIZED, so it shows the bucket anchor under firm B's own firm, not a fence.
- **A checker leniency:** `r56_checks.py fence` counts request-history and the no-selection call as "past" on UNEXPECTED. An error answer is not evidence the fence was passed.

**(3) The v26 gaps.**
- **The five read routes:** all driven; three shown against a working control (request-read, job-status, and on the synthetic target only), one past the fence (export-receipt), two with no working control (request-history, narrative).
- **The no-selection call:** driven, but with no working control.
- **The METRICS route** (`GET /api/scoped/tickets/metrics`): NOT driven; it is not in the driver's route list.
- **The write routes** (claim, complete, report, package, commentary-draft, commentary-sent, meeting): NOT driven; meeting is offline-tested only.

**(4) Leaks: 0, inferred from sizes.** Every firm-B report-side size equals the FIRM_BINDING envelope. The ticket sizes equal sittings 1 and 2. The 620 B ticket-list body is unrecorded; only its lack of the ticket id is checked.

**(5) Both principals are gone, read live:** email-index count 0 for `fwd5-cottonwood-r60` and `fwd5-control-r60@opal.invalid`; a consistent scan of 86 rows finds 0 `fwd5-` rows.

**L9 -- FWD-5 by clause.**
1. **FWD-5 DONE-WHEN-1, "tries the ticket": PASS.**
2. **FWD-5 DONE-WHEN-2, "and each package file": PASS as tried.** Both targets were tried, with the packaged files existing.
3. **FWD-5 DONE-WHEN-3, "refused every time": PASS.** 26 of 26, 0 leaks.
4. **FWD-5 DONE-WHEN-4, "repeatable": PASS.** Three sittings ran.
5. **FWD-5 ACCEPT-1, "refused the ticket": PASS.**
6. **FWD-5 ACCEPT-2, "every file in its package; a statement does not count": FAIL.**
   - On the packaged target, no file route had a served control.
   - request-history, narrative and the no-selection call have no working control.
   - Metrics and the writes are undriven.

**FWD-5 overall: FAIL, unproven, not refuted.** No leak was found in three sittings.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S5",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T00:52:00Z",
  "one_line": "FWD-5 addendum 1 (sitting 3) L9: FAIL overall, unproven not refuted. Firm B refused 26 of 26 with 0 leaks (FIRM_BINDING sizes) and both principals ABSENT live. On the PACKAGED target the staff control read the owner-read NOT_AUTHORIZED (+43 B over refuse()) on every file route, so no file was served to an entitled reader: that leg is ABSENT, not EXERCISED-AGAINST. request-history, narrative and the no-selection call have no working control; METRICS and the writes were not driven. ACCEPT-2 FAIL.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-C-S4"],
  "spec_asserts": "PRD FWD-5 (prd/IRPT_ANLREQ_PRD.md:65-68): refused the ticket and every file in its package; a statement that it is refused does not count. CVO grading rule: a refusal without a working control on the same route is ABSENT, not EXERCISED-AGAINST.",
  "world_is": "Sitting 3: firm B 13 REFUSED x2 (ticket 403/list without id/form 403; nine report routes FIRM_BINDING; no-selection NOT_AUTHORIZED 467 B). Control synthetic: served on ticket-read, ticket-list, original-upload, opal-report, request-read, job-status; NOT_FOUND on the PDFs and export-receipt; UNEXPECTED on request-history and no-selection; FIRM_BINDING on narrative. Control packaged: ALLOWED only on ticket-read and ticket-list; NOT_AUTHORIZED at refuse()+43 B on six report routes. Metrics not in the route list. Principals: index 0 and 0, consistent scan 86 rows 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd5_s3/packaged/fwd5_run_report.json, fwd5_control_report.json; .../synthetic/fwd5_run_report.json, fwd5_control_report.json",
    "python -I org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R56_CHECKS/r56_checks.py via the order's invocations: AR75-tz-AC1 R56-FENCE-FAIL, AR75-tz-AC2 R56-ABSENT-OK, AR75-tz-AC3 R56-REPORT-OK",
    "infra/aws/lambda/investor-reporting/_authz/served.py refuse() lengths computed here: NOT_AUTHORIZED 432/412/422/444/424/402 for original/report/pdf/commentary-pdf/request-read/status-job; FIRM_BINDING 430/410/420/442/422/428/400; UNEXPECTED request-read 420",
    "read-only: opal-users-v2 email-index count 0 for fwd5-cottonwood-r60 and fwd5-control-r60@opal.invalid; consistent scan 86 rows, 0 fwd5-"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owed for FWD-5 to PASS: (a) a working control on the packaged files: the owner of a packaged 49financial request (or an identity its owner read admits) SERVED the original, the report and both PDFs in the same sitting firm B is refused (the window-5 owner design at the CRO, owner 2.0.0_SA_COO~Y2/~T2); (b) a working control on request-history, narrative (a real report id) and the no-selection call (the UNEXPECTED answers to the irpt-status owner); (c) the METRICS route driven, and the write routes driven or ruled out of FWD-5 by the CTO. The r56 fence check should not count UNEXPECTED as past the fence."
 }
]
```
