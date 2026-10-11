# Deploy Completion Record
**Date opened:** 2026-10-11T09:01:44.916752+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF CB-bj-1 re-run under AMENDMENT 1 (FWD-7): targeted apply of 2 IAM addresses on the renamed inline policy RestrictedPrefixGetPutList, under the re-signed pair
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 2: targeted plan saved outside the repo; print the planned ROLE name + Branch A gate | the role name must read cloudops-cot-restricted-breakglass-role, plus '2 to add, 0 to change, 0 to destroy' and no third address |  | OPEN |
| L2 | activation | step 3: apply THE SAVED PLAN via .tools/safe-apply.sh (the WORLD act) | the apply summary line; which branch ran; any gate refusal verbatim and NOT overridden |  | OPEN |
| L3 | verify | step 4 proof 1: get-role (one principal) + get-role-policy --policy-name RestrictedPrefixGetPutList (four actions) | both outputs |  | OPEN |
| L4 | verify | step 5 proof 2: untargeted PLAN ONLY, the two addresses both no-op | the BREAKGLASS-PLAN-AFTER line (the_two=2 the_two_changed=0) |  | OPEN |

## Log

- 20261011T090144Z OPENED by 0.7.0_AE_CloudOps~CB2 with 4 leg(s)
