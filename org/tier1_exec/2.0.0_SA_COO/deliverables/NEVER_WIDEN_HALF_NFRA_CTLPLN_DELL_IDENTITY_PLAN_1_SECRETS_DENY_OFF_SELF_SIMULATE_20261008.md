# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, PLAN 1 of 2 -- the secrets read, the resource-policy Deny off, self-simulate

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~05:0xZ. **Read at:** trunk @35f5f12418 (the merge of cell CT-a-1 AMENDMENT 9, worker commit
`943d8eee65`). Root `infra/aws/terraform/nfra-ctlpln-identity/`. **Counterpart owed:** a CTO half.
**Authority:** Andrew-direct 2026-10-08 ~00:4xZ, "lets start with lifting 1 2 3 6" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md`;
this seat read the record and did not hear the word); `1.0.0_SA_CTO` msgs 106669 (rulings 1 and 3), 106652 (the carve-out),
106731 (ruling 3: the counts accepted), 106743 (split the plan if the whole cannot be verified by 05:15Z).

**This supersedes** this seat's half `NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_VENDOR_SECRETS_20261007.md` (four vendor keys; never applied).
**It reverses, on Andrew's word, two things this seat signed and had applied on 2026-10-07:** the resource-policy Deny (order
TO-APPLY-6) and the queue-attribute Deny that rode in it (order TO-APPLY-7).

## What is NOT in this plan (plan 2, a second pair)

- **The Allow of the resource-policy actions** (CTO ruling 106731 item 1). A worker is building it now. Until it is applied, what
  Andrew lifted as "change who may reach a resource" is delivered for ONE action only (see "The Deny off" below).
- **dell2's SSM public parameter read** (`ssm:GetParameter` on
  `arn:aws:ssm:us-east-1::parameter/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64`, CTO msg 106743).
  The root holds NO `ssm:GetParameter` grant of any kind today (read: no hit in its policy documents), so this is new text and
  cannot be signed as verified in this hour. It is the first item of plan 2. **So this plan unblocks
  `blackdiamond/49f/session` and the Kimi key; it does NOT unblock dell2's release 1.**

## The act

One `safe-apply` of the whole root, untargeted, at the laptop.

## The plan, MEASURED

Laptop, 2026-10-08 ~04:5xZ, read-only, exit 2: `Plan: 2 to add, 1 to change, 2 to destroy.` 101 added lines, 104 removed.

| resource | change | what it is |
|---|---|---|
| `aws_iam_policy.dell_agent_vendor_secrets[0]` | created | one statement `ReadVendorCredentialsAndClientSessions`: `secretsmanager:GetSecretValue` on 66 exact secret ARNs (counted in the plan: 66), no wildcard |
| `aws_iam_group_policy_attachment.dell_agent_vendor_secrets[0]` | created | attaches it to the Dell agent group (both Dell users) |
| `aws_iam_policy.dell_agent_create` | updated in place | exactly ONE statement added, `SimulateOwnPolicyOnly`: `iam:SimulatePrincipalPolicy` on `user/${aws:username}`; no other line of that policy changes |
| `aws_iam_policy.dell_agent_respol` | destroyed | the Deny of 75 resource-policy actions (`DenyResourcePolicyWrites`) |
| `aws_iam_group_policy_attachment.dell_agent_respol` | destroyed | its attachment |

**Writers of the property: N = 1.** This root alone writes the Dell group's policies; read.

## Blast radius

Two principals: `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user`, through their one group. No other principal, no
resource policy, no key policy, no secret's value or policy is touched.

### 1. The secrets read -- 66 of 114 listed secrets

The listing is the saved census of 2026-10-07T21:00:45Z (names, descriptions, tags, key ids; no value was read by any seat or
worker). A secret created after that time is not in the grant.

**Client-firm and custodian sessions and logins (31).** A holder can sign in as the firm, or act as the signed-in user, at that
service: `aaii/credentials`, `astn/ft/credentials`, `astn/ft/session`, `blackdiamond/49f/credentials`,
`blackdiamond/49f/session`, `blackdiamond/cot/credentials`, `blackdiamond/cot/session`, `bloomberg/session`,
`bloomberg/terminal/login`, `conferenceboard/credentials`, `dowjones/barrons/session`, `dowjones/credentials`,
`dowjones/wsj/session`, `opal/bd/cottonwood/credentials`, `opal/bd/credentials`, `orion/credentials`,
`orion/eclipse_jwt/current`, `orion/jwt/current`, `schwab/sdd-credentials`, `seeking-alpha/credentials`,
`seeking-alpha/session`, `smartx/cookie/current`, `smartx/credentials/password`, `smartx/credentials/username`,
`smartx/credentials/yaliu-bundle`, `smartx/credentials/yang-shared`, `smartx/jwt/current`, `ycharts/credentials`,
`ycharts/login/credentials`, `ycharts/session/current`, `ycharts/session/research-20260911`.

**Vendor credentials (35).** A holder can call that vendor on the firm's account and bill: `FredApiKey`, `ai/claude-api-key`,
`anthropic-api-key`, `astn/brightdata/residential-proxy`, `astn/kimi/api-key`, `brightdata-api-key`,
`find-dualbiz/bright-data/serp`, `find-insure/bright-data/api-key`, `find-insure/bright-data/scraping-browser-creds`,
`find-insure/job-board/builtin/api-key`, `find-insure/job-board/efinancialcareers/api-key`,
`find-insure/job-board/glassdoor/api-key`, `find-insure/job-board/indeed/api-key`,
`find-insure/job-board/insurancejobs/api-key`, `find-insure/job-board/linkedin-jobs/api-key`,
`find-insure/job-board/wellfound/api-key`, `find-insure/job-board/ziprecruiter/api-key`, `find-insure/lusha-ai/api-key`,
`massive-api-key`, `msci-api-credentials`, `multi-threadv2`, `nopecha/api-key`, `ocilar/credentials`,
`opal/opalai/analyst-claude-oauth-token`, `opal/openai/andrew-fideles`, `opal/openai/aws-lambda-ki`,
`opal/openai/layer3-curation`, `opal/openai/market-update`, `opal/openai/news-trending`, `openai-api-key`, `price_discovery`,
`quo/api-key`, `rivalfunds/openai-api-key`, `seeking-alpha/bright-data-api-key`, `twilio/credentials`.

**Stated at full width.** Both Dell boxes, and so every agent seat on them, can then read: the Bloomberg terminal login and
session, the Schwab data-delivery credentials, both Black Diamond client logins and sessions, the Orion and SmartX sign-ins,
and every model-provider key the firm holds. A read of a credential is not a permission to call that vendor: CLAUDE.md's
per-use rule for vendor calls and the vendor list are unchanged by this plan, and no tool enforces them at the read.

**Judgment calls that went the granted way** (thin or no description; classed by name and by the code that reads them):
`opal/opalai/analyst-claude-oauth-token`, `smartx/credentials/yang-shared`, `bloomberg/terminal/login`, `FredApiKey`, the five
`opal/openai/*` keys. The CTO may strike any of them; the grant is built from the census data, so a strike is one field.

**Withheld: 28 platform keys** (a holder could act as Opal's own platform), each with what it would let a box do, in the
worker's plan note `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~14/PLAN_NOTE_DELL_VENDOR_SECRETS.md`.
Among them: `opal/auth/jwt-private-key`, `opal/auth/irpt-render-jwt-private-key`, `opalinvest/jwt-secret`,
`opalinvest/admin-seed`, `opal/auth/origin-verify`, the four gateway bearer tokens, the gateway's signing and encryption keys,
the two pseudonym keys, `schwab/anonymization-key`, `schwab/ec2-credentials`, and the two Black Diamond one-time-code gateway
tokens. **One consequence to know:** `blackdiamond/49f/otp-gateway-token` and `blackdiamond/cot/otp-gateway-token` are
withheld, so a Dell holding the Black Diamond LOGIN cannot complete a fresh multi-factor sign-in by itself; it can use the saved
SESSION (granted) while that session lives. If a Dell run needs a fresh sign-in, that token enters by the refused-run route.

**Withheld: 19 unplaced**, for a person to rule (configuration bundles with no description, two GitHub tokens, two Google
logins, two public keys, the two directory application credentials, two one-time-code relays, a placeholder, a recovery code,
and a phone number). Named with reasons in the plan note.

**Left out because of its key: 1.** `schwab/sdd/session`, a custodian session, sits under a customer-managed key; the grant
would not be enough to read it and no key policy is touched. It is a granted-class secret that this plan does NOT deliver.

**Already true before this plan, unchanged by it, and worth the signer's eye:** the Dell create policy allows
`secretsmanager:PutSecretValue` on any secret, so a Dell can already OVERWRITE a secret it cannot read, the 28 withheld ones
included. Narrowing that is a cell the CTO asked for; it is not in this plan.

**Headroom:** the document is 5,968 of 6,144 characters. One or two more secrets force a split into two policies (by class);
the group then holds 6 managed policies of a quota of 10.

### 2. The Deny off

Measured by simulation over the 75 former actions, per Dell user, once the Deny is gone: **1 allowed, 71 implicitly denied
(no Allow covers them), 3 explicitly denied by statements that stay** (`iam:UpdateAssumeRolePolicy`,
`cloudtrail:PutResourcePolicy`, `cloudtrail:DeleteResourcePolicy`). The one freed action is `sqs:SetQueueAttributes`, on any
queue: a Dell can then change a queue's policy, its redrive target and its other attributes. `s3:PutBucketPolicy`,
`kms:PutKeyPolicy` and `lambda:AddPermission` all still read refused after this plan. The routes Deny, the pass-role Deny, the
ten protected functions and the API-key reads read exactly as before (simulation lines identical to the previous run).

### 3. Self-simulate

Each Dell user may run `iam:SimulatePrincipalPolicy` on its own user only. Simulated, nine arms: each on itself allowed; each
on the other Dell's user refused; each on a role refused; the control without the statement refused.

## Expected outcome, BOTH branches

- **A:** the applier's plan reads exactly `2 to add, 1 to change, 2 to destroy`, the five resources of the table and no
  other; the created policy holds exactly 66 secret ARNs and one action; the in-place update adds exactly the one statement
  `SimulateOwnPolicyOnly` and removes nothing; none of the 28 withheld names appears anywhere in the plan (the applier greps
  the plan for `jwt-private-key`, `admin-seed`, `jwt-secret`, `origin-verify`, `gateway/`, `otp-gateway-token`,
  `opal/mcp/`, `pseudonym`, `anonymization-key`, `ec2-credentials`: zero hits) -> apply.
- **B:** any other count, a sixth resource, a secret ARN count other than 66, any removed line in the create policy, any
  withheld name in the plan, a wildcard in the new statement -> apply NOTHING and report the plan as read.

## Rollback per key

- The secrets policy and attachment: detach and delete (or revert the merge and apply). Per secret: strike it in the census
  data and apply. A value a Dell read in the interval stays read; rotation of that secret is the only undo, and is its owner's.
- The Deny: the removed policy document is at `git show c7c6d13b85:infra/aws/terraform/nfra-ctlpln-identity/dell_respol_policy.json`;
  restoring the file, its resource and attachment, and applying, puts it back. A queue attribute a Dell changed in the interval
  is not undone by that; the saved file `tests/read_queue_attribute_writers.py` reads who can.
- Self-simulate: remove the statement and apply. It is read-only.

## Conditions

1. The plan shape of branch A, classified immediately before the apply, with the zero-hit grep recorded.
2. Immediately before the plan: `python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py` reads
   `selfsim_ok=9/9 ssm_ok=9/9 routes_ok=5/5 vendor_ok=235/235 all_ok=True`, and the secrets census check reads
   `secrets=114 ... granted=66 ok=True blocked_by_key=1 platform_key=28 other=19`. The census check is run in its SAVED mode
   only; a live re-take is the issuer's act, not the applier's.
3. The live documents of the two policies that change or go (`cloudops-dell-agent-create-policy`,
   `cloudops-dell-agent-respol-policy`) and the group's attachment list are saved with SHA-256 before the apply; one NEVER-2
   ledger entry is opened and closed.
4. Read-back LIVE with `simulate-principal-policy` on each Dell user, each arm with its matched statement: `GetSecretValue`
   on `blackdiamond/49f/session`, `astn/kimi/api-key` and `openai-api-key` allowed; on `opal/auth/jwt-private-key`,
   `opalinvest/admin-seed`, `gateway/mail/bearer` and `blackdiamond/49f/otp-gateway-token` refused; `sqs:SetQueueAttributes`
   allowed; `s3:PutBucketPolicy` refused; a routes arm refused as before; self-simulate allowed on self and refused on the
   other user. The group's attachment list reads the expected five names. A re-plan reads no changes.
5. THE APPLIER READS NO SECRET VALUE. The exercised read is the Dells' own: dell2's Black Diamond split pull
   (`blackdiamond/49f/session`) and dell1's classification run (`astn/kimi/api-key`). Until then: APPLIED, not EXERCISED.
6. The CTO tells Andrew, in plain words when it signs, the four widest facts of this plan: every Dell seat can read the
   Bloomberg, Schwab, Black Diamond, Orion and SmartX sign-ins and every model key; the 28 platform keys stay out; a Dell can
   already overwrite any secret; and "change who may reach a resource" is delivered by plan 2, not this one.

**SIGNED** -- `2.0.0_SA_COO~C`
