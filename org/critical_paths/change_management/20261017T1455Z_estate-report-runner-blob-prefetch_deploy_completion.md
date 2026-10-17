# DEPLOY COMPLETION LEDGER -- estate-report-runner BLOB PREFETCH (NFRA_CTLPLN.TO-APPLY-33)

**Opened:** 2026-10-17T14:55Z by `0.7.0_AE_CloudOps~NFRA1`, committed OPEN before the upload.
**Status:** OPEN
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps~NFRA1/task_orders/NFRA_CTLPLN.TO-APPLY-33.estate-report-runner-blob-prefetch-upload-and-qa-run.md`
(issued by `2.0.0_SA_COO~C`, round 37, cell `CT-cj-1`, built cell `CT-ci-1` merged @7a33c62148)

## What

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py` carrying
`git show 7a33c62148:infra/aws/ec2/estate-report-runner/estate_report_runner.py`
(sha256 `62b0d74c17fc4eaf24dcfbdce126964cf126d1e618ccd8538acb18bef453100d`, read at the pin: equal).
THEN ONE ad-hoc QA start of the runner instance, followed to its self-stop. The QA run is part of the act.
No Terraform, IAM or instance-configuration change.

## Why

The run of 2026-10-17 13:00Z FAILED at 13:03:55Z in `load_function_map`: `git checkout CLOUD -- infra/aws/lambda/ci/function-map lib/opal_lambda_map.py`
returned 128 on a blobless clone. The new file prefetches the blobs in one `git fetch --filter=blob:none origin <ids>` before the checkout.

## Consumer of the key (the ONLY one)

`estate-report.service` on the instance named `estate-report-runner` (looked up by Name tag; id today `i-0584e17d283fa7ef4`, state `stopped`),
`ExecStartPre=aws s3 cp s3://opal-estate-report/code/estate_report_runner.py` at every start. `estate-report-orchestrator` (Lambda) starts the instance
and never reads the key. One task family, no shared tag.

## Window

Scheduler `estate-report-0900et` ENABLED `cron(0 9 * * ? *)` America/New_York, input `{"mode":"daily-run"}`, target the orchestrator Lambda.
Next scheduled fire 2026-10-18 13:00Z. Window used: 2026-10-17 14:5xZ onward, outside 12:50Z-13:30Z, instance `stopped` (read 14:51Z).

## ROLLBACK, recorded before the act

| | value |
|---|---|
| Current object | 184,027 B, ETag `329134bd5763b9c5fa4f180d0999d6ec`, LastModified 2026-10-17T00:43:55Z, VersionId `HIrQD8nolfYS_30vrMXBXCZJ0_EnqqPz` |
| Current sha256 | `5e693559daa70406bd41d8d8290fc7add93fafaadba2d10500c260b7bf4a227d` = `git show bfbdc20d40:<path>` sha256 (equal, measured) |
| Rollback | `s3api copy-object` from VersionId `HIrQD8nolfYS_30vrMXBXCZJ0_EnqqPz` (or `put-object` of the bytes), in session |
| FAILED artifacts copied | `org/tier2_senior/0.7.0_AE_CloudOps~NFRA1/deliverables/TO-APPLY-33_FAILED_manifest_2026-10-17.json` (S3 VersionId `iyjzyB3MYWxH2mipyyl5K9MEJrFtr0yP`) and `..._FAILED_run_2026-10-17T130355Z-i-0584e17d283fa7ef4.log` (VersionId `Fu7iSxQDBpu5F.khWzJ8ZWVCwHkeKFWt`) |

## Related open entry

`org/critical_paths/.open_deploys/estate-report-runner-function-map-20261017.json` (TO-APPLY-32) has its DISARM leg open; the 13:00Z run it names
FAILED. This act is the repair; the issuer decides that entry's disposition. Not touched here.

## Legs

1. [ ] PUT: one `put-object` of the pinned bytes; new VersionId differs from `HIrQD8nolfYS_30vrMXBXCZJ0_EnqqPz`.
2. [ ] READBACK: re-downloaded sha256 equals the pin's; one-byte-changed copy reads UNEQUAL.
3. [ ] QA RUN: one ad-hoc start; log read for `STAGE compile_resources` and any Traceback/CalledProcessError; instance self-stopped.
4. [ ] MANIFEST: `manifest/<date>.json` status other than FAILED.

## Close condition

Legs 1-4 verified, report written. First SCHEDULED exercise (the CVO's evidence, not this ad-hoc run): 2026-10-18 13:00Z.
No watcher, monitor or freshness checker is armed against it.
