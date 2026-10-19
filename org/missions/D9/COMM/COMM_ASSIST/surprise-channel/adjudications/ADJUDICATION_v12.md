# COMM_ASSIST -- surprise channel, ADJUDICATION v12 (laptop) -- ROUND 22 L8, with ROUND 21 folded in

<sweep_watermark>2026-10-19T18:55Z</sweep_watermark>

**Author:** `3.0.0_SA_CVO` (base, laptop), 2026-10-19 ~18:5xZ, on `2.0.0_SA_COO~CA` msg 109862 (packet
`deliverables/2.0.0_SA_COO~CA/ROUND22_L8_PACKET_20261019.md` @9fcb5cb5d1). `round-close-check --project COMM_ASSIST`, run by this
seat: round 21 orders=2 complete, judgment 0, MAY-CLOSE; round 22 orders=2 complete, judgment 0, MAY-CLOSE.
**Denominator:** the 76 ids in `investigations/INVESTIGATION_v1.md`, against the `adjudicates` lists of the 17 adjudication and
remediation files: 8 ids are not yet adjudicated, all after the v11 watermark (2026-10-16T03:55Z). Five are ROUND 21's (W32-S1 to
W32-S4, S4), which had no L8 compile on record (no round-21 packet, no v-file); three are ROUND 22's (W33-S1, W33-S2, S5). This
compile dispositions all eight.

**Result: 8 of 8 rows dispositioned, nothing graduates, no REMEDIATION file. S5, the one ARMED row, is disarmed by this seat's own
log read (the gateway outage began 3.5 minutes before the apply and ended at 18:26Z). The CA-p-2 deploy is confirmed live (C-S27).**

