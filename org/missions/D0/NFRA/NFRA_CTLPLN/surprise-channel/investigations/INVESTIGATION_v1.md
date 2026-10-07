# NFRA_CTLPLN -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Opened by:** `3.0.0_SA_CVO`. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW
row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row is `NFRA_CTLPLN-S<k>`; a
worker's is `NFRA_CTLPLN-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## NFRA_CTLPLN-S1 -- the laptop accepts Remote Desktop from any network, not only the tailnet

```json
{
  "id": "NFRA_CTLPLN-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-06T19:15Z",
  "one_line": "The laptop already accepts Remote Desktop from ANY address on ANY network profile, including its Public-profile Ethernet; C-RDP (v0.4) requires port 3389 scoped to the tailnet only.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "Andrew (the laptop's owner): scope the three enabled Remote Desktop inbound rules to the tailnet range 100.64.0.0/10, or have the S14 applier (2.0.0_SA_COO~C) do it on his word",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Get-NetFirewallRule (Remote Desktop group, enabled) | Get-NetFirewallAddressFilter on the laptop, 2026-10-06 ~19:1xZ: 'Remote Desktop - User Mode (TCP-In)', '(UDP-In)' and 'Shadow (TCP-In)', each Profile Any, Inbound, RemoteAddress Any",
      "Get-NetConnectionProfile: 'Ethernet 6' NetworkCategory Public; 'Tailscale' Private",
      "HKLM Terminal Server fDenyTSConnections = 0 (Remote Desktop on); RDP-Tcp UserAuthentication = 1 (network-level authentication on, which limits but does not remove the exposure)",
      "C-RDP at NFRA_CTLPLN PRD v0.4 @1fa1a35a13: 'the Windows firewall scopes 3389 to the tailnet's address range only, never the public internet or the local network'; the CRO's record says firewall scope unmeasured"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "C-RDP: Remote Desktop reachable over the tailnet only; never the public internet or the local network.",
  "world_is": "On the laptop, 3389 is admitted from any address on every profile, including the network it is on now (Public). Site Z, dell1 and dell2 are not read here.",
  "notes": "Found while reviewing v0.4's ratified-text half; not caused by this project. S14's proof should include the negative arm: one connection from a non-tailnet address refused, on each box."
}
```

## NFRA_CTLPLN-W1-S1 -- iam:PassRole is explicitly denied in the Dell deploy policy, but a deploy that registers a

```json
{
  "id": "NFRA_CTLPLN-W1-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~1",
  "surfaced_at": "2026-10-07T03:26Z",
  "one_line": "iam:PassRole is explicitly denied in the Dell deploy policy, but a deploy that registers an ECS task definition naming a task or execution role, puts an EventBridge target with a role, or changes a Lambda's role needs iam:PassRole; the order's ALLOW of ECS task definitions and EventBridge targets is not usable for those deploys under the deny.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C with 1.0.0_SA_CTO: rule on a narrow PassRole allow (named role ARNs, iam:PassedToService condition) before the first Dell ECS or EventBridge-target deploy; without a ruling the Dell stays unable to pass any role",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell_deploy_policy.json statement DenyEveryIamWrite lists iam:PassRole (infra/aws/terraform/nfra-ctlpln-identity, this branch)",
      "AWS documents ecs:RegisterTaskDefinition, events:PutTargets and lambda role changes as requiring iam:PassRole on the role named; the simulation (tests/simulate_policy.py) evaluates ecs:RegisterTaskDefinition with no role in context, so it cannot show this"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order: deny iam:PassRole unless a deploy path needs it, and say which; ALLOW ECS task definitions, services and EventBridge targets.",
  "world_is": "PassRole is denied (no path in the order's named acceptance needs it: Lambda UpdateFunctionCode, S3, SQS, DynamoDB, Logs need none), but ECS task-definition registration with a role, EventBridge targets with a role and Lambda role changes would fail for a Dell. Code-only deploys (UpdateFunctionCode, UpdateService on an existing task definition) are unaffected."
}
```

## NFRA_CTLPLN-W1-S2 -- A first terraform init of the new root with no lock file downloads the 700 MB aws provider

```json
{
  "id": "NFRA_CTLPLN-W1-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~1",
  "surfaced_at": "2026-10-07T03:26Z",
  "one_line": "A first terraform init of the new root with no lock file downloads the 700 MB aws provider from the registry and did not finish in 590 s on this laptop, so check_identity.py (init -backend=false) timed out under the 120 s bound until a lock file existed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "terraform init with TF_LOG=TRACE, this worktree, 2026-10-07: with no .terraform.lock.hcl it GETs releases.hashicorp.com/.../terraform-provider-aws_5.100.0_windows_amd64.zip rather than using plugin_cache_dir",
      "After copying infra/aws/terraform/bd-pipeline/.terraform.lock.hcl (aws 5.100.0, constraint ~> 5.0, same as the new root) the check ran init and validate in 20 s"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order: the check runs init -backend=false and validate; the lock file is in the paths grant.",
  "world_is": "The committed lock file is a copy of the sibling bd-pipeline lock for the same provider and constraint, not one produced by a fresh init in this root; terraform accepted it (init rc 0, validate Success)."
}
```

## NFRA_CTLPLN-S2 -- disarm of NFRA_CTLPLN-W1-S1: PassRole stays denied for round 2; the deny fails closed and loud; a narrow allow is the CTO's ruling

```json
{
  "id": "NFRA_CTLPLN-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T03:40Z",
  "one_line": "Issuer disarm of NFRA_CTLPLN-W1-S1: iam:PassRole stays explicitly denied in cloudops-dell-agent-deploy-policy for round 2; the hazard is a loud AccessDenied on a role-bearing Dell deploy, never a silent widening, and nothing is applied until site Z runs the root.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Merged @002f93bacd: dell_deploy_policy.json DenyEveryIamWrite includes iam:PassRole; issuer re-ran tests/simulate_policy.py in the worker tree: POLICY-SIM allowed_ok=8/8 denied_ok=11/11 all_ok=True",
      "The root is unapplied (no apply in round 2 until 0.0.0_AB_MSTR routes it to site Z), so no Dell holds any credential yet"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-b-1: deny iam:PassRole unless a deploy path needs it, and say which.",
  "world_is": "Worker named the paths that need it (role-bearing ECS, EventBridge, Lambda role change); none is in round 2's acceptance; code-only deploys are unaffected. DISARM (issuer): the deny stands (C-IDENTITY: a Dell can never change access; PassRole is an access-granting act). Whether a Dell may pass named roles (role ARNs + iam:PassedToService) is a contract change asked of 1.0.0_SA_CTO; until a ruling, a Dell's role-bearing deploy (ECS task definition with a role, EventBridge target with a role, Lambda role change) fails with AccessDenied and routes through site Z."
}
```

## NFRA_CTLPLN-S3 -- nfra-agentbus-port2 pins aws ~> 5.0 but declares max_message_size 1048576, which provider 5.100.0 rejects; the adoption root cannot plan

```json
{
  "id": "NFRA_CTLPLN-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T03:59Z",
  "one_line": "infra/aws/terraform/nfra-agentbus-port2 (the live laptop/site Z bus pair, adoption only) pins hashicorp/aws ~> 5.0 and sets max_message_size = 1048576; provider 5.100.0, the newest 5.x, rejects any value over 262144 at validation, so that root cannot init-validate-plan as written.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Worker 0.9.0_WK_NFRA_CTLPLN~3 @768fca164e: 'Error: expected max_message_size to be in the range (1024 - 262144), got 1048576' under provider 5.100.0 for the same attribute block",
      "Issuer read ~04:0xZ: both live queues agentbus-ajbdev-sitez-to-laptop.fifo and agentbus-ajbdev-laptop-to-sitez.fifo MaximumMessageSize 1048576, no RedrivePolicy; local plugin cache holds only aws 5.100.0",
      "nfra-agentbus-port2/main.tf line 45 version ~> 5.0; sqs.tf max_message_bytes local 1048576"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "nfra-agentbus-port2 is an adoption root: import + 0-diff against the live queues.",
  "world_is": "It cannot reach a plan under its own provider pin; nothing is applied from it, so the live queues are untouched. The new Dell root pins aws ~> 6.0 (CT-b-3 amendment 2, CTO-accepted msg 105948). The port2 pin is a later round's item when the laptop/site Z pair migrates (CTO ruling)."
}
```

