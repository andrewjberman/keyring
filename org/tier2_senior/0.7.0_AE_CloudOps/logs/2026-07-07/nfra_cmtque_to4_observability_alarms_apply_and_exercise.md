# 0.7.0_AE_CloudOps~B -- NFRA_CMTQUE TO-4: observability + alarms, applied + exercised live

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

Window: ~1420Z -> ~1520Z, following COO's DRIVE GO Wave-1 (post-reboot restart). Design was
authored 2026-07-06 (f9fac368c, `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_CMTQUE_phase0_grounding_and_scaffold.md`
sec7) and held for box recovery; this window builds + applies + exercises it.

## Summary

1. **Wired `cw_metric()` to real `aws cloudwatch put-metric-data`** (`.tools/commit-worker.sh`),
   replacing the local-file-only stub. Backgrounded (fire-and-forget) so a slow/throttled
   CloudWatch API never stalls the serial commit loop. `worker_liveness`/`queue_depth` (emitted
   every daemon-loop iteration) rate-limited to 20s via a per-metric last-emit file; event metrics
   (committed/rejected/dlq/recovered/latency) fire unthrottled, once per request.
2. **Wired `CommitLatencyMs`** (design listed it, no emission existed). `ENQUEUE_TS` already
   existed in the request format (`cq_enqueue`) but was never read back. Added
   `REQ_ENQUEUE_TS` to `cw_parse_request` + a new `cq_iso_to_epoch` helper (GNU `date` needs
   dashes/colons; `ENQUEUE_TS` is compact-ISO) + a latency computation at result-classification
   time, covering all three outcomes (committed/rejected/errored).
3. **Provisioned 4 CloudWatch alarms** (`infra/aws/terraform/shared-infra/cmtque-alarms.tf`):
   WorkerDown (CRITICAL, missing-data>=3min), DlqDepth>=1, QueueBacklog (placeholder threshold),
   CommitLatencyHigh (placeholder threshold). All route to the existing
   `opal-infrastructure-alerts` SNS topic (data source, not a new resource).
