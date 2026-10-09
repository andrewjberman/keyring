# TO IRPT_ANLREQ.TO-AR-v13 -- the ticket page lists the package's files and opens each through IRPT's owned reader (I6)

<to_id>IRPT_ANLREQ.TO-AR-v13</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~13</issued_to>
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
`AR-v-13` (hop 9, I6) | **outcome_ref:** FWD-1 | **depends_on:** none to build

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~13`.
- **Portal worktree:** `C:/tmp/anlreq-v13-portal` (branch `wk-irpt_anlreq-v13`, from portal `origin/DEV`). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~13 -c user.email=0.9.0_WK_IRPT_ANLREQ~13@opal.agent commit -F <msgfile>`.
- **Workspace worktree:** `C:/tmp/anlreq-v` (shared). Commit ONLY your own paths with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~13 <0.9.0_WK_IRPT_ANLREQ~13@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool.

### THE CELL

Today an analysis ticket with a `package` shows its four refs as TEXT (`AnalysisDraftAndPackage` in
`src/pages/TicketCenter/AnalysisRequestParts.tsx`, portal 44c31b8e). I6 says each ref opens "through IRPT's signed-link reader
(`ops/owned_report.py:154`) under the VIEWER's own scope".

1. **Find, from source, how the portal reaches IRPT's owned reads.** Look in `src/api/endpoints/investor-reporting.ts` and the
   InvestorReporting pages. For example, `GET /api/scoped/investor-reporting/analysis/requests/{requestId}` and its `/pdf`, which
   returns a `download_route.url`. Use only existing client calls; add no endpoint.
2. **The Report package block** lists four files: Report, Branded PDF, Commentary, Original file.
   - Each file that HAS an existing owned reader opens through it in the viewer's session. The report opens the owned read; the PDF
     opens the signed `download_route.url` (open it in a new tab, and never store it).
   - A file whose ref has NO existing reader stays as text, labelled "(no reader yet)". Never invent a URL from a ref.
   - Name in your report which refs have a reader and which do not.
3. No call is made for a ticket without a package. Use the existing panel classes and add no colours.

**Tests** go in the new file `src/pages/TicketCenter/__tests__/package-open.test.tsx`, with EXACTLY these names:
- `lists the four package files on the ticket`
- `opens the report and the PDF through the owned reader`
- `names a file with no reader instead of linking it`
- `makes no call for a ticket without a package`

`commentary-package.test.tsx` must still pass. Update it only where it asserted text-only refs that now link, and say so.

### ACCEPTANCE

<criterion id="AR13-v-AC1" cell_refs="AR-v-13"><invocation>python C:/tmp/anlreq-v/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py v13-open --portal C:/tmp/anlreq-v13-portal</invocation><expect>V13-OPEN-OK</expect></criterion>
`AR13-v-AC1`: the four named tests exist and pass.

<criterion id="AR13-v-AC3" cell_refs="AR-v-13"><invocation>python C:/tmp/anlreq-v/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py portal-tsc --portal C:/tmp/anlreq-v13-portal</invocation><expect>PORTAL-TSC-OK</expect></criterion>
`AR13-v-AC3`: the portal typechecks.

<expected_criteria>AR13-v-AC1 AR13-v-AC3</expected_criteria>

## BOUNDS

- **Grant:** in the portal worktree, `src/pages/TicketCenter/AnalysisRequestParts.tsx` and the two test files below; in the workspace
  worktree, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~13/` and this order's file (status flip only).
- READ only: `src/api/endpoints/investor-reporting.ts` and `src/pages/InvestorReporting/**`.
- LOCAL: never push and never call the live API. No non-ASCII.

<paths>
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/pages/TicketCenter/__tests__/package-open.test.tsx
portal/src/pages/TicketCenter/__tests__/commentary-package.test.tsx
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> (round 1, workstream ~V2 TICKET), cell `AR-v-13`.
<owned_cells>AR-v-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR13-v-AC1 AR13-v-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~13/IRPT_ANLREQ.TO-AR-v13.ticket-page-opens-package.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AR13-v-AC1 AR13-v-AC3` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, which refs have a reader and which do not, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE (the viewer's own session). comp-adversary: DECLARED-NOT-APPLICABLE.
lane: product file; lands on portal DEV by the CTO review route.
</preflight>

Source: `~Y2` msg 2486; decomposition R1 @52e8fa4fe7 (hop 9, I6); PRD @97ef783e9a.

# pipeline-override: round 1's issuance is split by workstream under C-ABSORB; this is ~V2's issuance of its three cells.
