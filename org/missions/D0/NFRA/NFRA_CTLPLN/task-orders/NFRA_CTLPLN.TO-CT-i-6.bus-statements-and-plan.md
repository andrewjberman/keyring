# TO NFRA_CTLPLN.TO-CT-i-6 -- workstream INBOUND round 4 CT-i-6: the Teams agent's role may send to the two Dell bus queues (written, not applied), and the deploy's plan is measured

<to_id>NFRA_CTLPLN.TO-CT-i-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~34</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-6` (`decompositions/NFRA_CTLPLN_DECOMP.inbound4.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none (rounds 1 to 3 are merged)

---

## WORKER FACE

### THE CELL

`CT-i-6`. The Teams agent (a cloud function, Terraform root `infra/aws/terraform/transcripts/`, file `chat_assist.tf`, module
`ldo_001`) now offers a job to every box of the device register `org/devices/DEVICES.json`: four boxes, each with a `name` and
an `inbound_queue`. Its role may send to only two of the four queues: `chat_assist.tf` `extra_statements` holds
`TellTheLaptopMstrOnTheBus` and `TellTheSiteZMstrOnTheBus`. You WRITE the two missing statements and MEASURE the plan of the
deploy. **You apply NOTHING.** The apply is another seat's act, later, under two signatures that will quote your measurement.

### BUILD

1. `infra/aws/terraform/transcripts/chat_assist.tf`: add exactly two elements to `extra_statements`, directly after
   `TellTheSiteZMstrOnTheBus`, in the same one-line shape as the existing pair: Sid `TellDell1OnTheBus` and Sid
   `TellDell2OnTheBus`, each `Effect = "Allow"`, `Action = ["sqs:GetQueueUrl", "sqs:SendMessage"]`, and `Resource` the queue's
   ARN built like the existing pair's (region `us-east-1`, the account id from `data.aws_caller_identity.current.account_id`)
   with the queue name that box carries in the register's `inbound_queue`. Extend the comment above the pair by one line
   saying the four statements are the four boxes of the device register. Change nothing else in the file.
2. `infra/aws/terraform/transcripts/tests/check_chat_assist_bus.py` (standard library only; it parses the `.tf` file's text
   and reads the register; it calls nothing):
   - default mode: every box of the register has exactly one statement whose Resource ends with that box's `inbound_queue`;
     there are no bus statements beyond the register's boxes; each has exactly the two actions and `Effect` Allow. LAST line
     `CHAT-ASSIST-BUS ok=<True|False> boxes=<n> statements=<s> matched=<m> extra=<e>`.
   - `--plan-file <path>`: reads a saved `terraform plan -no-color` text and prints, LAST,
     `CHAT-ASSIST-PLAN ok=<True|False> add=<a> change=<c> destroy=<d> outside_module=<o>`, where `outside_module` counts
     resource lines whose address does not start with `module.ldo_001`, and `ok=True` needs `destroy=0` and
     `outside_module=0`.
3. Build the package: `bash infra/aws/lambda/teams-chat-assist/build.sh` in your worktree (first run
   `python data/transcripts/scripts/teams_chat/gen_bus_devices.py --check`; it must read `BUS-DEVICES ok=True`). `dist/` is a
   build product and is never committed. Record the zip's SHA-256 and its file count.
4. MEASURE the plan, read-only, with `TF_DATA_DIR` set to a NEW scratch directory outside the repository (so the root's own
   `.terraform` is not touched), through the estate's AWS shim on this machine:
   - `terraform init -input=false` (if it asks to migrate or reconfigure state, STOP: record the message, change nothing,
     and file a row, class BLOCKING);
   - `terraform plan -no-color -input=false -lock=false -target=module.ldo_001 -out=<scratch>/targeted.tfplan`, its text
     saved to `<your deliverables folder>/PLAN_TARGETED_module_ldo_001.txt`;
   - `terraform plan -no-color -input=false -lock=false`, its text saved to `PLAN_UNTARGETED.txt` beside it.
   A plan is a read. Never run `terraform apply`, `safe-apply`, `import`, `state` or `taint`. Never pass `-lock=true`.
