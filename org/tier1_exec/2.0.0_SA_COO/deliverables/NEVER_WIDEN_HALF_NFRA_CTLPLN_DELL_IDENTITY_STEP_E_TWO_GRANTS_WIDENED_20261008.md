# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP E (cell 2) -- the two grants widened

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~17:3xZ. **Read at:** branch `wk-NFRA_CTLPLN-16` @df84da40fa (order AMENDMENTS 16
and 17; build @fec6a71bbd). Root `infra/aws/terraform/nfra-ctlpln-identity/`. **Counterpart owed:** a CTO half.
**Authority:** Andrew-direct 2026-10-08 ~13:2xZ, "3.( WIDEN THE TWO GRANTS, YES", answering "the 28 platform keys, the audit
trail and its bucket, the portal's protected functions and the four cross-box queues" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_132xZ_TEN_ANSWERS_LIFT_ITEMS_5_AND_4_WIDEN_BOTH_GRANTS_DELL2_RETRIES_DELL1_INSTALLS.md`
row 3; this seat read the record and did not hear the word); `1.0.0_SA_CTO` msg 106945 cell (2); msg 106987 (this cell first);
`org/tier1_exec/1.0.0_SA_CTO/deliverables/FAST_FIX_RULINGS_20261008_162xZ.md` graph F1 (the graph read token ships here).

## Where the root stands

| step | what | state |
|---|---|---|
| A, B, C | Denies; secrets read of 66; resource-policy Allow of 70 | APPLIED 09:19:39Z, 11:33:48Z, step C (TO-APPLY-13) |
| **E (this half)** | the two grants widened (cell 2) | this pair |
| D | the routes Deny off (cell 1, AMENDMENT 15) | parked on `wk-NFRA_CTLPLN-14` until E applies (CTO 106987) |
| F | IAM create/change on the Dell group (cell 3) | not cut |

## The issuer's reading of "the two grants" (the CTO half confirms or widens it)

The SECRETS read grant and the RESOURCE-POLICY Allow. What comes in is what those two grants held out on the four named things.
Kept refused, because they are not a grant's hold-out: stopping, updating or deleting the audit trail; the seven non-policy
writes on the audit-trail bucket (lifecycle, logging, notification, encryption, versioning, ownership controls, public-access
block); the ten DEPLOY actions on the protected functions; every IAM write; the routes Deny. If the CTO reads "the audit trail
and its bucket" as the whole of both Denies, the bucket's seven are one statement (`DenyAuditTrailBucketWrites`) and the
trail's are one statement (`DenyCloudTrailWrites`): a one-statement removal each, a separate small pair.

## The plan, MEASURED

Laptop, 2026-10-08 ~17:2xZ, by this seat, read-only, untargeted, default variables, `-lock=false`, branch tree @df84da40fa,
exit 2: **`Plan: 2 to add, 3 to change, 0 to destroy.`** 67 added lines, 32 removed.

- `aws_iam_policy.dell_agent_platform_secrets[0]` CREATED (`cloudops-dell-agent-platform-secrets-policy`): one statement,
  `secretsmanager:GetSecretValue` only, on exactly 28 secret ARNs (counted in the plan: 28), `opal/mcp/graph-read-token` among
  them.
- `aws_iam_group_policy_attachment.dell_agent_platform_secrets[0]` CREATED: on the Dell agent group (7 of 10 managed policies).
- `aws_iam_policy.dell_agent_deploy` CHANGED in place: `DenyCloudTrailWrites` loses `cloudtrail:Put*` and `cloudtrail:Delete*`
  and gains seven explicit actions (`DeleteChannel`, `DeleteDashboard`, `DeleteEventDataStore`, `DeleteTrail`,
  `PutEventConfiguration`, `PutEventSelectors`, `PutInsightSelectors`); `Stop*` and `Update*` stay. `DenyProtectedFunctions`
  loses `lambda:AddPermission`, `RemovePermission`, `AddLayerVersionPermission`, `RemoveLayerVersionPermission` (added by
  @c777e72cbd); its ten deploy actions and twenty resources stay.
- `aws_iam_policy.dell_agent_create` CHANGED in place: 26 removed lines, none added -- the fourteen resource-policy actions leave
  the audit-bucket Deny (the statement keeps the seven and is renamed `DenyAuditTrailBucketWrites`); `DenyAgentbusQueuePolicy`
  (three `sqs:` actions on the four queues) is removed.
- `aws_iam_policy.dell_agent_respol_allow[0]` CHANGED in place: gains `cloudtrail:PutResourcePolicy` and
  `cloudtrail:DeleteResourcePolicy` (70 -> 72 actions).
- `aws_iam_policy.dell_agent_vendor_secrets[0]` (the 66): NO CHANGE (byte-identical; the split keeps it as part one).

Greps of the plan's ADDED lines: `"iam:` 0; `secretsmanager:PutResourcePolicy` / `DeleteResourcePolicy` 0.

