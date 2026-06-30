# 0.6.2_AE_PartnerETL -- work log 2026-06-30 (SI2 EventBridge re-time)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Session: canonical-schwab-si2 schedule -> EventBridge (Andrew-direct A+B). DEPLOYED + verified-producing. RAVC-COMPLETE.

### Context / trigger
Andrew-direct (via 0.4.0_DS~B relay): "re-time the SI2 box; it produced nothing today." Initial
spec said the box's built-in Win Task Scheduler "does not work" -> manage via EventBridge.

### DIAGNOSE -- premise REFUTED (Rule 22, grounded on-box BEFORE acting)
Grounded the mechanism via SSM on i-0f3d57a97f14727af (Get-ScheduledTaskInfo + the box's own
download-trigger.log / sync.log + the file tree), NOT rc=0:
- The Win scheduler FIRES fine (SchwabAutoDownload 16:00Z LastResult 0x0; sync every 30min rc=0
  all day; console session Active; SI2 pid 7044 up).
- The DOWNLOAD WORKS: the 16:00Z run pulled CRS20260629 into 29 per-account folders (popups
  dismissed=29).
- REAL no-land cause = sync SCOPE: sync-to-s3.ps1 $src is hardcoded to ONE account (08242234),
  which had no new 06-29 file -> sync transferred nothing -> rc=0 MASKED it (NEVER#5). The box
  actually downloads ~79 accounts daily but syncs only 08242234 by design.
Surfaced 2 sovereign decisions instead of defaulting. Andrew RULED: (A) KEEP 08242234-only (no
sync-scope change); (B) YES move the timer to EventBridge (control-plane upgrade). Cadence: 08242234
IS daily (later resolved: it arrives LATE -- posts 16:00-18:23Z, after the small siblings; no gap).

### DEPLOY (one clean pass; ledger schwab-si2-eventbridge-schedule, 4 legs, 6h window)
New ISOLATED TF module infra/aws/terraform/canonical-schwab-si2-schedule/ (own state key
canonical-schwab-si2-schedule/tfstate -- deliberately NOT the canonical-schwab-ec2 module, whose
runner-trigger.tf is HELD; my apply touches only my 5 resources):
- aws_cloudwatch_event_rule si2_download: cron(35 8,20 * * ? *) = 08:35/20:35 UTC (20:35 lands
  before the 23:00Z 49F BD gold).
- aws_cloudwatch_event_target: SSM RunCommand AWS-RunPowerShellScript on i-0f3d -- inline
  orchestration `schtasks /Run` of the EXISTING interactive SchwabAutoDownload (runs in the live
  console session, kept alive by SchwabKeepConsole), waits, then `schtasks /Run` SchwabS3Sync. NO
  box-script change, NO sync-scope change.
- Pinpoint IAM: events_invoke_ssm role w/ ssm:SendCommand on EXACTLY one instance ARN + the one
  document ARN (no wildcard instance).
- 14h absence alarm -> opal-critical-surface-alerts.

Mechanism solved (the interactive-GUI constraint DS flagged): a session-0 SSM `schtasks /Run`
DOES drive the interactive SI2 GUI in the logged-on console session -- proven, not assumed.

### Verification Sequence (paste of ACTUAL evidence)
- L1 git: commit 1c5a9ced1 (main.tf+schedule.tf+lock) on origin/CLOUD (merge-base ancestor
  confirmed; rejected push -> `git pull --no-rebase` then re-push, NO rebase); tag
  canonical-schwab-si2-schedule-v1.0.0 pushed (origin 8d0ca2beb).
- L2 activation: safe-apply (HALTGT passed) -> "Apply complete! Resources: 5 added, 0 changed, 0
  destroyed"; re-plan "No changes" (0-diff); LIVE `aws events describe-rule` State=ENABLED
  Sched=cron(35 8,20 * * ? *).
- L3 verify (mechanism): manual SSM run of the exact target orchestration -> eventbridge-cycle.log
  cycle START 18:23:43Z -> kicked download -> download-trigger.log fresh dismissals 18:24-18:25Z,
  task State=Running -> sync rc=0. END-TO-END PRODUCE: 08242234 CRS20260629 (12 files, ULN 189MB)
  landed in s3://opal-data-schwab/01_raw_quartz_validation/ at 18:25Z.
- L4 activation (the 20:35Z PRODUCTION fire): EventBridge-issued SSM command d589a897 @ 20:35:11Z
  Status=Success; eventbridge-cycle.log cycle START 20:35:12Z -> download 0x0 -> sync 0x0 -> cycle
  END 20:35:48Z. Internal triggers RETIRED: SchwabAutoDownload 3 daily + SchwabS3Sync 30-min set
  Enabled=false; AUTHORITATIVE registered-XML confirms <Enabled>false</Enabled> on every
  time-trigger, enabled-time-triggers-remaining=0; tasks stay State=Ready (EB on-demand path
  intact); SchwabKeepConsole untouched -> EventBridge is the SOLE timer. Absence alarm State=OK
  (cleared on the fire datapoint). Ledger CLOSED 4/4.

### Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-which | route "si2 box scheduled tasks config + SSM" | NO_FIT -> ran on-rails comp-grep (found EC2_MANIFEST entry) |
| deploy_ledger.py (open/close-leg/close) | NEVER-law deploy-completion gate | PASS -- opened 4-leg, closed all 4, ledger CLOSED |
| safe-apply.sh (HALTGT) | Rule-18 gated apply | PASS -- checkpoint passed, 5 add/0/0 |
| safe-commit.sh (surface-check) | Rule-14a commit | PASS -- 4 files, no critical surface |

**What worked:** grounding the mechanism on the box (task XML + logs + file tree) BEFORE acting
refuted the "scheduler dead" premise and avoided ripping out a working scheduler; isolating the new
module by state key kept the held runner-trigger surface untouched; proving the GUI-via-SSM kick
manually (L3) de-risked the production fire. **What failed:** my absence alarm shipped with
treat_missing_data=breaching -> fired build-out noise on the COO critical-surface channel before the
first fire. **Gap/banked:** the sibling canonical-schwab-runner trigger already documents the right
pattern (FLIP-AT-GO-LIVE: notBreaching until first real fire, then flip) -- I replicated the
anti-pattern; author absence alarms that way next time. Steady-state setting is correct now that it's
live, so no change made.

## Blockers
None. SI2 re-time complete.

## Current State
- canonical-schwab-si2 (i-0f3d57a97f14727af) now runs its download+sync on EventBridge rule
  `canonical-schwab-si2-download-schedule` (cron 35 8,20 UTC, ENABLED). Internal Win time-triggers
  are disabled (XML Enabled=false); SchwabAutoDownload/SchwabS3Sync remain Ready for the EB
  `schtasks /Run` kick; SchwabKeepConsole still 5-min. EventBridge is the sole timer.
- TF: infra/aws/terraform/canonical-schwab-si2-schedule/ (state key canonical-schwab-si2-schedule/tfstate),
  commit 1c5a9ced1, tag canonical-schwab-si2-schedule-v1.0.0. 5 resources (rule, target,
  events_invoke_ssm role+policy, absence alarm).
- Scope: 08242234-only (sync-to-s3.ps1 unchanged). The other ~78 accounts download to local disk,
  never sync.
- Ledger org/critical_paths/change_management/20260630T1818Z_schwab-si2-eventbridge-schedule_deploy_completion.md
  = CLOSED 4/4.
- A fresh-session backstop trigger (created earlier, not in my account context so un-cancellable)
  fires ~20:40Z; it will re-verify an already-CLOSED ledger + already-retired triggers and conclude
  done (idempotent independent re-check).

## Next Steps
- **[0.6.2 self]** Pivot per COO: offered 0.6.1 a 2nd pair of AE hands on the inf-refactor
  all-nighter (boundary-safe slices: dry-validate decommission/rebuild TF, parallel comp-iam/
  never-widen pass, ledger staging, parity-run support). Awaiting 0.6.1's pick or contingency-confirm.
- **[0.6.0_AE_PartnerETL]** folding RLW-not-daily robustness into 49-schwab-conv RLD step (RLW absent
  on CRS20260629; treat as periodic/Fri, clean-skip not failure).
- **[future]** non-08242234 files accumulate on the t3.large local disk (downloaded, never synced)
  -> a periodic local purge may eventually be wanted. Noted, not acting (ratified design).

## MCP traffic
~10 messages. Significant: RAVC opened+closed to 2.0.0_SA_COO (grounding -> A+B ruling -> DONE);
relays via 0.4.0_DS~B (premise correction + Andrew decisions); with-files proof + cadence resolution
to 0.6.0_AE; COO alarm-FYI answered; offer-of-hands to 0.6.1_AE (open). Andrew live-reconfirmed
08242234-only mid-session.
