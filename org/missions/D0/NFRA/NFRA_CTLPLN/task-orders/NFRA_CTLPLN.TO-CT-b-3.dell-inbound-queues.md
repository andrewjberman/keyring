# TO NFRA_CTLPLN.TO-CT-b-3 -- round 2 CT-b-3: the two Dell inbound queues, mirroring the live bus queues, names from the builder's FIFO form

<to_id>NFRA_CTLPLN.TO-CT-b-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~3</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-b-3` (`decompositions/NFRA_CTLPLN_DECOMP.round2.md`) | **outcome_ref:** FWD-3 |
**depends_on:** the builder's FIFO queue form (requested of `4.0.0_SA_CRO` by `1.0.0_SA_CTO`, msg 105928); the issuer flips this order to
`pending` and spawns when it lands.

---

## WORKER FACE

### THE CELL

`CT-b-3`, FWD-3 (C-BUS): each box has one inbound queue, drained by its fabric manager; any box sends to the recipient's queue. dell1 and dell2
have none today. You write the Terraform for their two inbound queues and prove it with a static check and a plan. You APPLY NOTHING.

**The names (builder output, C-BUS):** `name('agentbus', 'global', 'dell1', 'queue')` and `... 'dell2' ...` with the builder's FIFO form --
read the FIFO form from `lib/opal_naming.py` / NAMING_SCHEMA at your HEAD (it is the registry change this order waited for) and use exactly what
it returns. If the builder still returns no name ending in `.fifo`, stop (refusal clause): never type the suffix.

**Mirror the live queues exactly** (`infra/aws/terraform/nfra-agentbus-port2/sqs.tf`, measured three times): `fifo_queue = true`,
`content_based_deduplication = true`, `message_retention_seconds = 1209600`, `visibility_timeout_seconds = 30`,
`receive_wait_time_seconds = 20`, `max_message_size = 1048576`, `delay_seconds = 0`, `sqs_managed_sse_enabled = true`; no CMK, no queue policy.

**Build** a new Terraform root `infra/aws/terraform/nfra-ctlpln-agentbus/`:
- `main.tf`: required_version >= 1.5.0, aws ~> 5.0, backend `s3` bucket `opal-313476888478-terraform-state`, key `nfra-ctlpln-agentbus/tfstate`,
  region us-east-1; provider us-east-1; a header comment naming FWD-3, C-BUS and that the laptop/site Z pair migrates in a later round.
- `sqs.tf`: the two `aws_sqs_queue` resources.
- `tests/check_queues.py`: runs `terraform -chdir=<root> init -input=false` (the real backend: the state key is new, so the plan reads an
  empty state) and `terraform plan -input=false -detailed-exitcode -no-color`; asserts both names equal the builder's FIFO output and every
  attribute above; prints as the LAST line `QUEUES-CHECK names_from_builder=<k>/2 attributes_match=<True|False> plan_add=<a> plan_change=<c> plan_destroy=<d>`.

### ACCEPTANCE

<criterion id="CT2b3-AC1" cell_refs="CT-b-3"><invocation>python infra/aws/terraform/nfra-ctlpln-agentbus/tests/check_queues.py</invocation><expect>names_from_builder=2/2 attributes_match=True plan_add=2 plan_change=0 plan_destroy=0</expect></criterion>
`CT2b3-AC1` -- the root plans exactly two new queues, named by the builder, with the live bus queues' attributes, and touches nothing else.

<criterion id="CT2b3-AC2" cell_refs="CT-b-3"><invocation>python -m pytest -q .tools/tests/test_agentbus_tailnet_stamp.py</invocation><expect>passed</expect></criterion>
`CT2b3-AC2` -- (AMENDMENT 1) a message sent from each of the four boxes carries its own and the recipient's tailnet names from the register;
a received message whose sender tailnet name the register does not hold is refused.

<expected_criteria>CT2b3-AC1,CT2b3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No apply.** `terraform plan` reads the state bucket and the account read-only; that is the only AWS access.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W3-S<k>`), and do not weaken the check or type a name.

<paths>
infra/aws/terraform/nfra-ctlpln-agentbus/main.tf
infra/aws/terraform/nfra-ctlpln-agentbus/sqs.tf
infra/aws/terraform/nfra-ctlpln-agentbus/.terraform.lock.hcl
infra/aws/terraform/nfra-ctlpln-agentbus/tests/check_queues.py
.tools/agentbus-sqs.sh
.tools/agentbus-consumer.py
.tools/tests/test_agentbus_tailnet_stamp.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round2.md</decomp_doc> (round 2), cell `CT-b-3`.
<owned_cells>CT-b-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT2b3-AC1, CT2b3-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~3/NFRA_CTLPLN.TO-CT-b-3.dell-inbound-queues.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT2b3-AC1,CT2b3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the check line, the plan summary, the two names, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the Dell users' SQS access is CT-b-1's policy (send/receive on agentbus-* queues).
comp-adversary: RUN -- the live bus pair is never touched (a separate root and state key, as port2 isolates itself from port1); no typed name (builder FIFO form or refuse); BLIND: the consumer on each Dell (the Dell's /agentbus arm, a bring-up step, not this cell).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.6 C-BUS, FWD-3; CTO msgs 105920, 105928, 105929; decomposition round 2 (measured constraints 1, 2).

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~03:1xZ) -- unblocked; the names; the tailnet stamp on every bus message

