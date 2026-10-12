# TO IRPT_ANLREQ.TO-AR-y-164 -- the ticket panel shows who sent the final commentary and when, and offers the one confirmed control that records it

<to_id>IRPT_ANLREQ.TO-AR-y-164</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, deployed or called live; NO test presses the route)
**Decomp cell:** `AR-y-164` (`decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md`) | **outcome_ref:** FWD-1 (hop 15, the ticket page); TCKT_VNEXT round-6 item 3 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r16`, cut from portal DEV `0a06280a40`
  (confirm with `git rev-parse --abbrev-ref HEAD` before you edit). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`.
  Never push. Never run `bun install`. The worktree may list some generated files under `contracts/wire/` as modified with no
  content difference (line endings): never commit them.

### THE CELL (`AR-y-164`, inlined)

*The ticket panel shows who sent the final commentary and when, and offers the one control that records it.*

Why. An Analysis Request ticket carries a DRAFT commentary (`ticket.draft_commentary`, rendered in
`src/pages/TicketCenter/AnalysisRequestParts.tsx` at about line 386). When an Opal person has sent the final commentary to the
advisor, the ticket service can now record that: the ticket gains the member `commentary_sent: {sent_by, sent_at}`. The page does
not know the member and offers no way to record it.

The route (as its owning lane reports it; the service is live, UNEXERCISED): `POST /api/scoped/tickets/{ticketId}/commentary-sent`
with NO body field (any body key is a 400). 200 answers `{ticket_id, commentary_sent}`. 409 with one of four codes:
`SENT_WRONG_TICKET_TYPE`, `SENT_NO_DRAFT`, `SENT_ALREADY_RECORDED`, `SENT_TICKET_CHANGED`. 404 outside the caller's firm scope.
**It is written ONCE and cannot be undone.** Read the service's handler in the WORKSPACE worktree
(`infra/aws/lambda/ticket_center/lambda_function.py`: find the route and its four codes; cite the lines) and confirm each fact
above from the code; where the code differs from this paragraph, the CODE is right: say so and build to the code.

1. **Type and client.** `src/api/endpoints/tickets.ts`: add `commentary_sent?: { sent_by: string; sent_at: string } | null` to the
   `Ticket` type (read the handler for the member's exact shape) and ONE function that POSTs the route with NO body, in the file's
   existing style. That file is in your grant for those two additions only.
2. **Display.** Where the draft commentary is rendered: when `commentary_sent` is present, one line saying the final commentary
   was sent, by whom and when (the page's existing date formatting; reuse a class the panel already uses). When it is absent,
   nothing is shown about sending.
3. **The control.** Offered ONLY when the ticket has a draft, nothing is recorded yet, and the ticket is an analysis request (the
   states in which the service would accept; never offered otherwise). Pressing it does NOT post: it asks for confirmation first,
   in words that say this is recorded once and cannot be undone (use the page's existing confirm pattern if the Ticket Center
   has one -- read first; otherwise a second explicit press on a clearly worded confirm control; never the browser's `confirm()`
   if the page does not already use it). Only the confirmed press posts, ONCE; the control is disabled while the post is in
   flight; on 200 the panel shows the recorded sender and time from the ANSWER and the control is gone.
4. **Refusals in words.** Each of the four 409 codes, the 404 and any other failure is shown in one plain sentence each, your
   wording, no code shown: wrong ticket type; no draft to send; already recorded (and by whom and when, if the answer or a
   refreshed ticket says so); the ticket changed while you were looking (ask the person to reload). A closed list keyed by code,
   with a fallback sentence for a code not on it.
5. No restyle. No file outside `src/pages/TicketCenter/` and the two additions in `tickets.ts`. NO test presses the live route.
6. **One new test file**, `src/pages/TicketCenter/__tests__/commentary-sent.test.tsx`, typed fakes, no `any`, no `// @ts-` comment,
   with tests named exactly:
   - `a ticket with commentary_sent shows who sent it and when`
   - `the control is offered only when a draft exists and nothing is recorded`
   - `the press asks for confirmation before it posts`
   - `a confirmed press posts once with no body and shows the recorded sender`
   - `each refusal code is shown in words`
7. In your report: the handler's lines for the route and each code, and any difference from this face; the sentences; `bun run
   typecheck`; the eslint error-count line (`bun x eslint <changed files>`); `git diff --stat origin/DEV HEAD`.

### ACCEPTANCE

<criterion id="AR164-y-AC1" cell_refs="AR-y-164"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16_checks.py y164-sent --root C:/dev/wk-irpt-anlreq-51 --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y164-SENT-OK</expect></criterion>
`AR164-y-AC1`: the five named tests are in the new file and the whole TicketCenter folder passes (67 at the base, plus the five).

<criterion id="AR164-y-AC2J" cell_refs="AR-y-164" judgment="true"/>
`AR164-y-AC2J` (judgment, graded at L9, never by you): a person cannot record the send by one stray press, knows before pressing
that it cannot be undone, and reads each refusal as a sentence that says what to do.

<expected_criteria>AR164-y-AC1 AR164-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/` and the two additions in `src/api/endpoints/tickets.ts`.
- READ only: everything else. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md</decomp_doc>
<owned_cells>AR-y-164</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR164-y-AC1 AR164-y-AC2J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-164.ticket-page-commentary-sent.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-164`. `AR164-y-AC2J` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR164-y-AC1,AR164-y-AC2J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 2 lines at portal DEV 0a06280a40 (tickets.ts:103 draft_commentary on the Ticket type; AnalysisRequestParts.tsx:386 where the draft is rendered) and 1 message of the owning lane (2.0.0_SA_COO~V2 msg 5999: the route, its answers and codes); NOT seen: the service handler (the worker reads it in the workspace worktree and builds to the code where it differs). comp-routes: RUN -- by reading 1 route as reported (POST /api/scoped/tickets/{ticketId}/commentary-sent, no body; 200, 409 with 4 codes, 404, 400): the cell adds 1 client function for it and 0 tests call it live; the first live press is the issuer's own pair. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 fact (the write is made once and cannot be undone) against the face; the lens: one stray press recording a send that did not happen, or a double post. The face orders a confirm step, one post, a disabled control in flight and a named test for each. NOT seen: the route exercised (it is unexercised by anyone).
lane: the Ticket Center panel, two additions in the tickets client, one test file, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.4 @4b1447e2cc ROUND-16 item 4 and the CTO's TCKT_VNEXT round-6 analysis @0b932076f0 item 3.
  `AR164-y-AC1` base: FAIL as expected (no test file; the folder itself passes, 67).
- The candidate goes to the CTO after the drain. The control's first LIVE press is its own pair (an irreversible write on a real
  ticket), the issuer's, and is not part of this order. `2.0.0_SA_COO~V2` is sent this order's id.
- Seating: slot ~51 is reused; its earlier orders are terminal.