**Writers of the property: N = 1**, this root; read. Simulation at the same tree (this seat's run, 17:2xZ):
`POLICY-SIM allowed_ok=22/22 denied_ok=15/15 passrole_ok=5/5 protected_ok=8/8 freed_allowed=72/72 freed_excluded=3 undo_freed=167/167 undo_still_denied=443 selfsim_ok=9/9 ssm_ok=15/15 routes_ok=5/5 vendor_ok=245/245 all_ok=True`.
Static: `names_from_builder=13/13 policy_size_ok=True ok=True`. Census: `granted=94 platform_key=28 other=19 blocked_by_key=1 ok=True`.

## Blast radius

Two principals, `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user`, and so every agent seat on those two boxes.

**What they gain.**
1. **Read the 28 platform keys** (names and one sentence each: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~14/PLAN_NOTE_DELL_VENDOR_SECRETS.md`
   sections E and G). In plain terms a Dell can then act AS the platform: sign the portal's login tokens (`opal/auth/jwt-private-key`
   and its like), use the admin seed, call the firm's own gateway and graph with its bearer tokens, read the Schwab anonymization
   key. Andrew's "One consequence" section of the record states this plainly; no ceiling is added.
2. **Change the audit trail's resource policy** (`cloudtrail:PutResourcePolicy`, `DeleteResourcePolicy`).
3. **Change the audit-trail bucket's policy and ACLs** (the fourteen actions): a Dell could open or close who reads the logs.
4. **Change who may invoke the ten protected functions** (the portal's authorizers and auth handlers): a Dell could let another
   principal invoke them.
5. **Change the four agentbus queues' policies and attributes**: receive-only-own-queue then holds by the per-user receive
   policies only, not against a queue-policy change by a Dell.

**What still refuses after this step** (each simulated, explicitDeny, statement named): CloudTrail Stop/Update/Delete-trail and
selector writes (`DenyCloudTrailWrites`, 28 arms); the audit bucket's seven settings (`DenyAuditTrailBucketWrites`, 14 arms); the
protected functions' ten deploy actions (`DenyProtectedFunctions`, 400 arms); every IAM write (`DenyEveryIamWrite`); PassRole
except named; API key reads; production-data deletes; table deletes; the routes Deny. Not granted: the 19 OTHER secrets and
`schwab/sdd/session` (its own key); `secretsmanager:PutResourcePolicy` stays out of the Allow.

**Known open route, reported not closed (row W14-S19, AMENDMENT 17):** since step C both Dells may `kms:PutKeyPolicy` on the
transcripts key (accepted then, CTO 106733); this step does not change it.

**Not examined:** organization-level policies; the resource policies already on the resources above; Dell jobs in flight.

## Expected outcome, BOTH branches

- **A:** immediately before the apply, the plan on the merged trunk reads exactly `2 to add, 3 to change, 0 to destroy`, those
  five addresses and no other; the added lines carry 28 secret ARNs, zero `"iam:`, zero `secretsmanager:*ResourcePolicy`; the
  vendor-secrets policy shows no change -> apply.
- **B:** any other count, address or grep result (in particular any destroy, or any change to `dell_agent_vendor_secrets[0]` or
  to a routes resource) -> apply NOTHING and report.

## Rollback per key

Every change is to a policy document this root owns: re-apply the root at the parent of the merge commit (trunk before this
cell) and the four documents return byte-for-byte and the new policy and attachment are destroyed; or, by hand, detach and
delete `cloudops-dell-agent-platform-secrets-policy` and set the three changed policies' default version back to the prior
version (IAM keeps it; the applier records each prior version id before applying). A secret a Dell READ in the interval cannot
be un-read: if rollback is for exposure, the keys read must be rotated, and the audit trail names which were read.

## Conditions

1. Plan shape of branch A on the merged trunk, classified immediately before the apply, the greps recorded.
2. Immediately before the plan: the simulation line above reads `all_ok=True` with the same counts.
3. Each changed policy's current default version id recorded before; the group's attached-policy list saved; one NEVER-2 ledger
   entry opened and closed.
4. Read-back LIVE with `simulate-principal-policy` on each Dell user, matched statement named. ALLOWED:
   `secretsmanager:GetSecretValue` on `opal/mcp/graph-read-token`; `cloudtrail:PutResourcePolicy`; `s3:PutBucketPolicy` on the
   audit bucket; `lambda:AddPermission` on one protected function; `sqs:SetQueueAttributes` on one agentbus queue. REFUSED:
   `cloudtrail:StopLogging`; `s3:PutLifecycleConfiguration` on the audit bucket; `lambda:UpdateFunctionCode` on one protected
   function; `secretsmanager:GetSecretValue` on one OTHER secret and on `schwab/sdd/session`; `iam:CreateRole`. A re-plan reads
   no changes. THE APPLIER READS NO SECRET VALUE AND MAKES NO RESOURCE-POLICY CALL: read-back by simulation only.
5. Graph F1's proof is the Dells' own: one `comp-kuzu` query on dell1 and on dell2, reported to the laptop. Until then APPLIED,
   not EXERCISED.
6. Applied time to the CTO the minute the applier reports (CTO 106878).

**SIGNED** -- `2.0.0_SA_COO~C`
