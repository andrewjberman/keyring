# Deploy Completion Record
**Date opened:** 2026-10-14T16:26:42.149962+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-j-1 (ADHOC.canon-r7-publisher-deploy, WORLD): the opal-assets-mdpf-portal-publisher package rebuilt at pin 9592daf75c7469d212242cd63850c735f6f53238 and uploaded to the artifact key s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-mdpf-portal-publisher.zip (prior VersionId Deg26fXt..bp.9N3HB4sZKEu.MYLj4y2, content-sha256 a63f896adf7ab797628c1fb449017dd7c4b5a62dc0641b3579036f3172d81090), function opal-assets-mdpf-portal-publisher, MDPF_PUBLISHER_COMMIT (infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf value and its comment only; prior value e8994f23af282296037bd28bb539ac55cc9465dd) set in the same targeted apply on module.mdpf_publisher, one on-demand invoke. Four NEW keys: platinum/mdpf/{49financial,inflection,cottonwood,global}/category-views-history.json in opal-data-portal-v2. The 18 existing leaves platinum/mdpf/<scope>/<type>.json (4, 4, 5, 5) are rewritten with their own data by the invoke. Serving path: CloudFront EVTSA9VEHNZVH, /api/general/*, public-data-router (/api/general/mdpf/ -> /platinum/mdpf/), bucket opal-data-portal-v2. The gold lambda, the gold package and the runner code tree are NOT touched. GO: 2.0.0_SA_COO~D1 msg 5647 (pin named; the gold ledger mdpf-canon-r7-gold-deploy-dell1-20261014 is CLOSED); pair COO half 159b6d7a67, CTO half 9a492909b7.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions 2a-2g re-measured (edge read, FIRMBKTS gap, sentinels across every live worktree), before print (function, rollback copy of the prior artifact version by hash, schedule, 18 leaves, pointer, four absent history keys, dated counts), drift table at the GO pin | all recorded and printed |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-mdpf-portal-publisher.zip (D1 upload of the zip built from the pin) | new version whose content-sha256 metadata equals the sha256 of its bytes, read back before planning |  | OPEN |
| L3 | activation | module.mdpf_publisher (D1: .tf MDPF_PUBLISHER_COMMIT, one targeted plan, one safe-apply) | plan moves only s3_object_version, source_code_hash and MDPF_PUBLISHER_COMMIT; CodeSha256 equals the zip; commit equals the pin and the sidecar; every sidecar module equals git show pin; re-plan clean |  | OPEN |
| L4 | activation | the one on-demand invoke of opal-assets-mdpf-portal-publisher with the schedule's input {} (D2) | 200, no FunctionError, all_present true, published 18, history_rows 4 published, four keys exist, 18 baseline leaves same data apart from _provenance, runtime import recorded |  | OPEN |
| L5 | verify | the edge GET of each of the four leaves through the public host (D3, read-only) | status, bytes and JSON parse recorded per scope; 401/403 recorded and the sub-leg stopped |  | OPEN |
| L6 | verify | after print: function configuration (only CodeSha256, LastModified, MDPF_PUBLISHER_COMMIT changed), artifact versions, four keys, 18 leaves, pointer, schedule | differences listed, nothing deployed from them |  | OPEN |

## Log

- 20261014T162642Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 6 leg(s)