5. In your deliverables folder, `DEPLOY_PLAN_MEASURED.md`: for the TARGETED plan, the summary line and every resource
   address with its action and, in one line each, what the change is (the policy document's added statements; the function
   package's hash change; anything else, named); whether any line is NOT explained by this workstream's merged work, with
   the reason you believe so; for the UNTARGETED plan, the summary line and the list of resource addresses outside
   `module.ldo_001`; the zip's SHA-256; the `init` output's backend line. Quote no secret value; a plan line that shows one
   is replaced by `(redacted)`.

### RULES FOR THIS CELL

- **Apply nothing, deploy nothing, upload nothing.** Reads of AWS through a plan are the only calls that leave this machine.
  No `aws lambda update-function-code`, no `aws s3 cp`, no bus send, no model call, no text.
- Edit nothing under `infra/` but the two files in `<paths>`. `dist/`, `.terraform/` and any plan file are never committed.
- If the targeted plan shows a resource outside `module.ldo_001`, a destroy, or a replacement, that is a row, class BLOCKING;
  record it and finish the measurement file anyway.
- No non-ASCII in any file you write. Bake no absolute path and no account id the file does not already carry.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi6-AC1" cell_refs="CT-i-6"><invocation>python infra/aws/terraform/transcripts/tests/check_chat_assist_bus.py</invocation><expect>CHAT-ASSIST-BUS ok=True boxes=4 statements=4 matched=4 extra=0</expect></criterion>
`CTi6-AC1` -- the written change against the real device register: four boxes, four statements, none extra.

<criterion id="CTi6-AC2" cell_refs="CT-i-6"><invocation>python infra/aws/terraform/transcripts/tests/check_chat_assist_bus.py --plan-file org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~34/PLAN_TARGETED_module_ldo_001.txt</invocation><expect>CHAT-ASSIST-PLAN ok=True</expect></criterion>
`CTi6-AC2` -- the real targeted plan, read: no destroy and nothing outside the agent's own module.

<criterion id="CTi6-AC3" cell_refs="CT-i-6" judgment="true"/>
`CTi6-AC3` -- JUDGMENT, never self-graded: `DEPLOY_PLAN_MEASURED.md` explains every line of the targeted plan by this workstream's merged work, or names the line it cannot explain.
</proof_of_spec>

<expected_criteria>CTi6-AC1,CTi6-AC2,CTi6-AC3</expected_criteria>

Each invocation runs under `timeout 120` (the two plans are build steps, not criteria; bound each at 600 seconds and record a
timeout as the output). Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~34/NFRA_CTLPLN.TO-CT-i-6.bus-statements-and-plan.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi6-AC1,CTi6-AC2,CTi6-AC3`, and flip `<status>` to `complete`
only when both mechanical criteria pass and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W34-S<k>`; append lines
only to the investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound4.md</decomp_doc>
<owned_cells>CT-i-6</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/transcripts/chat_assist.tf
infra/aws/terraform/transcripts/tests/check_chat_assist_bus.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the function's clock is unchanged.
comp-iam: RUN by the cell's own check -- denominator: 4 register boxes, 4 statements, 2 actions each; the grant is send-only on four named queues and is written, not applied. BLIND: the role's other statements inside the module and the live policy are not read by this lens; the plan read is the cell's.
comp-adversary: RUN -- a worker applying (the face forbids every applying verb; the plan uses a scratch data directory and no lock); a queue name typed wrong (checked against the register); another project's unapplied work in the same root riding this deploy (the targeted plan must show nothing outside the module, the untargeted one is listed so the halves can say what is NOT covered); a backend reconfiguration answered by a worker (a BLOCKING stop); a secret in a plan text committed to git (redacted). BLIND: the plan is this hour's; the applier re-plans and the halves bind both branches.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-20; CTO ruling msg 106725; round-1 decomposition,
issuer act 3; `2.0.0_SA_COO~C`'s half `NEVER_WIDEN_HALF_NFRA_CTLPLN_TRANSCRIPTS_KEY_DELL_DECRYPT_20261007.md` (the root's
untargeted plan and backend facts, re-measured here).
