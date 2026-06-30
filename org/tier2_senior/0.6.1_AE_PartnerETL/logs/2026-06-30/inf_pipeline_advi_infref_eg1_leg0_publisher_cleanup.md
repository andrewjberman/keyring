# ADVI_INFREF EG-1 LEG-0 — inf-portal-publisher cleanup (F1+F2) LANDED

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, IMPLEMENT
**Agent:** 0.6.1_AE_PartnerETL (inf-refactor AE lane)
**Date:** 2026-06-30
**Assignment:** ADVI_INFREF EG-1 (writer-map confirm outcome) — DS~A spec'd (20260630T180636Z); CTO arch-gated + co-signed (20260630T181226Z)
**Status:** LANDED + GREEN-pending-CVO. inf-pipeline-v1.7.78.

---

## Summary

The EG-1 writer-map cleanup on `inf-portal-publisher`. ~A shipped the DS half (`3980bfd96`, INF_D_00 aua_by_tax_status removed); I landed the Lambda/TF half — removing the publisher's FE-dead + dead-code writes so the single-writer invariant is explicit (INF_D_04 sole header_metrics writer). Code-only, non-destructive (the orphan S3 object delete was DEFERRED by CTO to the RT publisher-decommission batch with Andrew-confirm). Deployed end-to-end with full discipline; verified live.

## What landed (source-verified before deploy — Rule 22)

- **F2 — removed dead `build_header_metrics()`** (`infra/aws/lambda/inf-portal-publisher/lambda_function.py` L569-650 + section comment): grep proved ZERO call-sites (dead since the 05-12 INFPUBLISHERDEDUP). INF_D_04 remains sole header_metrics writer -> single-writer invariant intact.
- **F1 — removed FE-dead `aua_by_tax_status` snapshot WRITE**: build block + print fragment + write dict-entry + module docstring line. `comp-platinum reverse platinum/firm/snapshots/aua_by_tax_status.json` -> "CONSUMED BY: (no components found)" independently corroborated FE-unconsumed. The SEPARATE `tax_status` FILTER block (different artifact) + the other 3 snapshots (architect/state/region) UNTOUCHED. tax_rows fully self-contained (zero dangling refs post-removal, assertion-verified).
- **+2 gate-forced removals**: pre-existing F841 dead local loads (`cp`, `aum_snapshot`) in the handler — the mandatory ds-commit-gate (ruff) blocked on them; confirmed pre-existing via ruff-on-HEAD, behavior-preserving (assigned-never-read). Flagged transparently in the commit.
- **Source-map infra-debt fix**: the `inf-portal-publisher` entry was a STRAY TOP-LEVEL legacy entry (old schema, NOT under `functions{}`) -> the canonical `build-and-upload.sh` (which reads `sm.functions`) couldn't see it ("No zip-based functions found"). Moved it under `functions{}` + upgraded to current schema (source_dir/handler/runtime/tf_file/tf_resource/s3_bucket) so the builder + CI drift-detection now cover it.

## Deploy (per-leg discipline, ledger 20260630T1821Z, 4 legs)

- Edit (assertion-guarded Python) -> ds-commit-gate green -> safe-commit source (`ef320f919`).
- `build-and-upload.sh inf-pipeline inf-portal-publisher`: zip 12K sha256 `03XZdv2/c+2nNZ8gXqNSY24jSTwFFdfGIfN+HwkQE0s=` uploaded to `opal-313476888478-lambda-artifacts/inf-pipeline/inf-portal-publisher.zip`. safe-commit source-map (`9eaa91688`).
- `terraform plan` -> 0 add / 1 change / 0 destroy (publisher Lambda code only: s3_object_version + source_code_hash). safe-apply HALTGT -> "Apply complete! 0 added, 1 changed, 0 destroyed."
- **LIVE verify (Rule 22):** `get-function-configuration CodeSha256 = 03XZdv2...` == new artifact (deployed Lambda runs the F1+F2 code). 0-diff re-plan "No changes."
- `record-terraform-deploy.sh` (CHANGELOG + source-map). tag `inf-pipeline-v1.7.78` pushed --follow-tags (`ea700f1d2`). Ledger CLOSED all-4-legs-proven. Never half-landed.

## Decisions / scope

- s3 rm of the orphan `aua_by_tax_status.json` DEFERRED (CTO): not done here; folds into the RT/SPEC-4 publisher-decommission batch with Andrew-confirm (CLAUDE.md autonomy: S3 deletes are human-confirm; the object is FE-unconsumed = harmless meanwhile).
- CVO independently verifies no-consumer-break (requested 182944Z) — closes the leg.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-which` | route "where is publisher + who consumes aua_by_tax_status" | -> comp-platinum reverse / pipescript --resource |
| `comp-platinum reverse <s3_key>` | FE-consumer check on aua_by_tax_status (F1 dead-proof) | "CONSUMED BY: (no components found)" -- FE-dead corroborated |
| `comp-grep` | locate inf-portal-publisher source + lambdas.tf wiring | found source (infra/aws/lambda/inf-portal-publisher/, NOT under inf-pipeline/) |
| ruff via `ds-commit-gate.sh` | mandatory pre-commit gate (Rule 14) | caught 2 pre-existing F841 -> fixed |
| `aws lambda get-function-configuration` | LIVE CodeSha256 ground-truth (Rule 22) | 03XZdv2... == new artifact |
| `deploy_ledger.py` | 4-leg deploy-completion ledger | opened + closed all-proven |

## Next

CVO sign-off closes EG-1 LEG-0. Then Leg-2 (the single-pull-stage + atomic-per-dim de-convert) when ~A starts authoring the pull-stage module (perf/txn first). Leg-1 (two-flow EventBridge) already GREEN. inf-AE P1 progressing: EG-1 + Leg-1 landed; Leg-2 sequenced.
