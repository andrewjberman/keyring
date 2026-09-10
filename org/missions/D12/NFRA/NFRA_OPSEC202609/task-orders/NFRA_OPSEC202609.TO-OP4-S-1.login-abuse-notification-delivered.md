# TO NFRA_OPSEC202609.TO-OP4-S-1 -- FWD-4: the login-abuse notification has NEVER run end to end with a subscriber attached. Fire it once now that delivery is live, and prove DELIVERED on the topic's own metric (OP4-s-1, FWD-4)

<to_id>NFRA_OPSEC202609.TO-OP4-S-1</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.9.0_WK_NFRA_OPSEC202609~7</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D12 · **Fabric:** site-z · **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14** (FWD-4) ·
**Decomp cell:** `OP4-s-1` (round 4, v0.1.0) · **Issuance:** round 4, one cell.

---

## THE CELL

FWD-4, verbatim from the PRD: *"When someone hammers the login page, a named person is told."* **DONE WHEN (EXERCISED):**
*"the notification has fired on a real or staged burst and the person named has read it."* **ACCEPT:** *"a burst of blocked
sign-in attempts produces a message that reaches a named human; a quiet day produces none."*

**What exists:** two CloudWatch alarms on the auth path -- `OPSEC-auth-throttled` (metric `opal/authabuse AuthThrottled`, a
metric filter on the auth log, period 60 s, 1 evaluation, threshold 0) and `OPSEC-auth-login-rate-limit-blocked` (metric
`AWS/WAFV2 BlockedRequests`) -- both with `AlarmActions` = SNS topic
`arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts`, and ONE email subscription on that topic to
`andrew@opalinvest.com`, **CONFIRMED on 2026-09-10** (ARN suffix `:7`).

**Why FWD-4 is NOT_REALIZED despite all of that:** round 2's staged burst (TO-OP-S-6, S6-AC2) transitioned
`OPSEC-auth-throttled` OK -> ALARM at 2026-09-04T00:03:36Z, but S6-AC3 measured **0 subscriptions** at that moment, so
nothing was delivered. The subscription arrived six days later. **The mechanism has never been exercised end to end with a
subscriber attached.** This order does that ONCE: one staged burst, the alarm transition read on the alarm, delivery read
on the topic's own `AWS/SNS` metrics -- and stops. The READ limb ("the person named has read it") is off-artifact by
construction and is NOT this order's: the issuer records Andrew's receipt at its terminal and `1.0.0_SA_CTO~Z` grades on
that record.

## GROUNDING -- read live by the issuer at ~21:5xZ on 2026-09-10; PHASE 1 IS TO RE-TAKE IT, NOT TO TRUST IT

| thing | issuer's read | instrument |
|---|---|---|
| topic subscriptions | 1: `email` `andrew@opalinvest.com`, ARN `...:opal-login-abuse-alerts:7` (CONFIRMED, not PendingConfirmation) | `sns list-subscriptions-by-topic` |
| `OPSEC-auth-throttled` | `OK` since 2026-09-10T11:13:06Z; period 60, evals 1, threshold 0; action = the topic | `cloudwatch describe-alarms` |
| `OPSEC-auth-login-rate-limit-blocked` | `OK` since 2026-09-03T23:51:29Z; same action | same |
| `opal-sentinel` | `SENTINEL_BLOCK_ARMED=false` (WATCH-only); table 674 WATCH / 0 ALLOW / 0 BLOCK | `lambda get-function-configuration`, `dynamodb scan` |
| round-2 burst shape (S6-AC2) | POST `https://opalinvest.dev/auth/login`, fixture identity `opsec-s6-probe-fixture2@opal.invalid`, `User-Agent: opal-s6-probe`, 240 requests; 235 of 240 answered 429; WAF `BlockedRequests` 0 (`Default_Action` on 240 of 240, the app throttle answers first) | the round-2 instance at `../deliverables/0.7.0_AE_CloudOps~T/NFRA_OPSEC202609.TO-OP-S-6.login-abuse-alarm.proof_of_spec.json` |

**Read-only references (reads need no grant):** the metric filter and alarms in
`infra/aws/terraform/portal-auth/cloudwatch-alarms.tf` (what log line counts as `AuthThrottled`); the round-2 instance
above for the burst's exact shape and its two pre-burst false starts.

## THE ACT, IN ORDER

1. **Phase 1 re-ground** = `S4-AC1`, `S4-AC2`, `S4-AC3` below. **Any difference from the table is a STOP and a ROW**; in
   particular a pre-burst `OPSEC-auth-throttled` state other than `OK` means a transition could not be attributed, and the
   burst is not run.
2. **Record `T0`** (UTC, seconds) and this device's egress address (`curl -sS https://checkip.amazonaws.com`) in the
   instance. Then **ONE burst**, round 2's shape and no wider: ~240 POSTs to `https://opalinvest.dev/auth/login`,
   `Content-Type: application/json`, body `{"email":"opsec-s6-probe-fixture2@opal.invalid","password":"not-a-credential"}`,
   `User-Agent: opal-s6-probe`, 8 concurrent threads, 10 s timeout each, run from a small python script you write under
   your deliverables dir. Count the status codes and paste the histogram. **Run `S4-AC2` in the same minute as `T0`** --
   round 2's negative control fired twice on a stale pre-state and this is the same trap.
