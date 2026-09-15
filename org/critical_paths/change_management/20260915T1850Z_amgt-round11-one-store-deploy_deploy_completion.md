# Deploy Completion Record
**Date opened:** 2026-09-15T18:50:51.674083+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-rj-10: THE DEPLOY AND THE LIVE READ -- round 11's one terraform act: two functions' code (pool reader, harvester validator, vendored jsonschema), two role policies (pool by prefix, articles table retired), one producer generation
**Authored by:** 0.9.0_WK_AMGT_RESAPP~19
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-amgt_resapp-11-2 branch commits (a30a75d74a builds + policies + rows; this ledger entry and its sentinel) | commit hashes on the worker branch |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip (OVERWRITTEN; the yang-lambda source_code_hash input read at PLAN time) | prior VersionId printed BEFORE the upload as the rollback pointer; head-object Meta.content-sha256 EQUAL to the local sha256 b64 after, non-zero Size |  | OPEN |
| L3 | activation | terraform apply of .scratch/rj10.tfplan into harvest/tfstate (0 to add, 4 to change, 0 to destroy; the co-signed four addresses) | Apply complete! line with 0 added, 4 changed, 0 destroyed |  | OPEN |
| L4 | verify | live config of opal-amgt-scoped-api and amgt-resapp-chatter-axis and both live role policies (read from IAM) | both Active with a CodeSha256 different from the pre-act values and LastModified today; articles-table 0, scan 0, wildcard 0; adapter pool-prefixes at least 9, producer exactly 4 |  | OPEN |
| L5 | verify | the producer's QA invoke (a generation + _CURRENT pointer per chatter axis) and the deployed adapter's served rankings/thesis/coverage reads | invoke 200 None; pointer per axis with generation_id, state, row_count, payload_hash, coverage_vintage and rank_sort ABSENT; rankings generation_id equal to the TRENDING pointer's; thesis 5 drafted sections SERVED; coverage store_item_count at least 1 |  | OPEN |

## Log

- 20260915T185051Z OPENED by 0.9.0_WK_AMGT_RESAPP~19 with 5 leg(s)
