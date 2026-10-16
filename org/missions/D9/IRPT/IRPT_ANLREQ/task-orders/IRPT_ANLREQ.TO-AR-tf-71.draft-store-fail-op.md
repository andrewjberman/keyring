# TO-AR-tf-71 -- FWD-4 build: the draft store's `fail` op writes the commentary hop_failure (AR-tf-71, round 48, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tf-71</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~225</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tf-71` (`decompositions/IRPT_ANLREQ_DECOMP_R48_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none (the writer `mark_hop_failure` is injected or faked; TO-AR-g-109 is `2.0.0_SA_COO~G2`'s)

---

## WORKER FACE

### THE CELL

`AR-tf-71`: "FWD-4 build: the draft store's `fail` op writes the commentary hop_failure." FWD-4 says a broken hop never silently stops the request. The CTO ruled (PRD v0.21, C-HOP-FAILURE) that the ticket READS the failure through the existing status route and the silent hops write one set-once `hop_failure` on the job row; this cell is the commentary hop's part.

**The contract all three cells serve** (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` row C-HOP-FAILURE, v0.21; ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`; `2.0.0_SA_COO~G2`'s msg 8961): the commentary draft hop writes ONE set-once value `hop_failure` = `{hop, code, at}` on the request's JOB row in table `irpt-jobs` (key `{tenant, job=<request_id>}`), never overwriting the job state. The writer is `DynamoGenerationStore.mark_hop_failure(job_id, hop, code, at)` in `infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py` (`2.0.0_SA_COO~G2`'s order TO-AR-g-109, NOT merged at your base): it returns True when written, False when `hop_failure` was already set (a no-op), and raises `LeaseRefused("HOP_FAILURE_INVALID")` for a hop or code outside its closed sets. For the hop `COMMENTARY` the closed codes are exactly `COMMENTARY_DRAFT_FAILED` and `COMMENTARY_DRAFT_REFUSED`. `at` is UTC `YYYY-MM-DDTHH:MM:SSZ`. THE `fail` OP (cell AR-tf-71 builds it, AR-tf-72 calls it): the draft store's invoke accepts the event `{"op": "fail", "tenant": <firm id>, "request_id": <id>, "hop": "COMMENTARY", "code": <one of the two codes>}` and answers `{"status": "OK", "hop_failure_written": true|false}` or `{"status": "REFUSED", "reason": "INVALID_REQUEST"|"UNAVAILABLE"}`. No draft body travels with it.

**What to build.** In `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py`: (1) `parse_request` admits the op `fail` (today it admits `put` and `get_ref`) with the contract's fields; any other hop than `COMMENTARY`, any code outside the two, or a missing field raises `DraftStoreRefused("INVALID_REQUEST")` BEFORE any read or write. (2) `store()` handles `fail` after the same `_resolve_record` binding the other ops use, so another firm's request or an absent one is `UNAVAILABLE` (the same answer for both), and a record that does not belong to the hinted tenant never reaches the write. (3) The write goes through an injected `jobs` port with the method `mark_hop_failure(job_id, hop, code, at)`; `handle()` passes the port from the composed ports; `compose_ports()` adds `"jobs"` built as `DynamoGenerationStore` (import it lazily INSIDE the function, from `ycharts.generate.durable_job`, with `client=clients["dynamodb"]`, `tenant=<the resolved tenant>`, `request_id=<id>`; read the class's constructor in your cone, and `_extend_path()` already adds the source folders). `at` comes from the injected clock (`time.gmtime`), formatted `YYYY-MM-DDTHH:MM:SSZ`. (4) A `LeaseRefused` from the port is answered `REFUSED` `INVALID_REQUEST`, never a raise. `put` and `get_ref` behave exactly as today (their tests stay green). Tests in `infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_fail_op.py`, a fake `jobs` port recording its calls, named `test_hop_failure_<what>`: the OK path writes once with the resolved tenant and the closed hop/code (True then False answers `hop_failure_written` true and false); another firm's request and an absent request answer the same `UNAVAILABLE` and call the port ZERO times; a bad hop, a bad code, a missing field answer `INVALID_REQUEST` and call it zero times; a port that raises `LeaseRefused` answers `INVALID_REQUEST`; `put` and `get_ref` unchanged (one control each). Where `DynamoGenerationStore` cannot be imported in your sparse cone, file a BLOCKING row naming the folder; do not rebuild the class.

**Files you write (the only files you may write besides your proof, the surprise channel and this order):**

infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_fail_op.py

Use plain synthetic names in tests (`firm-a`, `req-1`); no real client name, no credential, no secret. ASCII only in code and log lines. Do not edit any other file.

### ACCEPTANCE

<criterion id="AR71-tf-AC1" cell_refs="AR-tf-71"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 6 --prefix=test_hop_failure_ infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_fail_op.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR71-tf-AC1` -- the test file exists, every test function is named `test_hop_failure_*`, the tests pass and at least 6 pass. Dry-run at box/dell2 23ee4c175d: `R46-TESTS-FAIL absent: ...` -- FAIL as expected. The checker's `--self-test` reads `R46-SELFTEST-OK`.

<expected_criteria>AR71-tf-AC1</expected_criteria>

## BOUNDS

- **Grant.** The files listed, this order's file, your deliverables folder, the surprise channel. No other code, no other test.
- **No network, no AWS, no secret, no deploy, no apply.** Fakes only.
- **Refusal clause.** If a cited line is not what this order says, build for what the code does and file a surprise row; if a needed folder is outside your cone, file a `BLOCKING` row naming it and stop on that part.
- **No alarms, monitors or notifications.** A failure is a stored code the page reads.

<paths>
infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_hop_failure_fail_op.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R48_TX.md</decomp_doc> (round 48, workstream ~TX), cell `AR-tf-71`.
<owned_cells>AR-tf-71</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR71-tf-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~225/IRPT_ANLREQ.TO-AR-tf-71.draft-store-fail-op.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR71-tf-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the files, the count passed, for each guard in your code the test that fails without it (remove it in a scratch copy), the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new op and its callers inside one function's source; the consumers are named in the contract above. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change in this cell (the grant is AR-tf-73's).
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates and its proof instance. Traps named for the worker: a fake writer that accepts any hop or code, so the closed-set refusal is never exercised; a fail call that can change the function's own result or raise; a grant statement that leaks PutItem, GetItem, Query or Scan on the jobs table or touches S1 to S5; a request of another firm that still reaches the writer; the real DynamoGenerationStore not being in the draft-store zip, which this cell does not fix but must report.
</preflight>

- Cut on the CTO's rulings: FWD-4 read-not-write (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`, msg 8906), PRD v0.21 signed (msg 8924), the narrow grant (A) (msg 8970). Risk WORLD. WORLD by the path floor (`<paths>` under `infra/`, spine v3.19 L6); the work is source and tests, no deploy.
- Base: `AR71-tf-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 23ee4c175d, run by the issuer before the cut.
