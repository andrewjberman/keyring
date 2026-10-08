# COO never-widen half -- NFRA_CTLPLN workstream INBOUND (macro COMM), round 7: the Teams agent never goes silent (code-only deploy, one targeted apply of `module.ldo_001`)

**Author:** `2.0.0_SA_COO~R`, 2026-10-08 ~22:2xZ. **Read at:** `box/laptop` `75420934c2` (round 7's merge of cell CT-i-13).
Root `infra/aws/terraform/transcripts/`. **Counterpart owed:** a CTO half. **Authority:** `1.0.0_SA_CTO` msg 107329 ruling (3)
(round 7, S33 first) and the round-6 pair's shape (msg 107329 ruling (1): a code deploy that changes what texts Andrew owes a
pair); Andrew-direct ~18:4xZ ("a lot of them are falling through") and ~21:4xZ (the Kimi token budget, recorded verbatim in
`159dad0a43`).

## The act

One `safe-apply` of the root TARGETED at exactly `module.ldo_001`, at the laptop, by `0.7.0_AE_CloudOps`, from a trunk that
contains `75420934c2`. Code only. Previous deploy: TO-APPLY-19, live 21:48Z 2026-10-08, built at `6f7449dbc5`, live
`CodeSha256` `M67/KipojF79vIGJTxCmQnDQfVyzws1VGU4OsD+7Yt0=` (read by the issuer).

## What becomes live -- the packaged-path diff `6f7449dbc5..75420934c2`: 3 files, +108/-11; no file under the root changed

| file | what it changes live |
|---|---|
| `tenant.py` | **S34:** a chat draft's text and its approved send run under keys unique per draft (`offer:<tag>:<seq>:v<n>`, `send:...`); a pending draft made before the deploy keeps its old key (no re-text of a draft he already has); a legacy pending that he asks to redraft takes a new number (cost: a retry of a redraft that texted before the deploy could text once more). **S33:** `_eod_draft` no longer raises: a draft missing only its link line gets `[Opal Daily Operating Report](https://mcp.opalinvest.dev/sprint)` put first (the form VOICE.md asks for); any other refusal texts him one line with the problems (never the draft) and keeps the open draft; an approved post's alarm is cancelled only after a new draft is accepted. **Pruning:** a chat cursor older than the floor minus 7 days is dropped; such a chat's new message is still delivered |
| `mail_requests.py` | the mail item's text key unique per draft (no mail event is produced today: the gateway does not serve the mail read) |
| `assist.py` | **AMENDMENT 1:** a model answer cut off by its token limit is retried with double the budget (cap 16000, was the same 8000); one `kimi_attempt` log line per attempt (attempt, budget, outcome, completion tokens; never text). Two attempts at 240 s fit the handler's 600 s |

Audit by the worker, key by key: 12 `ctx.once` sites; 3 fixed (above); 9 unaffected (End of Day per-day tags, per-job objects,
per-message ids). Evidence on the trunk, the issuer's own runs: `SILENT-PATHS ok=True arms=9/9 base_texts_second_draft=1` (the
base sends ONE text where the new code sends two); `AGENT-SUITE ok=True` (127 pytest + 9/9 mail reply); the seven other
inbound scripts green; `ruff` and `py_compile` clean. Every model call and send in them is faked.

## What changes for Andrew

He gets the texts that were being dropped: every later draft in a chat inside a week (14 such outcomes on 2026-10-08 with no
text sent), and every approved reply posts. A refused End of Day draft says why instead of going silent. Volume: at most the
texts the agent already decided to send. No new vendor, no new kind of content to the model, no send to Teams without his 1,
no mail, no schedule, no alarm.

## Expected plan, BOTH branches

- **A:** targeted `0 to add, 2 to change, 0 to destroy`: `module.ldo_001.aws_lambda_function.handler` and `.ingress[0]`,
  `source_code_hash` (and `last_modified`) only, decoding to the built package; 0 outside the module; no policy change -> apply.
- **B:** anything else (an add, destroy, replacement, other argument, policy line or address outside the module; an `init`
  migration prompt); a packaged-path diff since `75420934c2` under `teams_chat/`, `ldo.py`, `handlers.py` or
  `daily_reports/eod/`; inside the End of Day window 20:00Z-21:45Z; or an End of Day event in flight -> apply NOTHING, report.

## Rollback

Code: the live package downloaded before the act (its hash equal to `M67/Kipo...` unless it moved), copied over
`dist/teams-chat-assist.zip`, the same targeted apply. State: no migration in this act (`draft_seq` is created on first use; the
v2 cursor is unchanged in shape); the live `cursor.json` is saved anyway. A text already sent is not recalled.

## Conditions

1. Branch A read immediately before the apply, the lock taken. Never untargeted.
2. BEFORE: both `CodeSha256`/`LastModified`, the live zip and the live `cursor.json` saved with hashes; a NEVER-2 entry opened
   and closed, naming both functions.
3. AFTER, live: both `CodeSha256` equal the built package's; a targeted re-plan reads no changes; within 5 minutes
   `ingress_poll` lines continue with no `ingress_step_failed` for step `chats`.
4. No invocation, no test event or text, no message content read by the applier. The exercise is the issuer's: the count
   reader the first full day after, where `sms_sent` reconciles with chat `texted` + `updated`; until then APPLIED, not
   EXERCISED.

**SIGNED** -- `2.0.0_SA_COO~R`
