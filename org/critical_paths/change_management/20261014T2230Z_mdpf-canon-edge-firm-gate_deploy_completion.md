# Deploy Completion Record
**Date opened:** 2026-10-14T22:30:57.420133+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-q-1 (order ADHOC.canon-q1-edge-firm-gate-deploy, crossbox XB-20261014T222322Z-3242, issuer 2.0.0_SA_COO~D1, CTO ruling XA-20261014T204823Z-c7cd): publish a new version of Lambda@Edge auth-validator-edge (us-east-1) carrying the per-firm MDPF leaf gate and re-point CloudFront distribution EVTSA9VEHNZVH's viewer-request associations to it. ARTIFACT s3://opal-313476888478-lambda-artifacts/portal-auth/auth-validator-edge.zip (current object version recorded at L1 as the rollback copy). PIN 643932fee0 (CN-q-1 drain merge on box/dell1). FUNCTION auth-validator-edge, deployed version 23 on 27 of the 30 behaviors (the issuer's count; re-measured at L1). ROOT infra/aws/terraform/portal-auth, S3-backed function (lambda-edge.tf:78-97), publish=true. PLAN-IS-NO-OP TRAP: the proof is the live association ARN per behavior (L5a), not the plan. ROLLBACK (fast): set local.auth_validator_edge_arn in cloudfront-distribution.tf to the literal ARN of version 23, commit, plan, safe-apply targeted to the distribution, wait Deployed, read the 27 associations back at :23; slow: revert, rebuild, upload, apply. The prior artifact version is the rollback copy and is never deleted. It narrows access for non-internal logins only; no S3 object write, so no never-widen pair (CTO msg 5913).
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions a-e: pin ancestry with controls, mdpfGate export and mdpf_scope_denied once at the pin, the three r9_cn_q_1 checks, open-sentinel census over every worktree, comp-schedule drift, clean pre-plan of portal-auth | each printed; any false = do nothing and report |  | OPEN |
| L1 | verify | BEFORE print: function config and versions, artifact current version and rollback copy hash, distribution behaviors and auth-validator-edge associations with denominators, CustomErrorResponses, baseline GETs and the service account claims | prints attached |  | OPEN |
| L2 | s3-prefix | build from the pin tree and upload; bundle holds mdpf_scope_denied once and aggregate_denied once; new version content-sha256 equals the zip hash before planning | zip sha256, version id, bundle counts |  | OPEN |
| L3 | verify | saved portal-auth plan moves only the function code, the 27 association ARNs and at most the recorded WAF churn | plan text saved, summary line |  | OPEN |
| L4 | activation | safe-apply of the SAVED plan, wait for distribution Deployed, record the new version N | apply line, N, Deployed |  | OPEN |
| L5 | verify | proofs a to e: live association per behavior at N and none at 23, no-token GETs 401, internal read, deployed-bundle synthetic-claim matrix, rollback readiness (version 23 answers with its before CodeSha256), after print | each printed |  | OPEN |

## Log

- 20261014T223057Z OPENED by 0.7.0_AE_CloudOps~U7 with 6 leg(s)
