# DEPLOY COMPLETION LEDGER -- estate-report-runner BLOB PREFETCH (NFRA_CTLPLN.TO-APPLY-33)

**Opened:** by `0.7.0_AE_CloudOps~NFRA1`, committed OPEN at `26e7986827` before the upload. CORRECTION at close: the header and file
name read 14:55Z, which was an estimate typed ahead of the clock; the upload returned at 14:53:25Z, so the commit preceded 14:53Z.
The order (open before act) held; the stamp did not.
**Status:** **CLOSED 2026-10-17T15:21Z** -- all four legs verified.
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

1. [x] PUT: one `put-object` at 14:53:25Z, instance `stopped` read at 14:53:22Z. New VersionId `LwDXDuLu9PZ.WHwKa.XV3Q4MQne9MR8i`
       (differs from the rollback's), 186,165 B, ETag `d4b80c85940e2288cf6050466236ff7e`, SSE AES256.
2. [x] READBACK by that VersionId: sha256 `62b0d74c...100d` == the pin's, 186,165 B both; one-byte mutant (offset 100) reads UNEQUAL.
3. [x] QA RUN: ad-hoc, one start via `lambda invoke estate-report-orchestrator` payload `{"mode":"daily-run","trigger":"manual"}` at
       14:54:44Z (`started:true`); instance launched 14:54:45Z, self-stopped 15:13:56Z (about 19 min, Kimi calls 1028 s of it). Log
       `s3://opal-estate-report/logs/2026-10-17T151354Z-i-0584e17d283fa7ef4.log` (VersionId `mnIGfWnxuNc4kdSXMgIDZiyUdVgFz1Sy`;
       the name carries the run's END time): `STAGE compile_resources kind=deterministic status=ok 4374 paths, 98 chain-resolved`;
       no Traceback, no CalledProcessError, no WARN line.
4. [x] MANIFEST `s3://opal-estate-report/manifest/2026-10-17.json` (VersionId `a5P0snAQuMq.k8iHMbZ51I5e3xMsQSYs`, written 15:13:55Z):
       `status` PENDING (awaiting CVO adjudication), not FAILED. It replaced the FAILED manifest (copy kept in the deliverables folder).

Unmeasured in the same run: strata C and A INSTRUMENT_FAILED; filed as row `NFRA_CTLPLN-S9138` (`32e21be4ae`). Not a leg of this entry.

## Close condition -- MET (the ad-hoc run is not production evidence)

Legs 1-4 verified, report written. First SCHEDULED exercise (the CVO's evidence, not this ad-hoc run): 2026-10-18 13:00Z.
No watcher, monitor or freshness checker is armed against it.
