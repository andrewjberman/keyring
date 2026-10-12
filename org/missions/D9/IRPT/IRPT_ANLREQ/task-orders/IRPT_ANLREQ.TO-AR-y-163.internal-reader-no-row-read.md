# TO IRPT_ANLREQ.TO-AR-y-163 -- a READ: the investor-reporting internal firm reader and a caller with no users row (row TCKT_VNEXT-D2-S48)

<to_id>IRPT_ANLREQ.TO-AR-y-163</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of code; in-process runs on fakes; no live call, no product file changed)
**Decomp cell:** `AR-y-163` (`decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md`) | **outcome_ref:** row TCKT_VNEXT-D2-S48 (PRD v0.4 ROUND-16 item 3) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W53-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`.

### THE CELL (`AR-y-163`, inlined) -- A READ. You change no product file and make no live call.

*The investor-reporting service's INTERNAL firm reader and a caller the users table does not know.*

Why. Row `TCKT_VNEXT-D2-S48`: the ticket service is being changed to refuse an internal caller with NO users row ("the service does
not grant its widest reading to a caller it cannot find", TCKT_VNEXT PRD v0.4 ADDENDUM 3, C-FENCE). The investor-reporting
service's internal firm reader -- the code that decides which firms an Opal-internal caller may read when a firm other than the
caller's own is selected -- returns UNCHANGED (unrestricted) for a caller with no row, and its docstring states that as the rule
(IB-pr-387). After the ticket release the two services answer the same caller differently. And the CTO's own correction (msg
6181): the ticket contract reads a row's EXISTENCE, so a DISABLED row still admits a caller. The CTO rules whether this reader
follows; first it needs this read.

1. `reader`: find it in `infra/aws/lambda/investor-reporting/` (start at `_authz/`; the functions that load a caller's firm list or allowed firms; the name the
   row cites, IB-pr-387, appears in commit messages and comments). `{"file_function": "...", "stated_rule": "<the docstring's
   sentence, with file:line>", "what_it_reads": "<table, key, members>", "who_calls_it": ["<file:line>", ...]}`.
2. `cases`, one row each, RUN IN PROCESS with the fakes the folder's tests use (read a test to see how; no live call), or
   `inferred` with the lines if it cannot be run: `NO_ROW`, `DISABLED_ROW` (a row whose status member says disabled or inactive --
   find the member's name and values first), `ACTIVE_ROW_OWN_FIRM`, `ACTIVE_ROW_OTHER_FIRM`. Each `{"case": "...", "returns":
   "<what the reader returns and what the route then serves>", "claim": "measured"|"inferred", "evidence": "<the test or the lines>"}`.
3. `routes_it_guards`: EVERY route whose answer depends on this reader, each `{"route": "<operation and path>", "file_line": "...",
   "what_a_no_row_caller_gets": "..."}`; print the count of routes searched (the contract's `routes.json` is the denominator).
4. `the_ticket_service_shape`: what TCKT_VNEXT round 7 changed, read from its order and its diff
   (`org/missions/D7/TCKT/TCKT_VNEXT/task-orders/` round 7; `infra/aws/lambda/ticket_center/lambda_function.py`): the rule it
   applies, the refusal a no-row caller now gets, the lines.
5. `proposed_cell`: `{"what": "<the change if the CTO rules this reader follows>", "write_set": [...], "risk": "...",
   "who_is_refused_that_is_served_today": "<which callers; whether any real caller class has no row today, and how you would
   count them without a live read>", "open_question": "..."}`; `not_read`: a list.
6. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r16/INTERNAL_READER_NO_ROW_READ.json`; commit it.

### ACCEPTANCE

<criterion id="AR163-y-AC1" cell_refs="AR-y-163"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16_checks.py y163-read --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y163-READ-OK</expect></criterion>
`AR163-y-AC1`: the record names the reader and its stated rule, a row for each of the four cases with its claim and evidence,
every route it guards, the ticket service's shape, a proposed cell, and what was not read. It grades the record's form.

<expected_criteria>AR163-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md</decomp_doc>
<owned_cells>AR-y-163</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR163-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-163.internal-reader-no-row-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-163`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR163-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 row (TCKT_VNEXT-D2-S48, read whole by the issuer: OBSERVATION, INERT) and 1 CTO message (6181: the contract reads a row's existence); NOT seen: the reader, its callers and the routes it guards (the worker reads them; the count of routes searched is printed). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called by this cell. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: RUN -- by reading 0 policies; the cell READS an authorization rule in code and changes none; whether the rule changes is the CTO's contract call after this read.
comp-adversary: RUN -- by reading 1 row against the face; the lens: a 'no row' case asserted from the docstring and never run, or a disabled row treated as no row. The face orders each case run in process on the folder's fakes and names DISABLED_ROW as its own case. NOT seen: whether any real caller class has no row today.
lane: the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.4 @4b1447e2cc ROUND-16 item 3 and CTO msg 6181. `AR163-y-AC1` base: FAIL as expected (no record).
- The cell that changes the reader, if the CTO rules it follows the ticket service, is cut from this record at the next issuance.
- Seating: slot ~53 is reused; its earlier orders are terminal.
