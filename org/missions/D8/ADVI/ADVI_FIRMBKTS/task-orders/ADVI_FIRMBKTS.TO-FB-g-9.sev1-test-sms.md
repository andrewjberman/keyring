# ADVI_FIRMBKTS task order -- `FB-g-9` -- ONE TEST TEXT TO THE ON-CALL PHONE FROM THE REGISTERED TOLL-FREE NUMBER (CALL c290, RULED YES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-9</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one message, once; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the actor -- 3 actions named (`sms-voice:DescribePhoneNumbers`, `sms-voice:SendTextMessage`, `sns:ListSubscriptionsByTopic`) read against the laptop identity (user/Andrew_Berman) before the send, 3 of 3 expected; blind to any permission boundary or service-control policy that denies only at send time; no grant is created or widened.
comp-adversary: RUN by the issuer -- at base no record exists (AC1 reads 0 of 3); on a fixture record 3 of 3; with a second send or a retry recorded, 2 of 3. Blindness: the grader reads the actor's record, not the carrier's logs; the delivery line is the actor's read.
EGRESS CLASS, declared: SMS to one phone (the ruled one message); no other channel.
</preflight>

## 1. THE ACT -- `FB-g-9` (the cluster-lead CTO's ruling on call `dell1-20261011T113148Z-c290`)

Ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_CLUSTER_TICK12_20261011_1157Z.md` @087b7ac3a1 (origin
`box/laptop`; read it first). **Terms, verbatim: exactly ONE text, body "Opal test, no action", from the registered
toll-free number straight to the on-call phone via the SMS send API (NOT SNS), by the laptop CloudOps seat with the
laptop identity, message id + status + delivery log line reported within the hour, NO retry.**

Why: every SEV1 page published through SNS fails with `No origination identity available to send to destination number`
(rows D1-S15, D1-S16, D1-S20). This one text tells whether the registered toll-free number can reach the phone at all,
outside SNS. Arrives: the SNS routing is fixed as a cell. Fails: an AWS Support case, which is Andrew's act.

### 1a. Steps

1. **The destination.** Read the one SMS subscription's endpoint of topic
   `arn:aws:sns:us-east-1:313476888478:opal-infrastructure-alerts` (`aws sns list-subscriptions-by-topic`). Hold it in a
   shell variable only. It is a phone number: it never appears in a file, a commit, a row or your report (the record
   below carries none, and its check fails on any).
2. **The origination.** `aws pinpoint-sms-voice-v2 describe-phone-numbers`: the phone number whose `NumberType` is
   `TOLL_FREE` and whose `Status` is `ACTIVE`. If there is not exactly one, STOP and file a BLOCKING row (never choose).
3. **The send, once.** One `aws pinpoint-sms-voice-v2 send-text-message` with `--destination-phone-number` the variable,
   `--origination-identity` that number's id, `--message-body "Opal test, no action"`, `--message-type TRANSACTIONAL`.
   Capture the `MessageId`. **Do not retry**, whatever the outcome: a failure is recorded as it is.
4. **The status and the delivery line.** Within five minutes read the delivery outcome for that `MessageId`: the account's
   SMS delivery log (the CloudWatch Logs group your send's event destination or configuration set writes; find it with
   `describe-log-groups`/`describe-configuration-sets`, read with `filter-log-events` on the id). Record the status word
   as the log gives it and the log line with any phone number masked to its last four digits. If no delivery log is
   configured for this number, record `delivery_status` as `NO_DELIVERY_LOG_CONFIGURED` and `delivery_log_line` as one
   sentence saying so; never write a guess as a status.
5. **The record.** Write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/evidence/sev1_test_sms_20261011.json` (JSON, ASCII, LF) with exactly these keys: `message_id`, `origination_identity_kind`
   (`toll-free`), `message_body`, `send_api` (`pinpoint-sms-voice-v2`), `sent_count` (1), `retry_count` (0),
   `delivery_status`, `delivery_log_line`, `recorded_at` (`date -u +%FT%TZ`) and, only if the send call itself failed,
   `send_error` (the API's error text, number masked).

## 2. BOUNDS

1. ONE `send-text-message` call in all; no `sns publish`, no second text, no retry; no change to any number, pool,
   configuration set, registration, topic or subscription. Read-only describes and one send only.
2. The phone number is never written anywhere. The body is exactly the ruled text.
3. If a step cannot be done as written, file a BLOCKING row and stop; do not substitute SNS.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-g-9.sev1-test-sms.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-9"><invocation>cd /c/dev/ajb_workspace &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_sms.py --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/evidence/sev1_test_sms_20261011.json; echo "exit=$?"</invocation><expect>ROUND 4 SMS RECORD: 3 of 3 arms</expect></criterion>
</proof_of_spec>

The grader reads your record: its fields, that one send and no retry are recorded with the ruled body through the SMS send
API, and that no phone number sits in it. One criterion: the act is one message. It terminates inside its bound.

## 5. WHEN YOU ARE DONE

Commit the record and the instance, flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report ONCE
through the laptop manager to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1` within the hour: the message id, the status
word and the delivery log line, and whether the text arrived.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the relay msg 3822 (bus e72ac582, laptop msg 108324); the ruling is the cluster-lead CTO's under
the deputization in LIVE_ARMS.md; Andrew is told to expect one text. A seat order carried as a crossbox ORDER (the laptop
manager delivers it). SEV1_SMS_TEST is a third workstream of round 4; the outcome is not this project's (the rows live
here). A failure is a row to Andrew (the Support case), an arrival is the SNS-routing cell the next round cuts.

<status>pending</status>
<round>4</round>
<workstream>SEV1_SMS_TEST</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-9</to_id>
<slot>~FBL</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
