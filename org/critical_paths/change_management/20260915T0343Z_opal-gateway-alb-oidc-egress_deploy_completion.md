# Deploy Completion Record
**Date opened:** 2026-09-15T03:43:30.323874+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260915T040635Z
**Deploy:** Approved ALB OIDC HTTPS egress repair; Andrew-direct cfcb13e03f item 1 and CTO Msg96866; one in-place SG update only; no push or merge
**Authored by:** 1.0.0_SA_CTO~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | alb.tf alone on CLOUD LOCAL under audited CLOUD_OPS_OR_ETL lane override | verified local commit hash and exact pathset; push held | Repository-verified local commit d9d51fc43d, exact path infra/aws/terraform/opal-gateway/alb.tf alone; author and committer 1.0.0_SA_CTO~A. Audited single-commit CLOUD_OPS_OR_ETL override directed by CTO Msg96866. Terraform fmt and scoped commit gates passed. CLOUD push and SITEZ merge remain held; LOCAL is the approved git boundary. | CLOSED 20260915T035415Z |
| L2 | activation | sg-02571ff2f33d2f9d4 gains TCP443 to 0.0.0.0/0 alongside existing TCP8080 VPC egress | saved-plan safe-apply rc0; exactly 0 add 1 in-place change 0 destroy | CTO Msg96877 authorized exact saved SG-only plan SHA256 00715c0dac2a7f5481d06e8fd352ac247531f94681ae85feafe568207c9d5a2b. Canonical safe-apply rc0: 0 added, 1 changed, 0 destroyed; only aws_security_group.alb egress. ALB_EGRESS/APPLIED.json and safe-apply.txt contain apply receipt and live readback. Ingress unchanged. Two WAF description-only differences remain deliberately unapplied under Msg96877; full-tree zero diff is not claimed. | CLOSED 20260915T040413Z |
| L3 | verify | live ALB SG and Terraform postcondition | describe-security-groups has both exact rules and re-plan has no changes | Live describe-security-groups on sg-02571ff2f33d2f9d4 verified TCP443 to 0.0.0.0/0 and preserved TCP8080 to 172.31.0.0/16, ingress unchanged (ALB_EGRESS/APPLIED.json). SG-only re-plan at 2026-09-15T04:04:12Z exited 0, managed_changes empty, changed_attributes empty (ALB_EGRESS/sg-only-after-apply-summary.json). The scoped pre-apply one-update flag stop_condition_clear is false on this zero-update postplan by design; rc0 and empty changes prove zero diff. Known deliberately unapplied full-tree differences: descriptions only on empty WAF IPv4 and IPv6 IP sets, per CTO Msg96877. | CLOSED 20260915T040446Z |
| L4 | verify | Andrew signs in to https://mcp.opalinvest.dev/sprint | report visible; ALB callback without AuthTokenEp error; ELBAuthSuccess above zero | EXERCISED: Andrew answered Report loads after prompt to open fresh https://mcp.opalinvest.dev/sprint and sign in (ALB_EGRESS/USER_VERIFICATION.md). At 04:05:37Z, CloudWatch ELBAuthSuccess is 1 in post-apply 04:04Z minute. ALB callback /oauth2/idpresponse at 04:04:58.944981Z returned 302, authenticate, error_reason=-. Delivered post-apply window: 11 requests, 0 parse errors, 0 AuthTokenEp errors, latest request 04:04:59Z. ALB_EGRESS/POST_APPLY_OBSERVATION.json contains bounded live proof. Report-visible confirmation is user supplied; log delivery can lag. | CLOSED 20260915T040635Z |

## Log

- 20260915T034330Z OPENED by 1.0.0_SA_CTO~A with 4 leg(s)
- 20260915T035415Z LEG L1 closed: Repository-verified local commit d9d51fc43d, exact path infra/aws/terraform/opal-gateway/alb.tf alone; author and commit
- 20260915T040413Z LEG L2 closed: CTO Msg96877 authorized exact saved SG-only plan SHA256 00715c0dac2a7f5481d06e8fd352ac247531f94681ae85feafe568207c9d5a2b
- 20260915T040446Z LEG L3 closed: Live describe-security-groups on sg-02571ff2f33d2f9d4 verified TCP443 to 0.0.0.0/0 and preserved TCP8080 to 172.31.0.0/1
- 20260915T040635Z LEG L4 closed: EXERCISED: Andrew answered Report loads after prompt to open fresh https://mcp.opalinvest.dev/sprint and sign in (ALB_EG
- 20260915T040635Z CLOSED -- all 4 legs proven
