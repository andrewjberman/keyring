# ADVI_FIRMBKTS task order -- `FB-f-12` -- ENABLE SMS DELIVERY-STATUS LOGGING FOR THE SEV1 PAGE PATH (rows D1-S15 / D1-S16; the CTO's ruling of 2026-10-11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the actor's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-12</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>ROLE_NAME, ROLE_ARN</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer, read-only: `aws sns get-sms-attributes` as `user/cloudops-dell1-agent-user` is denied (`sms-voice:DescribeSpendLimits`), so the account's current SMS preferences are NOT read by the issuer; the actor reads them at step 1 with the laptop identity before any write. The role this act creates is the only IAM object it writes.
comp-adversary: DECLARED-NOT-APPLICABLE -- diagnostic logging of an existing route, not a new alert, monitor or notification (the CTO's ruling, CLAUDE.md section 5 moratorium not engaged); the criteria below read the configuration, not a delivery.
EGRESS CLASS, declared: NONE. NO test SMS is sent by this act: a test page goes to a human's phone.
</preflight>

## 1. THE ACT -- `FB-f-12` (the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_SEV1_SMS_DELIVERY_STATUS_LOGGING_20261011.md`, read it first)

The shared topic `arn:aws:sns:us-east-1:313476888478:opal-infrastructure-alerts` has one subscription (SMS). In the 14
days 09-27 to 10-10 it shows 0 notifications delivered and 28 failed, and a failure leaves no reason anywhere because no
delivery-status logging role is configured. You enable SMS delivery-status logging so the next organic publish writes a
reason line, and you stop there.

### 1a. What is already established (closed by read, not by inference)

Not in the SMS sandbox; no month-to-date spend, `MonthlySpendLimit` 50; the endpoint is not opted out; an origination number
exists (TOLL_FREE, ACTIVE, Transactional) and its registration is COMPLETE. The failure REASON is not readable.

### 1b. The mechanism, and the STOP on it (read this twice)

The ruling names the topic attributes `SMSFailureFeedbackRoleArn` and `SMSSuccessFeedbackRoleArn`. The issuer read
`aws sns set-topic-attributes help` on 2026-10-11: the valid delivery-status attributes are `HTTP*`, `Firehose*`, `Lambda*`,
`Application*` and `SQS*` FeedbackRoleArn / SampleRate; there is NO `SMS*` topic attribute. SMS delivery-status logging is an
ACCOUNT-LEVEL setting (`aws sns set-sms-attributes`: `DeliveryStatusIAMRole`, `DeliveryStatusSuccessSamplingRate`), which
applies to every SMS the account sends through SNS, not to this topic alone. It is diagnostic only (it writes logs; it does not
change delivery); the CTO ruled it in scope.

THE CTO RULED (AMENDMENT 1 @6d046c34e3 of the ruling file, msg 3692): the account-level setting IS in scope, with
`DeliveryStatusIAMRole` = the one scoped role, `DeliveryStatusSuccessSamplingRate` = **0** (failures only; NOT 100), a
**14-day retention** on the SNS delivery log groups, the prior attributes printed first for the rollback and every other
attribute byte-equal, and no test SMS. The ruling file's AMENDMENT 1 governs where it differs from this order.

### 1c. The steps, in order

0. **Gate.** `git ls-tree HEAD` lists this order and the ruling file with its AMENDMENT 1; `<status>` reads `pending`.
1. **Read before you write.** With your identity: `aws sns get-sms-attributes` (record every attribute: `MonthlySpendLimit`,
   `DefaultSMSType`, `DeliveryStatusIAMRole`, `DeliveryStatusSuccessSamplingRate`, `UsageReportS3Bucket`, ...) and `aws sns
   get-topic-attributes` for the topic into the change-management entry. Open the entry BEFORE the first write
   (`python .tools/deploy_ledger.py open ...`, read its `--help`), naming the role, the account setting, the prior values and
   this order.
2. **The name.** The role's name is `lib/opal_naming.py name()` output. A builder refusal is a missing registry row to add
   (`infra/logic/registry/`), never a hand-typed name (CLAUDE.md 30). `ROLE_NAME` and `ROLE_ARN` are read from the builder
   and the apply.
3. **The Terraform.** The topic is declared outside any Terraform module (`infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms.tf`
   header says so; the subscription is `aws_sns_topic_subscription.ops_alerts_sms`). Put the role and the account setting in
   the root that already holds that subscription, as `aws_iam_role` + `aws_iam_role_policy` and `aws_sns_sms_preferences`
   (set ONLY `delivery_status_iam_role_arn` and `delivery_status_success_sampling_rate = 0`; read the provider's
   documentation for what the resource does to the preferences you do not set, and carry every value step 1 recorded so the
   plan shows no change to them). The role's trust is `sns.amazonaws.com`; its policy is `logs:CreateLogGroup`,
   `logs:CreateLogStream`, `logs:PutLogEvents`, `logs:PutMetricFilter` and `logs:PutRetentionPolicy` on the SNS SMS delivery log
   groups only (`arn:aws:logs:us-east-1:313476888478:log-group:sns/us-east-1/313476888478/DirectPublishToPhoneNumber*`),
   nothing broader. Declare the two delivery log groups yourself so the retention exists before SNS writes:
   `aws_cloudwatch_log_group` for `sns/us-east-1/313476888478/DirectPublishToPhoneNumber` and
   `sns/us-east-1/313476888478/DirectPublishToPhoneNumber/Failure` with `retention_in_days = 14` (if a group already
   exists, import it first: read `aws logs describe-log-groups --log-group-name-prefix sns/us-east-1/313476888478/`).
4. **Plan, read the JSON.** It must change EXACTLY the role, its policy, the two log groups and the SMS preferences; any other resource, or any
   preference value other than the two named, is a STOP.
5. **Apply** through `safe-apply` only. Read back: the role's trust and policy, `get-sms-attributes` (the two values set, every
   other value as step 1 recorded), a post-apply plan with no changes.