## NFRA_CTLPLN-W3-S1 -- CT-b-3: the pinned AWS provider (hashicorp/aws ~> 5.0, resolved 5.100.0) refuses max_messa

```json
{
  "id": "NFRA_CTLPLN-W3-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~3",
  "surfaced_at": "2026-10-07T03:45Z",
  "one_line": "CT-b-3: the pinned AWS provider (hashicorp/aws ~> 5.0, resolved 5.100.0) refuses max_message_size = 1048576, so the dell1/dell2 queue root cannot plan as the order specifies.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "check_queues.py output, 2026-10-07 ~03:4xZ, rc=1: 'Error: expected max_message_size to be in the range (1024 - 262144), got 1048576'",
      "infra/aws/terraform/nfra-ctlpln-agentbus/.terraform.lock.hcl: aws 5.100.0, constraints ~> 5.0; plugin cache holds only 5.100.0",
      "infra/aws/terraform/nfra-agentbus-port2/IMPORT.md:62 and commit 45498eef9f (port2 never initialized)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-b-3 requires aws ~> 5.0 and max_message_size 1048576 (mirroring the live bus queues) and CT2b3-AC1 expects plan_add=2 plan_change=0 plan_destroy=0.",
  "world_is": "terraform plan in infra/aws/terraform/nfra-ctlpln-agentbus (provider 5.100.0, the latest 5.x) fails at validation: 'Error: expected max_message_size to be in the range (1024 - 262144), got 1048576' (sqs.tf line 37). No plan is produced, so CT2b3-AC1 is FAIL as written. The reference config infra/aws/terraform/nfra-agentbus-port2/sqs.tf carries the same 1048576 and was never initialized (commit 45498eef9f says 'NOT initialized/imported/applied'), so it would fail identically; its IMPORT.md line 62 also records the live value as carried on ONE measurement. Nothing was weakened or typed around: main.tf keeps ~> 5.0 and sqs.tf keeps 1048576.",
  "notes": "Decision for the issuer/CTO, not taken by the worker: either widen the provider constraint so a version that allows a 1 MiB queue message is selected (INFERRED, not tested here: a 6.x provider), or re-measure the live max_message_size and use that value. Either is an edit to main.tf or sqs.tf plus a re-run of check_queues.py; the check and the root are otherwise complete."
}
```

## NFRA_CTLPLN-W3-S2 -- The tailnet receive-side refusal covers `recv` and the aws-CLI fallback loop of `watch`, b

```json
{
  "id": "NFRA_CTLPLN-W3-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~3",
  "surfaced_at": "2026-10-07T03:45Z",
  "one_line": "The tailnet receive-side refusal covers `recv` and the aws-CLI fallback loop of `watch`, but not the primary watch path, which exec's .tools/agentbus-consumer.py.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C: cut a task order that grants .tools/agentbus-consumer.py so the same register check runs in the boto3 consumer",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git:f9f72d4fd4:.tools/agentbus-sqs.sh watch branch: exec \"$_PYBIN\" agentbus-consumer.py --queue-url ...",
      "git:f9f72d4fd4:.tools/agentbus-consumer.py line 136 prints and deletes every received message with no sender check"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-b-3 amendment 1: the receive path refuses a message whose sender tailnet name the register does not hold.",
  "world_is": "agentbus-sqs.sh `watch` exec's agentbus-consumer.py (the boto3 daemon) whenever python+boto3 exist, which is the normal case; that file is outside this order's paths, so the daemon still emits and deletes a message with an unregistered or absent sender tailnet name. The test covers recv only.",
  "notes": "Until the consumer carries the check, the refusal is in force on recv and the fallback loop only."
}
```

## NFRA_CTLPLN-W3-S3 -- A refused message is left on the FIFO queue; on a single-message-group queue that blocks l

```json
{
  "id": "NFRA_CTLPLN-W3-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~3",
  "surfaced_at": "2026-10-07T03:45Z",
  "one_line": "A refused message is left on the FIFO queue; on a single-message-group queue that blocks later mail, and every pre-stamp message counts as refused.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C: decide the refusal's end state (dead-letter or delete-with-record) and the cutover for unstamped in-flight mail before the stamped script is deployed to a box",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      ".tools/agentbus-sqs.sh send path at f9f72d4fd4, --message-group-id opal-sqschat (unchanged by this order)",
      "infra/aws/terraform/nfra-agentbus-port2/sqs.tf: no redrive_policy, no DLQ on either live queue"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-b-3 amendment 1: refuse, say why, leave no silent drop.",
  "world_is": "agentbus-sqs.sh sends every message in MessageGroupId opal-sqschat and the queues have no redrive policy. A refused message is not deleted (so nothing is silently dropped), but after its visibility timeout it returns at the head of the group, and a FIFO group delivers nothing behind an in-flight head. Also, a message sent by the old script carries no from_tailnet attribute and is refused as ABSENT, so mail in flight at deployment is refused until an owner clears it.",
  "notes": "SQS FIFO ordering semantics are carried from the service contract, not exercised here (the test stubs aws)."
}
```

## NFRA_CTLPLN-W3-S4 -- CT-b-3 amendment 2: lock regenerated with init -upgrade; AC2 run time margin

```json
{
  "id": "NFRA_CTLPLN-W3-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~3",
  "surfaced_at": "2026-10-07T04:12Z",
  "one_line": "CT-b-3 amendment 2: plain 'terraform init' refused the 5.100.0 lock under ~> 6.0 (needed -upgrade, lock regenerated to 6.67.0), and the AC2 suite takes ~101 s of the 120 s bound.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "terraform init output 2026-10-07: 'locked provider ... aws 5.100.0 does not match configured version constraint ~> 6.0; must use terraform init -upgrade'",
      "infra/aws/terraform/nfra-ctlpln-agentbus/.terraform.lock.hcl now version 6.67.0, constraints ~> 6.0",
      "pytest -q .tools/tests/test_agentbus_tailnet_stamp.py: 14 passed in 101.15s (measured, run beside check_queues.py)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-b-3 amendment 2: run terraform init once before the timed criterion run; keep the AC2 run under 120 s.",
  "world_is": "The init step needed -upgrade because the lock file from the first run pinned 5.100.0; the lock is in the order's paths and was regenerated locally (it is gitignored, **/.terraform.lock.hcl, so it is not committed; hashicorp/aws 6.67.0; 6.67.0 accepts max_message_size 1048576, check_queues.py plan_add=2 plan_change=0 plan_destroy=0). The AC2 suite is 14 bash-spawning tests at ~7 s each on this box (every send/recv resolves the register through a python start); 101 s leaves under 20 s of margin against the 120 s bound, so a slower box could exceed it.",
  "notes": "nfra-agentbus-port2/sqs.tf (not in this order's grant, never initialized) carries the same max_message_size 1048576 and would be refused by a 5.x provider; it needs a ~> 6.0 pin before any init there. Named here, not touched."
}
```

## NFRA_CTLPLN-S4 -- disarm of NFRA_CTLPLN-W3-S2 and NFRA_CTLPLN-W3-S3: the consumer path checks, and refused mail is recorded then deleted, merged @c649197dd0

```json
{
  "id": "NFRA_CTLPLN-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T04:31Z",
  "one_line": "Issuer disarm of NFRA_CTLPLN-W3-S2 (the watch path's agentbus-consumer.py did not check the sender's tailnet name) and NFRA_CTLPLN-W3-S3 (a refused message left on a one-group FIFO queue blocks later mail; unstamped mail from not-yet-updated boxes): both fixed under CT-b-3 amendment 2 and merged @c649197dd0.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Merged @c649197dd0 (worker commits 221ee5b0b6, 2d01d40c9e): agentbus-consumer.py applies the same sender check as recv; an unheld sender's message is written to org/mcp/inbox/_agentbus_refused/<UTC>_<id>.json, a REFUSED line printed, then deleted; an unstamped message is delivered with a WARN line",
      "Issuer re-ran in the worker tree: pytest .tools/tests/test_agentbus_tailnet_stamp.py 14 passed in 81.54s (the consumer tests run the script as a subprocess against a stub boto3 that records deletes); bash -n and py_compile clean"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-b-3 amendment 2 items 2 and 3; CTO acceptance msg 105948 with a sunset: once all four boxes run the stamping script (four versions printed), unstamped mail is refused like any unknown sender.",
  "world_is": "Both hazards are closed in code on CLOUD. DISARM (issuer): the remaining open item is the CTO's sunset, carried to round 3's enrichment list: print the stamping script version on all four boxes, then flip unstamped mail to refused. The register check is written twice (jq in the shell script, Python in the consumer), noted by the worker; one shared reading is a later repair."
}
```

