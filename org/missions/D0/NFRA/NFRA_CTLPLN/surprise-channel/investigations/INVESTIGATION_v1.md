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
