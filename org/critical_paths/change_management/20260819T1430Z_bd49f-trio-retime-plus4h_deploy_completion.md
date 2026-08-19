# Deploy-completion ledger -- bd49f trio +4h retime (Andrew-direct 2026-08-19 ~14:2xZ at the CTO terminal)
**Opened:** 2026-08-19 ~14:30Z by 1.0.0_SA_CTO, BEFORE the apply (NEVER#8).
**Authority:** Andrew-direct verbatim (recorded @807c3c9190): BD refreshes prior-day API data ~01:02 ET (~05:00Z) -> pull 06:30Z / convert 07:05Z / reattempt 08:30Z. Consistent with ANDREW_DIRECT_20260811_BD_REST_0102ET. Executor = CTO (AE seats wound down 1405Z; two audited lane-override commits @807c3c9190 + @ee18a14e09, one lane each per Rule 14a).
**Targets (3, all in-place):** aws_cloudwatch_event_rule.bd49f_pull["pull"] (cron 30 2 -> 30 6) · aws_cloudwatch_event_rule.bd49f_pull["reattempt"] (cron 30 4 -> 30 8) · aws_scheduler_schedule.bd49f_convert_daily (cron 5 3 -> 5 7). No IAM, no data movement, no new resources.
**Expected plan:** 0 add / 3 change / 0 destroy, TARGETED (the opal-assets root is shared; targeting avoids ratifying unrelated staged rows).

| step | result |
|---|---|
| targeted plan matches expected | PASS 14:31Z: "0 to add, 3 to change, 0 to destroy" -- exactly the three schedule_expression literals, nothing else in the diff |
| safe-apply | PASS 14:32Z (HALTGT passed; apply completed, outputs rendered) |
| 0-diff-on-target re-plan | PASS 14:33Z: "No changes. Your infrastructure matches the configuration." |
| applied-plane read: describe-rule x2 + get-schedule show the new crons | PASS 14:33Z: pull=cron(30 6 * * ? *) / reattempt=cron(30 8 * * ? *) / convert=cron(5 7 * * ? *) |

**CLOSED 2026-08-19T14:33Z by 1.0.0_SA_CTO.** All legs landed; nothing stranded.

**Rollback:** revert the two commits + re-apply (pure cron literals; same-window).
**First fires on the new clock:** convert 07:05Z / pull 06:30Z / reattempt 08:30Z tomorrow 2026-08-20 (tonight's 02:30Z fire will NOT occur -- deliberate, per the ruling; the 06:30Z fire covers the day). Fam-interaction observation banked for AE Wave-1.
