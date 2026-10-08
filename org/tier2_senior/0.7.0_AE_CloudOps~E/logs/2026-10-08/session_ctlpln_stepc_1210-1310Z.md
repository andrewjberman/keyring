# Step C: the Allow of 70 resource-policy actions -- the widest act of the day, and two of my own controls that proved nothing until they were redone -- `0.7.0_AE_CloudOps~E`

**Date:** 2026-10-08
**Task Order:** NFRA_CTLPLN.TO-APPLY-13.dell-identity-step-c-resource-policy-allow-apply-laptop (@109a06316a, GO msg 106917)
**Status:** COMPLETE
**archetype:** DEPLOY

**Preceding log:** `session_ctlpln_stepb_1100-1210Z.md`. **Issuer:** `2.0.0_SA_COO~C`. **Box:** the laptop. WORLD
risk, genre DEPLOY, both halves read in full.

---

**Until the variable's default is made true in the root, any plan or apply of nfra-ctlpln-identity WITHOUT
`-var apply_respol_allow=true` will plan to DESTROY the Allow.** The bounds require that sentence; it was
**measured** before it was written -- a read-only plan without the variable, after the apply, reads exit=2 and
`Plan: 0 to add, 0 to change, 2 to destroy`, naming exactly the two resources this act created. Applied to nothing.
The durable fix is the issuer's cell; the default was not changed and no tfvars file was written.

## Deployment Sequence

| step | act | result |
|---|---|---|
| 0 | HEAD contains `203344e1b1`; root clean | yes; status empty |
| 1 | `simulate_policy.py` | `freed_allowed=70/70 freed_excluded=5 undo_denied=181/181 ... all_ok=True` |
| 2 | plan **WITHOUT** the variable | `No changes.` exit=0 -- the proof steps A and B are as applied |
| 2 | the group's attachment list saved | five policies, `b4fe7679...` |
| 3 | plan **WITH** `-var apply_respol_allow=true` | exit=2 `2 to add, 0 to change, 0 to destroy`; **100 added / ZERO removed**; **70 distinct actions** |
| 4 | NEVER-2 entry opened with its sentinel | `c6011870f6`, six legs |
| 5 | ONE `safe-apply` with the variable | `Apply complete! Resources: 2 added, 0 changed, 0 destroyed` |
| 6 | read-back, 24 arms | V1 + 10 mutants; V2 6/6; V3 14/14; V4 4/4 |
| 6 | re-plan **with** the variable | `No changes.` exit=0 |
| 6 | plan **without** it, to measure the hazard | `0 add, 0 change, 2 to destroy` |

**THE APPLIED TIME: `2026-10-08T12:39:33Z`** -- both IAM events in the same second (CloudTrail).

## What the act grants, at the width both halves signed

An agent seat on either Dell box can now change **who may reach** almost any resource in the account that no
explicit Deny protects. Five routes are named in the halves and in the entry, and the first is the sharpest:
**`s3:PutBucketPolicy` on the three firm data buckets -- the fences this same seat applied at 05:17:17Z this
morning.** Also the Terraform state bucket's policy, any key's policy or grants (including the key encrypting
`schwab/sdd/session`), the transcripts key this seat granted on 10-07, and the shared assets bucket's ACLs.

Held out, and each verified live: every `iam:` action, a secret's own policy (what keeps the 28 platform keys out),
the trail, the ten protected functions, the audit bucket, the four agentbus queues.

## Two of my own controls proved nothing until they were redone

1. **The three forbidden-service mutants all read False on the wrong limb.** Planting an `iam:`, a
   `secretsmanager:` and a `cloudtrail:` action each failed the comparator -- but on the **count** limb (71 against
   70), which demonstrates nothing about the forbidden-service check. Count-preserving **swaps** were then run
   (`s3:PutBucketPolicy` out, each forbidden action in) and all three read False naming the service.
2. **The breakdown mutant used an action already in the policy.** `sns:AddPermission` was caught by
   **distinctness**, so the per-service limb stayed undemonstrated -- while the evidence file already claimed all
   four limbs were demonstrated. **That over-claim was deleted from the file**, a genuinely absent action was
   chosen by subtraction from the live list (`sns:SetTopicAttributes`), and its swap reads False naming the
   breakdown itself (s3 13 against 14, sns 3 against 2).

