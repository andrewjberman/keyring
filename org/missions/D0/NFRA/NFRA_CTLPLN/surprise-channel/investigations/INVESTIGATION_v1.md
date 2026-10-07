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

## NFRA_CTLPLN-W10-S1 -- CT-d-7: lib/opal_naming.py validate REFUSES every resources.json row for this project's nine named resources, so step 3 (add the missing rows) cannot land

```json
{
  "id": "NFRA_CTLPLN-W10-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~10",
  "surfaced_at": "2026-10-07T08:37:30Z",
  "one_line": "TO-CT-d-7 step 3 asks for resources.json rows for the nine named resources of nfra-ctlpln-identity and nfra-ctlpln-agentbus, but the registry's own validator refuses each such row as redundant, because every one of the nine names already resolves its system (cloudops or agentbus) from its own tokens; no row was added.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "nine rows (system cloudops x7 for the group, two users and four policies; agentbus x2 for the two .fifo queues; systems.json carries both keys) appended to infra/logic/registry/resources.json in the worktree: `python lib/opal_naming.py validate` -> 'REFUSED resources.json[465].name: cloudops-dell-agents-group already resolves cloudops from its own tokens (type IAM_GROUP); a row naming the same system is redundant' and the same line for [466]..[473]; 'VALIDATE: REFUSED 9 refusal(s)'. Before the rows: 'VALIDATE: OK ... 465 rows'. The file was restored to its committed bytes (git diff empty).",
      "lib/opal_naming.py lines 605-612 and 654-669 (validate): a resources.json row fills a {system} placeholder ONLY where a name's own tokens resolve none; a row naming the SAME system as the tokens is refused",
      "lib/opal_naming.py grade() on each of the nine names returns CONFORMANT (the IAM user is NOT-GRADED by type) with no row; the opal_name module's name() gives agentbus-global-dell1-queue.fifo, equal to the module-formatted string"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-7 step 3 and PRD v0.13 C-NAMING clause (3): a new resource's row lands in infra/logic/registry/resources.json in the same commit as its Terraform; the read lists a name as MISSING when no row carries it.",
  "world_is": "(no AWS call was made; Terraform was read from commits only.) resources.json is the registry's carrier for names whose own tokens cannot resolve a system (NAMING_SCHEMA grade.placeholder), not a list of every resource. The nine names of the two roots are builder-conformant, so a row for any of them cannot be admitted (validate refuses it; the commit's naming limb and the registry readers sit on that validate). The read therefore prints MISSING for nine conformant names and its ok=False cannot be cleared by a row. No row was added; no vocabulary row was missing (cloudops and agentbus are systems.json keys). What 'everything should be registered' means for a conformant name is the registry owner's call: a different carrier or flag, a validator exemption for rows that restate a conformant name, or a read that grades a name CONFORMANT-BY-TOKENS instead of MISSING. CT4d7-AC2 expects only unresolved=0, which holds (0 of 9); the last line records missing=9."
}
```

## NFRA_CTLPLN-W10-S2 -- CT-d-7: the identity root names its resources with string literals, not through the opal_name module

```json
{
  "id": "NFRA_CTLPLN-W10-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~10",
  "surfaced_at": "2026-10-07T08:37:45Z",
  "one_line": "The order says the identity root names its resources through the opal_name module; at 208c5d85ee infra/aws/terraform/nfra-ctlpln-identity/iam.tf names all seven named resources with string literals and only the agentbus root calls modules/opal_name.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/nfra-ctlpln-identity/iam.tf @208c5d85ee: name = \"cloudops-dell-agents-group\" (line 16), \"cloudops-dell1-agent-user\" (20), \"cloudops-dell2-agent-user\" (25), \"cloudops-dell-agent-deploy-policy\" (36), \"cloudops-dell-agent-create-policy\" (51), \"cloudops-dell1-agent-bus-policy\" (65), \"cloudops-dell2-agent-bus-policy\" (72); the file has no module block; main.tf's header says tests/check_identity.py compares each name to the builder",
      "infra/aws/terraform/nfra-ctlpln-agentbus/sqs.tf:19-27 @208c5d85ee: module \"queue_name\" for_each over local.inbound_boxes, source ../modules/opal_name, resolved to agentbus-global-dell1-queue.fifo and agentbus-global-dell2-queue.fifo and equal to lib/opal_naming.py name()"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-7 build 1: the identity root names its resources through the opal_name module.",
  "world_is": "The read resolves the identity names as literals (7 of 7) and the agentbus names through the module with a builder cross-check (2 of 2, name() equal); for the seven literals the builder cross-check is the root's own tests/check_identity.py, not re-run here. No criterion depends on the difference."
}
```

## NFRA_CTLPLN-S11 -- a Dell's Git for Windows sets core.autocrlf=true system-wide; every Dell commit rewrites the CRLF files it touches

```json
{
  "id": "NFRA_CTLPLN-S11",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.0.0_AB_MSTR~DELL1",
  "surfaced_at": "2026-10-07T08:25Z",
  "one_line": "dell1 and dell2 run with core.autocrlf=true from C:/Program Files/Git/etc/gitconfig and no repo-local override; the laptop's effective value is false. A Dell's checkout writes CRLF working copies and its commits normalise CRLF and mixed files to LF, so a Dell's branch rewrites line endings the trunk keeps.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell1 2026-10-07 ~08:05Z: git config --show-origin --get-all core.autocrlf -> file:C:/Program Files/Git/etc/gitconfig true; no repo-local value",
      "dell1 git ls-files --eol: 60165 tracked; 2238 i/crlf, 466 i/mixed, 53429 i/lf",
      "dell2 (0.0.0_AB_MSTR~DELL2, bus 13e46198): same system value, no override; 41,747 i/lf w/crlf working copies",
      "q/dell1/CLOUD/r2 a9672da2a7 refused at the laptop merge: 206 CRLF endings in this file rewritten as LF (laptop 0.0.0_AB_MSTR, bus 81673b47)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The bring-up kit (Opal_New_Device_Kit_20261007 README_NEW_DEVICE.md) sets no git config; the git-pull skill's prerequisites name core.autocrlf=false for this repo.",
  "world_is": "Neither Dell carries the repo's expected value. A bare flip to false is not a fix on a live box: the existing CRLF working copies of LF files would then commit as whole-file CRLF rewrites. The fix is the flip plus a full re-checkout of the shared tree and every worktree, with the box's seats quiet; that act is held for Andrew on both Dells. Interim on dell1: the fabric manager merges and commits shared CRLF files only from a fresh worktree checked out with core.autocrlf=false, resolving them from origin's bytes. The kit needs a git-config step (core.autocrlf=false, core.longpaths=true) before the first checkout."
}
```

## NFRA_CTLPLN-W8-S1 -- TO-CT-d-5 four denied arms change required decision

```json
{
  "id": "NFRA_CTLPLN-W8-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~8",
  "surfaced_at": "2026-10-07T08:38:30Z",
  "one_line": "TO-CT-d-5 says the four existing denied arms 'keep passing', but they require implicitDeny and the new explicit Deny turns each into explicitDeny, so as written they fail 4 of 19.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py DENIED list at 208c5d85ee: s3:PutBucketPolicy, lambda:AddPermission, kms:PutKeyPolicy, secretsmanager:PutResourcePolicy each carry required decision implicitDeny",
      "after DenyResourcePolicyWrites, SimulateCustomPolicy returns explicitDeny for all four (RESPOL arms in the same run); the arms were changed to required explicitDeny in the worker branch, an edit inside the order's paths, so denied_ok=19/19 holds with the same four actions still denied"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-5 build step 3: 'the existing denied arms for s3:PutBucketPolicy, lambda:AddPermission, kms:PutKeyPolicy and secretsmanager:PutResourcePolicy keep passing' with denied_ok=19/19 unchanged.",
  "world_is": "Those arms pass only if their required decision is changed from implicitDeny to explicitDeny, because the whole point of the cell is that the refusal is now explicit. The expected value 19/19 is met; the four required values moved, the actions did not. The issuer may want the order text to say so."
}
```

## NFRA_CTLPLN-W8-S2 -- TO-CT-d-5 apigateway UNSURE, no policy-write Deny

```json
{
  "id": "NFRA_CTLPLN-W8-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~8",
  "surfaced_at": "2026-10-07T08:38:40Z",
  "one_line": "apigateway is the one UNSURE service of CT-d-5: a REST API resource policy is written through apigateway:PATCH/PUT/POST, which the create policy allows, and no deny names it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO: read the UNSURE list printed by tests/derive_respol_actions.py and rule on apigateway (a Deny on a documented dedicated action, a resource-path Deny, or accept the residual like the six ruled calls)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/nfra-ctlpln-identity/dell_create_policy.json at 208c5d85ee: CreateUpdateTagEdgeAndDns allows apigateway:POST, apigateway:PUT, apigateway:PATCH",
      "installed botocore 1.43.0 apigateway and apigatewayv2 models list no IAM-only action name; SimulateCustomPolicy returned explicitDeny for apigateway:BogusZzz against a Deny naming it, so the simulator cannot confirm a name either; nothing was guessed into the Deny",
      "tests/derive_respol_actions.py line 'UNSURE apigateway', counted unsure=1 in the RESPOL-DERIVED line"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-5: the Deny lists the resource-policy actions of every Dell-allowed service, derived; a service that cannot be settled is UNSURE, counted and listed for a senior read.",
  "world_is": "apigateway cannot be settled from derived sources, so no apigateway action is in the Deny and a Dell holding the allowed PATCH/PUT/POST can still set a REST API resource policy. The same mixed-call shape is printed (not counted) for ec2 CreateVpcEndpoint/ModifyVpcEndpoint and kms ReplicateKey, which are not allowed to a Dell today."
}
```

## NFRA_CTLPLN-W7-S3 -- TO-CT-d-4 last-line extension and enum edge

```json
{
  "id": "NFRA_CTLPLN-W7-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~7",
  "surfaced_at": "2026-10-07T09:19:58Z",
  "one_line": "TO-CT-d-4's LAST-line format has no field that names the failed field and its ledger enum has no value for 'closed, names no commit'; the script appends failed=<fields> after ok= and files that case as other-commit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/deploy_readback_check.py last line: DEPLOY-READBACK ... ledger=<v> ok=<b> failed=<comma list|none>; org/devices/test_deploy_readback.py asserts the exact line for all six arms and prints cases=6/6",
      "the order's ledger enum is closed-named|open|missing|other-commit; a closed entry carrying no named_commit line (a deploy made on-trunk, or never recorded) fits none, so it reports other-commit and the step-4 line prints the named_commit values found (or none)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-4 build 1: the LAST line is `DEPLOY-READBACK commit= device= admitted= on_trunk= objects_equal= ledger= ok=`; the worker brief adds that the last line must say which field failed. Ledger values: closed-named|open|missing|other-commit.",
  "world_is": "Two things the order did not say: (1) a trailing failed= field was added after ok= so a consumer matching the order's prefix still matches; (2) other-commit also stands for a closed entry that names no commit, and on_trunk may print Unknown when the fetch or ancestry read fails, and admitted=False skips steps 2-4 (printed as SKIPPED) so on_trunk=Unknown, objects_equal=0/n, ledger=missing then mean not-read."
}
```

## NFRA_CTLPLN-W12-S1 -- CT-k-1: three Lambda-vendored copies of the trading calendar already differ from lib/ and keep the old silent fallback

```json
{
  "id": "NFRA_CTLPLN-W12-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~12",
  "surfaced_at": "2026-10-07T09:23:05Z",
  "one_line": "The three Lambda-vendored byte-copies of lib/trading_calendar.py (inf-etf-ownership-daily, bd-served-vintage-alarm, opal-assets-absence-check) are already not copies of lib/ and keep the old silent 2024-2027 fallback, so TO-CT-k-1's fail-closed fix does not reach those three functions until someone re-vendors them.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "diff of `git show a68599cde3:lib/trading_calendar.py` against each of infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/trading_calendar.py, infra/aws/lambda/bd-pipeline/bd-served-vintage-alarm/trading_calendar.py, infra/aws/lambda/opal-assets-absence-check/trading_calendar.py: all three DIFFER (each is 163 lines; the first hunk is the missing weekly_production_day, lines 122-154), so they were not byte-copies before this order either",
      ".github/workflows/lib-vendored-copies-parity.yml PAIRS lists those three plus infra/aws/lambda/schwab-bronze-freshness/trading_calendar.py; `ls infra/aws/lambda/schwab-bronze-freshness` -> No such file or directory, so that parity job reports MISSING_VENDORED and DRIFT today",
      "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~12/TRADING_CALENDAR_IMPORTERS.md section 1 and 3: all three vendored lambdas run without pandas_market_calendars (stdlib-only packages), so they answer from the old 2024-2027 set, silently outside it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-k-1 cell text: lib/trading_calendar.py is the estate's ONE trading-day definition and Lambdas vendor this ONE file; the fail-closed raise changes what deployed importers do the next time they are rebuilt.",
  "world_is": "Three deployed Lambdas carry their own older 163-line copy of the module, outside the order's grant (it edits no importer and deploys nothing). The new fallback and CalendarCoverageError reach them only if the copies are replaced from lib/. Until then they answer a pre-2024 holiday as a trading day, and from 2028-01-01 every weekday, with no error; their current call sites pass current dates (bd-served-vintage-alarm, opal-assets-absence-check) or an event day (inf-etf-ownership-daily, UNKNOWN). Disarm owner is the issuer who decides whether a re-vendor cell is cut; this worker did not copy the file."
}
```

## NFRA_CTLPLN-W13-S1 -- CT-k-2: pip's local cache on the laptop is empty, so the pack's preference (a) is built but never exercised against a real cached wheel

```json
{
  "id": "NFRA_CTLPLN-W13-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T09:21:46Z",
  "one_line": "The order's pack prefers a wheel already in pip's local cache or wheelhouse; on the laptop that cache holds 0 bytes and 0 wheels, so every packed artifact is rebuilt from installed files (preference b) and the cached-wheel arm has no real wheel to find.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pip cache info, run in worktree C:/tmp/wk-ctlpln-13 on 2026-10-07: wheels location under LOCALAPPDATA/pip/cache/wheels, size 0 bytes, 0 locally built wheels; http-v2 size 0 bytes",
      "org/devices/kit_python_pack.py (branch wk-NFRA_CTLPLN-13): the pack run against a target with nothing installed wrote 69 wheels, every 'how' = rebuilt-from-installed-files; pip install --no-index --dry-run of all 69 rc=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-k-2 build 2: for each missing distribution, (a) a wheel already in pip's local cache or wheelhouse that matches the target is preferred, then (b) a wheel rebuilt from the installed files.",
  "world_is": "python -m pip cache info on the laptop (pip 26.0.1): 'Package index page cache size: 0 bytes', 'Number of HTTP files: 0', 'Number of locally built wheels: 0'; no wheelhouse directory is named. All 69 artifacts of a full-closure pack for a target with nothing installed were 'rebuilt-from-installed-files'; the cache arm (fits_target and find_cached_wheel in org/devices/kit_python_pack.py) is code, not exercised against a real wheel. The pip --dry-run self-check validated every rebuilt wheel instead."
}
```

## NFRA_CTLPLN-W13-S2 -- CT-k-2: blpapi, an import in .tools/ or lib/, is not installed on the laptop; it is the only NOT-INSTALLED-HERE module

