# TO IRPT_ANLREQ.TO-AR-y-316.submit-input-owner-check -- BUILD the owner check on the attachment's input_id at SUBMIT-FORM (row W101-S3) in the ticket service, with the one read grant it needs as Terraform SOURCE

<to_id>IRPT_ANLREQ.TO-AR-y-316</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~126</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: an infrastructure path; the worker still deploys, applies and invokes NOTHING)
**Decomp cell:** `AR-y-316` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop 1, the filing) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~126`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-126` (branch `wk-IRPT_ANLREQ-126`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~126 <0.9.0_WK_IRPT_ANLREQ~126@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W126-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet` fixture):
  never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID). No live call of any kind: no AWS, no network, no deploy, no apply, no Terraform plan or apply (`terraform fmt -check` on the one file is allowed if the binary is installed). No non-ASCII in what you add.

### THE CELL (`AR-y-316`, inlined) -- BUILD ONLY. Nothing is deployed, applied or invoked.

*The ticket service's SUBMIT-FORM route (`POST /api/scoped/tickets/submit`, `infra/aws/lambda/ticket_center/lambda_function.py`, function `submit_form`, about line 1111) lets a client login file an `analysis_request` whose `attachment` is `{upload_id, input_id}`. `_validate_attachment` (about line 746) checks the SHAPE only (`input_id` must match `^portfolio_[0-9a-f]{64}$`), so a client login of one firm can file a ticket naming ANOTHER firm's input, or another advisor's input in its own firm (row W101-S3, the CTO's ruling msg 7620). Build the owner check: before the ticket row is written, the service reads the retained input's owner row and refuses unless the input belongs to the caller.*

**THE RULE (CTO ruling 7620 and the approved grant shape, msg 7633):**
1. The read keys on the caller's VERIFIED firm: the table is `irpt-requests` (env `IRPT_REQUESTS_TABLE`, default `irpt-requests`), partition key `tenant`, sort key `request_revision`; the row is `Key={"tenant": <caller firm>, "request_revision": "INPUT#" + input_id}` with `ConsistentRead=True`. The caller's firm is the authorizer context firm (`actor["firmId"]`, the variable `firm` in `submit_form`), NEVER the body. Another firm's input is then NOT FOUND and is refused.
2. The row is accepted only when (the same four tests as `load_input_owner`, `infra/aws/lambda/investor-reporting/intake/uploads.py` line 260-270, read it): the row exists; `row["tenant"] == firm`; `row["identity"] == input_id`; `row["owner"]["firm_id"] == firm`. And the OWNER must be the caller: `row["owner"]["principal_id"]` must equal the caller's principal id. The door computes `principal_id` for a partner viewer in `infra/aws/lambda/investor-reporting/_scope/prospect.py` `resolve_prospect_owner(headers, data_firm)` (read it, and `_scope/interactive_access.py` lines 80-100 and `_scope/ordinary_viewer.py`): find which authorizer-context value the ticket service has that equals it (the caller's `email` is the likely one; the ticket service has `actor["email"]`, `actor["firmId"]`, `actor["allowedFirmIds"]`). State the mapping with the file and line evidence in your record. If NO value the ticket service holds can equal the door's `principal_id`, STOP that half: file a BLOCKING row naming the two derivations, implement the firm and identity tests (1 and 2 without the principal test), and say so in your report; do NOT invent a mapping.
3. ANY failure refuses with HTTP 400 and a message that does NOT reveal whether the input exists for another firm: the same text for not-found, other-firm and other-owner (for example `attachment.input_id is not available to the caller`). Any exception of the read (a missing table, a throttle, a malformed row) REFUSES (fail closed, HTTP 503 or 400 as the neighbouring code does for a store error; read how `_table` errors are answered nearby and match it); a read error must never admit.
4. Only an `analysis_request` SUBMIT is checked. CREATE (internal humans and the service subjects), the other ticket types, LIST, REPORT, PACKAGE and the draft routes are NOT changed. The check is a seam: a module-level reader function (for example `_input_owner_reader`) that the tests replace, so no test reaches AWS (`tests/conftest.py` guards the users table; add an equivalent guard for `irpt-requests` reads or replace the reader in every test that submits an analysis request).

**THE IAM GRANT (Terraform SOURCE only; the CTO approved this shape, msg 7633, "one widening of the pair"):** in `infra/aws/terraform/ticket-center/main.tf`, in the `opal_ticket_api_ddb` policy beside `UsersDirectoryReadForClaimEnrichment`, add ONE statement with its own `Sid` `IrptRequestsInputOwnerRead`: `Effect` Allow, `Action` exactly `["dynamodb:GetItem"]`, `Resource` the `irpt-requests` table ARN (read it by a `data "aws_dynamodb_table"` source exactly as `opal_users_v2` is read at the top of the file, so a rename fails the plan loudly), and a `Condition` block with `ForAllValues:StringEquals` on `dynamodb:LeadingKeys` = `["49financial", "inflection", "cottonwood"]` (the three firms of the signed release-29 pair; a new firm is a grant edit), and, because the `INPUT#` row holds more than the owner fields, `ForAllValues:StringEquals` on `dynamodb:Attributes` = the attributes your code projects (`tenant`, `request_revision`, `identity`, `owner`) AND `StringEqualsIfExists` `dynamodb:Select` = `SPECIFIC_ATTRIBUTES`; your read MUST then pass `ProjectionExpression` of exactly those attributes (a read without the projection would be refused by IAM). Add the environment variable `IRPT_REQUESTS_TABLE` to the Lambda's environment block in the same file if the file builds the environment there. You do NOT plan, apply or run Terraform.

### ACCEPTANCE

<criterion id="AR316-y-AC1" cell_refs="AR-y-316"><invocation>python -m pytest C:/dev/wk-irpt-anlreq-126/infra/aws/lambda/ticket_center/tests/test_submit_input_owner.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
`AR316-y-AC1`: the new test file `tests/test_submit_input_owner.py` passes with every one of these cases named in a test: the caller's own input is admitted (201); ANOTHER firm's input is refused and the refusal text is the same as for a missing input; ANOTHER advisor's input in the SAME firm is refused; a malformed owner row (no `owner`, wrong `identity`, wrong `tenant`) is refused; a reader that raises is refused (fail closed); the reader is called with the VERIFIED firm and never the body's; a non-`analysis_request` submit and CREATE do not call the reader; the existing `tests/test_submit_analysis_request.py` still passes (run it too and print its count; edit it only where its fixtures need the reader replaced).

<criterion id="AR316-y-AC2" cell_refs="AR-y-316"><invocation>python C:/dev/wk-irpt-anlreq-126/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~126/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR316-y-AC2` (the one mutant that fails): you write `deliverables/0.9.0_WK_IRPT_ANLREQ~126/mutant_check.py`: it copies `lambda_function.py` to a scratch folder OUTSIDE the product tree with the owner check neutralised (the call removed or the comparison replaced by `True`), runs your new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (and `MUTANT-SURVIVES` otherwise, exit 1).

<criterion id="AR316-y-AC3" cell_refs="AR-y-316"><invocation>python C:/dev/wk-irpt-anlreq-126/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~126/iam_shape_check.py</invocation><expect>IAM-SHAPE-OK</expect></criterion>
`AR316-y-AC3` (a third check, with a reason: the grant is the release's one widening and is not reachable by a unit test): you write `deliverables/0.9.0_WK_IRPT_ANLREQ~126/iam_shape_check.py`: it reads `infra/aws/terraform/ticket-center/main.tf` and prints `IAM-SHAPE-OK` only when the statement `IrptRequestsInputOwnerRead` exists exactly once with `Action` exactly `dynamodb:GetItem`, its `Resource` the `irpt-requests` data source and nothing else, the `dynamodb:LeadingKeys` condition equal to the three firms and no other value, and the `dynamodb:Attributes` list equal to the attributes your code projects (it imports them from, or greps them in, `lambda_function.py`); otherwise it prints `IAM-SHAPE-BAD <why>` and exits 1. Run it against a copy of `main.tf` with one extra firm and show it print BAD (record the negative control).

<criterion id="AR316-y-AC4J" cell_refs="AR-y-316" judgment="true"/>
`AR316-y-AC4J` (judgment, graded at L9, never by you): the caller-to-owner mapping you state is the door's own (with the file and line evidence), the refusal reveals nothing about another firm's inputs, a read error never admits, and the IAM statement grants exactly one action on one table to exactly the three firms with the attributes the code projects.

<expected_criteria>AR316-y-AC1 AR316-y-AC2 AR316-y-AC3 AR316-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~126/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else (including `infra/aws/lambda/investor-reporting/**`).

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_submit_input_owner.py
infra/aws/lambda/ticket_center/tests/test_submit_analysis_request.py
infra/aws/lambda/ticket_center/tests/conftest.py
infra/aws/terraform/ticket-center/main.tf
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-316</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~126/IRPT_ANLREQ.TO-AR-y-316.submit-input-owner-check.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-316`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR316-y-AC1,AR316-y-AC2,AR316-y-AC3,AR316-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source only in a worker worktree; nothing is deployed, applied or invoked. The release pair (the issuer's, after this cell) names the one widening: a read grant on irpt-requests for the ticket role, GetItem only, the three firms, the owner attributes only (CTO msg 7633).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; SUBMIT-FORM gains a refusal. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- the IAM statement is SOURCE in a Terraform file; nothing is planned or applied here.
comp-adversary: RUN -- by reading row W101-S3 and the release-28 pair line 56 (any client login can file a ticket naming another firm's input) against this cell; the lens: a check that keys on the body's firm, a refusal that tells another firm's input apart from a missing one, a read error that admits, a grant wider than the three firms or the owner attributes. The cell requires the verified firm as the key, one refusal text, fail closed, and a mutant that fires. NOT seen: the live irpt-requests rows and the live role.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling msg 7620 (row `D2-S96`, W101-S3 live) and the approved grant shape msg 7633, in round 40 workstream `ZD` beside the release-29 window. Base: `AR316-y-AC1`, `AC2` and `AC3` FAIL as expected (no test file, no checker file).
- It ships in the NEXT `opal-ticket-api` release under a pair the issuer writes after this cell; the partner-firm page's PROD promote waits for it; the FWD-1 run on DEV does not.
