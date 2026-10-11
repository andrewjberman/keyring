# Deploy Completion Record
**Date opened:** 2026-10-11T07:58:36.726225+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T081142Z
**Deploy:** ADVI_COTBKF CB-bj-1 (FWD-7): create cloudops-cot-restricted-breakglass-role + its inline policy by a TARGETED apply of 2 IAM addresses under the FWD-7 never-widen pair
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 2: targeted plan, saved outside the repo, Branch A gate | the plan's two addresses and its count line: exactly '2 to add, 0 to change, 0 to destroy' and no third address | step 2 BRANCH A MET, rc=0, 0 Error blocks. Count line exactly 'Plan: 2 to add, 0 to change, 0 to destroy.' Addresses, exactly two and exactly the targets: aws_iam_role.restricted_breakglass (create), aws_iam_role_policy.restricted_breakglass (create). No third address, no change, no destroy. Plan saved OUTSIDE the repo at C:/dev/_cotbkf_private_evidence_20261009/r62/breakglass_targeted.tfplan. Plan body read against both halves and matching: role cloudops-cot-restricted-breakglass-role, path /, max_session_duration 3600; trust = ONE statement Sid ConsoleUserOnly, sts:AssumeRole, Principal.AWS arn:aws:iam::313476888478:user/Andrew_Berman_Console, no condition, no service, no wildcard; inline policy restricted-prefix-get-put-list = s3:GetObject + s3:GetObjectVersion + s3:PutObject on arn:aws:s3:::opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/* and s3:ListBucket on the bucket under a StringLike s3:prefix condition scoped to that prefix. FOUR actions, NO delete. ONE DISCREPANCY RECORDED, not a Branch B: the COO half's section 1 says the role has 'no tags', but the plan shows tags_all with 4 provider default_tags (Environment=Production, ManagedBy=Terraform, Project=OpalPortal, System=SharedInfra). Tags are metadata, grant nothing, and are not a third address, a change or a destroy, so Branch A stands; the half's blast-radius sentence is inexact on that one point and the report says so. NOTE on row D2-S92: this targeted plan returned rc=0 with ZERO AccessDenied errors, where the untargeted plan of round 61 returned rc=1 with two -- empirical confirmation of the CTO half's narrowing, since targeting excluded the portal bucket from the refresh. | CLOSED 20261011T080140Z |
| L2 | activation | step 3: apply THE SAVED PLAN via .tools/safe-apply.sh (the WORLD act) | the apply's summary line; which branch ran; every gate refusal verbatim | NOT APPLIED. NOTHING WAS CREATED. This leg is closed as REFUSED-BEFORE-APPLY, not as done. safe-apply.sh rc=7; terraform was never invoked. Final line verbatim: 'safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=1). Nothing was planned further or applied.' The refusal: '[naming-plan-gate] NAMING REFUSE aws_iam_role_policy.restricted_breakglass restricted-prefix-get-put-list -> cloudops-49f-restricted-breakglass-policy ... [grade() said: RAISE as IAM_POLICY: a rule or registry defect, not a naming verdict: R1.f: restricted is in no vocabulary; no registry row resolves it. DEC-6: refused like any refusal once enforcing]'. The sibling ROLE name graded CONFORMANT. Seat gates both passed (APPLY-WHO ADMITTED, CROSSBOX-DEPLOY CLEAR), so the naming limb is the sole stop. VERIFIED ABSENT AFTER THE REFUSAL, not assumed: get-role -> NoSuchEntity beside an isolated positive control returning a real ARN; terraform state 253 rows, 0 breakglass, 10 lgic_firm. No rollback was needed or performed and Branch C's pre-authorised destroy was NOT invoked -- it presupposes a created role, and there is none. Row ADVI_COTBKF-D2-S98. | CLOSED 20261011T081141Z |
| L3 | verify | step 4 proof 1: get-role (one principal) + get-role-policy (four actions) | both outputs | UNREACHABLE BY CONSTRUCTION -- not run, and not a pass. Proof 1 (get-role one principal, get-role-policy four actions) reads objects that the refused apply never created. The only get-role this seat ran returns NoSuchEntity, with an isolated positive control passing, which is the evidence for L2's 'nothing created' and is NOT evidence for this leg's criterion. CB62bj1-AC2 therefore cannot be met as written. | CLOSED 20261011T081141Z |
| L4 | verify | step 5 proof 2: untargeted PLAN ONLY, the two addresses both no-op | the BREAKGLASS-PLAN-AFTER line (the_two=2 the_two_changed=0) | UNREACHABLE BY CONSTRUCTION -- not run, and not a pass. Proof 2 is the post-apply untargeted plan whose JSON feeds CB62bj1-AC1; with nothing applied, an after-plan would read the two addresses as 2 creates, which is the pre-state, not the criterion's 'the_two_changed=0'. Running it would produce a number that looks like a reading and means nothing, so it was not run. C:/dev/_cotbkf_private_evidence_20261009/r62/shared_infra_plan_after.json does NOT exist and CB62bj1-AC1 cannot be met as written. | CLOSED 20261011T081141Z |

