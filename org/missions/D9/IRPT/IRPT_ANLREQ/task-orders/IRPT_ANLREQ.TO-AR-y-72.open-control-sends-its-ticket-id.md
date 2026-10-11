# TO IRPT_ANLREQ.TO-AR-y-72 -- the Ticket Center's Open control sends the ticket's own id with the report read and shows a binding refusal

<to_id>IRPT_ANLREQ.TO-AR-y-72</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, deployed or called live)
**Decomp cell:** `AR-y-72` (`decompositions/IRPT_ANLREQ_DECOMP_R7_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-71` merged (its interface), and round 6's `AR-y-61` terminal in this slot (the same portal files)

**NOT SPAWNED AT ISSUANCE.** The issuer spawns this order when both predecessors are terminal, and at that time states in an
amendment: the portal branch and its base, and the selector's name and the refusal's code as `AR-y-71` committed them.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`; the branch and its base are named in this order's spawn amendment (read it;
  if there is none, STOP: the order was spawned too early). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`. Never push.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The workspace worktree shows
  ` M portal`: never commit it. Never run `bun install`.

### THE CELL (`AR-y-72`, inlined)

*The Ticket Center's Open control sends the ticket's own id with the report read, and shows a binding refusal as a refusal (never the
request record, never an empty report).*

Why: a ticket's creator will be able to record which request's report belongs to the ticket. That word is unchecked, so a ticket
could show a report that is not its own. The service's report read now takes an optional `ticket_id` and refuses when the request
was filed under a different ticket (cell `AR-y-71`; the selector's exact name, its carrier and the refusal's code are in this order's
spawn amendment and in the contract document that amendment cites -- read them there, not from memory).

1. The Open control for a ticket's Report (`src/pages/TicketCenter/AnalysisRequestParts.tsx`, the open path that calls the Investor
   Reporting client's owned-report read; and `openReport` in `analysisRequest.ts` if the older "Open report" button uses the same
   read) passes the TICKET's id as that selector on every report read it makes for a ticket. Read how the client method takes its
   arguments (`src/api/endpoints/investor-reporting.ts`) and add the selector in the client's existing style for an optional selector;
   a call that is not made from a ticket sends none.
2. The refusal: when the read answers the binding refusal, the opened panel says so in one plain sentence of your wording that names
   no ticket id and no request id other than the one the page already shows, and renders NO report section and NOT the request record.
   Use the page's existing refusal or error presentation (the one the open path already uses for a refused read); do not style a new one.
3. PDF and Original open controls: read whether their reads are the same service read or different routes. If they are different
   routes, they are NOT this cell's: say in your report which routes they call, and change nothing there.
4. **One new test file**, `src/pages/TicketCenter/__tests__/package-open-ticket-binding.test.tsx`, in the style of the existing
   `package-open.test.tsx` and `package-report-reader.test.tsx` (typed fakes; no `any`, no `// @ts-` comment), with tests named exactly:
   - `the Open control sends the ticket's own id with the report read`
   - `a binding refusal is shown as a refusal and no report is rendered`
   - `the request record is never shown in place of a refused report`
   Existing tests keep their names; change only what the new argument forces.
5. Do not restyle anything. Do not touch the form, the filing sequence or any file outside the grant.

---

**SPAWN AMENDMENT (AMENDMENT 1, issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~14:0xZ): both predecessors are terminal; the facts this face
said it would give.** Gate limb that graded this amendment: read from this commit's own output.

