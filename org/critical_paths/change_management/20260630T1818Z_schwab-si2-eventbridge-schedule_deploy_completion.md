# Deploy Completion Record
**Date opened:** 2026-06-30T18:18:19.176856+00:00
**Status:** OPEN
**Deploy:** canonical-schwab-si2: move SI2 download+sync schedule to EventBridge (cron 35 8,20 UTC) -> SSM kick of interactive SchwabAutoDownload task in live console session, sequenced sync. KEEP 08242234-only scope. Parallel-safe cutover (retire internal Win triggers after verify). Andrew-ruled A+B.
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit (new TF module canonical-schwab-si2-schedule) + tag | commit hash + tag pushed --follow-tags |  | OPEN |
| L2 | activation | TF safe-apply creates aws_cloudwatch_event_rule (cron 35 8,20) + SSM RunCommand target on i-0f3d + EventBridge ssm:SendCommand IAM role/policy | terraform apply complete + 0-diff re-plan |  | OPEN |
| L3 | verify | EventBridge->SSM kick drives a download cycle in the live console session + sequenced sync rc=0 (box download-trigger.log new entry + sync.log rc=0); rule lands ENABLED | SSM invocation Success + box-log evidence + aws events describe-rule State=ENABLED |  | OPEN |
| L4 | activation | RETIRE internal Win triggers after L3 (disable SchwabAutoDownload 12/16/20Z time-triggers + SchwabS3Sync 30-min repeat); KeepConsole left as-is | schtasks/Get-ScheduledTask shows internal time-triggers disabled, EventBridge sole timer |  | OPEN |

## Log

- 20260630T181819Z OPENED by 0.6.2_AE_PartnerETL with 4 leg(s)
