# MDPF Global v0 — Daily-Refresh Chain Codify: Design Brief

**Author:** 0.7.0_AE_CloudOps
**Date:** 2026-05-18
**Source of work:** `data/mdpf/scripts/RUNBOOK_AE_mdpf_daily_chain.md` (DS Base, commit `8d9325558`)
**Andrew directive (verbatim, via runbook):** "make sure the backend work is done, then 0.7.0_AE can make sure that system is codified for daily refresh/scheduling."
**GO chain:** COO design+prep GO -> DS Base deploy-gate cleared (origin/CLOUD @ `01a51e5d7`, identity_2 PASS end-to-end via `2e815b467`) -> full execution.
**Status:** DESIGN — pending RAVC1 (CTO + COO) before `terraform apply` (new pipeline module + new EC2 + new IAM = non-trivial provisioning per the cloud-ops pre-flight checklist).
**Frontend explicitly OUT** (Andrew-scoped): the `/aum/aggregate-mdpf` portal_data_proxy Lambda route stays PARKED.

---

## 1. What is being codified

A daily, idempotent, S3-artifact-model chain that keeps
`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` +
`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json` fresh.
4-stage DAG (runbook §"The daily chain"):

```
Stage 1 (parallel):  WS-B  wsb_49f_smartx_model_aua.py            --date {d} --upload
                      WS-D.1 build_mdpf_wsd2_etf_netassets_feeder.py --date {d} --upload
                      WS-D.2 wsd_partner_held_etf.py               --date {d} --upload
Stage 2:             WS-E  build_mdpf_wse_49f_non_model_aua.py     --date {d} --upload   (after WS-B)
Stage 3:             WS-A  mdpf_aggregate_aua.py                   --date {d} --source s3 --upload  (after S1+S2)
Stage 4:             rollup build_aggregate_aua_timeseries.py      --upload              (after WS-A)
```

CLI contracts validated against the actual argparse signatures of all 6 scripts on
`origin/CLOUD` — exact match, no runbook discrepancy.

### Failure semantics (runbook §"Failure semantics", encoded in the dispatcher)
- **WS-A exits 1 on any reconciliation ERROR and writes NO partition.** Treat non-zero WS-A
  as a hard failure: alert, do NOT run Stage 4 (rollup would just re-publish stale). The
  bandaid partition for that date stays as the floor (acceptable — not stale-to-zero).
- Feeder (Stage 1/2) failure -> skip Stages 3/4, alert.
- RPS lag ~3 days: WS-D.2 + WS-E roll-forward the latest available partition (contract §3.4) —
  expected, recorded in each artifact's `rps_date_used`/date-offset diag. NOT a failure.

## 2. Data access matrix (drives least-privilege IAM)

| Stage | Reads | Writes | External |
|-------|-------|--------|----------|
| WS-B | (SmartX REST API) | `opal-data-mdpf` | SmartX `api.smartxadvisory.com` + Secrets Manager `smartx/credentials/{username,password}` |
| WS-D.1 | `opal-data-etfs` `silver/netassets_daily.parquet` | `opal-data-mdpf` | none (S3-only) |
| WS-D.2 | `opal-data-bd` `schwab/silver/rps/date=*/` | `opal-data-mdpf` | none |
| WS-E | `opal-data-bd` `silver/allocations/`, `silver/fees/`, `gold/aua_certification/` + `opal-data-mdpf` (WS-B feed) | `opal-data-mdpf` | none |
| WS-A | `opal-data-mdpf` (all feeder prefixes) | `opal-data-portal-v2` `platinum/mdpf/aggregate_aua/{date}.json` | none |
| rollup | `opal-data-portal-v2` `platinum/mdpf/*` partitions | `opal-data-portal-v2` `platinum/mdpf/aggregate_aua_timeseries.json` | none |

## 3. Chosen infra shape (AE call per runbook delegation)

**Dedicated MDPF EC2 runner on the proven inf-gold-layer-runner pattern:**

```
EventBridge rule (cron, post-smartx-exporter offset, created DISABLED)
   -> mdpf-daily-trigger Lambda  (ec2:StartInstances on the stopped runner;
                                  poll SSM-online; ssm:SendCommand AWS-RunShellScript;
                                  DLQ on failure)
   -> mdpf-daily-runner EC2  (stopped between runs; SSM bootstrap S3-pulls
                              s3://opal-data-mdpf/code/{scripts,mdpf-daily-dispatch.sh};
                              runs the 4-stage DAG + failure semantics + telemetry;
                              `shutdown` -> instance_initiated_shutdown_behavior=stop)
```

Mirrors `infra/aws/terraform/inf-pipeline` (runner + trigger + DLQ) and
`infra/aws/terraform/smartx-pipeline` (EventBridge -> autostart Lambda -> EC2). New module
`infra/aws/terraform/mdpf-pipeline/`, new state key `mdpf-pipeline/tfstate`.

### Rejected alternatives
- **Reuse the existing `smartx-exporter` instance** (zero new EC2, SmartX creds already
  wired). REJECTED: it is an *imported* Docker/ECR instance with TF `ignore_changes` on
  user_data (cannot cleanly extend its bootstrap), its env lacks the pandas/pyarrow/mdpf
  deps, its IAM lacks `opal-data-mdpf` + `opal-data-portal-v2 platinum/mdpf` write +
  BD/RPS read, and co-locating two pipelines on one instance is an org anti-pattern with
  incident history. Isolation (separate IAM/SG/state) is the established org norm
  (inf-pipeline explicitly: "isolated IAM, KMS, and SG").
