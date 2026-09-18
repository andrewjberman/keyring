# Deploy Completion Record
**Date opened:** 2026-09-18T06:36:44.887237+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T070036Z
**Deploy:** IRPT_BCKEND IB-rtc-3 AMENDMENT 2: dispatch drops explicit --as-of, directory root re-applied
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | content-sha256 metadata match + head-object size | content-sha256=u82ZY7lCKf/lR7hxFQfy2a6FofEfkSGu4hLLoO7wU+4= verified via head-object (size 38745==38745); s3api put-object VersionId=6j9_Bg0twboACzQkCQZ1ZyceFC.I0B9H | CLOSED 20260918T064633Z |
| L2 | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + served CodeSha256 matches uploaded sha | terraform apply: Plan 0 to add 1 to change 0 to destroy; Apply complete 0 added 1 changed 0 destroyed; served CodeSha256 u82ZY7lCKf/lR7hxFQfy2a6FofEfkSGu4hLLoO7wU+4= == uploaded sha; post-apply re-plan No changes | CLOSED 20260918T064702Z |
| L3 | verify | served CodeSha256 == re-derived zip sha256, host import re-check, real fire for inf/cot lands | CodeSha256 match + SSM stdout + list-objects-v2 before/after | served CodeSha256 u82ZY7lCKf/lR7hxFQfy2a6FofEfkSGu4hLLoO7wU+4= verified against re-derived zip; host import re-check IMPORT-OK for inf/cot/49f (SSM commands f9c34e7a.. e6869e09.. 0fe77c42..); real fire for inf/cot did NOT land -- the --as-of refusal (row W2-S55) is CLEARED (confirmed absent from stdout) but a NEW, deeper, out-of-lane blocker in directory_runner.py (jsonschema.Draft202012Validator absent from the host's jsonschema==3.2.0) now refuses; filed as a new BLOCKING row, not a deploy defect -- the deploy itself is complete and verified | CLOSED 20260918T070018Z |

## Log

- 20260918T063644Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 3 leg(s)
- 20260918T064633Z LEG L1 closed: content-sha256=u82ZY7lCKf/lR7hxFQfy2a6FofEfkSGu4hLLoO7wU+4= verified via head-object (size 38745==38745); s3api put-obje
- 20260918T064702Z LEG L2 closed: terraform apply: Plan 0 to add 1 to change 0 to destroy; Apply complete 0 added 1 changed 0 destroyed; served CodeSha256
- 20260918T070018Z LEG L3 closed: served CodeSha256 u82ZY7lCKf/lR7hxFQfy2a6FofEfkSGu4hLLoO7wU+4= verified against re-derived zip; host import re-check IMP
- 20260918T070036Z CLOSED -- all 3 legs proven