```json
{
  "id": "NFRA_CTLPLN-W13-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T09:21:46Z",
  "one_line": "The census finds 1 third-party module the laptop itself lacks (blpapi, OPTIONAL, 1 importing file), so compare reads missing=1 on the laptop and on any box, and the pack lists it UNPACKABLE.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/kit_python_required.json not_installed_modules = [{module: blpapi, usage: OPTIONAL, importers: 1}], from python org/devices/kit_python_census.py required on branch wk-NFRA_CTLPLN-13 (base a68599cde3)",
      "KIT-COMPARE device=laptop python=3.12.10 required=21 present=20 missing=1 version_differs=0 hard_missing=0 ok=False (this worker's compare of the laptop's own installed read)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-k-2 bounds: if required reports a third-party module NOT-INSTALLED-HERE, that is a finding for the report (the laptop itself lacks something its tools import), not something to install; compare ok=True only when m == 0.",
  "world_is": "KIT-REQUIRED files=745 unparsed=0 modules=135 stdlib=67 local=47 third_party=21 distributions=20 not_installed_here=1: the one is blpapi (the Bloomberg API Python binding), imported in a try, 1 file. KIT-COMPARE on the laptop reads required=21 present=20 missing=1 ok=False, so the order's compare line cannot read ok=True on any box until blpapi is installed there or dropped from the list. The pack and install tools treat an OPTIONAL module with no distribution as UNPACKABLE and counted but not failing their own ok; compare keeps the order's rule (ok only when missing=0). Nothing was installed."
}
```

## NFRA_CTLPLN-W13-S3 -- CT-k-2: 26 of the 47 modules classified LOCAL resolve to a repo name outside the path roots the order names

```json
{
  "id": "NFRA_CTLPLN-W13-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T09:21:46Z",
  "one_line": "Read literally, the order's LOCAL rule (inside .tools/, lib/, or beside the importing file) leaves 26 more repo-internal module names classed as third-party; the census classifies them LOCAL by a repo-wide name match and records local_via per module.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/devices/kit_python_census.py required, first run (path roots only): local=21 third_party=47 not_installed_here=27; second run (repo-wide names added): local=47 third_party=21 not_installed_here=1, on branch wk-NFRA_CTLPLN-13",
      "org/devices/kit_python_required.json is a third_party-only list; the 26 repo-wide-name modules were printed from census_required() with local_via=repo-wide-name and shadows_installed_distribution=false"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-k-2 build 1: classify an import LOCAL only when it resolves to a module or package inside the repository (.tools/, lib/, or a package beside the importing file); everything else THIRD-PARTY.",
  "world_is": "With only the order's roots the census read local=21 third_party=47 not_installed_here=27 (price_axis_pull, kuzu_cli, orchestrator, serp and 23 others, each the stem of a tracked .py elsewhere in the repo, reached by a sys.path insert the static read cannot follow). The census now classes a name LOCAL when no installed distribution provides it and a tracked .py stem or directory of that name exists anywhere in the repo (local_via=repo-wide-name, 26 modules), leaving third_party=21 and not_installed_here=1. No LOCAL name shadows an installed distribution (shadows_installed_distribution=false for all 47)."
}
```

## NFRA_CTLPLN-W6-S3 -- The fence admission lists are registry-generated; the join is a typed third term in each concat(), not an exemptions.json row

```json
{
  "id": "NFRA_CTLPLN-W6-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T09:08:35Z",
  "one_line": "The fences' admitted lists are generated from two registry files (scopes.json patterns, exemptions.json named exemptions) that the order's grant excludes; the join was made as one added typed term in each fence's own concat(), the construct s3-49financial.tf already uses for its adapter role, not as an exemptions.json row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/shared-infra/s3-49financial.tf:139-143 and s3-lgic-firm-buckets.tf:160-164 @3ec42c56bf: aws:PrincipalArn = concat(module.opal_name.fence_patterns[...], exemption arns, ...) -- the first two terms are registry-generated; s3-49financial.tf already carries a third typed term (the adapter role arn)",
      "infra/logic/registry/exemptions.json keys: every fenced bucket has a row list; no cloudops dell user is in any list (measured: 0 of 7 key lists name a dell user)",
      "s3-49financial.tf:93-96 header: the two lists are 'never typed here (DEC-4 iii)'; the typed third term is a departure from that sentence's letter, in the same concat the adapter-role precedent uses"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-2 AMENDMENT 1: if the admitted list is read from a registry file rather than typed in the .tf, STOP and file a BLOCKING row; otherwise add the user to the construct the fence already uses.",
  "world_is": "The concat is typed in the .tf (in grant) and its registry terms are untouched; a third typed term adds the one user without a registry write, so the stop clause was read as not triggered. The senior seat that signs may prefer the registry route (a named exemption row with its change-management sign-off); that is a later swap of the same single-user admission. The shared for_each term applies to every bucket that resource produces: today exactly 2 (both in the pairs), and a future FIRM row the registry hands to that file would gain the user too."
}
```

## NFRA_CTLPLN-W10-S3 -- CT-d-7 amendment 1: the registry has no public single-name system resolver; the read calls validate()'s own two private steps

```json
{
  "id": "NFRA_CTLPLN-W10-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~10",
  "surfaced_at": "2026-10-07T09:27:40Z",
  "one_line": "Amendment 1 says to decide SELF-RESOLVING / REGISTERED / ROW-NEEDED by calling the registry's own reader, but lib/opal_naming.py exposes no public function that returns the system a name's own tokens resolve; grade() returns NOT-GRADED for IAM_USER, so the read calls _res_tokens and _slots, the two steps validate() itself runs on a resources.json row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming.py:642-664 (validate, resources.json limb): `rtoks = _res_tokens(body, v_res, ...)` then `_rsysv, _rout, _rscope, rph = _slots(None, rtoks, typ, v_res)`; a row is refused when `not rph and _rsysv == system`; for an SQS_QUEUE the .fifo suffix is removed from the body first (line 655-656)",
      "lib/opal_naming.py grade('cloudops-dell1-agent-user', 'IAM_USER') -> ('NOT-GRADED', None); grade() on the other eight names -> CONFORMANT; so grade() cannot answer the question for the two Dell users",
      "org/devices/round_created_resources.py registry_class() makes exactly those calls (private names, same module, same repo); for the ten named resources of the two roots it returns SELF-RESOLVING 10 of 10, and the validator's count line is `VALIDATE: OK 53 system row(s), 13 scope row(s), 41 warning(s) at registry@d669df6cb07575c8 over all 8 registry file(s)` (rc=0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-7 amendment 1 item 1: decide by calling the registry's own reader in lib/opal_naming.py (read how validate and name resolve a system; call that, do not re-implement it).",
  "world_is": "There is no public single-name resolver. The read depends on two underscore-private functions and on the .fifo-removal line copied from validate(); a change to either in lib/opal_naming.py changes this read with no error. The .fifo removal is the only step re-stated here (one line); everything else is a call. Whether to export a public resolver is the registry owner's call; nothing in this order's paths edits lib/opal_naming.py."
}
```

## NFRA_CTLPLN-W10-S4 -- CT-d-7 amendment 1: eight of ten named resources read NO-NODE although the graph was built AFTER their introducing commits

```json
{
  "id": "NFRA_CTLPLN-W10-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~10",
  "surfaced_at": "2026-10-07T09:27:50Z",
  "one_line": "Over rounds 2 and 3 the cloud-graph arm finds 0 nodes for 10 named resources: 2 are labelled NO-NODE-GRAPH-OLDER (policies introduced 06:48Z and 08:40Z, after the graph's 06:16:58Z build) and 8 are plain NO-NODE (introduced 03:29Z-03:49Z, before the graph's build); a commit time says when a resource was declared, not when it was applied, so the read cannot tell 'not applied' from 'applied and not modelled'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ROUND_2_3_CREATED_RESOURCES.txt last line: created=16 nameless=6 named=10 self_resolving=10 registered=0 row_needed=0 unresolved=0 graph_unread=0 graph_nodes=0 no_node=8 no_node_graph_older=2 graph_built=2026-10-07T06:16:58Z ok=True",
      "comp-find --corpus aws on each name: DEFERRED 0 of 1, `0 hit(s) across 2833 aws node(s) scanned`, VINTAGE `Built from the estate as of 2026-10-07 06:16:58 UTC`; positive control through the same parser: gateway-access-state-table -> 1 node (DYNAMODB_TABLE, drift DECLARED) and `opal-gateway` -> 71 hits, 71 parsed (2 name matches, 69 properties-only)",
      "introducing commits (committer time, UTC): a0ad635429 03:29:39Z (group, 2 users, deploy and 2 bus policies), 768fca164e 03:49:44Z (2 queues), d452dcffe5 06:48:20Z (create policy), ce05f0e838 08:40:50Z (respol policy)",
      "the drain commit for TO-CT-d-5 says its resource-policy Deny is NOT APPLIED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-7 amendment 1 item 2: a miss explained by the graph being older than the resource is labelled NO-NODE-GRAPH-OLDER by comparing the graph's built time with the introducing commit's time; every other miss is NO-NODE.",
  "world_is": "The comparison is by commit time as ordered, so 8 misses read plain NO-NODE. Whether those eight are unapplied (declared in Terraform, never created in the account) or applied-and-absent-from-the-graph is not decided by this read, which makes no AWS call and has no apply time; the order's NO-NODE finding is carried as measured and no interpretation is added. Reading each root's Terraform state or apply ledger would decide it and is outside this order."
}
```

## NFRA_CTLPLN-W10-S5 -- CT-d-7 amendment 1: the last-line field order and the CT4d7-AC2 expectation cannot both hold

```json
{
  "id": "NFRA_CTLPLN-W10-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~10",
  "surfaced_at": "2026-10-07T09:32:00Z",
  "one_line": "Amendment 1 fixes the last-line field order with graph_nodes, no_node and no_node_graph_older between unresolved and graph_unread, but CT4d7-AC2 expects the contiguous string 'unresolved=0 graph_unread=0', which the checker matches as a substring; the read prints graph_unread directly after unresolved.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/proof-of-spec-check.py on the instance with the amendment's field order: `VIOLATION: acceptance[CT4d7-AC2]: status=PASS but output_evidence does NOT match expect 'unresolved=0 graph_unread=0'`, INVALID rc=1; the last line then read `... unresolved=0 graph_nodes=0 no_node=8 no_node_graph_older=2 graph_unread=0 ...`",
      "after moving graph_unread beside unresolved the line reads `... row_needed=0 unresolved=0 graph_unread=0 graph_nodes=0 no_node=8 no_node_graph_older=2 graph_built=2026-10-07T06:16:58Z ok=True`; every field the amendment names is present with the same name and meaning"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-7 amendment 1 item 3 (last-line field order: ... unresolved=<u> graph_nodes=<k> no_node=<z> no_node_graph_older=<o> graph_unread=<w> ...) and its acceptance (CT4d7-AC2 expects `unresolved=0 graph_unread=0`).",
  "world_is": "The two statements cannot both hold under a substring match. The order of the other fields was changed (graph_unread moved up two places and past none of the named values); the expectation and every value are unchanged. A consumer that reads the line by field name is unaffected; one that reads it by position would see the move."
}
```

## NFRA_CTLPLN-W13-S4 -- CT-k-2: The agentbus root has no .terraform.lock.hcl, so the premise that the identity and agentbus roots lock two dif

```json
{
  "id": "NFRA_CTLPLN-W13-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T09:55:00Z",
  "one_line": "The agentbus root has no .terraform.lock.hcl, so the premise that the identity and agentbus roots lock two different major versions does not hold: the tree locks exactly one provider version (hashicorp/aws 5.100.0).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/devices/kit_terraform_providers.py required: TF-REQUIRED roots=15 locked=10 no_lock=5 providers=1 distinct_versions=1 ok=True, on branch wk-NFRA_CTLPLN-13 (base df95fb06b5); infra/aws/terraform/nfra-ctlpln-agentbus holds main.tf, sqs.tf, tests/ and no lock file (git ls-files lists 39 lock files, none there)",
      "infra/aws/terraform/nfra-ctlpln-agentbus/main.tf required_providers: hashicorp/aws version ~> 6.0; the identity root's lock pins 5.100.0 under ~> 5.0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-k-2 AMENDMENT 1 item 5 (1): required lists hashicorp/aws and at least the two versions this project's two roots lock (the identity root and the agentbus root lock different major versions).",
  "world_is": "Only the identity root locks a version (5.100.0). The agentbus root declares ~> 6.0 and carries no lock, so its init resolves the newest 6.x the source offers. Test case 1 asserts what is true (identity LOCKED at 5.100.0; agentbus NO-LOCK declaring ~> 6.0) rather than two locked versions. The kit carries the agentbus need through pack --include-unlocked: the highest on-box version satisfying the declared constraint (6.67.0 in the plugin cache). Whether the Dell should lock the agentbus root at 6.67.0 is the issuer's call."
}
```

## NFRA_CTLPLN-W13-S5 -- CT-k-2: Five of the 15 derived Terraform roots (bd-49f-auto-login, estate-report, mdpf-secclass, modules, nfra-ctlpln-

```json
{
  "id": "NFRA_CTLPLN-W13-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T09:55:30Z",
  "one_line": "Five of the 15 derived Terraform roots (bd-49f-auto-login, estate-report, mdpf-secclass, modules, nfra-ctlpln-agentbus) have no lock file; a mirror built from locks alone would not serve them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/devices/kit_terraform_providers.py required prints NO-LOCK for those five roots, with declared constraints hashicorp/aws ~> 5.0 (four roots), ~> 6.0 (agentbus) and hashicorp/archive ~> 2.4 (estate-report)",
      "python org/devices/kit_terraform_providers.py located prints UNLOCKED lines: best on-box satisfying versions aws 5.100.0, aws 6.67.0, archive 2.8.1 (plugin cache holds aws 5.100.0 and 6.67.0, archive 2.8.0 and 2.8.1, local 2.9.1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-k-2 AMENDMENT 1 item 1: a root with no lock file is NO-LOCK, counted; the pack lays out the found providers the roots LOCK.",
  "world_is": "no_lock=5 of 15. The order's pack covers locked providers only (1 version); the five NO-LOCK roots need aws 5.x, aws 6.x and archive 2.x. This worker added an off-order flag, pack --include-unlocked, which adds the highest on-box version satisfying each declared constraint; without it the Dell cannot init those roots from the mirror. The flag is opt-in and the test suite does not depend on it."
}
```

## NFRA_CTLPLN-S12 -- shared-infra's .terraform pointed at a deleted Desktop tree belonging to another root

