# TO-AR-tf-74 -- FWD-4 build: the draft store's fail op writes through G2's keyed writer (AR-tf-74, round 49, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tf-74</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~228</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tf-74` (`decompositions/IRPT_ANLREQ_DECOMP_R49_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** `2.0.0_SA_COO~G2`'s TO-AR-g-109 (merged, bc0e7e96c4)

---

## WORKER FACE

### THE CELL

`AR-tf-74`: "FWD-4 build: the draft store's fail op writes through G2's keyed writer." FWD-4 says a broken hop never silently stops the request. The CTO ruled (PRD v0.21, C-HOP-FAILURE) that the ticket READS the failure through the existing status route and the silent hops write one set-once `hop_failure` on the job row; this cell is the commentary hop's part.

**The contract all three cells serve** (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` row C-HOP-FAILURE, v0.21; ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`; `2.0.0_SA_COO~G2`'s msg 8961): the commentary draft hop writes ONE set-once value `hop_failure` = `{hop, code, at}` on the request's JOB row in table `irpt-jobs` (key `{tenant, job=<request_id>}`), never overwriting the job state. The writer is `DynamoGenerationStore.mark_hop_failure(job_id, hop, code, at)` in `infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py` (`2.0.0_SA_COO~G2`'s order TO-AR-g-109, NOT merged at your base): it returns True when written, False when `hop_failure` was already set (a no-op), and raises `LeaseRefused("HOP_FAILURE_INVALID")` for a hop or code outside its closed sets. For the hop `COMMENTARY` the closed codes are exactly `COMMENTARY_DRAFT_FAILED` and `COMMENTARY_DRAFT_REFUSED`. `at` is UTC `YYYY-MM-DDTHH:MM:SSZ`. THE `fail` OP (cell AR-tf-71 builds it, AR-tf-72 calls it): the draft store's invoke accepts the event `{"op": "fail", "tenant": <firm id>, "request_id": <id>, "hop": "COMMENTARY", "code": <one of the two codes>}` and answers `{"status": "OK", "hop_failure_written": true|false}` or `{"status": "REFUSED", "reason": "INVALID_REQUEST"|"UNAVAILABLE"}`. No draft body travels with it.

**What to build.** AR-tf-71 (merged) built the `fail` op with an injected jobs factory and left the LIVE factory `_hop_failure_jobs` (near the end of `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py`) as a stub that answers UNAVAILABLE, because the writer then needed `composition_sha256`. `2.0.0_SA_COO~G2` merged the sha-free writer (`2.0.0_SA_COO~G2` msg 9024, commit bc0e7e96c4): `mark_hop_failure_keyed(client, tenant, job_id, hop, code, at, table="irpt-jobs")` in `infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py` (READ it first; it validates the closed sets itself and raises `LeaseRefused("HOP_FAILURE_INVALID")`, returns True when it wrote and False when the condition failed, and does one `update_item` with no read). DO: (1) replace the stub so `compose_ports()` supplies a live `jobs` factory `jobs(tenant, request_id)` that returns a port with `mark_hop_failure(job_id, hop, code, at)` calling `mark_hop_failure_keyed(clients["dynamodb"], tenant, job_id, hop, code, at, table=<the jobs table name compose_ports already reads>)`. Import `mark_hop_failure_keyed` lazily inside the factory from `ycharts.generate.durable_job` (the module already extends the path for its other source folders; follow the same pattern). Keep the fake-port contract AR-tf-71's tests use unchanged (all of `test_hop_failure_fail_op.py` stays green). Remove the stub's docstring that says it is unwired. (2) A `LeaseRefused` from the real writer is already answered `INVALID_REQUEST` by the op; a `False` answers `hop_failure_written` false. (3) Tests in `infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_live_writer.py` (a fake DynamoDB client object recording `update_item` calls; named `test_hop_failure_<what>`): the OK path through the REAL `mark_hop_failure_keyed` issues exactly one `update_item` with `TableName` the jobs table, `Key` `{tenant, job=<request_id>}` (strings), `UpdateExpression` `SET hop_failure = :value`, the ConditionExpression `attribute_exists(#job) AND attribute_not_exists(hop_failure)`, and the value Map `{hop, code, at}`, with NO `get_item` and NO second call; a `ConditionalCheckFailedException` answers `hop_failure_written` false; any other client error does not become a success; another firm's request and an absent request never reach the client (zero `update_item` calls); a bad code never reaches the client; the table name follows the `JOBS_TABLE_ENV` environment setting. (4) REPORT, in your final message and not as an edit: whether `infra/aws/lambda/ci/lambda-source-map.json` entry `irpt-commentary-draft-store-lambda` (near line 7142) packages `ycharts/generate/durable_job.py` with the function's other members (read the entry and the build script it names); if it does not, file an OBSERVATION row naming the entry and the missing member, and do not edit the map.

**Files you write (the only files you may write besides your proof, the surprise channel and this order):**

infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_live_writer.py

Use plain synthetic names in tests (`firm-a`, `req-1`); no real client name, no credential, no secret. ASCII only in code and log lines. Do not edit any other file.

### ACCEPTANCE

<criterion id="AR74-tf-AC1" cell_refs="AR-tf-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 5 --prefix=test_hop_failure_ infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_live_writer.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR74-tf-AC1` -- the test file exists, every test function is named `test_hop_failure_*`, the tests pass and at least 5 pass. Dry-run at box/dell2 c71e9b0310: `R46-TESTS-FAIL absent: ...` -- FAIL as expected. The checker's `--self-test` reads `R46-SELFTEST-OK`.

<expected_criteria>AR74-tf-AC1</expected_criteria>

## BOUNDS

- **Grant.** The files listed, this order's file, your deliverables folder, the surprise channel. No other code, no other test.
- **No network, no AWS, no secret, no deploy, no apply.** Fakes only.
- **Refusal clause.** If a cited line is not what this order says, build for what the code does and file a surprise row; if a needed folder is outside your cone, file a `BLOCKING` row naming it and stop on that part.
- **No alarms, monitors or notifications.** A failure is a stored code the page reads.

<paths>
infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_live_writer.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R49_TX.md</decomp_doc> (round 49, workstream ~TX), cell `AR-tf-74`.
<owned_cells>AR-tf-74</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR74-tf-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~228/IRPT_ANLREQ.TO-AR-tf-74.draft-store-fail-op-live-writer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR74-tf-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the files, the count passed, for each guard in your code the test that fails without it (remove it in a scratch copy), the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new op and its callers inside one function's source; the consumers are named in the contract above. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change in this cell (the grant is AR-tf-73's).
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates and its proof instance. Traps named for the worker: a fake client that accepts any update_item shape so the real writer's condition is never checked; a request of another firm that still reaches the client; a ConditionalCheckFailed read as a success or any other client error swallowed; breaking the fake-port tests of AR-tf-71.
</preflight>

- Cut on the CTO's rulings: FWD-4 read-not-write (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`, msg 8906), PRD v0.21 signed (msg 8924), the narrow grant (A) (msg 8970). Risk WORLD. WORLD by the path floor (`<paths>` under `infra/`, spine v3.19 L6); the work is source and tests, no deploy.
- Base: `AR74-tf-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 c71e9b0310, run by the issuer before the cut.
