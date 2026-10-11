# Dead-letter inventory of `irpt-generation-dlq` -- read only, nothing deleted, sent, moved or redriven

Executor: `1.0.0_SA_CTO` on the laptop (identity `user/Andrew_Berman`; `sqs:ReceiveMessage`, `sqs:ChangeMessageVisibility`,
`kms:Decrypt` on key `7f4d3042-...` simulated allowed), 2026-10-11 10:54-10:58Z, for `2.0.0_SA_COO~G2`'s cross-box ask
`XB-20261011T104936Z-073c` (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/CROSSBOX_ASK_DEAD_LETTER_INVENTORY_20261011.md`).
Row it sizes: `IRPT_YCDGEN-D2-S45`. What leaves the laptop: ids, times, counts, state names. No message body beyond tenant, request
id and kind; no owner or ref VALUES (their key NAMES only, where the ask needed a presence answer).

## 1 and 4. Queue counts

| read | UTC | visible | in flight |
|---|---|---|---|
| before | 10:54:37Z | 8 | 0 |
| after (visibility reset on all 8 receipt handles, 8 of 8 OK) | 10:55:20Z | 8 | 0 |

## 2. The eight messages (4 receives, `--max-number-of-messages 10 --visibility-timeout 120`, no delete)

Every body: keys `composition_sha256, kind, request_id, revision, tenant`; `kind` = `analysis_generate` on all 8; `ApproximateReceiveCount` = 6 on all 8.

| # | MessageId | SentTimestamp | FirstReceive | tenant | request id |
|---|---|---|---|---|---|
| 1 | aab34d30-9e32-4c77-ba3a-533b56f66d4b | 2026-10-07T18:07:49.952Z | 2026-10-07T18:07:49.953Z | cottonwood | REQ-ef7b39c548d08cbb4822f7cc |
| 2 | 1a6335d0-d94f-4958-9132-378a50a8737a | 2026-10-08T21:10:30.654Z | 2026-10-08T21:10:30.661Z | cottonwood | REQ-8966d24ffefa1c28269ef26c |
| 3 | d4a3abad-1f8f-456c-a929-f8957260dc7f | 2026-10-09T09:13:26.968Z | 2026-10-09T09:13:26.975Z | 49financial | REQ-1f8b4cc4682f2d929cc70215 |
| 4 | cc33f6c7-1069-4020-8b43-74d13ca85d08 | 2026-10-09T09:51:25.927Z | 2026-10-09T09:51:25.929Z | 49financial | REQ-3d76e5b49dae4f91db1694b0 |
| 5 | bd3e766b-c393-4649-ba47-247611528718 | 2026-10-09T09:51:30.722Z | 2026-10-09T09:51:31.509Z | 49financial | REQ-9d59d4d2334f841152914569 |
| 6 | 479d196d-f045-48b2-9d07-91fb99ff9596 | 2026-10-09T09:53:51.110Z | 2026-10-09T09:53:51.112Z | 49financial | REQ-f7ddede91f98562412314b6e |
| 7 | 13b9fecc-9373-4918-97cf-5b8abf0ae24d | 2026-10-09T10:37:05.620Z | 2026-10-09T10:37:05.628Z | 49financial | REQ-448d42480cadd873fa74c3cf |
| 8 | 9a32975d-543f-4975-b969-aa685a3acfcd | 2026-10-09T14:59:07.760Z | 2026-10-09T14:59:07.768Z | 49financial | REQ-4b5155ac2ea9467ab771b414 |

## 5. Per request id (denominator 8), from `irpt-jobs` (key tenant + job) and `irpt-requests` (key tenant + request_revision)

`irpt-jobs` attribute names: `composition_sha256, fence_token, job, outbox_state, request_revision, state, tenant`. There is NO
reason field of any name on a job record, so "reason token" reads ABSENT for all 8. `irpt-requests` is a content-addressed
store (`request_revision` = `ARTIFACT#ART-...` / `RETENTION#RET-...` / `analysis#...`; attributes `blob, logical_id, owner, ref`);
it carries NO accepted-time field, so "the accepted time" is not readable from either table. A request's records are found by
`logical_id` (`<request id>` or `<request id>-<suffix>`), scan of 1,894 items.

| request id | tenant | job state | outbox_state | reason token | request records (kinds) | ticket_id key anywhere |
|---|---|---|---|---|---|---|
| REQ-ef7b39c548d08cbb4822f7cc | cottonwood | RECEIVED | SENT | ABSENT | 3 (ARTIFACT, RETENTION, analysis) | no |
| REQ-8966d24ffefa1c28269ef26c | cottonwood | RECEIVED | SENT | ABSENT | 3 (ARTIFACT, RETENTION, analysis) | no |
| REQ-1f8b4cc4682f2d929cc70215 | 49financial | RECEIVED | SENT | ABSENT | 3 (ARTIFACT, RETENTION, analysis) | no |
| REQ-3d76e5b49dae4f91db1694b0 | 49financial | RECEIVED | SENT | ABSENT | 3 (ARTIFACT, RETENTION, analysis) | no |
| REQ-9d59d4d2334f841152914569 | 49financial | RECEIVED | SENT | ABSENT | 3 (ARTIFACT, RETENTION, analysis) | no |
| REQ-f7ddede91f98562412314b6e | 49financial | RECEIVED | SENT | ABSENT | 3 (ARTIFACT, RETENTION, analysis) | no |
| REQ-448d42480cadd873fa74c3cf | 49financial | RECEIVED | SENT | ABSENT | 3 (ARTIFACT, RETENTION, analysis) | no |
| REQ-4b5155ac2ea9467ab771b414 | 49financial | RECEIVED | SENT | ABSENT | 5 (ARTIFACT x3, RETENTION, analysis) | no |

Key-name census (names only): `owner` carries `account_ids, advisor_id, firm_id, home_firm_id, ownership_fingerprint,
principal_class, principal_id, prospect_input_id, schema_version`; `ref` carries `artifact_id, byte_length, content_type, family,
immutable, policy_revision, retention_id, retention_ref, sha256, version_id`. `ticket_id` / `ticketId` appears under neither, nor
as a top-level attribute, for any of the 8.

## 6. TCKT_VNEXT run 3's request (49financial, accepted ~2026-10-11T08:14Z)

Not identifiable from the two tables: neither carries a time field, and the ask's ruling file names no `REQ-` id for run 3. What
IS measured: every one of the 8 dead letters was sent 2026-10-07 to 2026-10-09 (table above), so a request accepted
2026-10-11T08:14Z is NOT one of the 8. When dell2 names the id, its job state and outbox_state are one `irpt-jobs` query away.

## What was NOT done

No `delete-message`, no `send-message`, no redrive, no `start-message-move-task`, no write to either table. The queue read 8/0
before and 8/0 after.