## Log

- 20261011T075836Z OPENED by 0.7.0_AE_CloudOps~CB2 with 4 leg(s)
- 20261011T080140Z LEG L1 closed: step 2 BRANCH A MET, rc=0, 0 Error blocks. Count line exactly 'Plan: 2 to add, 0 to change, 0 to destroy.' Addresses, ex
- 20261011T081141Z LEG L2 closed: NOT APPLIED. NOTHING WAS CREATED. This leg is closed as REFUSED-BEFORE-APPLY, not as done. safe-apply.sh rc=7; terraform
- 20261011T081141Z LEG L3 closed: UNREACHABLE BY CONSTRUCTION -- not run, and not a pass. Proof 1 (get-role one principal, get-role-policy four actions) r
- 20261011T081141Z LEG L4 closed: UNREACHABLE BY CONSTRUCTION -- not run, and not a pass. Proof 2 is the post-apply untargeted plan whose JSON feeds CB62b
- 20261011T081142Z CLOSED -- all 4 legs proven

## CLOSE DISPOSITION -- NOT APPLIED. NOTHING WAS CREATED. READ THIS BEFORE THE STATUS LINE.

**The Status line above says CLOSED. That means every leg is dispositioned and nothing is stranded. It does
NOT mean the deploy happened. IT DID NOT.** The two IAM objects this entry was opened for do not exist.

- `aws_iam_role.restricted_breakglass` -- **NOT created.**
- `aws_iam_role_policy.restricted_breakglass` -- **NOT created.**

`safe-apply.sh` exited 7 and terraform was never invoked:

> safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=1). Nothing was planned
> further or applied.

The targeted plan itself was **Branch A** and correct (`2 to add, 0 to change, 0 to destroy`, only the two
targets). The stop came after the plan and before the apply, from the naming gate. Both seat gates passed
(`APPLY-WHO ... verdict=ADMITTED`, `CROSSBOX-DEPLOY ... verdict=CLEAR`), so the naming limb is the sole stop.

**Verified absent after the refusal, not assumed:** `get-role` -> `NoSuchEntity` beside an isolated positive
control returning a real ARN; `terraform state list` 253 rows, 0 matching `breakglass`, 10 matching
`lgic_firm`. No rollback was needed or performed. **Branch C's pre-authorised targeted destroy was NOT
invoked** -- it presupposes a created role, and there is none.

## HELD IN EFFECT (the tool could not carry this state, so the text does)

`deploy_ledger.py hold` refused both forms: `--pre-apply` because the plan leg already carries proof ("the act
has started"), and a normal `hold` because an open apply leg reads to it as "a half-landed deploy". Neither
describes this act, which planned, was refused at the gate, and created nothing. Filed as row
`ADVI_COTBKF-D2-S99`. So the hold is recorded here instead:

- **Gate class:** external.
- **Named dependency:** an LGIC naming-canon resolution for the token `restricted`, so that
  `opal_naming.grade('restricted-prefix-get-put-list','IAM_POLICY')` returns a verdict instead of raising
  `RaiseDefect R1.f: 'restricted' is in no vocabulary; no registry row resolves it`. Registry owner: the laptop
  `1.0.0_SA_CTO` (CTO ruling @27ba4d3769 item 4). Routed via `2.0.0_SA_COO~C2`. Row `ADVI_COTBKF-D2-S98`.
- **Re-read event:** an amendment to `ADVI_COTBKF.TO-CB-bj-1` naming the resolved policy name and the commit
  carrying it. Re-read by re-running the targeted plan and confirming it is still Branch A **before** any apply.
- **Not a date.** Nothing about this act decays with time; it waits on a named remedy.

**Do not clear the gate by typing the owed name in.** The gate's suggestion,
`cloudops-49f-restricted-breakglass-policy`, carries the **49f** firm token on a policy whose only grants are on
`opal-data-cottonwood`'s `commonwealth/cottonwood/bronze/crm/` prefix -- while the same gate graded the sibling
role CONFORMANT as `cloudops-cot-`. Adopting it as printed would name a Cottonwood-only break-glass grant after
49 Financial. CLAUDE.md rule 30 also makes a builder refusal a registry row to add, never a hand-typed
workaround, and editing the `.tf` literal would change the very blob both pair halves pinned at `8c6fc7652a`.

**A re-run is a NEW ledger entry.** This one is terminal.
