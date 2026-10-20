# TO IRPT_ANLREQ.TO-AR-y-440.confirm-ticket-stamps-a-create-path-analysis-request-by-its-creator -- C-SWITCH for staff: confirm_ticket also stamps an analysis_request ticket created through /tickets when the ticket's created_by (the token subject) equals the accepting principal, so every Ticket Center filing takes the Opal producer; the dashboard_form rule is unchanged

<to_id>IRPT_ANLREQ.TO-AR-y-440.confirm-ticket-stamps-a-create-path-analysis-request-by-its-creator</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~318</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ99</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-440` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the Opal-generated report, not the YCharts vendor report), C-SWITCH | **depends_on:** CTO msg 11206 item 2 (a MUST cell, ships with or before r34m v2); the issuer's measurement below; AR-g-67 (the existing confirm and stamp)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~318`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-318` (branch `wk-IRPT_ANLREQ-318`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~318 <0.9.0_WK_IRPT_ANLREQ~318@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W318-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-440`, inlined)

*Context and the measured chain.* An Opal staff filing from the Ticket Center was accepted by the door and then refused by the resident at the RECIPE step (run 5C, IB2 receipt `irpt_anlreq_commentary_e2e5c/A_E2E5C.txt`): the vendor recipe `prepare_normalized_upload` in `infra/aws/lambda/investor-reporting/ycharts/generate/normalized_input.py` refuses a holding with no provider receipt, and the request took the VENDOR producer because `producer_for(record)` in `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py` returns "OPAL" only when the accepted principal is on `OPAL_PRODUCER_PRINCIPALS` or the accepted record carries `ticket_confirmed` True. The door stamps `ticket_confirmed` from `confirm_ticket(ticket_id, principal_id)` (`infra/aws/lambda/investor-reporting/ycharts/generate/submission_service.py` lines 148-158), built by `make_confirm_ticket` in `infra/aws/lambda/investor-reporting/ycharts/generate/ticket_confirmation.py`. That confirm is True only for a ticket whose `source` starts with `dashboard_form:` (the client-facing submit route `POST /api/scoped/tickets/submit`) and whose `requester.email` equals the principal. The Ticket Center's staff path creates the ticket through `POST /api/scoped/tickets` (portal `createTicket`), where the ticket service sets `source = body.get("source") or "portal"` (`infra/aws/lambda/ticket_center/lambda_function.py` line 1399; `dashboard_form:` is RESERVED for the submit path and a CREATE body claiming it is rejected) and stores `created_by` = the token subject, ALWAYS (module docstring; item field `"created_by": created_by` at line 635). So no Ticket Center filing is ever stamped.

*The change (CTO msg 11206 item 2, verbatim intent).* `confirm` ALSO returns True for a ticket that `ticket_type == "analysis_request"`, whose `source` does NOT start with `dashboard_form:`, and whose top-level `created_by` string equals the accepted principal, compared case-insensitively after strip, exactly as the existing email comparison is made. Everything else stays: the `TCK-YYYYMMDD-8hex` shape check on the id; ONE consistent GetItem; a source that starts with `dashboard_form:` is decided ONLY by the existing rule (`requester.email` equals the principal), never by `created_by` (on that path `created_by` is the form service's subject); any missing field, any other type and ANY exception is False; no exception text, no logging, no environment read. Change nothing else in the file and no other product file.

*What to do.* (1) Read `ticket_confirmation.py`, `ycharts/generate/tests/test_ticket_stamp.py`, `test_ticket_binding.py` and `test_producer_for_ticket.py` (they pin the current confirm and stamp; a test that pins "source portal -> False" is updated to pin the new rule, keeping its intent, weakening nothing) and baseline them: `cd infra/aws/lambda/investor-reporting && python -m pytest -q --color=no -p no:cacheprovider ycharts/generate/tests/test_ticket_stamp.py ycharts/generate/tests/test_ticket_binding.py ycharts/generate/tests/test_producer_for_ticket.py` (print the summary line). (2) Write the NEW file `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_confirmation_create_path.py` with EXACTLY seven tests, built on an in-memory fake `dynamodb.get_item` as the existing tests do: T1 a CREATE-path analysis_request (`source` "portal", `created_by` equal to the principal) confirms True; T2 the same with the principal's letters in a different case and padded with a space confirms True; T3 `created_by` of another address is False; T4 a missing or empty `created_by` is False; T5 `ticket_type` other than analysis_request is False even with `created_by` equal; T6 the dashboard_form rule is unchanged: `source` "dashboard_form:49financial" with `requester.email` equal is True, and with `requester.email` different is False EVEN when `created_by` equals the principal; T7 a `get_item` that raises, and an id that does not match the ticket-id shape, are False. Run the file against the UNCHANGED code first (T1 and T2 must FAIL: the difference control) and print the summary. (3) Make the change; run the new file (`7 passed`) and the three existing files (all pass). `controls.mutant` = the new code with the `created_by` comparison removed (T3 must FAIL). (4) Write `check_confirm_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~318/` (ruff clean, stdlib only): it lists the files changed since your cut commit (`git log --format=%H --grep='TO-AR-y-440' -1` anchors the cut) and prints `CONFIRM-BOUND-OK files=<n>` only when every changed path is under `infra/aws/lambda/investor-reporting/ycharts/generate/` and n is 2 to 6, otherwise `CONFIRM-BOUND-BAD <paths>` and a non-zero exit. (5) Commit the product files and the workspace files, then the proof instance, and flip on VALID with all three PASS.

---

## ACCEPTANCE

<criterion id="AR440-y-AC1" cell_refs="AR-y-440"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q --color=no -p no:cacheprovider ycharts/generate/tests/test_ticket_confirmation_create_path.py</invocation><expect>^7 passed</expect></criterion>
<criterion id="AR440-y-AC2" cell_refs="AR-y-440"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q --color=no -p no:cacheprovider ycharts/generate/tests/test_ticket_stamp.py ycharts/generate/tests/test_ticket_binding.py ycharts/generate/tests/test_producer_for_ticket.py</invocation><expect>^[0-9]+ passed</expect></criterion>
<criterion id="AR440-y-AC3" cell_refs="AR-y-440"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~318/check_confirm_bound.py</invocation><expect>^CONFIRM-BOUND-OK files=[2-6]$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~318/IRPT_ANLREQ.TO-AR-y-440.confirm-ticket-stamps-a-create-path-analysis-request-by-its-creator.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-440.confirm-ticket-stamps-a-create-path-analysis-request-by-its-creator`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR440-y-AC1,AR440-y-AC2,AR440-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-440</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/ticket_confirmation.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~318/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-440.confirm-ticket-stamps-a-create-path-analysis-request-by-its-creator.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one function in the door Lambda's confirm module and the tests that pin it; a branch, nothing landed, pushed or deployed (the release is a later order).
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the confirm module, the submission service (lines 148-158) and the ticket service CREATE path against this cell; the lens: a created_by compared to a principal on the dashboard_form path (forbidden: there created_by is the form service), a widening to any ticket type (analysis_request only), an exception that leaks text, a test weakened to pass (the difference control runs the new file on the old code and T1, T2 must fail). NOT seen (blind): the live ticket rows; denominator: three criteria.
</preflight>
