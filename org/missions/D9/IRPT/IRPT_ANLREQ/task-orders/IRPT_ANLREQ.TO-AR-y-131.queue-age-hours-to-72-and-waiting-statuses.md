# TO IRPT_ANLREQ.TO-AR-y-131 -- the queue age shows hours up to 72 hours, and only for a named closed list of waiting statuses

<to_id>IRPT_ANLREQ.TO-AR-y-131</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, deployed or called live)
**Decomp cell:** `AR-y-131` (`decompositions/IRPT_ANLREQ_DECOMP_R13_Y.md`) | **outcome_ref:** FWD-1 (the surface); TCKT_VNEXT FWD-5 by CTO msg 5682 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>`. The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r13`, cut from portal DEV `c2c6a8aedd`
  (confirm with `git rev-parse --abbrev-ref HEAD` before you edit). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`.
  Never push. Never run `bun install`.

### THE CELL (`AR-y-131`, inlined)

*The queue age shows hours up to 72 hours and whole days from there; and an age is shown only for a named, closed list of waiting statuses.*

Why. On portal DEV the Ticket Center queue list shows, beside each ticket's created time, how long it has waited
(`src/pages/TicketCenter/elapsedAge.ts` `elapsedAge(createdAt, now)`; `CreatedCell` in `TicketCenter.tsx`; the tests in
`src/pages/TicketCenter/__tests__/queue-elapsed-age.test.tsx`). The reviewer found two limits and the CTO ruled both:

1. **47 hours reads "1 day".** A person ranks the queue by how long each request has waited; a floor to whole days hides almost a
   day of waiting on exactly the tickets being ranked. THE RULE: under one minute `under a minute`; minutes below one hour; HOURS
   from one hour up to but not including 72 hours (`1 hour`, `47 hours`, `71 hours`); whole DAYS from 72 hours on (`3 days`,
   `40 days`). Units in words, singular for one, as today. The empty-string cases stay exactly as they are (no created time, an
   unparseable one, a created time after `now`).
2. **The code shows an age for every status except `completed`.** That is wider than what was asked. THE RULE: an age is shown for
   the statuses in which a ticket is WAITING, named as a CLOSED LIST in the code, exported as `WAITING_STATUSES`, and for no other
   status. A status added later shows no age until someone adds it to that list on purpose.
   **Read first, before you write the list:** which statuses exist -- the `TicketStatus` type in `src/api/endpoints/tickets.ts`, and
   the ticket type's own definition on the service side, read in the WORKSPACE worktree (`infra/aws/lambda/ticket_center/` -- find
   where a ticket's status values and the per-type definitions are declared; cite file and line). For each status that exists say
   whether a ticket in it is waiting on Opal (it shows an age) or not, and why, in one line each in your report. If the portal's
   type and the service's values DIFFER, do not reconcile them: list the difference in your report and file a row.
   Type the list so that it can only hold real statuses (for example `readonly TicketStatus[]`), and decide by membership
   (`WAITING_STATUSES.includes(status)`), never by "not completed".
3. The age not ticking while the page sits open is ACCEPTED: build no timer.
4. Tests, in the existing file `queue-elapsed-age.test.tsx`: keep its five tests' NAMES; change only the expectations the new rule
   forces (say which). ADD tests named exactly:
   - `47 hours reads as 47 hours`
   - `71 hours reads as hours and 72 hours reads as 3 days`
   - `a status outside the waiting list shows no age`
   - `every waiting status shows an age`
   The third passes a status value that is NOT in the list (cast through the type as the folder's tests do for an unknown value; no
   `any`, no `// @ts-` comment) and asserts no age; the fourth loops over `WAITING_STATUSES`. Every test fixes `now` as a literal:
   the file must not contain `Date.now()` or `new Date()` with no argument.
5. No other change: no restyle, no column, no change to `fmtWhen`, the fetch or any file outside `src/pages/TicketCenter/`.
6. In your report: the statuses read (portal type and service side, with file and line), which are in `WAITING_STATUSES` and why;
   the helper's words for 59 minutes, 1 hour, 47 hours, 71 hours, 72 hours, 95 hours, 96 hours and 40 days; `bun run typecheck`;
   the eslint error-count line (`bun x eslint <changed files>`); `git diff --stat origin/DEV HEAD`.

### ACCEPTANCE

<criterion id="AR131-y-AC1" cell_refs="AR-y-131"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r13/ar13_checks.py y131-age --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y131-AGE-OK</expect></criterion>
`AR131-y-AC1`: the four named tests are present with the five earlier ones, the file never reads the real clock, a closed list
named `WAITING_STATUSES` exists, the age is no longer decided by "everything except completed", and the file passes.

<criterion id="AR131-y-AC2" cell_refs="AR-y-131"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r13/ar13_checks.py y131-keep --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y131-KEEP-OK</expect></criterion>
`AR131-y-AC2`: the difference control -- the whole TicketCenter test folder passes (58 at the base, plus yours).

<criterion id="AR131-y-AC3" cell_refs="AR-y-131" judgment="true"/>
`AR131-y-AC3` (judgment, graded at L9, never by you): the statuses named as waiting are the ones in which a ticket is waiting on
Opal, read from the ticket type's definition, and a person ranking the queue is not misled by the unit the age is shown in.

<expected_criteria>AR131-y-AC1 AR131-y-AC2 AR131-y-AC3</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/` only.
- READ only: everything else. No live call, no push, no deploy. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R13_Y.md</decomp_doc>
<owned_cells>AR-y-131</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR131-y-AC1 AR131-y-AC2 AR131-y-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-131.queue-age-hours-to-72-and-waiting-statuses.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-131`. `AR131-y-AC3` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with `method`, `invocation`, `denominator` and a `status_reason`
naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR131-y-AC1,AR131-y-AC2,AR131-y-AC3`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 2 files of the landed cell whole at its drain (elapsedAge.ts, 27 lines; the CreatedCell diff, 18 lines); NOT seen: the service side's status values and per-type definitions (the worker reads and cites them before writing the list). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 analysis of 3 limits (2 corrected here) against the face; the lens: a list that is 'not completed' under another name, or a 72-hour boundary off by one. The check refuses the old expression and names a test for 71 and 72 hours. NOT seen: whether the service has a status the portal type does not name.
lane: the Ticket Center list cell, its helper and its test file, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-13 analysis @7542d8555c, items 2.1 and 2.3. `AR131-y-AC1` base: FAIL as expected (4 tests absent, no
  `WAITING_STATUSES`, the old expression present). `AR131-y-AC2` base: PASS as expected (58 pass at DEV c2c6a8aedd).
- After the drain: the issuer files eslint, typecheck and the suite on the candidate's head; the CTO reads the product-file change.
- Seating: slot ~51 is reused; its earlier orders are terminal.
