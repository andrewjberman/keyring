# COO never-widen half -- NFRA_CTLPLN workstream INBOUND (macro COMM), round 6: the Teams agent's code-only deploy (one targeted apply of `module.ldo_001`)

**Author:** `2.0.0_SA_COO~R`, 2026-10-08 ~21:3xZ. **Read at:** `box/laptop` `79d7b6cbbe` (carries round 6's last merge `b3afc00597`
and the hookups `fff0bc0a11`). Root `infra/aws/terraform/transcripts/`. **Counterpart owed:** the CTO half for this act.
**Authority:** `1.0.0_SA_CTO` msg 107329 ruling (1): "a never-widen pair is owed for the ldo_001 code-only deploy (it changes what
texts Andrew); sign your half and send it ... apply via 0.7.0_AE_CloudOps outside the End of Day window". The outcome is FWD-20
(PRD v0.20); the work is items 1-4 of `1.0.0_SA_CTO` msg 107165 on Andrew's point 1 of 2026-10-08 ~18:4xZ ("I feel like I am not
getting all the team's messages").

## The act

One `safe-apply` of the root TARGETED at exactly `module.ldo_001`, at the laptop, by `0.7.0_AE_CloudOps`, after building the
package from a trunk that contains `79d7b6cbbe`. Code only: NO policy line changes in this act.

## What becomes live -- the packaged-path diff since the last deploy's base `ebc8931b3c` (deployed 08:15Z), read at `79d7b6cbbe`

`git diff --stat ebc8931b3c HEAD` over every path `build.sh` packages: 10 files, +831/-41. No file under
`infra/aws/terraform/transcripts` changed.

| file | from | what it changes live |
|---|---|---|
| `teams_chat/tenant.py` | round 6 CT-i-9 + hookups | the minute poll keeps a cursor per chat and pages all chats and messages (v1 cursor migrated, nothing older than it minus 15 minutes replayed); a `channels` step; the `teams.channel_mention` route; the `tenant` log line carries the object hash |
| `teams_chat/channel_mentions.py` (new) | CT-i-12 | channel posts and replies that @mention Andrew -> ONE text each ("@ team / channel - sender: first 300 characters", "Reply in Teams."); paused when he is `#off`; first run sends nothing |
| `teams_chat/assist.py` | CT-i-12 | three gateway read methods |
| `teams_chat/inbound_count.py` (new) | CT-i-10 | packaged with the folder; nothing in the functions calls it |
| `teams_chat/voice.py`, `voice_record.py` (new) | round 5 CT-i-7 | the harvest tool's spread choice and the recorder; packaged with the folder (read by the issuer: the draft path's use of `voice.py` is unchanged in behaviour unless an examples object is read, which exists since 2026-10-08 ~10:4xZ) |
| `infra/aws/lambda/teams-chat-assist/build.sh` | round 5 CT-i-8 | text files written LF inside the package: the hash no longer depends on the working tree's line endings |
| `infra/logic/registry/key_rulings.json`, `reporting_policies.json`, `root_map.json` | LGIC (not this workstream) | registry data the naming library reads; the agent's addresses MEASURED unchanged (below) |

**The agent's addresses, measured:** at `79d7b6cbbe` the code builds bucket `opal-data-transcripts`, bronze
`teams/transcripts/bronze/chat_messages/chat=<key>/...`, silver `teams/transcripts/silver/chat_threads/chat=<key>/context.md`, state
`teams/transcripts/state/chat_assist/global/...`; the real count run of ~21:1xZ listed today's live bronze objects under exactly
that prefix (31 received in 3 chats). Not every path of the naming library was read.

**What depends on another box and is NOT in this act:** the gateway's three channel routes ship with NFRA_OPLGTW's release
(ruling (2) of msg 107329). Until then the new `channels` step fails once a minute (`ingress_step_failed`, caught; the chat poll
and the End of Day step run as before): accepted by that ruling.

## Expected plan, BOTH branches

- **A:** targeted plan `0 to add, 2 to change, 0 to destroy`: `module.ldo_001.aws_lambda_function.handler` and
  `module.ldo_001.aws_lambda_function.ingress[0]`, each changing ONLY `source_code_hash` (and `last_modified`, known after apply),
  the new hash decoding to the SHA-256 of the package the applier built; 0 addresses outside the module; NO change to
  `aws_iam_policy.exec` -> apply.
- **B:** any policy change; any add, destroy or replacement; any other function argument (role, handler, memory, timeout,
  environment, layers); any address outside the module; an `init` that asks to migrate or reconfigure; a packaged-path diff
  since `79d7b6cbbe` that touches `teams_chat/`, `ldo.py`, `handlers.py` or `daily_reports/eod/` (a change this half did not
  read); the apply time inside the End of Day window 20:00Z-21:45Z; or an End of Day event still in flight on
  `teams-global-chat-assist-queue.fifo` (row S33: read `ApproximateNumberOfMessagesNotVisible` and the handler log for
  `eod.` lines in the last hour) -> apply NOTHING and report.

## Blast radius

Two functions (one package): `teams-global-chat-assist-handler-lambda`, `teams-global-chat-assist-ingress-lambda`. What changes
for Andrew: texts for chat messages a late Graph preview or a page past 50 would have dropped; a new kind of text for a channel
@mention once the gateway serves channels. No new vendor, no new model call (the mention text is built without a model), no
send to Teams, no mail, no schedule, no alarm. State writes stay under the declared `chat_assist/` prefix (`cursor.json` v2,
`channels.json`, `channel_cursors.json`; writer declaration `f3170c6f94`). **Served output:** texts to Andrew only.

## Rollback

Code, exactly: before the apply, download the LIVE package with `lambda get-function` and confirm its SHA-256 equals both
functions' live `CodeSha256` (the 08:15Z deploy's `YYWO/dxPxySPpaAPmr+FhxZtQBnkChJ4SGGntvvvMr4=`, unless it moved since); the
rollback copies that zip over `dist/teams-chat-assist.zip` and runs the same targeted apply. The state: the v2 `cursor.json`
is read by the old code as a v1 cursor with no `since` -> a first run (delivers nothing for one minute, then resumes); save the
live `cursor.json` before the apply so a rollback can restore it. A text already sent is not recalled.

## Conditions

1. The targeted plan of branch A, read immediately before the apply with the state lock taken. NEVER an untargeted apply
   under this half.
2. BEFORE: both functions' `CodeSha256` and `LastModified`, the live package zip and the live `cursor.json` saved with hashes;
   a NEVER-2 ledger entry opened before and closed after, naming both functions as the families that take the package.
3. AFTER, read live: both `CodeSha256` equal the built package's; a targeted re-plan reads no changes; within 5 minutes the
   ingress log shows `ingress_poll` with the new fields `chats_read`, `pages`, `messages` and no `ingress_step_failed` for step
   `chats` (one for `channels` is expected until the gateway ships).
4. The applier invokes neither function, sends no test event or text, and reads no message content. The exercised reads are
   the issuer's: the count reader on the first full day after the deploy (positive arm), and one real @mention once the
   gateway carries the routes. Until then the deploy is APPLIED, not EXERCISED.

**SIGNED** -- `2.0.0_SA_COO~R`
