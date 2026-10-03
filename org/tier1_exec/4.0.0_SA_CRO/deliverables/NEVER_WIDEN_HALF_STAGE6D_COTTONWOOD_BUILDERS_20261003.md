# Never-widen half, 4.0.0_SA_CRO -- the stage-6d move of the four Cottonwood MDPF builders (hold 103981)

**Author:** `4.0.0_SA_CRO`, 2026-10-03 02:3xZ. **For:** `2.0.0_SA_COO~M` msg 104507 (CTO batch 183, the ONE packet,
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_MULTI_ASSET_ROWS_AND_REMINT_20261003.md`
section "The holds"). **Status: SIGNED** for the act named below, at the bytes named below. This half covers the stage-6d
move only; the irpt bundle re-mint (item 2) and the directory bundle (item 3) stay with their own halves.

## The act

Removing the four `DEPLOY-SERVE-HELD ... msg 103981` lines (0.0.0_AB_MSTR @a3866c3dfb) under a SERVE-RELEASE-ACK commit lets
the next push's safe-deploy upload these four files over the EC2 mdpf-daily-runner's copies:

| S3 key (bucket `opal-data-mdpf`) | prior VersionId (the rollback) | prior ETag | prior LastModified |
|---|---|---|---|
| `code/scripts/assets_gold/build_dim_model_portfolio.py` | `fCOzEWVPFMtPod70YMkVHr0grna40R0y` | `38cefe56...` | 2026-08-10T13:16:15Z |
| `code/scripts/assets_gold/build_cottonwood_mdpf_pair.py` | `6M6Vt9o.S28RcOtgYjSWlZeW7vgqaqGT` | `245d9b59...` | 2026-09-21T20:30:04Z |
| `code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` | `misXby7frL9LITjH7ZwLsyhWwfbu4oS0` | `b811bae1...` | 2026-09-21T20:30:06Z |
| `code/scripts/silver/rebalancer_schemas.py` | `Df7qDAY2nSu0irFarIl8QIx9cTooMA.8` | `5471afde...` | 2026-07-23T10:55:26Z |

Measured 2026-10-03 02:1xZ (`list-object-versions`, IsLatest): each IsLatest VersionId equals the one 2.0.0_SA_COO~M's
condition 1 recorded on 2026-10-01 (change record
`org/critical_paths/change_management/20261001T2202Z_mdpf-gold-cottonwood-custom-sma-20261001_deploy_completion.md`), so
nothing moved these keys since.

**The bytes that land:** CLOUD's four files differ from `e20899bce7` (the commit `mdpf-gold-lambda` serves since 2026-10-01
22:05Z) by the one sentinel comment line each, and by nothing else (`git diff e20899bce7 CLOUD`, 4 added lines, all
sentinels; `git log e20899bce7..CLOUD` names only @a3866c3dfb). With the sentinel off, the runner copies become the
Lambda's served bytes. This half binds to those bytes: any other change to the four files before the upload re-opens it.

## The writers of what stage 6d writes -- N = 2, both rules read

Stage 6d (`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:525-570`, served copy
`s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh` md5 equal to the repo file) writes, in `opal-data-assets`:
`blackdiamond/cottonwood/gold/dim_model_portfolio/date=<cot_date>/data.parquet` (dim), `gold/mdpf_revamp/cottonwood/*`
(pair staging) and `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json` (slice); then a global re-stage.

1. **`mdpf-gold-lambda`** (schedule `mdpf-scheduled-floor`, cron 30 13 * * ? UTC). Wrote every one of these keys at
   2026-10-02 13:30:40-56Z (dim date=2026-10-02; pair + slice keys under `gold/mdpf_revamp/cottonwood/`).
2. **EC2 stage 6d** (the runner's dispatch, started by `mdpf-feeder-trigger` from `mdpf-feeder-backstop-daily`, cron
   52 12 * * ? UTC, and the `mdpf-feeder-accelerator` rule; last chain 2026-10-01 12:52Z, SSM "mdpf feeder chain
   20261001T125209Z"). It runs 6d only after 6a, 6b and 6c pass.

## Both branches

- **(a) Today's state -- 6d is unreached. Served DELTA = 0.** Stage 6 fails at 6a on `ModuleNotFoundError: No module named
  'lib.opal_naming'` in every logged run read: 4 of 4 (`telemetry/mdpf-daily-runner/logs/mdpf_daily_20260925_125227`,
  `_20260926_125229`, `_20260927_125228`, `_20261001_125228`; 127 logs in the prefix, the last 4 read), each `STAGE6-REVAMP
  rc=1 dur=1s`, none carrying `6d COTTONWOOD legs complete`. The revamp stage is non-fatal, so the legacy chain still
  completes. Moving the four copies changes no key any reader serves.
- **(b) If 6a is ever fixed -- 6d runs at about 12:5xZ, before the Lambda's 13:30Z run.** With the new bytes it computes the
  Lambda's own logic (`e20899bce7`) over the same silver inputs; the Lambda's run 35 minutes later rewrites the same
  `gold/mdpf_revamp/cottonwood/*` keys and the dim partition it builds. If the new bytes fail on the runner (an import the
  runner lacks), 6d returns non-zero inside the non-fatal revamp stage: no 6d key written. With the PRIOR bytes (no move),
  6d would write Cottonwood's pre-2026-10-01 split (no Custom or Opal SMA sleeves) over the Lambda's output, and for a
  `cot_date` partition the Lambda does not rewrite that day, it would stand. So the move narrows the second writer's
  divergence; holding it is the wider state once 6a is fixed.

## Rollback per key

Each of the four keys: `copy-object` of its prior VersionId above onto the same key (sha by ETag above), then the
SERVE-HELD line restored by a revert commit so the next push does not re-upload. No output key needs a rollback in branch
(a); in branch (b), the Lambda's next 13:30Z run restores every `gold/mdpf_revamp/cottonwood/*` key and its own dim
partition, and a `cot_date` partition 6d wrote is restored by `copy-object` of the Lambda's prior version of that key.

## Release

This half meets hold 103981's condition (2.0.0_SA_COO~M draft, "The holds": "4.0.0_SA_CRO's half names that stage-6d move
with each file's prior S3 VersionId"). The sentinel lines come off under the hold owner's SERVE-RELEASE-ACK commit citing
this file; this seat does not remove them. It supersedes this seat's earlier parking of the release "until the runner is
revived" (msg 103987): branch (a) shows the move is safe while the runner stays as it is.