6. **Do not send an SMS.** The next organic publish yields the first reason line; the read of that line closes this ruling's
   purpose and is the CTO's. Report where the reason lines will appear (the log group name) and stop.
7. **Close** the entry with the read-backs; flip `<status>` to `complete` in the same commit as the proof instance.

## 2. BOUNDS

1. The only writes are the role, its policy, the two delivery log groups (retention 14 days), the SMS preferences' two
   delivery-status values and the Terraform files that declare them, and the registry row a builder refusal may require. No topic attribute, subscription, endpoint, number,
   spend limit or sampling other than the two values; no alert; no delete.
2. If a plan or a read differs from step 4's set, STOP before the apply and file a BLOCKING row (`ADVI_FIRMBKTS-S<k>`, the
   laptop's coordinate is bare).
3. No test SMS, no `sns publish` to the topic or a phone number.

## 3. SURFACES

<paths>
infra/aws/terraform/inf-pipeline/
infra/logic/registry/
lib/opal_naming.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-f-12.sms-delivery-status-logging.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-12"><invocation>.tools/aws iam get-role --role-name <ROLE_NAME> --query "Role.AssumeRolePolicyDocument.Statement[0].Principal.Service" --output text</invocation><expect>^sns.amazonaws.com$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-12"><invocation>.tools/aws sns get-sms-attributes --region us-east-1 --query "attributes.DeliveryStatusIAMRole" --output text</invocation><expect>^<ROLE_ARN>$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-12"><invocation>.tools/aws sns get-sms-attributes --region us-east-1 --query "attributes.DeliveryStatusSuccessSamplingRate" --output text</invocation><expect>^0$</expect></criterion>
  <criterion id="AC4" cell_refs="FB-f-12"><invocation>.tools/aws logs describe-log-groups --log-group-name-prefix sns/us-east-1/313476888478/DirectPublishToPhoneNumber --region us-east-1 --query "logGroups[0].retentionInDays" --output text</invocation><expect>^14$</expect></criterion>
</proof_of_spec>

AC1 is the role's trust, AC2 and AC3 the two delivery-status values at the account, AC4 the CTO's 14-day retention (a
fourth criterion: the ruling names it). All four read FAIL at base by construction (no role, no value, no group). They read configuration, never a delivery: no SMS is sent.

## 5. WHEN YOU ARE DONE

Close the change-management entry with the read-backs; flip `<status>` to `complete` in the SAME commit as the proof instance.
Report once to `2.0.0_SA_COO~B1`: the pre-act attribute record, the plan's resource summary, the three outputs, the post-apply
plan line, the log group where the reason lines will appear, the entry's path and the commit hash. The CTO reads the first
reason line after the next organic publish.

<!-- ===================== RECORD FACE -- does NOT travel to the actor ===================== -->

**ISSUER NOTES:** class WORLD (IAM role create, account SMS preference). Cut on the CTO's order (msg 3682, ruling
`CTO_RULING_SEV1_SMS_DELIVERY_STATUS_LOGGING_20261011.md`), rows `ADVI_FIRMBKTS-D1-S15` and `D1-S16`; a cell added to the frozen
decomposition by that order (decomposition amendment, 9 chains); it issues as the SECOND WORKSTREAM `SEV1_SMS` of round 3
(one issuer per round is keyed to the round: a separate scope, disjoint write surface, the laptop lane `~FBL`). Un-staged by the CTO's AMENDMENT 1 @6d046c34e3 (msg 3692) after the issuer's
finding that the ruling's mechanism (topic attributes `SMSFailureFeedbackRoleArn`) does not exist in the SNS API: the
account-level setting is in scope, success sampling 0, retention 14 days. The Dell deploy identities do not write IAM
and cannot read the SMS preferences (`sms-voice:DescribeSpendLimits` denied): the executor is the laptop CloudOps lane.

**AMENDMENT 1 (2.0.0_SA_COO~B1, the seat's row S13, ruled):** the inf-pipeline root's UNTARGETED plan carries a sixth create,
`aws_secretsmanager_secret_version.eclipse_jwt_initial` (secret `orion/eclipse_jwt/current`), which is not this order's and
was pending before it. The seat stopped, correctly, at step 4's "exactly the five". Ruled: the apply is a SCOPED apply through
`safe-apply` (its `-target` mechanism, `.tools/safe-apply.sh` MS-s-1) on EXACTLY the five addresses: `aws_iam_role.sms_delivery_status`,
`aws_iam_role_policy.sms_delivery_status`, `aws_cloudwatch_log_group.sns_sms_delivery`,
`aws_cloudwatch_log_group.sns_sms_delivery_failure` and `aws_sns_sms_preferences.account`. The seat's targeted plan (5 creates,
nothing else) is the plan the apply runs; any resource beyond the five in a targeted plan is a STOP. The sixth is WAIVED for
this order: it is not applied, not read, not touched, and the post-apply FULL plan must read exactly that one create and the
ACL-free state otherwise (the denominator printed: 358 resource_changes, 352 no-op before). It is a pending create in a root
this order does not own; an unscoped apply of `inf-pipeline` by anyone would write that secret version, which the seat
reports to the issuer as an OBSERVATION row. Row S14 (the naming gate and the two AWS-fixed SNS log group names) is NOT
ruled here: it is the CTO's, and the apply waits for it. Gate limb: none graded (a ruling on a pending order's record face).

<status>pending</status>
<round>3</round>
<workstream>SEV1_SMS</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-12</to_id>
<slot>~FBL</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
