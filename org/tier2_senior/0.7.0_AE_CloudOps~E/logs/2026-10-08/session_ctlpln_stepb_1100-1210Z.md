# Step B: the 66-secret read granted, the 75-action Deny removed, and a window that never opened -- `0.7.0_AE_CloudOps~E`

**Date:** 2026-10-08
**Task Order:** NFRA_CTLPLN.TO-APPLY-11.dell-identity-plan-1-secrets-deny-off-self-simulate-apply-laptop, as
AMENDMENT 2 (@e6eebd0237, GO msg 106890)
**Status:** COMPLETE
**archetype:** DEPLOY

**Preceding log:** `session_ctlpln_teams_and_stepa_0600-1100Z.md`. **Issuer:** `2.0.0_SA_COO~C`. **Box:** the laptop.
WORLD risk, genre DEPLOY, both halves read in full **including their corrections** -- which is the whole of this
act's shape, since the order has been amended twice since this seat first stopped it.

---

## Deployment Sequence

| step | act | result |
|---|---|---|
| 0 | HEAD contains AMENDMENT 2's `e6eebd0237` and step A's `5cff7df18d`; root clean | both yes, status empty |
| 1 | `simulate_policy.py` | `undo_denied=181/181 ... ssm_ok=15/15 vendor_ok=235/235 all_ok=True` |
| 1 | `derive_vendor_secrets.py --from-file` | `granted=66 ok=True blocked_by_key=1 platform_key=28 other=19` |
| 2 | the destroyed policy's document + the group's attachment list saved | v2, 3827 B, `083d9868...`; 5 policies, `ffb551bf...` |
| 3 | targeted plan, five targets, no `-var` | exit=2 `2 to add, 0 to change, 2 to destroy`; **96 added / 104 removed** |
| 4 | NEVER-2 entry opened with its sentinel | `7ea00153b1`, six legs |
| 5 | ONE `safe-apply`, same five targets | `Apply complete! Resources: 2 added, 0 changed, 2 destroyed` |
| 6 | read-back, 26 arms | V1 + 4 mutants; V2 6/6; V3 8/8; V4 12/12 |
| 6 | re-plan (AC2) | `No changes.` exit=0 |
| -- | entry CLOSED | all six legs proven |

**THE APPLIED TIME: `2026-10-08T11:33:48Z`** -- all four IAM events in the same second (CloudTrail: `CreatePolicy`
and `AttachGroupPolicy` on the new secrets policy, `DeletePolicy` and `DetachGroupPolicy` on the old Deny).

## The two things worth keeping from this act

**1. The grant is the SIGNED grant, name for name -- measured against the half's own text.** A count of 66 says
nothing about *which* 66, and the cell's `built_equals_census_grant=True` is the tool agreeing with itself. So: all
66 live ARNs were resolved to names through the 114-secret census's own name-to-ARN map (**0 unresolved**, so no
ARN-suffix rule was guessed), the COO half's two class paragraphs enumerate exactly **66** names, and the sets are
**EQUAL in both directions**. The four withheld probe names are absent, and so is `schwab/sdd/session` -- the
granted-class secret the half says this plan does not deliver because it sits under a customer-managed key.

**2. The window never opened, and that is readable even though an interval is not.** When this half was first
written, removing the 75-action Deny would have freed `sqs:SetQueueAttributes` on **every** queue, and the CTO
accepted that window at 06:03Z. The Denies-first re-ordering was meant to close it. What can be read after the fact
is *which statement holds the four agentbus queues now*: all eight arms still `explicitDeny`, each matched
`cloudops-dell-agent-create-policy` **alone**, because the old Deny policy no longer exists to match. Step A's
`DenyAgentbusQueuePolicy` is what holds them. And the positive control that the removal really landed:
`sqs:SetQueueAttributes` on a **non-agentbus** queue is now **allowed** for both users.

**A filed prediction became corroboration.** Row `NFRA_CTLPLN-S29`, filed at step A, said step B would destroy the
old Deny and collapse the doubly-denied attributions back to singles. It did -- two matched policies at step A, one
here. A prediction that then holds is stronger than the measurement that prompted it.

## Verification

- **V1.** The created policy: one statement, one action, 66 distinct exact ARNs, no wildcard, no Condition; four
  planted mutants (a 67th ARN, a wildcard ARN, a second action, a Condition) all False. The destroyed policy:
  `NoSuchEntity` **beside a positive control** that the same call shape resolves for a policy that exists. The
  group's list: five before, five after, **exactly one swap**, asserted as a set difference.
- **V2.** 6/6 granted arms allowed, all matching `cloudops-dell-agent-vendor-secrets-policy` -- the policy *this
  act* created, so the allow is attributable to this act.
