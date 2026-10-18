# Deploy Completion Record
**Date opened:** 2026-10-18T15:13:08.668271+00:00
**Status:** OPEN
**Deploy:** HVST-cl-2: opal-research-pull-enqueue redeployed by Terraform so a slash ticker's status object is written under the canonical prefix (source md5 45c83ddf74640e90368e8bebf712b52c); window from GO 15:10Z; rollback = previous artifact version, sha256 equal to CodeSha256 cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state of the function, artifact, queue and probe key (read only) | cl2_before.out holds the function config, the artifact version and sha256, the queue count, the absent probe key, the rollback copy equal to CodeSha256, and the scheduled-task read with its control |  | OPEN |
| U1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip | cl2_upload.out: one entry lambda_function.py equal to the source md5 45c83ddf, new VersionId read back with content-sha256 |  | OPEN |
| V1 | verify | after-state reads and the refusal probe | cl2_after.out and cl2_probe.out: CodeSha256 equals the new zip, env keys/runtime/handler equal, deployed code equals source, probe 400 with queue count and probe key unchanged |  | OPEN |
| W1 | verify | the one real invoke for BP/ LN Equity through the queue | cl2_slash_write.out: 202 with status.json under BP-SLASH-_LN_Equity and nothing under BP/_LN_Equity, or REFUSED_BY_QUEUE recorded plainly |  | OPEN |
| Z1 | verify | cl2_served.out, proof instance VALID, close committed | cl2_served.out ends with the five lines; proof checker last line VALID |  | OPEN |
| opal-research-pull-enqueue | tf-lambda | opal-research-pull-enqueue | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261018T151308Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