The order flips `staged` -> `pending`: the FIFO form landed (NAMING_SCHEMA v1.14 @1ea925a095; the Terraform module patch applied @a8a55c73b3).
The issuer amends its own order; gate limb: none graded this modification (LIMB 6 grades new orders only; no `<placeholders>`).
1. **Names (CTO ruling, msg 105938):** the signed C-BUS form, `name('agentbus','global','dell1','queue', fifo=True)` ->
   `agentbus-global-dell1-queue.fifo`, likewise dell2. In Terraform, compute them with the naming module
   `infra/aws/terraform/modules/opal_name` (its new FIFO input; read its `variables.tf` and `tests/fifo.tftest.hcl`), never a typed name;
   `check_queues.py` compares the planned names to the Python builder's output.
2. **The tailnet stamp (CTO msg 105932, on Andrew's word "the tailnet name is the real identifier"):** `.tools/agentbus-sqs.sh` stamps the
   sender's and the recipient's tailnet names -- read from `org/devices/DEVICES.json` field `tailnet_name` (the MagicDNS name: laptop
   `cloud-local`, sitez `sitez`, dell1 `dell1`, dell2 `dell2`; ruled one grain, msg 105936), never typed -- as SQS message attributes AND in
   the message envelope, beside the serial. Its receive path REFUSES (does not deliver, says why, leaves no silent drop) a message whose sender
   tailnet name the register does not hold. Read the script's send and receive paths first; keep every existing behaviour.
3. **The test** `.tools/tests/test_agentbus_tailnet_stamp.py` (pytest; no real SQS call -- stub the AWS CLI or boto3 call the script makes, or
   exercise the envelope builder directly): for each of the four register boxes as sender, the stamped attributes and envelope carry that
   box's and the recipient's tailnet names; a message with an unknown sender name is refused; the register is read, not typed (point
   `OPAL_DEVICE_REGISTER` at a fixture with a fifth box and show it stamps without a script edit).

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-07 ~04:0xZ) -- rulings on rows W3-S1, W3-S2, W3-S3; the provider; refused mail never blocks the queue

The issuer rules inside its own order; gate limb: none graded this modification (LIMB 6 grades new orders only; no `<placeholders>`).
CT2b3-AC1's and CT2b3-AC2's invocations and expectations are UNCHANGED.
1. **W3-S1 (AC1 FAIL, provider 5.100.0 rejects `max_message_size = 1048576`).** Measured by the issuer ~04:0xZ: both live bus queues read
   `MaximumMessageSize 1048576` and no `RedrivePolicy`; the local provider cache holds only `5.100.0`. The value stays (mirror the live
   queues exactly). THIS NEW ROOT pins `hashicorp/aws` `~> 6.0` (the naming module declares no provider constraint). Run `terraform init`
   once BEFORE the timed criterion run (the plugin cache `C:/Users/AndrewBerman/.terraform.d/plugin-cache` then holds the 6.x provider; a
   cold download took ~8 min). If a 6.x provider also rejects 1048576, stop under the refusal clause with the version and the error.
   `nfra-agentbus-port2` carries the same latent defect; it is NOT in your grant -- name it in your report only.
2. **W3-S2 (the `watch` primary path runs `.tools/agentbus-consumer.py`, which does not check).** Now in your `<paths>`: the consumer applies
   the SAME check as `recv`, reading the register the same way (one shared reading, not a second copy of the rule where avoidable).
3. **W3-S3 (a refused message left on a one-group FIFO queue blocks all later mail; unstamped mail from not-yet-updated boxes).**
   - A message whose sender tailnet name the register does NOT hold is REFUSED: its whole body and attributes are written to
     `org/mcp/inbox/_agentbus_refused/<UTC stamp>_<SQS message id>.json` (gitignored runtime tree), a line `REFUSED agentbus sender_tailnet=<name>
     reason=<why> record=<path>` is printed, and the message is then DELETED from the queue, so it never blocks the FIFO group. Refused is
     recorded, never silently dropped.
   - A message with NO tailnet stamp (sent by a box still running the old script) is DELIVERED with a printed line `WARN agentbus
     unstamped sender=<serial>`, until every box sends stamped; the strict refusal of an unstamped message is a later flip, not this order.
   - Your test adds: a refused message is recorded to that path and deleted (the stubbed delete is called); an unstamped message is delivered
     with the WARN line; the consumer path refuses an unknown name the same way. Keep the run under 120 s.
4. **Inherited state:** your slot's prior commit `768fca164e` on `wk-NFRA_CTLPLN-3` (root, stamp, 11 tests). Build on it; do not redo it.
