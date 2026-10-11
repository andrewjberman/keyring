# TO IRPT_ANLREQ.TO-AR-y-101 -- the ticket's Open report read falls back ONCE without the ticket id when the live service refuses the query member

<to_id>IRPT_ANLREQ.TO-AR-y-101</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, deployed or called live)
**Decomp cell:** `AR-y-101` (`decompositions/IRPT_ANLREQ_DECOMP_R10_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r7`, at `14e77fb583` (round 7's candidate
  with portal DEV `9ca634c6` merged in by the issuer). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`. Never push.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The workspace worktree shows
  ` M portal`: never commit it. Never run `bun install`.

### THE CELL (`AR-y-101`, inlined)

*The ticket's Open report read sends `ticket_id`, and on the ONE refusal the live service gives for an unknown query member
(`UNEXPECTED_OWNED_READ_QUERY`) it repeats the read ONCE without it. Any other refusal is shown as it is.*

Why. Round 7 made the Ticket Center's Open control send the ticket's own id with the report read (`getOwnedAnalysisReport(requestId,
selectedTenant, ticketId)` in `src/api/endpoints/investor-reporting.ts`; the open path in `src/pages/TicketCenter/analysisRequest.ts`
`openReport` and `AnalysisRequestParts.tsx`; the binding refusal `isReportTicketMismatch` / `REPORT_TICKET_MISMATCH_MESSAGE`). The
service that understands `ticket_id` is not released yet: the LIVE service refuses any query member but `selected_tenant` with the
public reason code `UNEXPECTED_OWNED_READ_QUERY`. So today this candidate would make every ticket's Open report read fail. The CTO's
ruling: make the order of the two releases not matter.

1. Find every report read the Ticket Center makes for a ticket with a ticket id (read `openReport` and every caller of
   `getOwnedAnalysisReport` under `src/pages/TicketCenter/`; say in your report how many call sites there are). Put the fallback in
   ONE place they all go through (a small helper beside `isReportTicketMismatch` in `analysisRequest.ts` is the expected shape).
2. The fallback, exactly: make the read WITH the ticket id. If, and only if, it is refused with reason code
   `UNEXPECTED_OWNED_READ_QUERY`, make the same read ONCE more WITHOUT the ticket id and use that second answer, whatever it is
   (a report, or a refusal shown as it is). Never a third read. Recognise the refusal the way `isReportTicketMismatch` recognises its
   code (read how the client surfaces `status.public_reason_code` on a refused read and use the same carrier; do not match on a
   message string or on an HTTP status alone).
3. Every other refusal -- `REPORT_TICKET_MISMATCH` above all, and NOT_READY, NOT_FOUND, any error -- is shown exactly as on this
   branch today, with NO second read. A binding refusal must never be retried without the id: that would open the report the binding
   exists to refuse.
4. Do not touch `src/api/endpoints/investor-reporting.ts`: the client method is unchanged. Do not restyle anything; no new wording
   on the page (the fallback is silent: the page reads as it does today).
5. **One new test file**, `src/pages/TicketCenter/__tests__/package-open-ticket-fallback.test.tsx`, in the style of
   `package-open-ticket-binding.test.tsx` (typed fakes; no `any`, no `// @ts-` comment), with tests named exactly:
   - `the first read sends the ticket's id`
   - `an unexpected-query refusal repeats the read once without the ticket's id`
   - `any other refusal is shown and the read is not repeated`
   - `a binding refusal is still shown as a binding refusal`
   The second test asserts the fake was called exactly twice and that the second call carried no ticket id; the third and fourth
   assert it was called exactly once. Existing tests keep their names.
6. In your report: `bun run typecheck` result, and the eslint ERROR count of the files you changed (`bunx eslint <files>`; report the
   line it prints, do not fix files you did not change).

---

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~17:4xZ): RE-OPENED. The code this face named is never served; the fallback keys on
the served reason `INVALID_INPUT`.** The fault is in the face (and in the analysis it copied), not in the first build: CTO msg 5465.

