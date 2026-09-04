# Deploy Completion Record
**Date opened:** 2026-09-04T12:32:00.153024+00:00
**Status:** OPEN
**Deploy:** IAM grant s3:GetBucketNotification to PRINCIPAL arn:aws:iam::313476888478:role/opal-globgrph-derive-runner-task (NFRA_CLDGRPH CG-s-16, TO-CG-D-12); reaches 34 account buckets
**Authored by:** 0.9.0_WK_NFRA_CLDGRPH~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/globgrph/iam.tf on branch wk-NFRA_CLDGRPH-1 | commit hash of the one-action grant |  | OPEN |
| L2 | activation | terraform apply targeted on the one IAM address in root infra/aws/terraform/globgrph | apply summary line quoted + unscoped plan control by address list |  | OPEN |
| L3 | verify | iam simulate-principal-policy on the live role | allowed + >=1 MatchedStatements for s3:GetBucketNotification, one ARN per call, PLUS implicitDeny on the write twin s3:PutBucketNotification |  | OPEN |
| L4 | verify | one ad-hoc ECS derive on image sha256:1b89853fe44133f10a60dc2b3e7b463c0d3b68b827a2ddff249bf427ecde2778 | derive exit 0 and its log printing s3 notifications buckets read=34 / buckets unreadable=0 |  | OPEN |
| L5 | verify | served projection at projection.opal-globgrph.local:8181 at the post-derive vintage | TRIGGERS count > 0 and the three declared bd-pipeline targets present |  | OPEN |

## Log

- 20260904T123200Z OPENED by 0.9.0_WK_NFRA_CLDGRPH~1 with 5 leg(s)

## The IAM act: its PRINCIPAL and the BUCKETS it reaches (NEVER-2, IAM limb)

- **Principal (the ONLY principal this entry moves):** `arn:aws:iam::313476888478:role/opal-globgrph-derive-runner-task`
  (the globgrph derive-runner ECS task role; assumed by `ecs-tasks.amazonaws.com` only, task family `globgrph-derive-runner`).
- **Action added:** `s3:GetBucketNotification` -- ONE action, read-only, no write twin, no `s3:*`, no managed policy, no other principal, no bucket policy.
- **Resource in the grant:** `*` (the scope of the role's sibling account-wide reads).
- **Reach, enumerated (34 buckets = every bucket the derive's own `ListAllMyBuckets` returned and then failed to read on 2026-09-04T08:49Z, log stream `derive-runner/derive-runner/7286e56c80614ab49fa2fba791bb8b43`):**

   1. `opal-313476888478-globgrph`
   2. `opal-313476888478-lambda-artifacts`
   3. `opal-313476888478-lambda-layers`
   4. `opal-313476888478-terraform-state`
   5. `opal-313476888478-yang-qa-scratch`
   6. `opal-cloudtrail-logs-313476888478`
   7. `opal-cur-313476888478`
   8. `opal-data-49financial`
   9. `opal-data-assets`
  10. `opal-data-astn`
  11. `opal-data-bd`
  12. `opal-data-cot`
  13. `opal-data-demo`
  14. `opal-data-etfs`
  15. `opal-data-imo`
  16. `opal-data-inf`
  17. `opal-data-mdpf`
  18. `opal-data-news-av`
  19. `opal-data-news-v2`
  20. `opal-data-pm`
  21. `opal-data-portal-v2`
  22. `opal-data-portfolio`
  23. `opal-data-security`
  24. `opal-data-security-access-logs`
  25. `opal-data-trade-submissions`
  26. `opal-estate-report`
  27. `opal-infrastructure-snapshots`
  28. `opal-mcp-athena-results`
  29. `opal-mcp-audit`
  30. `opal-runner-shared`
  31. `opal-security-evidence`
  32. `opal-served-key-write-trail-logs`
  33. `opal-website-backups`
  34. `opalinvest-portal`

  DENOMINATOR: 34 of 34 buckets the derive enumerated; `read=0 / unreadable=34` before this act.
- **Blast radius:** the derive role only. No other role, user or service principal is modified by this entry.

