# TO TCKT_VNEXT.TO-TV-p1 -- the Ticket Center page files an Analysis Request with its file and opens the finished report from the ticket

<to_id>TCKT_VNEXT.TO-TV-p1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~2</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>thread</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (a portal branch; nothing lands on DEV from this order) | **Decomp cell:** `TV-p-1`
(`decompositions/TCKT_VNEXT_DECOMP.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (built against the contract below)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~2`. You have TWO worktrees:
- **Portal:** `C:/tmp/tckt-r1-2-portal` (the `portal` repository, branch `wk-tckt_vnext-1-2-portal`, cut from portal `DEV`). All
  product code and tests go here. Commit there with plain `git -C C:/tmp/tckt-r1-2-portal commit -F <msgfile>` (message file written with
  the Write tool), author `0.9.0_WK_TCKT_VNEXT~2 <0.9.0_WK_TCKT_VNEXT~2@opal.agent>`. Never push.
- **Workspace:** `C:/tmp/tckt-r1-2` (branch `wk-tckt_vnext-1-2`, cut from CLOUD). Only your proof-of-spec instance, this order's status
  flip and any surprise row go here, committed with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~2 <0.9.0_WK_TCKT_VNEXT~2@opal.agent>" -F <msgfile> -- <paths>`.

Run tests with `bun test <file>` from the portal worktree root (`bun` is on PATH).

### THE CELL

`TV-p-1`: the Ticket Center page (`src/pages/TicketCenter/TicketCenter.tsx`, internal users, today: a board, a create form with four
plain types, one-touch claim, complete, metrics) gains the Analysis Request journey. The ticket service is being changed in parallel to
exactly this contract; build against it (mock it in tests):

- **Create** `POST /api/scoped/tickets` with `{ticket_type: "analysis_request", title, answers, attachment: {upload_id, input_id}}`.
  `answers`: `advisor` (text, req), `firm` (firm id, req), `household` (text, req), `report_type` (`Overview` | `Comparison` |
  `Multi-Comp`, req), `comparison_model` (text, required unless `Overview`), `advisory_fee` (number, optional, show the default),
  `needed_by` (date, optional), `add_commentary` (boolean, default false). The ticket returned carries `answers`, `attachment` and,
  later, `report_ref`.
- **Report reference** `POST /api/scoped/tickets/{ticketId}/report` with `{request_id, revision?}` (assignee only, ticket
  `in_progress`). The ticket then carries `report_ref {request_id, revision, recorded_by, recorded_at}`.
- **Self-claim:** the filer may claim and complete their own ticket (no UI block for it).

**The journey to build:**
1. **File.** In the create form, choosing "Analysis Request" shows its questions and a file input. On submit, the page first sends the
   file through the Analysis upload door: `uploadAnalysisInput(req, selectedTenant)` on the investor-reporting client
   (`src/api/endpoints/investor-reporting.ts:823`, live impl :1100; body shape `src/pages/InvestorReporting/contracts/wire/AnalysisUploadRequest.ts`,
   result `.../AnalysisUploadResult.ts`), with `selectedTenant` = `answers.firm`. Only when the result's `state` is `NORMALIZED` does it
   call create with `attachment = {upload_id, input_id}` from that result. On `NEEDS_CORRECTION` (or `RESOLVING`) it files NOTHING and
   shows the result's findings to the person filing.
2. **Generate.** On a ticket of type `analysis_request` that is `in_progress` and has no `report_ref`, its assignee sees "Request
   report". It calls `submitAnalysisRequest(body, scope)` (`investor-reporting.ts:1325`; body shape
   `src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts`) with `input_id` = the ticket's `attachment.input_id`,
   `variant` from `answers.report_type` (Overview -> `overview`, Comparison -> `comparison`, Multi-Comp -> `multicomp`), scope's tenant
   = `answers.firm`. The response carries `data.identity.request_id` (+ `revision`); the page then calls the report-reference route
   with them.
3. **Open.** A ticket with `report_ref` shows "Open report", which opens the IRPT report for `report_ref.request_id` through the
   investor-reporting client's `analysis-request-read` operation (`GET .../analysis/requests/{requestId}`, route table :214) -- the
   reader's entitlement is IRPT's, never a copy.

