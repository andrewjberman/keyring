# TO IRPT_ANLREQ.TO-AR-v11 -- the Analysis Request form offers the catalogue models and other ETFs, and files the I1 sequence with no "Request report" click

<to_id>IRPT_ANLREQ.TO-AR-v11</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~11</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>TICKET</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (portal DEV; a product file, landed by the CTO review route) | **Decomp cell:**
`AR-v-11` (`decompositions/IRPT_ANLREQ_DECOMP_R1.md`, hop 1) | **outcome_ref:** FWD-1 | **depends_on:** none (builds to I1; the backend
admitting `ticket_id` is `~Y2`'s AR-y-11)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~11`.
- **Portal worktree:** `C:/tmp/anlreq-v11-portal` (branch `wk-irpt_anlreq-v11`, from portal `origin/DEV`). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~11 -c user.email=0.9.0_WK_IRPT_ANLREQ~11@opal.agent commit -F <msgfile>`.
- **Workspace worktree:** `C:/tmp/anlreq-v` (branch `wk-irpt_anlreq-v`, the issuance commit). It holds this order and the checks.
  Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~11 <0.9.0_WK_IRPT_ANLREQ~11@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool.

### THE CELL

Hop 1 of FWD-1: an Opal person files ONE Analysis Request and the backend finishes the rest itself.

Today the Ticket Center form (`src/pages/TicketCenter/TicketCenter.tsx`, `AnalysisRequestParts.tsx`, `analysisRequest.ts`) files the
upload and then the ticket. A person must later click "Request report" (`AnalysisRequestParts.tsx:117-143`). Change it so that:

1. **Comparables.**
   - The form shows the Opal-model comparison choices as CHECKBOXES, read from the comparison catalogue the portal already uses for
     analysis. Find it: the Investor Reporting analysis tab picks comparables from IRPT's catalogue; reuse that client call or
     constant, and add no new endpoint.
   - It has an "Other ETFs" text field (comma- or space-separated tickers).
   - Comparables travel as `comparison_keys`: the checked models' catalogue keys plus the typed ETF keys. At most FIVE in total; the
     form refuses more, with a message.
2. **Filing sequence (I1, `decompositions/IRPT_ANLREQ_DECOMP_R1.md` Interfaces):**
   1. the upload door, as today;
   2. on NORMALIZED, the ticket CREATE, as today;
   3. immediately, `POST /api/scoped/investor-reporting/analysis` with the existing prospect body (`input_id`, `variant`,
      `comparison_keys`, ...) PLUS `ticket_id` (the new ticket's id).

   The form reports each step's outcome. If step 3 fails, the ticket stays filed and the failure is shown. The ticket is not deleted.
3. A NEW filing shows no "Request report" button. Leave the existing button for tickets filed before this change; do not delete it.
4. Use the portal's existing panel classes; add no new colours.

**Tests** go in the new file `src/pages/TicketCenter/__tests__/analysis-form-i1.test.tsx`, with EXACTLY these names:
- `offers the Opal model checkboxes from the catalogue`
- `takes other ETFs as typed keys`
- `files upload then ticket then analysis with ticket_id`
- `never shows a Request report button on a new filing`
- `sends at most five comparison keys`

The existing `analysis-request.test.tsx` and `commentary-package.test.tsx` must still pass. Where an assertion encodes the old click,
update it only to the new sequence, and say so in your report.

### ACCEPTANCE

<criterion id="AR11-v-AC1" cell_refs="AR-v-11"><invocation>python C:/tmp/anlreq-v/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py v11-form --portal C:/tmp/anlreq-v11-portal</invocation><expect>V11-FORM-OK</expect></criterion>
`AR11-v-AC1`: the five named tests exist and pass.

<criterion id="AR11-v-AC3" cell_refs="AR-v-11"><invocation>python C:/tmp/anlreq-v/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py portal-tsc --portal C:/tmp/anlreq-v11-portal</invocation><expect>PORTAL-TSC-OK</expect></criterion>
`AR11-v-AC3`: the portal typechecks.

<expected_criteria>AR11-v-AC1 AR11-v-AC3</expected_criteria>

## BOUNDS

- **Grant:**
  - in the portal worktree, `src/pages/TicketCenter/` (all files);
  - in the workspace worktree, your deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~11/` and
    this order's file (status flip only).
- READ only: `src/pages/InvestorReporting/**` and `src/api/endpoints/investor-reporting.ts`, because the IRPT client is imported, not
  edited.
- LOCAL: never push, never call the live API, and run dev servers on port 5174 only. No non-ASCII.

**AMENDMENT 1 (issuer, 2026-10-09 ~05:4xZ; rules row IRPT_ANLREQ-D2-W11-S2).** Replace the date gate
(`I1_FILING_SINCE = 2026-10-09T00:00:00Z`) with a marker the ticket stores.
- **The marker.** The I1 filing's ticket CREATE sends `source: "ticketcenter:i1"`. The service already accepts any `source` except
  the reserved `dashboard_form:` prefix (`ticket_center/lambda_function.py:1101`), so this needs no backend change.
- **The button.** "Request report" hides ONLY on a ticket whose `source` is `ticketcenter:i1`. Old-form tickets keep it, whatever
  their date. Remove the date constant.
- **The retry.** When step 3 (the `POST /analysis`) failed, the form shows "Retry analysis request". It re-sends step 3 with the SAME
  body and `ticket_id`, and never re-uploads or re-creates the ticket. The same retry appears on an `ticketcenter:i1` ticket that has
  no `report_ref`.
- **One new test**, named exactly `retries the analysis step without refiling`.
- The order stays HELD from landing until row W11-S1 (the portal client admitting `ticket_id`) is fixed by its owner.

**AMENDMENT 2 (issuer, 2026-10-09 ~05:5xZ; decomposition AMENDMENT 5 @2bd14c3fbc, `~Y2` msg 2607). Row W11-S1 is now THIS cell's.**
1. **Re-base first.** Portal DEV moved to `c34ff9c0` (AR-v-13 landed). Put your commits onto a branch from `origin/DEV`; both
   touch `AnalysisRequestParts.tsx`, so resolve any overlap by keeping BOTH behaviours.
2. **Client reader.** `src/pages/InvestorReporting/contracts/submission-request.ts` (`readSubmissionRequest`, `:13-38`) admits
   `ticket_id` ONLY beside `input_id`, matching `^TCK-\d{8}-[0-9a-f]{8}$`. Any other `ticket_id` shape, or `ticket_id` without
   `input_id`, is refused as today. Every other rule is unchanged.
3. **Wire type.** `src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts` is GENERATED. Regenerate it with its
   own generator (`src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`) from the schema at the workspace root
   (`docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json`, which carries `ticket_id` since `~Y2`'s
   AR-y-11 @3ad7526e06). Never hand-edit it; the header's source sha256 must match the schema. If the generator cannot reach
   the schema from the portal worktree, STOP and report.
4. **One more test** in your test file, named exactly `the client admits ticket_id only beside input_id`.
5. With the reader fixed, the form is no longer HELD on W11-S1. W11-S1 resolves on your drain.

<paths>
portal/src/pages/InvestorReporting/contracts/submission-request.ts
portal/src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/pages/TicketCenter/analysisRequest.ts
portal/src/pages/TicketCenter/__tests__/analysis-form-i1.test.tsx
portal/src/pages/TicketCenter/__tests__/analysis-request.test.tsx
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> (round 1, workstream ~V2 TICKET), cell `AR-v-11`.
<owned_cells>AR-v-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR11-v-AC1 AR11-v-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~11/IRPT_ANLREQ.TO-AR-v11.form-files-i1-sequence.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AR11-v-AC1 AR11-v-AC3` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the portal and workspace commits, any old assertion you updated, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE (portal; the user's own session). comp-adversary: DECLARED-NOT-APPLICABLE.
lane: product file; lands on portal DEV by the CTO review route.
</preflight>

Source: `~Y2` msg 2486; IRPT_ANLREQ decomposition R1 @52e8fa4fe7 (hop 1, I1); PRD @97ef783e9a.

# pipeline-override: round 1's issuance is split by workstream under C-ABSORB (decomposition @52e8fa4fe7: "each lane issues ONLY the cells named for it, into its own scope"); this is ~V2's issuance of its three cells.