- **Lambda chain / Step Functions** (no EC2). REJECTED for v0: the 6 deliverables are CLI
  data scripts under `data/*/scripts/` — Rule 12/13 say data-script code runs on EC2
  pulled from S3, not refactored into Lambda handlers. Refactoring 6 scripts into
  handlers is against-grain + high-risk + out of scope for a v0 codify. (Step Functions
  is a reasonable v1.1 orchestration hardening — noted, not v0.)

### Sizing & cost
- `t3.medium` (2 vCPU/4 GB) — chain is ~5-10 min/weekday, mostly S3 + one ~2-3 min
  throttled SmartX pull. (NOT the inf runner's `c6a.4xlarge` — that is sized for the
  heavy INF gold chain; MDPF is light.)
- `instance_initiated_shutdown_behavior = "stop"` — root EBS (gp3, encrypted) persists
  across runs so the dep install is once-off; instance billed only ~10 min/weekday.
- gp3 50 GB encrypted root.

### Scheduling placement
- Anchor: existing `smartx-daily-export-trigger` = `cron(0 14 ? * MON-FRI *)` (14:00 UTC
  Mon-Fri). WS-B + the exporter both hit SmartX — the chain must run AFTER the exporter's
  SmartX reads complete.
- v0 = **fixed conservative offset**: `cron(0 15 ? * MON-FRI *)` (15:00 UTC, +60 min) as
  an independent post-exporter EventBridge target (runbook explicitly sanctions
  "independent post-exporter EventBridge target"). The exporter is a ~t3.small Docker
  export; 60 min is a safe completion margin for v0.
- v1.1 hardening (noted, not v0): chain off an exporter-completion signal rather than a
  fixed offset.
- **Rule created in `state = "DISABLED"`.** Enabled ONLY after a manual end-to-end
  validation run passes the runbook acceptance. No silent first-fire.

## 4. IAM (least-privilege — no `*` resource without justification)

**mdpf-daily-runner role:**
- `secretsmanager:GetSecretValue` on `arn:...:secret:smartx/credentials/*` (WS-B only).
- `s3:{GetObject,PutObject,ListBucket}` on `opal-data-mdpf` + `/*` (dedicated MDPF bucket;
  all feeders RW; code prefix lives here too).
- `s3:{GetObject,ListBucket}` on `opal-data-etfs/silver/*` (WS-D.1, read-only).
- `s3:{GetObject,ListBucket}` on `opal-data-bd` scoped to `schwab/silver/rps/*`,
  `silver/allocations/*`, `silver/fees/*`, `gold/aua_certification/*` (WS-D.2/WS-E,
  read-only).
- `s3:{GetObject,PutObject}` on `opal-data-portal-v2/platinum/mdpf/*` + `s3:ListBucket`
  with `s3:prefix` condition `platinum/mdpf/*` (WS-A write + rollup read/write). **Tightly
  scoped — opal-data-portal-v2 is the shared CloudFront origin; never bucket-wide.**
- `AmazonSSMManagedInstanceCore` (managed) for SSM agent.
- `logs:{CreateLogGroup,CreateLogStream,PutLogEvents}` for the dispatch log group.

**mdpf-daily-trigger Lambda role:**
- `ec2:StartInstances` scoped to the runner instance ARN; `ec2:Describe*` global (Describe
  has no resource-level scoping — standard, mirrors smartx autostart).
- `ssm:{SendCommand,GetCommandInvocation,ListCommandInvocations}` scoped to the runner
  instance + `AWS-RunShellScript` document.
- `sqs:SendMessage` to the DLQ; `logs:*` basic execution.

## 5. Deploy sequence (post-RAVC1 GO)

1. `safe-commit.sh` (author 0.7.0_AE_CloudOps, scoped pathspec): TF module + dispatch
   script + lambda src + source-map entry.
2. Push CLOUD.
3. S3 code-sync: `data/mdpf/scripts/**` + `mdpf-daily-dispatch.sh` ->
   `s3://opal-data-mdpf/code/` (S3-artifact model, Rule 12).
4. `terraform init` (new module/state) -> `plan` -> **RAVC1 plan diff to CTO+COO** ->
   `apply` -> re-`plan` 0-diff.
5. Manual end-to-end validation run (invoke trigger Lambda OR SSM-direct), verify runbook
   acceptance: `platinum/mdpf/aggregate_aua/{d}.json` `.reconciliation.overall == "PASS"`,
   `aggregate_aua_timeseries.json` `.as_of_last == {d}`.
6. ONLY on validation PASS: flip the EventBridge rule `DISABLED -> ENABLED` (1-attribute
   apply).
7. Tag `mdpf-pipeline-v1.0.0`, push `--follow-tags`. Update `pipeline_inventory.xml`.
   RAVC2 (CTO+COO) with full evidence.

## 6. Risks / open items
- WS-B SmartX ROPC creds in Secrets Manager (`smartx/credentials/*`) — confirm the runner
  role's SM read resolves the same secret the script expects (validation run proves it).
- WS-D.1 depends on `opal-data-etfs/silver/netassets_daily.parquet` being fresh — owned by
  ETFS_NETAST; runbook says "already produced 2026-05-18". The chain fails-loud if absent
  (Stage-1 fail semantics) — acceptable, not silent.
- First-run dep install on the runner (boto3/pandas/pyarrow/requests) — handled in
  user-data with an idempotent sentinel; persists via stop (not terminate).
- v0 fixed-offset scheduling assumes the exporter finishes < 60 min. v1.1: completion-signal.

## 7. Non-negotiables honored
Rule 1 (TF-only deploy) · Rule 5 (sized memory/timeout deliberately) · Rule 12 (S3-artifact
model, code pulled from S3, no inline code in SSM) · least-privilege IAM (no unscoped `*`)
· EventBridge created DISABLED (no silent first-fire) · RAVC1 before apply (non-trivial
provisioning) · frontend PARKED (Andrew scope-out).
