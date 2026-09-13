# FIRMSEP'S S3-BYPASS ALARM HAS NEVER DELIVERED -- INCLUDING DURING THE TEST THAT CERTIFIED IT -- AND THE KNOWN SMS REMEDY WILL NOT REACH IT

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer). **Found:** 2026-09-13 ~03:3x-05:0xZ, while sweeping the D8
migration's destination buckets for FWD-6 (`FWD6_QUIET_WINDOW_IS_UNPROVABLE_FOR_COTTONWOOD_20260913.md`).
**Status:** verified; nothing changed on any plane; every read read-only. **Push state:** LOCAL. This seat does not push.
**PII:** SMS destinations are phone numbers and are **not reproduced here**, though some of the records cited below
contain them.

---

## 0. MOST OF WHAT I FIRST FOUND WAS ALREADY KNOWN -- CITED HERE, NOT CLAIMED

I re-measured all of the following live this turn and every figure holds. None of it is new, and the first draft of
this file presented it as if it were:

| already on the record | where |
|---|---|
| The account is in the SNS **SMS sandbox**; the one registered destination is **Pending**, never verified; **every SMS-protocol subscription in the estate is non-functional** | `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ALERT_DELIVERY.md` s.4 |
| `opal-infrastructure-alerts` reaches nobody: 24 alarms, one SMS leg, 70 connected resources, both EventBridge rules feed it | same folder, `ANOMALY_IN_EDITION.md` |
| The SMS pager was found broken on **2026-07-07** -- by **this seat** | `org/tier1_exec/3.0.0_SA_CVO/logs/2026-07-07/cvo_WS-1_allstep_alarm_exercise-cert_PASS-coverage_P1-SMS-paging-BROKEN.md` |
| Surfaced to Andrew **2026-07-13**; the OTP verification was then **stood down -- "CANCELLED, not deferred"** -- on the principle that an alert calibrated against an unproven process is device spam. That is why the number is still Pending: a decision, not an omission | `2.0.0_SA_COO` -> `0.0.0_AB_MSTR` 07-13 00:14Z; `0.7.0_AE_CloudOps` -> `1.0.0_SA_CTO~B` 07-13 04:38Z |
| The production SMS path was **filed 2026-09-09** on Andrew's word: toll-free number provisioned, registration in carrier review, spend increase pending | `org/tier0/ledger/LD-0537.md`; `org/tier0_exec/0.0.0_AB_MSTR/deliverables/SMS_TOLL_FREE_REGISTRATION_DRAFT_20260909.md` |

**WITHDRAWN from the first draft:** `cmtque-worker-down` in ALARM for 54 days is **not an outage**. It is the worker
of the commit queue that this seat recorded on 2026-07-09 as **dormant by design** -- no worker process runs because the
queue was never switched on. A latched missing-data alarm on a system that is off.

## 1. NEW -- THE EVENTBRIDGE LAYER FAILS 100%, INDEPENDENTLY OF SMS

The known record attributes the silence to the SMS leg. There is a second failure upstream of it. Both EventBridge
rules that target `opal-infrastructure-alerts` **never reach the topic at all**:

| rule | invocations | failed | window |
|---|---|---|---|
| `FIRMSEP-s3-direct-access-bypass` | **34,334,399** | **34,334,399** | every day, 2026-05-11 .. 2026-09-13 (126 days) |
| `moltbot-ssm-sendcommand-alert` | **159** | **159** | 2026-02-20 .. 2026-08-28 |

The CloudWatch alarms on the same topic DO publish -- 203 messages published over the retention window -- so this is
specific to EventBridge. The topic carries only the unmodified SNS default policy and **no statement granting
`events.amazonaws.com`**; no KMS key. **Stated as consistent-with, not root cause:** neither target has a dead-letter
queue, so no failure reason was ever retained, and no topic in this account receives from EventBridge successfully to
serve as a difference control.

## 2. NEW -- THE ALARM WAS CERTIFIED ON A METRIC THAT CANNOT SEE THE FAILURE

The FIRMSEP phase-2 close log certified AC4 "empirical bypass test -> rule fires" as **"DONE (21 triggers @
19:40-19:45Z; 100% SNS delivery)"**, reasoning *"Invocations = TriggeredRules (0 failed deliveries). SNS delivery to
opal-infrastructure-alerts: confirmed."* (`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-05-11/session_firmsep_phase2_close.md:56`, `:94`)

`Invocations` counts ATTEMPTS. Failure is a separate metric, `FailedInvocations`, which the log never read. **Measured
for the certification hour itself, 2026-05-11, 1-hour resolution:**

| hour | TriggeredRules | Invocations | **FailedInvocations** |
|---|---|---|---|
| **19:00Z** (the test ran 19:40-19:45Z) | 67 | 67 | **67** |
| 20:00Z | 10,142 | 10,142 | **10,142** |
| 21:00Z | 26,165 | 26,165 | **26,165** |

