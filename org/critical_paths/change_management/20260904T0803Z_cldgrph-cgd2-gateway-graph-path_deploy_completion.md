# Deploy Completion Record
**Date opened:** 2026-09-04T08:03:36.792287+00:00
**Status:** OPEN
**Deploy:** NFRA_CLDGRPH CG-s-5: the gateway traversal -- globgrph integration (dormant) + the /graph/* static-capability path, secret+IAM+ALB rule, deployed to i-07dccb1615503ac99
**Authored by:** 0.9.0_WK_NFRA_CLDGRPH~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-NFRA_CLDGRPH-2 worker-branch commit of the gateway app + terraform + deploy script | commit hash (LOCAL, worker branch; never pushed) |  | OPEN |
| L2 | activation | Secrets Manager secret opal/mcp/graph-read-token created out-of-band (value never in TF state, repo or log) | live describe-secret ARN read |  | OPEN |
| L3 | activation | targeted terraform apply: aws_iam_role_policy.gw_graph_read_secret_read + aws_lb_listener_rule.graph_capability | apply output + live aws iam get-role-policy and elbv2 describe-rules |  | OPEN |
| L4 | ec2-baked-asset | gateway code on i-07dccb1615503ac99 via safe-ec2-deploy.sh (S3->SSM) | SSM on-box md5 of the RUNNING /opt/opal-gateway files + unit active |  | OPEN |
| L5 | verify | the exercise: this seat POSTs /graph/cypher over HTTPS (200 + vintage) and the no-bearer control (401); box /graph/health 200 | the recorded HTTP responses |  | OPEN |
| L6 | verify | ONE unscoped terraform plan asserted BY ADDRESS LIST to contain none of this order's addresses | saved plan file + the address assertion output |  | OPEN |

## Log

- 20260904T080336Z OPENED by 0.9.0_WK_NFRA_CLDGRPH~2 with 6 leg(s)
