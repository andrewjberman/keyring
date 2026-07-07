# CVO Exercise-Cert — WS-1 all-step ChainStepDegraded alarm: coverage+firing PASS (my gap CLOSED) + NEW P1: SMS human-paging limb PROVABLY BROKEN

**archetype:** VALIDATE
**Date:** 2026-07-07 | **Agent:** 3.0.0_SA_CVO | **Requested:** 0.6.1_AE_PartnerETL 160545Z (exercise-cert on my original alarm-coverage-gap find `b7dc964db`)
**Grounding:** all against LIVE AWS (Rule 22a exercised+applied), independently pulled — NOT 0.6.1's report. Raw `aws` inspection rail-checked (no comp-tool surfaces CloudWatch alarm-history / SNS delivery metrics / SNS SMS-sandbox / SQS attrs).

## Verdict (split)

- **WS-1 all-step alarm COVERAGE + FIRING = PASS.** My original gap (only PERF had a ChainStepDegraded alarm) is genuinely CLOSED. **Per-step PERF retirement AUTHORIZED** on strict-superset grounds.
- **NEW finding P1 — the SMS human-paging limb of `opal-partner-etl-ops-alerts` is PROVABLY FAILING** (not "unprovable receipt" as the request bounded it — a measured SNS-layer delivery FAILURE). Affects EVERY alarm on that topic, orthogonal to the retirement.

## Leg 1 — coverage is genuinely all-step (structural, closes the original gap)

Live alarm `inf-gold-chain-step-degraded-allstep` Metrics Insights expression:
```
SELECT SUM(ChainStepDegraded) FROM SCHEMA("Inflection/GoldChain", Service, Step)
```
No `WHERE Step=...` pin → aggregates ChainStepDegraded across ALL (Service, Step) dimension combinations. Any step (TXN / PERF / ASSETS_V2 / a future step emitting under {Service, Step}) increments the sum → fires. This structurally kills the forget-to-add-per-step class that was the WS-1 finding. `ActionsEnabled=true`, `AlarmActions=[opal-partner-etl-ops-alerts]`.
- **Residual (low):** SCHEMA() matches metrics with EXACTLY the {Service, Step} dimension set — a future step emitting ChainStepDegraded with a different dimension shape would silently fall out. Contract-note for the step emitters, not a defect today.

## Leg 2 — fired on a real degrade + action executed (exercised)

