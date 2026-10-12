# Deploy Completion Record
**Date opened:** 2026-10-12T09:43:09.275817+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-w-3 (FWD-28, SECOND pair): release the CODE of ONE function, opal-portal-data-proxy, by ONE safe-apply of infra/aws/terraform/market-overview at pin 50c8feb76b, so the two class-(i) routes (POST /sentiment/keyword-intelligence, GET /aum/metrics) answer only a caller whose authorizer firmId is in the route set (firm_page_access.py ROUTE_FIRMS) or whose tier is internal; the 39 internal-only routes are unchanged. AUTHORITY: order NFRA_CTLPLN.TO-CT-w-3 AMENDMENT 1 (issuer 2.0.0_SA_COO~C, msg 108502). BOTH HALVES READ WHOLE BEFORE THIS ENTRY: COO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/CT-w-3_PAIR_20261012.md (54 lines, @47edbc46ee) and CTO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/1.0.0_SA_CTO/NEVER_WIDEN_CT_W3_FWD28_FIRM_CHECK_CTO_HALF.md (50 lines, msg 108501). BUILD INPUT THREE members at the pin: lambda_function.py 17b122b004684f6a8464b35374a1074741f6679c06aa8efd0ba79997d8af3d07, session_tracker.py 00f8c6a31aab295973a9c573f6f8eec83a4e68dbb1eb0cf5c531f4e50873ef40, firm_page_access.py 80590106282c2d44271a5e8d66b30d0a79f6693ddd891155b51b72f37508f33c (all three equal the pair values when read from the pin blobs). ARTIFACT KEY market-overview/opal-portal-data-proxy.zip; PREVIOUS (rollback) version id 5Xgupv5fa4W1mFULZco6ByEPzs9HRK2C, content-sha256 6/BPExXEB1KneUKzyY45cbkw2px01XEOFMV0h/5Vst8= equal to the live CodeSha256 (the CT-u-7 release), 25668 bytes; rollback = re-point s3_object_version to it by one safe-apply, one resource moved, then the internal-caller read. CONSUMERS: a Lambda pulls no task family or image tag; none exist. Callers outside the authorizer path (direct invokes, ruled c404), opal_ai, mcportal and scheduled jobs are NOT searched. CALLERS of the exercise: per the first pair CTO half section 2, option (b) prime then (a); ui_walker_account.py takes no second account id (PK constant), so (a) the OW_SD2 precedent in terms (one synthetic row, firm 49financial, tier advisor, created and deleted inside this entry, token <=60 min, never printed). BOUNDS: one function code only; no IAM, API Gateway, authorizer, env, layer or portal change; no update-function-code (the function deploy.sh is NOT a build path); a pre-apply table that is not not_admitted=0 STOPS the act before the build.
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE state, PRE table and P0 | BEFORE state recorded; PRE: every request to the two routes tabulated by firmId and tier from CloudWatch over the stated window with denominator, not_admitted=0 (any other value STOPS with no build); P0: deployed lambda_function.py = 5f0fad0e...7427 and session_tracker.py = 00f8c6a3...ef40, no third member |  | OPEN |
| L2 | s3-prefix | build three members at the pin and upload | zip member list read back = exactly lambda_function.py, session_tracker.py, firm_page_access.py with all three hashes equal to the pin; uploaded version id and content-sha256 recorded |  | OPEN |
| L3 | activation | plan then ONE safe-apply | Branch A exactly 0 to add 1 to change 0 to destroy on aws_lambda_function.portal_data_proxy; anything else STOP and apply nothing |  | OPEN |
| L4 | verify | after-reads and exercise | CodeSha256 equals the built file; deployed package diffed member by member both directions (3 members); env and layers unchanged; R1 partner caller GET /aum/metrics 200; R2 internal caller on both open routes 200; R3 partner caller on one class-(ii) route 403; R4 unadmitted-firm caller 403 or NOT-EXERCISED with a reason and nothing minted; replan 0-diff |  | OPEN |
| L5 | git | record the deploy | record-terraform-deploy.sh run, source map stamped, annotated tag, push state stated as a measured value |  | OPEN |
| L6 | verify | cleanup | walker disarmed by its own tool; synthetic row deleted only after token exp and read back ABSENT with a control; census of synthetic rows zero |  | OPEN |

## Log

- 20261012T094309Z OPENED by 0.7.0_AE_CloudOps~U7 with 6 leg(s)
