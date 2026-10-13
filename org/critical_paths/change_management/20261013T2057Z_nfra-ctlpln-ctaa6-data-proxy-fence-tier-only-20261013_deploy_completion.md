# Deploy Completion Record
**Date opened:** 2026-10-13T20:57:34.707951+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-aa-6 (FIFTH pair, NARROWS): release the CODE of ONE function, opal-portal-data-proxy, by ONE safe-apply of infra/aws/terraform/market-overview at pin cc09499bd5, so _require_route_access admits tier == internal only (the userType Dev clause of the fourth pair removed). BOTH HALVES READ WHOLE BEFORE THIS ENTRY: COO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/CT-aa-6_PAIR_20261013.md @3afb98f3fc, CTO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/1.0.0_SA_CTO/NEVER_WIDEN_CT_AA6_FENCE_TIER_ONLY_CTO_HALF.md. BUILD INPUT THREE members at the pin: lambda_function.py aa82b86c882d7b8a7cc482bfa2e1654a5f01e6f0c63eaf62e4399c437ab6a9a6, session_tracker.py 00f8c6a31aab295973a9c573f6f8eec83a4e68dbb1eb0cf5c531f4e50873ef40, firm_page_access.py 7365de94fa8059c9a196f86bfe0a457f6825278507c9ec8f827f047bb2b3e868 (read from the pin blobs, equal the pair; 0 changed paths pin..HEAD under the root and the function dir). LIVE TODAY (fourth pair): CodeSha256 q4iLGld/nR2jOOaL2JJ6frlUSNNEgJnV2I8oyIQ6z/Y= (the CTO condition 3 value), LastModified 2026-10-12T15:02:18Z. ARTIFACT KEY market-overview/opal-portal-data-proxy.zip; PREVIOUS (rollback) version id iXfMozSh1d5C4EbKLGnhYgSKH3b8yt4j (26310 bytes, IsLatest); rollback = re-point s3_object_version to it by one safe-apply, one resource moved, then R1 and R2; it returns the Dev clause. CONSUMERS: a Lambda pulls no task family or image tag; none exist. ARMING: the UI walker row by its own tool (arm, real login, disarm), used as it is; the partner caller is ONE synthetic row (firm 49financial, tier advisor) created and deleted inside this entry because the walker tool takes no second account id (the OW_SD2 / CT-aa-4 precedent, CT-w-10 pair line 44); NOT an edit of an existing seed row. BOUNDS: one function code only; no IAM, API Gateway, authorizer, env, layer, log-group or retention change; no update-function-code; no token or cookie value printed or stored; PRE-1 finding a Dev row off the internal firm is Branch B (no build, one line to 2.0.0_SA_COO~C). Start conditions: both halves SIGNED at the pin; CT-ab-2 apply complete and its ledger CLOSED (8ef2c65918), the two entries never shared.
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE state, PRE-1 and P0 | PRE-1 counts only over opal-users-v2 PROFILE rows (Dev, of those internal tier, off-internal-firm must be 0); P0: the three deployed members equal the fourth pair pin |  | OPEN |
| L2 | s3-prefix | build three members at the pin and upload | member list read back exactly three, hashes equal the pair; version id and content-sha256 recorded |  | OPEN |
| L3 | activation | plan then ONE safe-apply | Branch A exactly 0 to add 1 to change 0 to destroy on aws_lambda_function.portal_data_proxy; anything else STOP |  | OPEN |
| L4 | verify | after-reads, exercise and the new log lines | CodeSha256 equals the built file; R1 internal 200, R2 partner 403, R3 walker as it is 200, R4 post-apply jwt_shaped=0 bearer=0; replan 0-diff |  | OPEN |
| L5 | git | record the deploy | record-terraform-deploy.sh run, source map stamped, annotated tag, push state a measured value |  | OPEN |
| L6 | verify | cleanup | walker disarmed; synthetic row deleted after token exp and read back ABSENT with a control; census zero |  | OPEN |

## Log

- 20261013T205734Z OPENED by 0.7.0_AE_CloudOps~U7 with 6 leg(s)
