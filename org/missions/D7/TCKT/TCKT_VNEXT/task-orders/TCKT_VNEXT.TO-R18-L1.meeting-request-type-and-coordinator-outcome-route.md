# TO TCKT_VNEXT.TO-R18-L1 -- BUILD the meeting_request type definition and the coordinator's confirm-or-propose route in the ticket service (source and tests only)

<to_id>TCKT_VNEXT.TO-R18-L1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~41</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a Lambda source path; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `R18-mt-1` (`decompositions/TCKT_VNEXT_DECOMP_R18.md`) | **outcome_ref:** FWD-11 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~41`.
- **Worktree:** `C:/dev/wk-tckt-vnext-41` (branch `wk-TCKT_VNEXT-41`), provisioned by the issuer. Work and commit only there, with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~41 <0.9.0_WK_TCKT_VNEXT~41@opal.agent>" -F <msgfile> -- <paths>`. If a `portal`
  folder exists in the worktree it is a separate repository: never touch or stage it.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `TCKT_VNEXT-D2-W41-S<k>` (take the next free `<k>`). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before
  its commit (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every
  non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call of any kind: no AWS, no network, no
  mail, no deploy, no apply, no Terraform (`tests/conftest.py` refuses a real call). Scratch outside the product tree.

### THE CELL (`R18-mt-1`, inlined) -- BUILD ONLY. Nothing is deployed, applied or invoked.

*PRD v0.6 C-MEETING-REQUEST: an Opal staff person files a Meeting Request (firm, who, purpose, up to three proposed times); the ticket
lands in the meeting coordinator's queue (`jeanette@opalinvest.com`); the coordinator CONFIRMS one of the proposed times or PROPOSES other
times on the ticket; the filer reads the outcome on the same ticket. In-house, no Calendly, and NO mail or notification is sent.*

In `infra/aws/lambda/ticket_center/lambda_function.py` (read first: `TYPE_DEFINITIONS` about lines 88-128, `_validate_answers` about 704,
`create_ticket` about 1218, `get_ticket` about 1402, `claim_ticket` about 1427 for the conditional-update style, `_event_row` about 437,
the `MATRIX` of actions and `lambda_handler` about 1889):

1. **The definition.** `meeting_request` keeps `label` `Meeting Request` and `attachment` None, and gains the questions: `firm` (kind
   `firm`, required), `who` (text, required), `purpose` (text, required), `proposed_time_1` (text, required), `proposed_time_2` (text,
   optional), `proposed_time_3` (text, optional). CREATE then validates them through the existing `_validate_answers` path with the same
   firm check every typed ticket gets (`_create_firm_allowed`); a ticket with no `who` or no first time is refused 400. The other
   untyped types (`service_request`, `other`) are unchanged. The four existing types keep their exact rows.
2. **The route.** `POST /api/scoped/tickets/{ticketId}/meeting` (a new function `meeting_ticket(event, tid)`, wired in `lambda_handler`
   beside `commentary_sent`, and a new `MATRIX` action `MEETING` permitted to the INTERNAL class ONLY). Body, exactly one of:
   `{"action":"confirm","time":"<string>"}` or `{"action":"propose","times":["<string>", ...]}` (1 to 3 non-empty strings, each at most
   200 characters); any other member or shape: 400. Rules, in this order, each with its own answer:
   - not INTERNAL: 403 (the matrix); the caller's email (`actor["email"]`) must be in the ticket's `routing.primary` (the coordinator),
     else 403 with a message that names no one;
   - ticket not found or outside the caller's profile scope: 404 (read `get_ticket` and use the SAME lookup and scope test);
   - ticket type not `meeting_request`: 409; ticket `completed`: 409;
   - `confirm`: `time` must equal (after stripping) one of the ticket's `answers.proposed_time_1/2/3`, else 400;
   - the write is ONE conditional `update_item` (condition: status is not `completed` AND `ticket_type` is `meeting_request`; a failed
     condition is a 409 "ticket changed under the write") that sets `meeting = {"status": "confirmed" (confirm) or "rescheduled" (propose),
     "time": <the confirmed string, or null on propose>, "proposed_times": <[] on confirm, the list on propose>, "by": <email>, "at":
     <now iso>}` and appends ONE event row (`meeting_confirmed` or `meeting_proposed`) with `_event_row`;
   - it changes NOTHING else: not `status`, not `assignee`, no mail, no notice (`notify_*` are never called). `complete` stays the
     existing route. A second call overwrites `meeting` and appends another event row.
   - 200 returns `{"ticket_id": tid, "meeting": {...}}`.
3. **Reads.** `get_ticket` already returns the whole item; the list route must also carry the `meeting` member to an INTERNAL caller (read
   `list_tickets`; if it projects named fields, add `meeting`). A CLIENT caller's projection (`_client_projection`) is NOT changed.
4. **Tests.** The new file `infra/aws/lambda/ticket_center/tests/test_meeting_request.py` (copy the style of the existing files in
   `tests/`; a fake table, no AWS) names one test per case: CREATE with all answers works; CREATE missing `who`, `purpose` or the first time
   is 400; CREATE with a firm outside the caller's scope is refused as for every typed ticket; the coordinator CONFIRMS a time and the
   ticket carries `meeting.status` `confirmed`, the time, `by` and `at`, plus exactly one new event row, and `status` still `open`;
   confirm of a time that is not one of the three answers is 400; the coordinator PROPOSES two times (`rescheduled`, `time` null,
   the list stored); propose with 0 or 4 times, a non-string or a 201-character string is 400; an INTERNAL human who is not in
   `routing.primary` is 403; a CLIENT caller and a service subject are 403; another ticket type is 409; a `completed` ticket is 409;
   the conditional-write failure is 409; no `notify_*` function is called on any path (a spy); the list route carries `meeting` to an
   INTERNAL caller. Set the routing in the test's environment so `jeanette@opalinvest.com` is the coordinator.
5. Edit an existing test or `conftest.py` ONLY where a fixture needs the new action or the new definition (`tests/test_authz_matrix.py`
   enumerates actions); list each such edit in your report with the old and the new assertion. No existing assertion about another type
   or another action may change.
6. **Write `deliverables/0.9.0_WK_TCKT_VNEXT~41/mutant_check.py`** (AC2 below) and a short `R18_L1_RECORD.json`: the lines you changed, the
   test counts, the before-arm (the new tests run on the base: every case FAILS), what a coordinator can and cannot do, `not_read`.

### ACCEPTANCE

<criterion id="R18L1-AC1" cell_refs="R18-mt-1"><invocation>python -m pytest C:/dev/wk-tckt-vnext-41/infra/aws/lambda/ticket_center/tests/test_meeting_request.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`R18L1-AC1`: the new test file passes with every case of step 4 named in a test, and no failures or errors. Also run the whole
`infra/aws/lambda/ticket_center/tests/` folder once and record the counts in your record (a drain check; the issuer re-runs it).

<criterion id="R18L1-AC2" cell_refs="R18-mt-1"><invocation>python C:/dev/wk-tckt-vnext-41/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~41/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R18L1-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `lambda_function.py` to a scratch folder OUTSIDE the product
tree with the coordinator test (`actor["email"]` in `routing.primary`) removed, runs the new test file against the copy, and prints
`MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R18L1-AC3J" cell_refs="R18-mt-1" judgment="true"/>
`R18L1-AC3J` (judgment, graded at L9, never by you): only the coordinator can record an outcome, the outcome changes nothing but the
`meeting` member and one event row, no mail or notice is sent, and a refusal reveals nothing about tickets outside the caller's scope.

<expected_criteria>R18L1-AC1 R18L1-AC2 R18L1-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~41/` and this order's file
  (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- **Shared file:** `lambda_function.py` is also edited by the next order of your queue (`TO-R18-L2`, the trade type). Touch only the
  meeting definition, `meeting_ticket`, its `MATRIX` action and its router line, so the two merge cleanly.
- READ only: everything else, including `infra/aws/terraform/` (the route and the routing entry are another cell's; the wire contract is
  `decompositions/TCKT_VNEXT_DECOMP_R18.md`, section WIRE CONTRACT, item 1).

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md</decomp_doc>
<owned_cells>R18-mt-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~41/TCKT_VNEXT.TO-R18-L1.meeting-request-type-and-coordinator-outcome-route.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R18-L1`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R18L1-AC1,R18L1-AC2,R18L1-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source in a worker worktree; nothing is deployed, applied or invoked. The release is another cell's (`R18-mt-4`).
comp-routes: DECLARED-NOT-APPLICABLE -- the API route entry is Terraform SOURCE in `TO-R18-TR2`; this cell adds the handler only. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler reads and writes the ticket table it already uses.
comp-adversary: RUN -- by reading C-MEETING-REQUEST and C-FENCE against this cell; the lens: a route any internal person can call, an outcome that completes or reassigns the ticket, a refusal that tells another firm's ticket apart from a missing one, a send. The cell requires the coordinator-only check, the one conditional write, no send, and a mutant that fires. NOT seen: the live users table row of the coordinator (the CTO confirmed it in `opal-users-v2`) and the live routing config.
</preflight>

---

## RECORD FACE

- Cut on the CTO's re-seat msg 7806 and PRD v0.6 @c578883de8 (ratified half SIGNED by `3.0.0_SA_CVO~DELL2`). First of the two orders in slot 41's queue; round 18 chain A with `TO-R18-L2`. Base: `R18L1-AC1` and `R18L1-AC2` FAIL as expected (no test file, no checker file).
- It ships in the release order `TO-R18-REL` after the Terraform source of `TO-R18-TR2`; the DEV run is `TO-R18-RUN-MT`.
