# COMM_ASSIST decomposition -- round 18: the ingress mark, and one sitting for Andrew (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-14 ~03:0xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO`'s round-17 analysis `ledger/ROUND_ANALYSIS.round17.md` (msg 109054), over PRD v0.7 (the ratified-text half SIGNED by `3.0.0_SA_CVO~L`, current by ENDPOINT hash). The CVO's L10 slug `REMEDIATION_v4.md` @bd4d7b90e4 (watermark 02:45Z) closed round 17:
14 of 14 orders complete, three rows graduate, one ARMED (`W10-S2`).

**Direction (binding):** muse replaces the Kimi text agent as Andrew's interface; the text path stays the fallback. Whether Kimi also stops drafting is held at Andrew (`87a2`).

**The analysis's five items and what the issuer does with each.**

1. `W10-S2` the SMS ingress mark (P1, a WORLD deploy under its own pair) -> cells CA-j-1, CA-j-2, CA-j-3, CA-j-5 below.
2. FWD-6 and `W18-S2` as ONE Andrew sitting -> not a cell: it is Andrew's act. The issuer rewrites the open call (`8fb2` and `cd2d` close as superseded by one new call) and the card (`r18/MUSE_SITTING_CARD.md`). The sitting needs a draft Andrew is content to drop.
3. J290's first real use, then the OPLGTW draft route -> Andrew's act (carried open call) and MSTR's, not a cell.
4. The agentbus read (no `unstamped sender=LDO-001` since CA-i-4) -> not a cell: the issuer asks `0.0.0_AB_MSTR` to read every box's consumer log and reads the laptop's own.
5. ONE batch cell: `D2-S1` (the forwarder creates `answers/` and its subfolders) -> CA-j-4.

**Why W10-S2 is five cells, not one.** The producers of the two text-driven kinds (`sms.reply`, `owner.text`) are FOUR sites in `tenant.py`: the ingress (`_route_commands`: one for `owner.text`, one for `sms.reply`) and the handler's own re-sends (`on_owner_text`, two `ctx.send` of `sms.reply`).
A mark that covers only the ingress would make the handler's own re-sends look forged, so all four are stamped together. A mark that is enforced the moment it is deployed would drop any text already in flight from the old ingress, so the rollout has a mode: `off`, `record` (check and count, act anyway), `enforce` (refuse).
The mark is an HMAC-SHA256 over the object id, the kind, the mark time and the canonical payload, keyed by a secret that only the assistant's two functions can read; an identity that can write to the queue but not read the secret cannot forge it, and reading the secret is a logged management event (the CTO's stated limit).

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-1` | `ingress_mark.py` (stamp, verify), the `dispatch` gate with the three modes, the four producer sites stamped, the `NAMES.json` row `secrets.ingress_mark`, tests | FWD-7 (every answer in his name) | LOCAL | chain 0, slot ~19 | none |
| `CA-j-4` | the forwarder creates `answers/`, `answers/done/`, `answers/rejected/` when absent (seat row D2-S1) | FWD-7, FWD-8 | LOCAL, DIRECT-ACT | chain 1, slot ~20 | none |
| `CA-j-2` | `chat_assist.tf`: the secret resource, the secret in `secret_arns`, the variable and environment key `INGRESS_MARK_MODE` defaulting to `record` | FWD-7 | WORLD (inferred floor; edit only) | after CA-j-1 | CA-j-1 merged |
| `CA-j-3` | DEPLOY 1: the targeted apply of `module.ldo_001` (code, the new secret, the environment key), and the secret's VALUE put out of band; never-widen set | FWD-7 | WORLD | the CloudOps seat | CA-j-1, CA-j-2 merged; halves |
| `CA-j-5` | DEPLOY 2: the variable's default flips `record` -> `enforce` (an environment-only change), after the record-mode read shows no unmarked legitimate event | FWD-7 | WORLD | the CloudOps seat | CA-j-3 closed; a stated observation window; halves |
| `CA-j-6` | FWD-12, muse's efficacy against the text path | FWD-12 | LOCAL / SERVED | next round | FWD-6 read (Andrew's sitting) |

`fanout: 2 of 2 chains, cap 8, reason: CA-j-1 writes tenant.py, ingress_mark.py, NAMES.json and tests; CA-j-4 writes forwarder.py; they share nothing. CA-j-2 waits on CA-j-1's NAMES.json row (Terraform reads it at plan time) and the deploys wait on both.`

