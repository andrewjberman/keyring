# Service-Linked Role Review — role-by-role (Andrew-requested 2026-07-30)

Live-usage probes run 2026-07-30 ~14:5xZ (rc + counts in census session record). Note the built-in
safety: **IAM refuses to delete an SLR while its service still has resources** — so a DELETE verdict
here is double-checked by AWS itself at execution time. Deletion is via
`aws iam delete-service-linked-role --role-name <name>` (async, returns a deletion-task id).

| # | Role | Service | Live usage measured | Verdict |
|---|---|---|---|---|
| 1 | AWSServiceRoleForRDS | RDS | 0 instances, 0 clusters | **DELETE** (also orphans rds og/pg/subgrp relics) |
| 2 | AWSServiceRoleForAmazonOpenSearchService | OpenSearch | 0 domains | **DELETE** |
| 3 | AWSServiceRoleForAmazonOpenSearchServerless | AOSS | 0 collections | **DELETE** |
| 4 | AWSServiceRoleForSMSVoice | Pinpoint SMS-Voice | 0 phone numbers | **DELETE** |
| 5 | AWSServiceRoleForECS | ECS | 1 cluster, 2 services (globgrph-nessie etc.) | KEEP |
| 6 | AWSServiceRoleForElasticLoadBalancing | ELB | 1 load balancer | KEEP |
| 7 | AWSServiceRoleForCloudFrontLogger | CloudFront logging | 1 live distribution | KEEP |
| 8 | AWSServiceRoleForAPIGateway | API Gateway | 5 HTTP APIs + 1 REST API live | KEEP |
| 9 | AWSServiceRoleForLambdaReplicator | Lambda@Edge | replicas live (us-east-2 edge log groups prove execution) | KEEP |
| 10 | AWSServiceRoleForResourceExplorer | Resource Explorer | 2 indexes (used by this census) | KEEP |
| 11 | AWSServiceRoleForSupport | AWS Support | AWS-mandatory | CANNOT-DELETE |
| 12 | AWSServiceRoleForTrustedAdvisor | Trusted Advisor | AWS-mandatory | CANNOT-DELETE |

**Net: 4 DELETE / 6 KEEP / 2 CANNOT.** The 4 deletes are also the tombstones of the abandoned-service
archaeology (RDS/OpenSearch/AOSS/SMSVoice all measured dead); deleting them removes the last
misleading evidence that those services are in use.