- **Portal branch:** `wk-IRPT_ANLREQ-51-portal-r7`, cut from portal DEV `cece88f603` (round 6's form change is ON DEV at that commit).
- **The interface, as cell `AR-y-71` committed it** (merged @31d02ad19c; read it in
  `docs/contracts/investor-reporting/v1/routes.json`, the `analysis-report` route's `query` object, and
  `docs/contracts/investor-reporting/v1/CONTRACT.md`, the vocabulary row for the new reason):
  - operation `analysis-report`, `GET /api/scoped/investor-reporting/analysis/{jobId}/sections`;
  - the selector is the QUERY STRING member `ticket_id` (beside `selected_tenant`), the ticket service's id form;
  - the refusal a caller reads is `status.public_reason_code` = `REPORT_TICKET_MISMATCH`. It is served ONLY to a caller already
    admitted to the request. It is NOT `NOT_FOUND` and it is not a waiting state.
- **What the page says** (CTO ruling msg 4984): in words, that this ticket's recorded report belongs to another ticket; NO waiting
  state, no report section, not the request record. On DEV `isReportNotReady` (`analysisRequest.ts`) treats only NOT_READY, NOT_FOUND
  and 404 as waiting, so the new value already falls out of that branch: make its presentation deliberate, not an accident of a rethrow.
- **One more thing in this cell's grant, by CTO condition (msg 5045, item 4), row `IRPT_ANLREQ-D2-W52-S7`:** the portal's generated
  contract-named reason-code set must contain the new value, or `src/pages/InvestorReporting/__tests__/fe-s-40/reason-codes.test.ts`
  (its arm at about line 243) goes red and a page prints the code as "not defined by the v1 contract". Regenerate it with the
  generator `src/pages/InvestorReporting/__tests__/fe-s-40/gen-named-codes.mjs` (read it for its entry point and what file it writes:
  `CONTRACT_NAMED_REASON_CODES` in `src/pages/InvestorReporting/render/Page.tsx` or wherever it writes) and commit EXACTLY what it
  writes. Never hand-edit the generated set, the generator or the test. The generator reads the contract documents from the workspace
  worktree, which carries the new row. Run that test file and report its line. If the generator changes anything beyond adding the
  one value, list every other change and why; if it would drop or rewrite something by hand, STOP that step and file a row.
  The grant widens by exactly the file(s) that generator writes.
- The typecheck criterion `AR72-y-AC3` covers the regenerated file too.

### ACCEPTANCE

<criterion id="AR72-y-AC1" cell_refs="AR-y-72"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r7/ar7_checks.py y72-open --root C:/dev/wk-irpt-anlreq-51 --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y72-OPEN-OK</expect></criterion>
`AR72-y-AC1`: the new test file holds the three named tests and passes.

<criterion id="AR72-y-AC2" cell_refs="AR-y-72"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r7/ar7_checks.py y72-keep --root C:/dev/wk-irpt-anlreq-51 --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y72-KEEP-OK</expect></criterion>
`AR72-y-AC2`: the difference control -- the whole TicketCenter test folder passes.

<criterion id="AR72-y-AC3" cell_refs="AR-y-72"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py portal-tsc --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>PORTAL-TSC-OK</expect></criterion>
`AR72-y-AC3`: the portal typechecks. A third criterion because the cell changes a shared client method's signature.

<expected_criteria>AR72-y-AC1 AR72-y-AC2 AR72-y-AC3</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/` (the open path and tests) and the ONE client method in
  `src/api/endpoints/investor-reporting.ts` with its request type.
- READ only: everything else. No live call, no push, no deploy. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R7_Y.md</decomp_doc>
<owned_cells>AR-y-72</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR72-y-AC1 AR72-y-AC2 AR72-y-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-72.open-control-sends-its-ticket-id.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-72`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR72-y-AC1,AR72-y-AC2,AR72-y-AC3`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading: the open path's files named from this lane's rounds 3 and 6 (AnalysisRequestParts.tsx, analysisRequest.ts, 2 files); NOT seen by the issuer: every other caller of the client's owned-report read outside TicketCenter (the worker searches src and reports the count before changing the signature; an optional argument leaves them unchanged). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission changes.
comp-adversary: RUN -- by reading 0 of the cell's files at this cut (they are being edited by round 6's cell); NOT seen: the open path as it will stand after AR-y-61. The lens: a refusal rendered as the request record or as an empty report. The face forbids both and names a test for each.
lane: the Ticket Center open path, one client method, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO msg 4955 item (b), with TO-AR-y-71 in one issuance. Not spawned at issuance: it waits on `AR-y-71` merged and round 6's
  `AR-y-61` terminal. `AR72-y-AC1` base: FAIL as expected (no test file).
- Seating: slot ~51 holds round 6's open order `TO-AR-y-61` (same project); this order queues behind it in the same slot.
