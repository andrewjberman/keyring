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