```json
{
  "id": "NFRA_CTLPLN-S12",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~E",
  "surfaced_at": "2026-10-07T10:12Z",
  "one_line": "The shared tree's shared-infra Terraform root carried a .terraform/plugin_path pointing at a DELETED directory on the Desktop belonging to a DIFFERENT root, which is why its .terraform/providers was empty and why a plan of it could not run without an init.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "Already corrected as a side effect of a required act, not left for anyone: the TO-APPLY-4 init (-plugin-dir=C:/Users/AndrewBerman/.terraform.d/plugin-cache) rewrote plugin_path to the local cache. No owner is owed an act for THIS root. Named here because the CAUSE -- a -plugin-dir init in one session persisting an absolute foreign path into a shared-tree root's untracked metadata -- is not specific to this root and has no owner.",
  "spec_asserts": "The order's context says a read-only plan from the issuer's session 'stopped at \"Backend initialization required\"' and makes the executor's first read 'whether terraform init of this root needs a provider that is not already on this box', with a provider FETCH from the registry as a STOP. That framing treats the root's local state as merely un-initialised.",
  "world_is": "It was not merely un-initialised; it was initialised AGAINST A FOREIGN TREE. infra/aws/terraform/shared-infra/.terraform/plugin_path (dated 2026-09-25) contained exactly [\"C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923/infra/aws/terraform/investor-reporting/performance/.terraform/providers\"] -- a path that (a) is outside this workspace, (b) belongs to the investor-reporting/performance root rather than shared-infra, and (c) NO LONGER EXISTS on disk. So .terraform/providers was empty and the provider had to come from somewhere. The STOP did NOT fire: the lock pins hashicorp/aws 5.100.0 and the local plugin cache holds exactly that version (terraform-provider-aws_v5.100.0_x5.exe), so init was run with registry installation DISABLED via -plugin-dir and reported 'Using hashicorp/aws v5.100.0 from the shared cache directory', rc=0, with no fetch. Separately, the 'Backend initialization required' message was a STRUCTURE mismatch, not a wrong backend: the on-disk record's bucket/key/region (opal-313476888478-terraform-state / shared-infra/tfstate / us-east-1) are identical to the declared block at main.tf:11-15, so -reconfigure re-pointed at the SAME state, and the control on that was `state list` returning 252 resources including all three fence policies. Census after the fix: 1 plugin_path file exists across infra/aws/terraform (denominator printed), and 0 now carry a foreign Desktop path.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cat infra/aws/terraform/shared-infra/.terraform/plugin_path BEFORE the init, 2026-10-07 ~10:0xZ: the single foreign entry quoted in world_is; file mtime 2026-09-25 19:37",
      "test -d on that path: ABSENT -- the Desktop tree irpt-smoke-p-backend-20260923 no longer exists, so the pointer was dangling",
      "ls infra/aws/terraform/shared-infra/.terraform/ BEFORE: modules, plugin_path, terraform.tfstate -- NO providers directory; find .../.terraform/providers returned nothing",
      "infra/aws/terraform/shared-infra/.terraform.lock.hcl: hashicorp/aws version 5.100.0, constraints ~> 5.0",
      "ls C:/Users/AndrewBerman/.terraform.d/plugin-cache/registry.terraform.io/hashicorp/aws/5.100.0/windows_amd64/: terraform-provider-aws_v5.100.0_x5.exe present (718820352 B); cache also holds 6.67.0",
      "terraform -chdir=infra/aws/terraform/shared-infra init -input=false -no-color -reconfigure -plugin-dir=C:/Users/AndrewBerman/.terraform.d/plugin-cache -> 'Successfully configured the backend \"s3\"!', 'Reusing previous version of hashicorp/aws from the dependency lock file', 'Using hashicorp/aws v5.100.0 from the shared cache directory', rc=0",
      "cat plugin_path AFTER the init: [\"C:/Users/AndrewBerman/.terraform.d/plugin-cache\"]; ls .terraform/ now also shows providers",
      "terraform state list after the init: 252 resources, including aws_s3_bucket_policy.opal_data_49financial, aws_s3_bucket_policy.lgic_firm[\"cottonwood\"] and aws_s3_bucket_policy.lgic_firm[\"inflection\"] -- the control proving -reconfigure did not re-point the state",
      "python -c over infra/aws/terraform: 1 plugin_path file scanned, 0 carrying a foreign Desktop path, after the fix"
    ]
  },
  "notes": "Filed under CLAUDE.md section 2 (append a row and keep working, do not halt to investigate). It is NOT the reason TO-APPLY-4 stopped -- that was the cottonwood rider, reported to 2.0.0_SA_COO~C at ~10:0xZ and recorded at commit 54295756ad. Checked against the channel before filing: existing rows discuss the plugin CACHE and a provider kit for the Dells (around lines 128, 154, 1322, 1342), but none names a dangling foreign plugin_path in a shared-tree root, so this is not a re-file of an owned class. Disposition left UNDER_INVESTIGATION because terminating a row is the CVO's act, not this seat's.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_CTLPLN-W13-S6 -- CT-k-2: The laptop's portal node_modules is an older install than the DEV lockfile (absent=6, extra=103), so the kit has no correct tree to carry yet

```json
{
  "id": "NFRA_CTLPLN-W13-S6",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T10:27:42Z",
  "one_line": "The laptop's portal node_modules does NOT match the DEV lockfile: 6 locked packages are on disk at other versions and 103 packages on disk are in no lock entry, so describe reads absent=6 ok=False and pack refuses.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/devices/kit_portal_tree.py describe (read-only, 1-2 s): PORTAL-TREE head=481b3bcc5f22 lockfile=bun.lock lock_sha256=b32cb20e3d31 equals_dev=True bun=1.3.9 node=v26.10.0 packages=487 present=409 absent=6 files=41952 bytes=447989421 ok=False, on branch wk-NFRA_CTLPLN-13 (base 16b9fd1ba8 + this commit)",
      "PORTAL-ABSENT lines: @types/d3-array lock=3.2.2 disk=3.0.3; @types/d3-interpolate lock=3.0.4 disk=3.0.1; baseline-browser-mapping lock=2.10.0 disk=2.11.22; caniuse-lite lock=1.0.30001775 disk=1.0.30001810; d3-format lock=3.1.0 disk=1.4.5; d3-time-format lock=4.1.0 disk=3.0.0; PORTAL-CLASSES extra_on_disk=103 (for example @nivo/*, @puppeteer/browsers, @react-spring/animated)",
      "the working bun.lock equals git show origin/DEV:bun.lock after folding CRLF to LF (equals_dev=True; raw SHA-256 differs only by line endings); node_modules has no .package-lock.json and mtime Feb 20 2026 (react/package.json Mar 2 2026), older than the lockfile, so the tree was installed from an earlier lockfile"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-k-2 AMENDMENT 2 and CTO msg 106138: the bring-up kit carries the laptop's portal dependency tree at the DEV lockfile.",
  "world_is": "The laptop's tree is NOT at the DEV lockfile: it is an older install. The lockfile equals DEV, the tree does not equal the lockfile (absent=6 of 487, extra=103). The tool's pack therefore refuses (pack on the real tree was not run; no archive exists). The tree must be brought to the lockfile by an install on a box that may reach the registry, which this order forbids this worker to do; until then there is nothing correct to carry. The test cases and the tool's refusal arm are proven on stand-ins."
}
```

## NFRA_CTLPLN-W9-S1 -- the row schemas still refuse a Dell id and a dell fabric value

```json
{
  "id": "NFRA_CTLPLN-W9-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~9",
  "surfaced_at": "2026-10-07T08:46:27Z",
  "one_line": "The two row schemas still admit only laptop and site-z (enum) and only the Z- infix (id pattern), so a Dell row is refused by the gate's Draft-07 limb even though CT-d-6's derivation now admits it.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/surprise_channel/schemas/investigation_item.schema.json and remediation_row.schema.json at f70d7dd545: properties.fabric.enum = ['laptop','site-z'] and properties.id.pattern = '^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$'",
      "CT-d-6 worktree, 2026-10-07: surprise-row-gate._check_row on {id: X_PRJ-D1-S1, fabric: dell1} against investigation_item.schema.json prints \"fabric='dell1' is not in the ratified enum ['laptop', 'site-z']\" and \"'X_PRJ-D1-S1' does not match '^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$'\"; the identity derivation itself returns no complaint"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-6 AMENDMENT 1: after the edit a row filed on dell1 as <CODE>-D1-S<n> is admitted and a bare Dell id is refused; the order's paths name the gate, PRD_HEADER.schema.json and DEVICES.json only.",
  "world_is": "The gate's id-to-fabric derivation now reads the register and admits D1-/D2- ids, but the row schemas it validates every new row against (outside this order's paths) still carry the two-value fabric enum and the (Z-)? id pattern, so a real Dell row is refused at the schema limb until both files change. The ID_RE grammar in the gate is widened; the two schema patterns are a third copy of that grammar. Not fixed here (not in the grant); the issuer or the CTO owns the schema edit."
}
```

## NFRA_CTLPLN-W9-S2 -- adjudicates and disarms item patterns still carry the old id grammar

```json
{
  "id": "NFRA_CTLPLN-W9-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~9",
  "surfaced_at": "2026-10-07T09:24:00Z",
  "one_line": "Two more copies of the old id pattern remain in the row schemas: adjudicates items (investigation) and disarms items (remediation) still refuse a Dell id.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/surprise_channel/schemas/investigation_item.schema.json properties.adjudicates.items.pattern and remediation_row.schema.json properties.disarms.items.pattern, after the CT-d-6 AMENDMENT 2 edit, still read '^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$'",
      "CT-d-6 worktree, 2026-10-07: Draft7Validator on each items subschema: 'X_PRJ-S1' ADMIT and 'X_PRJ-D1-S1' REFUSE, for adjudicates and for disarms"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-6 AMENDMENT 2: change the fabric enum and the id pattern in both schemas and nothing else, so a Dell row is admitted by the schema limb.",
  "world_is": "The id property is widened, but a row that cites a Dell id in `adjudicates` (an adjudication row) or in `disarms` (a remediation row) is still refused by the schema limb, because those two item patterns are separate copies of the old grammar and are outside the order's stated change. Not edited here. A Dell's plain row is unaffected; a Dell row that disarms or adjudicates another Dell row is not admitted until the two patterns follow."
}
```

## NFRA_CTLPLN-W9-S3 -- two more readers of the old id grammar outside the order's grant

```json
{
  "id": "NFRA_CTLPLN-W9-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~9",
  "surfaced_at": "2026-10-07T09:55:53Z",
  "one_line": "Two more readers of the old id grammar sit outside the order's grant: proof-of-spec-check.py SURPRISE_ID_RE and surprise-watch.sh ID_RE refuse or miss a Dell row id.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/proof-of-spec-check.py:1198 at 4ff3443cb4: SURPRISE_ID_RE = ^\\s*([A-Z0-9_]+-(?:Z-)?(?:W[0-9]+-|C-)?S[0-9]+)\\b ; CT-d-6 worktree 2026-10-07: re.match on 'X_PRJ-D1-S1' -> None, on 'X_PRJ-D1-W3-S2' -> None, on 'X_PRJ-S1' -> a match; the surprises limb (line 1308) turns a None into 'surprises[i] carries NO row id'",
      "org/surprise_channel/surprise-watch.sh:82 at 4ff3443cb4: ID_RE='^[[:space:]]*\"id\":[[:space:]]*\"[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+\"' counts rows by the old grammar, so a Dell row (<CODE>-D1-S<n>) is not counted by the watcher"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-6 AMENDMENT 3 report asks whether any other file under .tools/ or org/surprise_channel/ still holds the old two-fabric id pattern; the order's paths name the gate, the two row schemas, the test and the census only.",
  "world_is": "Two copies of the old id grammar remain outside the grant. proof-of-spec-check.py's surprises limb would refuse a Dell worker's proof instance that cites its own D1- row (the worker could not flip its order complete); surprise-watch.sh would not count a Dell row. Neither edited here. The gate's own ID_RE and both row schemas are current."
}
```

## NFRA_CTLPLN-W9-S4 -- a fourth live reader of the old id grammar outside the order's grant: the IRPT_YCDGEN stop-row filer

```json
{
  "id": "NFRA_CTLPLN-W9-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~9",
  "surfaced_at": "2026-10-07T10:32:46Z",
  "one_line": "The whole-repo id-grammar sweep finds a fourth live reader of the old grammar outside the order's grant: infra/aws/lambda/investor-reporting/ycharts/research/file_stop_row.py ID_PATTERN refuses a Dell row id.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/research/file_stop_row.py:13 at 75b3d75714: ID_PATTERN = re.compile(r\"^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$\") with the comment 'investigation_item.schema.json id'; section() (line 19) raises ROW_ID_NOT_ADMITTED for any id the pattern does not match, so section(row, 'X_PRJ-D1-S1') is refused although the gate, both row schemas, the proof checker and the watcher now admit it",
      "test_fabric_readers_dell.py sweep() at this worktree, 2026-10-07: ID-GRAMMAR-SWEEP files_scanned=57075 hits=60 fixed_here=8 gate_derived=2 record=49 live_outside_grant=1; the one live hit is the line above; a second, independent census (every non-record code file whose regex holds the project class [A-Z0-9_]+- , 6 files) found no other reader"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-d-6 AMENDMENT 4 item 3: the sweep's zero is the condition for landing; a LIVE-READER-OUTSIDE-GRANT is listed, not edited, and carried by old_grammar_left.",
  "world_is": "One code file outside the grant still decides on the old two-fabric grammar. It is the IRPT_YCDGEN stop-row filer (prints a channel section for a runner stop row); a Dell-fabric stop row cannot be filed through it. Not edited here (path outside the order's grant); old_grammar_left carries 1, so CT4d6-AC1 reads old_grammar_left=1 ok=False until the issuer brings the file to the gate's grammar (or rules it out of scope) and the sweep reads zero."
}
```

## NFRA_CTLPLN-W14-S1 -- TO-CT-a-1: no declared SSM command document is RESIDENT-FIXED (0 of 16); dell2's policy carries no send statement

```json
{
  "id": "NFRA_CTLPLN-W14-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T10:21:13Z",
  "one_line": "TO-CT-a-1 read: 0 of 16 declared SSM command documents classify RESIDENT-FIXED; both resident documents take a free-text parameter that is interpolated into a shell command line, so dell2's policy is built with no send statement.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_ssm_documents.py --check, last line: SSM-DOCS declared=16 unresolved=0 resident_fixed=0 resident_free_text=2 export_render=1 other=13 unsure_params=2 in_policy=0 ok=True; census cross-check 16 uncommented 'resource \"aws_ssm_document\"' over 544 .tf files = 16 parsed, MATCH",
      "irpt-ycharts-deploy (investor-reporting/ycharts:aws_ssm_document.deploy, ssm.tf:19): parameter ArtifactPrefix (String, default the artifact prefix, no allowedValues, no allowedPattern) -> FREE-TEXT-COMMAND at infra/aws/terraform/investor-reporting/ycharts/ssm.tf:43: \"aws s3 cp {{ArtifactPrefix}} $APP_DIR/ --recursive --exclude 'secret-ids.env'\" (a caller value is substituted into the shell line, and what it fetches is then run: chmod +x run-ycharts-session.sh, npm install, npx playwright install)",
      "irpt-ycharts-run (aws_ssm_document.run, ssm.tf:56): parameter Task CONSTRAINED by allowedValues=['probe'] (ssm.tf:84 export YC_TASK='{{Task}}'); parameter MaxReacquisitions (String, default '1', no allowedValues, no allowedPattern) -> FREE-TEXT-COMMAND at ssm.tf:85: \"export YC_MAX_REACQUISITIONS='{{MaxReacquisitions}}'\" (a value containing a single quote closes the literal and the rest runs as shell)",
      "classifier control run on every --check: 5 synthetic blocks (free-text parameter, allowedValues, tight date allowedPattern, loose allowedPattern '^.*$', no parameters) classify as expected, so the 0 is not a broken classifier; the date allowedPattern on the unrelated advi chain document classifies CONSTRAINED through the same code",
      "the build per the order's bound: dell2_ssm_policy.json carries ReadCommandResults and DenyShellDocuments (the seven AWS shell and session document ARNs plus irpt-export-render-run, irpt-ycharts-deploy, irpt-ycharts-run by name) and NO send statement and NO DenyRewriteOfGrantedDocuments (an IAM statement cannot have an empty Resource list); simulate_policy.py: ssm_ok=12/12, allowed send arms 0",
      "not read: the live documents in the account were not compared to the repository text"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-a-1: the dell2 user gets ssm:SendCommand on the instance and on the RESIDENT-FIXED documents (at most three arms expected); 'if NO document classifies RESIDENT-FIXED, do not widen the rule: write the policy with the read statement and the Deny statements only, file a BLOCKING row with the table'.",
  "world_is": "The two resident documents are the only ones declared under investor-reporting/ycharts/, and each has one unconstrained parameter used inside a shell command line, so neither is fixed text; the grant is empty as the order's bound provides. What would change the classification is a text change by the document's owner, not by this cell: an allowedPattern on MaxReacquisitions (ssm.tf:71-75) and allowedValues on ArtifactPrefix (ssm.tf:28-32); irpt-ycharts-run is in addition a live vendor call that its own header says needs Andrew's per-use word, so whether it is ever granted to a Dell is a ruling, not a classification. The one document sent to the instance by code today is irpt-export-render-run (export/dispatch.py, to render_host_id), classified EXPORT-RENDER and denied by name."
}
```

## NFRA_CTLPLN-W14-S2 -- TO-CT-a-1: both Dells can rewrite a command document and the objects it runs, through the group policies

```json
{
  "id": "NFRA_CTLPLN-W14-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T10:21:13Z",
  "one_line": "Both Dells can rewrite a command document and the objects it downloads and runs, through the group policies; the same code-injection path the free-text read closes for SendCommand stays open, for dell1 as well and with no SendCommand grant at all.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell_create_policy.json statement CreateUpdateTagCompute allows ssm:CreateDocument, ssm:UpdateDocument and ssm:UpdateDocumentDefaultVersion on Resource *; it is a GROUP policy, so dell1 and dell2 both hold it. simulate_policy.py SSM-PROBE lines (iam:SimulateCustomPolicy, read-only): 'dell2 ssm:UpdateDocument on irpt-ycharts-deploy -> allowed' and 'dell1 ssm:UpdateDocument on irpt-ycharts-deploy -> allowed'",
      "the export controller sends irpt-export-render-run to i-0167fd745ad906a66 by itself (infra/aws/lambda/investor-reporting/export/dispatch.py RENDER_DOCUMENT; export/main.tf:84 render_host_id), under its own role: a Dell that rewrites that document's text, or makes another version its default, has its text run on the host's role at the next dispatch, with no SendCommand of its own",
      "run-time fetches of the documents read (derive_ssm_documents.py FETCH lines): irpt-ycharts-deploy ssm.tf:43 copies s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-ycharts/ (its default prefix) to /opt/investor-reporting-ycharts, then ssm.tf:44-46 chmod +x run-ycharts-session.sh, npm install, npx playwright install, and irpt-ycharts-run ssm.tf:86 runs bash /opt/investor-reporting-ycharts/run-ycharts-session.sh; irpt-export-render-run export/ssm.tf:55 copies s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/ and export/ssm.tf:91 runs bash /opt/investor-reporting-export/run-export-render.sh on every render",
      "who can write those two prefixes: dell_deploy_policy.json statement S3ObjectsOnOpalBuckets allows s3:PutObject on arn:aws:s3:::opal-*/*, which matches the artifacts bucket; no Deny in the five Dell policy files matches s3:PutObject there (DenyS3DeletesOnProductionData is opal-data-* only). Static match in derive_ssm_documents.py: dell_put_allowed_by=['dell_deploy_policy.json:S3ObjectsOnOpalBuckets'] dell_put_denied_by=none on both prefixes; simulator SSM-PROBE: 'dell2 s3:PutObject on the ycharts runner artifact prefix -> allowed', same for dell1",
      "the new policy's DenyRewriteOfGrantedDocuments covers only RESIDENT-FIXED documents (0 today), and it is attached to dell2 only, so it closes none of the above; whether the create policy has been applied was not read (no account call beyond the simulator)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "1.0.0_SA_CTO with 2.0.0_SA_COO~C: rule whether a Dell keeps ssm:UpdateDocument, ssm:UpdateDocumentDefaultVersion and ssm:CreateDocument on documents the estate sends to a host and s3:PutObject on the ec2/ artifact prefixes those documents download from, before dell_create_policy.json and dell_deploy_policy.json are applied; a Deny on those documents and prefixes in the group policies is a new cell, not this order's paths",
  "spec_asserts": "TO-CT-a-1: a Dell that can rewrite a resident document's text can run anything through the grant; add DenyRewriteOfGrantedDocuments on the RESIDENT-FIXED documents to the new policy and file ONE row saying the same hole is open for dell1 through the group's create policy and for both Dells on the instance's other inputs, naming any script a fixed document fetches at run time and whether a Dell can write it.",
  "world_is": "No document is RESIDENT-FIXED, so the Deny statement has no resource and is not in the policy. The hole is wider than the order stated: it does not need the SendCommand grant, because the render document and the runner scripts are executed by the estate's own controller and operators on the host's role, and the artifact prefixes they fetch are writable by both Dells under the group deploy policy. No fixed document exists, so the 'run-time script a granted document fetches' is reported for the documents that would have been in scope: the two resident documents and the export render document."
}
```

## NFRA_CTLPLN-W14-S3 -- TO-CT-a-1: the naming limb refuses the rendered targeted Deny; stopped after the census

```json
{
  "id": "NFRA_CTLPLN-W14-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T11:25:00Z",
  "one_line": "The commit gate's naming limb refuses the rendered targeted Deny (29 strings across the two new group policies name pipeline-owned functions, documents and S3 prefixes); the worker did not override, kept the census committed, and stopped before steps 2 to 4 landed.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh on the step-2 commit: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode)'; '[naming-gate] NAMING-GATE: REFUSE 29 graded'; 17 refused lines in the documents-and-prefixes policy file and 12 in the functions policy file, each a lookup of a pipeline-owner name on an ARN that names a function, a command document or an S3 prefix the census reached.",
      "the render itself succeeded and is reproducible: derive_reached_roles.py --from-file tests/reached_roles_census.json --render check|write printed 'ROUTES-DENY functions=31 (already in DenyProtectedFunctions: 2) task_definitions=0 documents=12 prefixes=5 policies=2 sizes=[5219, 1445] limit=6144', so two additional policies suffice and the more-than-two stop did not fire; the files were deleted from the worktree after the refusal and regenerate with --render write.",
      "the census (commit d6aed4ab85, tests/reached_roles_census.json) read 175 of 175 distinct roles, unread 0: 10 roles read YES (1 on IAM, 0 on the audit trail, 9 on production-data delete) and 165 read NO; the resident host's role reads NO. W14-S2's routes therefore stay open until the Deny lands."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "1.0.0_SA_CTO: rule how a policy that must name a pipeline-owned function, document or prefix passes the naming limb (an R20 register entry Andrew acknowledges, or a role-owning-project prefix form); then 2.0.0_SA_COO~C recuts steps 2 to 4 of the order.",
  "spec_asserts": "TO-CT-a-1 amendment 1 step 2: render the Deny for the YES roles' routes into group policy files; 'If the commit gate refuses a firm-name string in a policy file, do NOT use any override: file a BLOCKING row, keep step 1 committed, and stop.'",
  "world_is": "The gate refuses 29 strings in the rendered files, so no Deny, no dell2 command grant and no sixth or seventh simulation block were committed; step 1 and its census are. The order stays in_progress."
}
```

## NFRA_CTLPLN-W14-S4 -- TO-CT-a-1: the naming limb reads a reference to an existing resource as a minted name (for the LGIC_BLANKFIX project)

```json
{
  "id": "NFRA_CTLPLN-W14-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T12:03:41Z",
  "one_line": "The commit gate's naming limb read 29 lines that REFER to resources that already exist (functions, command documents, S3 prefixes) as if they were newly minted names and refused them; the form that passed holds no such name in any policy file.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "row NFRA_CTLPLN-W14-S3 in this file (commit 6704cbeb93): safe-commit.sh refused the rendered Deny with '[naming-gate] NAMING-GATE: REFUSE 29 graded' (17 refused lines in the documents-and-prefixes policy file, 12 in the functions policy file); every one of the 29 strings named a function, a command document or an S3 object prefix that exists in the account and is owned by another pipeline, not a name this cell mints",
      "the ruled form (CTO msg 106190, form b) keeps those names in one file under tests/ (the census) and lets Terraform build the statements from it at plan time; the commit that landed it (0c212eff57) passed the same gate with '[naming-gate] NAMING-GATE: PASS 2 graded' (the two policy names this cell does mint, both CONFORMANT)",
      "counts only, by design: the census holds 233 functions, 33 hosts and 175 roles; the module's route set is 33 function routes (31 not already in the name-based protected list), 12 command documents and 5 artifact prefixes; no name appears in this row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-a-1 amendment 2 step 9 (the CTO's ask): 'File the gate's blindness (a reference read as a minted name) as a row for LGIC_BLANKFIX'; class OBSERVATION, INERT.",
  "world_is": "The naming limb grades a string in a declaration-tree file by its shape and cannot tell a reference to an existing resource from a declaration of a new one, so any policy that must name an existing function, document or prefix is refused unless the names live outside the graded domain. Owner: the COO of the LGIC_BLANKFIX project, which is the project that would give the limb a way to tell the two apart. Nothing is harmed by leaving it: the workaround holds, at the cost that a policy cannot state its own resources in the file that applies it."
}
```

## NFRA_CTLPLN-W14-S5 -- TO-CT-a-1: CTa1-AC1's equality with RESIDENT-FIXED cannot hold under ruling D; the rule compares the policy with the granted set

```json
{
  "id": "NFRA_CTLPLN-W14-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T12:03:41Z",
  "one_line": "The face's CTa1-AC1 rule (the policy names exactly the RESIDENT-FIXED documents) cannot hold under ruling D, which grants the two resident documents that classify RESIDENT-FREE-TEXT (0 fixed, 2 free-text); derive_ssm_documents.py's ok rule now compares the policy with the granted set, and the face's rewrite Deny was not rendered.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_ssm_documents.py --check, last line: SSM-DOCS declared=16 unresolved=0 resident_fixed=0 resident_free_text=2 export_render=1 other=13 unsure_params=2 in_policy=2 ok=True; with the face's rule (k == resident_fixed) the same read would be ok=False by construction (k=2, a=0)",
      "the change is in derive_ssm_documents.py (commit 109a410fe7): granted_documents() returns the resident documents (RESIDENT-FIXED and RESIDENT-FREE-TEXT) only while the census reads NO for the resident host's role (read from tests/reached_roles_census.json, header taken_at 2026-10-07T11:05:41Z), and ok requires the policy's send statement to name exactly that set; the classification itself and its 16 of 16 resolved read are unchanged and still printed; unresolved=0 remains a condition",
      "the face's DenyRewriteOfGrantedDocuments (a Deny on rewriting the RESIDENT-FIXED documents) was never emitted (0 fixed documents) and is not in the amendment's three statements; amendment 1 point C rules no blanket Deny on document writes where the role at the end reads NO. Row NFRA_CTLPLN-W14-S2 (INVESTIGATION_v1.md) already records that both Dells can rewrite a document through the group create policy; that stays open and is now relevant to two granted documents whose host role reads NO"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-a-1 face: CTa1-AC1 'ok=True only when ... the policy of step 2 names EXACTLY the RESIDENT-FIXED documents (k == a)'; amendment 2 step 6: the policy names the two resident documents, and 'the classification stays a record, it no longer decides the grant'.",
  "world_is": "The two instructions cannot both be met: the two resident documents are free-text, so k == a was false the moment ruling D granted them. The ok rule was changed so that the recorded line stays a faithful check of the policy against what the ruling says the policy names; the expected value text in CTa1-AC1 (unresolved=0) is unchanged and the line still reports resident_fixed, resident_free_text and unsure_params so a reader can see the classification beside the grant."
}
```

## NFRA_CTLPLN-W6-S4 -- AMENDMENT 3: the generated marks over exemptions.json went stale at the dell2 registry rows, and every row landed there moves them again

```json
{
  "id": "NFRA_CTLPLN-W6-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T12:04:47Z",
  "one_line": "The mark in modules/opal_name/generated_locals.tf (and vectors.json, opal_name.tftest.hcl) is a hash over exemptions.json + scopes.json; it no longer matches since the dell2 rows landed, so the next row landed there (the scoped dell1 rows) needs the restamp the dell2 rows already need.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "derive_fence_row_shape.py output at this worktree: registry_hash(only=[exemptions.json, scopes.json]) = 9641c8676ad38b19 now; generated_locals.tf:1 carries registry@7cf7580cda2303a3 over exemptions.json,scopes.json",
      "the same hash computed from git show at commit e7ac51a04c^ is 7cf7580cda2303a3 and at e7ac51a04c is 9641c8676ad38b19: the mark was current before the dell2 rows commit and stale after it",
      "lib/opal_naming.py:134-136 TARGET_REGISTRY_KEYS: generated_locals.tf reads scopes+exemptions, vectors.json and opal_name.tftest.hcl read four files including exemptions; registry_hash(only=...) :173-184 feeds whole file bytes, so any row moves it although _gen_locals :1003-1029 uses only account_id"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 3 asks only whether a row can carry an action set and a prefix and for the shape to land; it names no restamp of generated files.",
  "world_is": "Landing any exemptions.json row changes the hash the three generated carriers declare; the dell2 rows were landed without the restamp, so the carriers already declare an old hash. The content of generated_locals.tf does not depend on the rows (only account_id), so nothing renders wrongly today; a freshness reader that compares the mark to the registry would read the module as stale. The proposal's landing steps include the restamp."
}
```

## NFRA_CTLPLN-W6-S5 -- AMENDMENT 3: a row carrying the new action and prefix fields is rendered by today's module as a FULL admission, so landing the row before the module learns the fields fails open

```json
{
  "id": "NFRA_CTLPLN-W6-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T12:04:47Z",
  "one_line": "Measured on a scratch copy outside the repository: a row with extra actions and prefix keys passes the validator and is rendered by modules/opal_name/main.tf:91-95 into the fence's admitted list as an ordinary admission, so the scoped dell1 row, if landed before the module and fence changes, would admit that user to the whole bucket with its own put.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "derive_fence_row_shape.py output: validator refusals 0 for three dell1 rows carrying actions+prefix (and 0 with a string and an integer in those keys); control with reason removed gives 3 refusals, so the scratch directory was the one read",
      "terraform console on a scratch copy of the module reading the scratch registry: local.fence_exemption_arns holds the dell1 ARN under 3 of 3 buckets (modules/opal_name/main.tf:91-95 reads r.arn / r.principal only)",
      "the simulator on plain admission (saved policy + the user in the admitted list): PutObject allowed, because dell_deploy_policy.json stmt S3ObjectsOnOpalBuckets allows s3:PutObject on opal-* and the fence's Deny no longer applies"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 3 expects absent fields to keep today's meaning and a new row to carry the scope; the order treats the shape as an addition.",
  "world_is": "No reader refuses an unknown key and the one reader that renders admission ignores it, so a new field is silent for every reader that was not changed in the same landing. INERT now because no such row exists and this pass lands none; it arms if the rows land before the module and the two fence files render the statements. The proposal states the landing order and an alternative shape (a sibling key) that fails closed."
}
```

## NFRA_CTLPLN-W13-S7 -- CT-k-2 AMENDMENT 4: a Terraform root holding only locals and an output does not plan to exit 0 on a fresh local backend; it reads 2

```json
{
  "id": "NFRA_CTLPLN-W13-S7",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T12:04:45Z",
  "one_line": "The order's premise that `plan -detailed-exitcode` reads 0 on a temporary local-backend root with only locals and outputs is false for a FRESH root: a new output is a change and the plan exits 2; the test seeds a hand-written state holding the output to reach 0, and keeps the fresh root as the exit-2 control.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "terraform 1.15.8 on this box, readback on a fresh root (backend local, locals a, output o): 'Changes to Outputs: + o = \"x\"' then TF-READBACK version=1.15.8 init=ok plan_exit=2 ok=True",
      "the same root with a terraform.tfstate (version 4, serial 1, outputs.o = x, no resources): 'no differences' then TF-READBACK version=1.15.8 init=ok plan_exit=0 ok=True; test_kit_terraform_providers.py case 10 asserts both lines"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-k-2 AMENDMENT 4 item 2: readback on a temporary root with a local backend and only locals and outputs reads init=ok plan_exit=0.",
  "world_is": "A fresh root reads plan_exit=2 (output additions count as changes under -detailed-exitcode). Case 10 therefore writes the state file by hand (no apply, no network) and reads 0, and also asserts the fresh root reads 2 loudly, which doubles as the control for the 0/2 distinction. Nothing was weakened: the expected line init=ok plan_exit=0 is asserted verbatim."
}
```

## NFRA_CTLPLN-W13-S8 -- CT-k-2 AMENDMENT 4: `terraform version` makes a version-check network call unless CHECKPOINT_DISABLE=1, so every terraform run in the kit sets it

```json
{
  "id": "NFRA_CTLPLN-W13-S8",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T12:04:45Z",
  "one_line": "A bare `terraform version` and `terraform init` consult Hashicorp's checkpoint service by default (a network call) unless CHECKPOINT_DISABLE is set, which the order's no-network rule does not mention; the kit sets CHECKPOINT_DISABLE=1 in the environment of every terraform it runs.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/kit_terraform_providers.py terraform_run_env() sets CHECKPOINT_DISABLE=1 and TF_IN_AUTOMATION=1 and drops TF_CLI_ARGS*, TF_LOG and TF_DATA_DIR; run_version, readback and the binary verb all run through it",
      "the checkpoint behaviour is Terraform's documented default (the CHECKPOINT_DISABLE environment variable switches it off); not exercised against a network here, by the rule"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-k-2 AMENDMENT 4: THE NO-NETWORK RULE STANDS; nothing is downloaded.",
  "world_is": "The order did not name the checkpoint call. The kit closes it in the environment it builds. The earlier seam probe (test case 5) built its own environment without the variable; it now sets CHECKPOINT_DISABLE=1 too (one added line in terraform_env, the case's expectations unchanged)."
}
```

## NFRA_CTLPLN-S13 -- bun auto-installs from the public registry on a run outside a node_modules tree: egress on dell2, the laptop unmeasured

```json
{
  "id": "NFRA_CTLPLN-S13",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T12:24:20Z",
  "one_line": "bun installs a missing package from the public registry when it runs a file outside a node_modules tree; two such fetches happened on dell2, and the user-level setting meant to stop it was measured ineffective there on bun 1.4.2.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C: cell CT-k-2 AMENDMENT 5 measures each candidate form against a loopback listener and the kit carries the form that passes; until then the CTO's interim rule (msg 106214) is the control on all three boxes",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "Relay file org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_1215Z.md, bus id 857091e4, from 0.0.0_AB_MSTR~DELL2: a seat's bun run fetched react and react-dom 19.3.0; the dell2 manager's own probe with ~/.bunfig.toml [install] auto = \"disable\" fetched left-pad (cache 506 -> 509)",
      "Finding file named there as CRO_FINDING_BUN_AUTO_INSTALL_EGRESS_DELL2_20261007.md @fd0c709235; that commit is NOT on the laptop trunk at this row's filing (git cat-file: not a valid object; positive control 414eb87094 is an ancestor), so this row rests on the relay, not on the finding's bytes",
      "1.0.0_SA_CTO msg 106214: the interim rule and the cell's control (a loopback listener that logs requests)",
      "The laptop (bun 1.3.9) is UNMEASURED: no bun run was made by this seat for this row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD C-KIT and the no-egress rule every order of this project carries: nothing a seat or worker runs on a box reaches a public package index without Andrew's per-use word; the portal kit (CT-k-2) was built so that a Dell needs no install.",
  "world_is": "The kit delivers node_modules for the portal tree only. bun, the runtime the kit names, has an auto-install behaviour that fetches from the public registry whenever an import does not resolve from a node_modules tree, so a bun run of a scratch file egresses silently. The one disarm tried on dell2 did not work. A fetch failure and a disabled install print the same error, so a dead-proxy probe cannot tell them apart; the cell's control is a listener that counts requests.",
  "notes": "Interim (CTO msg 106214), laptop and both Dells: bun runs only inside a portal tree that holds node_modules; no bun run of a file outside one; no probe that can reach the public registry. Disarms when the cell's measured form is in the kit and each box has read it back."
}
```

## NFRA_CTLPLN-S14 -- the dell2 command grant's read actions are on every command in the account; whether any command output holds a secret is unmeasured

```json
{
  "id": "NFRA_CTLPLN-S14",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T12:52:47Z",
  "one_line": "Once the dell2 command grant is applied, dell2 can read the result of any command sent in the account, not only its own; nobody has measured whether an existing command prints a secret to its output.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/nfra-ctlpln-identity/dell2_ssm_policy.json statement ReadCommandResults: ssm:GetCommandInvocation, ListCommandInvocations, ListCommands, DescribeInstanceInformation on Resource *",
      "CTO half org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_DELL_DENIES_AND_DELL2_GRANT_20261007.md @eb74cfb2d2, 'Two things this half adds': accepted and named; not measured by that seat; asks this row",
      "The grant is NOT applied at this row's filing (order NFRA_CTLPLN.TO-APPLY-6 pending)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The CTO's ruling for CT-a-1: dell2 gets the read actions that return a command's result.",
  "world_is": "The service offers no narrower resource for those four actions, so the grant reads every command's result. A command whose output prints a secret would be a defect in that command, and dell2 could read it. No read of existing command outputs for secrets has been made by any seat. Open: a bounded read of recent command invocations' output for secret-shaped strings, by a laptop seat, or an explicit acceptance."
}
```

## NFRA_CTLPLN-S15 -- the portal tree pack was unpacked on both Dells outside the kit's own verify step: bun 1.4.2 against the manifest's 1.3.9, and dell2 at a different portal commit

```json
{
  "id": "NFRA_CTLPLN-S15",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T12:52:47Z",
  "one_line": "Both Dells unpacked the portal dependency pack and passed the typecheck, but two of the conditions written for the unpack were not the ones met: their bun is 1.4.2 where the manifest names 1.3.9, and dell2 ran at portal commit 8ddfe40994 where the carrier named 481b3bcc5f.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "0.0.0_AB_MSTR msg 106209, relaying each Dell's read-back: 41,860 files each, typecheck rc=0 and 0 error lines each; both note bun 1.4.2 against the manifest's 1.3.9; dell2 typecheck at portal DEV 8ddfe40994; lockfile sha256 equal on both",
      "1.0.0_SA_CTO msg 106199, the unpack condition: lockfile sha256 equal AND portal HEAD 481b3bcc5f on DEV; a mismatch is a row, never an unpack",
      "org/devices/kit_portal_tree.py verify refuses a bun version difference by design (CT-k-2 AMENDMENT 3); the Dells' reports do not say that step was run",
      "Not read by this seat: either Dell's tree"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-k-2 AMENDMENT 3: the pack installs only where lockfile, bun version and platform equal the manifest's; the carrier's relay added the portal commit.",
  "world_is": "The lockfile matched on both boxes and the typecheck passed, which is the evidence the tree works there. The bun version rule was not enforced at the unpack, and dell2's portal commit differs from the one named while its lockfile hash is equal. Open for the CTO: whether the kit's bun check is exact or tolerates a minor version, and whether the commit condition is the lockfile hash alone."
}
```

## NFRA_CTLPLN-S16 -- sequence-check's capacity and NEXT COO SLOT lines read one box's liveness; with four boxes they answer for the laptop only

```json
{
  "id": "NFRA_CTLPLN-S16",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T12:52:47Z",
  "one_line": "The sequence check counts the laptop broker's lanes only, so its capacity and next-slot lines flag a project seated on a Dell as needing a slot.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "1.0.0_SA_CTO msg 106077, verbatim: 'sequence-check reads MDPF_SECHIST NEEDS-SLOT because it counts the laptop broker's lanes only and the tree row's coo_lane is empty ... a row for NFRA_CTLPLN's backlog -- sequence-check's capacity and NEXT COO SLOT lines read one box's liveness; with four boxes they must read each box's lanes or say which box they read.'",
      "Not re-run by this seat"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD NFRA_CTLPLN: four devices, each with its own broker; a fabric reader either reads every box or says which box it read.",
  "world_is": "A backlog item for a later round's enrichment list: the check reads each box's lanes, or prints the box it read beside the number. Until then a NEEDS-SLOT flag on a Dell-seated project is not a finding against that Dell."
}
```

## NFRA_CTLPLN-W13-S9 -- the provisioning script's default mode was already link (none only where the main tree holds no node_modules)

```json
{
  "id": "NFRA_CTLPLN-W13-S9",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T13:00:11Z",
  "one_line": "the provisioning script's default mode was already link (none only where the main tree holds no node_modules); the order's 'default becomes link' therefore changes no behaviour, and the install mode was the only live registry path",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-k-2.dell-python-kit.md AMENDMENT 5 item 3 and CTO msg 106220: 'the default becomes link'",
      ".tools/wk-provision.sh at 69288c8ca0, cmd_portal: with no --node-modules the mode was link when <main>/portal/node_modules exists, else none; install was reachable only by naming it",
      ".tools/tests/test_wk_provision_no_registry.py check D-default: a default provision on a scratch repository prints NODE_MODULES: link; check G: the pre-change script and the new script print identical lines for default, none and link"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 5 item 3: the DEFAULT mode becomes link; link and none behave exactly as before.",
  "world_is": "The default was already link wherever a main-tree node_modules exists, and none where it does not (a link to a missing target would fail after the nested worktree is created, a half-landed state). The script now states the default in a comment and its usage text and keeps the none fallback; the only behavioural change is the install-mode refusal, raised before any worktree is created."
}
```

## NFRA_CTLPLN-W13-S10 -- the measuring tool's first user-level control arm sent 6 requests toward the PUBLIC registry host in each of t

```json
{
  "id": "NFRA_CTLPLN-W13-S10",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T13:00:11Z",
  "one_line": "the measuring tool's first user-level control arm sent 6 requests toward the PUBLIC registry host in each of two runs; the loopback proxy listener caught every one (CONNECT registry.npmjs.org:443, answered 502) and the arm was replaced by one that needs no network",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/test_kit_bun_no_egress.py first full run printed 'BUN-NO-EGRESS ... positive_requests=6 ... leaked_public=6 ... ok=False' with arm 'control:user-bunfig-registry-is-read' at registry=0 proxy=6; a second measure run with the file written to both HOME and XDG_CONFIG_HOME printed the same, proxy lines 'CONNECT registry.npmjs.org:443 HTTP/1.1' x6 (kept in the worktree scratch measure2.json, uncommitted)",
      "cause: the control gave a user-level bunfig a registry= line expecting bun run to read it from the temporary HOME; bun 1.3.9 does not read the user-level file for bun run (see row W13-S11), so bun used its default registry, and the second redirect (the proxy) kept the request on this machine: cache_files=0 in both arms, rc=1 with bun's resolution error",
      "fix: org/devices/kit_bun_no_egress.py arm control:user-bunfig-is-read-by-run now uses a MALFORMED user-level file and the --no-install flag, so it makes no request by construction; the final measure reads leaked_public=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 5: every bun process runs inside a harness with two independent redirects; a candidate is judged by counting requests on the two listeners.",
  "world_is": "A control arm of the worker's own design could reach the public host if the redirect it relied on was not read. The proxy listener is what held it: both runs show the request on the proxy listener, none on any other path that this seat can see. What stays unproven is a request that bypassed BOTH listeners; bounded by cache_files=0 and bun's own resolution error text in those arms."
}
```

## NFRA_CTLPLN-W13-S11 -- bun 1.3.9 on Windows does not read a user-level .bunfig.toml for `bun run` (a malformed file in the temporary 

```json
{
  "id": "NFRA_CTLPLN-W13-S11",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T13:00:11Z",
  "one_line": "bun 1.3.9 on Windows does not read a user-level .bunfig.toml for `bun run` (a malformed file in the temporary HOME and in XDG_CONFIG_HOME is ignored), so `[install] auto = \"disable\"` there cannot stop the runtime auto-install; this is the measured reason the other machine's user-level setting failed",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/kit_bun_no_egress.py measure, arm control:user-bunfig-is-read-by-run: user-level file '[install]' + 'auto = ' (a TOML syntax error) in %HOME% and %XDG_CONFIG_HOME%, run as 'bun --no-install run probe.js': registry=0 proxy=0 rc=1 and bun reported the probe's resolution error, not a config error, so the file was never read",
      "arm user-bunfig (the valid file with auto = \"disable\"): registry=0 proxy=6 rc=1, verdict FAIL, the same count as the positive arm",
      "NOT measured: whether bun install / bunx read the user-level file (no install is run by this order)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 5 item 1(c): the same setting in a user-level bunfig inside the temporary home, to reproduce the other machine's reading on this version.",
  "world_is": "The reading reproduces (6 requests), and the control shows why: for `bun run` the user-level bunfig is not consulted at all, so the setting is inert rather than ignored-in-part. A project bunfig and the --no-install flag do pass."
}
```

## NFRA_CTLPLN-W13-S12 -- an extra step 0b was added to the order of proof: a bun fetch of a loopback URL through the proxy variables, t

```json
{
  "id": "NFRA_CTLPLN-W13-S12",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T13:00:11Z",
  "one_line": "an extra step 0b was added to the order of proof: a bun fetch of a loopback URL through the proxy variables, to establish that this bun's HTTP client honours the proxy before any arm that could fetch from the registry",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/kit_bun_no_egress.py run_order_of_proof: arm proxy-honor-check, 'bun run fetchcheck.js' whose only URL is the loopback registry listener: registry=0 proxy=1 (the request line GET http://127.0.0.1:<port>/proxy-honor-check arrived on the proxy listener, answered 502, bun printed fetch-status 502)",
      "the order of proof in the task order names steps 0, 1 and 2 only; step 0b runs after step 0 and before step 1, makes no request that can leave the machine by construction (the URL is loopback), and gates the single-form trials of Redirect A on its result"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 5 ORDER OF PROOF: (0) bun --version, (1) proxy proof with --no-install, (2) the positive arm; step 1 'cannot prove the proxy works'.",
  "world_is": "The proxy was proven honoured by this bun before the positive arm, so the single-form trials of Redirect A ran with a proven second net. Step 1 stays as ordered and still reads zero requests."
}
```

## NFRA_CTLPLN-W13-S13 -- the earlier criterion CTk2-AC5's test (org/devices/test_kit_portal_tree.py case 7) runs `bun run --silent --no

```json
{
  "id": "NFRA_CTLPLN-W13-S13",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T13:03:41Z",
  "one_line": "the earlier criterion CTk2-AC5's test (org/devices/test_kit_portal_tree.py case 7) runs `bun run --silent --no-install typecheck` once in a synthetic portal under the system temporary directory, outside the loopback harness; the script is `echo typecheck-ok`, so nothing is resolved or fetched",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/test_kit_portal_tree.py line 91 builds the synthetic package.json with scripts.typecheck = 'echo typecheck-ok'; case 7 calls kit_portal_tree.typecheck, which builds argv ['bun','run','--silent','--no-install','typecheck'] (org/devices/kit_portal_tree.py line 782) and runs it in the synthetic portal; the case printed PORTAL-TYPECHECK ... exit=0 last_line=typecheck-ok",
      "this order told the worker that kit_portal_tree.py describe runs bun for its version only (true); it also required running the AC5 test, whose case 7 is a further bun process. It was run once, by this seat, in the earlier-criteria pass, and its zero-request status was not counted by a listener",
      "the form it carries, --no-install, is the form this cell measured as passing on this bun (flag:--no-install: registry=0 proxy=0 against a positive arm of 6)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 5: every bun process runs inside a harness with loopback redirects; the only unharnessed bun is a bare bun --version.",
  "world_is": "One bun process of the earlier kit's own test ran outside the harness. It carries --no-install and a script with no import, so it cannot auto-install; the Dell read-back typecheck in kit_portal_tree.py already uses that flag. Not counted by a listener, so reported rather than measured."
}
```

## NFRA_CTLPLN-S17 -- disarm record for NFRA_CTLPLN-S13: --no-install measured on bun 1.3.9 and 1.4.2; dell2 covered by Andrew's word; a bare run still fetches

```json
{
  "id": "NFRA_CTLPLN-S17",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T14:23:01Z",
  "one_line": "Disarm record for NFRA_CTLPLN-S13: the flag --no-install stops bun's registry fetch on bun 1.3.9 (laptop) and bun 1.4.2 (dell1), measured by request count; dell2 is not measured, on Andrew's word that dell1's read stands for both.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Laptop, issuer's own run at 3b95b7c3aa: BUN-NO-EGRESS bun=1.3.9 positive_requests=6 candidates=9 passing=4 leaked_public=0 form=flag:--no-install ok=True",
      "dell1, bus c1d80ce3 (file org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_READBACKS_FOR_COO_C_20261007_1420Z.md), behind an outbound firewall block on bun.exe that Andrew added in an elevated shell: BUN-LISTENER-SELFCHECK ok=True; BUN-NO-EGRESS bun=1.4.2 positive_requests=6 candidates=12 passing=4 leaked_public=0 form=flag:--no-install ok=True",
      "dell2: NOT measured. Andrew-direct at the dell2 terminal ~14:0xZ as relayed by 0.0.0_AB_MSTR msg 106292, verbatim: 'we dont need to test the bun firewall process here because we've already proved it on dell1.' dell2 runs bun 1.4.2 by its own earlier report (msg 106209)",
      "Merged @e131723efb: org/devices/kit_bun_no_egress.py wrap carries the flag and refuses install-class commands; .tools/wk-provision.sh refuses its install mode without a non-public registry redirect (CTk2-AC8 7/7, CTk2-AC9 ok)",
      "Not read at this filing: dell1's confirmation that the firewall rule was removed; dell1's full result file (kept on dell1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "NFRA_CTLPLN-S13 (ARMED): bun fetches from the public registry on a run outside a node_modules tree; disarm when the measured form is in the kit and each box has read it back.",
  "world_is": "The measured form is in the kit and two of three boxes read it back; the third is covered by Andrew's word, not by a measurement. What the disarm is: a wrapper and a flag a seat must USE. A bare `bun run` of a file outside a node_modules tree still fetches on every box; nothing mechanical stops a seat from typing it. The CTO's interim rule (msgs 106214, 106220: bun only inside a portal tree that holds node_modules; no bun install) therefore remains the standing control, and S13 is disarmed only for a seat that follows it or uses the wrapper. Whether a mechanical stop is wanted (a PATH shim, a standing firewall rule) is an open question for the CTO and Andrew, not built here."
}
```

## NFRA_CTLPLN-W8-S3 -- TO-CT-d-5 amendment: dell_respol_policy.json has no generator and the script has no --check

```json
{
  "id": "NFRA_CTLPLN-W8-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~8",
  "surfaced_at": "2026-10-07T14:14:33Z",
  "one_line": "The amendment says dell_respol_policy.json is produced by tests/derive_respol_actions.py and names a --check and a regenerate command; the script is a read-only checker that takes no argument and writes nothing.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/nfra-ctlpln-identity/tests/derive_respol_actions.py main(): reads the four policy documents and the Deny statement, prints, returns; no write call and no argparse",
      "git log --follow dell_respol_policy.json: one commit, ce05f0e838, the file created by hand with the build"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT step 2: add sqs:SetQueueAttributes by the file's own generator (tests/derive_respol_actions.py), regenerate with the generator's own command, run its --check.",
  "world_is": "The JSON (hand-wrapped, one Deny statement, sorted actions) was edited by inserting one sorted entry in place; derive_respol_actions.py was changed to carry the action as RULED-IN (removed from RULED_ALLOWED) and its single run is the check: RESPOL-DERIVED ... actions=75 covered=75/75 ruled_allowed_caught=0 ok=True. No --check flag exists and none was added."
}
```

## NFRA_CTLPLN-W8-S4 -- TO-CT-d-5 amendment: the simulation block count 13 needs one arm the amendment did not name

```json
{
  "id": "NFRA_CTLPLN-W8-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~8",
  "surfaced_at": "2026-10-07T14:14:33Z",
  "one_line": "The existing respol block already held sqs:SetQueueAttributes -> allowed, so adding the two named arms to a block of 11 cannot read 13: that arm has to flip, giving 12; a neighbouring-action control (sqs:TagQueue -> allowed) was added to reach the ordered respol_ok=13/13.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py RESPOL list before this pass: 11 arms including (sqs:SetQueueAttributes, allowed)",
      "last line of the simulation after the edit: POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=13/13 ssm_ok=9/9 routes_ok=5/5 all_ok=True"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT step 2: extend the block by two arms (SetQueueAttributes -> explicitDeny; CreateQueue -> allowed); the block then reads 13 of 13.",
  "world_is": "Block is now 9 explicitDeny arms + sqs:SetQueueAttributes explicitDeny + sqs:CreateQueue allowed + sqs:TagQueue allowed + sns:SetTopicAttributes allowed = 13; the old SetQueueAttributes-allowed arm was changed, not kept. TagQueue is the unnamed addition: it shows the Deny does not catch the neighbouring queue action the create policy allows."
}
```

## NFRA_CTLPLN-W8-S5 -- TO-CT-d-5 amendment: the Deny leaves a dead Allow, and a read-only derivation still lists SetQueueAttributes as a queue update need

```json
{
  "id": "NFRA_CTLPLN-W8-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~8",
  "surfaced_at": "2026-10-07T14:14:33Z",
  "one_line": "dell_create_policy.json still Allows sqs:SetQueueAttributes and tests/derive_resource_kinds.py still lists it as an update action of aws_sqs_queue; the explicit Deny now overrides both, so a Dell can no longer update a queue, and six roots that declare a separate queue policy cannot be applied from a Dell.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "tests/queue_attribute_writers.json declared.by_root and the native Grep over infra/aws/terraform for the four resource kinds: 23 aws_sqs_queue, 9 aws_sqs_queue_policy, 0 redrive_policy, 0 redrive_allow_policy",
      "infra/aws/terraform/nfra-ctlpln-identity/dell_create_policy.json line 36 and tests/derive_resource_kinds.py line 80 at b062620452"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT: deny sqs:SetQueueAttributes for the Dell group; a later change goes by write-in; say which roots declare a separate policy resource and whether any is Dell-placed.",
  "world_is": "Read-only files are unchanged (dell_create_policy.json line 36, derive_resource_kinds.py line 80); check_identity.py still reads ok=True. Roots declaring a separate aws_sqs_queue_policy: globgrph, inf-pipeline, nfra-agentbus, nfra-agentbus-alyssa01, opal-gateway, partner-etl-ops-alerts (9 resources). No project row in org/projects carries a Dell fabric (392 rows: 38 laptop, 16 site-z, 338 unset), and the root-to-project mapping was not read, so no root is shown Dell-placed or not."
}
```

## NFRA_CTLPLN-W13-S14 -- ruff is installed as py3-none-win_amd64 (Root-Is-Purelib false), a build that fits Python 3.14 on win_amd64 bu

```json
{
  "id": "NFRA_CTLPLN-W13-S14",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T14:36:33Z",
  "one_line": "ruff is installed as py3-none-win_amd64 (Root-Is-Purelib false), a build that fits Python 3.14 on win_amd64 but is neither pure Python nor stable-ABI; the order's classes do not name it, so it is classed ABI3-INSTALLED with fit_kind no-abi-platform",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/kit_python_wheels_cp314.json requirements[name=ruff]: class ABI3-INSTALLED, tags [py3-none-win_amd64], fit_kind no-abi-platform, evidence <site-packages:3.12>/ruff-0.15.11.dist-info",
      "packaging.tags.compatible_tags(python_version=(3,14), interpreter='cp314', platforms=['win_amd64']) yields py3-none-win_amd64, so the target installs it; the order defines PURE-INSTALLED as Root-Is-Purelib true with py*-none-any and ABI3-INSTALLED as cp3X-abi3-win_amd64 only",
      "the other ABI3-INSTALLED rows are true stable-ABI builds (bcrypt cp39, curl_cffi cp39, psutil cp37, PyMuPDF cp310, cryptography cp311, safetensors cp38, tokenizers cp39); the tool also reserves fit_kind native-target for an installed cp314 build, which no copy on this machine is"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 6: an installed distribution is PURE-INSTALLED (py3-none-any, Root-Is-Purelib true), ABI3-INSTALLED (cp3X-abi3-win_amd64, X <= 14), or does not fit (cp312-cp312-win_amd64); no class for a platform-specific, ABI-free build.",
  "world_is": "ruff 0.15.11 is a py3-none-win_amd64 wheel: it fits 3.14 on win_amd64 and has no Python-version binding, but its files include a platform binary and a Scripts entry, so a re-pack from RECORD must keep the platform tag. The tool classed it ABI3-INSTALLED and says why in fit_kind; the issuer may rename or split the class."
}
```

## NFRA_CTLPLN-W13-S15 -- this machine holds no Python 3.14 interpreter and its pip cache holds zero entries, so no requirement is WHEEL

```json
{
  "id": "NFRA_CTLPLN-W13-S15",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T14:36:33Z",
  "one_line": "this machine holds no Python 3.14 interpreter and its pip cache holds zero entries, so no requirement is WHEEL-ON-DISK: every non-compiled-for-3.12 package depends on an offline re-pack from installed files, and the 3.14 stand-in folder is empty",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/kit_python_wheels_cp314.json sources: pip cache present, entries 0, bytes 0; kit pack output (3 directories under the temporary root), Downloads (45597 directories walked), this worktree and the base checkout: 0 wheels identified (the only .whl file under the repository is a 0-byte numpy-1.26.4-cp312 file under infra/aws/lambda/layers/pyiceberg-nessie-deps/python, counted not_a_wheel)",
      "interpreters: py -0p lists one (3.12.10 under the user's Programs\\Python\\Python312); a Program Files Python314 folder has Doc, Lib/site-packages (empty) and Scripts but no python.exe; HKLM PythonCore 3.14 has no InstallPath; HKCU PythonCore 3.12 names an anaconda3 folder that does not exist",
      "pip cache list prints 'No locally built wheels cached.'; the kit's own pack tool (a) 'wheel already in pip's local cache' therefore finds nothing on this machine"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 6: sources to read include the pip HTTP and wheel caches, kit pack output, Downloads and the repository for wheel files, and the installed distributions of every interpreter py -0p lists.",
  "world_is": "Only one interpreter's site-packages (3.12, 307 distributions read, plus 7 in the user site) can be read; the 3.14 folder is empty and no wheel file of any tag exists in any named source. The result is therefore: 41 PURE-INSTALLED and 8 ABI3-INSTALLED (re-pack from installed files, not yet done), 18 NEEDS-FETCH (compiled cp312 only), 0 WHEEL-ON-DISK."
}
```

## NFRA_CTLPLN-S18 -- requirements.txt omits 73 dependencies of the 67 packages it lists; 12 are compiled for Python 3.12 only

```json
{
  "id": "NFRA_CTLPLN-S18",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T15:28:38Z",
  "one_line": "The regenerated root requirements.txt lists 67 packages and omits 73 that those packages themselves require; 12 of the 73 are compiled for Python 3.12 only, so an install from the file alone would not be complete on any box and cannot be on a Dell.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Issuer's re-run on the merged tool: PY-REQ lines=67 parsed=67 unparsed=0 in_both=20 only_requirements=47 only_census=0 ok=True; PY-WHEELS target=cp314-win_amd64 requirements=67 wheel_on_disk=0 pure_installed=41 abi3_installed=8 needs_fetch=18 not_applicable=0 unparsed=0 undeclared_deps=73 ok=True",
      "Decision file org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/PYTHON_WHEELS_NEEDING_A_FETCH_FOR_CP314.md (merged @bd489b912b): the 73 names with the requirement that needs each; in a secondary read of the installed copies 59 are pure, 12 compiled for cp312 only (aiohttp, cffi, charset-normalizer, click, contourpy, coverage, fonttools, greenlet, jiter, kiwisolver, mmh3, regex), 2 fit",
      "requirements.txt @bc10584676 (3.0.0_SA_CVO, on Andrew's word); the file's own caveat: a clean-start resolve is not verified",
      "1.0.0_SA_CTO msg 106317 item 3: 'The 73 omitted dependencies are a defect in requirements.txt; file it for 3.0.0_SA_CVO, who wrote the file.'",
      "How the 73 were counted: the Requires-Dist of each found installed copy, markers evaluated for Python 3.14 on 64-bit Windows; a dependency needed only under another marker is not counted; a package with no installed copy here contributes none"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The record for the regenerated file: requirements.txt holds all actual dependencies.",
  "world_is": "The file holds the packages the firm's code imports directly. Their own dependencies are not listed, so the list is complete for an index-backed install (pip resolves the rest) and incomplete for an offline one, which is the only kind a Dell may make. The Python kit therefore installs with no dependency resolution and reports an import that fails for a missing dependency as its own class. Owner of the file: 3.0.0_SA_CVO. Whether the file should pin the full closure, or a second generated file should, is for that owner and the package-intake design (PRD v0.16, C-INTAKE)."
}
```

## NFRA_CTLPLN-W6-S6 -- AMENDMENT 4: check_dell_fence_join.py is still a reader that ignores an unknown row key, and it is outside the grant and pinned

```json
{
  "id": "NFRA_CTLPLN-W6-S6",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T13:34:29Z",
  "one_line": "After the validator and the module refuse an unknown key, tests/check_dell_fence_join.py (render_arns, registry_diff) still ignores one: measured by derive_fence_row_shape.py, a scratch row with an unknown key renders the dell1 ARN into 3 of 3 buckets there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "derive_fence_row_shape.py output (AC2 after the build): validator refusals 3 for rows plus an unknown key; terraform plan in a scratch module rc=1 (precondition); join check renderer: dell1 ARN in the rendered list of 3/3 buckets; FENCE-ROW-SHAPE ... extra_key_ignored=1 extra_key_refused=2",
      "infra/aws/terraform/shared-infra/tests/check_dell_fence_join.py render_arns() reads r.get('arn') / r['principal'] only; the check is not in this amendment's write grant and the order says not to touch it or its pin"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 4: every reader of the file must refuse an unknown key, never ignore it.",
  "world_is": "Two of the three row-parsing readers now refuse (the validator, and the module at plan time). The third is a test that renders nothing into any policy, so the hazard is INERT: it can only mis-grade, not admit. It is left as it is by the order; the issuer re-grades it at the merge when it moves the pin."
}
```

## NFRA_CTLPLN-W6-S7 -- AMENDMENT 4: derive_fence_row_shape.py (AC2) did not finish in 120 s at the start of this pass, and its probe had to change

```json
{
  "id": "NFRA_CTLPLN-W6-S7",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T13:34:29Z",
  "one_line": "CT4d2-AC2's script read rc=124 after 120 s on this worktree before any edit; the order did not say it would need changes, but the amendment's closed key set makes its actions+prefix probe a valid row, and its scratch module copy collided with the landed output.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "timeout 120 python infra/aws/terraform/shared-infra/tests/derive_fence_row_shape.py before any edit: real 2m0.7s, rc=124 (check_dell_fence_join.py in the same worktree: 1m9s, rc=0)",
      "after the edit: real 42 s, rc=0, last line FENCE-ROW-SHAPE rows=29 key_sets=1 rows_with_actions=0 rows_with_prefix=0 readers=16 extra_key_ignored=1 extra_key_refused=2 can_carry_today=False ok=True",
      "changes: sim_call caches results in a temporary directory outside the repository (key = the whole request incl. the document bytes, TTL 3600 s, an ERROR never cached); 6 workers instead of 2; the extra-key probe is now an UNKNOWN key (actions and prefix are known keys); the scratch module copy no longer writes the proposed HCL (it is the module now)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 3 criterion CT4d2-AC2 and AMENDMENT 4's rule that every invocation finish under timeout 120.",
  "world_is": "The simulator shim runs about 3 s a call; the old script made ~38 calls with 2 workers. The script's meaning is kept (rows, readers, can_carry_today as measured) and its three-reader count now reads 1 ignored, 2 refused."
}
```

## NFRA_CTLPLN-W6-S8 -- AMENDMENT 4: lib/tests/test_opal_naming.py reads 6 failed / 87 passed on the pinned base, not the 2 / 91 its docstring states

```json
{
  "id": "NFRA_CTLPLN-W6-S8",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T13:34:29Z",
  "one_line": "Before any edit of lib/opal_naming.py (the base file written over the worktree copy, then restored) pytest on test_opal_naming.py gives 6 failed, 87 passed; after the edit the same 6 ids fail and 87 pass.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "pytest -q lib/tests/test_opal_naming.py with the file at 06c783b92b: 6 failed, 87 passed; failing ids: test_grade_agrees_with_every_worked_case for inf-silver-chain|LAMBDA, Inflection-SilverChain-DimConversionFailure|CW_ALARM, inf/otp-relay/token|SECRET, opal-portal-data-proxy-api|API_GW, wsb-49f-model-aua-pull-daily|SCHEDULE; and test_lambda_plane_consumers_is_import_aware_not_a_bare_substring (8 == 7)",
      "the same pytest after the edit: the identical six ids, 6 failed, 87 passed; run as a script (python lib/tests/test_opal_naming.py) the file prints nothing and exits 0 both before and after"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "the test file's docstring: the baseline is 2 failed / 91 passed.",
  "world_is": "The baseline has moved since the docstring was written; the identical failing set before and after is the control, so this build changes none. Not adjudicated here."
}
```

## NFRA_CTLPLN-W6-S9 -- AMENDMENT 4: the module also refuses a half-scoped or malformed scoped row, which the order did not name

```json
{
  "id": "NFRA_CTLPLN-W6-S9",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T13:34:29Z",
  "one_line": "The order asked the module to refuse an unknown key; main.tf also refuses a row with only one of actions/prefix, an action outside the closed set, a prefix not ending in /, and a wildcard or non-ARN principal on a scoped row, because the module renders from rows the validator may not have graded.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "check_fence_scoped_rows.py: module plan in a scratch root refuses cases 1,2,3,4,6 (unknown key, actions without prefix, prefix without /, PutObject in actions, wildcard ARN); cases 5 (other firm's prefix) and 7 (duplicate principal) are validator-only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 4 item 1: the module must refuse a key outside the closed set.",
  "world_is": "Without the extra rules, a row with actions but no prefix would pass the module's key check and render as a full admission. Each extra rule is one more precondition on the same two outputs; fence_exemption_arns' value is unchanged for today's rows."
}
```

## NFRA_CTLPLN-W6-S10 -- AMENDMENT 4: CT4d2-AC3's expect carries an unescaped + that the checker reads as a quantifier

```json
{
  "id": "NFRA_CTLPLN-W6-S10",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T13:44:38Z",
  "one_line": "CT4d2-AC3's <expect> unknown_key_refused_by=validator+module is read by the proof checker as a regex, where + is a quantifier, so the criterion's own correct output line can never match it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -c re.search('unknown_key_refused_by=validator+module', <the check's last line>, re.S) returns None; re.search(r'unknown_key_refused_by=validator\\+module', same line, re.S) matches (the last line reads unknown_key_refused_by=validator+module)",
      "python .tools/proof-of-spec-check.py on the instance with AC3 status PASS: VIOLATION acceptance[CT4d2-AC3]: status=PASS but output_evidence does NOT match expect 'unknown_key_refused_by=validator+module' -- INVALID",
      "the order's own last-line format names the token validator+module as one of four values (validator+module|validator|module|none), so the output cannot be changed to satisfy the pattern"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 4 CT4d2-AC3: <expect>unknown_key_refused_by=validator+module</expect>, graded by the checker as a regex match on the output.",
  "world_is": "The expectation is a literal string that contains a regex metacharacter. The criterion is met by its words (the line reads validator+module with ok=True and unchanged_today=True), but a mechanical PASS row cannot be written. The worker did not amend the expectation (the issuer's to amend, with the gate limb stated); the proof row records AC3 as UNVERIFIABLE-BY-INSTRUMENT with the verbatim line, and the order stays in_progress.",
  "notes": "Remedy for the issuer: <expect>unknown_key_refused_by=validator\\+module</expect>; the same pattern in any other criterion that quotes a '+' or other metacharacter verbatim."
}
```

## NFRA_CTLPLN-S19 -- the directives check knows two boxes; a directive placed on a Dell prints as unruled

```json
{
  "id": "NFRA_CTLPLN-S19",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T16:10:12Z",
  "one_line": "The directives check knows two boxes: a directive placed on a Dell prints as unruled, so the first Dell placement (D7 on dell2) reads as having no placement.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/directives-check.py device_of(): `for d in (\"LAPTOP\", \"SITEZ\")` then `return \"UNRULED\"` (read by this seat)",
      "Issuer's run of `python .tools/directives-check.py` at 2026-10-07 ~16:1xZ: `8. D7  Opal Ticketing` / `Where:   UNRULED`",
      "org/missions/DIRECTIVES.yaml D7 placement set to DELL2 @98fcdce272 (1.0.0_SA_CTO); asked as a row in 1.0.0_SA_CTO msg 106361",
      "Unread: the full population of tools that parse a placement"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD NFRA_CTLPLN FWD-2 / C-REGISTRY: a box is named once, in org/devices/DEVICES.json, and every script that names devices reads that file.",
  "world_is": "At least one placement parser carries its own two-box list. A cell for the next issuance: every tool that parses a directive's placement reads the device register, found by a sweep of the repository for placement parsers with its denominator printed, not by this one named function."
}
```

## NFRA_CTLPLN-W13-S16 -- two installed RECORDs (PyMuPDF, ruff) list every file twice, once with backslash separators and a hash and onc

```json
{
  "id": "NFRA_CTLPLN-W13-S16",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T16:00:28Z",
  "one_line": "two installed RECORDs (PyMuPDF, ruff) list every file twice, once with backslash separators and a hash and once with forward slashes and NO hash, and ruff lists its own binary at its wheel path, so a plain RECORD read marks them missing or unverifiable",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PyMuPDF 1.27.1 installed RECORD (<site-packages:3.12>/pymupdf-1.27.1.dist-info/RECORD): 109 forward-slash lines with an empty hash and 109 backslash-separator lines carrying sha256 and size for the same files, including pymupdf/_mupdf.pyd; ruff 0.15.11: 7 empty-hash lines and 8 backslash-separator lines, plus the line 'ruff-0.15.11.data/scripts/ruff.exe' (written with backslash separators, hashed, 32283648 bytes) and '../../Scripts/ruff.exe' (no hash); ruff has no entry_points.txt, so its Scripts/ruff.exe is the tool's own binary and NOT a generated launcher",
      "org/devices/kit_python_repack.py plan_package: reads RECORD with backslashes normalised to '/', merges duplicate paths with the hashed line winning, reads a '<name>-<version>.data/scripts/<f>' line whose file is not under site-packages as '../../Scripts/<f>' (the plan notes list it), and packs ruff.exe under ruff-0.15.11.data/scripts/; with this, 0 of the 49 packages carry an unverified (empty-hash) file and ruff is built (before the merge the first cut read ruff as MODIFIED: 'ruff-0.15.11.data/scripts/ruff.exe listed in RECORD, missing on disk')",
      "org/devices/test_kit_python_repack.py case 8 builds a synthetic distribution with exactly this duplicated shape and asserts one packed file with the hash verified"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 7: RECORD paths are relative to site-packages with forward slashes; a file listed with an empty hash is not a mismatch only for RECORD itself and sometimes INSTALLER; a file listed in RECORD but missing on disk is MODIFIED.",
  "world_is": "Two of the 49 installed RECORDs hold duplicate and partly unhashed lines (the installer that wrote them recorded both the wheel's layout and the installed layout). Read literally, the order's rule would have marked ruff MODIFIED and left it out, and would have counted PyMuPDF's compiled files as unverifiable. The worker merged the duplicates (the hashed line wins) so every byte is still compared with a hash RECORD states; this is a choice the order did not state."
}
```

## NFRA_CTLPLN-W13-S17 -- pip rewrote the first line of four installed scripts (awscli aws and aws_completer, pdfminer.six dumppdf.py an

```json
{
  "id": "NFRA_CTLPLN-W13-S17",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~13",
  "surfaced_at": "2026-10-07T16:00:28Z",
  "one_line": "pip rewrote the first line of four installed scripts (awscli aws and aws_completer, pdfminer.six dumppdf.py and pdf2txt.py) to this machine's python.exe path, so the kit carries them with the line put back to '#!python' and their bytes differ from the installed ones by that line",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Scripts/aws and Scripts/dumppdf.py first line on disk: '#!' plus the absolute path of this machine's Python312 python.exe, followed by CRLF; the RECORD hashes match those rewritten bytes (pip hashes after the rewrite), so the byte comparison passes while the shebang is still the laptop's path",
      "org/devices/kit_python_repack.py restore_shebang puts '#!python' back (pip rewrites a first line that starts '#!python' at install, with the Dell's interpreter) and lists each restored path in MANIFEST.json shebangs_restored: awscli 2, pdfminer.six 2; the wheel's RECORD carries the hash of the restored bytes",
      "org/devices/test_kit_python_repack.py case 8 asserts the restored bytes"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 7: a file outside site-packages, such as a script in Scripts/, is placed under <name>-<version>.data/scripts/; every file is compared with the hash its RECORD states before packing; a kit must not carry bytes no index ever published.",
  "world_is": "Copying the installed script byte for byte would carry the laptop's interpreter path into the Dell's Scripts folder, where it names a python.exe that does not exist. Restoring the line makes the packed bytes differ from the installed bytes (and from the installed RECORD hash) for these four files, while matching what the package's own wheel carries; the worker chose restoration, said so here, and the order did not say it."
}
```

## NFRA_CTLPLN-S20 -- dell1's Python 3.14 holds pyarrow, pyiceberg and hdbscan at versions off the pins; their likely source is an index install at bring-up, a fifth fetch if so

```json
{
  "id": "NFRA_CTLPLN-S20",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T17:19:29Z",
  "one_line": "dell1 imports pyarrow 25.0.1, pyiceberg 0.12.0 and hdbscan on Python 3.14.7; the pins are 18.1.0, 0.9.1 and 0.8.41 and no kit delivered them, so they reached the box some other way, likely a requirements install from the public index this morning.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_1700Z.md block 1, bus da723c41, from 1.0.0_SA_CTO~DELL1 at 16:57Z: the three imports succeed at those versions; kuzu absent; 'the source is unread (box image or an earlier install)'",
      "Same block, added by dell1's fabric manager: dell1's bring-up session installed the repository requirements on Python 3.14 this morning (its handoff records 'all 83 requirements.txt packages, pip check clean'), before the download tiers were stated",
      "1.0.0_SA_CTO msg 106445: the off-pin copies are not used; those cells run on the laptop by relay; nothing is uninstalled today; this row asked",
      "Not read by this seat: dell1's interpreter, its pip log or cache, or the handoff the manager cites. HOW and WHEN are therefore the manager's inference, not a measurement"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD NFRA_CTLPLN v0.16 C-INTAKE and Andrew's download-tier word: a package reaches a box by the checked route (the laptop checks it, then Taildrop); a box fetches nothing itself. Today's earlier counted fetches: two bun auto-installs on dell2, the provisioning install on dell1, the laptop's frozen-lockfile install.",
  "world_is": "If the manager's inference holds, dell1 made an index install of the whole requirements file at bring-up: a fifth fetch, larger than the other four, made before the tiers were stated. It also explains the off-pin versions: on Python 3.14 the pinned versions have no build, so a resolver that was not held to the pins took newer ones. Open, for dell1 to measure and report: the install's time and command (pip's own log or the cache's file times), what it fetched (count and names), and whether the same was done on dell2 (dell2 reported no PyMuPDF this morning, which argues against). No uninstall is ordered; the copies are simply not imported by project work."
}
```

## NFRA_CTLPLN-S21 -- the Python kit on dell2: 49 of 49 wheels verified and installed offline; 3 imports fail on dependencies the kit does not carry, and the tool mislabelled them

```json
{
  "id": "NFRA_CTLPLN-S21",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T17:19:29Z",
  "one_line": "The 49-wheel kit installs on Python 3.14 with no index; 46 of 49 packages import, and the three that do not each lack a dependency the requirements file never listed. The kit's tool reported them as failed where its own design calls them a missing dependency.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_1700Z.md block 2, bus a7670095, from 0.0.0_AB_MSTR~DELL2 at 16:57Z, Python 3.14.7: tar sha256 matches; PY-KIT-VERIFY wheels=49 verified=49 stray=0 ok=True; PY-KIT-INSTALL installed=49 imported=46 import_missing_dep=0 failed=3 ok=True",
      "The three, as dell2 names them: pandas_market_calendars (needs exchange_calendars), yfinance (needs frozendict), s3fs (needs aiobotocore). Real install then made offline with --no-index --no-deps --user, rc 0; nothing fetched",
      "org/devices/kit_python_repack.py (merged @f0d4d48d4e): the worker's report says 'A package whose own module is missing is counted as failed, not as import_missing_dep'; dell2 reads the three as mislabelled. Which branch of the tool took them is not read by this seat",
      "Row NFRA_CTLPLN-S18: requirements.txt omits 73 dependencies; 1.0.0_SA_CTO msg 106445: 'That is C-INTAKE clause 2's closure gap, measured: close the list before round 5 fetches.'",
      "First install of this kit on any Python 3.14: the eight compiled packages' stable-ABI claim held for import on dell2 (46 imported; which 46 is in dell2's result file, unread here). dell1's result is not reported"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CT-k-2 AMENDMENT 7: an import that fails for an absent dependency is reported as import_missing_dep with the module's name, distinct from a wheel that will not install; C-INTAKE clause 2: a list is closed under dependencies before anything is fetched.",
  "world_is": "The kit is proven to install on 3.14 and is live on dell2. Two things follow for round 5. (1) Its first cell is the closure: the full dependency set of the 67 requirements for Python 3.14 on 64-bit Windows, computed from metadata with no index call where the laptop holds the metadata, the remainder named as unknown until fetched; the three names here are its first measured members. (2) The tool's label is repaired in that cell so a missing dependency of a dependency (the import error names a module that is not the package's own) reads import_missing_dep."
}
```

## NFRA_CTLPLN-W14-S6 -- TO-CT-a-1 amendment 3: the policy simulator reads the key policy's account-root principal as a direct grant, so two admin arms read allowed in the raw run

```json
{
  "id": "NFRA_CTLPLN-W14-S6",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T17:07:15Z",
  "one_line": "iam simulate-custom-policy reads the account-root principal of a KMS key policy as a direct grant to every account user, so kms:ScheduleKeyDeletion and kms:PutKeyPolicy read allowed for a Dell user on the transcripts key policy before AND after this change; KMS itself treats the root statement as delegation to IAM, and the Dell users' own live policies refuse both",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python infra/aws/terraform/transcripts/tests/check_transcripts_dell_decrypt.py, ARM lines: for both cloudops-dell1-agent-user and cloudops-dell2-agent-user, kms:ScheduleKeyDeletion and kms:PutKeyPolicy read raw_doc=allowed AND raw_pre_edit_doc=allowed (identical on the document without this change); with the root statement removed (named_statements_only) both read implicitDeny; the rule the script counts is the KMS rule (a statement naming the user, or a root statement naming the action AND the user's own policy allowing it): own_policies kms:ScheduleKeyDeletion implicitDeny, kms:PutKeyPolicy explicitDeny (cloudops-dell-agent-respol-policy), so the counted result is dell_write_refused=10/10 while the raw simulator reads 6/10",
      "the simulator also refuses a bare Resource \"*\" in a resource policy (ResourceNames are not in a valid ARN format), so the script passes the document with each \"*\" replaced by the key ARN for the simulator call only; the rendered and committed document keeps \"*\"",
      "the same two raw 'allowed' arms exist today for any account user the root statement of RootAdministersTheKeyAndCannotUseIt names by principal; the amendment's expectation (each write arm implicitDeny or explicitDeny) is therefore met under the KMS rule and not under the raw simulator, and the proof row says which"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-a-1 amendment 3 step 3: each Dell user kms:Encrypt, kms:GenerateDataKey, kms:ReEncryptFrom, kms:ScheduleKeyDeletion, kms:PutKeyPolicy -> NOT allowed, by iam simulate-custom-policy with the rendered document as the resource policy.",
  "world_is": "The raw simulator answers allowed for two of the five arms on the document with and without the added statement; the added statement is not their cause. The worker kept the raw column printed beside the KMS-rule column and counted the KMS rule, and did not edit the key policy's root statement (outside the amendment). A future reader of a KMS key policy with a simulator needs the same composition."
}
```

## NFRA_CTLPLN-W8-S6 -- receipt imports entries carry two keys beyond THE SEAM

```json
{
  "id": "NFRA_CTLPLN-W8-S6",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~8",
  "surfaced_at": "2026-10-07T18:52:54Z",
  "one_line": "THE SEAM's receipt record has no per-import class, but install must tell import_missing_dep from a real import failure, so intake_receive.py adds two keys to each imports entry.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/intake/intake_receive.py run_import writes class (imported | import_missing_dep | failed) and, for a missing dependency, missing_dep into each imports entry; receipt_gate reads class",
      "task order NFRA_CTLPLN.TO-CT-e-4 THE SEAM RECEIPT line lists imports entries as module, rc, first_error_line only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "THE SEAM: RECEIPT imports per top-level module carry module, rc, first_error_line; install is refused unless each receipt reads installed_imported or installed_import_failed with only import_missing_dep causes.",
  "world_is": "A cause cannot be read back reliably from first_error_line alone (the package's own module names are not in the receipt), so the receipt carries the tool's classification in two additional keys; any reader that rejects unknown keys in an imports entry must be aligned, and a reader that ignores them loses nothing. Also resolved without a row: a pack-level defect (manifest, stray, non-wheel file) refuses every wheel while a wheel-level defect refuses only that wheel; INTAKE-PROVE failed= counts install failures only."
}
```

## NFRA_CTLPLN-W6-S11 -- TO-CT-e-3: the platform scanner on this laptop exits 2 with 'Product/Feature disabled', which the order reads as 'a threat was found'

```json
{
  "id": "NFRA_CTLPLN-W6-S11",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T18:54:42Z",
  "one_line": "MpCmdRun.exe -Scan -ScanType 3 -File <own synthetic wheel> -DisableRemediation exits 2 on this laptop with '[Failed][0x80004005] Unspecified error' because Defender's antivirus is disabled; exit 2 is not a threat verdict here, so check 7 reads failed on this box whatever the file holds.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "intake_check.py check_7 on a tiny synthetic wheel the test built: exit_code=2, last_lines ['[Failed][0x80004005] Unspecified error', 'CmdTool: Failed with hr = 0x80004005. Check ...MpCmdRun.log for more information']; the scanner's own log line before it reads 'WARN: Product/Feature disabled'.",
      "powershell Get-MpComputerStatus: AMServiceEnabled False, AntivirusEnabled False, RealTimeProtectionEnabled False; SecurityCenter2 lists 'Windows Defender' (productState 393472) and 'Little Dog Tech Managed Antivirus Antimalware' (266240)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-e-3 BUILD 1 check 7: exit code 0 means no threat found, 2 means a threat was found; anything else, or the scanner absent or refusing, is failed.",
  "world_is": "Exit 2 also means the scanner refused to scan (Defender's antivirus off, a managed third-party product active). The tool records failed either way and says in the summary when the output shows an error, so no pass is possible; but while Defender is off, check 7 cannot pass on this laptop and no file can reach 'checked' here. The real-scanner test case is counted skipped for that reason.",
  "notes": "For the issuer: either the CTO's signed batch accepts a failed check 7 is never 'checked' (the seam says so), or check 7 needs the managed product's own scanner named in a later round."
}
```

## NFRA_CTLPLN-W6-S12 -- TO-CT-e-3: THE SEAM leaves four format points open that the tool resolved one way; the fetch, receive and closure tools should read the same way

```json
{
  "id": "NFRA_CTLPLN-W6-S12",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~6",
  "surfaced_at": "2026-10-07T18:54:42Z",
  "one_line": "THE SEAM does not fix (a) whether OPAL_INTAKE_RECORDS is the base of <base>/<batch>/ or the batch folder itself, (b) whether held_path starts with holding/, (c) whether attestation is a string or an object, (d) the shape of a check's evidence; intake_check.py resolves each tolerantly or by a stated rule.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "intake_check.py Cfg/records_dir: records at <OPAL_INTAKE_RECORDS>/<batch>/<file>.check.json; the FETCH record is read from there, else from <OPAL_INTAKE_RECORDS>/ directly.",
      "held_path_ok: accepts holding/<batch>/<file> and <batch>/<file>; the file is read at <root>/holding/<batch>/<file> either way.",
      "check_5: attestation may be the string 'present'|'absent'|'unread' (URL read from top-level attestation_url) or an object with state/status/value and url.",
      "each check's evidence is an object with a 'summary' string plus detail keys; a not_applicable check carries evidence.reason; check 8 carries evidence.signer and evidence.path; MANIFEST.json lists files[] with name, sha256, size, check_record(+_sha256), delivery(+_sha256)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "THE SEAM: record formats fixed so four cells share files and never wait on each other's code.",
  "world_is": "The listed fields are underdetermined by the seam text; the check tool is tolerant on read where it can be and states its write format. The receive tool reading evidence as a plain string, or the fetch tool writing OPAL_INTAKE_RECORDS as the batch folder, would be the mismatch to look for at the drain."
}
```

## NFRA_CTLPLN-W14-S7 -- TO-CT-a-1 amendment 5: placement IS recorded (as a target) in project.json, DIRECTIVES.yaml and the CTO four-box record; the order said no register lists it

```json
{
  "id": "NFRA_CTLPLN-W14-S7",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T21:09:58Z",
  "one_line": "The order says no register places a project on a Dell, but 13 tree project.json files carry a placement field of DELL1 or DELL2, the directive register places D7 (OPAL_TICKET_VNEXT) on DELL2, and the CTO four-box record places ADVI_PERFRP on DELL2; the field is the TARGET box, so a live project may still be running elsewhere until its round boundary",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_vendor_secrets.py --from-file infra/aws/terraform/nfra-ctlpln-identity/tests/vendor_secrets_census.json prints one PLACED line per project with file:line: 13 org/missions/D*/*/*/project.json placement lines (DELL1: MDPF_HEALGAP, MDPF_SECCLASS, MDPF_SECHIST, MDPF_TAXSMA; DELL2: ADVI_BILLING, ADVI_COTBKF, DSGN_IRPTV1, IRPT_BCKEND, IRPT_CUSTDY, IRPT_DASHBD, IRPT_YCDGEN, NFRA_OPSWKF, NFRA_TRNSPT)",
      "org/missions/DIRECTIVES.yaml:325 (D7 placement DELL2) and the members line naming OPAL_TICKET_VNEXT; org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20261007_FOUR_BOX_LAYOUT_ANDREW_APPROVED.md:18 (ADVI_PERFRP, DELL2, no tree home)",
      "the CTO record says a live project moves at its next round boundary and the project.json placement_ruling for ADVI_COTBKF says 'TARGET BOX dell2 ... Replaces the dell1 target of the four-box layout': the field is a target and two registers disagree on ADVI_COTBKF (layout table DELL1, project.json DELL2); org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261007_071xZ_DELL2_SEATING_CTO_SELF_DRIVE_COO_CANONICAL_DRIVE_MSTR_ARMS.md lines 46-50 quote seats ~K2 ~C2 ~P2 ~Y2 ~M2 ~G2 ~D2 on dell2 for IRPT_CUSTDY, ADVI_COTBKF, IRPT_BCKEND, IRPT_YCDGEN, IRPT_DASHBD"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-a-1 amendment 5 step 1(c): 'NO register lists this (the directive register names DELL2 for D7 only; project rows carry laptop or site-z)'; infer placement from lane suffixes where the relay files confirm the convention.",
  "world_is": "Project rows carry DELL1/DELL2 in a placement field (13 tree rows) and the census uses those lines, not the lane-suffix convention: org/devices/DEVICES.json lists no lane letters for dell1 or dell2 (lane_letters_claim absent), so the convention is read only from the relay files and places no project. placement_inferred=False for all 15 placed projects; the placed list is a TARGET list.",
  "notes": "For the issuer: the join is only as current as the target; a project that has not yet moved still runs elsewhere, and a project moved later is missed until the census is retaken (--live)."
}
```

## NFRA_CTLPLN-W14-S8 -- TO-CT-a-1 amendment 5: the whitelist scopes OpenAI to ETFS_RIVALS only, and the census finds MDPF_SECCLASS programs reading the OpenAI key

```json
{
  "id": "NFRA_CTLPLN-W14-S8",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T21:09:58Z",
  "one_line": "The standing vendor-egress whitelist scopes OpenAI to ETFS_RIVALS only ('not any other project's use of OpenAI'), while the vendor census finds four MDPF_SECCLASS programs on dell1 reading openai-api-key; the Dell grant lets a Dell read the key and says nothing of whether a call is allowed, which the whitelist older wording would refuse for that project",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/ref/VENDOR_EGRESS_WHITELIST.yaml VEW-2: vendor OpenAI, scope 'ETFS_RIVALS -- the rivalfunds AI chain only', not_covered 'OpenAI for any project other than ETFS_RIVALS'; VEW-3 Kimi scope 'any'",
      "tests/vendor_secrets_census.json join: MDPF_SECCLASS reads openai-api-key in data/black_diamond/scripts/classification/classify_bd_securities.py:159, data/black_diamond/scripts/gold/B_01b.classify_new_securities.py:283, data/cot/scripts/gold/B_01b.classify_new_securities.py:284, data/inf/scripts/classification/classify_assets.py:290",
      "Andrew 18:3xZ item 4 ('The Dell Boxes have vendor egress as needed', org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_183xZ_TWELVE_ITEMS_ANSWERED_INSTALLER_PUSH_VENDOR_EGRESS_STORE_OUTLOOK_LAW_LINE_D2_HOLD_LIFTED.md) is newer than the register row and broader; the register row was not struck or widened by it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-a-1 amendment 5: grant the Dell group read of exactly the vendor secrets its placed projects need; whether a given vendor call is one Andrew allowed stays the rule seats follow.",
  "world_is": "openai-api-key is classed VENDOR (an AI model provider key read by name by MDPF_SECCLASS programs) and is in the built grant; the register row that records Andrew's standing OpenAI word covers one project. No call is made by this cell; the half request carries the secret so a person can strike it or widen VEW-2.",
  "notes": "For 1.0.0_SA_CTO (the register's only writer): whether item 4 widens VEW-2 for the Dell-placed projects, or the key leaves the grant."
}
```

## NFRA_CTLPLN-W14-S9 -- TO-CT-a-1 amendment 5: CTa1-AC5 cannot read ok=True after the apply, because its ok includes 'live key policy equals the pre-edit render'

```json
{
  "id": "NFRA_CTLPLN-W14-S9",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_CTLPLN~14",
  "surfaced_at": "2026-10-07T21:26:53Z",
  "one_line": "CTa1-AC5 reads ok=False on the live account because its check requires the LIVE transcripts key policy to equal the PRE-edit render, and the amendment 3 change has since been applied: the live key policy now holds 3 statements, the pre-edit render 2; every other field of the line passes",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "timeout 120 python infra/aws/terraform/transcripts/tests/check_transcripts_dell_decrypt.py (rc 1) prints 'live key policy (kms get-key-policy) statements=3 equals the pre-edit render (one-element lists normalised as KMS stores them): False' and LAST line 'TRANSCRIPTS-DELL-DECRYPT dell_decrypt=2/2 dell_write_refused=10/10 reader_unchanged=True unlisted_refused=True statements_added=1 ok=False'",
      "the same script on the committed amendment 3 state read ok=True in the earlier pass (proof instance row CTa1-AC5, before the apply); the render still reads 'statements after=3 before(55ec1bd250)=2' and the diff added=['DellAgentUsersDecryptOnly']",
      "check_transcripts_dell_decrypt.py, the line after 'the live key policy equals the pre-edit render': live_same is part of ok, so a correct apply makes the check fail by construction; I did not compare the live statements' content to the after-render (kms get-key-policy is not in amendment 5's read list), so 'the live policy is the applied after-state' is inferred from the count 3"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CT-a-1 amendment 5: the other five criteria are unchanged and must still pass; CTa1-AC5 expects ok=True with statements_added=1.",
  "world_is": "The check's ok includes 'live key policy equals the pre-edit render', true only before the apply. After the apply the line reads ok=False although the expected substring dell_decrypt=2/2 and statements_added=1 hold. I did not edit the test (a change to how ok is formed is the issuer's to rule, as amendment 4 did for AC2); the order stays in_progress with AC5 recorded FAIL.",
  "notes": "For 2.0.0_SA_COO~C: amend CTa1-AC5 so the live comparison accepts the applied state (live equals the after-render) or drop it from ok, then re-run; no other criterion is affected."
}
```
