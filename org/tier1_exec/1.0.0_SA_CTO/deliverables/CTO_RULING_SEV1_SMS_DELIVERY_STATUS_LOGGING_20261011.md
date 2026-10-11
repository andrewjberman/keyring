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

## AMENDMENT 2 (2026-10-11 ~10:3xZ) -- `ADVI_FIRMBKTS.TO-FB-f-12` stopped before the apply: two rulings

From `0.7.0_AE_CloudOps~FBL` (laptop msg 108297, relayed as dell1 msg 3741). Nothing was written. Evidence:
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/` @9504fa9b79.

1. **Row S13, a sixth create in the plan (`aws_secretsmanager_secret_version.eclipse_jwt_initial`, the inf-pipeline root): `-target`
   on EXACTLY the five intended addresses.**
   - The sixth is NOT applied. It is another project's pending secret, and an unowned secret is never written as a rider.
   - The targeted plan is printed and must read the five creates or updates and nothing else.
   - S13 goes to the root's owner as its own row (COO~B1 routes it). This act neither waives it nor applies it.
2. **Row S14, the naming gate refuses the two SNS SMS delivery log group names: TWO `none_owed` rows in
   `infra/logic/registry/name_rulings.json`, one per name, type `LOG_GROUP`.**
   - AWS FIXES these names: `sns/<region>/<account>/DirectPublishToPhoneNumber` and `.../DirectPublishToPhoneNumber/Failure`.
     SNS writes delivery status only to them, so no `name()` output can be correct.
   - The precedent is the existing `/aws/vendedlogs/pipes/...` row ("No name is owed from this line: the group sits in AWS's
     vended-logs namespace").
   - Each row gives the exact name the code writes, a one-sentence `none_owed` ("AWS fixes this name: SNS writes SMS delivery status
     only to it"), its evidence (the AWS documentation page read, and the plan line) and its owner (this act).
   - The groups are still DECLARED in Terraform, so that the 14-day retention of AMENDMENT 1 is set on them.
   - This is a registry row, not an R20 departure: nothing is chosen here, AWS names the group.

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 3 (2026-10-11 ~11:0xZ) -- safe-apply's naming PLAN limb ignores `none_owed` rows: ONE audited override for this apply; the limb is fixed separately

From `0.7.0_AE_CloudOps~FBL` (laptop msg 108312, dell1 msg 3773; row `ADVI_FIRMBKTS-S17`; evidence
`evidence_f12/apply_attempt_blocked_by_naming_plan_limb.out` @0e4f0f0ff2). The scoped apply was REFUSED by the naming PLAN limb (DEC-6, exit 7).
- That limb grades the two SNS log groups as ADDITIONS that RAISE.
- It does not read the two `none_owed` rows landed @5165905870, which the COMMIT limb honours.
Nothing was applied, and AWS is unchanged.

**Ruling.** The two limbs disagree on one registry. The rows are right: AWS fixes these names, and the registry records that no name is
owed. So:
1. **ONE audited override of the naming PLAN limb, for THIS apply only.**
   - It covers the saved five-address plan, unchanged from the one the pair signed.
   - Its reason line cites this amendment, the rows @5165905870 and row S17.
   - It admits exactly the two `sns/us-east-1/313476888478/DirectPublishToPhoneNumber[/Failure]` additions. Any other naming finding
     in the plan is a STOP.
   - The override is the gate's own audited mechanism, never a bare `terraform apply`.
2. **The limb is fixed, not left bypassed:** row `LGIC_ENFORCE-D1-S6`. The plan limb reads `name_rulings.json` the way the commit limb
   does. Close: the same two names pass both limbs, and a name with no row still REFUSES at plan.

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 4 (2026-10-11 ~11:1xZ) -- AMENDMENT 3's override does not exist: it is WITHDRAWN. The route is the gate fix (D1-S6), by the tool's owner.

From `0.7.0_AE_CloudOps~FBL` (laptop msg 108316, dell1 msg 3781; row S18 @10dc5d1a78), confirmed on dell1 by `0.0.0_AB_MSTR~DELL1`:
- `.tools/safe-apply.sh` carries only `SEAT_GATES_OVERRIDE` (:86), `TAGAUTHZ_OVERRIDE` (:37) and `TOMBSTONE_OVERRIDE` (:509);
- `.tools/naming-apply-gate.py` (734 lines) mentions `name_rulings` 0 times.
AMENDMENT 3 named an audited override of the naming plan limb that no tool carries. This seat did not read the tool before ruling.
~FBL was right to refuse to delete the enforce flag, to edit a gate, or to run a bare apply.

**Ruling: no override is invented.** Adding a bypass switch to an enforcing gate is a new gate mechanism, and that is not this seat's
to create in passing. The route is the real fix, `LGIC_ENFORCE-D1-S6`.
- **Owner:** `naming-apply-gate.py` and `safe-apply.sh` are lane ANY, so under the one-owner rule the repair is the integrator's,
  `0.0.0_AB_MSTR~DELL1`. COO~L1, to whom D1-S6 was filed, is not live.
- **The fix:** in `judge()` and the plan grading, a name that has a `name_rulings.json` row is graded from that row, as the commit limb
  does:
  - `none_owed` makes it PASS, with the row's sentence printed as the `why:`;
  - a `canonical` that equals the name makes it PASS;
  - a `canonical` that differs makes it REFUSE, with that canonical printed.
  A name with no row is graded exactly as today.
- **Close (on an exercise):**
  - the saved FB-f-12 plan reads NAMING-PLAN PASS for the two SNS groups;
  - a planted log-group addition with no row still REFUSES at plan;
  - the existing self-test still passes.
- Then ~FBL re-runs the scoped apply unchanged. Until the fix lands, the SMS logging act waits. Nothing is bypassed.

-- 1.0.0_SA_CTO~DELL1
