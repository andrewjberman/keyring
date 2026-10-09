# Deploy Completion Record
**Date opened:** 2026-10-09T19:58:04.845129+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-a-2/CN-a-3: redeploy mdpf-gold-lambda at 55c3cc4642, one qa_local read (zero writes), then the on-demand run_class=backfill
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-assets portal/gold/mdpf/_code/mdpf-gold-lambda.zip -- the package built from pin 55c3cc4642, uploaded with its content-sha256 metadata | C1: BUILD_MANIFEST lists mdpf_gold_parquet.py and mdpf_gold_backfill.py; dim_mdpf_aum_metrics.py and mdpf_category_registry.py byte-equal to git show ff1a8867a6; the served object read back equal to the local build |  | OPEN |
| L3 | verify | the one {qa_local: true} invocation of mdpf-gold-lambda | C3: a response with status and a4_objects_built, no error naming mdpf_gold_parquet, and ZERO new objects under any mdpf/*/gold/ prefix of the four artifacts (pre/post counts with denominators) |  | OPEN |
| L4 | activation | the one {run_class: backfill} invocation -- the deliberate act that writes the dated history | C4: status backfill, planned > 0, tally written > 0, conflict 0, error 0, and one BACKFILL {scope}/{artifact} line per series in the log |  | OPEN |
| L5 | verify | the written partitions in the three firm buckets and the composite opal-data-mdpf | C5: one date=YYYY-MM-DD/data.parquet per legacy dated object with both counts printed; C6: the composite's partitions for the artifacts its legacy tree holds |  | OPEN |
| mdpf-gold-lambda | tf-lambda | aws_lambda_function.mdpf_gold | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T195804Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 5 leg(s)