## NFRA_CTLPLN-W5-S1 -- dell1 and dell2 enter the gate's enum; one COMPARES reader and one enum copy outside the grant still admit two values

```json
{
  "id": "NFRA_CTLPLN-W5-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~5",
  "surfaced_at": "2026-10-07T06:45:44Z",
  "one_line": "With dell1 and dell2 in the gate's FABRIC_ENUM, one two-way COMPARES reader and one second enum carrier outside the CT-c-6 grant still admit only laptop and site-z.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C: amend the grant (or cut a cell) so .tools/surprise-row-gate.py:2042-2054 and org/standards/PRD_HEADER.schema.json:20 handle dell1 and dell2 before any project.json row is flipped to a Dell fabric",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git:wk-NFRA_CTLPLN-5:.tools/surprise-row-gate.py:2042 id_fabric = \"site-z\" if (m and m.group(\"z\")) else \"laptop\"; :2051 refuses a new row whose fabric != id_fabric, so a row with fabric dell1 or dell2 (no Z- infix in its id) is refused as 'fabric=dell1 but the id lacks the Z- infix, which means laptop' (COMPARES, two-way branch on the pair)",
      "git:wk-NFRA_CTLPLN-5:org/standards/PRD_HEADER.schema.json:20 \"enum\": [\"laptop\", \"site-z\"] (ENUM-SOURCE, a second carrier of the allowed set, described as the same enum as the gate's FABRIC_ENUM)",
      "python .tools/tests/fabric_value_census.py -> FABRIC-CENSUS files_scanned=1692 hits=53 enum_source=5 compares=1 display=33 fixture=14 unclassified=0 ok=True; the ENUM-SOURCE hits are to-pipeline-gate.py:93 (edited), DEVICES.json:42,44,47 (register, not mine) and PRD_HEADER.schema.json:20",
      "readers that handle a Dell by construction (not rowed): .tools/sequence-check.py:346-348 compares fabric with hyphens stripped against the box name from the device register; :301 compares the file's fabric to the register row's; capacity() looks up caps.get(box) and reads None for a box with no cap"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-c-6 step 3: every COMPARES hit outside the two-file grant is listed in the record and rowed once, the issuer amends the grant.",
  "world_is": "The census (rule-24 record in deliverables/0.9.0_WK_NFRA_CTLPLN~5/FABRIC_ENUM_RULE24_RECORD.md) found ONE COMPARES line outside the grant: .tools/surprise-row-gate.py:2042 (id_fabric derived from the Z- id infix, then row fabric must equal it; a Dell-box row filed with its true fabric is refused). One ENUM-SOURCE outside the grant also lags: org/standards/PRD_HEADER.schema.json:20 (a PRD header fabric of dell1 or dell2 fails the schema). Neither fires today: no project.json row carries a Dell fabric (the rows are the CTO's). Census blind spot: a reader that compares fabric without the token site-z within three lines of the word fabric is not in the hit list; only the readers above were read."
}
```


## NFRA_CTLPLN-W4-S1 -- CT-c-1: sqs:SetQueueAttributes and sns:SetTopicAttributes are allowed and each can set a resource policy

```json
{
  "id": "NFRA_CTLPLN-W4-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T06:47:09Z",
  "one_line": "The create grant allows sqs:SetQueueAttributes and sns:SetTopicAttributes (an update needs them), and each sets a resource policy as one attribute among many, so access-granting is not separable from the update by action name.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO: rule on whether the two actions stay allowed before the Dell group policy is applied at site Z",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell_create_policy.json and tests/derive_resource_kinds.py in infra/aws/terraform/nfra-ctlpln-identity/ on branch wk-NFRA_CTLPLN-4: Allow statement CreateUpdateTagDataAndMessaging lists sqs:SetQueueAttributes and sns:SetTopicAttributes",
      "PRD v0.8 / TO-CT-c-1 item 2 names both as inseparable from access by action name and orders them allowed with one row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-1: allow the two actions (an update needs them) and file ONE row naming both; the access-granting actions (sqs:AddPermission, sns:AddPermission) stay unallowed.",
  "world_is": "With the policy applied, a Dell can call SetQueueAttributes(Attributes={Policy: ...}) on any queue and SetTopicAttributes(AttributeName=Policy) on any topic, which grants any principal access to that queue or topic, the same effect as the unallowed sqs:AddPermission and sns:AddPermission. The policy file is not applied by this order, so the hazard is latent until the group policy is applied."
}
```

## NFRA_CTLPLN-W4-S2 -- CT-c-1: create-time access carriers: kms:CreateKey, sqs:CreateQueue, sns:CreateTopic and s3:CreateBucket take a policy or grant at creation

```json
{
  "id": "NFRA_CTLPLN-W4-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T06:47:09Z",
  "one_line": "Four allowed create actions carry access at creation (kms:CreateKey with a key Policy, sqs:CreateQueue and sns:CreateTopic with a Policy attribute, s3:CreateBucket with ACL grant headers), so the unallowed kms:PutKeyPolicy, sqs/sns:AddPermission and s3:PutBucketPolicy are reachable at create time on a NEW resource.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO: rule whether create-time policy parameters are in or out of the open access-granting question before the group policy is applied",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell_create_policy.json and tests/derive_resource_kinds.py in infra/aws/terraform/nfra-ctlpln-identity/ on branch wk-NFRA_CTLPLN-4: Allow actions kms:CreateKey, sqs:CreateQueue, sns:CreateTopic, s3:CreateBucket; tests/simulate_policy.py shows kms:PutKeyPolicy implicitDeny while CreateKey is allowed (service API contract, not exercised here)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-1: no allowed action grants access; the access-granting actions are unallowed.",
  "world_is": "The four create actions are required by the derived kinds (aws_kms_key, aws_sqs_queue, aws_sns_topic, aws_s3_bucket). Each service's create call accepts a policy or ACL parameter that the action name does not separate. It reaches only a resource the Dell is creating, not an existing one. Not exercised against AWS; carried from the service API contracts."
}
```

## NFRA_CTLPLN-W4-S3 -- CT-c-1: existing Deny statements block the update of two derived kinds

```json
{
  "id": "NFRA_CTLPLN-W4-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T06:47:09Z",
  "one_line": "Two of the four byte-identical Deny statements block an update the create grant is for: cloudtrail:UpdateTrail and cloudtrail:PutEventSelectors (aws_cloudtrail), and s3:PutLifecycleConfiguration on opal-data-* (aws_s3_bucket_lifecycle_configuration).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "tests/derive_resource_kinds.py prints [DENY-BLOCKED ...] on aws_cloudtrail and aws_s3_bucket_lifecycle_configuration; DenyCloudTrailWrites (cloudtrail:Update*, Put*) and DenyS3DeletesOnProductionData (s3:PutLifecycleConfiguration on opal-data-*) in dell_deploy_policy.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-1: create, update and tag for every GRANT kind; the four Deny statements are kept byte-identical.",
  "world_is": "An explicit Deny overrides any Allow, so a Dell can create a trail (cloudtrail:CreateTrail is allowed) but cannot update it, and cannot apply a lifecycle configuration to an opal-data-* bucket (the derived roots declare opal-data-* buckets in shared-infra, bd-pipeline, investor-reporting, cot-pipeline). The create actions the criterion checks are covered; the update of those kinds is not."
}
```

## NFRA_CTLPLN-W4-S4 -- CT-c-1: the read side of the derived kinds is absent for 10 services and part of s3; an apply refreshes before it writes

```json
{
  "id": "NFRA_CTLPLN-W4-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T06:47:09Z",
  "one_line": "ReadOnlyForTerraformPlan has no Get/List/Describe for apigateway, cloudfront, codebuild, cur, route53, scheduler, secretsmanager, ses, ssm and wafv2, and s3 has no GetEncryptionConfiguration or GetLifecycleConfiguration, so a Dell apply of the derived roots fails at refresh even though every create is allowed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python check over dell_deploy_policy.json Allow actions per service of the GRANT table, 2026-10-07: apigateway, cloudfront, codebuild, cur, route53, scheduler, secretsmanager, ses, ssm, wafv2 have no read action; s3 reads are GetObject*, GetBucket*, ListBucket* only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-1 grants create, update and tag only; reads were not named in the order.",
  "world_is": "The order grants create, update and tag. Terraform reads each resource (apigateway:GET, cloudfront:Get*, scheduler:Get*, secretsmanager:Describe*, wafv2:Get*, s3:GetEncryptionConfiguration and so on) before and after a write. Not added here (widening the order; secretsmanager:Get* would include GetSecretValue)."
}
```

