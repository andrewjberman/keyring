# Deploy Completion Record
**Date opened:** 2026-10-01T06:08:17.698912+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate and irpt-status as WHOLE bundles at CLOUD 21eca74f40, with the etf-classifications Scan grant first; CTO rulings batch 61 item 2b and batch 62 items 5 and 6
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | verify | both bundles built at one commit, gated and uploaded | every member equals the pin; served.py import closure 0 stale; the four standing gates on the built zips; S3 versions read back |  | OPEN |
| G1 | activation | dynamodb Scan on etf-classifications for irpt-ycharts-generate-role, grant first | targeted safe-apply on the inline policy alone; simulate-principal-policy allowed |  | OPEN |
| F1 | activation | irpt-ycharts-generate code pointer | both halves at HEAD; targeted safe-apply 0 add 1 change 0 destroy; CodeSha256 equals the built artifact |  | OPEN |
| F2 | activation | irpt-status code pointer | both halves at HEAD; targeted safe-apply 0 add 1 change 0 destroy; CodeSha256 equals the built artifact |  | OPEN |
| V1 | verify | both functions after the applies | before and after empty-headers invoke; one invoke per function reaching the changed path; re-plan No changes; ten minutes of logs with 0 TypeError and 0 ImportModuleError |  | OPEN |
| V2 | verify | service boundary on irpt-ycharts-generate | svc-irpt-analysis selecting a foreign firm refused FIRM_BINDING and cottonwood not |  | OPEN |

## Log

- 20261001T060817Z OPENED by 2.0.0_SA_COO~Y with 6 leg(s)