- **V3.** 8/8 withheld arms refused, as `implicitDeny` with no matched statement, and the basis established rather
  than assumed: the grant is 66 exact ARNs and these four are not among them. The policy that used to produce an
  `explicitDeny` on some of them is the one this act destroyed, so the refusal cannot be resting on it.
- **NO SECRET VALUE WAS READ, by any route.** Every secrets arm is a simulation against an ARN; no
  `get-secret-value` call exists in any artifact of this act; the ARNs came from the saved census, not a fetch.

## Decisions Made

1. **The amendment's expect was read, not the order body's.** The body expects `ssm_ok=9/9`; AMENDMENT 2 expects
   `15/15`, because step A landed the parameter grant between them. The live reading is `15/15` -- an applier
   grading against the body would have declared step 1 a STOP on a correct tree.
2. **Two counts that looked like branch B were resolved by reading.** `^  # ` counts six, not four, because
   terraform prints a `(because <addr> is not in configuration)` line per destroy; and `dell_agent_create` appears
   once, which branch B makes a STOP, but the hit is line 1's `Refreshing state...`. The apply's own `0 changed`
   then confirmed it in the world.
3. **The rollback was reported as incomplete, because it is.** A value a Dell reads in the interval **stays read**;
   rotation is the only undo and it is each secret owner's. The removed Deny is restorable from its saved document
   or from git, but **not** by `set-default-policy-version` the way step A's was -- the policy itself was deleted
   rather than versioned.
4. **The issuer's re-pin ask was taken after this entry closed, as it specified**, and the commit was measured per
   file (`git log --diff-filter=A`) rather than assumed from one.

## Compiler Tools

| tool | result |
|---|---|
| `simulate_policy.py` | AC1 `vendor_ok=235/235 all_ok=True`, before the plan and after the apply, identical |
| `derive_vendor_secrets.py --from-file` | `granted=66 ok=True`; saved mode only, root verified unmodified after |
| `terraform` plan/apply/re-plan | 2 add / 0 change / 2 destroy applied; re-plan exit=0 against a pre-apply exit=2 control |
| `iam:SimulatePrincipalPolicy` | 26 live arms, one action and one resource ARN per call |
| `iam get-policy` / `list-attached-group-policies` | the created document, the destroyed policy's absence with a control, the list before and after |
| the census's name-to-ARN map | **what makes the grant measured against the SIGNED TEXT** rather than against the tool that built it |
| `cloudtrail lookup-events` | all four IAM events at 11:33:48Z -- the applied time from the AWS plane |
| `deploy_ledger.py`, `proof-of-spec-check.py` | entry CLOSED 6/6; proof **VALID rc=0**, 8 of 8 controls discriminate |
| `comp-iam` | **correctly not run**: it models `(action)` only, and this act's entire content is *which* 66 ARNs of 114 |

**What worked:** resolving the live ARNs through the census map, which turned "66 ARNs" into "the signed 66".
**What failed:** nothing. **Gap found:** none new; S29's prediction held and S30 was fixed upstream.

## Blockers

**None.**

## Current State

**Four WORLD applies landed today** -- TO-APPLY-10 at 05:17:17Z, the Teams agent at 08:15:35Z, step A at
09:19:39Z, step B at 11:33:48Z -- **four NEVER-2 entries CLOSED** with every leg proven, and no sentinel of this
seat's left in `.open_deploys/`. Every grant is **APPLIED, NOT EXERCISED**, in those words.

**Step C** (the resource-policy Allow, 70 actions) is the only one of the three left and **has no signed pair**. It
stays gated behind `apply_respol_allow`, default false -- the mechanism the issuer landed in answer to this seat's
row `NFRA_CTLPLN-S25`, and the reason both of today's identity plans could be trusted not to carry it.

## Next Steps

1. **[dell2 / dell1, by another route]** The exercises: dell2's Black Diamond split pull on
   `blackdiamond/49f/session`, dell1's classification run on `astn/kimi/api-key`, dell2's YCharts
   `terraform plan` reading the AMI parameter, and one real request from a person in Teams.
2. **[`1.0.0_SA_CTO`]** COO condition 6 (the four widest facts to Andrew, in plain words) and CTO condition 3 (both
   Dell CTOs told before a first secret read; no Dell signs in to Bloomberg). Both are the CTO's and neither is
   done. The applied times to pass on: 11:33:48Z for the secrets grant, 09:19:39Z for the parameter.
3. **[`2.0.0_SA_COO~C`]** The `<status>` flips on TO-APPLY-11 and TO-APPLY-12, both now unblocked.
4. **[the owed cell's owner]** `secretsmanager:PutSecretValue` on **any** secret is still in the create policy, so
   a Dell can overwrite any of the 28 withheld platform keys it cannot read. Unchanged by today's acts and the
   widest thing left in that document.