## NFRA_CTLPLN-W4-S5 -- CT-c-1: iam:PassRole is denied, so every derived kind that takes a role cannot be created by a Dell

```json
{
  "id": "NFRA_CTLPLN-W4-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T06:47:09Z",
  "one_line": "Kinds that pass a role at create (aws_lambda_function, aws_scheduler_schedule, aws_codebuild_project, aws_instance with an instance profile, aws_lambda_event_source_mapping) need iam:PassRole, which DenyEveryIamWrite denies, so their create actions are allowed and still fail for a Dell.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell_deploy_policy.json DenyEveryIamWrite lists iam:PassRole; tests/simulate_policy.py iam:PassRole -> explicitDeny with dell_create_policy.json present; the TO names iam:PassRole as an open question above the order"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-1: do not allow iam:PassRole and add no new Deny; the roles are an open question above this order.",
  "world_is": "The criterion proves the create actions are allowed (lambda:CreateFunction allowed on the simulator) and not that the call succeeds. For role-bearing kinds the call carries a role ARN and the service checks iam:PassRole on it. Carried from the service contracts, not exercised."
}
```

## NFRA_CTLPLN-S5 -- disarm of NFRA_CTLPLN-W5-S1; apply condition for NFRA_CTLPLN-W4-S1 and W4-S2: no Dell-fabric row exists and the create policy is not applied

```json
{
  "id": "NFRA_CTLPLN-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T06:55Z",
  "one_line": "Issuer disarm of NFRA_CTLPLN-W5-S1, and the apply condition for NFRA_CTLPLN-W4-S1 and NFRA_CTLPLN-W4-S2: none of the three hazards is live because no project row carries a Dell fabric and the create policy is not applied; each is tied to the act that would arm it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Read 2026-10-07 ~06:5xZ: 42 project.json rows under org/missions, 0 with a fabric value starting dell (W5-S1 fires only on a row filed from a Dell-fabric project)",
      "CT-c-1 merged @7091ecaecc and NOT APPLIED: the create policy document exists only in the repo; the live group carries the round-2 policy (site Z apply, msg 105980)",
      "CTO msg 106014 (PRD v0.10): bucket policies, key policies and Lambda permissions go through the C-ROLE-REQUEST write-in; their Deny statements are a cell for the next issuance"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-c-6: every reader of a fabric value handles dell1 and dell2. CT-c-1 / PRD v0.7-v0.10: a Dell creates non-IAM resources and never changes access; access-granting resource policies go through the laptop.",
  "world_is": "W5-S1 DISARM (issuer): the surprise-row gate (lines 2042-2051) and the PRD header schema (line 20) still know two fabrics; both are outside CT-c-6's grant. No row is flipped to a Dell fabric until both are repaired: the repair is one cell of the next issuance, and 1.0.0_SA_CTO (whose register the rows are) is told in one line naming this row. W4-S1 and W4-S2 (the second owned by 1.0.0_SA_CTO): sqs:SetQueueAttributes, sns:SetTopicAttributes and the create calls for a key, queue, topic and bucket can carry an access policy that no action name separates. They arm only at the apply of the create policy. The issuer does not route that apply until the never-widen pair for it names these four create calls and two attribute calls and the CTO half rules them in or out; that ruling and the next issuance's Deny cell (msg 106014) are one decision."
}
```

## NFRA_CTLPLN-Z-S1 -- halt-gate's principal resolver refuses a multi-letter lane, and its banner prescribes the one remedy that would turn the refusal into a false PASS

```json
{
  "id": "NFRA_CTLPLN-Z-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~RV",
  "surfaced_at": "2026-10-07T05:05Z",
  "one_line": "halt-gate-check.sh's principal resolver admits a SINGLE-uppercase-letter lane only, so every multi-letter-lane seat is refused fail-closed on safe-apply / safe-ec2-deploy -- and the banner it prints misdiagnoses the refusal as a CORRUPTED session serial file and tells the operator to overwrite it, which is the one act that would convert this loud refusal into a silent false PASS.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/halt-gate-check.sh:172-174 -- '(1) the BASE serial must match an agent home folder under the tier dirs; (2) a ~lane suffix must be a single uppercase letter (every fabric lane is: ~A..~E, ~Z; \"Zn\" is exactly the corruption shape that got through)'",
      "Measured 2026-10-07 ~04:58Z: safe-apply of infra/aws/terraform/nfra-ctlpln-identity as 0.7.0_AE_CloudOps~RV printed 'HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed)' and terraform was never invoked",
      "The serial is NOT corrupt: it is the <issued_to> of org/tier2_senior/0.7.0_AE_CloudOps~RV/task_orders/NFRA_CTLPLN.TO-DELL-1.dell-identity-apply-site-z.md, the executor named by BOTH never-widen halves, and the addressee of GO msg 30579 (acked). org/mcp/sessions/471a9973-0b57-41d2-a496-adc2fa5545b8.serial reads it exactly",
      "SCOPE: 4 of the 14 serial rows in org/mcp/liveness.json carry a multi-letter lane -- 0.7.0_AE_CloudOps~RV, 2.0.0_SA_COO~AI, 2.0.0_SA_COO~RV, 3.0.0_SA_CVO~RV. That 14 bounds the SAMPLE only; the regex at :174 bounds the INFERENCE, and it refuses ANY multi-letter lane, seated or not, now or later",
      "A second, independent cause was ruled out by exercise, not by reading: the first refusal came from a sparse worktree whose cone lacked org/tier2_senior/, so check (1) could also have fired. org/tier2_senior/0.7.0_AE_CloudOps/ was added to the cone and the refusal REPRODUCED, which localises it to check (2)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-DELL-1 step 5 and the CTO half's section 2: ONE safe-apply of the root. CLAUDE.md NEVER-9 and Deployment Rule 18: safe-apply is the only admitted apply path, and its HALTGT checkpoint is expected to evaluate the acting seat's own inbox.",
  "world_is": "The apply path is closed to a multi-letter-lane seat. It was cleared here by safe-apply's own audited escape, HALT_OVERRIDE, with the reason naming this defect; the apply then ran once and landed 10 added / 0 changed / 0 destroyed. NO halt-gate PASS is claimed or cited anywhere in the evidence: the condition the checkpoint exists to enforce was measured by the sound instrument instead -- broker check_inbox empty, 20 of 20 delivery rows READ and acked by this serial, 0 STOP/HALT-class across all 20 -- which is also what CLAUDE.md Rule 22a's DELIVERY line and ADHC_HALTGT already prescribe ('NOBODY CITES A HALTGT PASS'; a ~lane agent is unhaltable regardless). THE HAZARD IS THE BANNER, NOT THE REFUSAL: the refusal is loud and correct-ish, but the banner's prescribed remedy is to rewrite the session serial file, and a seat that complies by writing a single-letter lane would make the gate scan ANOTHER agent's inbox and exit 0 -- the false-negative shape the gate's own comments at :143-152 condemn ('A SAFETY GATE THAT CANNOT NAME ITS OWN PRINCIPAL MUST NOT GUESS'). The remedy would manufacture the fault it cures.",
  "notes": "Disarm is a one-line widening of the lane pattern at halt-gate-check.sh:174 to one-or-more uppercase letters, plus a banner branch that names a VALID-BUT-UNADMITTED lane separately from a CORRUPT serial so the prescribed remedy is never 'overwrite your serial file'. .tools/ is outside this order's <paths>, so this seat names it and does not touch it. The same resolver contract is cited as shared with inbox-watch.sh:82-89 and agent-poller.py _find_agent_folder, so the fix is checked against those two before it lands -- my inbox watcher DOES deliver to ~RV, so at least inbox-watch.sh does not carry the same restriction, and that asymmetry is itself the tell that :174 is the outlier."
}
```

## NFRA_CTLPLN-Z-S2 -- disarm of NFRA_CTLPLN-Z-S1: the refusal was unknown-base from a sparse cone, reproduced; the letter count never refused ~RV