Add the ticket API calls (create with answers/attachment, report reference) and the new fields to `src/api/endpoints/tickets.ts`
(:13-102). Do NOT edit `investor-reporting.ts` or anything under `src/pages/InvestorReporting/` -- they are IRPT's; import only.
Follow the portal's colour law in `portal/CLAUDE.md` (light canvas, white hairline panels, navy ink) for any new element.

**Tests** in the new file `src/pages/TicketCenter/__tests__/analysis-request.test.tsx` (`bun:test`; mock the two API modules), with
EXACTLY these test names (the checks look them up by name; a missing name fails):
- `files only on NORMALIZED with answers and input_id` -- door mocked NORMALIZED -> create called once with the answers and the
  door's `upload_id`/`input_id`.
- `NEEDS_CORRECTION shows findings and files nothing` -- door mocked NEEDS_CORRECTION with a finding -> create never called, the
  finding text rendered.
- `requests the report with the ticket input_id and writes request_id back` -- submit called with the ticket's `input_id`, then the
  report route called with the returned `request_id`.
- `opens the report from the ticket` -- a ticket with `report_ref` renders an "Open report" control bound to that `request_id`.

### ACCEPTANCE

<criterion id="TV1-p1-AC1" cell_refs="TV-p-1"><invocation>python C:/tmp/tckt-r1-2/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_CHECKS/r1_checks.py p1-file --portal C:/tmp/tckt-r1-2-portal</invocation><expect>TV1-P1-FILE-OK</expect></criterion>
`TV1-p1-AC1` -- the two filing tests named above exist and pass.

<criterion id="TV1-p1-AC2" cell_refs="TV-p-1"><invocation>python C:/tmp/tckt-r1-2/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_CHECKS/r1_checks.py p1-report --portal C:/tmp/tckt-r1-2-portal</invocation><expect>TV1-P1-REPORT-OK</expect></criterion>
`TV1-p1-AC2` -- the two report tests named above exist and pass.

<expected_criteria>TV1-p1-AC1 TV1-p1-AC2</expected_criteria>

Dry-run at the base (portal DEV 339851c7): both `FAIL absent: .../analysis-request.test.tsx`, as expected. `tsc -b` and the portal's
full test run are the issuer's drain checks; do not break them.

## BOUNDS

- **Grant.** The `<paths>` block below (portal paths are relative to `C:/tmp/tckt-r1-2-portal`, workspace paths to `C:/tmp/tckt-r1-2`),
  plus your deliverables folder `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~2/` and this order's file (status flip only).
- **LOCAL.** Never push either repository, never run the dev server against a live API, never call AWS or IRPT, never edit the ticket
  service. The portal landing on DEV is the issuer's, by the portal review route.
- No new notification or alert.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `TCKT_VNEXT-D2-W2-S<k>`, next unused, appended to the channel below), and do not weaken a test to pass.

<paths>
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/index.ts
portal/src/pages/TicketCenter/__tests__/analysis-request.test.tsx
portal/src/api/endpoints/tickets.ts
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (the `portal/` prefix maps to your portal worktree root). New component files you add under
`portal/src/pages/TicketCenter/` are inside the grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP.md</decomp_doc> (round 1), cell `TV-p-1`.
<owned_cells>TV-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TV1-p1-AC1 TV1-p1-AC2. Instance at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~2/TCKT_VNEXT.TO-TV-p1.portal-analysis-request-form.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TV1-p1-AC1 TV1-p1-AC2` BEFORE the flip to `complete`.
</proof_of_spec>

**REPORT (your final message, once):** each check line verbatim, the portal commits and the workspace commits on your branches, any
surprise row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- a portal branch; no IAM is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches C-FENCE (FWD-2).
lane: the <paths> block IS the grant; portal product files land on DEV only by the portal review route, the issuer's act.
</preflight>

Source: PRD v0.2 @99eb4053c2 (section 2 thread, C-ONE-DOOR, C-HANDOFF); decomposition round 1 cell TV-p-1 and its API contract;
X-2 answer msg 929 (request_id with selected_tenant = the owner firm; report read at GET .../analysis/requests/{requestId}).
