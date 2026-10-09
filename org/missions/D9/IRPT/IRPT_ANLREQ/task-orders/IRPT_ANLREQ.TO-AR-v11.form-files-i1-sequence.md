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

<paths>
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