```json
{
  "id": "NFRA_CTLPLN-Z-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~Z",
  "surfaced_at": "2026-10-07T06:08:11Z",
  "one_line": "Disarm of NFRA_CTLPLN-Z-S1 by its disarm_owner, on a reproduction and not on the fix: the 04:58Z halt-gate refusal of 0.7.0_AE_CloudOps~RV was check (1), unknown-base, from a sparse worktree whose cone lacked the seat's home folder; the letter count never refused ~RV. The misleading banner, the row's real hazard, is gone @1f1bacdf66.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Reproduction by this seat 2026-10-07 ~06:1xZ, a fresh detached sparse worktree at EXACTLY 0ef817adb0 (the commit the seat applied from), HALT_GATE_REPO_ROOT set to it, serial 0.7.0_AE_CloudOps~RV. Cone WITHOUT org/tier2_senior: the new gate file (@1f1bacdf66) reads rc=1 reason unknown-base; the gate file AT 0ef817adb0 reads rc=1. Cone WITH org/tier2_senior/0.7.0_AE_CloudOps: the new file reads rc=0; the file AT 0ef817adb0 reads rc=0. Control: ~QQ on the new file reads rc=1 reason lane-no-inbox.",
      "The gate file at 0ef817adb0, line 223, admits one, two or three uppercase letters; 64a3ef4b4e (the 1-to-3 rule) is an ancestor of 0ef817adb0 (merge-base --is-ancestor, with a positive control on the same instrument). So no copy of the gate the seat could have run refused ~RV on its lane.",
      "2.0.0_SA_COO~O msg 30636 measured the same on the shared tree (rc=0 for ~RV, rc=1 for ~Zn). 1.0.0_SA_CTO~Z ruling ADDENDUM 1 @24ef9e0791 asked for this read before the disarm.",
      "The fix, 0.0.0_AB_MSTR~Z @1f1bacdf66: the lane check is uppercase letters plus the existence of the lane's inbox; the refusal names which check failed and says a sparse worktree can give unknown-base for a real seat; the line that overwrote the session serial file is out of the banner. Falsifier .tools/halt-gate-lane-test.sh re-run by this seat: 10 of 10.",
      "NOT reproduced: Z-S1's fifth evidence line (the refusal persisting after org/tier2_senior/0.7.0_AE_CloudOps/ joined the cone). By this seat's run the old gate admits the seat once that folder is present. What differed in the seat's second attempt is unread; the seat's worktree now carries all of org/tier2_senior (76 folders)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "NFRA_CTLPLN-Z-S1: the halt gate's principal resolver refuses a multi-letter lane. CTO ruling CTO_RULING_HALT_GATE_MULTI_LETTER_LANE_20261007.md and its ADDENDUM 1: close the row on a read of the named check from a sparse worktree, not on the fix.",
  "world_is": "DISARM (disarm_owner). The refusal was unknown-base: a sparse cone without the acting seat's home folder under org/tier2_senior. The remedy for an apply from a sparse worktree is the cone (add the seat's base home folder), and the gate now says so in its banner. Both Dell applies ran under the audited HALT_OVERRIDE and cite no halt-gate pass; nothing in the world depends on this row. Z-S1's diagnosis (letter count) is superseded by this row; its hazard (a banner prescribing a serial-file overwrite) is closed in code in the shared tree, and a worktree gets it at its next cut."
}
```

## NFRA_CTLPLN-S6 -- the CTO's rulings on NFRA_CTLPLN-W4-S1 to W4-S4, carried by the issuer: S1 and S2 allowed, S3 stands, S4 fixed before the apply

```json
{
  "id": "NFRA_CTLPLN-S6",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T07:15Z",
  "one_line": "The CTO's rulings on rows NFRA_CTLPLN-W4-S1 to NFRA_CTLPLN-W4-S4, carried into the channel by the issuer at the CTO's ask (msg 106017): S1 and S2 stay allowed, S3's two Deny statements stand, S4's read actions land before the apply.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_CT_c_1_DELL_CREATE_GRANT_20261007.md @bb0e587e22: the rulings table and the CTO never-widen half for the Dell create grant, SIGNED on three conditions",
      "CT-c-1 reopened by the issuer for W4-S4 (AMENDMENT 1, commit f51fb64cc4 on wk-NFRA_CTLPLN-4): one read-only statement, no read that returns secret material",
      "CT-c-1 merged @7091ecaecc and NOT APPLIED at the time of this row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.10 C-IDENTITY: a Dell creates non-IAM resources; the laptop administers access-granting resource policies (Andrew, card 2: 'For now, laptop should admin').",
  "world_is": "RULED by 1.0.0_SA_CTO (org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_CT_c_1_DELL_CREATE_GRANT_20261007.md @bb0e587e22). W4-S1: sqs:SetQueueAttributes and sns:SetTopicAttributes STAY ALLOWED; IAM has no condition separating the Policy attribute. W4-S2: the four create actions (key, queue, topic, bucket) STAY ALLOWED, policy parameter included; the reach is a resource the Dell is itself creating. For these six actions no cloud refusal backs the laptop-administers rule: the rule on a Dell is the write-in, and the mechanism is stated by the CTO as absent. W4-S3: the CloudTrail and opal-data lifecycle Deny statements STAND; those two acts go through the laptop write-in. W4-S4: the read actions the derived kinds need are added before the apply, read-only only; this is condition 2 of the CTO half and the issuer has reopened CT-c-1 for it. This row replaces the apply condition stated in NFRA_CTLPLN-S5 for W4-S1 and W4-S2: the apply now waits on the three conditions of the CTO half and the issuer's own half, nothing else."
}
```

## NFRA_CTLPLN-W4-S6 -- A refresh of aws_ssm_parameter and aws_secretsmanager_secret_version needs a read that returns the value (ssm:

```json
{
  "id": "NFRA_CTLPLN-W4-S6",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T07:05:44Z",
  "one_line": "A refresh of aws_ssm_parameter and aws_secretsmanager_secret_version needs a read that returns the value (ssm:GetParameter, secretsmanager:GetSecretValue); the amendment-1 read statement does not grant them, so a plan from a Dell cannot refresh those two kinds and their refresh is left to the laptop.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell_create_policy.json statement ReadForDerivedKinds @this branch grants secretsmanager:DescribeSecret, GetResourcePolicy, List* and ssm:DescribeParameters, DescribeDocument*, GetDocument, ListTagsForResource only",
      "derive_resource_kinds.py last line read_held=2 (aws_ssm_parameter, aws_secretsmanager_secret_version)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-1 AMENDMENT 1 step 1: grant read actions the derived kinds need, but never a read that returns secret material; file ONE row saying a refresh of an aws_ssm_parameter needs ssm:GetParameter and is therefore left to the laptop.",
  "world_is": "tests/derive_resource_kinds.py READ_HELD names two GRANT kinds in the derived tree: aws_ssm_parameter (refresh reads ssm:GetParameter, which returns the value) and aws_secretsmanager_secret_version (refresh reads secretsmanager:GetSecretValue, which returns the value; the order names only the first, the second is the same shape and is held on the same rule, so this row names both). Neither read is allowed (tests/simulate_policy.py secretsmanager:GetSecretValue -> implicitDeny). A terraform plan or apply from a Dell on a root that holds either kind will fail at refresh until the CTO rules a different treatment; the derivation prints them as READ-HELD and does not count them unread. Carried from the provider's read behaviour, not exercised."
}
```

## NFRA_CTLPLN-W4-S7 -- The existing read statement grants sqs:GetQueueAttributes and sqs:GetQueueUrl only on the four agentbus queues

```json
{
  "id": "NFRA_CTLPLN-W4-S7",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T07:05:44Z",
  "one_line": "The existing read statement grants sqs:GetQueueAttributes and sqs:GetQueueUrl only on the four agentbus queues, so a refresh of aws_sqs_queue from a Dell fails for any other queue; the worker added those two read actions to ReadForDerivedKinds on Resource *, a read the amendment did not list.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell_deploy_policy.json lines 23-32 and 34-45 read at HEAD f51fb64cc4",
      "derive_resource_kinds.py READ[aws_sqs_queue] and the policy statement ReadForDerivedKinds @this branch"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-1 AMENDMENT 1 step 1 lists apigateway, cloudfront, codebuild, cur, route53, scheduler, secretsmanager, ses, ssm, wafv2 and two s3 reads as the gaps; sqs is not listed.",
  "world_is": "dell_deploy_policy.json AgentbusSendToInboundQueues allows sqs:GetQueueUrl and sqs:GetQueueAttributes on four agentbus ARNs only, and ReadOnlyForTerraformPlan holds sqs:List* only; the READ table for aws_sqs_queue (sqs:GetQueueAttributes, sqs:GetQueueUrl, sqs:ListQueueTags) is therefore not satisfied for a queue the Dell creates. The worker also added s3:GetAccelerateConfiguration, GetReplicationConfiguration, GetObjectLockConfiguration and GetObjectTagging for the aws_s3_bucket and aws_s3_object refresh, all Get-verb. sqs:GetQueueAttributes can return a queue's Policy attribute (a read of access, not a write); the CTO may strike the two sqs actions, in which case the sqs kind joins READ_HELD. Not exercised against a real refresh."
}
```