3. **Wait for the transition**, polling `describe-alarms` every 60 s for up to 5 minutes; then `S4-AC4`.
4. **Wait for delivery metrics**: SNS topic metrics can lag several minutes; poll `get-metric-statistics` every 60 s for
   up to 10 minutes after the transition, then run `S4-AC5` and `S4-AC6` ONCE each as the recorded invocation.
5. `S4-AC7`, `S4-AC8`, `S4-AC9`: nothing created, nothing armed.
6. Write the instance, run the checker from inside the worktree, flip `complete` only if every mechanical criterion PASSES,
   commit once, report once.

## BOUNDS

- **Staged burst under `OP-x-1`'s probe verdict (Andrew's card, ratified), round 2's exact shape.** An invalid fixture
  identity, no credential of any kind. Never paste a credential; there is none.
- ⛔ **ONE BURST.** If `S4-AC4` or `S4-AC5` fails after the first burst, the next act is a ROW naming what the instruments
  read -- not a second burst. "A quiet day produces none" is FWD-4's negative arm and repeated bursts erode it.
- ⛔ **CREATE NOTHING, CHANGE NO INFRASTRUCTURE.** No alarm, topic, subscription, metric filter, dashboard, digest,
  checker, IAM or Terraform change of any kind. The FWD-4 moratorium exception covers exactly the two alarms and one
  topic that exist. If a limb turns out to need a change, STOP and file a row.
- ⛔ **THE SENTINEL STAYS WATCH-ONLY.** Your burst will add or append a WATCH row and a case file for this device's egress
  address, as round 2's bursts did; that is expected. **No ALLOW row, no BLOCK row, no touch to `SENTINEL_BLOCK_ARMED`,
  no touch to the ALLOW list** -- C-4 is not this order's to move.
- **A WAF rate-based block of this device's own egress, if it occurs, self-expires.** Note it in the instance; do not
  clear it, do not touch any IP set.
- **Do NOT attempt the READ limb.** Do not email, message or otherwise contact anyone. Record FIRED and DELIVERED; the
  receipt is the issuer's record.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY; ids
  `NFRA_OPSEC202609-Z-W7-S<n>`; carry `project`, `fabric`, `spec_asserts`, `world_is`, `class`, `hazard_standing`,
  `disposition`, `disarm_owner`; append ONE new fenced ```json block at the END, never edit an existing row) -- then
  keep working. Never a message.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSEC202609~7
  <0.9.0_WK_NFRA_OPSEC202609~7@opal.agent>" -F <msgfile> -- <paths>` (msgfile written by a NON-SHELL writer; **no
  non-ASCII in a commit message**; never `-m`; never pre-`git add`; never `GIT_COMMIT_AUTHOR_OVERRIDE`).
- **Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE**, using the worktree's own copy, with the expected
  ids: `"S4-AC1,S4-AC2,S4-AC3,S4-AC4,S4-AC5,S4-AC6,S4-AC7,S4-AC8,S4-AC9,S4-AC10"`. It treats a tracked artifact with
  only unstaged edits as the CCX class: stage your exact path list for the check, confirm VALID, unstage, then
  `safe-commit`.
- Every criterion invocation runs under `timeout 120`; a timeout is recorded AS the output. The burst itself is an ACT,
  not a criterion's invocation, and is bounded by its own thread and per-request timeouts.
- **Replace `<T0>` and `<T0+Nm>` in the invocations below with the recorded UTC instants** in `YYYY-MM-DDTHH:MM:SSZ` form.

## ACCEPTANCE CRITERIA

<criterion id="S4-AC1" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts --output json</invocation><expect>exactly one subscription, Protocol email, Endpoint andrew@opalinvest.com, whose SubscriptionArn is a full ARN and not the literal PendingConfirmation, pasted verbatim.</expect></criterion> `S4-AC1` -- THE SUBSCRIBER IS STILL THERE AND STILL CONFIRMED, RE-READ, NOT INHERITED.

<criterion id="S4-AC2" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws cloudwatch describe-alarms --alarm-names OPSEC-auth-login-rate-limit-blocked OPSEC-auth-throttled --query 'MetricAlarms[].{n:AlarmName,s:StateValue,t:StateUpdatedTimestamp,a:AlarmActions}' --output json</invocation><expect>both alarms are present with the topic ARN in AlarmActions, and OPSEC-auth-throttled reads StateValue OK at a timestamp within the same minute as T0, pasted verbatim.</expect></criterion> `S4-AC2` -- THE PRE-BURST STATE IS OK, MEASURED IN T0's MINUTE. **This is the control that must be able to fail: a standing ALARM makes any later ALARM reading uninterpretable, and a non-OK read here means NO BURST and a ROW.**

