# Deploy Completion Record
**Date opened:** 2026-10-12T04:22:47.557422+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-u-7 (FWD-28): release the CODE of ONE function, opal-portal-data-proxy, by ONE safe-apply of infra/aws/terraform/market-overview at pin 6a1607d1e0, so 39 of 41 routes answer only tier internal; the 2 class-(i) routes stay open. AUTHORITY: order NFRA_CTLPLN.TO-CT-u-7 AMENDMENT 3 (issuer 2.0.0_SA_COO~C). BOTH HALVES READ WHOLE BEFORE THIS ENTRY: COO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/CT-u-7_PAIR_20261012.md (73 lines, @fa15bf525a) and CTO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/1.0.0_SA_CTO/NEVER_WIDEN_CT_U7_FWD28_DATA_PROXY_FENCE_CTO_HALF.md (62 lines). CONSUMERS: a Lambda pulls no task family or image tag; none exist. CALLERS of the function are the portal API routes behind the portal authorizer; outside-the-tree callers (opal_ai, mcportal, scheduled jobs) NOT SEARCHED per CTO half section 4. ROLLBACK K1: re-point s3_object_version to the PRIOR artifact version rBMEa1msFligoftTM_aJHjyCxB87oT4U (content-sha256 LpodJICuU9XTUklcvNeZA8WEKBDmQF2fU72YzwkD2cI=, 24846 bytes, 2026-06-10T15:32:38Z), one safe-apply, one resource moved, then the R2 read. NON-INTERNAL CALLER: ui_walker_account.py cannot take a second account id (PK is a module constant), so per CTO half section 2 option (a) the OW_SD2 precedent is adopted in terms: one synthetic row on firm 49financial tier advisor, created and deleted inside this entry, token <=60 min, never printed or stored. BOUNDS: one function code only; no IAM, API Gateway, authorizer, env, layer change; no update-function-code; no CLOUD push; no alert or monitor.
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE state and P0 | BEFORE: CodeSha256, rollback artifact version, env and layers recorded; P0: deployed lambda_function.py hashes 24dc244f...79bb (the base) before any row or token exists |  | OPEN |
| L2 | activation | internal caller armed and non-internal caller row plus token | walker armed by its own tool (HOLDER recorded); ONE synthetic row 49financial advisor written conditionally and read back; ONE token minted in memory with exp <=60 min; claim NAMES and expiry only recorded |  | OPEN |
| L3 | verify | R0 before the apply | non-internal caller GET a class-(ii) route answers 200 (the fence not yet live); 403 means STOP |  | OPEN |
| L4 | s3-prefix | build at the pin and upload with content-sha256 | members lambda_function.py 5f0fad0e...7427 and session_tracker.py 00f8c6a3...ef40 hash at the pin before the build; uploaded object content-sha256 and new version id recorded |  | OPEN |
| L5 | activation | plan then ONE safe-apply | Branch A exactly 0 to add 1 to change 0 to destroy on aws_lambda_function.portal_data_proxy; anything else STOP and apply nothing |  | OPEN |
| L6 | verify | after-reads | CodeSha256 equals built file; deployed package diffed member by member both directions; env and layers unchanged; R1 403 forbidden message; R2 internal 200; R3 class-(i) open 200 for both callers; replan 0-diff |  | OPEN |
| L7 | git | record the deploy | record-terraform-deploy.sh run, source map stamped, annotated tag, push state stated as a measured value |  | OPEN |
| L8 | verify | cleanup | walker disarmed by its own tool; synthetic row deleted only after token exp and read back ABSENT with a control; census of synthetic rows zero |  | OPEN |

## Log

- 20261012T042247Z OPENED by 0.7.0_AE_CloudOps~U7 with 8 leg(s)
