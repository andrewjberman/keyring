# Deploy Completion Record
**Date opened:** 2026-10-11T13:40:47.317505+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T134644Z
**Deploy:** ADVI_FIRMBKTS TO-FB-g-8 (window act 0): create ONE inline policy advi-49f-platinum-canonical-rw-policy on role bd-exporter-ec2-role (root infra/aws/terraform/bd-pipeline), the producers' grant for the canonical platinum home; pair COO half @0911fa9901 + CTO half @37ef51525c; rollback = aws iam delete-role-policy of that one name; the QA runner shares the role and is a recipient of the Allow
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: both pair halves SIGNED at the current bytes, the role's 16 inline policies and none of this name, the actor's iam:PutRolePolicy read at the role ARN | the entry carries the read lines | COO half @0911fa9901 and CTO half @37ef51525c both SIGNED and unchanged since (git log of each file = its signing commit, 0 uncommitted); before-state 16 inline policies on bd-exporter-ec2-role and none named advi-49f-platinum-canonical-rw-policy; actor iam:PutRolePolicy simulated allowed at arn:aws:iam::313476888478:role/bd-exporter-ec2-role (cloudops-dell-agent-iam-roles-policy), DeleteRolePolicy allowed | CLOSED 20261011T134643Z |
| L2 | activation | scoped plan of bd-pipeline (-target module.opal_name_platinum_grant and the policy resource) reads exactly Plan: 1 to add, then .tools/safe-apply.sh on the saved plan | the plan summary line and the apply result line | scoped plan Plan: 1 to add, 0 to change, 0 to destroy (module.opal_name_platinum_grant and the policy resource; plan JSON: 1 create, 2 resource_changes in all); .tools/safe-apply.sh on the saved plan 13:43:23Z-13:44:07Z: Apply complete! Resources: 1 added, 0 changed, 0 destroyed; id bd-exporter-ec2-role:advi-49f-platinum-canonical-rw-policy | CLOSED 20261011T134643Z |
| L3 | verify | AC1 get-role-policy returns the two Sids, AC2 the role holds 17 inline policies, AC3 the scoped plan reads No changes | the three outputs quoted | AC1 AdviPlatinumCanonicalObjects AdviPlatinumCanonicalList; AC2 17 inline policies; AC3 the scoped plan reads No changes. Your infrastructure matches the configuration. (line 4 of 17, evidence/act0/ac3_full_plan.out); the order's literal tail -n 6 window excludes that line, so AC3 FAILS as ordered and the invocation is the issuer's to amend | CLOSED 20261011T134643Z |
| L4 | git | proof instance written and TO-FB-g-8 status flipped complete in one commit | commit hash | proof instance deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-g-8.act0-grant.proof_of_spec.json committed with this entry; TO-FB-g-8 status NOT flipped to complete (AC3 literal FAIL, the issuer's invocation); commit hash is this commit | CLOSED 20261011T134644Z |

## Log

- 20261011T134047Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
- 20261011T134643Z LEG L1 closed: COO half @0911fa9901 and CTO half @37ef51525c both SIGNED and unchanged since (git log of each file = its signing commit
- 20261011T134643Z LEG L2 closed: scoped plan Plan: 1 to add, 0 to change, 0 to destroy (module.opal_name_platinum_grant and the policy resource; plan JSO
- 20261011T134643Z LEG L3 closed: AC1 AdviPlatinumCanonicalObjects AdviPlatinumCanonicalList; AC2 17 inline policies; AC3 the scoped plan reads No changes
- 20261011T134644Z LEG L4 closed: proof instance deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-g-8.act0-grant.proof_of_spec.json committed with t
- 20261011T134644Z CLOSED -- all 4 legs proven

## RECIPIENTS AND OUTCOME (0.7.0_AE_CloudOps~FB1, 2026-10-11T13:46:43Z)

- **Recipients of the Allow (the order's condition):** the policy attaches to the ROLE `bd-exporter-ec2-role`, so every principal that
  assumes it gains Put and Get on `opal-data-49financial/advi/49financial/platinum/*` and List under that prefix: the gold layer runner
  `bd-gold-layer-runner` (i-01003b035d2988dfb) AND the QA runner `bd-gold-qa-runner` (i-0090b823a4a0997e3), which share the profile
  `bd-exporter-profile`. The grant is inert until act 2 moves the mode; the CTO's condition on the QA reach binds act 2's pair.
- **Plan:** `Plan: 1 to add, 0 to change, 0 to destroy`, one resource, name `advi-49f-platinum-canonical-rw-policy`, resolved bucket
  `opal-data-49financial` and prefix `advi/49financial/platinum/`, no Delete and no wildcard action. `evidence/act0/scoped_plan.out`.
- **Apply:** 13:43:23Z to 13:44:07Z, `Apply complete! Resources: 1 added, 0 changed, 0 destroyed.` `evidence/act0/apply_safe-apply.out`.
- **Gate note:** the cross-box seat gate read `open_deploy=hit verdict=STOP` (mode WARN, so it proceeded) for OPEN-DEPLOY
  `healgap-r3-act3-asset-dim-reattempt-20261011` (2.0.0_SA_COO~G1), which names the bd-pipeline root by token. The scoped plan of
  this act changed one resource and none of that entry's. This lane did not read the gate with `--dry-seat-gates` first.
- **AC1** PASS (the two Sids), **AC2** PASS (17), **AC3** literal FAIL by the invocation's `tail -n 6` window; the full plan reads
  `No changes. Your infrastructure matches the configuration.` at line 4 of 17. The order's status is not flipped by this lane.
- **Rollback, unused:** `aws iam delete-role-policy --role-name bd-exporter-ec2-role --policy-name advi-49f-platinum-canonical-rw-policy`.


## AC3 RE-RUN UNDER AMENDMENT 2 (0.7.0_AE_CloudOps~FB1, 2026-10-11T13:49:20Z)

The issuer amended AC3 to `... 2>&1 | grep -E "^(Plan:|No changes)"` (order @d7af35b8ca, msg 3902). Re-run 2026-10-11T13:48:41Z:
`No changes. Your infrastructure matches the configuration.` (1 matched line). AC1 PASS, AC2 PASS, AC3 PASS. The order's status is
flipped to `complete` in the commit that carries the updated proof instance. The 13:44Z reading under the original `tail -n 6`
window stays recorded above and in `evidence/act0/ac3_tail6_as_ordered.out`.
