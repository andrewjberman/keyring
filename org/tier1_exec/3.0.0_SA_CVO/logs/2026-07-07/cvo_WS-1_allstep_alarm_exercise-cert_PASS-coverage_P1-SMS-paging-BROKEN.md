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

**INFERRED root cause — CORRECTED (F5 on my own claim):** My first hypothesis ("DKIM NOT_STARTED → DMARC-misalign quarantine") was WRONG and I withdrew it. That `NOT_STARTED` was on the RECIPIENT identity (andrew@opalinvest.com) — irrelevant to outbound auth. The actual SENDER, `opalinvest.dev` / `noreply@opalinvest.dev`, has DKIM `SUCCESS` + signing ENABLED (verified live) — so the mail IS DKIM-signed and DMARC-aligned for opalinvest.dev. DKIM is not the problem, and "complete DKIM" is not the fix.
**Latency also RULED OUT:** on re-check, a LATER external email (16:35:33Z, cottonwoodmail.com) arrived and is visible in the mailbox while the earlier ~16:29Z SES forwards are STILL absent — the mailbox receives fine, the SES forwards specifically do not land. So: not latency, not DKIM.
**Revised INFERRED cause (still hypothesis — message-trace pending):** an M365/Defender impersonation or look-alike-domain filter (sender `opalinvest.dev` is a look-alike of the tenant's OWN `opalinvest.com` — Defender impersonation protection commonly quarantines this class even with valid DKIM), or content spam-scoring on the raw machine-generated body. NOT proven — the definitive check is an M365 message-trace on the SES MessageId; the FIX should not be committed until the trace confirms the cause (Rule 22 — a hypothesis cannot authorize a fix).

**DISPOSITION:** P1 stays OPEN. Mechanical chain PASS; delivery uncertified. Next: (a) I re-verify the mailbox shortly to rule out ingestion latency vs a drop; (b) 0.7.0/Andrew check M365 Junk + run a message-trace on SES MessageId 778dae49-fd50-54ad-990a-cc8ed6536be4 to confirm the mechanism; (c) durable fix if quarantined — send from an **opalinvest.COM** verified identity (intra-domain, trusted) instead of opalinvest.dev, and/or complete DKIM+DMARC for the sending domain. **Cert bar reaffirmed:** delivery certs only when a test message DEMONSTRABLY appears where a human reads it (inbox, not quarantine).

## RESOLUTION — root cause GROUNDED (both directions proven) + a fast no-DNS fix

Collaborative convergence with 0.7.0 (they corrected my sender error; I confirmed their mechanism + found the fast fix). **I was wrong on the sender twice** (inferred noreply@opalinvest.dev from ETFS-orchestrator context without reading THIS Lambda; owned). Ground truth, all independently verified this session:
- **Actual sender = `andrew@opalinvest.com`** — read the deployed code myself: `infra/aws/lambda/partner-etl-ops-sqs-consumer/lambda_function.py:41` `EMAIL_SENDER="andrew@opalinvest.com"`, `Source=EMAIL_SENDER` L119.
- **andrew@opalinvest.com auth:** SES Verified=true but DKIM=NOT_STARTED, SigningEnabled=false (unsigned).
- **opalinvest.com DNS (my own nslookup):** SPF `v=spf1 include:mailgun.org include:spfa.cpmails.com include:spf.protection.outlook.com ~all` — SES NOT included → SPF fail for SES-origin mail; DMARC `p=none` (monitor-only). So it's EOP's own anti-impersonation heuristic (external infra claiming to BE the tenant's exact own address, zero SPF/DKIM alignment = spoof signature), not a DMARC-policy reject. Silent quarantine, no SES bounce — matches the symptom exactly.

**Both directions PROVEN against Andrew's live mailbox:**
- **FAILING path (the consumer):** `search_email` for the alarm subjects → EMPTY. From:andrew@opalinvest.com forwards absent (quarantined).
- **WORKING path (existence proof):** `search_email "Opal ETF Ownership Month-End Report"` → TWO emails IN the mailbox, both **From: noreply@opalinvest.dev** (2026-05 @06-25T23:30Z, 2026-06 @07-01T14:02Z). The ETFS reporter's opalinvest.dev sender (DKIM-SUCCESS via the verified domain → DMARC-aligned) reliably delivers to andrew@opalinvest.com's inbox.

**FAST FIX (grounded, no DNS/IT dependency, deployable today) — handed to 0.7.0:** change the consumer's `EMAIL_SENDER` from `andrew@opalinvest.com` to `noreply@opalinvest.dev` (recipient unchanged). It's the exact sender proven-in-mailbox above. This unblocks the pager NOW — the opalinvest.com-domain SES-verify + DKIM-CNAME + SPF-include DNS chain (GoDaddy/IT-gated, per 0.7.0) is downgraded from BLOCKING to a nice-to-have (only needed if mail must legitimately come From:@opalinvest.com). The message-trace is no longer gating the fix (the working-vs-failing sender proof is stronger for the fix direction than the trace's quarantine-reason would be).

**RE-CERT BAR:** after 0.7.0 switches the sender + redeploys + fires a test, I confirm the forward APPEARS in Andrew's mailbox (search_email) → then endpoint-delivery certs PASS and this P1 closes. Until then: mechanical chain PASS, delivery uncertified, P1 OPEN.

## Compiler Tools

Raw `aws` CloudWatch/SNS/SQS inspection only — rail-checked markers carried (no comp-tool surfaces alarm-history, SNS delivery metrics, SMS-sandbox state, or SQS attributes; comp-routes=CF/apigw, comp-iam=IAM, comp-freshness=S3). Gap candidate: an alarm/SNS-delivery inspection comp-tool ("does this alarm actually page anyone") — recurring cert need, no rail today.

— 3.0.0_SA_CVO
