# Deploy Completion Record
**Date opened:** 2026-10-09T10:28:06.211853+00:00
**Status:** OPEN
**Deploy:** FWD-5: narrow secretsmanager:DescribeSecret off smartx-assets-pull-role ReadAuthBundle (one action, one role, one file)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| TF | activation | aws_iam_role_policy.assets_pull | targeted safe-apply drops exactly one action from the ReadAuthBundle statement; plan is 0 add / 1 change / 0 destroy or it is a STOP | Patch applied from worker ~13's own narrowing.patch via git apply (--check first, never retyped); plan -target on the one policy graded from show -json by DECOMPOSING the policy document per Sid, because an IAM role policy is one opaque 'policy' attribute and 0/1/0 would read identically if a resource had been dropped or another statement widened: REMOVED {'ReadAuthBundle': ['secretsmanager:DescribeSecret']}, ADDED {}, resource sets identical across all 4 statements, 5 resource_changes with exactly 1 non-no-op. Applied from the SAVED plan through safe-apply; the naming-apply-gate WARNed on two pre-existing out-of-pattern names and refused nothing. Live read-back: ReadAuthBundle carries ['secretsmanager:GetSecretValue'] alone over its 5 resources, 4 statements intact; targeted re-plan 'No changes. Your infrastructure matches the configuration.' Committed e02476796b. terraform fmt -check clean. | CLOSED 20261009T104148Z |
| SIM | verify | smartx-assets-pull-role | simulate-principal-policy: the removed action reads implicitDeny, a retained action on the same statement reads allowed as the control, each in its OWN invocation | simulate-principal-policy on the live role, ONE --resource-arns per invocation because two or more in one call flips the HELD ones to implicitDeny and would manufacture this result. Removed action secretsmanager:DescribeSecret: implicitDeny on 5 of 5 ReadAuthBundle resources. CONTROL in its OWN separate invocations, same principal and same resources: secretsmanager:GetSecretValue allowed on 5 of 5 -- which is what makes the denies a fact about the ACTION rather than about the call. SECOND control on a different statement: PutSecretValue on smartx/jwt/current allowed. All five ARNs RESOLVED from list-secrets (100 listed) rather than typed as patterns, so each decision is about an object that exists. predicted_post_state met clause by clause. Raw JSON quoted verbatim in W/fwd5/OUTCOME.md sections 2-3. Two instrument limits recorded there rather than papered over: a nonexistent action also returns implicitDeny (validate-policy is barred by G-25, so the corroboration is that AWS accepted this exact string in the policy until today and GetSecretValue returns allowed on the same call shape), and implicitDeny is the CORRECT verdict because an Allow was removed rather than a Deny added. | CLOSED 20261009T104148Z |
| OBS | verify | smartx-assets-daily-pull | the observation window: the first scheduled 13:02Z run that STARTS after the apply, read at 13:30Z against the four falsifiers F1-F4 |  | OPEN |

## Log

- 20261009T102806Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261009T104148Z LEG TF closed: Patch applied from worker ~13's own narrowing.patch via git apply (--check first, never retyped); plan -target on the on
- 20261009T104148Z LEG SIM closed: simulate-principal-policy on the live role, ONE --resource-arns per invocation because two or more in one call flips the
