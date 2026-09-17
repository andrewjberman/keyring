# Deploy Completion Record
**Date opened:** 2026-09-17T04:32:20.905741+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260917T043710Z
**Deploy:** RETROACTIVE -- AMGT-rk-6/rk-7 combined redeploy of opal-amgt-scoped-api at 2026-09-17T03:27:57Z, opened after landing per CTO ruling row Z-S143
**Authored by:** 2.0.0_SA_COO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-act anchor + 8-GET census | CodeSha256 + artifact VersionId + census JSON | Pre-act (measured at rk-7 COO co-sign signing, before AMGT-rk-6 deployed): CodeSha256 x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw=, artifact S3 VersionId X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA, CodeSize 754470, Layers 0, MemorySize 512, Timeout 29. GET census (8 route-table entries, 8 GET): lead-panel/rankings 200, lead-panel/timeseries 200, watchlist 200, overlay 200, thesis 200, peers 200, coverage 200, print 500. Sets: 7 of 8 200, print the sole 500. | CLOSED 20260917T043709Z |
| L2 | verify | post-act anchor + 16-route census + IAM census | CodeSha256 + layer + route census + IAM policy read | Post-act (measured by issuer independently, 2026-09-17, on two instruments): CodeSha256 zHmPoWu9jZqUUqlK9zwvfoZk/aFg+rOoOLbuJwHGRHA=, LastModified 2026-09-17T03:27:57Z, Layers 1 (arn ...layer:opal-amgt-print-deps:1), MemorySize 512, Timeout 29 (unchanged). Route census read from the deployed branch's own scoped_amgt_route_table(): 16 entries (10 pre-existing + 5 new: freshness, lists, ledger, versions, compare + refresh unchanged), all invoked live on the DEPLOYED adapter: 8 of 8 GET 200 (print now 200, was 500). apigatewayv2 paginated read: 16 /api/scoped/amgt/* routes on api 7k3ed8px20, ALL AuthorizationType CUSTOM (0 exceptions). IAM opal-amgt-scoped-api-role inline policy opal-amgt-scoped-api-grants: GetObject Resource 12 entries, ListBucket StringLike s3:prefix 12 entries -- BOTH limbs at 12 (the co-signed packs/* and raw/* widening landed on both), no write action added, no lib/ or social/ prefix present. list_event_source_mappings on opal-research-pull-requests: 0. | CLOSED 20260917T043710Z |
| L3 | verify | 0-diff targeted re-plan (DESIRED==APPLIED) | terraform plan -target=module.scoped_amgt_api output | terraform plan -target=module.scoped_amgt_api -no-color, run from the deployed branch's own worktree (wk-amgt_resapp-12-24 @89f6a35e46), 2026-09-17: refreshed module.scoped_amgt_api.data.aws_s3_object.artifact, data.aws_s3_object.amgt_print_deps_zip, module.scoped_amgt_api.aws_cloudwatch_log_group.lambda, aws_iam_role.scoped_amgt_api, aws_dynamodb_table.harvest_security_metrics, aws_dynamodb_table.harvest_articles, aws_lambda_layer_version.amgt_print_deps, module.scoped_amgt_api.aws_lambda_function.this. Output: 'No changes. Your infrastructure matches the configuration.' DESIRED == APPLIED, 0-diff, confirmed. | CLOSED 20260917T043710Z |
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | RETROACTIVE: the apply-time plan resource list was NOT RECORDED AT THE ACT and is NOT reconstructed here (the worker's own report states 'Resources: 6 added, 2 changed, 0 destroyed' from its own terminal output, taken at face value, not independently captured). Compensating verification: L1 (pre-act anchor), L2 (post-act anchor + live census, two instruments) and L3 (0-diff targeted re-plan proving DESIRED==APPLIED post-hoc) together demonstrate the act landed exactly the co-signed blast radius (rk-6 COO half @34d68dcfaf, rk-6 CTO half @653de214b1, rk-7 COO half @09b20e5546, rk-7 CTO half @7e84705c7a) with no destroy, no IAM write, no route beyond the signed five, and every pre-existing served route unregressed. Signer's own independent verification: row AMGT_RESAPP-Z-S143 @3c3134e069 (1.0.0_SA_CTO~Z), citing rows S141 (print 500 persists for BP/_LN_Equity and NG/_LN_Equity, a slash-in-filename defect, carried to L9/L10, not a regression) and S142 (the missing-entry finding this ledger record answers). | CLOSED 20260917T043710Z |

## Log

- 20260917T043220Z OPENED by 2.0.0_SA_COO~Z with 4 leg(s)
- 20260917T043709Z LEG L1 closed: Pre-act (measured at rk-7 COO co-sign signing, before AMGT-rk-6 deployed): CodeSha256 x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS
- 20260917T043710Z LEG L2 closed: Post-act (measured by issuer independently, 2026-09-17, on two instruments): CodeSha256 zHmPoWu9jZqUUqlK9zwvfoZk/aFg+rOo
- 20260917T043710Z LEG L3 closed: terraform plan -target=module.scoped_amgt_api -no-color, run from the deployed branch's own worktree (wk-amgt_resapp-12-
- 20260917T043710Z LEG opal-amgt-scoped-api closed: RETROACTIVE: the apply-time plan resource list was NOT RECORDED AT THE ACT and is NOT reconstructed here (the worker's o
- 20260917T043710Z CLOSED -- all 4 legs proven
