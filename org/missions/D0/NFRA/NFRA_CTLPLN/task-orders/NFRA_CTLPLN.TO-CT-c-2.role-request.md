# TO NFRA_CTLPLN.TO-CT-c-2 -- round 3 CT-c-2: the role request -- a Dell writes in for a role; its shape, its writer, its record

<to_id>NFRA_CTLPLN.TO-CT-c-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~5</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-c-2` (`decompositions/NFRA_CTLPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none (second in this worker's queue, after CT-c-6)

---

## WORKER FACE

### THE CELL

`CT-c-2`, PRD v0.8 C-ROLE-REQUEST (a): "A Dell never creates, edits or attaches policy to a role. When work placed on a Dell needs a
role, the Dell WRITES IN: one request naming the project, the resource the role is for, the service that assumes it and the permissions
asked, each permission tied to the code line that needs it. The laptop reads the request, writes the role in that project's Terraform
root and applies it." The carrier is the bus the Dells already have. You build the request's shape, its writer and its record. You send
nothing on the live bus and you create no role.

**What exists:** `org/devices/DEVICES.json` (the device register: each box's `name`, `role`, `inbound_queue`, `tailnet_name`);
`.tools/agentbus-sqs.sh` (`send <device> <body>`; every message carries the sender's tailnet name); a box's own name is the environment
variable `AGENTBUS_DEVICE`, never derived from a path; each project's box is `placement` in its
`org/missions/D*/*/*/project.json` (`DELL1`, `DELL2`, `LAPTOP`, ...).

**Build:**

1. `org/standards/ROLE_REQUEST.schema.json` -- JSON Schema of one request: `request_id` (`<device>-<UTC compact>-<4 hex>`), `device`,
   `tailnet_name`, `requested_by` (a serial), `requested_at` (UTC), `project`, `terraform_root` (a directory under
   `infra/aws/terraform/`), `resource` (`kind`, `name`), `assuming_service` (for example `lambda.amazonaws.com`), `permissions` (a
   non-empty list of `{action, resource_arn, code_ref}` where `code_ref` is `<repo path>:<line>`), `status` (always `requested` in the Dell's
   record). The schema also defines the ANSWER, a separate file the laptop writes later at
   `org/devices/role_requests/<laptop device>/answers/<request_id>.json` (one writer per file: the laptop never edits a Dell's record):
   `request_id`, `status` (`applied` | `refused`), `role_name`, `role_arn`, `applied_at`, `applied_by`, `commit`, or `reason` on a
   refusal. A request's effective status is its answer's `status` when an answer file exists, else `requested`: `status` is the field
   a reader rejects on.
2. `org/devices/role_request.py` with three verbs:
   - `write --project <CODE> --root <dir> --kind <k> --name <n> --service <s> --permission <action>,<arn>,<path>:<line> [...]
     [--dry-run]`: reads `AGENTBUS_DEVICE` (refuse if unset); refuses unless the device's register `role` is `execution`, the project's
     `placement` names this device, the root exists, every `code_ref` names an existing file and a line inside it, and no permission is
     an `iam:` action or has action `*`; writes the record to `org/devices/role_requests/<device>/<request_id>.json` (a per-box
     directory: only that box writes there); then sends ONE bus line to the laptop
     (`ROLE-REQUEST <request_id> <project> <kind>/<name> org/devices/role_requests/<device>/<request_id>.json`). With `--dry-run` it
     writes nothing, sends nothing and prints the record and the bus line.
   - `validate <file>`: schema plus the same refusals; LAST line `ROLE-REQUEST-VALID <request_id> ok=<True|False>`.
   - `list [--status <s>] [--records <dir>]`: every record under `org/devices/role_requests/*/`, one line each with its EFFECTIVE
     status (read from `*/answers/<request_id>.json` when present), and the count per status as the last line.
   The verbs that WRITE an answer (`mark-applied`, `mark-refused`) are NOT this cell's; leave a clear place for them.
3. `org/devices/test_role_request.py` -- cases, each in a temporary copy of the register and a temporary records directory, never the
   live ones: a valid request writes a record that validates; unset device refused; a device whose role is not `execution` refused; a
   project placed on the other Dell refused; a missing `code_ref` file refused; a `code_ref` line past the file's end refused; an `iam:`
   permission refused; a `*` action refused; the bus line names the record path; `list` counts by effective status (one fixture answer file marks one request `applied`). The bus send is replaced by a
   recorder in the tests. LAST line `ROLE-REQUEST cases=<k>/<n> ok=<True|False>` with `n` = 10.

### ACCEPTANCE

<criterion id="CT3c2-AC1" cell_refs="CT-c-2"><invocation>python org/devices/test_role_request.py</invocation><expect>ROLE-REQUEST cases=10/10 ok=True</expect></criterion>
`CT3c2-AC1` -- the writer accepts a well-formed request and refuses each of the seven malformed ones.

<criterion id="CT3c2-AC2" cell_refs="CT-c-2"><invocation>AGENTBUS_DEVICE=dell1 python org/devices/role_request.py write --dry-run --project IRPT_BCKEND --root investor-reporting --kind aws_lambda_function --name ctlpln-roundtrip-probe --service lambda.amazonaws.com --permission logs:CreateLogStream,arn:aws:logs:us-east-1:313476888478:log-group:/aws/lambda/ctlpln-roundtrip-probe:*,org/devices/role_request.py:1</invocation><expect>ROLE-REQUEST dell1-</expect></criterion>
`CT3c2-AC2` -- the seam probe against the REAL register and a REAL placed project: the dry run prints the bus line and writes nothing.

<expected_criteria>CT3c2-AC1,CT3c2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No live bus send, no AWS call, no IAM act.** The tests never touch `org/devices/DEVICES.json` or a live records directory.
- No non-ASCII in any file you write.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
org/devices/role_request.py
org/devices/test_role_request.py
org/standards/ROLE_REQUEST.schema.json
org/devices/role_requests/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `org/devices/DEVICES.json`, `.tools/agentbus-sqs.sh`,
`org/devices/test_readers.py` (the register readers' test, for the fixture pattern), every `org/missions/D*/*/*/project.json`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round3.md</decomp_doc> (round 3), cell `CT-c-2`.
<owned_cells>CT-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT3c2-AC1, CT3c2-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~5/NFRA_CTLPLN.TO-CT-c-2.role-request.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT3c2-AC1,CT3c2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the schema's required fields; the refusals and their messages; where `mark-applied` will attach; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy in this cell; the writer refuses an `iam:` permission in a request.
comp-adversary: RUN -- a request asking for more than the code needs (each permission tied to a code line, checked to exist; `*` and `iam:` refused; the laptop reads before it applies); a box writing another box's record (per-box directory, FWD-8 one-writer stage 12); a forged sender (the bus stamps and checks the tailnet name, round 2); BLIND: a truthful-looking `code_ref` that does not need the permission -- the laptop's read is the control.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.8 @6df8d231f4 ADDENDUM v0.8 C-ROLE-REQUEST (a); CTO msg 105999; decomposition round 3. Base dry-run at the cut:
CT3c2-AC1 and CT3c2-AC2 base FAIL as expected (neither file exists).
