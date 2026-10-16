# TO-AR-tf-73 -- FWD-4 build (Terraform source): a narrow UpdateItem grant for the draft store on irpt-jobs (AR-tf-73, round 48, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tf-73</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~227</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tf-73` (`decompositions/IRPT_ANLREQ_DECOMP_R48_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none (the writer `mark_hop_failure` is injected or faked; TO-AR-g-109 is `2.0.0_SA_COO~G2`'s)

---

## WORKER FACE

### THE CELL

`AR-tf-73`: "FWD-4 build (Terraform source): a narrow UpdateItem grant for the draft store on irpt-jobs." FWD-4 says a broken hop never silently stops the request. The CTO ruled (PRD v0.21, C-HOP-FAILURE) that the ticket READS the failure through the existing status route and the silent hops write one set-once `hop_failure` on the job row; this cell is the commentary hop's part.

**The contract all three cells serve** (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` row C-HOP-FAILURE, v0.21; ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`; `2.0.0_SA_COO~G2`'s msg 8961): the commentary draft hop writes ONE set-once value `hop_failure` = `{hop, code, at}` on the request's JOB row in table `irpt-jobs` (key `{tenant, job=<request_id>}`), never overwriting the job state. The writer is `DynamoGenerationStore.mark_hop_failure(job_id, hop, code, at)` in `infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py` (`2.0.0_SA_COO~G2`'s order TO-AR-g-109, NOT merged at your base): it returns True when written, False when `hop_failure` was already set (a no-op), and raises `LeaseRefused("HOP_FAILURE_INVALID")` for a hop or code outside its closed sets. For the hop `COMMENTARY` the closed codes are exactly `COMMENTARY_DRAFT_FAILED` and `COMMENTARY_DRAFT_REFUSED`. `at` is UTC `YYYY-MM-DDTHH:MM:SSZ`. THE `fail` OP (cell AR-tf-71 builds it, AR-tf-72 calls it): the draft store's invoke accepts the event `{"op": "fail", "tenant": <firm id>, "request_id": <id>, "hop": "COMMENTARY", "code": <one of the two codes>}` and answers `{"status": "OK", "hop_failure_written": true|false}` or `{"status": "REFUSED", "reason": "INVALID_REQUEST"|"UNAVAILABLE"}`. No draft body travels with it.

**What to build.** The CTO ruled (A) (msg 8970): the draft-store role gains a narrow UpdateItem on the jobs table for the `fail` op, with NO PRD change. In `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf` add to the role's policy (the jsonencode statement list; keep every existing statement byte-identical): (1) a statement `S6` Allow `dynamodb:UpdateItem` on EXACTLY the jobs table ARN (`data.terraform_remote_state.core.outputs.tables.jobs`, the same remote-state pattern S1 uses), with the Condition block: `ForAllValues:StringEquals` `dynamodb:LeadingKeys` = `local.b1_served_firms` (the same leading-key set S1 uses), `ForAllValues:StringEquals` `dynamodb:Attributes` = [`hop_failure`, `tenant`, `job`] (the attribute `hop_failure` plus the two key attributes of the jobs table; read `infra/aws/terraform/investor-reporting/core/dynamodb.tf` for the jobs table's key attribute names and use them exactly), and `StringEqualsIfExists` `dynamodb:ReturnValues` = `NONE`. (2) a statement `S7` Allow `kms:Encrypt`, `kms:Decrypt`, `kms:GenerateDataKey` on the same KMS key ARN S2 uses, with the same Condition shape as S2 (`kms:ViaService` = the dynamodb service, `kms:EncryptionContext:aws:dynamodb:tableName` = the JOBS table name). NO other action on the jobs table: no PutItem, DeleteItem, GetItem, Query or Scan. Do not change S1 to S5. (The set-once rule is the writer's conditional expression `attribute_not_exists(hop_failure)`; IAM cannot state it, so say that in a comment above S6.) Because `terraform` is not installed on this box and a worker holds no AWS, the check is a static test in `infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py` (stdlib and pytest; named `test_hop_failure_<what>`) that reads the `.tf` text and, for the S6 and S7 statements located by their Sid: asserts the action list is exactly the stated one, the resource names the jobs table output and not the requests table, the three Condition elements are present with the stated values, S1 still names only the requests table, no jobs-table ARN appears in any other statement, and the policy text contains no wildcard `*` action. Two in-memory mutants inside the test (a copy of the text with `dynamodb:PutItem` added to S6, and a copy with the Attributes condition removed) must each be refused by the same check function. Write NO plan, NO apply, NO AWS call: the apply is a later WORLD act by the applier under a pair whose packet carries an `iam simulate-custom-policy` battery (allowed: the hop_failure update; denied: PutItem, DeleteItem, Query, Scan, and an UpdateItem naming any other attribute); that packet is the issuer's, not this cell's.

**Files you write (the only files you may write besides your proof, the surprise channel and this order):**

infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf
infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py

Use plain synthetic names in tests (`firm-a`, `req-1`); no real client name, no credential, no secret. ASCII only in code and log lines. Do not edit any other file.

### ACCEPTANCE

<criterion id="AR73-tf-AC1" cell_refs="AR-tf-73"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 5 --prefix=test_hop_failure_ infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR73-tf-AC1` -- the test file exists, every test function is named `test_hop_failure_*`, the tests pass and at least 5 pass. Dry-run at box/dell2 23ee4c175d: `R46-TESTS-FAIL absent: ...` -- FAIL as expected. The checker's `--self-test` reads `R46-SELFTEST-OK`.

<expected_criteria>AR73-tf-AC1</expected_criteria>

## BOUNDS

- **Grant.** The files listed, this order's file, your deliverables folder, the surprise channel. No other code, no other test.
- **No network, no AWS, no secret, no deploy, no apply.** Fakes only.
- **Refusal clause.** If a cited line is not what this order says, build for what the code does and file a surprise row; if a needed folder is outside your cone, file a `BLOCKING` row naming it and stop on that part.
- **No alarms, monitors or notifications.** A failure is a stored code the page reads.

<paths>
infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf
infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R48_TX.md</decomp_doc> (round 48, workstream ~TX), cell `AR-tf-73`.
<owned_cells>AR-tf-73</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR73-tf-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~227/IRPT_ANLREQ.TO-AR-tf-73.draft-store-role-jobs-grant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR73-tf-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the files, the count passed, for each guard in your code the test that fails without it (remove it in a scratch copy), the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new op and its callers inside one function's source; the consumers are named in the contract above. comp-iam: RUN -- `comp-iam service irpt-commentary-draft-store-lambda` printed `No service matching` against 197 Lambda services and 222 IAM roles scanned: the function and its role are NOT in the census, so the lens is BLIND on this subject (declared, not read as clean). This cell writes policy source only, no permission is applied; the grant is checked by a static test here and by an `iam simulate-custom-policy` battery in the applier's packet.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates and its proof instance. Traps named for the worker: a fake writer that accepts any hop or code, so the closed-set refusal is never exercised; a fail call that can change the function's own result or raise; a grant statement that leaks PutItem, GetItem, Query or Scan on the jobs table or touches S1 to S5; a request of another firm that still reaches the writer; the real DynamoGenerationStore not being in the draft-store zip, which this cell does not fix but must report.
</preflight>

- Cut on the CTO's rulings: FWD-4 read-not-write (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`, msg 8906), PRD v0.21 signed (msg 8924), the narrow grant (A) (msg 8970). Risk WORLD. WORLD by the path floor (`<paths>` under `infra/`, spine v3.19 L6); the work is source and tests, no deploy.
- Base: `AR73-tf-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 23ee4c175d, run by the issuer before the cut.
