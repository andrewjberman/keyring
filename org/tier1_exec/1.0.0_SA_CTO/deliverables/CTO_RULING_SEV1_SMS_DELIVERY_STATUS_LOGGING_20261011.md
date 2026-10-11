# CTO ruling -- the SEV1 SMS page path: enable delivery-status logging on `opal-infrastructure-alerts` (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~09:0xZ)

**Rows:** `ADVI_FIRMBKTS-D1-S15`, `D1-S16` (`org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md`).
Reads were relayed by `0.0.0_AB_MSTR~DELL1` (msgs 3661, 3663, 3665, 3667), run read-only on the laptop as `user/Andrew_Berman`.

## What is established

- **The page path is dead.** In the 14 days 09-27 to 10-10 the topic's one subscription (SMS) shows 0 notifications delivered and
  28 failed (CloudWatch `AWS/SNS`).
- **Closed by read, not by inference:**
  - not in the SMS sandbox (`IsInSandbox` false);
  - no spend (`SMSMonthToDateSpentUSD` has no datapoints; `MonthlySpendLimit` 50);
  - the endpoint is not opted out;
  - an origination number exists: TOLL_FREE, ACTIVE, Transactional;
  - its registration (`US_TOLL_FREE_REGISTRATION`) is COMPLETE.
- **Not readable today: the failure reason.** The topic has no `SMSFailureFeedbackRoleArn` or `SMSSuccessFeedbackRoleArn`, and the
  account has no `DeliveryStatusIAMRole`. A failure leaves no reason anywhere.

## Ruling

Enable SMS delivery-status logging for this topic. It is diagnostic logging of an EXISTING route, not a new alert, monitor or
notification (the CLAUDE.md section 5 moratorium is not engaged). It is built to LGIC, in Terraform, through `safe-apply`:
- ONE IAM role that SNS assumes, with `logs:CreateLogGroup`, `logs:CreateLogStream` and `logs:PutLogEvents` on the SNS SMS delivery log
  groups only. Its name is `lib/opal_naming.py name()` output; a builder refusal is a registry row (CLAUDE.md 30).
- The topic attributes `SMSFailureFeedbackRoleArn` set to that role and `SMSSuccessFeedbackRoleArn` set to it as well, with a 100
  percent success sample, so one delivered message would also be visible.
- Executed by an identity allowed to write IAM: the laptop CloudOps seat, coordinated MSTR to MSTR. The Dell deploy identities do not
  write IAM.

**NO test SMS is sent to make it fire.** A test page goes to a human's phone. The next organic publish (there were 1 to 5 per day in
the window read) yields the first reason line, and the read of that line closes this ruling's purpose.

**The fix itself is NOT pre-ruled.** If the reason names a carrier block, the toll-free number's throughput or a regional or
country limit, the remedy is read from it then. A change that costs money or alters the vendor relationship goes to Andrew as an open
call.

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 1 (2026-10-11 ~09:2xZ) -- there is no topic-level SMS feedback attribute; the account-level setting is IN scope, narrowed

**Correction, from `2.0.0_SA_COO~B1` msg 3689 (order `ADVI_FIRMBKTS.TO-FB-f-12` @d206374256).** `sns set-topic-attributes` carries
delivery-status attributes for HTTP, Firehose, Lambda, Application and SQS only. `SMSFailureFeedbackRoleArn` and `SMSSuccessFeedbackRoleArn`,
as this ruling named them, do not exist. SMS delivery-status logging is ACCOUNT-level (`set-sms-attributes`: `DeliveryStatusIAMRole`,
`DeliveryStatusSuccessSamplingRate`). This seat's error; the ruling's topic-attribute lines are void.

**Ruling: the account-level setting is in scope, narrowed to what the diagnosis needs.**
- `DeliveryStatusIAMRole` = the one LGIC-named role above, scoped to the SNS SMS delivery log groups.
- `DeliveryStatusSuccessSamplingRate` = `0`. Failures are always logged and successes are not, so the account's other SMS (if any)
  leaves no success trail.
- The delivery log groups get a 14-day retention, set in the same act. The records carry destination phone numbers; nothing keeps
  them longer than the diagnosis needs.
- Before the write, the act reads and prints the account's prior SMS attributes, so the rollback is setting those values back. Only
  `DeliveryStatusIAMRole` and `DeliveryStatusSuccessSamplingRate` change; `MonthlySpendLimit` and every other attribute stay
  byte-equal.
- Still no test SMS. The read steps may run now; the write runs on this amendment.

-- 1.0.0_SA_CTO~DELL1
