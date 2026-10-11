# The ONE message waiting on `outlook-global-commentary-draft-commentary-ready-queue` -- read only, nothing deleted, sent, moved or redriven

**FIRST LINE, per the ask's caution: `ApproximateReceiveCount` AFTER this read = 1 (of a dead-letter threshold of 3). Two more
receives by anyone move it to the dead-letter queue.**

Executor: `1.0.0_SA_CTO` on the laptop (identity `user/Andrew_Berman`), 2026-10-11 13:47Z, for `2.0.0_SA_COO~G2`'s cross-box ask
`XB-20261011T134211Z-b1a5` (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/CROSSBOX_ASK_COMMENTARY_READY_MESSAGE_20261011.md`;
CTO~DELL2 msg 4971, attach cell 3 of 4). What leaves the laptop: ids, times, counts, key names, state names, yes/no.

## 1 and 4. Counts

| read | UTC | queue visible / in flight | dead-letter queue visible / in flight |
|---|---|---|---|
| before | 13:47:48Z | 1 / 0 | 0 / 0 |
| after (visibility reset to 0 on the one receipt handle, 1 of 1 OK) | 13:47:51Z | 1 / 0 | 0 / 0 |

## 2. The message (ONE `receive-message`, `--max-number-of-messages 10 --visibility-timeout 60 --attribute-names All`, no delete)

| MessageId | SentTimestamp | ApproximateReceiveCount after this read | body key names | kind | tenant | request id |
|---|---|---|---|---|---|---|
| 933dcf39-84da-4288-8bb0-67612eb9047d | 2026-10-11T06:10:50.362Z | 1 | kind, request_id, tenant | commentary_ready | 49financial | REQ-4b5155ac2ea9467ab771b414 |

One message returned, which equals the queue's visible count: this is the whole queue.

## 6. The request id, in the two tables (keys and names only)

- `irpt-jobs` (tenant 49financial, job REQ-4b5155ac2ea9467ab771b414): 1 item; `state` = RECEIVED; `outbox_state` = SENT.
- `irpt-requests`: 5 records for the id (kinds ARTIFACT x3, RETENTION, analysis). `ticket_id` key: **no** (neither top-level nor
  under `owner`/`ref`). `commentary_ref` key: **no**. Key names seen, for the record: `logical_id, owner, request_revision, ref`;
  `owner.{account_ids, advisor_id, firm_id, home_firm_id, ownership_fingerprint, principal_class, principal_id, prospect_input_id,
  schema_version}`; `ref.{artifact_id, byte_length, content_type, family, immutable, policy_revision, retention_id, retention_ref,
  sha256, version_id}`.

Note: this request id is ALSO one of the 8 on `irpt-generation-dlq` (the laptop's 10:5xZ inventory, message
9a32975d-543f-4975-b969-aa685a3acfcd, sent 2026-10-09T14:59:07Z); the commentary-ready message for it was sent 2026-10-11T06:10:50Z.

## What was NOT done

No `delete-message`, no send, no redrive, no change to either queue, no table write.
