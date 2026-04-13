# Yang Benchmarks SI Unannualize — Deploy Log

**Date:** 2026-04-13
**Agent:** 0.5.0_AE_OpalETL
**Source commit (DS):** `bc6f4ccb` (0.4.0_DS_ClientPlatform)
**Brief:** `docs/briefs/ae-brief-yang-benchmarks-si-unannualize.md`
**Authorization:** DS deploy request via MCP msg 20260413T153706Z; Andrew-authorized fix per brief.

## Summary

Deployed 2 yang-pipeline Lambdas after DS removed a double-annualization bug in the SI column of the benchmark heatmap. TF apply at 0-diff. Tagged `yang-v2.3.7`.

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | Pre-build cleanup commit | `<hash>` chore: post-migration cleanup (state file + lock) |
| 2 | build-and-upload.sh yang-pipeline yang-model-portfolio-benchmarks | SHA256 `XhddnWgnLKe2TtcFdMfUj5UwNb9ou8DvjsudMXKp0Qs=` |
| 3 | build-and-upload.sh yang-pipeline yang-generate-benchmark-returns | SHA256 `ZoMXOGZKJg3cDaKSWZcFrdrzdfwDdJrSqiO1QnrERak=` |
| 4 | Commit source map | `77a0d684` ci: upload yang benchmark artifacts [skip ci] |
| 5 | terraform plan | 0 add, 2 change, 0 destroy (exactly the 2 target lambdas) |
| 6 | terraform apply | `542681ea` apply successful |
| 7 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 8 | record-terraform-deploy.sh --version yang-pipeline-v2.3.7 | `a41790f0` (CHANGELOG.json write failed but source map committed) |
| 9 | git tag -a yang-v2.3.7 + git push --follow-tags | pushed to origin/CLOUD |
| 10 | MCP notify DS + DT | both delivered |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| yang-pipeline | `yang-v2.3.7` | `a41790f0` |

## Verification

- Terraform plan pre-apply: 0 add, 2 change, 0 destroy — only the two target Lambdas (`yang-model-portfolio-benchmarks`, `yang-generate-benchmark-returns`).
- Terraform plan post-apply: "No changes."
- S3 artifacts present: `s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-model-portfolio-benchmarks.zip` (new version), `s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-benchmark-returns.zip` (new version).
- Output validation (per DS brief) pending next PKL refresh / Step Functions run. Expected: UST model SI 9.52 (was 4.79), LTC 33.32 (was 15.93); benchmark indexes analogously uplifted (~2x). S3 JSON still carries old values until refresh.

## Compiler Tools

Not applicable — no cross-layer tracing required. Single one-block deletion in two files by DS; my role was build + deploy only. comp-pipescript io was not run because the scope explicitly limited to already-validated source.

## Anomaly

- `record-terraform-deploy.sh` printed "CHANGELOG.json write failed — source map update still committed". Source map + commits are correct; CHANGELOG.json for yang-pipeline may need manual follow-up. Not blocking.

## Next Steps

- [DS] Run verification query on benchmark_returns.json after next PKL refresh to confirm SI values match brief expectations.
- [DT] Merge portal-side PR (annualizeSI removal) after S3 verification passes; deploy to PROD + CloudFront purge.
- [0.5.0_AE] Follow up on record-terraform-deploy.sh CHANGELOG.json write failure (next session).