## NFRA_CTLPLN-W4-S8 -- one PassedToService list for all named roles

```json
{
  "id": "NFRA_CTLPLN-W4-S8",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T07:15:57Z",
  "one_line": "The rendered AllowPassNamedRoles carries one iam:PassedToService list for ALL named roles, so with two applied roles for different services each role may be passed to either service; the order specifies this shape.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "tests/render_passrole.py render(): one Allow statement, Resource = sorted ARNs, Condition StringEquals iam:PassedToService = sorted distinct services; scratch run with two applied records (alpha for ec2.amazonaws.com, zeta for lambda.amazonaws.com) rendered Resource [alpha, zeta] with services [ec2.amazonaws.com, lambda.amazonaws.com]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-3 build step 1: AllowPassNamedRoles has Resource = the same sorted ARNs and Condition StringEquals iam:PassedToService = the sorted distinct services of those records.",
  "world_is": "The pairing of role to service is lost in the single statement: with N applied roles over M services, every role may be passed to every one of the M services. It is inert today (zero applied records, no Allow statement is written) and the one-fixture simulation cannot show it. A per-role statement (one Allow per applied record, its own Resource and its own service) would hold the pairing and costs one statement per role against the 6,144 limit. Not changed: the order specifies the single statement. Exercised only by the scratch run named in the evidence, not against the cloud's evaluator."
}
```

## NFRA_CTLPLN-W4-S9 -- BOUNDS section truncated in the order file

