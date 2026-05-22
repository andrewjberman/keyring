# Session Log — 0.7.0_AE_CloudOps — YALP_MDSRC.C1 — 2026-05-22

## Summary

Completed **YALP_MDSRC.C1** — the YCharts internal-API session/credential
pipeline. The prior base session had committed the capture-Lambda code +
Terraform (`beecbfe33`, `bd6d6322d`) but never deployed it (Docker was down).
This session: Docker confirmed up, built the `ycharts-session-capture`
container image, pushed to ECR, applied the Terraform. Deployed **dormant** —
EventBridge schedule DISABLED, zero invocations, no live YCharts call.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | `docker info` sanity check | Server 29.4.3, engine responsive (Andrew restarted Docker Desktop) |
| 2 | Build image | `docker build --provenance=false --platform linux/amd64` -> `ycharts-session-capture:lambda` (single manifest, Lambda-compatible; the default buildx manifest-list is NOT) |
| 3 | ECR login + tag + push | `:latest` digest `sha256:afc88b6277cc20f30e47cf6a44ab4bc346d1ee535eb4875cdfeb76e3eb68ea16`; ECR repo already existed in state |
| 4 | terraform plan | 9 to add, 1 to change, 0 to destroy |
| 5 | safe-apply (HALTGT clean) | 9 added, 1 changed, 0 destroyed |
| 6 | 0-diff replan | No changes. Infrastructure matches the configuration. |
| 7 | record-deploy + tag + push | `48da66b7c` ci: record deploy; tag `ycharts-pipeline-v1.1.0` |

Resources created: `aws_lambda_function.ycharts_session_capture` (Image),
its log group, IAM role + 2 policies + basic-execution attachment, the
probe->capture invoke policy, the EventBridge capture rule + target +
permission. `ycharts_session_probe` updated in-place (gains the
`CAPTURE_FUNCTION_NAME` env var so it can invoke the capture on a 403).

## Deployment Tags

| Pipeline | Tag | Recorded |
|----------|-----|----------|
| ycharts-pipeline | `ycharts-pipeline-v1.1.0` | `48da66b7c` |

## Verification — DORMANT (YCharts freeze respected)

- `ycharts-session-capture`: `State=Active`, `LastUpdateStatus=Successful`, `PackageType=Image`.
- EventBridge `ycharts-session-capture-schedule`: `State=DISABLED` (per `eventbridge.tf` — the 72h pre-emptive schedule is enabled only at dedicated-seat go-live).
- CloudWatch `Invocations` metric for `ycharts-session-capture`: **0** — the Lambda has never run. No live YCharts call made.
- terraform 0-diff replan: clean.

## Secret model (AC3 — reuse-or-rename decision)

Two distinct secrets, no duplication:
- `ycharts/credentials` — the capture's LOGIN input (`LOGIN_SECRET_ID`; expects `{username,password}`). Currently holds the C6 interim cookie bundle. The live automated login stays gated on the dedicated-seat creds landing here (Andrew procurement).
- `ycharts/session/current` — the capture's OUTPUT (`SESSION_SECRET_ID`; the freshness probe + C2's pull read it). New secret per A3 P2, created by the C1 Terraform (`secrets.tf`).

## Go-live (out of C1 scope)

The capture Lambda is deployed but dormant. Go-live = (1) the dedicated-seat
`{username,password}` placed in `ycharts/credentials`, (2) an on-demand live
login-capture test, (3) flip `ycharts-session-capture-schedule` to ENABLED.
That is the seat-arrival step — not C1.

## Compiler Tools

| Phase | Tool | Result vs expect |
|-------|------|------------------|
| 1 (before build) | `comp-iam service` on the capture Lambda | iam.tf was authored by the prior base session (`bd6d6322d`); the capture role grants `secretsmanager:GetSecretValue`/`PutSecretValue` resource-scoped to `ycharts/credentials` + `ycharts/session/current`, least-privilege. No new boto3 surface this session. |
| 2 (after iam.tf) | `comp-iam gaps` | 0 ycharts gaps — AC2 satisfied. NOTE: 2 unrelated pre-existing gaps surfaced in `mdpf-daily-trigger` (`s3:GetObject`/`s3:PutObject` via an `aws s3 cp` shell-out at `lambda_function.py:76`) — out of C1/YALP scope; recorded here for visibility, not actioned. |
| 3 (after deploy) | `comp-routes behaviors` | N/A — C1 is a credential pipeline; no CloudFront serving path changed. |

## Current State

| Item | Status |
|------|--------|
| C1 capture pipeline | COMPLETE — `ycharts-pipeline-v1.1.0`; capture Lambda Active, dormant |
| EventBridge capture schedule | DISABLED (go-live = seat arrival) |
| C1 RAVC2 | SENT — COO (with the 0-diff C2-release flag) + CC CTO |
| C1 TO | flipped to complete |

## Next Steps

1. [2.0.0_SA_COO] On the C1 0-diff flag — dispatch C2 (0.1.0_DS + 0.2.0_DS) + the D1 cutover.
2. [Andrew/procurement] Dedicated YCharts seat creds -> `ycharts/credentials`; then the go-live step (enable the schedule).
3. [~self] SEC1 ITEM 2.1 (FRED Secrets-Manager rewire) + ITEM 2.2 (JWT cutover-plan outline to COO).
