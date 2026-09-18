# Deploy Completion Record
**Date opened:** 2026-09-18T05:13:33.518473+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T054356Z
**Deploy:** IRPT_BCKEND IB-rtc-3: repo-shaped unpack recipe deployed and the directory root re-applied
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L3 | verify | served CodeSha256 == built zip sha256, host import check re-run for inf/cot | CodeSha256 match + SSM import-check stdout | Served CodeSha256 6ELkwh91ssB4nvlWE/S5InQ2amQBIZkB4zC7oP0AzkE= == built zip sha256 == source-map artifact_sha256 (verified above). Host import re-check for inf/cot: SSM 74c1f0f4-2267-4ea1-9bf2-849f4d8f32cb (inflection) and 71f11079-ae43-477e-b803-02fa91791c34 (cottonwood), both Status Failed rc=1 but BOTH print 'IMPORT-OK first-party modules resolved: trading_calendar, ids, contract' and 'SOURCE_SETS [49financial, cottonwood, inflection]' before failing later at directory_runner.py's own select_business_date() refusal (row IRPT_BCKEND-W2-S55) -- the repo-shaped unpack itself is proven on the host, distinct from the business-date defect it exposed. | CLOSED 20260918T054337Z |
| irpt-directory-refresh | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply rc=0: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Re-plan: 'No changes. Your infrastructure matches the configuration.' Served CodeSha256 6ELkwh91ssB4nvlWE/S5InQ2amQBIZkB4zC7oP0AzkE= == built zip sha256 (local, verified against S3 head-object metadata content-sha256 and ContentLength=36937 before the apply) == source-map artifact_sha256. Timeout unchanged at 60s. | CLOSED 20260918T052757Z |

## Log

- 20260918T051333Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
- 20260918T052757Z LEG irpt-directory-refresh closed: TF apply rc=0: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Re-plan: 'No changes. Your infrastructure m
- 20260918T054337Z LEG L3 closed: Served CodeSha256 6ELkwh91ssB4nvlWE/S5InQ2amQBIZkB4zC7oP0AzkE= == built zip sha256 == source-map artifact_sha256 (verifi
- 20260918T054356Z CLOSED -- all 2 legs proven