```json
{
  "id": "NFRA_CTLPLN-W4-S9",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T07:27:50Z",
  "one_line": "The BOUNDS section of NFRA_CTLPLN.TO-CT-c-5 is truncated in the committed order file: it ends at 'Grant. The `<paths>' and carries no no-apply clause, no allowed-AWS-calls clause and no refusal clause; the worker acted on the dispatching message's statement of the bounds.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-c-5.lambda-scope-narrowing.md lines 82-94 at HEAD 119586d184: the BOUNDS bullet 'Grant.' is cut after the opening of the paths tag, the paths block follows directly, and no later bullet exists; CT-c-1 and CT-c-3 carry four full bullets"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-5 BOUNDS (per the dispatching message): read-only AWS inspection calls (function, authorizer, distribution and region listings) are allowed and nothing else; no apply; refusal clause as in the sibling orders.",
  "world_is": "The order file as committed states none of that. The worker made only list/get/describe calls through .tools/aws (ec2 describe-regions; lambda list-functions, apigatewayv2 get-apis and get-authorizers, apigateway get-rest-apis and get-authorizers per region; cloudfront list-distributions), no write call and no apply, and wrote only the paths the order's paths block names. The cause (the paths tag inside the bullet text swallowed the rest of the section when the order was cut) is carried from the file's shape, not exercised. Repair of the order file is the issuer's."
}
```

## NFRA_CTLPLN-W4-S10 -- CT-c-5 blocked at commit by the naming limb

```json
{
  "id": "NFRA_CTLPLN-W4-S10",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T07:27:50Z",
  "one_line": "CT-c-5 passes its three criteria in the worktree but cannot be committed: the commit's naming limb (LGIC_ENFORCE DEC-6, ENFORCE) refuses every NEW hand-kept firm-token function name in dell_deploy_policy.json, protected_functions.json and protected_functions_listing.json, and the order's grant carries no registry path to read them through; the order is left pending.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh run on HEAD 119586d184 with the five CT-c-5 paths: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode)', NAMING-GATE: REFUSE 153 graded, 136 NAMING REFUSE lines; recorded in org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~4/NFRA_CTLPLN.TO-CT-c-5.blocked_attempt.outputs.txt",
      ".tools/naming-gate.py lines 21-26: a firm or product token is permitted only in infra/logic/registry/*.json, a generated block or file, the arguments of key()/address()/name()/lookup(), or an opal_name module call; anywhere else a NEW string carrying one is refused",
      "the whole attempt (script, rendered statement, saved census, simulation block) is preserved as org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~4/NFRA_CTLPLN.TO-CT-c-5.blocked_attempt.patch"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-5: the protected list is derived by census and the Deny statement is rendered from protected_functions.json into dell_deploy_policy.json, each protected function ARN and the same ARN with :*; the census is saved beside the policies for the bounded run.",
  "world_is": "Two of the 15 protected functions have names that carry firm tokens (a bd and a cot name), and the saved census lists all 233 function names, 100 or more of them with a firm token. The rendered policy needs the literal ARN of a function, and a policy file cannot call lookup(). Without a waiver the gate refuses the commit of the three data files, so the criteria cannot hold at any committed HEAD. In the worktree, uncommitted, the three criteria printed: CT3c5-AC1 'PROTECTED-CENSUS functions=233 regions=17 refused_regions=0 protected=15 by_authorizer=1 by_edge=5 name_only=9 in_sync=True ok=True'; CT3c5-AC2 'POLICY-SIM allowed_ok=21/21 denied_ok=18/18 passrole_ok=5/5 protected_ok=8/8 all_ok=True'; CT3c5-AC3 'IDENTITY-STATIC ... names_from_builder=7/7 policy_size_ok=True ok=True' (deploy policy 5532 of 6144). The worker did not weaken a criterion, did not touch org/mcp/naming-gate.enforce and did not use any override. Ways forward that are not the worker's to take: an R20 declared exception or a NAMING_LEGACY_READS entry for the literals (org/standards and the register are outside the grant), a registry row that lets the renderer read the names through lookup() (infra/logic/registry is outside the grant), or an order that moves the saved census under a tests/ path (the gate does not grade strings under */tests/*) while the two firm-token ARNs in the policy remain a CTO or issuer ruling."
}
```

## NFRA_CTLPLN-W4-S11 -- CT-c-5: the /apikeys simulator arm cannot discriminate the Deny

```json
{
  "id": "NFRA_CTLPLN-W4-S11",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~4",
  "surfaced_at": "2026-10-07T07:42:11Z",
  "one_line": "CT-c-5 AMENDMENT 3's denied arm on the bare ARN /apikeys cannot discriminate the new Deny: iam:SimulateCustomPolicy matches no statement at all for it and returns implicitDeny, so the arm is graded implicitDeny and the Deny is shown on /apikeys/<id>.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "SimulateCustomPolicy, apigateway:GET on arn:aws:apigateway:us-east-1::/apikeys with the three real policy documents: implicitDeny, MatchedStatements empty; the same with DenyApiKeyReads removed from the deploy policy: implicitDeny, MatchedStatements empty (the Allow on * matches /apis and /apikeys/abc but not /apikeys)",
      "same call on /apikeys/abc: explicitDeny with the Deny (matched PolicyInputList.1), allowed without it (matched PolicyInputList.2)",
      "infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py: the arm is kept at the order's resource with required decision implicitDeny (the file's own rule counts either deny decision as denied), and an uncounted APIKEY-ITEM-PROBE line prints the /apikeys/x decision (explicitDeny)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-c-5 AMENDMENT 3 item 4: the first simulation block gains one DENIED arm, apigateway:GET on arn:aws:apigateway:us-east-1::/apikeys, as evidence that the typed DenyApiKeyReads statement denies the key read.",
  "world_is": "The simulator treats the bare collection ARN as matching no statement, Allow or Deny, so the arm returns implicitDeny with or without the Deny statement and proves nothing about it; the statement does deny the item ARN /apikeys/<id> (explicitDeny). Whether real IAM evaluates the list call GET /apikeys against the bare ARN (the statement lists it, so it would match) is carried from the policy text, not exercised: no AWS call that lists API keys was made. The count 19/19 holds as ordered; the issuer may prefer the arm on /apikeys/<id> with explicitDeny."
}
```

## NFRA_CTLPLN-S7 -- dell2 box user cannot read the graph token; comp-blast dead on dell2

```json
{
  "id": "NFRA_CTLPLN-S7",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T08:02:00Z",
  "one_line": "On dell2 the box user cloudops-dell2-agent-user cannot read secret opal/mcp/graph-read-token, so comp-blast (the served dependency graph) fails on every call there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2, 2026-10-07 ~08:0xZ: `comp-blast irpt-export-render` -> TOOL-FAILED: ProjectionClientError ... AccessDeniedException ... User: arn:aws:iam::313476888478:user/cloudops-dell2-agent-user is not authorized to perform: secretsmanager:GetSecretValue on resource: opal/mcp/graph-read-token because no identity-based policy allows the secretsmanager:GetSecretValue action; comp-blast does not fall back"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CLAUDE.md rule 20 and org/XXX.md (COO minimum): a seat queries the dependency graph (comp-blast) before decomposing or changing cloud/infra; the Dell box users are this project's (round 2: the AWS user per box).",
  "world_is": "On dell2 the graph query is refused at the secret read, so every dell2 seat's rule-20 check is a coverage limitation, not a result. Not exercised on dell1. The grant (or a different bearer path for the Dells) is this project's to decide; 2.0.0_SA_COO~K2 recorded the gap in its IRPT_CUSTDY decomposition and kept working."
}
```

## NFRA_CTLPLN-S8 -- dell1 came up with one of the repo's git hooks; every seat's commit there ran ungated until 07:3xZ

```json
{
  "id": "NFRA_CTLPLN-S8",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-07T07:35Z",
  "one_line": "The new-device bring-up left dell1 with only the owned-paths pre-commit hook: no pre-push deploy gate, no law lock, no to-pipeline gate, no surprise-row gate. dell1's fabric manager ran .tools/install-all-git-hooks.sh at ~07:3xZ.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell1 2026-10-07 ~07:3xZ: git rev-parse --git-path hooks = .git/hooks, holding pre-commit only (non-sample files)",
      "a push of q/dell1/ARMS/r1 at ~07:3xZ printed no pre-push line at all",
      "after bash .tools/install-all-git-hooks.sh on dell1: commit-msg, post-commit, pre-commit, pre-push live; HOOK BODIES 20 total / 19 wired / 1 ORPHANED (prd-header-notify-post-commit.sh, no installer references the body)",
      "the kit's README_NEW_DEVICE.md (Opal_New_Device_Kit_20261007) names no hook install step; the dell1 handoff reports the owned-paths hook alone"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "install-all-git-hooks.sh header (LD-0343): RUN THIS ON EVERY FRESH CLONE; a clone starts with zero hooks and the ungated site is the one that succeeds.",
  "world_is": "dell1's seats (1.0.0_SA_CTO~DELL1, 2.0.0_SA_COO~M1, 2.0.0_SA_COO~H1) committed between ~07:15Z and the install with only the owned-paths gate, so their local commits before it (incl. 78756a9b74, ea7b1706a9, a35cc608fe) were not graded by the law lock, to-pipeline gate or surprise-row gate; the trunk merge at site Z grades them on the merged index. dell2 is unmeasured from here. The kit has no hook step, so every future box repeats it. The prd-header-notify orphan is repo-wide, not dell1's."
}
```

## NFRA_CTLPLN-S9 -- disarm of NFRA_CTLPLN-W1-S1: the round-3 Dell policy is applied at the laptop; the named-role PassRole rule is live

```json
{
  "id": "NFRA_CTLPLN-S9",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T08:32Z",
  "one_line": "Issuer disarm of NFRA_CTLPLN-W1-S1: the round-3 Dell policy is APPLIED at the laptop (2 added, 1 changed, 0 destroyed) and the PassRole rule Andrew confirmed is live -- a Dell passes only roles the laptop names, and none is named yet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "0.7.0_AE_CloudOps~E msg 106072 and the CLOSED ledger entry org/critical_paths/change_management/20261007T0811Z_nfra-ctlpln-dell-policy-r3-laptop-20261007_deploy_completion.md (5 of 5 legs; open f381720cde, close 95b6e421cd)",
      "Issuer's own re-plan of the identity root after the apply, 2026-10-07 ~08:3xZ: terraform plan -detailed-exitcode exit 0 (no changes)",
      "Issuer's own comparison of the seat's saved LIVE documents to the repo files: deploy policy v2 equal, create policy v1 equal; the live deploy document carries DenyPassRoleExceptNamed on Resource * beside the four round-2 Deny statements",
      "Both never-widen halves: COO d3ffdf3, CTO 2d27f79524; Andrew's card-1 answer 'Yes' (PRD v0.10)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "W1-S1 (round 2): iam:PassRole is denied outright, so a Dell deploy that registers a task definition or a target naming a role fails; rule a narrow allow. PRD v0.8 and v0.10: a Dell may pass only the named roles the laptop made for Dell-placed work, with the iam:PassedToService condition.",
  "world_is": "DISARM (issuer): the ruled form is live. Passing a role is refused for every role today because no role request has been applied; the first applied request renders that role into the policy (tests/render_passrole.py) and the next laptop apply admits it. So a Dell deploy that needs a role still fails closed and loud, now with a written route (C-ROLE-REQUEST) instead of no route. NOT yet exercised: the live round trip (a Dell writes in, the laptop applies, the Dell creates with the role); it waits on a Dell publishing its branch (CTO msg 106056)."
}
```

## NFRA_CTLPLN-S10 -- CT3c6-AC2 passed untracked and fails committed: the fabric-reader census does not classify its own files

```json
{
  "id": "NFRA_CTLPLN-S10",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T08:32Z",
  "one_line": "A round-3 criterion passed in the worker's tree and fails on the trunk: CT3c6-AC2's census of fabric readers reads unclassified=5 ok=False once its own two files are committed, and the issuer did not re-run it after the merge.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Worker proof at 13ec2d1be4: FABRIC-CENSUS files_scanned=1692 hits=53 ... unclassified=0 ok=True",
      "Issuer's run on the trunk, 2026-10-07 ~08:1xZ: FABRIC-CENSUS files_scanned=1700 hits=58 enum_source=5 compares=1 display=33 fixture=14 unclassified=5 ok=False; the five hits are three lines of .tools/tests/fabric_value_census.py and two of .tools/tests/test_fabric_enum_dell.py",
      "The census scans tracked files (git ls-files); both files were untracked when the worker ran it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-c-6 CT3c6-AC2: every reader of a fabric value in the scanned tree is found and classified (unclassified=0 ok=True); its proof instance is VALID at HEAD.",
  "world_is": "The instance is VALID and the criterion's output was true where it was run; on the trunk the same invocation fails. Cause: a check whose population (tracked files) changes when the check itself is committed. The issuer's drain re-ran CT3c6-AC1 and not AC2. Repair: cell CT-d-6 of round 4 (handed, worker ~9) repairs the census table and keeps a hit in a new test file UNCLASSIFIED until named. The general case for the drain: re-run every criterion whose invocation reads tracked files AFTER the merge, not before it."
}
```

## NFRA_CTLPLN-W11-S1 -- CT-d-8 probe finding

```json
{
  "id": "NFRA_CTLPLN-W11-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~11",
  "surfaced_at": "2026-10-07T08:32:10Z",
  "one_line": "No resources.json row names a builder-conformant resource: all 465 rows grade OUT-OF-PATTERN, so CT-d-8's case (A), 'a builder-conformant name that HAS a row', cannot be built, and the probe's registered_wellnamed key measures a registered legacy name instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/tests/probe_missing_registry_row.py, 2026-10-07 ~08:3xZ: 'registry census: resources.json holds 465 row(s); 0 of 465 row name(s) grade CONFORMANT under lib/opal_naming.grade()'",
      "case A re-uses the first LAMBDA row, inf-gold-trigger (registry_count=1): the gate prints 'NAMING REFUSE ... inf-gold-trigger -> advi-inf-gold-trigger-lambda' and exits 1 (OUT-OF-PATTERN as LAMBDA), so a registered name is refused on its grade, not admitted",
      "infra/logic/registry/resources.json _about and lib/opal_naming.py:605-610 @208c5d85ee: a row fills a {system} placeholder for a name whose own tokens resolve no system; the row never makes the name conformant"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-8 build item 1 (A): 'a builder-conformant name that HAS a row in infra/logic/registry/resources.json (pick an existing row and re-use its name)', and the last-line key registered_wellnamed.",
  "world_is": "resources.json holds the system attribution of 465 legacy, non-conformant names; none of them is a registered well-named resource, and the gate refuses the one the probe tried. The probe ran case A as the order's recipe says (an existing row's name) and prints the census beside it; the key registered_wellnamed=refused therefore reads 'a registered legacy name is refused', which is a stronger statement than the key suggests. ok=True and AC1 are unaffected (they rest on case C). No test was weakened."
}
```

## NFRA_CTLPLN-W11-S2 -- CT-d-8 probe finding

```json
{
  "id": "NFRA_CTLPLN-W11-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~11",
  "surfaced_at": "2026-10-07T08:32:40Z",
  "one_line": "C-NAMING clause (3), 'its row lands in resources.json in the same commit as its Terraform', collides with lib/opal_naming.py validate(): a row for a builder-conformant name is REFUSED as redundant, so a missing-row refusal for a conformant name would demand a row the registry validator rejects.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "scratch copy of infra/logic/registry in .scratch/regcopy with one row appended {name: blackdiamond-49f-missing-row-probe-lambda, type: LAMBDA, system: blackdiamond}: lib/opal_naming.validate(reg_dir=...) returns 1 refusal: \"already resolves 'blackdiamond' from its own tokens (type 'LAMBDA'); a row naming the same system is redundant\" (baseline validate on the unmodified registry: 0 refusals)",
      "lib/opal_naming.py:642-664 @208c5d85ee, the redundant-row check; infra/logic/registry/resources.json _about (rows exist only for names whose tokens resolve no system)",
      "the same probe: the unregistered, builder-conformant name is ADMITTED by the apply gate (NAMING-PLAN: PASS 1 graded), so today nothing requires the row that clause (3) says must exist"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "NFRA_CTLPLN PRD v0.13 C-NAMING clause (3) and cell (b): every new resource has a row in infra/logic/registry/resources.json, and an apply for a missing row is refused.",
  "world_is": "For a conformant name the row resources.json can hold is a redundant one that validate() refuses, so 'the missing row' is undefined for exactly the resources C-NAMING is about; the proposal for CT-d-8 states this and offers the index question to the gate's owner rather than choosing. Whether a commit-time or CI gate runs validate() on a pushed registry was not measured by this worker; only the function's return was."
}
```

## NFRA_CTLPLN-W7-S1 -- deploy_ledger.py has no verb that adds a field or note to an open entry; the named-commit line is carried by named_commit_check.py writing the sentinel log and the entry's Log section directly

```json
{
  "id": "NFRA_CTLPLN-W7-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~7",
  "surfaced_at": "2026-10-07T08:34:25Z",
  "one_line": "deploy_ledger.py has no verb that adds a field or note to an open entry; the named-commit line is carried by named_commit_check.py writing the sentinel log and the entry's Log section directly",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/deploy_ledger.py@208c5d85ee:_render_entry prints state['log']; no note verb in the argparse table (cmd_open, cmd_close_leg, cmd_close, cmd_hold, cmd_check, cmd_list)",
      "worktree test: python .tools/tests/test_named_commit_deploy.py case 8 -> carried=True survives_rerender=True for both wrappers"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-3 build item 2: the wrappers pass or append named_commit=<hash> trunk=OFF-TRUNK branch=<b> device=<d> to the entry the actor opened, reading deploy_ledger.py for how a field or note is added; if the ledger tool cannot carry the field without an edit, that is a surprise row and the wrapper prints the line instead.",
  "world_is": "deploy_ledger.py@208c5d85ee has open, close-leg, close, hold, check, list and no note or field verb. The entry is a re-rendering of the sentinel (_render_entry prints the sentinel's `log` array under `## Log`), so a line added to the sentinel's `log` survives every later close-leg re-render. named_commit_check.py --record therefore appends one line to the sentinel JSON `log` (plus a `named_commit` key) and the same line to the entry's Log section, without editing deploy_ledger.py. Proven by test case 8 including a close-leg re-render. This is a second writer of the sentinel format; a future change to the sentinel schema must read named_commit_check.py _record."
}
```

## NFRA_CTLPLN-W7-S2 -- The named-commit check runs only when DEPLOY_COMMIT is set; with it unset the wrappers do not read HEAD's relation to the trunk at all

```json
{
  "id": "NFRA_CTLPLN-W7-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~7",
  "surfaced_at": "2026-10-07T08:34:25Z",
  "one_line": "The named-commit check runs only when DEPLOY_COMMIT is set; with it unset the wrappers do not read HEAD's relation to the trunk at all",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-d-3.named-commit-deploy.md:build item 2 and BOUNDS@208c5d85ee",
      "git diff of .tools/safe-deploy.sh and .tools/safe-apply.sh: the block is guarded by [ -n \"${DEPLOY_COMMIT:-}\" ]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-3 build item 2: DEPLOY_COMMIT=<full hash>; when unset the wrapper uses git rev-parse HEAD and behaves as today; bounds: every existing path works unchanged when DEPLOY_COMMIT is unset.",
  "world_is": "Read as: unset means no check and no change, because grading HEAD for a Dell on every unset deploy would newly refuse an unpublished HEAD (and a Dell with AGENTBUS_DEVICE unset) on paths that never refused before. So a Dell that deploys without naming its commit is not graded by this check, and the pre-push hook path (which does not set DEPLOY_COMMIT) is unchanged. Also: when DEPLOY_COMMIT IS set the device must resolve in the register, so an ON-TRUNK deploy from a box with AGENTBUS_DEVICE unset is refused (case 6 as written). If the issuer meant unset to grade HEAD, that is one line in each wrapper."
}
```

## NFRA_CTLPLN-W6-S1 -- The census calls AWS through .tools/aws.cmd, the Windows twin of the .tools/aws shim, beca

```json
{
  "id": "NFRA_CTLPLN-W6-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T08:39:30Z",
  "one_line": "The census calls AWS through .tools/aws.cmd, the Windows twin of the .tools/aws shim, because a native Python subprocess cannot execute the extensionless bash shim.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python subprocess.run(['.tools/aws', ...]) from the worktree: FileNotFoundError [WinError 2] (the shim is a bash script); .tools/aws.cmd resolves the same real AWS CLI with the same default credential chain (sts get-caller-identity: user/Andrew_Berman)",
      "infra/aws/terraform/shared-infra/tests/dell_fence_census.py, AWS constant: aws.cmd on Windows, the bash shim elsewhere",
      "iam simulate-principal-policy takes the bucket policy as --resource-policy file://<path relative to the worktree root>; 48 evaluator calls all returned a decision, none errored"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-1 step 1: s3api list-buckets through the repo's .tools/aws shim.",
  "world_is": "The shim is a bash script a native Python process cannot exec; the script uses its Windows twin aws.cmd (same CLI, same credentials), and passes the large resource-policy document by file. No boto3 was used."
}
```

## NFRA_CTLPLN-W6-S2 -- The order's undeclared=<x> is ambiguous between 'a fence' and 'any live bucket policy'; th

```json
{
  "id": "NFRA_CTLPLN-W6-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T08:39:40Z",
  "one_line": "The order's undeclared=<x> is ambiguous between 'a fence' and 'any live bucket policy'; the census counts every live policy with no declaring .tf found: 2, and none of the 3 fences is among them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "FENCE-CENSUS line: fenced=3 undeclared=2; the 2 undeclared are NO-FENCE policies on legacy firm buckets (CloudFront read grants), which only a data aws_s3_bucket_policy source reads under infra/aws/terraform/portal-auth/firm-bucket-cross-ref.tf:29-39 (no resource declares them)",
      "the 3 fences are declared at shared-infra/s3-49financial.tf:122 and shared-infra/s3-lgic-firm-buckets.tf:142 (for_each over the scopes.json registry, so no firm token appears in that file)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-1 step 4 and the last-line field undeclared: the .tf file and line that declares each bucket's policy, or UNDECLARED; the report lists every UNDECLARED fence.",
  "world_is": "Counted as: a bucket with a live policy whose declaring aws_s3_bucket_policy resource is not found by the resolver (literal bucket, a local holding the literal, a for_each over the registry, or the two registry idioms). NO-POLICY buckets read 'n/a'. UNDECLARED fences = 0; each bucket's declaring file and line are in the saved JSON under its declared field."
}
```