<criterion id="S4-AC3" cell_refs="OP4-s-1"><invocation>timeout 120 curl -sS -o /dev/null -w '%{http_code}' -X POST https://opalinvest.dev/auth/login -H 'Content-Type: application/json' -H 'User-Agent: opal-s6-probe' --data '{"email":"opsec-s6-probe-fixture2@opal.invalid","password":"not-a-credential"}'</invocation><expect>a single HTTP status code recorded verbatim that is a 4xx (400, 401, 403 or 429) and not 5xx or 000.</expect></criterion> `S4-AC3` -- THE PROBE PATH ANSWERS BEFORE 240 REQUESTS ARE SENT AT IT.

<criterion id="S4-AC4" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws cloudwatch describe-alarm-history --alarm-name OPSEC-auth-throttled --history-item-type StateUpdate --start-time <T0> --end-time <T0+15m> --output json</invocation><expect>a StateUpdate item whose HistorySummary reads a transition from OK to ALARM with a Timestamp inside the window, pasted verbatim.</expect></criterion> `S4-AC4` -- FIRED: THE ALARM TRANSITIONED, MEASURED ON THE ALARM'S OWN HISTORY, NOT ON THE RULE.

<criterion id="S4-AC5" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws cloudwatch get-metric-statistics --namespace AWS/SNS --metric-name NumberOfNotificationsDelivered --dimensions Name=TopicName,Value=opal-login-abuse-alerts --statistics Sum --period 60 --start-time <T0> --end-time <T0+20m> --output json</invocation><expect>the Datapoints' Sum values total at least 1 inside the window, pasted verbatim.</expect></criterion> `S4-AC5` -- DELIVERED: SNS REPORTS AT LEAST ONE NOTIFICATION DELIVERED ON THIS TOPIC. **Publish returning a MessageId is SENT, not delivered, and does not satisfy this.**

<criterion id="S4-AC6" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws cloudwatch get-metric-statistics --namespace AWS/SNS --metric-name NumberOfNotificationsFailed --dimensions Name=TopicName,Value=opal-login-abuse-alerts --statistics Sum --period 60 --start-time <T0> --end-time <T0+20m> --output json</invocation><expect>no Datapoint in the window carries a Sum greater than 0, pasted verbatim (an empty Datapoints list satisfies this).</expect></criterion> `S4-AC6` -- NOT FAILED: THE DELIVERY DID NOT BOUNCE.

<criterion id="S4-AC7" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:313476888478:opal-login-abuse-alerts --query 'length(Subscriptions)' --output text</invocation><expect>the value 1, read after the run.</expect></criterion> `S4-AC7` -- NO SUBSCRIPTION WAS ADDED.

<criterion id="S4-AC8" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws cloudwatch describe-alarms --alarm-name-prefix OPSEC- --query 'length(MetricAlarms)' --output text</invocation><expect>the value 2, read after the run.</expect></criterion> `S4-AC8` -- NO ALARM WAS ADDED.

<criterion id="S4-AC9" cell_refs="OP4-s-1"><invocation>timeout 120 .tools/aws lambda get-function-configuration --function-name opal-sentinel --query 'Environment.Variables.SENTINEL_BLOCK_ARMED' --output text</invocation><expect>the literal false, read after the run.</expect></criterion> `S4-AC9` -- THE SENTINEL IS STILL WATCH-ONLY.

<criterion id="S4-AC10" cell_refs="OP4-s-1" judgment="true"/> `S4-AC10` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9, NOT SELF-GRADED.** Whether FWD-4's in-artifact limbs (FIRED and DELIVERED) are now EXERCISED end to end with a subscriber attached, the READ limb being the issuer's record. **Record what the instruments read and offer NO verdict.**

<expected_criteria>S4-AC1, S4-AC2, S4-AC3, S4-AC4, S4-AC5, S4-AC6, S4-AC7, S4-AC8, S4-AC9, S4-AC10</expected_criteria>

<paths>
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP4-S-1.login-abuse-notification-delivered.md
org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~7/
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round4.md</decomp_doc> v0.1.0, cell `OP4-s-1`, round 4.
<owned_cells>OP4-s-1</owned_cells>
Read-dependencies, NOT claimed: `OP-s-6` (round 2, COMPLETE -- built the alarms and the topic), `OP3-s-2` (round 3, COMPLETE -- the subscription Andrew confirmed), `OP-x-1` (the probe verdict authorising a staged burst).
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell builds no scheduled job and no monitor; it exercises two alarms and one topic that already exist and changes none of their cadence, targets or alerting.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Lambda is touched; the AWS reads run under this device's operator credentials and the burst is unauthenticated HTTP against a public path. Stated rather than implied: if a delivery failure turned out to be a topic-policy or subscription problem, that is a ROW for the owning lane, never an edit by this order.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every referent in this face was read LIVE by the issuer at ~21:5xZ (subscription, both alarms, the sentinel's env, the table census) or from the round-2 instance at HEAD, and S4-AC1..AC3 re-take the three that decide whether the burst may run.
</preflight>

<proof_of_spec>
org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~7/NFRA_OPSEC202609.TO-OP4-S-1.login-abuse-notification-delivered.proof_of_spec.json
</proof_of_spec>