4. **IAM: no new grant needed.** The worker is a LOCAL daemon (design sec7.4 flags this as
   outside comp-iam's TF-Lambda/EC2-role scope). Live-verified (not config-read): the host
   identity (`Andrew_Berman` IAM user, group `AdministratorAccessOpalCapital`) already has
   `cloudwatch:PutMetricData` via a real `put-metric-data` call that succeeded (exit 0).
   `comp-iam gaps` returns 0 CMTQUE-related hits (clean).
5. **Exercised both required alarms live** (AC1/AC2 -- "exercised, not config-read"):
   - Launched the real commit-worker daemon on the actual repo, manufactured a genuinely
     CORRUPT request (missing PATH field -> `cw_parse_request` returns 1 -> the real
     `CORRUPT request -> DLQ` code path, not a synthetic/mocked trigger) -> `DlqDepth=1`
     datapoint landed in CloudWatch (`get-metric-statistics` confirms Sum=1.0) -> **`cmtque-dlq-depth`
     alarm transitioned OK->ALARM** (confirmed via `describe-alarms`), then self-resolved to OK
     once the transient event passed (correct behavior for a single-event alarm,
     evaluation_periods=1/period=60).
   - Killed the worker daemon (`kill $(cat worker.pid)`) to start the missing-data clock on
     `WorkerLiveness` for the real `Repo=ajb_workspace` dimension. **WorkerDown alarm-transition
     confirmation is IN PROGRESS as of this log** (needs the full 3x60s missing-data window;
     tracked via a background poll, notification pending) -- see Next Steps.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-iam gaps` | check the new CloudWatch/SNS grant for gaps (TO requirement 3) | 0 CMTQUE-related hits -- clean (no new IAM grant created; existing admin-group host identity already covers `cloudwatch:PutMetricData`, live-verified) |
| `comp-which/rail` | HUD-nudged on `.tf`/`aws` inspections; used native `Read`/`Grep` for source-file lookups (SNS-topic-reference pattern, existing-alarm style) + operational `aws`/`terraform`/`codebuild`/`logs` calls (deploy + live-state grounding, not gated) | rail respected; a couple of `# rail-checked:` markers on literal-string ARN lookups no comp-tool covers |

## Deployment Sequence (AE)

| Step | Action | Result |
|---|---|---|
| 1 | Commit source (`da46c14bc`) | `.tools/commit-worker.sh` + `commit_queue_lib.sh` + new `cmtque-alarms.tf` |
| 2 | `git push origin CLOUD` | `393a8b723..da46c14bc` |
| 3 | `terraform init` (backend needed reinit) + `terraform plan` | 4 to add, 0 to change, 0 to destroy |
| 4 | `.tools/safe-apply.sh` | Apply complete: 4 added, 0 changed, 0 destroyed |
| 5 | 0-diff verify (scoped `-target` on the 4 new resources + the data source) | "No changes. Your infrastructure matches the configuration." (unrelated pre-existing drift on `infra_snapshot`/`infrastructure_snapshot_policy` noted, NOT mine -- out of scope) |
| 6 | Update core doc | deferred to TO close (pipeline_inventory.xml) -- see Next Steps |
| 7 | Tag + push | `shared-infra-v1.34.0`, pushed `--follow-tags` |
| 8 | Alarm-fire exercises | DlqDepth CONFIRMED (ALARM observed); WorkerDown IN PROGRESS |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| shared-infra | v1.34.0 | da46c14bc |

## Verification

```
$ aws cloudwatch get-metric-statistics --namespace Opal/CommitQueue --metric-name Committed \
    --dimensions Name=Repo,Value=cw_selftest_171237 --period 60 --statistics Sum ...
{"Datapoints": [{"Sum": 1.0, "Unit": "Count"}]}   # selftest emission, real CloudWatch, not local-only

$ aws cloudwatch get-metric-statistics --namespace Opal/CommitQueue --metric-name CommitLatencyMs \
    --dimensions Name=Repo,Value=cw_selftest_171237 --period 60 --statistics Average Maximum ...
{"Datapoints": [{"Average": 7500.0, "Maximum": 8000.0, "Unit": "Milliseconds"}]}

$ aws cloudwatch get-metric-statistics --namespace Opal/CommitQueue --metric-name DlqDepth \
    --dimensions Name=Repo,Value=ajb_workspace --period 60 --statistics Sum ...
{"Datapoints": [{"Sum": 1.0, "Unit": "Count"}]}   # the real DLQ exercise on the actual repo

$ aws cloudwatch describe-alarms --alarm-names cmtque-dlq-depth --query "...StateValue..."
ALARM   # observed mid-exercise, then self-resolved OK once the event passed (correct)
```

## Files Modified

- `.tools/commit-worker.sh` -- `cw_metric()` real CloudWatch wiring + rate-limiting; `REQ_ENQUEUE_TS`
  parse; `CommitLatencyMs` computation at result-classification.
- `.tools/commit_queue_lib.sh` -- `cq_iso_to_epoch()` helper.
- `infra/aws/terraform/shared-infra/cmtque-alarms.tf` (new) -- 4 alarms + the `ops_alerts` data source.

## Blockers

None load-bearing. WorkerDown alarm confirmation is in-progress (mechanical wait on a 3-minute
missing-data window), not blocked on anything external.

## Current State (zero-context handoff)

- All 4 alarms LIVE on the real `Repo=ajb_workspace` dimension. `cw_metric` emission proven live
  end-to-end (selftest + the real DLQ exercise both landed real CloudWatch datapoints).
- Worker daemon is currently DOWN (intentionally, for the WorkerDown exercise) -- callers degrade
  to the in-line mutex fallback (D6) in the meantime, exactly as designed; not a live incident.
- `QueueBacklog`/`CommitLatencyHigh` thresholds are explicit placeholders (commented in the .tf)
  pending `NFRA_CMTQUE.TO-6R`'s load-test baseline -- flagged for re-tune, not a gap in this TO's
  scope (TO-4's own `<requirements>` only mandate WorkerDown + DlqDepth exercises, IAM-clean, and
  a real SNS subscriber -- all four satisfied or in-progress).

## Next Steps

- [0.7.0_AE_CloudOps~B] confirm the WorkerDown ALARM transition (background poll running); relaunch
  the worker daemon once confirmed (`bash .tools/commit-worker-launch.sh`) so the fabric's normal
  commit path isn't left on the degraded in-line-mutex fallback longer than the exercise requires.
  RAVC2 COO with the WorkerDown confirmation once it lands.
  Also update `pipeline_inventory.xml` (core doc, deferred) with the 4 new alarms.
- Re-tune `QueueBacklog`/`CommitLatencyHigh` thresholds once `NFRA_CMTQUE.TO-6R`'s load-test lands
  a real baseline (currently explicit placeholders).
- [2.0.0_SA_COO] TO-4 substantively complete pending the WorkerDown confirmation -- moving to
  `ADHC_COMMITGATE` next per the DRIVE GO sequencing (before `TO-6R`'s load-test).
