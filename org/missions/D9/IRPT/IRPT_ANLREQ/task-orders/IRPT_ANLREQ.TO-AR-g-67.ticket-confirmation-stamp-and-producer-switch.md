# TO-AR-g-67 -- C-SWITCH, placement A: the accept step stamps a server-owned `ticket_confirmed` after one read of the ticket table, and `producer_for` admits a confirmed record; source and tests only, no grant, no deploy

<to_id>IRPT_ANLREQ.TO-AR-g-67</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~179</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-67` (`decompositions/IRPT_ANLREQ_DECOMP_R10_G.md`) |
**outcome_ref:** FWD-1 (C-SWITCH, hop 8) | **depends_on:** `AR-g-53` (merged `286f7c048d`, the design read this cell implements).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~179`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-179` (branch `wk-IRPT_ANLREQ-179`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~179 <0.9.0_WK_IRPT_ANLREQ~179@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W179-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you edit or add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.

### Read first (under `C:/dev/wk-irpt-anlreq-179/`)

- The design this cell implements: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/r7/C_SWITCH_DESIGN.json` (q1, q3, q4.A and `q4.forgeability` especially).
- Under `infra/aws/lambda/investor-reporting/`: `ycharts/generate/submission_service.py` (the constructor at line 24 and `submit` at lines 104-160), `ycharts/generate/acceptance.py` (`accept`, lines 106-145; see how `ticket_id` and
  `commentary_requested` are carried at lines 136-139), `ycharts/generate/submission.py` (`PUBLIC_FIELDS`, line 16: a client may send only these), `ycharts/generate/prospect_submission.py` (the factory that builds the service, about line 110),
  `reports/generate_installed.py` (`compose_ports`, about lines 275-350, and `RoutedSubmissionService._prospect`, about line 201), `ycharts/generate/resident_worker.py` (`producer_for`, about lines 168-180) and `reports/resident_installed.py` (`make_opal_stores`, about lines 258-299, which calls `producer_for`).
- The ticket service's item shape (read only): `infra/aws/lambda/ticket_center/lambda_function.py` lines 600-625 (`_new_item`: `ticket_type`, `source`, `requester`) and 1290-1300, 1340-1346 (the `dashboard_form:` source).
- Tests to mirror: `ycharts/generate/tests/test_commentary_requested_member.py` (how a new accepted-record member was added and tested) and `ycharts/generate/tests/test_producer_actor.py`.

### THE CELL (`AR-g-67`, inlined)