- State history: single transition `INSUFFICIENT_DATA -> ALARM` @ ts 1783434895.086 = **2026-07-07T14:34:55Z** (I converted the epoch; matches 0.6.1's claim). Currently in ALARM catching the live ongoing PERF degrade (the M1 600s-timeout defer). Both the new all-step AND the old per-step PERF alarm are in ALARM on the SAME real degrade — cross-confirms the all-step responds to a genuine degrade, not a synthetic.
- Action history: `Successfully executed action arn:...opal-partner-etl-ops-alerts` at that transition. CloudWatch fires AlarmActions on any transition INTO ALARM (incl. from INSUFFICIENT_DATA) — valid action-firing.

## Leg 3 — delivery (went ONE level past the requested bar; found the defect)

0.6.1's stated bar was "action-Succeeded + confirmed subscriptions; can't prove SMS reached the phone." "Action Succeeded" only means CW published to the TOPIC — it is blind to per-endpoint fan-out. Pulling the SNS topic delivery metrics (07-07 14:30Z bucket) surfaces what that bar cannot:
```
NumberOfMessagesPublished     = 1   (the alarm's publish)
NumberOfNotificationsDelivered = 1
NumberOfNotificationsFailed    = 1   <-- one endpoint FAILED
```
The topic fanned 1 message to its 2 subs → 1 delivered, 1 FAILED. Attribution (grounded, convergent — not inferred):
- **SQS `partner-etl-ops-queue` = DELIVERED.** Queue depth 8 messages / 0 in-flight → the SNS→SQS durable path works.
- **SMS `+17862617679` = FAILED.** `aws sns get-sms-sandbox-account-status` → `IsInSandbox: true`; `list-sms-sandbox-phone-numbers` → `+17862617679` status `Pending` (never verified). In the SNS SMS sandbox, SMS delivers ONLY to VERIFIED numbers → the message to a Pending number is dropped. `NumberOfSMSMessagesDelivered` for the window = EMPTY (0 successful SMS), consistent.

So the human-pager SMS limb of this alarm — and every alarm on `opal-partner-etl-ops-alerts` — does NOT deliver. This is a measured failure, materially stronger (and worse) than the "unprovable receipt" the request assumed was the ceiling.

## Dispositions

1. **Per-step PERF retirement: AUTHORIZED.** `inf-gold-chain-step-degraded-allstep` is a strict superset of the per-step PERF alarm on every dimension (coverage ⊇, same topic, same actions). The SMS failure affects BOTH identically (shared topic), so retiring per-step PERF loses nothing. CloudOps may retire it. (Anti-sprawl end-state, CTO keep-both-then-retire satisfied.)
2. **P1 → 0.7.0_AE_CloudOps (topic/alarm infra owner) + 0.6.1 (requestor), CC COO: fix the SMS paging path.** Either (a) exit the SNS SMS sandbox (production SMS access request) — the right prod posture, or (b) complete sandbox verification of +17862617679 (the OTP step someone started but left `Pending`). Then RE-EXERCISE and confirm `NumberOfNotificationsFailed=0` on the next fire. Until then the ONLY working delivery is SQS.
3. **Observation → 0.7.0/0.6.1: confirm a live consumer drains `partner-etl-ops-queue`** (8 messages, 0 in-flight = possibly no active consumer). If SMS is down AND nobody polls the queue, the alarm pages no human at all. Verify the on-call actually SEES a message on this topic by SOME path.

## ESCALATION (post-cert, 0.7.0 re-grounding + my independent confirm)

The P1 is worse than first flagged, and the obvious email fix has a grounded caveat:
- **SQS limb also dead:** `lambda list-event-source-mappings` on `partner-etl-ops-queue` = EMPTY (I independently confirmed). Zero consumers, ever — not "no consumer right now." So `opal-partner-etl-ops-alerts` reaches **NO human by ANY path** currently; every alarm on it is mute-to-humans. My 8-msg/0-in-flight observation resolves to "no consumer," not "slow consumer."
- **SMS sub is undeclared in TF** (0.7.0, comp-grep zero matches) — same undeclared-drift class as the day's other findings.
- **Both fixes are human/console-gated** (0.7.0 can't complete either as an agent): (a) SNS SMS sandbox-exit = console-only form (no Premium Support on account → no Support-API path); (b) OTP verify of the pager number = needs physical SMS receipt.
- **Proposed durable fix = SQS-consumer Lambda → SES email. GROUNDED CAVEAT (verifier catch):** 0.7.0's premise "email has no sandbox failure mode" is FALSE — `sesv2 get-account` ProductionAccessEnabled=**false**, Max24HourSend=200 → SES IS in sandbox (verified-recipients-only, same class as SMS). BUT `andrew@opalinvest.com` is `VerifiedForSending=true` (and the ETFS reporter delivers to it live), so a forward to a **verified** identity (andrew@ / any address in `list-email-identities`) works TODAY; a forward to an **unverified** address (Slack inbound-email, new distro) rebuilds the failure one layer over. Fix must target a verified identity, or exit SES sandbox for arbitrary destinations.
- **Sequencing:** advisory-routed — (ii) SQS-consumer→verified-SES-email = durable primary (agent-completable today), (iii) TF-declare the SMS sub, SMS/SES-sandbox-exit = parallel Andrew-console track. **Build-GO deferred to COO** (dispatch lane). **Cert bar for the fix:** end-to-end exercise-proof — alarm fire → message DEMONSTRABLY ARRIVES at the human-read endpoint (NotificationsFailed=0 + the email lands at the verified address), NOT "Lambda deployed"/config-read.

## P1-FIX CERT (0.7.0 SQS-consumer, shared-infra-v1.37.0) — MECHANICAL PASS, ENDPOINT DELIVERY NOT CERTIFIED (message absent from Andrew's mailbox)

0.7.0 built `partner-etl-ops-sqs-consumer` (SQS→SES email→andrew@opalinvest.com), exercised via a real labeled-TEST SNS publish through the live topic, and — to their credit — honestly flagged their evidence ceiling (SES Send/Bounce/Reject, no configuration-set Delivery event). I took the bar to the true endpoint.

**MECHANICAL CHAIN — PASS (independently confirmed on live AWS):**
- ESM now LIVE on `partner-etl-ops-queue` (uuid 2f476f55, Enabled → the consumer) — the zero-consumer gap I found is CLOSED.
- SQS drained 0/0 (the 8-message backlog cleared).
- SES Send=9, Bounce=0 (no datapoint), Reject=0 — 9 messages left SES clean (8 backlog + 1 test).
- Lambda Invocations=9, Errors=0.
The pipe from the topic up through SES works and the stranded backlog drained. Real, verified improvement over "pages nobody."

**ENDPOINT DELIVERY — NOT CERTIFIED (the reason the bar exists):** The M365 gateway is authenticated as Andrew@opalinvest.com (the forward recipient), so I checked the actual mailbox. The 9 SES-sent messages (~16:29Z) are **ABSENT from Andrew's mailbox as of ~16:34Z** — newest item is 16:15:58Z, predating the send; the listing includes Andrew's own Sent items (spans folders, not Inbox-only), so a Junk-foldered copy would show too and does not. `search_email` for the alarm terms → empty. **SES "Send" did NOT equal inbox arrival — demonstrated live.** This is exactly the failure class SES-Send metrics hide and that this whole P1 is about; my earlier "works today to a verified address" was true at the SES-acceptance layer but the true-endpoint check refined it.

**INFERRED root cause (Rule 22 — hypothesis, NOT confirmed; no message-trace/quarantine access):** cross-domain sender `noreply@opalinvest.dev` → `andrew@opalinvest.com` with DKIM `NOT_STARTED` on the SES identity → DMARC misalignment → EOP quarantines a machine-generated alarm from a look-alike-but-different domain, no SES-level bounce. Plausible, not proven.

**DISPOSITION:** P1 stays OPEN. Mechanical chain PASS; delivery uncertified. Next: (a) I re-verify the mailbox shortly to rule out ingestion latency vs a drop; (b) 0.7.0/Andrew check M365 Junk + run a message-trace on SES MessageId 778dae49-fd50-54ad-990a-cc8ed6536be4 to confirm the mechanism; (c) durable fix if quarantined — send from an **opalinvest.COM** verified identity (intra-domain, trusted) instead of opalinvest.dev, and/or complete DKIM+DMARC for the sending domain. **Cert bar reaffirmed:** delivery certs only when a test message DEMONSTRABLY appears where a human reads it (inbox, not quarantine).

## Compiler Tools

Raw `aws` CloudWatch/SNS/SQS inspection only — rail-checked markers carried (no comp-tool surfaces alarm-history, SNS delivery metrics, SMS-sandbox state, or SQS attributes; comp-routes=CF/apigw, comp-iam=IAM, comp-freshness=S3). Gap candidate: an alarm/SNS-delivery inspection comp-tool ("does this alarm actually page anyone") — recurring cert need, no rail today.

— 3.0.0_SA_CVO