**Rule 24.** Domain: the analysis's enrichment items 1 to 5. Uncovered member by subtraction from the printed denominator (5 items): item 1 is CA-j-1, 2, 3, 5; item 2 is Andrew's sitting; item 3 Andrew's act; item 4 the read; item 5 CA-j-4. None uncovered.

**The issuer's real runs at close:** the live `check_j3_live` and `check_j5_live` reads after each apply; one real text from Andrew's phone routed through the ingress and visible as a marked event with `unmarked_seen` still 0 in record mode (read from the state row, never from content); a forged `sms.reply` put on the queue by the issuer in enforce mode refused and recorded.

## AMENDMENT 1 (2.0.0_SA_COO~CA, 2026-10-14 ~03:5xZ): CA-j-1 merged, CA-j-2 cut

CA-j-1 merged @0ca94ce0b6 (worker ~19; `check_j1_mark` 9 of 9, `check_i2_regression` 64 of 64, `check_i13_fresh` 6 of 6, the whole flow-test set 544 of 544). Row W19-S2 (the sibling flow test compared the handler re-sends as exact payloads) was ruled by adding `test_teams_chat_natural.py` to that order's paths (its AMENDMENT 1, commit 53be82a3cd); rows W19-S1, S3, S4, S5, S6 are INERT.
CA-j-2 depends only on the `NAMES.json` row, now merged, so it is cut under workstream `INGRESSTF` (the gate admits a new order in an issued round only with a `<workstream>` element). The issuer amends its own decomposition without a CTO ruling; no gate limb is claimed for this paragraph, and the new order's own commit states the limb that graded it.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-2` | `chat_assist.tf`: the secret shell, the secret in `secret_arns`, the variable and environment key `INGRESS_MARK_MODE` defaulting to `record`; issuer check `r18/checks/check_j2_tf.py` (base 4 of 7, scratch reference 7 of 7) | FWD-7 | WORLD (inferred floor; edit only) | workstream INGRESSTF, slot ~21 | CA-j-1 merged |

`fanout (amendment 1): 1 of 1 chain, cap 8, reason: one file (chat_assist.tf); CA-j-3 and CA-j-5 wait on this merge and on their never-widen halves.`

For CA-j-5 (the flip to enforce): the mark's freshness bound is 15 minutes (`ingress_mark.verify`) and the handler refuses a replayed mark, so the record-mode read must show `unmarked_seen` 0 across a real text AND must look for `stale-mark` refusals from queue delay or redelivery before the flip is asked for.

## AMENDMENT 2 (2.0.0_SA_COO~CA, 2026-10-14 ~04:4xZ): CA-j-2 merged, CA-j-3 staged

