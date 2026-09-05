# Deploy Completion Record
**Date opened:** 2026-09-03T18:38:01.919147+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T190605Z
**Deploy:** NFRA_CLDGRPH CG-s-4 verified projection serving plane
**Authored by:** 0.7.0_AE_CloudOps~T
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-globgrph-derive-runner image with /app/projection_server.py | CodeBuild SUCCEEDED and ECR digest recorded | CodeBuild globgrph-derive-build:72336fae-740c-491b-a962-e44bc76bd925 SUCCEEDED; ECR latest/20260903-183958 digest sha256:68c822ff9cc4784f6fa8eb83fcde513f6ef1a1659f0220f44a2b78c9fcbd12b5 (source HEAD ab38d89f34; C1 commit 8f0dff109f ancestor; intervening commit changed no COPY source) | CLOSED 20260903T184046Z |
| L2 | activation | seven CG-s-4 Terraform resources | safe-apply targeted result adds-only with no change or destroy | safe-apply consumed saved seven-address targeted plan: Apply complete! Resources: 7 added, 0 changed, 0 destroyed; task definition globgrph-serving:1, service arn:aws:ecs:us-east-1:313476888478:service/opal-globgrph/globgrph-serving, SG sg-0e85dd853fbe5584e | CLOSED 20260903T184203Z |
| L3 | verify | Terraform and applied serving task IAM | one unscoped re-plan names exactly four known foreign addresses and no C1 address; refreshed applied IAM equals V2(ii) | ONE unscoped plan saved as c1-unscoped.tfplan: exactly aws_glue_partition.tool_activity[rolling_log]=update, [rolling_log_summary]=update, [routing]=create, aws_sns_topic_subscription.critical_surface_alerts_email=create; saved-plan JSON assertions ASSERT_EXACT_FOUR=PASS and ASSERT_NO_C1=PASS. comp-iam census refreshed 2026-09-03T18:43:46Z (221 roles); applied IAM direct read is one inline GlobgrphServingReadOnly, zero attached, exactly s3:GetObject/ListBucket/GetBucketLocation on bucket+projection/* and log writes on /ecs/globgrph-serving:*. | CLOSED 20260903T184511Z |
| L4 | verify | projection.opal-globgrph.local:8181 current query | non-service VPC caller returns rows and pointer-equal vintage with RTT | SSM command 2e708112-9eec-44ef-9e65-4eeded137343 on non-service gateway i-07dccb1615503ac99/ip-172-31-89-135 at 2026-09-03T18:46:14Z: DNS 172.31.9.108; MATCH (n) RETURN count(n) AS nodes -> rows nodes=27225, vintage 2026-09-03T17:01:08.128628+00:00 equal to fresh projection/current.json, age_line+manifest SHA+prefix present, HTTP 200 RTT 0.026205s; health HTTP 200 RTT 0.002202s. | CLOSED 20260903T184633Z |
| L5 | verify | forward swap plus backward refusal | real pointer advance served without restart and health swap time; planted backward pointer refused unchanged | C2 writer task f8b288ad95ec42dab2d17ef5a33cbd29 advanced projection/current.json to vintage 2026-09-03T19:02:18.412096+00:00 manifest 751b870534c474298e0e968390f143e325b4741a4a4fc471c3bf341cd39c0b58. Gateway SSM command 62213ecc-b319-4d23-b91b-37e765b0f2fc returned HTTP 200 and nodes=27225 from that vintage. C1 task ARN arn:aws:ecs:us-east-1:313476888478:task/opal-globgrph/c18ee8b40e4a4bf3993f8f78cc2f98a6 and startedAt 1788460967.358 were unchanged; health last_swap=2026-09-03T19:03:42.191303+00:00. Post-advance backward-pointer seam refused candidate 2026-09-03T17:01:08.000000+00:00, made LOADER_CALLS=0, and retained served vintage 2026-09-03T18:01:08.000000+00:00. | CLOSED 20260903T190601Z |

## Log

- 20260903T183801Z OPENED by 0.7.0_AE_CloudOps~T with 5 leg(s)
- 20260903T184046Z LEG L1 closed: CodeBuild globgrph-derive-build:72336fae-740c-491b-a962-e44bc76bd925 SUCCEEDED; ECR latest/20260903-183958 digest sha256
- 20260903T184203Z LEG L2 closed: safe-apply consumed saved seven-address targeted plan: Apply complete! Resources: 7 added, 0 changed, 0 destroyed; task 
- 20260903T184511Z LEG L3 closed: ONE unscoped plan saved as c1-unscoped.tfplan: exactly aws_glue_partition.tool_activity[rolling_log]=update, [rolling_lo
- 20260903T184633Z LEG L4 closed: SSM command 2e708112-9eec-44ef-9e65-4eeded137343 on non-service gateway i-07dccb1615503ac99/ip-172-31-89-135 at 2026-09-
- 20260903T190601Z LEG L5 closed: C2 writer task f8b288ad95ec42dab2d17ef5a33cbd29 advanced projection/current.json to vintage 2026-09-03T19:02:18.412096+0
- 20260903T190605Z CLOSED -- all 5 legs proven