⛔ **THE ACCEPTANCE TEST WAS FAILING DELIVERY AT THE MOMENT IT WAS CERTIFIED AS 100% DELIVERED.** And the check could
not have come out otherwise: `Invocations = TriggeredRules` is true whether every delivery succeeds or every delivery
fails. It is a certification whose legs never read the coordinate the defect lives on, so it passes the defect every
time. The same reasoning is carried in `infra/aws/terraform/portal-auth/cloudwatch-alarms.tf:244-245` ("no additional
policy change needed"), which 34.3 million failed invocations falsify.

## 3. NEW -- THE TWO FAILURES ARE IN SERIES, SO THE KNOWN REMEDY LEAVES THESE TWO DARK

The fabric's remedy in flight is the SMS path (LD-0537, or verifying the Pending number). Completing it would restore
delivery for the **24 CloudWatch alarms**, because they already reach the topic. **It would not restore the two
EventBridge rules**, which do not reach the topic at all. The two that would stay dark are:

- **`FIRMSEP-s3-direct-access-bypass`** -- the firm-separation alarm on direct, non-CloudFront reads of firm buckets;
- **`moltbot-ssm-sendcommand-alert`** -- the alert on remote command execution against a named instance.

Both are security controls, and the fix everyone is waiting on passes them by. The only oracle for any of this is a
message arriving at a person; a green `Invocations` count is exactly what certified FIRMSEP in May.

## 4. A QUESTION, NOT A FINDING -- DOES LD-0537 EXIT THE *SNS* SMS SANDBOX?

LD-0537's own draft (s.2) says the filing targets **End User Messaging**, which the auth handler sends through, and
states: *"SNS's own sandbox flag is a separate, console-only case and is NOT needed for this sender."* Every alert
topic's SMS leg is an **SNS** subscription. If the draft's statement is right, **the alert SMS legs stay sandboxed after
LD-0537 completes**, while the fabric reasonably believes SMS has been fixed. **Carried from `0.0.0_AB_MSTR`'s text,
not measured by this seat** -- the interaction between the two sandbox flags is exactly the kind of product behaviour I
would get wrong by inference. Routed to `0.0.0_AB_MSTR` as LD-0537's holder.

## 5. LATENT -- FIRMSEP.10'S COTTONWOOD EXTENSION IS VOID

`FIRMSEP-s3-direct-access-bypass` matches `GetObject` on `opal-data-bd`, `-inf` and `-cot` (committed and live pattern
agree). CloudTrail emits object reads only for `bd` and `inf` -- the organization trail's sole read selector holds
exactly those two values, applied by CLI and absent from Terraform. **So the rule cannot fire for Cottonwood.** Moot
while s.1 stands; it surfaces the moment s.1 is fixed. The trail gap itself is documented
(`infra/aws/terraform/globgrph/item2e_served_write_trail.tf:8-9`, 2026-06-30); **its consequence for FIRMSEP.10,
which extended the rule to `cot` on 2026-06-09, is not** -- nobody connected the two.

## 6. MY OWN ERROR IN THIS WORK

I sent Andrew a terminal notification headlining the SMS failure **before** my prior-record search returned. I had
ordered that search specifically to keep a false novelty claim out of this FILE, and let the notification go ahead of
it. The facts in it were accurate; the implied news was not -- the matter was known, decided and in flight. **A
prior-record search precedes an announcement, not just a document.**

## 7. WHERE THIS BELONGS, AND WHO CAN ACT

- The natural channels are `NFRA_OPSEC202609` and `NFRA_REPORT`, both D12. `NFRA_OPSEC202609`'s channel is site-Z
  fabric (193 of 193 rows `fabric: site-z`), and whether a laptop seat can write a site-Z row was recorded as
  **unresolved** today. So this is a file under this seat's own path, routed to `1.0.0_SA_CTO` for placement.
- The topic is created outside this repository (both repo references are `data "aws_sns_topic"` lookups); a grant to
  `events.amazonaws.com` belongs to whoever owns it, and the rules are `0.7.0_AE_CloudOps`'s.
- **Any change to the alerting plane sits under the standing moratorium** on alerts and monitors (CLAUDE.md s.5): it is
  Andrew's word, and it may be deliberately held -- the 07-13 stand-down suggests it is. This seat proposes no change
  and made none.

## 8. WHAT THIS FILE DOES NOT CLAIM

- **Not that any alarm condition was real.** It measures whether a person could have been told.
- **Not the EventBridge mechanism as root cause** (s.1).
- **Not that LD-0537 fails to fix the alert legs** -- that is a question (s.4).
- **Not that the 159 `SendCommand` events were improper** -- only that nobody was told they happened.

---

**Instruments, all read-only:** `events describe-rule`, `list-targets-by-rule`, `list-rule-names-by-target`;
`cloudwatch describe-alarms`, `get-metric-statistics` (AWS/Events and AWS/SNS, daily over full retention and hourly
for 2026-05-11); `sns get-topic-attributes`, `list-subscriptions`, `get-sms-sandbox-account-status`,
`list-sms-sandbox-phone-numbers`; `cloudtrail get-event-selectors`; `sqs get-queue-attributes`;
`lambda list-event-source-mappings`. Prior-record search: `org/**/*.md` for the sandbox terms (85 files) and for
`FailedInvocations|events.amazonaws.com|FIRMSEP-s3-direct-access-bypass` (71 files); the relevant ones are cited above.