CA-j-2 merged @38ce5a7981 (worker ~21; `check_j2_tf` 7 of 7, `check_i4a_tf` green; the first proof instance read INVALID at the worker's final head because its artifact row predated the instance commit, and a fresh worker pinned the row to 6cfb79f314; row W21-S1, the client-data list absent on this box, was measured by hand: no client id in the 130 added lines). The CloudOps seat `0.7.0_AE_CloudOps~CA` is given CA-j-3 as a STAGED order (`<status>staged</status>`, GO written when all three halves are SIGNED on the pin 38ce5a7981).

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-3` | DEPLOY in three steps: (1) the secret shell by a targeted apply, (2) its value out of band, (3) one targeted apply of `module.ldo_001` (code, environment `INGRESS_MARK_MODE=record`, the one policy ARN); issuer checks `check_j3_equiv.py` (before; pre-flight read 17 of 17, files=3, foreign=1), `check_j3_live.py` (after), `check_j3_ledger.sh` (NEVER-2) | FWD-7 | WORLD | workstream DEPLOY18, the CloudOps seat | CA-j-1, CA-j-2 merged; halves |

`fanout (amendment 2): 1 of 1 chain, cap 8, reason: one deploy act; CA-j-5 (the flip to enforce) waits on its close and on an observation window.`

## AMENDMENT 3 (2.0.0_SA_COO~CA, 2026-10-14 ~04:4xZ): CA-j-3 GO; two prerequisites carried to CA-j-5

All three halves for CA-j-3 are SIGNED on the pin 38ce5a7981 (CTO @fa9ad4302e, CVO @29f8d9d49f); the order is `pending` with GO. The CVO half names two things the enforce flip (CA-j-5) must settle BEFORE its own pair:
1. The Dell users `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` can read the mark's key (`simulate-principal-policy`: `secretsmanager:GetSecretValue` ALLOWED), and W10-S2 named the Dell identities among those that can put `sms.reply` on the queue, so in enforce mode the mark does not stop them. CA-j-5 states this limit in the PRD's words, or narrows the key first (a resource policy on the secret denying `GetSecretValue` to every principal except the two function roles).
2. Whether a legitimate text can reach the handler more than 15 minutes after its mark (a mailbox backlog, a retried event) has not been read; in enforce it would be refused `stale-mark`. The record-mode read must look for `stale-mark` refusals.

## AMENDMENT 4 (2.0.0_SA_COO~CA, 2026-10-14 ~05:4xZ): CA-j-3 closed; the CTO narrows the mark's key (call 97c6); CA-j-7 cut, CA-j-8 named

CA-j-3 is CLOSED (ledger `comm-assist-r18-deploy` @1daa4a97ce; the issuer's own `check_j3_live` and `check_j3_ledger` read PASS at 05:11Z). The CTO ruled call 97c6 NARROW (msg 109075, `CTO_RULING_20261014_052xZ_COMM_ASSIST_INGRESS_MARK_KEY_NARROWED.md`): a resource policy on `teams/global/ingress-mark` denies `GetSecretValue` to every principal except the assistant's execution role, as its own WORLD cell with its own pair, cut and applied BEFORE CA-j-5's flip; CA-j-5's pair reads it live (a Dell agent user's simulated read `explicitDeny`, the execution role's `allowed`); the residual (an admin can rewrite the policy, a recorded management write) is stated in the PRD addendum beside v0.7's.
The handler and the ingress share ONE role (`module.ldo_001.execution_role_name`, one output of the module, so no module edit). The issuer simulated the exact policy before cutting: the execution role allowed, both Dell users explicitDeny, and allowed with no policy (3 principals). New orders in an issued round are admitted only with `<workstream>`.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-7` | `chat_assist.tf`: the resource policy `aws_secretsmanager_secret_policy.ca_ingress_mark` (Deny `GetSecretValue` unless the principal is the execution role); issuer check `r18/checks/check_j7_tf.py` (base 2 of 6, scratch reference 6 of 6, two negative controls fail as intended) | FWD-7 | WORLD (inferred floor; edit only) | workstream INGRESSKEY, slot ~22 | CA-j-3 closed |
| `CA-j-8` | DEPLOY of the policy (one targeted apply, expected `1 to add, 0 to change, 0 to destroy`, code unchanged), its own never-widen set, a live check (policy present; Dell users explicitDeny, execution role allowed, by simulation against the live policy) | FWD-7 | WORLD | the CloudOps seat | CA-j-7 merged; halves |
| `CA-j-5` | (restated) the flip to `enforce`, after CA-j-8 closes AND a stated observation window with no unmarked legitimate event and no `stale-mark` refusal | FWD-7 | WORLD | the CloudOps seat | CA-j-8 closed; window; halves |

`fanout (amendment 4): 1 of 1 chain, cap 8, reason: one file (chat_assist.tf); CA-j-8 waits on the merge, CA-j-5 on CA-j-8 and Andrew's texts.`

## AMENDMENT 5 (2.0.0_SA_COO~CA, 2026-10-14 ~10:5xZ): the CVO's open question on the 15-minute bound is ANSWERED by a read, and it is a yes

AMENDMENT 3 carried to CA-j-5 whether a legitimate text can reach the handler more than 15 minutes after its mark. Read at ~10:4xZ from the live mailbox `teams-global-chat-assist-queue.fifo`: `VisibilityTimeout` 3600 s, `RedrivePolicy` maxReceiveCount 3 (dead-letter queue `teams-global-chat-assist-dlq.fifo`), `MessageRetentionPeriod` 345600 s; the handler's event source mapping is batch size 1 with `ReportBatchItemFailures` and no maximum-retry cap. `ingress_mark.MAX_AGE_S` is 15 * 60 (line 20).
So an event whose first handling FAILS (an exception in the handler) is redelivered an HOUR later (and again an hour after that, then dead-lettered). In `record` mode that retry acts (and counts a `stale-mark`). In `enforce` mode the same retry is refused as `stale-mark`: `dispatch` returns `unmarked-refused` normally, so SQS DELETES the event and the answer is lost, leaving only a line in `mark_refusals`. The same applies to the 15-minute bound on any handler stall longer than the bound. Replay protection does not rest on the bound alone: a mark is single-use (`marks_seen`, the last 100 per object), and a forger cannot mint a mark without the key (now narrowed to the execution role).
This is a design choice, queued to the CTO as a call with a recommendation: widen `MAX_AGE_S` to cover the retry gaps (the REC is 4 hours: two redeliveries at 3600 s plus margin), as a LOCAL code cell with a deploy pair BEFORE the flip to `enforce`; the alternative is to accept that a failed-then-retried answer is dropped in `enforce`. Until it is ruled, CA-j-5 does not flip, and the observation read (`check_j5_obs`) also counts `stale-mark` refusals as DIRTY.

## AMENDMENT 6 (2.0.0_SA_COO~CA, 2026-10-14 ~11:0xZ): the CTO rules call 847f (widen to 4 hours); CA-j-9 cut, CA-j-10 named

The CTO ruled call 847f (msg 109095, `CTO_RULING_20261014_104xZ_COMM_ASSIST_MARK_FRESHNESS_4H.md`): `MAX_AGE_S` becomes 4 hours, as a LOCAL code cell with its own deploy pair BEFORE CA-j-5; the queue's visibility timeout is not shortened. Binding: `marks_seen` holds EVERY mark younger than `MAX_AGE_S` (pruned by age, never a count cap); the test shows a replay at 3h59m refused and a 4h01m mark `stale-mark`; a refusal records the event's kind and tag (never the payload). New orders in an issued round are admitted only with `<workstream>`.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-9` | `ingress_mark.py` `MAX_AGE_S` 4 h; `tenant.py` `_mark_refused` keeps marks by age with no count cap and records kind and tag on a refusal; tests; issuer check `r18/checks/check_j9_fresh.py` (base 1 of 7, scratch reference 7 of 7, a restored count cap reads 6 of 7); the CA-j-1 check amended to stale its mark at 5 hours so it reads 9 of 9 before and after | FWD-7 | LOCAL | workstream FRESHMARK, slot ~23 | CA-j-1 merged |
| `CA-j-10` | DEPLOY of CA-j-9 (one targeted apply of `module.ldo_001`, code only), its own never-widen set | FWD-7 | WORLD | the CloudOps seat | CA-j-9 merged; halves |
| `CA-j-5` | (restated) the flip to `enforce`, after CA-j-10 closes AND the observation window reads CLEAN (`check_j5_obs`: at least 3 marked texts, 0 unmarked and no `stale-mark`) | FWD-7 | WORLD | the CloudOps seat | CA-j-10 closed; window; halves |

`fanout (amendment 6): 1 of 1 chain, cap 8, reason: two source files and one test file (tenant.py, ingress_mark.py, test_ingress_mark.py); CA-j-10 waits on the merge.`

## AMENDMENT 7 (2.0.0_SA_COO~CA, 2026-10-14 ~12:0xZ): CA-j-10 closed; Andrew's word adds FWD-13 (muse ALERTS him); the folder side of its first read

CA-j-10 is CLOSED (ledger `comm-assist-r18-fresh-deploy` @0a79b22d2a; the issuer's own `check_j10_live` PASS, `check_j10_ledger` PASS, proof VALID, 0 `AccessDenied`). Andrew-direct ~11:4xZ via the CTO (msg 109111; record `ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md`): call 87a2 answered, Kimi keeps drafting until FWD-12 retires it; and "I have not yet seen muse alert me with new emails/teams" becomes PRD v0.9 FWD-13 @98f61b8a2e: muse tells him of each new Teams message or @mention, or mail naming him, from the SAME dell2 folder FWD-6 serves, once per item, an unreadable item as unreadable, an item not for him as no alert. The ratified-text half re-signs (an ENDPOINT addition: CVO owed, `prd-signoff.py status` reads STALE), and a newly added task order is refused until it does.
**Folder side of the first read (the issuer's read of the repo; the muse side is muse's to answer, delivered off git, never committed).** What `drafts.json` and `eod_today.json` carry today, from `refresh.py` and `tenant.py`/`mail_requests.py`: a row per DRAFT waiting for his 1 or 0, with `object_id`, `tag`, `kind` (`chat`, `mail` or `eod`), `version`, `seq`, `status`, `texted_at` and the aged keys `age_minutes`/`age_from`; every source has `status` ok/absent/unreadable, `read_at`, `last_good_at` in `INDEX.json`; the job refreshes every 15 minutes. So a row is identified by (`object_id`, `version`), carries when it was texted, and a source that failed says so. What the folder does NOT carry: (1) a channel @MENTION: `channel_mentions.on_channel_mention` texts him once and writes no draft and no state row (its own docstring: "No draft and no send to Teams"); only a once-record keyed by the message id sits on the event object, and it holds no sender, channel or time; (2) any chat message the assistant does not draft a reply for (an ignored chat: by design, the "not for him" case); (3) most mail: only a mail the poller CONSIDERS (`mail_requests.considered`, a sender-domain test) gets a draft row, and the mail object holds ONE `pending` (`mail_requests.py` line 273 overwrites it), so a second considered mail before the 15-minute refresh HIDES the first; the object's `draft_seq` rises by one per considered mail, so a jump in `seq` between two reads is the only trace of a mail the folder never showed (muse can alert "one earlier mail not shown" from that gap, but cannot show it).
Consequence: FWD-13's DONE WHEN (one real Teams item and one real mail each reach him as a muse alert, one not-for-him item none) is reachable for CHAT items by muse keeping a seen-set of (`object_id`, `version`) over `drafts.json`, and for MAIL only as the latest considered mail plus a seq-gap notice (a mail-list source would close it); a @MENTION cannot alert from the folder until the reader gains a source for it (a minimal state record written when a mention is texted: message id, team and channel names, sender, created time, a short scrubbed snippet, never a secret). The alert's latency floor is the 15-minute refresh plus muse's own poll.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-11` | FWD-13 first read, MUSE side: what muse watches today, how often, how it keeps a seen-set across sessions, how it reaches Andrew, what it needs from the folder to know new / for him / unreadable; delivered to muse off git; the issuer's DIRECT-ACT, no worker (a worker cannot message) | FWD-13 | LOCAL read | the issuer | none (a read) |
| `CA-j-12` | the reader gains a `mentions` source (a record written where a mention is texted, read into the folder, scrubbed) and, if muse's answer asks for it, a list of recent considered mail (the single `pending` hides all but the latest); tests; a dell2 pick-up | FWD-13 | LOCAL code, then SERVED | next order, not cut | CA-j-11's answer; the CVO re-sign |
| `CA-j-13` | FWD-13's exercise: one real Teams item and one real mail alert him, one not-for-him item none | FWD-13 | SERVED | not cut | CA-j-11, CA-j-12 |

`fanout (amendment 7): none cut now; CA-j-11 is the issuer's own read. CA-j-12 and CA-j-13 are named, not cut, and wait on muse's answer and on the CVO's re-sign of the ratified-text half.`

## AMENDMENT 8 (2.0.0_SA_COO~CA, 2026-10-14 ~13:3xZ): muse answered; the FWD-13 cells cut (CA-j-12, CA-j-13), the rest named and renumbered

The CTO ruled call 608c YES (msg 109140, `RULING_20261014_124xZ_COMM_ASSIST_608C_FWD13_TWO_SCRUBBED_RECORDS.md`): the two scrubbed records, metadata only (never a body, link or actionable token), written where the item is texted today with a 7-day expiry enforced on write, the negative arm unchanged. Muse answered the shape question in the Gmail thread Andrew authorized as the coordination channel: it has no standing watch today; on its side it needs a scheduled read, an alert ledger and a wake mechanism (its own build); and it asked for `mentions.json` and `mail_log.json` beside `drafts.json`, flat rows with stable ids, timestamps and ages. The issuer replied with the field list below; muse has not objected. The record fields and the two checks are the contract: `r18/checks/check_k1_records.py` (assistant half) and `check_k2_reader.py` (reader half).
The cell numbers of AMENDMENT 7 are SUPERSEDED: CA-j-12 is now the assistant half, CA-j-13 the reader half, and the deploys and the exercise follow.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-12` | assistant half: `channel_mentions.on_channel_mention` writes `state["mentions"]` and `mail_requests.on_mail_messages` writes `state["mail_log"]` (fields in `check_k1_records.py`; a shared scrub; 7-day expiry and a cap on write; written only where the item is texted/considered); tests; issuer check `check_k1_records.py` (base 1 of 8, scratch reference 8 of 8, a kept link reads 6 of 8) | FWD-13 | LOCAL | workstream MENTREC, slot ~24 | none |
| `CA-j-13` | reader half: `muse_reader/refresh.py` gains the sources `mentions` and `mail_log` (read from the state rows, 7-day expiry on read, absent not empty, scrubbed, README); tests; issuer check `check_k2_reader.py` (base 0 of 7, scratch reference 7 of 7, no-expiry reads 4 of 7); the existing reader controls still pass against it (`check_i1_ages` 5 of 5, `check_h1_failure_shape` ok) | FWD-13 | LOCAL | workstream RDRSRC, slot ~25 | none (disjoint files from CA-j-12) |
| `CA-j-14` | DEPLOY of CA-j-12 (a targeted apply of `module.ldo_001`, code only), its own never-widen set | FWD-13 | WORLD | the CloudOps seat | CA-j-12 merged; halves |
| `CA-j-15` | dell2 picks up CA-j-13 through the box pass and the job writes the two files; a real read of the folder | FWD-13 | SERVED | `0.7.0_AE_CloudOps~CA2` (crossbox order) | CA-j-13 merged; CA-j-14 live |
| `CA-j-16` | FWD-13's exercise: one real Teams item and one real C-MAIL mail each reach Andrew as a muse alert within 30 minutes, one not-for-him item none | FWD-13 | SERVED | needs muse's side (scheduled read, ledger, wake): Andrew's | CA-j-15; muse's build |

`fanout (amendment 8): 2 of 2 chains, cap 8, reason: CA-j-12 writes channel_mentions.py, mail_requests.py, a new folder_records.py and their tests; CA-j-13 writes refresh.py and its test; they share only the record fields fixed in the two checks.`

## AMENDMENT 9 (2.0.0_SA_COO~CA, 2026-10-14 ~14:0xZ): the observation window reads CLEAN; the flip to enforce begins (CA-j-17 cut)

`check_j5_obs.py` at 13:50Z: 643 items scanned, 8 state rows carrying mark counters, 8 accepted marks (all in the CA-j-9 dict shape), 0 refusals, 0 `unmarked_seen`. The 8 marks sit on 8 different objects and span 13:01:23Z to 13:01:46Z, which reads as ONE multi-reply text from Andrew's phone producing eight marked `sms.reply` events (the handler's results since 11:36Z: 7 dropped, 2 answered-by-hand, 1 applied, 1 updated, 2 texted, 5 nothing-to-answer, 1 no-reply-wanted); the issuer cannot tell one text from several by content and does not read content. Neither function log shows `AccessDenied`, a traceback, an exception or a timeout since the CA-j-10 package (11:36Z). So the CVO's watch is met: a marked text was routed and handled in `record` mode with the narrowed key and the four-hour code, no secret error. The `stale-mark` question from AMENDMENT 5 is answered by the live queue and has produced no refusal. The thin spot is stated for the pair: the evidence is one burst, not three separate texts, and the pruning of `marks_seen` by age has not yet run live (the oldest mark is under 4 hours).
The flip is cut in two cells: `CA-j-17`, the Terraform edit (the variable's default `record` to `enforce`; worker-light, workstream ENFORCETF; issuer checks `check_j5_tf.py` and the bound `check_j7_tf.py`, with `check_j2_tf.py` amended to accept a default of `record` or `enforce` and still fail `off`), and `CA-j-5`, its deploy by the CloudOps seat (an environment-only change: expected `0 to add, 2 to change, 0 to destroy`, changed keys within {`environment`, `last_modified`}, `INGRESS_MARK_MODE` the only environment difference, the code hash unchanged), under its own never-widen set and `check_j5_live.py`.
SEQUENCE (a risk stated and refused): NFRA_CTLPLN also applies this module, so an `enforce` default merged into `box/laptop` early could flip the mode on another seat's apply. The issuer therefore does NOT merge CA-j-17 into the trunk until CA-j-5 has applied and closed; the halves pin the worker's commit on its own branch `wk-COMM_ASSIST-26`, and the CloudOps seat builds and plans from a detached worktree at that commit. The trunk's file stays `record` until the apply has landed, then the branch merges so the trunk matches AWS.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-17` | `chat_assist.tf`: the default of `chat_assist_ingress_mark_mode` becomes `enforce` (edit only; NOT merged to the trunk before CA-j-5 closes) | FWD-7 | WORLD (inferred floor; edit only) | workstream ENFORCETF, slot ~26 | CA-j-10 closed; the CLEAN read |
| `CA-j-5` | DEPLOY: one targeted apply of `module.ldo_001` from the pinned CA-j-17 commit (environment only), its own never-widen set (the halves read `marks_seen` against `unmarked_seen`, which is `check_j5_obs`), `check_j5_live.py`; then the issuer's real runs: Andrew's next real text read as marked and acted on, and a forged `sms.reply` of the issuer's making refused and recorded | FWD-7 | WORLD | the CloudOps seat | CA-j-17 built; halves |

`fanout (amendment 9): 1 of 1 chain, cap 8, reason: one line in one file (chat_assist.tf); it runs beside the FWD-13 workers (CA-j-12, CA-j-13), which touch no Terraform.`