- **Measured by the issuer in the LIVE package of `irpt-status`** (the downloaded zip, digest `6idtFvAm...`, 49 members searched):
  `UNEXPECTED_OWNED_READ_QUERY` is the MESSAGE of an exception of class `RequestReadRefused` (`entry.py` lines 165 and 185). The
  served `public_reason_code` is derived from the exception's CLASS through the entry's reasons map, `entry.py` line 252:
  `"RequestReadRefused": "INVALID_INPUT"`. The message string is never served. So the page sees `INVALID_INPUT`.
- **What to change, in the portal branch as it stands at `d763d48c` (your earlier commit is inherited state; add a commit, do not
  rewrite it):** the helper's predicate compares `publicReasonCode === 'INVALID_INPUT'` and is renamed to say what it reads (for
  example `isInvalidInputRefusal`); its comment says the truth: this is the reason the live service serves for an unknown query
  member, and it is BROAD -- every refusal of class `RequestReadRefused` on the report read shares it (the live package raises that
  class at about 25 places in `owned_report.py`, for a bad request id and for binding and retention faults). That breadth is accepted
  by the CTO: a second read WITHOUT the ticket id on any of them answers exactly as the page reads today. Say that in the comment
  in two lines.
- Unchanged and still required: `REPORT_TICKET_MISMATCH` is NEVER retried (it is its own served reason, not `INVALID_INPUT`); one
  second read at most; every other reason (NOT_FOUND, NOT_AUTHORIZED, UNEXPECTED, a network error) propagates with no second read.
- The four test names stay exactly as they are. The second test's fake refuses with `publicReasonCode` `'INVALID_INPUT'`. Neither
  `analysisRequest.ts` nor the test file may contain the quoted string `'UNEXPECTED_OWNED_READ_QUERY'` (the check refuses it; a
  comment may name the message without quotes).
- Then: both criteria again, verbatim; a NEW proof instance over the old one (same path), validated after its commit; flip
  `<status>` to `complete` on VALID. Report typecheck and the eslint error count as before (`bun x eslint`).
- Gate limb that graded this amendment: read from this commit's own output.

### ACCEPTANCE

<criterion id="AR101-y-AC1" cell_refs="AR-y-101"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r10/ar10_checks.py y101-fallback --root C:/dev/wk-irpt-anlreq-51 --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y101-FALLBACK-OK</expect></criterion>
`AR101-y-AC1`: the new test file holds the four named tests and passes.

<criterion id="AR101-y-AC2" cell_refs="AR-y-101"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r10/ar10_checks.py y101-keep --root C:/dev/wk-irpt-anlreq-51 --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y101-KEEP-OK</expect></criterion>
`AR101-y-AC2`: the difference control -- the whole TicketCenter test folder passes (49 at the base, plus yours).

<expected_criteria>AR101-y-AC1 AR101-y-AC2</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/` only (the open path and the one new test file).
- READ only: everything else. No live call, no push, no deploy. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R10_Y.md</decomp_doc>
<owned_cells>AR-y-101</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR101-y-AC1 AR101-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-101.open-read-falls-back-once-without-ticket-id.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-101`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR101-y-AC1,AR101-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading: 1 search of the Ticket Center folder and the client file for the read and its two codes (40 lines shown of more; the client method at lines 1201-1204 and 1647-1651, the open path's imports at AnalysisRequestParts.tsx:16 and :223); NOT seen by the issuer: the body of openReport and the count of call sites (the worker counts them before changing anything). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 ruling (the CTO's analysis, item 1) against 2 refusal codes; the lens: a retry that fires on the BINDING refusal and so opens the report the binding refuses, or a retry loop. The face forbids both and names a test for each. NOT seen: how the client carries the reason code on a refused read.
lane: the Ticket Center open path, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-10 analysis @57cdd1cdde, item 1 (row `IRPT_ANLREQ-D2-S51`, ARMED, disarm owner the CTO).
  `AR101-y-AC1` base: FAIL as expected (no test file). `AR101-y-AC2` base: PASS as expected (49 pass).
- After the drain: the issuer files tsc, the test count and the eslint error count; the CTO reads the product-file change; the
  integrator lands it on DEV; row S51 closes on the landing.
- Seating: slot ~51 is reused; its earlier orders are terminal.
