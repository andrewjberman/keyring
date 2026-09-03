# Deploy Completion Record
**Date opened:** 2026-09-03T21:20:18.030252+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-1 limb 2 (FWD-1, scope ruled (A) on row Z-S80): ONE REQUEST authorizer requiring the CloudFront origin secret, attached to the 19 CloudFront-REACHABLE methods of f61h681z9g. The other 20 of 39 have NO CloudFront route and are a NAMED RESIDUAL, not served
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the REST authorizer Lambda source (reusing the limb-2a extracted module, never a second copy of the read), its Terraform, and the OpenAPI body change attaching the authorizer to the 19 reachable methods; committed under 0.7.0_AE_CloudOps~Z | commit hash + the 19/20 split printed |  | OPEN |
| L2 | verify | SCOPE PROOF before any apply: exactly 19 methods carry the authorizer in the body and exactly 20 do not, enumerated by path+verb, matching the CloudFront-reachability measurement in row Z-S80. A method outside the 19 carrying the authorizer is a STOP and a row | the two enumerated sets |  | OPEN |
| L3 | activation | build the REST authorizer via build-nodejs-lambda.sh and PROVE the extracted module is inlined in the artifact BEFORE applying (the limb-2a shape: download, recompute sha, unpack, module strings present in the bundle and absent from the entrypoint source) | artifact sha + the inlining measurement |  | OPEN |
| L4 | activation | THE ROLLBACK EXERCISED BEFORE IT IS RELIED ON, per deliverable 6: attach on ONE method, read it, DETACH, read it back to NONE, then attach the 19 -- ROLLBACK NAMED BEFORE THE APPLY: remove the authorizer from the body, re-apply, redeploy BOTH stages; both stages currently serve deployment 4ykw9p | both live reads plus the apply outputs |  | OPEN |
| L5 | verify | S1-AC3 AS AMENDED: get-authorizers reads exactly ONE; get-resources --embed methods (auto-paginated, no position key) reads the authorizer on 19 of 39 with BOTH denominators printed and the 20 out-of-reach stated with the reason; get-stages reads a NEW deploymentId on prod AND production, neither left on 4ykw9p | pasted before/after reads |  | OPEN |
| L6 | verify | THE PROBES: a refused GET and a refused OPTIONS at the raw address of BOTH stages; AMEND D's POSITIVE CONTROL, a preflight THROUGH CloudFront on a REACHABLE path that SUCCEEDS (a refusal there is a STOP and a rollback), and N/A-BY-CONSTRUCTION for the 20 since no browser path exists to preflight | exact invocations + captured responses |  | OPEN |
| L7 | verify | re-plan: portal-auth files UNVERIFIABLE-BY-INSTRUMENT per the S1-AC5 amendment; portfolio-management owes a REAL 0-diff; 0 destroy and 0 forces-replacement PLAN-WIDE on both; push state MEASURED with a positive control | plans + ls-remote |  | OPEN |

## Log

- 20260903T212018Z OPENED by 0.7.0_AE_CloudOps~Z with 7 leg(s)
