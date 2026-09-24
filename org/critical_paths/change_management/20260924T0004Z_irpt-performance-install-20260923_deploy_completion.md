# Deploy Completion Record
**Date opened:** 2026-09-24T00:04:11.548716+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T001315Z
**Deploy:** Performance retained installation: native layer, two-family role, runtime handler
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | Saved plan f0a18919 via safe-apply | apply receipt: 3 add 1 change 0 destroy | Saved plan f0a189191e4f566f8cd76673ee8fb83f707f78c07e6f75dd7bad1a7d2b247a55 applied via safe-apply from irpt-smoke-p-backend-20260923 at 2026-09-24T00:07:15Z under CTO GO 99821: 3 added (irpt-performance-native-layer:1, irpt-performance-retained-policy, irpt-performance-adapter-selection-read-policy), 1 changed (irpt-performance-adapter), 0 destroyed; halt gate 22 routine acknowledged, naming/tagauthz/tombstone gates clean; apply-2.log | CLOSED 20260924T001210Z |
| V1 | verify | Live function, layer version, policies, zero-diff | readback JSON + post-install plan rc 0 | Postflight 00:07:33Z 7/7 OK: CodeSha256 JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk= (== artifact h.hlJhL3), runtime.lambda_handler 120s 1536MB Active/Successful, layers irpt-common:5 + irpt-performance-native-layer:1 (content sha EhuEB0Fc...), both policies present, post-install plan rc 0 No changes, state serial 17; PERFORMANCE_INSTALL_APPLY_20260924.json | CLOSED 20260924T001210Z |
| R1 | git | Exact-function recorder | record-terraform-deploy commit hash | record-terraform-deploy.sh exact-function record committed ac8e2cf502 on irpt-smoke-p-backend-20260923: irpt-performance-adapter last_deployed_commit 068e9ccd85, last_deployed_at 2026-09-24T00:09:07Z, deployed_code_sha256 JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk=, deploy_ledger d4c37ad495; CHANGELOG untagged-d4c37ad4 | CLOSED 20260924T001315Z |

## Log

- 20260924T000411Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260924T001210Z LEG A1 closed: Saved plan f0a189191e4f566f8cd76673ee8fb83f707f78c07e6f75dd7bad1a7d2b247a55 applied via safe-apply from irpt-smoke-p-bac
- 20260924T001210Z LEG V1 closed: Postflight 00:07:33Z 7/7 OK: CodeSha256 JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk= (== artifact h.hlJhL3), runtime.lam
- 20260924T001315Z LEG R1 closed: record-terraform-deploy.sh exact-function record committed ac8e2cf502 on irpt-smoke-p-backend-20260923: irpt-performance
- 20260924T001315Z CLOSED -- all 3 legs proven
