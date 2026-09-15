# Deploy Completion Record
**Date opened:** 2026-09-15T03:34:02.720139+00:00
**Status:** OPEN
**Deploy:** LGIC_ENFORCE fence on opal-data-49financial
**Authored by:** 0.9.0_WK_LGIC_ENFORCE~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the authored change committed | commit hash | 080e1b97c6 (branch wk-lgic-enforce-1-1-f1, LOCAL): exemptions.json 16 rows, module opal_name fence_exemption_arns, s3-49financial.tf scope-derived Deny, lgic-enforce-fence-probes.tf; plan 6 add / 1 change / 0 destroy | CLOSED 20260915T040400Z |
| L2 | activation | safe-apply shared-infra: the policy + 3 probe roles -- ROLLBACK: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PRIOR_POLICY.json | apply output + changed-resource list |  | OPEN |
| L3 | verify | the four probe arms | FENCE_PROBES.md |  | OPEN |
| L4 | verify | probe roles removed + re-plan 0-diff | get-role NoSuchEntity x3 + plan |  | OPEN |

## Log

- 20260915T033402Z OPENED by 0.9.0_WK_LGIC_ENFORCE~1 with 4 leg(s)
- 20260915T040400Z LEG L1 closed: 080e1b97c6 (branch wk-lgic-enforce-1-1-f1, LOCAL): exemptions.json 16 rows, module opal_name fence_exemption_arns, s3-49

## Sign-off (gate G-E; never-widen, NEVER #1)

The packet is `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PLAN.md`; the rollback is
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PRIOR_POLICY.json`. Each seat writes ONE line in its slot below,
in the form `SIGNOFF <serial> <YYYYMMDDTHHMMSSZ> <scope>`, before leg L2 is run. The author of this entry writes neither.

1.0.0_SA_CTO:
SIGNOFF 1.0.0_SA_CTO 20260915T072924Z scope: the act EN-f-2 performs -- ONE safe-apply of infra/aws/terraform/shared-infra/ per FENCE_PLAN.md s.1, exactly the 7 changes listed there (aws_s3_bucket_policy.opal_data_49financial to Deny s3:* where aws:PrincipalArn is ArnNotLike role/*-49f-* and the 16 exemption ARNs; 3 fenceprobe roles and their 3 inline read policies), and nothing else -- a plan with any other change stops the apply; conditions: (1) the applying identity is one of the 2a exempt principals, printed before apply; (2) the probe window is bounded -- L3 runs and L4 removes the 3 probe roles in the same session, no later than 1h after L2 lands, because the probe roles trust the account root and mdpf-49f-fenceprobe-role can read this bucket until L4; (3) any L3 arm reading otherwise, or any AccessDenied on a 2a principal, rolls the policy back from FENCE_PRIOR_POLICY.json and keeps the ledger OPEN (FENCE_PLAN s.4 branches A-B); writers cross-checked by this seat with a second instrument, the repo Terraform (9 files naming opal-data-49financial): mdpf-pipeline/iam.tf's 49F-dims grant is already removed and its role mdpf-daily-runner-ec2-role is denied before and after (unchanged); bd-pipeline/iam.tf AdviChainGoldRW/CodeRead/49fListScoped are bd-exporter-ec2-role's (exempt); advi_49f_floor.tf's advi-49f-* is undenied before and after; advi_stitch_landing.tf's role is exempt -- no principal outside the census loses access; the account root is narrowed, with recovery by root policy replacement

2.0.0_SA_COO~G:
SIGNOFF 2.0.0_SA_COO~G 20260915T070844Z scope: the act EN-f-2 performs -- ONE safe-apply of infra/aws/terraform/shared-infra/ per FENCE_PLAN.md s.1, 7 changes: aws_s3_bucket_policy.opal_data_49financial updated to Deny s3:* where aws:PrincipalArn is ArnNotLike 1 derived pattern (role/*-49f-*) and 16 exemption ARNs, and 3 probe roles with 3 inline read policies created; writers of access to opal-data-49financial counted: 16 live IAM grants (census, all exempt, unchanged), 0 AWS service principals delivering into it (live graph 05:56:10Z: 3 nodes, 0 event notifications; repo: 0 logging/replication/inventory/notification targets), 1 declared role family advi-49f-* (derived pattern; denied neither before nor after); narrows every other principal, the account root included (recovery: root may replace the policy); rollback per key: FENCE_PRIOR_POLICY.json via put-bucket-policy and the L1 revert, probes via L4; the applying identity must be an exempt 2a principal

