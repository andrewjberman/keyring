# Deploy Completion Record
**Date opened:** 2026-09-03T08:16:37.950743+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T085928Z
**Deploy:** NFRA_OPSEC202609 TO-OP-S-3: origin secret on both gateway origins + required by auth-handler and portal-authorizer
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ lane commit of the TF + both consumers | commit hash, push state MEASURED (LOCAL expected, integrator pushes) | Lane commit 7abe7552b5 (author 0.7.0_AE_CloudOps~Z), 10 files / 687 insertions: the 3 portal-auth .tf, originVerify.ts + index.ts, index.mjs, lambda-source-map.json, the channel row Z-S10, the rotation runbook and this ledger. Verified against the REPOSITORY not the tool's stdout: git log -1 7abe7552b5 returns the subject and author, with a bogus-hash negative control failing as required. PUSH STATE MEASURED: LOCAL -- not an ancestor of origin/SITEZ, the expected reading under LD-0367 / GATE 5; 0.0.0_AB_MSTR~Z integrates. | CLOSED 20260903T085928Z |
| L2 | activation | mint opal/auth/origin-verify out of band (two slots) + terraform import of the container | describe-secret returns the ARN AND terraform state show lists the resource | Secret minted OUT OF BAND (value never printed, never in argv, local plaintext copy removed) and IMPORTED, per the module's documented convention at secrets.tf:9-11. ARN arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/auth/origin-verify-Pe97BM (suffix Pe97BM = 6 chars, matches the ?????? pattern in both IAM grants). terraform import rc=0, 'Import successful!'; data.aws_secretsmanager_secret_version.origin_verify Read complete. Two slots {current,previous}; current = 48 urlsafe bytes (~384 bits). | CLOSED 20260903T082706Z |
| L3 | activation | safe-apply on portal-auth: custom_header on the 2 gateway origins + the authorizer IAM grant | apply completes and a re-plan reads 0-diff | safe-apply (HALT_ACK=1 after reading the 12d-old routine base-inbox message in full; it is a withdrawn-TO notice that says in terms 'neither is a gate'). Apply complete: 1 added, 3 changed, 0 DESTROYED, rc=0. PRE-CHANGE plan exhibited the cloudfront-distribution.tf:5 import bound with -detailed-exitcode = 0 ('No changes. Your infrastructure matches the configuration'). POST-APPLY re-plan -detailed-exitcode = 0 (0-diff). Diff surface was exactly 4 resources, nothing riding: distribution in-place, auth_permissions in-place, portal_authorizer_origin_verify created, secret in-place (tags/import defaults only). | CLOSED 20260903T082706Z |
| L4 | activation | opalinvest-auth-handler code deploy (origin gate) | live CodeSha256 equals the built artifact sha | opalinvest-auth-handler live CodeSha256 = 5XvFxdr07h4AxhWMVPrkgFVD9g5NCRf2HbtJ1Q0jUYw= == the sha printed by build-nodejs-lambda.sh for the uploaded zip. State Active / LastUpdateStatus Successful. Deployed AFTER the distribution read Status=Deployed, so the header was already propagated to every edge before any consumer began requiring it. | CLOSED 20260903T084245Z |
| L5 | activation | opal-portal-authorizer code deploy (origin gate) | live CodeSha256 equals the built artifact sha | opal-portal-authorizer live CodeSha256 = RvHb6Lj55WjOKCvBAkxQvKIXEEl5jdZfhyT1AY6ZEf4= == the built sha. State Active / LastUpdateStatus Successful. Both functions carry the TTL'd-cache fix; an earlier build pair (K4a25xu.../P5l9MyW...) was superseded in-session after the unbounded cache was found to break the rotation this secret exists to support. | CLOSED 20260903T084245Z |
| L6 | verify | live distribution carries the header on both gateway origins + IAM reads allowed | get-distribution-config with the origin denominator printed, and simulate-principal-policy allowed on both roles | LIVE get-distribution AFTER apply: Status=Deployed, ORIGIN DENOMINATOR 7, APIGateway-portal and APIGateway-portfolio each HeaderCount=1 name X-Opal-Origin-Verify, all 5 S3 origins HeaderCount=0 (never-widen holds). IAM measured on the REAL ARN opal/auth/origin-verify-Pe97BM, one --resource-arns per call, each control its own invocation: opalinvest-auth-lambda-role allowed, opal-portal-lambda-role allowed; both read implicitDeny BEFORE the grant, with a role-specific positive control allowed on each, so the instrument could fail and did. Final terraform re-plan -detailed-exitcode = 0. | CLOSED 20260903T084245Z |

## Log

- 20260903T081637Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)
- 20260903T082706Z LEG L2 closed: Secret minted OUT OF BAND (value never printed, never in argv, local plaintext copy removed) and IMPORTED, per the modul
- 20260903T082706Z LEG L3 closed: safe-apply (HALT_ACK=1 after reading the 12d-old routine base-inbox message in full; it is a withdrawn-TO notice that sa
- 20260903T084245Z LEG L4 closed: opalinvest-auth-handler live CodeSha256 = 5XvFxdr07h4AxhWMVPrkgFVD9g5NCRf2HbtJ1Q0jUYw= == the sha printed by build-nodej
- 20260903T084245Z LEG L5 closed: opal-portal-authorizer live CodeSha256 = RvHb6Lj55WjOKCvBAkxQvKIXEEl5jdZfhyT1AY6ZEf4= == the built sha. State Active / L
- 20260903T084245Z LEG L6 closed: LIVE get-distribution AFTER apply: Status=Deployed, ORIGIN DENOMINATOR 7, APIGateway-portal and APIGateway-portfolio eac
- 20260903T085928Z LEG L1 closed: Lane commit 7abe7552b5 (author 0.7.0_AE_CloudOps~Z), 10 files / 687 insertions: the 3 portal-auth .tf, originVerify.ts +
- 20260903T085928Z CLOSED -- all 6 legs proven
