# TO IRPT_ANLREQ.TO-AR-y-132 -- a READ: how several accounts in one file can be recognised, and what the upload door does today with each bad sheet

<to_id>IRPT_ANLREQ.TO-AR-y-132</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read; synthetic sheets run in process; no live call, no product file changed)
**Decomp cell:** `AR-y-132` (`decompositions/IRPT_ANLREQ_DECOMP_R13_Y.md`) | **outcome_ref:** FWD-1 (the surface); TCKT_VNEXT FWD-3 by CTO msg 5737 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>`. The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either.

### THE CELL (`AR-y-132`, inlined) -- A READ. You build nothing and change no product file.

*How can "several accounts in one file" be recognised at all, and what does the upload door do today with each kind of bad sheet?*

Why. A person files an Analysis Request in the Ticket Center and attaches a holdings sheet. Today a sheet that cannot be used
(several accounts in one file, a totals row, a holding that cannot be priced) is found later and comes back by email. The outcome
asked for (TCKT_VNEXT FWD-3): "a known-bad sheet (several accounts in one file, a totals row, a holding that cannot be priced) is
turned back with what to fix, and a known-good sheet goes through ... a file that today would come back by email comes back from
the form instead." A first read by another lane found that the normalizer reads NO account column at all
(`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~20/ONE_ACCOUNT_CHECK_READ.json`: `infra/aws/lambda/investor-reporting/intake/parse.py`
recognises identifier, name, unit and currency headers only; `uploads.py:209` sets `account_ids=[]` for a prospect input). So before
a check can be built, someone must say how several accounts in one file could be RECOGNISED. That is this cell.

Read `infra/aws/lambda/investor-reporting/intake/` (`uploads.py`, `parse.py`, `template_reader.py`, `upload_resolution.py`,
`portfolio.py`, their tests and test fixtures), the upload contract documents under `docs/contracts/investor-reporting/v1/` that the
door answers to, and the form's side in the portal BY REF ONLY (`git -C C:/dev/wk-irpt-anlreq-51/portal show origin/DEV:<path>`,
`... grep -n <term> origin/DEV -- src/pages/TicketCenter`; another worker edits that worktree: never its working files).

1. **`account_recognition`** -- every SIGNAL by which a sheet could show it holds more than one account, each a row
   `{"signal": "...", "where_seen": "<file:line of a fixture, template, test or document that shows this shape, or 'no example in
   the repository'>", "how_the_parser_would_see_it": "<what parse.py does with it today, with the line>", "false_positive_risk":
   "<a one-account sheet that would trip it>", "claim": "measured"|"inferred"}`. Consider at least: a column whose header names an
   account (list the header words you would treat as one and why); a repeated header row or repeated identifier block; an
   identifier that appears on several rows; several worksheets in one workbook; subtotal rows between blocks. Do not invent a
   signal you cannot tie to a file or to parser behaviour: say `inferred` and why.
2. **`door_today`** -- for EACH of four kinds, build ONE small SYNTHETIC sheet (made-up tickers such as `AAA`, `BBB`; made-up
   numbers; no real security identifier you did not find in a test fixture, no name, no account number that looks real) in a temp
   folder OUTSIDE the worktree, and run the door's own parsing and validation on it IN PROCESS, the way the folder's tests call it
   (read a test to see the entry function and its arguments; no AWS call, no network, no upload): kinds `SEVERAL_ACCOUNTS`,
   `TOTALS_ROW`, `UNPRICEABLE_HOLDING`, `KNOWN_GOOD`. Each row: `{"kind": "...", "input_built": "<the sheet's shape in words>",
   "invocation": "<the function called>", "result": "<what came back: accepted, or the refusal's code>", "turned_back":
   true|false, "says_what_to_fix": true|false, "claim": "measured"}`. If a kind cannot be run in process (for example pricing
   needs a live source), write `"claim": "not_run"` with `"why_not_run"` and what the code says would happen, with the line.
   For `UNPRICEABLE_HOLDING` say where pricing happens at all (in the door, or later in the resident) with the line.
3. **`door`** -- `{"file_function": "<where an upload is refused today>", "refusal_carrier": "<how a refusal reaches the caller:
   the status, the member, the code vocabulary>", "existing_refusal_codes": ["..."], "where_a_new_refusal_would_go": "..."}`.
4. **`form`** -- `{"file_function": "<the portal code that sends the upload and reads the answer, at origin/DEV>",
   "how_a_refusal_is_shown": "<what the person sees today for a refused upload, with the line>", "shows_what_to_fix": true|false}`.
5. **`proposed_cells`** -- the cells that would BUILD the check, each `{"what": "...", "write_set": ["<paths>"], "risk":
   "LOCAL"|"SERVED"|"WORLD", "depends_on": "...", "open_question": "<anything a ruling must settle first, or null>"}`. Say plainly
   if a kind cannot be turned back at the door at all with what the door can see.
6. **`not_read`** -- a list of what you did not read or could not run.
7. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r13/ONE_ACCOUNT_CHECK_READ.json` with those six
   members plus `"read_at"` and `"tree_head"`. Commit it. Delete your temp sheets.

### ACCEPTANCE

<criterion id="AR132-y-AC1" cell_refs="AR-y-132"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r13/ar13_checks.py y132-read --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y132-READ-OK</expect></criterion>
`AR132-y-AC1`: the record holds at least one recognition signal with its false-positive risk, a row for each of the four kinds
(measured, or not run with the reason), the door's and the form's side, at least one proposed cell, and what was not read.
It grades the record's form, not whether a reading is right.

<criterion id="AR132-y-AC2" cell_refs="AR-y-132" judgment="true"/>
`AR132-y-AC2` (judgment, graded at L9, never by you): the record is enough to cut the build -- each proposed cell could be
issued as written, and no signal is offered that a one-account sheet would commonly trip.

<expected_criteria>AR132-y-AC1 AR132-y-AC2</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only). No product file is changed.
- READ only: everything else. No live call, no push, no deploy. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R13_Y.md</decomp_doc>
<owned_cells>AR-y-132</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR132-y-AC1 AR132-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-132.one-account-check-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-132`. `AR132-y-AC2` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with `method`, `invocation`, `denominator` and a `status_reason`
naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR132-y-AC1,AR132-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 record of another lane (11 file:line reads of the intake folder and the form); NOT seen by the issuer: parse.py itself, the folder's tests and fixtures (the worker reads them). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called; the door is run in process on synthetic sheets. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 outcome of 3 bad kinds against the face; the lens: a recognition signal with no example behind it, or a 'today' behaviour asserted from reading instead of run. The face makes where_seen and a claim word required on each and orders an in-process run per kind. NOT seen: any real uploaded sheet (none may be used; the sheets are synthetic).
lane: the worker's deliverables; read-only on the intake folder and on the portal's refs.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-13 analysis @7542d8555c, item 3.2 ("first a read of how several accounts in one file can be recognised
  at all"). `AR132-y-AC1` base: FAIL as expected (no record).
- The build is cut from this record at the next issuance; `2.0.0_SA_COO~V2` is sent this order's id.
- Seating: slot ~52 is reused; its earlier orders are terminal.
