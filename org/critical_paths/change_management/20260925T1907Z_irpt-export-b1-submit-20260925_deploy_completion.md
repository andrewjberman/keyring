# Deploy Completion Record
**Date opened:** 2026-09-25T19:07:59.548746+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T191358Z
**Deploy:** Export B1: irpt-export-render serves submit-export on a retained Performance report (QUEUED, dispatch off) -- publish 7bfd665d0e, export root e14cd90571
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | build-and-upload OK line with content-sha256 of the 7bfd665d0e build | build-and-upload irpt-export-render from publish 7bfd665d0e (all 40 staged rows pinned 755c13bc19, sha-verified): s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip write VERIFIED size=340942, content-sha256 1oJDheftIk2WNmTuJiYGQpZK0VC4kPWo76NTMFh1ir8= (head-object 19:08:40Z); staged members cleaned from the source dir | CLOSED 20260925T191011Z |
| A2 | activation | module.irpt_export_render + aws_iam_role_policy.export_render_submit | live CodeSha256 == uploaded content-sha256; env IRPT_REQUESTS_TABLE / IRPT_PORTAL_CHECKOUT / IRPT_CONTRACTS_DIR=/var/task/irpt_contracts; policy irpt-export-render-submit-policy present | safe-apply 1 added / 1 changed / 0 destroyed (19:1xZ). Live irpt-export-render CodeSha256 1oJDheftIk2WNmTuJiYGQpZK0VC4kPWo76NTMFh1ir8= == uploaded content-sha256, State Active/Successful; env IRPT_REQUESTS_TABLE=irpt-requests, IRPT_PORTAL_CHECKOUT=/var/task/render_package_checkout, IRPT_CONTRACTS_DIR=/var/task/irpt_contracts; role policies include irpt-export-render-submit-policy (7 total). | CLOSED 20260925T191320Z |
| N1 | verify | negative arm before and after | ungranted advisor submit NOT_AUTHORIZED before+after; internal submit of a nonexistent report UNEXPECTED before -> OBJECT_NOT_COVERED after; internal receipt of a nonexistent export UNEXPECTED before -> NOT_FOUND after; 0 objects under generations/exr_* at 3 firms after | Direct-invoke probes, same events before (old artifact 2gSDyx..) and after: internal (opal-capital, Dev) submit of a nonexistent report UNEXPECTED -> OBJECT_NOT_COVERED (the B1 path composed in-role and the live retained index refused it); internal receipt of a nonexistent export UNEXPECTED -> NOT_FOUND (the old artifact failed every internal user on this route, silently -- no sink); ungranted advisor submit NOT_AUTHORIZED before and after; no response carried a data key; 0 objects under firms/{cottonwood,49financial,inflection}/generations/exr_* after. | CLOSED 20260925T191320Z |
| V1 | verify | export root re-plan | No changes | export root re-plan after apply (vendored terraform 1.9.8, -detailed-exitcode rc=0): No changes. Your infrastructure matches the configuration. | CLOSED 20260925T191357Z |

## Log

- 20260925T190759Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260925T191011Z LEG A1 closed: build-and-upload irpt-export-render from publish 7bfd665d0e (all 40 staged rows pinned 755c13bc19, sha-verified): s3://o
- 20260925T191320Z LEG A2 closed: safe-apply 1 added / 1 changed / 0 destroyed (19:1xZ). Live irpt-export-render CodeSha256 1oJDheftIk2WNmTuJiYGQpZK0VC4kP
- 20260925T191320Z LEG N1 closed: Direct-invoke probes, same events before (old artifact 2gSDyx..) and after: internal (opal-capital, Dev) submit of a non
- 20260925T191357Z LEG V1 closed: export root re-plan after apply (vendored terraform 1.9.8, -detailed-exitcode rc=0): No changes. Your infrastructure mat
- 20260925T191358Z CLOSED -- all 4 legs proven
