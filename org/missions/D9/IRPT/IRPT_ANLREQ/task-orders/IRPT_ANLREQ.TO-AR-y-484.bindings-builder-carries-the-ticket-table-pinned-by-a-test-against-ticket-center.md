# TO IRPT_ANLREQ.TO-AR-y-484.bindings-builder-carries-the-ticket-table-pinned-by-a-test-against-ticket-center -- BUILD AND PROVE OFFLINE: the resident bindings builder writes `tickets_table` = "opal-tickets", and a test pins that value to the name line of the aws_dynamodb_table resource in infra/aws/terraform/ticket-center/main.tf; nothing is planned, applied, built into a release or run

<to_id>IRPT_ANLREQ.TO-AR-y-484.bindings-builder-carries-the-ticket-table-pinned-by-a-test-against-ticket-center</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~352</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ143</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-484` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** CTO ruling msg 11713 (RULED A: the builder carries the name, pinned by a test against ticket-center/main.tf, with a mutant that fires); AR-y-483 (the resident half, row W351-S1 is this cell)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~352`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-352` (branch `wk-IRPT_ANLREQ-352`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~352 <0.9.0_WK_IRPT_ANLREQ~352@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W352-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy, no release build.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; its controls kind is `script`, not `code`), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR484-y-AC1,AR484-y-AC2"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID. The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it).

### THE CELL (`AR-y-484`, inlined)

*What and why.* `infra/aws/lambda/investor-reporting/reports/build_resident_package.py` writes `resident_bindings.json` (the `bindings` dict, from line 108). The resident (AR-y-483, drained) reads an OPTIONAL binding `tickets_table` and passes it to the packager so the analysis-audit record can be written; with the binding absent the audit ports stay unwired. The bindings builder already carries `"jobs_table": "irpt-jobs"` and `"requests_table": "irpt-requests"` as literals. The CTO ruled (msg 11713): the builder carries `"tickets_table": "opal-tickets"` the same way, and a test keeps it equal to the existing table's name: the `aws_dynamodb_table` resource in `infra/aws/terraform/ticket-center/main.tf` (its `name = "opal-tickets"` line, about line 48; read the file to find the resource, do not trust the line number).

*The change.* (1) In `build_resident_package.py` add `"tickets_table": "opal-tickets",` to the `bindings` dict (one line, after `requests_table`; nothing else changes in that file). (2) New `infra/aws/lambda/investor-reporting/reports/tests/test_resident_tickets_table_pin.py` (hermetic, stdlib only). Read `build_resident_package.py` as TEXT and read `infra/aws/terraform/ticket-center/main.tf` as text, both from the repository root found with `git rev-parse --show-toplevel` (never a typed or device path). The test extracts the `tickets_table` value from the builder text with a regex, and extracts the `name` of the `resource "aws_dynamodb_table"` block that holds `ticket_id` as its hash key from `infra/aws/terraform/ticket-center/main.tf`, and requires them EQUAL. It also requires the builder value to match `[A-Za-z0-9_.-]{3,255}`. A pure helper `compare(builder_text, tf_text)` returns the pair (builder value, table name) or raises; tests call it on the real files (must pass) and on THREE in-memory mutants that must each be refused: the builder value changed to `opal-ticket`, the builder line removed, the Terraform name changed to `opal-tickets-v2`. No test is skipped.

*The check.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~352/`: `check_tickets_pin.py` (stdlib only, ruff clean, offline). It prints `TICKETS-PIN-OK builder=opal-tickets terraform=opal-tickets equal=yes` after reading the two files at the repository root, or `TICKETS-PIN-BAD <why>` (rc 1). `--selftest` applies the same three mutants in memory and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the builder line and the test as ONE commit first, message citing AR-y-484; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR484-y-AC1" cell_refs="AR-y-484"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~352/check_tickets_pin.py</invocation><expect>^TICKETS-PIN-OK builder=opal-tickets terraform=opal-tickets equal=yes$</expect></criterion>
<criterion id="AR484-y-AC2" cell_refs="AR-y-484"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~352/check_tickets_pin.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR484-y-AC3" cell_refs="AR-y-484"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest reports/tests/test_resident_tickets_table_pin.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~352/IRPT_ANLREQ.TO-AR-y-484.bindings-builder-carries-the-ticket-table-pinned-by-a-test-against-ticket-center.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-484.bindings-builder-carries-the-ticket-table-pinned-by-a-test-against-ticket-center`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR484-y-AC1,AR484-y-AC2,AR484-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-484</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_tickets_table_pin.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~352/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-484.bindings-builder-carries-the-ticket-table-pinned-by-a-test-against-ticket-center.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one builder line and one test file; nothing is planned, applied, deployed, built into a release or run against AWS; the release r34q is built by 2.0.0_SA_COO~G2 and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the builder, the Terraform resource and the CTO's ruling against this cell; the lens: a name typed that differs from the Terraform name, a test that reads a typed path, a regex that matches the wrong resource, a mutant that cannot fire, an edit outside the one dict line. NOT seen (blind): G2's release machinery (r34p_build.py, make_scripts_r34p.py) and whether it calls this builder; denominator: three criteria.
</preflight>
