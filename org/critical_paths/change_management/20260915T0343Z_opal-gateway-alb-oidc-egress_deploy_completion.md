# Deploy Completion Record
**Date opened:** 2026-09-15T03:43:30.323874+00:00
**Status:** OPEN
**Deploy:** Approved ALB OIDC HTTPS egress repair; Andrew-direct cfcb13e03f item 1 and CTO Msg96866; one in-place SG update only; no push or merge
**Authored by:** 1.0.0_SA_CTO~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | alb.tf alone on CLOUD LOCAL under audited CLOUD_OPS_OR_ETL lane override | verified local commit hash and exact pathset; push held | Repository-verified local commit d9d51fc43d, exact path infra/aws/terraform/opal-gateway/alb.tf alone; author and committer 1.0.0_SA_CTO~A. Audited single-commit CLOUD_OPS_OR_ETL override directed by CTO Msg96866. Terraform fmt and scoped commit gates passed. CLOUD push and SITEZ merge remain held; LOCAL is the approved git boundary. | CLOSED 20260915T035415Z |
| L2 | activation | sg-02571ff2f33d2f9d4 gains TCP443 to 0.0.0.0/0 alongside existing TCP8080 VPC egress | saved-plan safe-apply rc0; exactly 0 add 1 in-place change 0 destroy |  | OPEN |
| L3 | verify | live ALB SG and Terraform postcondition | describe-security-groups has both exact rules and re-plan has no changes |  | OPEN |
| L4 | verify | Andrew signs in to https://mcp.opalinvest.dev/sprint | report visible; ALB callback without AuthTokenEp error; ELBAuthSuccess above zero |  | OPEN |

## Log

- 20260915T034330Z OPENED by 1.0.0_SA_CTO~A with 4 leg(s)
- 20260915T035415Z LEG L1 closed: Repository-verified local commit d9d51fc43d, exact path infra/aws/terraform/opal-gateway/alb.tf alone; author and commit