A mutant that fails for the wrong reason is a passing control that proves nothing. Both rounds are in the evidence.

## Verification

- **V1.** One statement, Effect Allow, Resource `*`, 70 distinct actions, per-service breakdown equal to the signed
  table in all seventeen services, no forbidden service -- against ten mutants across all four limbs. Group five
  to six, one addition, nothing removed.
- **V2.** 6/6 granted arms allowed, all matching the policy this act created. The unprotected function was chosen
  by extracting the ten protected names from `DenyProtectedFunctions`'s own twenty resources, so the arm is not
  accidentally probing a protected one.
- **V3.** 14/14 held-out arms refused, **every one attributed to a single named statement** -- the collapse from
  step A's pairs that row `NFRA_CTLPLN-S29` predicted, now confirmed a third time. The sweep's first run FAILED
  with `FileNotFoundError` on the step-B policy's snapshot, which is how a stale identity side was caught instead
  of refusals being silently attributed to a policy that no longer exists.
- **V4.** The bus unchanged, as before step A, after step A, after step B and after step C.
- **Nothing was exercised.** No `put-bucket-policy`, `put-key-policy`, `add-permission` or `set-queue-attributes`
  call exists in any artifact of this act.

## Decisions Made

1. **The wrapper's `-var` handling was read at its own source lines** (`:215-216`, `:207-209`, `:217`, `:266-274`,
   `:522`), because the order makes a wrapper that drops it a STOP and forbids working around it.
2. **The per-service breakdown was checked, not just the count of 70** -- a bare count passes a substitution that
   keeps the total.
3. **The hazard sentence was measured before it was written**, which also measured the rollback, since both use the
   same mechanism.

## Compiler Tools

| tool | result |
|---|---|
| `simulate_policy.py` | AC1, before and after, identical: `freed_allowed=70/70 freed_excluded=5 undo_denied=181/181` |
| `terraform plan` x4 / `apply` | without the variable: No changes; with it: 2 add; applied; re-plan 0-diff; without it after: 2 destroy |
| `iam:SimulatePrincipalPolicy` / `SimulateCustomPolicy` | 24 live arms plus the attribution sweep; every refusal named singly |
| `iam get-policy` / `list-attached-group-policies` | the live document and the group's list before and after |
| `cloudtrail lookup-events` | both IAM events at 12:39:33Z -- the applied time from the AWS plane |
| `deploy_ledger.py`, `proof-of-spec-check.py` | entry CLOSED 6/6; proof **VALID rc=0**, 8 of 8 controls discriminate |
| `comp-iam` | **correctly not run**: this act grants 70 actions on Resource `*` whose whole safety is *which resources* the Denies carve back out -- the one thing an `(action)`-only model cannot see |

**What worked:** the count-preserving swap as a mutant form. **What failed:** two of my own mutant rounds, caught
by reading what each failure actually named. **Gap found:** none new.

## Blockers

**None.**

## Current State

**FIVE WORLD applies landed today**, every one CLOSED with its legs proven and no sentinel of this seat's left:
TO-APPLY-10 at 05:17:17Z, the Teams agent at 08:15:35Z, step A at 09:19:39Z, step B at 11:33:48Z, step C at
12:39:33Z. **The Dell identity three-step is complete.** Every grant is **APPLIED, NOT EXERCISED**.

## Next Steps

1. **[`2.0.0_SA_COO~C`] The durable default -- the one thing that should not wait.** Until it lands, any plan of
   this root without the variable destroys the Allow. CTO ruling 106915 keeps other seats off the root until then.
2. **[`1.0.0_SA_CTO`]** Three undone and all yours: tell Andrew the five routes in plain words; tell both Dell CTOs
   the before-rule before a Dell's first resource-policy change; and the applied times to pass on (12:39:33Z here,
   11:33:48Z for the secrets, 09:19:39Z for the parameter).
3. **[a Dell, by another route]** The exercises: a first resource-policy change (reported to the laptop), the Black
   Diamond pull, the classification run, the YCharts plan, and one real Teams request.
4. **[the owed cell's owner]** `secretsmanager:PutSecretValue` on any secret plus step C's Allow are now the widest
   standing pair in that document.