An Opal staff user's Analysis Request must reach the Opal report engine without adding any human principal to the allow list. The accept step already holds both the verified owner and the client's `ticket_id`. It will confirm
the ticket against the ticket table (one `GetItem`) and write a SERVER-OWNED boolean on the accepted record; the resident's `producer_for` then also admits a record carrying it. The IAM grant that lets the Lambda read the ticket table is NOT in this
cell (a later CloudOps act under a pair, after the role's identity is read): until it exists the read fails, the record stays unstamped and the request goes to the YCharts path exactly as today. Six files change; nothing is deployed.

**A. NEW file `ycharts/generate/ticket_confirmation.py`.** `make_confirm_ticket(dynamodb, table_name)` returns a function `confirm(ticket_id, principal_id) -> bool`. `table_name` that is not a non-blank `str` raises `ValueError("TICKET_TABLE")`.
`confirm` returns `True` ONLY when all of these hold, and `False` otherwise; it never raises and puts no exception text anywhere:
  1. `ticket_id` is a `str` that fully matches `TCK-[0-9]{8}-[0-9a-f]{8}`, and `principal_id` is a non-blank `str`; if not, return False WITHOUT any read;
  2. exactly one call `dynamodb.get_item(TableName=table_name, Key={"ticket_id": {"S": ticket_id}}, ConsistentRead=True)` (the low-level typed client) returns an `Item`;
  3. `Item["ticket_type"]["S"] == "analysis_request"`;
  4. `Item["source"]["S"]` starts with `dashboard_form:` (the only creation path whose requester email is server-derived);
  5. `Item["requester"]["M"]["email"]["S"]`, lower-cased, equals `principal_id` stripped and lower-cased (the filer is the accepted principal).
  Any exception or missing key -> False. The module is pure: it imports only `re` (and `__future__`/`typing`), opens no connection of its own and reads no environment variable.

**B. `ycharts/generate/acceptance.py`, `accept`.** Add a keyword parameter `ticket_confirmed=False` at the END of the signature. A NEW record gets `record["ticket_confirmed"] = True` ONLY when `ticket_confirmed is True`; otherwise the key is absent (not False). A prior
record is returned exactly as stored. Do NOT add `ticket_confirmed` to `submission.py`'s `PUBLIC_FIELDS`: a client that sends it must still be refused `UNKNOWN_OR_SERVER_OWNED_FIELD`. Mirror every place the code carries or validates `commentary_requested` on the record so the new key is
carried the same way (find them by reading `test_commentary_requested_member.py` and the readers it exercises).

**C. `ycharts/generate/submission_service.py`.** The constructor gains an optional keyword `confirm_ticket=None`. In `submit`, for a NEW acceptance only (the branch where `prior is None`): `confirmed = False`; if the browser body holds `ticket_id` and `self.confirm_ticket` is callable, `confirmed = (self.confirm_ticket(browser["ticket_id"], owner["principal_id"]) is True)`
inside a `try`/`except Exception` that leaves `confirmed` False (the request is still accepted unstamped); pass `ticket_confirmed=confirmed` to `self.acceptance.accept(...)`. Every existing caller that does not pass `confirm_ticket` behaves as today.

**D. Wiring.** `ycharts/generate/prospect_submission.py` (the factory) accepts an optional `confirm_ticket` and hands it to the `SubmissionService` it builds; `reports/generate_installed.py` builds it in `compose_ports`/`_prospect` ONLY when the environment names a table:
`environ.get("IRPT_TICKETS_TABLE")` non-blank and a low-level DynamoDB client is among the composed clients, then `make_confirm_ticket(client, table)`; otherwise `None`. No default table name is typed. The custody submission path (`custody_submission.py`) is untouched.

**E. `ycharts/generate/resident_worker.py`, `producer_for`.** Return `"OPAL"` when the accepted principal is on `OPAL_PRODUCER_PRINCIPALS` (as today) OR `record.get("ticket_confirmed") is True`; otherwise `"YCHARTS"`. It still reads only the accepted record. The list is unchanged (do not remove the synthetic address). The docstring and the list's comment say why a confirmed record is admitted.
`make_opal_stores` in `reports/resident_installed.py` already calls `producer_for`; it needs no edit, and a test pins that it uses the same choice.

**F. Tests.** Two NEW files with EXACTLY these test function names (the checker looks for each name), offline:
- `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_stamp.py`: `test_accept_records_ticket_confirmed_true_only_when_the_service_says_true`, `test_client_cannot_send_ticket_confirmed`,
  `test_confirm_failure_leaves_the_record_unstamped_and_the_request_accepted`, `test_replay_returns_the_prior_record_unchanged`.
- `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_producer_for_ticket.py`: `test_producer_for_admits_a_confirmed_record`, `test_producer_for_refuses_an_unconfirmed_ticket_record`,
  `test_producer_for_keeps_the_allow_list`, `test_opal_stores_uses_the_same_choice`.
(`ticket_confirmation.py` needs no test file of yours: the checker asks it twelve direct cases.)

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR67-g-AC1" cell_refs="AR-g-67"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g67_checks.py g67</invocation><expect>^AR-G67-OK</expect></criterion>

<criterion id="AR67-g-AC2" cell_refs="AR-g-67"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g67_checks.py regress</invocation><expect>^AR-G67-REGRESS-OK</expect></criterion>

<expected_criteria>AR67-g-AC1,AR67-g-AC2</expected_criteria>

- AC1 imports `ticket_confirmation` and asks it twelve direct cases with a fake DynamoDB client, then checks the eight named tests exist in your two new files and runs them (0 failed, all eight passed). At base it FAILs.
- AC2 runs seven existing test files one at a time (acceptance actor, the `commentary_requested` member, the ready-signal ticket gate, the producer actor, the Opal thread integration, the resident installer, the generate installer) and requires each to pass and 65 or more tests in all. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. No Terraform, no IAM, no deploy, no AWS call, no HTTP, no installs. Do not edit `submission.py`, `custody_submission.py`, the portal or any other file.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/ticket_confirmation.py
infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py
infra/aws/lambda/investor-reporting/ycharts/generate/submission_service.py
infra/aws/lambda/investor-reporting/ycharts/generate/prospect_submission.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/reports/generate_installed.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_stamp.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_producer_for_ticket.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~179/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-67.ticket-confirmation-stamp-and-producer-switch.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R10_G.md</decomp_doc> round 10, workstream ~G, cell `AR-g-67`.
<owned_cells>AR-g-67</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR67-g-AC1, AR67-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~179/IRPT_ANLREQ.TO-AR-g-67.ticket-confirmation-stamp-and-producer-switch.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-67`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR67-g-AC1,AR67-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- for A to E, the function and lines changed;
- where you found `commentary_requested` carried on the record, and that you mirrored it;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `accept` is called by the prospect and custody submission paths; the new keyword defaults to False so every caller and every stored record is unchanged; `producer_for` gains one OR clause reachable only through the new server-owned key; the confirmation function is new and called by nothing until the wiring finds an environment table name, which no deployed Lambda sets today. NOT seen: the deployed bytes, the Lambda role and its environment; this cell neither reads nor changes them.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change in this cell. The ticket-table read is a NEW grant ruled for a later CloudOps cell: `generate.tf` after line 120 per the design record is NOT adopted yet, because that statement list reads as the generation job's role, not the acceptance Lambda's; the role's identity is read first.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or wire change; `ticket_confirmed` is never accepted from a client. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the design record's forgeability rule. Traps: a client sending `ticket_confirmed` (PUBLIC_FIELDS unchanged); a confirmation that passes for a ticket another person filed (clause 5) or one a service created with the staff user's email (clause 4); a read failure that blocks the request (it only leaves it unstamped); a stamp of False written into the record (absent instead); a replay that re-confirms and changes a stored record; an exception text in a log or a result. The checker feeds a green arm (a reference build passes all twelve direct cases and the eight named tests) and a base arm (the tree without the module fails).
</preflight>

- Cut on the AR-g-53 record (recommendation A) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed or granted. Base: `AR67-g-AC1` FAILs as expected; `AR67-g-AC2` PASSes as expected (65 tests).
- After it merges, the switch still needs, in order: the role-identity read and the one `GetItem` grant on the ticket table (CloudOps, a pair with the CTO's half), the `IRPT_TICKETS_TABLE` environment value, and the release of the `irpt-ycharts-generate` package and the resident tarball.
