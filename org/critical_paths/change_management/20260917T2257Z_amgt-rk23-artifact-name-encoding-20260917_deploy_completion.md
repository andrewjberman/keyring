# Deploy Completion Record
**Date opened:** 2026-09-17T22:57:26.197613+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260917T235332Z
**Deploy:** AMGT-rk-23: path-safe LOCAL artifact names (S141 slash keys) -- render_pack.py security_key() + scoped_amgt.py _read_drafting_document local_filename. Lambda deploy 1 of 4, batch B. Co-signed CTO 533f216c74 / COO 6b7d4f2341, HALF 2.
**Authored by:** 0.9.0_WK_AMGT_RESAPP~27
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | PRE-ACT live get_function_configuration: CodeSha256 zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=, LastModified 2026-09-17T19:23:42Z, CodeSize 782668, MemorySize 512, Timeout 29, one layer opal-amgt-print-deps:1, Env unchanged. Pre-deploy census: 13 of 13 GET routes -> 200. AC1 BEFORE (full 33-key sweep): served_ok 31 of 33, failures BP/_LN_Equity 404 and NG/_LN_Equity 404 (router refusal, NOT a 500 -- differs from the order's own premise). BUILD: infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh -- 47 code + 7 data + 139 vendored entries, ISOLATED runtime 3/3 arms OK, uploaded s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip, local sha256 iGmDkRbA6ZenF0CHAgU7nwNZkmdUEzMKRdBEJsDlbP0=, VersionId v9DDa68o8Y0HNgDXiL7lB0A1HYKbDlWF. Targeted plan: 0 to add, 1 to change, 0 to destroy, naming ONLY module.scoped_amgt_api.aws_lambda_function.this (source_code_hash/s3_object_version/last_modified). APPLY (HALT_ACK=1, safe-apply.sh -target=module.scoped_amgt_api.aws_lambda_function.this): Apply complete! Resources: 0 added, 1 changed, 0 destroyed. POST-ACT live config: CodeSha256 iGmDkRbA6ZenF0CHAgU7nwNZkmdUEzMKRdBEJsDlbP0= (matches uploaded artifact exactly), LastModified 2026-09-17T23:33:34Z, CodeSize 783126, layer/memory/timeout/env unchanged. Post-deploy census: 13 of 13 GET routes -> 200, LOST=[] GAINED=[] (identical key set to pre-deploy). AC1 AFTER (full 33-key sweep): served_ok 31 of 33, failures UNCHANGED -- BP/_LN_Equity 404 and NG/_LN_Equity 404, same router-refusal body pre and post. Root cause (row AMGT_RESAPP-Z-W27-S10, ARMED, disarm_owner CTO/COO next-round cell): handler()'s /security/{key}/* route match requires len(rest)==3 after splitting rawPath on '/', so a raw slash inside the security_key is read as an EXTRA path segment and the request 404s at ROUTING, before render_pack.py or _read_drafting_document (this act's own fix) ever runs. This act's deployed code is verified correct and complete against its own covered claim (the LOCAL filesystem join is now path-safe, S3 key stays unsanitized) but cannot reach either slash-bearing key at all. Targeted 0-diff replan: No changes. Your infrastructure matches the configuration. AC1 (this order's own <status>): FAIL on its literal terms (2 of 2 slash keys still non-200; not empty failures). | CLOSED 20260917T235304Z |

## Log

- 20260917T225726Z OPENED by 0.9.0_WK_AMGT_RESAPP~27 with 1 leg(s)
- 20260917T235304Z LEG opal-amgt-scoped-api closed: PRE-ACT live get_function_configuration: CodeSha256 zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=, LastModified 2026-09-1
- 20260917T235332Z CLOSED -- all 1 legs proven
