# Deploy Completion Record
**Date opened:** 2026-10-18T15:13:08.668271+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T153947Z
**Deploy:** HVST-cl-2: opal-research-pull-enqueue redeployed by Terraform so a slash ticker's status object is written under the canonical prefix (source md5 45c83ddf74640e90368e8bebf712b52c); window from GO 15:10Z; rollback = previous artifact version, sha256 equal to CodeSha256 cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state of the function, artifact, queue and probe key (read only) | cl2_before.out holds the function config, the artifact version and sha256, the queue count, the absent probe key, the rollback copy equal to CodeSha256, and the scheduled-task read with its control | PASS. cl2_before.out 15:16Z-15:18Z: source md5 45c83ddf.. at 349e7ee0da; live CodeSha256 cWiraC3E.. = rollback zip (VersionId pHqpZEyjzx1PPaeKAGgJUIB.1hQUU.v2) sha256 b64; queue 0/0/0; probe key absent (control found); 207 scheduled tasks read, none applies Terraform; 38 tests pass | CLOSED 20261018T153506Z |
| U1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip | cl2_upload.out: one entry lambda_function.py equal to the source md5 45c83ddf, new VersionId read back with content-sha256 | PASS. cl2_upload.out 15:19Z: zip 3090 B, one entry lambda_function.py sha256 ad395e19.. equals the source; VersionId oV0CTP3MzbVWkp8Rsw7YuDVnRF_.e6kn content-sha256 7c4gYrZHxrNDhf2bqv3wo2JTUWdUxt/BeDFQsp33fx4= read back and re-downloaded by VersionId; previous version pHqpZEyjzx1PPaeKAGgJUIB.1hQUU.v2 still stored | CLOSED 20261018T153506Z |
| V1 | verify | after-state reads and the refusal probe | cl2_after.out and cl2_probe.out: CodeSha256 equals the new zip, env keys/runtime/handler equal, deployed code equals source, probe 400 with queue count and probe key unchanged | PASS. cl2_after.out: env keys, runtime, handler, memory, timeout, role, layers, arch equal to before; cl2_probe.out 15:25:44Z: one invoke of ZZ-SLASH-PROBE US Equity returned 400 'missing or invalid ticker in request body', queue 0/0/0 before and after, no object under packs/ZZ-SLASH-PROBE | CLOSED 20261018T153506Z |
| W1 | verify | the one real invoke for BP/ LN Equity through the queue | cl2_slash_write.out: 202 with status.json under BP-SLASH-_LN_Equity and nothing under BP/_LN_Equity, or REFUSED_BY_QUEUE recorded plainly | PASS on the order's step 5b criteria. cl2_slash_write.out: ONE invoke of BP/ LN Equity at 15:26:59Z returned 202; packs/BP-SLASH-_LN_Equity/status.json exists (REQUESTED, security_key raw BP/_LN_Equity); nothing at packs/BP/_LN_Equity/status.json; one message with the raw security_key enqueued (peeked once, not consumed). NOT shown: the box consumer had not drained it by 15:33Z (status still REQUESTED); row AMGT_HARVST-D1-S63; the issuer regrades | CLOSED 20261018T153506Z |
| Z1 | verify | cl2_served.out, proof instance VALID, close committed | cl2_served.out ends with the five lines; proof checker last line VALID | PASS. cl2_served.out ends PLAN_ONE_CHANGE=PASS, DEPLOYED_BYTES_EQUAL_SOURCE=PASS, ENV_AND_CONFIG_UNCHANGED=PASS, REFUSAL_PROBE_NO_SIDE_EFFECT=PASS, SLASH_WRITE_CANONICAL=PASS; proof instance AMGT_HARVST.TO-HVST-cl-2.the-pull-enqueue-lambda-is-redeployed-with-the-canonical-status-key.proof_of_spec.json checker last line on the committed bytes at 95ed6ae24e: VALID (rc=0); deliverables 95ed6ae24e LOCAL (origin box/dell1 63bb0aa6d0, push is integrator-only). NOT PROVEN by this grade: the box consumer had not drained the one queued BP message by 15:39:26Z (status REQUESTED, queue 1; row D1-S63), so 'the drained pull lands normally' is open for the issuer; a non-ASCII refusal is shown offline only; the source-map stamp was refused (no function-map row, row D1-S62). Rollback: version pHqpZEyjzx1PPaeKAGgJUIB.1hQUU.v2 (CodeSha256 cWiraC3E..) | CLOSED 20261018T153947Z |
| opal-research-pull-enqueue | tf-lambda | opal-research-pull-enqueue | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | PASS. cl2_plan.out: 53 resource_changes = 52 no-op + 1 update, only module.harvest_enqueue.aws_lambda_function.this (last_modified, s3_object_version, source_code_hash); cl2_apply.out: safe-apply of the saved plan, Apply complete 0 added 1 changed 0 destroyed at 15:24Z; cl2_after.out: CodeSha256 7c4gYrZHxrNDhf2bqv3wo2JTUWdUxt/BeDFQsp33fx4= equals the new zip, deployed code byte equal to the source, plan after: No changes | CLOSED 20261018T153506Z |

## Log

- 20261018T151308Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
- 20261018T153506Z LEG S0 closed: PASS. cl2_before.out 15:16Z-15:18Z: source md5 45c83ddf.. at 349e7ee0da; live CodeSha256 cWiraC3E.. = rollback zip (Vers
- 20261018T153506Z LEG U1 closed: PASS. cl2_upload.out 15:19Z: zip 3090 B, one entry lambda_function.py sha256 ad395e19.. equals the source; VersionId oV0
- 20261018T153506Z LEG opal-research-pull-enqueue closed: PASS. cl2_plan.out: 53 resource_changes = 52 no-op + 1 update, only module.harvest_enqueue.aws_lambda_function.this (las
- 20261018T153506Z LEG V1 closed: PASS. cl2_after.out: env keys, runtime, handler, memory, timeout, role, layers, arch equal to before; cl2_probe.out 15:2
- 20261018T153506Z LEG W1 closed: PASS on the order's step 5b criteria. cl2_slash_write.out: ONE invoke of BP/ LN Equity at 15:26:59Z returned 202; packs/
- 20261018T153947Z LEG Z1 closed: PASS. cl2_served.out ends PLAN_ONE_CHANGE=PASS, DEPLOYED_BYTES_EQUAL_SOURCE=PASS, ENV_AND_CONFIG_UNCHANGED=PASS, REFUSAL
- 20261018T153947Z CLOSED -- all 6 legs proven
