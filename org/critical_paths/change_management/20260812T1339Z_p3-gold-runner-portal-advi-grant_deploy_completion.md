# Deploy Completion Record
**Date opened:** 2026-08-12T13:39:49.851579+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260812T135539Z
**Deploy:** P3 IAM leg: consolidation-gold-runner-role ADDITIVE grant on portal/gold/advi/49financial (Get+Put+conditioned List) -- old schwab/08335338/gold grant RETAINED; unblocks DS's code re-point
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted safe-apply of the 3 statement adds (Get/Put/List-condition) on aws_iam_role_policy.gold_runner_inline | apply output + targeted replan -detailed-exitcode rc=0 | targeted plan: 'Plan: 0 to add, 1 to change, 0 to destroy'; plan detail read line-by-line = THREE '+' lines only (Get Resource, Put Resource, List s3:prefix), ZERO '-' lines -- schwab/08335338/gold/* retained on both Get and Put and in the List condition. safe-apply complete; targeted replan -detailed-exitcode rc=0 | CLOSED 20260812T135444Z |
| L2 | verify | APPLIED truth: live get-role-policy shows the new Resource on BOTH Get and Put AND the new s3:prefix in the List Condition, with the OLD schwab/08335338/gold entries still present | aws iam get-role-policy read | APPLIED truth, live get-role-policy on consolidation-gold-runner-inline: ReadGoldInputsAndCode Resource now 4 entries incl portal/gold/advi/49financial/*; WriteGoldAndRunlog Resource now 2 entries incl the same; ListMonolithScoped Condition StringLike s3:prefix now 4 entries incl portal/gold/advi/49financial/*. OLD schwab/08335338/{silver,gold} + code/consolidation-gold entries ALL still present (additive verified at rest, not inferred from the plan) | CLOSED 20260812T135444Z |
| L3 | verify | EXERCISED: simulate-principal-policy PutObject on the exact P3 key = allowed (was implicitDeny), ONE --resource-arns per call + isolated positive control + the PLATINUM FENCE re-asserted implicitDeny | three separate simulate invocations | EXERCISED, five SEPARATE invocations, ONE --resource-arns each: (1) PutObject portal/gold/advi/49financial/gold/canonical/dim_account/... = ALLOWED (DS measured implicitDeny pre-apply); (2) GetObject .../account_gains/... = ALLOWED (the gold-reads-gold edge COO's re-spec required); (3) ListBucket on the bucket WITH --context-entries s3:prefix=portal/gold/advi/49financial/gold/canonical/ = ALLOWED (context passed deliberately -- a conditioned statement returns a FALSE implicitDeny without it, Rule 22a mode 2). DISCRIMINATING NEGATIVES, both isolated: (4) PutObject schwab/08335338/platinum/* = implicitDeny -- the PLATINUM FENCE survives the widening; (5) PutObject portal/gold/advi/someotherfirm/* = implicitDeny -- the one-scope pin holds, other advisors remain unreachable. 4+5 prove the instrument discriminates for this principal | CLOSED 20260812T135444Z |
| L4 | git | TF committed (locals + 3 statements + the amended policy grammar comment) | commit hash | committed @b6e5cf9c2f (main.tf portal_gold_out_prefix local + runner-iam.tf three statement adds + the amended WriteGoldAndRunlog grammar comment) | CLOSED 20260812T135539Z |

## Log

- 20260812T133949Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260812T135444Z LEG L1 closed: targeted plan: 'Plan: 0 to add, 1 to change, 0 to destroy'; plan detail read line-by-line = THREE '+' lines only (Get Re
- 20260812T135444Z LEG L2 closed: APPLIED truth, live get-role-policy on consolidation-gold-runner-inline: ReadGoldInputsAndCode Resource now 4 entries in
- 20260812T135444Z LEG L3 closed: EXERCISED, five SEPARATE invocations, ONE --resource-arns each: (1) PutObject portal/gold/advi/49financial/gold/canonica
- 20260812T135539Z LEG L4 closed: committed @b6e5cf9c2f (main.tf portal_gold_out_prefix local + runner-iam.tf three statement adds + the amended WriteGold
- 20260812T135539Z CLOSED -- all 4 legs proven
