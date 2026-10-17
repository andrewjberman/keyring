# DEPLOY COMPLETION LEDGER -- estate-report-runner reads the function-map folder (NFRA_CTLPLN.TO-APPLY-32)

**Opened:** 2026-10-17T00:45Z by `0.7.0_AE_CloudOps~NFRA1`, committed OPEN before the upload
**Status:** OPEN
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps~NFRA1/task_orders/NFRA_CTLPLN.TO-APPLY-32.estate-report-runner-function-map-upload-laptop.md`
(cell `CT-ch-1`, apply leg of built cell `CT-cg-1` @`bfbdc20d40`; CTO ruling msg 109774; row `NFRA_CTLPLN-W151-S2`)

## What

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`, carrying
`infra/aws/ec2/estate-report-runner/estate_report_runner.py` at the pin `bfbdc20d40`. No Terraform change, no policy change.

## Consumer of the key (one)

`estate-report.service` on the estate-report-runner instance, which pulls the key at every start
(`ExecStartPre=/usr/bin/aws s3 cp s3://${local.bucket_name}/code/estate_report_runner.py ...`,
`infra/aws/terraform/estate-report/instance.tf:233`). `estate-report-orchestrator` holds only
`ESTATE_REPORT_BUCKET` and `ESTATE_INSTANCE_ID` and never reads the key. One task family, no shared tag.

**ORDER DISCREPANCY (measured):** the order names instance `i-0512bd3cbaf602b7f`; `describe-instances` on it returns
`InvalidInstanceID.NotFound` (the host was replaced; ledger `20260909T1510Z`). The live consumer is
**`i-0584e17d283fa7ef4`** (tag `Name=estate-report-runner`, `Project=ESTATE_REPORT`), the same id the orchestrator's
`ESTATE_INSTANCE_ID` carries. Same service, same key: the named consumer is unchanged, only its id.

## Pre-state, measured 2026-10-17T00:3xZ

| | value |
|---|---|
| Served object | 182,986 B, ETag `3468e13b854c5e9af649c90cd1e11c39`, LastModified 2026-09-10T14:15:40Z, **VersionId `8pG9vs5I4CSGNVC8OcUy2Q9ARArGgumx`** |
| Served sha256 | `ee3bda020b355da6d63285bc910b8214f3e065430b59551de830d264ec51e163` (downloaded by VersionId) |
| Identical to | `git show 22ca10d25e:...estate_report_runner.py`, the last ledger's sha (`20260910T1412Z_estate-report-runner-os27-stratum-strings-serialized.md`): explained, not a STOP |
| Pin file | `git show bfbdc20d40:...estate_report_runner.py`, 184,027 B, sha256 `5e693559daa70406bd41d8d8290fc7add93fafaadba2d10500c260b7bf4a227d` |
| Diff served -> pin | 29 lines: two comment edits, `FUNCTION_MAP_REL` + `load_function_map()`, the `lambda_map` loader line. One repo commit between (`3ccb99154a`). `lib/opal_lambda_map.py` imports `json`, `os` only |
| origin/CLOUD | `infra/aws/lambda/ci/function-map/` 241 files, `lib/opal_lambda_map.py` present; `lambda-source-map.json` absent; absent-path control reads 0 |

## Window

Scheduler `estate-report-0900et` ENABLED `cron(0 9 * * ? *)` America/New_York, next start 2026-10-17 13:00Z.
Instance `i-0584e17d283fa7ef4` **stopped** (last run launched 2026-10-16 13:00:46Z, self-stopped 13:27:24Z). Upload at
~00:50Z: no run in flight, 12 h before the next pull, outside 12:50Z-13:30Z.

## ROLLBACK (recorded before the act)

`s3api copy-object` (or `put-object` of the downloaded bytes) from VersionId `8pG9vs5I4CSGNVC8OcUy2Q9ARArGgumx`,
sha256 `ee3bda02...e163`. Trigger: a RAISE or the retired path in the next start's log, or a read-back that differs.

## Legs

1. [ ] PUT: one `put-object` of the pinned file.
2. [ ] READBACK: object re-downloaded by its new VersionId, sha256 equals the pin's, VersionId differs from the rollback's,
       comparator proven able to fail (one-byte-changed copy reads UNEQUAL).
3. [ ] DISARM: the 13:00Z start's log shows the lambda hop reading `function-map/` with no WARN naming the retired map.
