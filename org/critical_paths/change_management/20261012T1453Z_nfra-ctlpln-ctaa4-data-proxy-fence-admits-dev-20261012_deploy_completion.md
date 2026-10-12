# Deploy Completion Record
**Date opened:** 2026-10-12T14:53:36.527903+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-aa-4 (FWD-28 Dev admission, FOURTH pair): release the CODE of ONE function, opal-portal-data-proxy, by ONE safe-apply of infra/aws/terraform/market-overview at pin 96c4f5f063, so _require_route_access admits a caller whose authorizer tier is internal OR whose userType is exactly Dev (this WIDENS the admitted callers by one class). AUTHORITY: order NFRA_CTLPLN.TO-CT-aa-4 AMENDMENT 1 (issuer 2.0.0_SA_COO~C, msg 108596). BOTH HALVES READ WHOLE BEFORE THIS ENTRY: COO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/CT-aa-4_PAIR_20261012.md (53 lines, @35780df2d0) and CTO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/1.0.0_SA_CTO/NEVER_WIDEN_CT_AA4_FWD28_DEV_ADMISSION_CTO_HALF.md (37 lines, msg 108594). BUILD INPUT THREE members at the pin: lambda_function.py 9cbf41a0f0a5c3766d9bd9958eb9283b68d0f9e1ff0472ffaf30c21f8d238dcc, session_tracker.py 00f8c6a31aab295973a9c573f6f8eec83a4e68dbb1eb0cf5c531f4e50873ef40, firm_page_access.py 7365de94fa8059c9a196f86bfe0a457f6825278507c9ec8f827f047bb2b3e868 (all equal the pair values when read from the pin blobs). LIVE TODAY (third pair): CodeSha256 zoCWZxmn6nwzFEEIEIl4NoVP2rojFGntQaLSxy8lLSU=, members a9c7a403..., 00f8c6a3..., 7365de94.... ARTIFACT KEY market-overview/opal-portal-data-proxy.zip; PREVIOUS (rollback) version id fhBfCdz9uAco4sDgntJqhw6yWhGo8ZLT (26148 bytes, content-sha256 equal to the live CodeSha256); rollback = re-point s3_object_version to it by one safe-apply, one resource moved, then R1 and R2 again; the previous package returns the fence to internal tier only. CONSUMERS: a Lambda pulls no task family or image tag; none exist. ARMING: the UI walker row by its own tool (arm, in-process password, real login, disarm), used AS IT IS, no row edited; ui_walker_account.py takes no second account id, so the partner caller is option (a) of the first pair CTO half: one synthetic row on firm 49financial tier advisor created and deleted inside this entry, token <=60 min, never printed. BOUNDS: one function code only; no IAM, API Gateway, authorizer, env, layer, log-group or retention change; no update-function-code; no token or cookie value printed or stored; PRE-1 finding any Dev row whose firmId is not the internal firm is Branch B (no build, one line to 2.0.0_SA_COO~C).
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE state, PRE-1 and P0 | BEFORE state recorded; PRE-1: counts only over opal-users-v2 PROFILE rows of (a) userType Dev, (b) of those tier internal, (c) of those tier other than internal or absent, (d) Dev rows on a firm other than the internal firm (must be 0, else STOP); P0: the three deployed members equal the third pair pin |  | OPEN |
| L2 | s3-prefix | build three members at the pin and upload | zip member list read back = exactly three, all hashes equal to the pin; uploaded version id and content-sha256 recorded |  | OPEN |
| L3 | activation | plan then ONE safe-apply | Branch A exactly 0 to add 1 to change 0 to destroy on aws_lambda_function.portal_data_proxy; anything else STOP and apply nothing |  | OPEN |
| L4 | verify | after-reads, exercise and the new log lines | CodeSha256 equals the built file; deployed package diffed member by member both directions; env and layers unchanged; R1 internal caller 200, R2 partner caller 403 on one class-(ii) route, R3 Dev-type non-internal caller 200 or NOT-RUN with the measured reason, R4 post-apply log events jwt_shaped=0 bearer=0; replan 0-diff |  | OPEN |
| L5 | git | record the deploy | record-terraform-deploy.sh run, source map stamped, annotated tag, push state stated as a measured value |  | OPEN |
| L6 | verify | cleanup | walker disarmed by its own tool; synthetic row deleted only after token exp and read back ABSENT with a control; census of synthetic rows zero |  | OPEN |

## Log

- 20261012T145336Z OPENED by 0.7.0_AE_CloudOps~U7 with 6 leg(s)
