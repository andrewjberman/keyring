# Deploy Completion Record
**Date opened:** 2026-06-29T20:54:10.576969+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260629T205833Z
**Deploy:** Legacy bd portal-publish chain teardown (Andrew-direct go scope#1): bd-portal-publisher + bd-capture-output-versions lambdas + the dead pipeline-complete.json->PortalPublisherTrigger + the bd_gold_layer_invoke fan-out grant. Superseded by the modern gold D_02 EC2 chain at the GLDRST cutover ~2026-04-06; all 0-invoke since. advisor-publisher already gone (06-03). Shared bd_gold_layer role NOT touched. Served old-path artifacts = scope#2 never-widen, NOT in this teardown.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: remove TF (2 modules + permission + fan-out policy + capture role/policy/attach + PortalPublisherTrigger) + source-map x2 + source dirs | hash pushed | commit 700b0892d pushed CLOUD f69f9b70b..700b0892d; 6 files, 2374 deletions (2 lambda modules + s3_portal_publisher perm + bd_gold_layer_invoke policy + bd_capture_versions role/policy/attach + PortalPublisherTrigger + 2 source-map entries + 2 source dirs). plan = 0add/1change/9destroy. | CLOSED 20260629T205719Z |
| L2 | activation | safe-apply destroys 2 lambdas + 2 log groups + capture role/policy/attach + s3 permission + fan-out policy; PortalPublisherTrigger off the bucket notification | apply complete + 0-diff re-plan | safe-apply complete: 0 added/1 changed/9 destroyed (2 lambdas + 2 log-groups + bd_capture_versions role/policy/attach + s3_portal_publisher perm + bd_gold_layer_invoke policy; bucket notification updated in-place). HALTGT passed. 0-diff re-plan: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260629T205833Z |
| L3 | verify | get-function ResourceNotFound x2; bucket notification has no PortalPublisher rule; artifacts removed; 0-residual + CVO co-verify | live-state check | LIVE verify: get-function bd-portal-publisher + bd-capture-output-versions -> ResourceNotFound x2; get-role bd-capture-versions-lambda-role -> NoSuchEntity; bucket notification LambdaFunctionConfigurations = [ProcessAllocationFiles, GoldLayerPricesTrigger] (live triggers KEPT, PortalPublisher gone); both artifact zips removed (0-residual). CVO co-verify requested separately. | CLOSED 20260629T205833Z |

## Log

- 20260629T205410Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260629T205719Z LEG L1 closed: commit 700b0892d pushed CLOUD f69f9b70b..700b0892d; 6 files, 2374 deletions (2 lambda modules + s3_portal_publisher perm
- 20260629T205833Z LEG L2 closed: safe-apply complete: 0 added/1 changed/9 destroyed (2 lambdas + 2 log-groups + bd_capture_versions role/policy/attach + 
- 20260629T205833Z LEG L3 closed: LIVE verify: get-function bd-portal-publisher + bd-capture-output-versions -> ResourceNotFound x2; get-role bd-capture-v
- 20260629T205833Z CLOSED -- all 3 legs proven
