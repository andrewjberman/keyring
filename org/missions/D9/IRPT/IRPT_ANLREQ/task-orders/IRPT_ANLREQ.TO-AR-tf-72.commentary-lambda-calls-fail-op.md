# TO-AR-tf-72 -- FWD-4 build: the commentary function reports its failed draft to the draft store's `fail` op (AR-tf-72, round 48, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tf-72</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~226</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tf-72` (`decompositions/IRPT_ANLREQ_DECOMP_R48_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none (the writer `mark_hop_failure` is injected or faked; TO-AR-g-109 is `2.0.0_SA_COO~G2`'s)

---

## WORKER FACE

### THE CELL

`AR-tf-72`: "FWD-4 build: the commentary function reports its failed draft to the draft store's `fail` op." FWD-4 says a broken hop never silently stops the request. The CTO ruled (PRD v0.21, C-HOP-FAILURE) that the ticket READS the failure through the existing status route and the silent hops write one set-once `hop_failure` on the job row; this cell is the commentary hop's part.

**The contract all three cells serve** (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` row C-HOP-FAILURE, v0.21; ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`; `2.0.0_SA_COO~G2`'s msg 8961): the commentary draft hop writes ONE set-once value `hop_failure` = `{hop, code, at}` on the request's JOB row in table `irpt-jobs` (key `{tenant, job=<request_id>}`), never overwriting the job state. The writer is `DynamoGenerationStore.mark_hop_failure(job_id, hop, code, at)` in `infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py` (`2.0.0_SA_COO~G2`'s order TO-AR-g-109, NOT merged at your base): it returns True when written, False when `hop_failure` was already set (a no-op), and raises `LeaseRefused("HOP_FAILURE_INVALID")` for a hop or code outside its closed sets. For the hop `COMMENTARY` the closed codes are exactly `COMMENTARY_DRAFT_FAILED` and `COMMENTARY_DRAFT_REFUSED`. `at` is UTC `YYYY-MM-DDTHH:MM:SSZ`. THE `fail` OP (cell AR-tf-71 builds it, AR-tf-72 calls it): the draft store's invoke accepts the event `{"op": "fail", "tenant": <firm id>, "request_id": <id>, "hop": "COMMENTARY", "code": <one of the two codes>}` and answers `{"status": "OK", "hop_failure_written": true|false}` or `{"status": "REFUSED", "reason": "INVALID_REQUEST"|"UNAVAILABLE"}`. No draft body travels with it.

**What to build.** In `data/transcripts/scripts/commentary/lambda_handler.py` (the COMMENTARY-POST outcomes `POSTED`, `ALREADY_SET`, `REFUSED`, `FAILED`, `NO_TICKET`, the `commentary refused queue message` and `commentary failed` handlers, around the lines the round-45 record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~213/FWD4_PER_HOP_FAILURE_MAP.md` cites as hops 10 and 11: `lambda_handler.py:308`, `:330`, `:356`, `:366`): after the request id is known, each of these failures calls the draft store's `fail` op (use the SAME invoke client the function already uses to store the draft; read how `persist` or the store call is made and reuse it; the event is the contract's): `COMMENTARY_DRAFT_REFUSED` when the queue body is refused WITH a usable request id and tenant, or when the ticket post is refused (`draft_post_refused`); `COMMENTARY_DRAFT_FAILED` when the ticket post failed (`draft_post_failed`) or the draft step raised (`commentary failed`). No `fail` call for: a success (`POSTED`, `ALREADY_SET`, `NO_TICKET`), a message with no usable request id (nothing to name), and the configured no-vendor-word stop (a deliberate stop, not a failure; say so in a row). A failure of the `fail` call itself NEVER changes the function's result and NEVER raises: it is logged as one line `HOP-FAILURE-REPORT-FAILED request_id=<id> error=<type name>` (no message text, no address), and the function's own failure handling (batchItemFailures, results entries, the dead-letter path) is byte-for-byte as before. The log line `HOP-FAILURE-REPORTED request_id=<id> hop=COMMENTARY code=<code> written=<true|false>` is printed on success. ASCII only. Tests in `data/transcripts/scripts/tests/test_hop_failure_calls.py` (fake invoke client; named `test_hop_failure_<what>`): each of the four failures makes exactly one `fail` call with the right code and the contract's event; the three non-failures make none; a raising `fail` call leaves the result and the dead-letter behaviour unchanged and logs the one failure line; the recorded events contain no draft text. Reuse the existing tests' harness in the same folder.

**Files you write (the only files you may write besides your proof, the surprise channel and this order):**

data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/tests/test_hop_failure_calls.py

Use plain synthetic names in tests (`firm-a`, `req-1`); no real client name, no credential, no secret. ASCII only in code and log lines. Do not edit any other file.

### ACCEPTANCE

<criterion id="AR72-tf-AC1" cell_refs="AR-tf-72"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 6 --prefix=test_hop_failure_ data/transcripts/scripts/tests/test_hop_failure_calls.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR72-tf-AC1` -- the test file exists, every test function is named `test_hop_failure_*`, the tests pass and at least 6 pass. Dry-run at box/dell2 23ee4c175d: `R46-TESTS-FAIL absent: ...` -- FAIL as expected. The checker's `--self-test` reads `R46-SELFTEST-OK`.

<expected_criteria>AR72-tf-AC1</expected_criteria>

## BOUNDS

- **Grant.** The files listed, this order's file, your deliverables folder, the surprise channel. No other code, no other test.
- **No network, no AWS, no secret, no deploy, no apply.** Fakes only.
- **Refusal clause.** If a cited line is not what this order says, build for what the code does and file a surprise row; if a needed folder is outside your cone, file a `BLOCKING` row naming it and stop on that part.
- **No alarms, monitors or notifications.** A failure is a stored code the page reads.

<paths>
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/tests/test_hop_failure_calls.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R48_TX.md</decomp_doc> (round 48, workstream ~TX), cell `AR-tf-72`.
<owned_cells>AR-tf-72</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR72-tf-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~226/IRPT_ANLREQ.TO-AR-tf-72.commentary-lambda-calls-fail-op.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR72-tf-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the files, the count passed, for each guard in your code the test that fails without it (remove it in a scratch copy), the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new op and its callers inside one function's source; the consumers are named in the contract above. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change in this cell (the grant is AR-tf-73's).
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates and its proof instance. Traps named for the worker: a fake writer that accepts any hop or code, so the closed-set refusal is never exercised; a fail call that can change the function's own result or raise; a grant statement that leaks PutItem, GetItem, Query or Scan on the jobs table or touches S1 to S5; a request of another firm that still reaches the writer; the real DynamoGenerationStore not being in the draft-store zip, which this cell does not fix but must report.
</preflight>

- Cut on the CTO's rulings: FWD-4 read-not-write (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`, msg 8906), PRD v0.21 signed (msg 8924), the narrow grant (A) (msg 8970). Risk LOCAL.
- Base: `AR72-tf-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 23ee4c175d, run by the issuer before the cut.
