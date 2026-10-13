# TO IRPT_ANLREQ.TO-AR-y-271.j2-request-id-recorded-for-partner-firm-filer -- J2: the request id lands on a partner-firm filer's ticket, without the REPORT route

<to_id>IRPT_ANLREQ.TO-AR-y-271</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~92</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-271` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~92`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-92` (branch `wk-IRPT_ANLREQ-92`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~92 <0.9.0_WK_IRPT_ANLREQ~92@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W92-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-271`, inlined) -- J2. A PARTNER-FIRM ADVISOR'S TICKET MUST CARRY ITS REQUEST ID. Read the hop; build the smallest fix that WIDENS NOBODY'S REACH; nothing is released.

*FWD-1 (PRD v0.5, ADMITTED @68115f2d84; CTO GO msg 7191): one Analysis Request goes from the Ticket Center form to FOUR attachments on the same OPEN ticket with no person in between: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report (the Opal producer, not YCharts), (4) the AI commentary draft. The driven arm is a SYNTHETIC partner-firm advisor under a never-widen pair. Binding constraints: C-FIRM (the firm is the signed-in user's, never a choice outside its domain; the staff picker stays out of the advisor path), the variant the advisor selects is the variant produced, Opal staff do not file in the Ticket Center, FWD-4 (a failed hop shows on the ticket). PRD: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (ENDPOINT, C-PACKAGER, C-FIRM, C-ABSORB); the direction: `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 2 O1. Hop J2 (direction O1): the portal orchestration `fileAndRequestAnalysis` (`portal/src/pages/TicketCenter/analysisRequest.ts` :304-322 at origin/DEV) runs upload, create ticket, POST the analysis with the `ticket_id`, then records the request id on the ticket with `POST /tickets/{id}/report`. The ticket service route table (`infra/aws/lambda/ticket_center/lambda_function.py` :8-25) admits REPORT for 'internal humans; the ticket's assignee only' and a partner-firm human only SUBMIT-FORM, so a partner-firm advisor's request id likely never reaches its ticket. Of 27 tickets 3 carry a `report_ref` and none forms a usable pair (`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R24_TR_DP24_CANDIDATE_READ_20261012.md`). The CTO's rule: 'the SUBMIT-FORM path or a named service records it; the advisor never needs the REPORT route'.*

1. **Read the hop, from the code that runs it.** (a) The portal client: `src/pages/TicketCenter/analysisRequest.ts` (`fileAndRequestAnalysis`, what it calls in what order and what it does on each refusal) and `src/api/endpoints/tickets.ts`. (b) The ticket service: `infra/aws/lambda/ticket_center/lambda_function.py` (SUBMIT-FORM, CREATE, REPORT, PACKAGE: who is admitted, what each writes, `TYPE_DEFINITIONS['analysis_request']`, how `report_request_id` / `report_ref` are stored and which member names the service accepts) and its tests. (c) The analysis side: who receives `POST /api/scoped/investor-reporting/analysis` with a `ticket_id` and whether that receiver knows the ticket (`infra/aws/lambda/investor-reporting/ycharts/generate/submission.py`, `acceptance.py`, the READY event `analysis_ready` at `resident_worker.py` :191-200). Record `trace` {`hops` ({file:line, who calls, with which principal, what is written}), `where_the_id_is_lost` (for a PARTNER-FIRM human: the first hop where the request id does not reach the ticket, READ or RUN), `principals` (which principal each hop signs in as)}.
2. **Choose the smallest path that widens no human's reach.** Candidates, each judged on the code: (i) the SUBMIT-FORM path accepts and stores the request id from the same filer (a request id the filer owns, written once, bound to the ticket's own requester); (ii) a NAMED service (an existing service subject such as the one the packager or the drafter uses) records it after the analysis is accepted; (iii) REPORT is opened to the ticket's requester (REJECT unless it is the only way: it widens a human). Record `options` ({path, files to change, who is newly admitted to what, the test that would pin it}) and `chosen` with the reason.
3. **Build it, if it lies inside this grant.** The grant is the ticket service file and its tests plus the portal client and its tests (see `<paths>`). Write the change and the tests: (a) the chosen principal records the id once; (b) a second write is refused; (c) a different filer or a different ticket is refused; (d) a partner-firm advisor's filing ends with the id on its ticket, read back; (e) every existing authorization test still passes (list the counts; edit none to make it pass). `before_arm`: the new tests FAIL at HEAD. **If the chosen path needs a file outside the grant (the analysis receiver, the packager, the resident), STOP before building, file a BLOCKING row naming the file and its lane, and write the record with `built` absent.** A change to who may write what in the ticket service is an authorization change: the record states it in one paragraph for the never-widen pair that will govern its release (what is newly admitted, to do what, to which keys, rollback).
4. **Write `r23/J2_REQUEST_ID.json`:** `trace`, `options`, `chosen`, `built` (files changed, commit), `authorization_change` (the paragraph), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `claim`, `not_read`.
5. **In your report:** where the id is lost (file:line), the chosen path, what is newly admitted, the counts.

### ACCEPTANCE

<criterion id="AR271-y-AC1" cell_refs="AR-y-271"><invocation>python C:/dev/wk-irpt-anlreq-92/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y271-j2 --root C:/dev/wk-irpt-anlreq-92</invocation><expect>Y271-J2-OK</expect></criterion>
`AR271-y-AC1`: the record traces the hop for a partner-firm human with file:line, names the options and the chosen path, states the authorization change in one paragraph, and (if built) a new test file passes with its before-arm failing at HEAD and the existing ticket service tests still pass.

<criterion id="AR271-y-AC2J" cell_refs="AR-y-271" judgment="true"/>
`AR271-y-AC2J` (judgment, graded at L9, never by you): the hop was READ from the code (not the route table alone), the chosen path admits no human newly to a write the service withheld, the id is written once and only for its own ticket, a cause outside the grant stopped the cell with a row, and nothing was released.

<expected_criteria>AR271-y-AC1 AR271-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~92/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_analysis_request.py
infra/aws/lambda/ticket_center/tests/test_request_id_record.py
portal/src/pages/TicketCenter/analysisRequest.ts
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-271</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~92/IRPT_ANLREQ.TO-AR-y-271.j2-request-id-recorded-for-partner-firm-filer.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-271`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR271-y-AC1,AR271-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR271-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