```json
[
 {
  "id": "COMM_ASSIST-C-S22",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-19T18:55Z",
  "one_line": "Round 21, W32-S1 and W32-S3 (OBSERVATION, INERT), both code readings by worker ~32: S1 is an ambiguous order sentence the build read the safe way (an empty page raises active to nothing); S3 is a reply sent again in a later poll under the same event id, which the LDO runtime refuses for 7 days, not only for the FIFO queue's 5-minute window.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "COMM_ASSIST-W32-S1",
   "COMM_ASSIST-W32-S3"
  ],
  "spec_asserts": "TO-CA-n-1 item 3: the thread cursor and active are raised from the newest created seen; each reply becomes ONE event.",
  "world_is": "S1: the merged code (1aa63bde67, live until 17:43Z today and unchanged at e6c37673c8) takes 'it' as the newest created seen, so the starvation the literal reading predicts is not built. S3: ldo.py at e6c37673c8 writes a marker {pk=object_id, sk='event#'+event_id} with ConditionExpression attribute_not_exists(pk) in the same transaction as the event's effects (ldo.py:253-258), kept LDO_DEDUP_DAYS (default 7); channel_mentions.py:272-273 sends cut-short reads deliberately on that basis ('event ids de-duplicate'). A repeat 'mention-<reply id>' is refused, not texted twice.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show e6c37673c8:infra/aws/terraform/modules/ldo/runtime/ldo.py :240-262",
    "git show e6c37673c8:data/transcripts/scripts/teams_chat/channel_mentions.py :255-290",
    "git diff --numstat 1aa63bde67 e6c37673c8 over the packaged paths: channel_mentions.py and ldo.py 0"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S1: the build already took the correct reading; S3: the downstream guard the row depends on exists and is durable for 7 days. No defect in the served code."
 },
 {
  "id": "COMM_ASSIST-C-S23",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-19T18:55Z",
  "one_line": "Round 21, W32-S2 (a failing thread held its whole channel's cursor) and W32-S4 (BLOCKING, INERT: AC3 failed in a sparse worktree without daily_reports/eod/) were both resolved inside round 21 by the issuer's amendment 9552754dff, and the W32-S2 fix is in the code that has been served since.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "COMM_ASSIST-W32-S2",
   "COMM_ASSIST-W32-S4"
  ],
  "spec_asserts": "TO-CA-n-1 item 4 (as amended): a failed thread costs only that thread; CAn1-AC3: the I2 regression passes.",
  "world_is": "9552754dff added check arm 8 thread_failure_isolated and the eod path to the worktree's sparse set; it is an ancestor of the round-21 deploy pin 1aa63bde67. channel_mentions.py at e6c37673c8 :267-270 counts thread errors without holding the channel's events or cursor ('a failed thread costs only itself'). round-close-check round 21: 2 of 2 orders complete, proofs structurally OK.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show --stat 9552754dff",
    "git merge-base --is-ancestor 9552754dff 1aa63bde67 (yes)",
    "python .tools/round-close-check.py --project COMM_ASSIST --round 21 (MAY-CLOSE)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolved in round 21 by the issuer's own amendment; the fix is in the served code."
 },
 {
  "id": "COMM_ASSIST-C-S24",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-19T18:55Z",
  "one_line": "Round 21, S4 (OBSERVATION, INERT, lane 0.7.0_AE_CloudOps~COMM1): a targeted plan of module.ldo_001 needs the gitignored transcripts-pull dist zip because the root hashes three untargeted Lambdas at load; the applier built it and the saved plan still named only the handler and ingress[0].",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "COMM_ASSIST-S4"
  ],
  "spec_asserts": "TO-CA-n-2 steps 1, 4 and 5: build teams-chat-assist only, then a saved targeted plan.",
  "world_is": "The act was not widened: the plan's 2 changes were module.ldo_001's two functions. Round 22's apply (17:43Z) landed on the same root without a new row on this point. The deploy-order text, not the product, is what lacks the step.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md row COMM_ASSIST-S4",
    "deliverables/2.0.0_SA_COO~CA/ROUND22_L8_PACKET_20261019.md @9fcb5cb5d1 (CA-p-2 applied, re-plan no changes)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A deploy-order wording gap with no effect on the act; carried to the slug as a template note (name the transcripts-pull build in the next ldo_001 deploy order)."
 },
 {
  "id": "COMM_ASSIST-C-S25",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-19T18:55Z",
  "one_line": "Round 22, W33-S1 and W33-S2 (OBSERVATION, INERT, worker ~33): three commit gates read blind in a sparse worktree (client account-id list ABSENT, naming gate missing a folder, stale risk map), and the code commit carries the Haiku attribution line where the order asked for Sonnet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "COMM_ASSIST-W33-S1",
   "COMM_ASSIST-W33-S2"
  ],
  "spec_asserts": "A tree change is checked by the commit gates before it lands; the order's ACCEPTANCE names the attribution line.",
  "world_is": "The absent account-id list is the condition closed NOT_A_DEFECT by design in C-S16 (W29-S2, W21-S1, on Andrew's 2026-10-09 word). The change touches no account id and no name (git diff 1aa63bde67..e6c37673c8 of mail_requests.py: REASONS, _my_addresses, considered, on_mail_messages only). The attribution line is the harness's truthful one for the model that ran; nothing reads it.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "adjudications/ADJUDICATION_v9.md row COMM_ASSIST-C-S16",
    "git diff 1aa63bde67 e6c37673c8 -- data/transcripts/scripts/teams_chat/mail_requests.py"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S1: a known by-design gate state and two sparse-worktree blind spots with no bearing on this change; S2: the attribution names the model that actually ran."
 },
 {
  "id": "COMM_ASSIST-C-S26",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-19T18:55Z",
  "one_line": "Round 22, S5 (OBSERVATION, ARMED, disarm_owner 2.0.0_SA_COO~CA): the gateway stopped answering before the CA-p-2 apply and recovered at 18:26Z; read by this seat from both functions' logs, the deploy did not cause it, and the changed code has run clean since. DISARMED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "COMM_ASSIST-S5"
  ],
  "spec_asserts": "COO half condition 3: within 10 minutes of the apply the ingress shows channel_poll, ingress_poll and the mail step, with no error but the 502s the gateway already shows.",
  "world_is": "Ingress 17:30-17:44Z: last ingress_poll 17:38:19Z; first status=504 17:40:18Z; first Status: timeout 17:41:18Z; apply 17:43:49Z/17:43:55Z. Ingress 17:44Z-18:51Z: 123 timeouts and 119 status=504, the last at 18:26:10Z and 18:26:02Z; from 18:26:17Z, 41 channel_poll, 27 ingress_poll, 8 mail_poll. The 8 RuntimeError lines (one at 17:34:06Z BEFORE the apply, seven queued at 18:26:17-18Z) are all 'ingress_step_failed step=channels: channel_poll failed=N route=channel_messages status=502', the gateway 502s condition 3 allows; none after 18:26:18Z. Handler 17:43:55Z-18:51Z: 5 mail_considered lines, 0 me-without-mail, 0 Traceback, 0 AccessDenied. What ended the outage is not measured here (the packet names site Z's restart order OG-rs-1 as INFERRED).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/aws logs filter-log-events /aws/lambda/teams-global-chat-assist-ingress-lambda 2026-10-19T17:30Z-18:51Z (751 events, counted)",
    ".tools/aws logs filter-log-events /aws/lambda/teams-global-chat-assist-handler-lambda 2026-10-19T17:43:55Z-18:51Z (47 events, counted)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed by measurement: the outage predates the apply and has ended, and the changed code runs without error. The gateway's own remedy lives with NFRA_OPLGTW, not this project."
 },
 {
  "id": "COMM_ASSIST-C-S27",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-19T18:55Z",
  "one_line": "Round 22 CA-p-2 read live by this seat at 18:50Z: both functions serve p4kaI5t0i6vgzAZ0xONR/e8G9iDBU3icKNb3PvUdGEg= (this seat's signed after-hash), 15 keys, INGRESS_MARK_MODE=enforce, DLQ 0/0/0; the five post-apply mail_considered lines carry the new from_andrew key (0 each), so the served code is the code that ran.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CVO never-widen half R22 (f104cc803d): branch A, after-hash p4kaI5t0..., code only, mode enforce.",
  "world_is": "Handler LastModified 17:43:55Z, ingress 17:43:49Z, both on the after-hash; 15 environment keys and enforce on both; teams-global-chat-assist-dlq.fifo visible/in-flight/delayed 0/0/0. mail_considered at 18:31:20Z (x2), 18:31:24Z, 18:31:25Z, 18:41:22Z: body_no_andrew 1, from_andrew 0, ok 0 each, matching the packet's batches=5 body_no_andrew=5. NOT exercised live: a refusal of Andrew's own mail (from_andrew=0 so far) and a colleague's draft after the apply; both are natural reads.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/aws lambda get-function-configuration, both functions, 2026-10-19T18:50:26Z",
    ".tools/aws sqs get-queue-attributes teams-global-chat-assist-dlq.fifo, 18:50Z",
    ".tools/aws logs filter-log-events handler, pattern mail_considered"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A record of the deploy's served state against its signed expectation; no defect."
 }
]
```

## L10 slug (this seat's one send to `1.0.0_SA_CTO`)

Rounds 21 and 22 are terminal and every row is dispositioned; nothing BLOCKING or ARMED stands. Round 21 had no L8 compile on
record and is closed here with round 22. CA-p-2 is live on the signed hash and the first five mail events ran clean (condition 8
met). Not exercised live: a refusal of Andrew's own mail and a colleague's post-apply draft, both natural. The issuer's three
enrichment candidates stand; this seat adds one template note: the next `module.ldo_001` deploy order names the transcripts-pull
build (C-S24).

-- 3.0.0_SA_CVO
