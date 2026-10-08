# CTO never-widen half -- NFRA_CTLPLN: the Dell identity root, PLAN 1 of 2 -- the secrets read (66 of 114), the resource-policy Deny off, self-simulate

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~05:1xZ. **Counterpart read in full, all 160 lines:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_PLAN_1_SECRETS_DENY_OFF_SELF_SIMULATE_20261008.md`
@fa6d36f4a3. **Not read by this seat:** the plan itself, the census file, the simulator's output, the worker's plan note (the
28 withheld and 19 unplaced by name), any secret's value.
**Authority:** Andrew-direct 2026-10-08 ~00:4xZ, "lets start with lifting 1 2 3 6"; item 1 as put to him: "Read any stored
secret: vendor keys, client sign-in sessions"; item 3: "Change who may reach a resource". Record @14a030c049.
**Supersedes** `CTO_HALF_NFRA_CTLPLN_DELL_VENDOR_SECRETS_20261007.md` (@922ebc4b5d; three keys; never applied).

## What this half signs

The act the counterpart names: one untargeted `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/`, plan shape
`2 to add, 1 to change, 2 to destroy`: a read of 66 named secrets for the Dell group; the 75-action resource-policy Deny
removed; each Dell user may simulate its own policy.

## Where this seat's judgment was used, and how it went

1. **No strike among the 66.** The counterpart offers the CTO a strike of any of them. None is struck: his word lifted the
   read of vendor keys and client sign-in sessions, the 66 are those two classes, and narrowing his word a second time
   (the 28 are already held out as an interim reading) is not this seat's to do.
2. **One of the 66 can upset another box, and is bound by a rule instead of a strike:** `bloomberg/terminal/login` and
   `bloomberg/session`. Site Z is the only box with the terminal; a second sign-in can end the first, and the sign-in is
   budgeted (`integrations/bloomberg/READ_HERE.md`). A Dell may hold the value. A Dell does NOT sign in to Bloomberg: that is
   site Z's, under this project's C-LEASE. This is the cross-box case his 19:0xZ word leaves with the laptop. Condition 3.
3. **The 28 platform keys stay out**, as an interim reading he has been told of and has not answered. **The Secrets Manager
   resource-policy actions stay out of plan 2's Allow**, so the withholding is not undone by the door beside it.
4. **"A read is not a permission to call"** is true and is enforced by nothing. For the Dells he has said vendor calls are
   theirs "as needed"; the vendor list's own lines (OpenAI scoped to one project) still read as they did. Stated, not solved.

## Blast radius

Two principals, through one group. Changed: what the two Dell users may READ (66 secrets, exact ARNs, one action);
`sqs:SetQueueAttributes` becomes allowed to them on any queue; each may simulate its own policy. Not changed: any secret's
value or policy; any key policy; any other principal; the routes Deny; `s3:PutBucketPolicy`, `kms:PutKeyPolicy` and
`lambda:AddPermission`, which stay refused until plan 2.

## Expected outcome, BOTH branches

As the counterpart's. A: exactly the five resources, exactly 66 secret ARNs and one action, the one added statement, zero hits
for the ten withheld-name patterns in the plan -> apply. B: anything else -> apply nothing and report.

## Conditions

1. The counterpart's conditions 1 to 6 stand.
2. The applier reads no secret value. The first exercised reads are the Dells' own: dell2's Black Diamond pull and dell1's
   classification run.
3. Both Dell CTOs are told, before a Dell seat first reads a secret: no Dell signs in to Bloomberg; and a credential read is
   reported to the laptop like a deploy (which secret, which run), not approved by it.
4. Plan 2 follows as its own pair and leads with dell2's SSM public-parameter read by exact ARN; this half does not cover it.
5. The standing overwrite (`secretsmanager:PutSecretValue` on any secret, in the create policy) is not made safer or worse by
   this plan. Its narrowing stays an owed cell, ahead of the remaining SEATS cells.

**SIGNED** -- `1.0.0_SA_CTO`

## AMENDMENT 1 (1.0.0_SA_CTO, 2026-10-08 ~07:2xZ) -- the act is a TARGETED apply at the five signed addresses

**Why.** The applier, `0.7.0_AE_CloudOps~E`, stopped at its step 3 on branch B and applied nothing (row NFRA_CTLPLN-S25, read by
this seat): the untargeted plan read 4 to add, 1 to change, 2 to destroy, seven resources. The two extra are plan 2's
resource-policy Allow (`aws_iam_policy.dell_agent_respol_allow[0]` and its group attachment), which commit f7b668e9c5 landed in
the root after the issuer planned and which both halves exclude. The stop was right. The signed five each read exactly as signed.

**What changes.** "One untargeted safe-apply of the root" becomes: one `safe-apply` TARGETED at exactly
`aws_iam_policy.dell_agent_vendor_secrets[0]`, `aws_iam_group_policy_attachment.dell_agent_vendor_secrets[0]`,
`aws_iam_policy.dell_agent_create`, `aws_iam_policy.dell_agent_respol` and `aws_iam_group_policy_attachment.dell_agent_respol`.
Branch A: the targeted plan reads exactly 2 to add, 1 to change, 2 to destroy, those five and no other, each as signed.
Branch B: anything else, and in particular either `dell_agent_respol_allow` address appearing in the targeted plan.

**What does not change.** Every condition of this half and the counterpart's. The Allow is NOT applied under this pair: it
waits for plan 2's own pair, which carries the three Deny exclusions ruled at 06:03Z; applied without them it would open the
ten protected functions, the audit-trail bucket and the agentbus queues. After this targeted apply the untargeted plan of the
root still reads the Allow as 2 to add: reported, not applied.

**For the root's owner:** a resource that must not apply yet was merged into a root whose signed act was untargeted, with no
flag holding it back. Plan 2's resources stay out of the trunk, or behind a count that is 0, until their pair is signed.

**SIGNED, as amended** -- `1.0.0_SA_CTO`
