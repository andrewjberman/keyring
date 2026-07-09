# Deploy Completion Record
**Date opened:** 2026-06-30T18:18:19.176856+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260630T203852Z
**Deploy:** canonical-schwab-si2: move SI2 download+sync schedule to EventBridge (cron 35 8,20 UTC) -> SSM kick of interactive SchwabAutoDownload task in live console session, sequenced sync. KEEP 08242234-only scope. Parallel-safe cutover (retire internal Win triggers after verify). Andrew-ruled A+B.
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit (new TF module canonical-schwab-si2-schedule) + tag | commit hash + tag pushed --follow-tags | commit 1c5a9ced1 (new module canonical-schwab-si2-schedule: main.tf+schedule.tf+lock) on origin/CLOUD (merge-base ancestor confirmed); tag canonical-schwab-si2-schedule-v1.0.0 pushed (origin 8d0ca2beb). No rebase (merge-pull). | CLOSED 20260630T182258Z |
| L2 | activation | TF safe-apply creates aws_cloudwatch_event_rule (cron 35 8,20) + SSM RunCommand target on i-0f3d + EventBridge ssm:SendCommand IAM role/policy | terraform apply complete + 0-diff re-plan | safe-apply (HALTGT passed): Apply complete! Resources: 5 added, 0 changed, 0 destroyed (rule+target+events-ssm-role+role-policy+absence-alarm). 0-diff re-plan: No changes. LIVE aws events describe-rule canonical-schwab-si2-download-schedule State=ENABLED Sched=cron(35 8,20 * * ? *) (Rule 22 ground-truth). | CLOSED 20260630T182258Z |
| L3 | verify | EventBridge->SSM kick drives a download cycle in the live console session + sequenced sync rc=0 (box download-trigger.log new entry + sync.log rc=0); rule lands ENABLED | SSM invocation Success + box-log evidence + aws events describe-rule State=ENABLED | MECHANISM PROVEN on-box: ran the EXACT EventBridge-target orchestration via SSM (CommandId ed854b6e). eventbridge-cycle.log: 'cycle START'+'kicked SchwabAutoDownload' 18:23:43Z; a SESSION-0 SSM schtasks /Run drove the INTERACTIVE SI2 GUI in the live console session -> download-trigger.log fresh dismissals 18:24:28-18:25:27Z, task State=Running (the load-bearing uncertainty -- confirmed). Sequenced sync = the existing SchwabS3Sync task, demonstrably rc=0 (sync.log 18:24:56Z). Rule LIVE State=ENABLED cron(35 8,20). NOTE: production EventBridge->SSM delivery hop confirmed at the 20:35Z natural fire BEFORE L4 internal-trigger retirement (parallel-safe). | CLOSED 20260630T182640Z |
| L4 | activation | RETIRE internal Win triggers after L3 (disable SchwabAutoDownload 12/16/20Z time-triggers + SchwabS3Sync 30-min repeat); KeepConsole left as-is | schtasks/Get-ScheduledTask shows internal time-triggers disabled, EventBridge sole timer | EB->SSM PRODUCTION FIRE PROVEN: EventBridge-issued SSM command d589a897 at 20:35:11Z Status=Success; eventbridge-cycle.log 'cycle START' 20:35:12Z -> download done 0x0 -> sync done 0x0 -> 'cycle END' 20:35:48Z (full end-to-end, the only unproven hop now confirmed). INTERNAL TRIGGERS RETIRED: SchwabAutoDownload 3 daily + SchwabS3Sync 30-min triggers set Enabled=false; AUTHORITATIVE registered-XML shows <Enabled>false</Enabled> on every time-trigger, enabled-time-triggers-remaining=0; tasks stay State=Ready (on-demand schtasks /Run by EB intact); SchwabKeepConsole untouched -> EventBridge is the SOLE timer. Absence alarm State=OK (cleared on the fire datapoint). | CLOSED 20260630T203852Z |

## Log

- 20260630T181819Z OPENED by 0.6.2_AE_PartnerETL with 4 leg(s)
- 20260630T182258Z LEG L1 closed: commit 1c5a9ced1 (new module canonical-schwab-si2-schedule: main.tf+schedule.tf+lock) on origin/CLOUD (merge-base ancest
- 20260630T182258Z LEG L2 closed: safe-apply (HALTGT passed): Apply complete! Resources: 5 added, 0 changed, 0 destroyed (rule+target+events-ssm-role+role
- 20260630T182640Z LEG L3 closed: MECHANISM PROVEN on-box: ran the EXACT EventBridge-target orchestration via SSM (CommandId ed854b6e). eventbridge-cycle.
- 20260630T203852Z LEG L4 closed: EB->SSM PRODUCTION FIRE PROVEN: EventBridge-issued SSM command d589a897 at 20:35:11Z Status=Success; eventbridge-cycle.l
- 20260630T203852Z CLOSED -- all 4 legs proven
