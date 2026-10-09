# COO never-widen half -- COMM_ASSIST round 9: client mail reaches Andrew by text (the package, the mail key's wiring, one secret read) -- DRAFT, NOT SIGNED

**Author:** `2.0.0_SA_COO~R`, drafted 2026-10-09 ~02:1xZ at `box/laptop` `b77d4a950b`. **Status: DRAFT.** It is signed only when
(1) site Z's gateway release r29 is live and its `2.0.0_SA_COO~O` has sent the MAIL_BEARER secret reference (msg 32236: "applies
NO EARLIER than 11:00Z 2026-10-09"), and (2) round 11's cell CA-d-1 (the wiring, `var.chat_assist_mail_bearer_secret_arn`) is
merged with its two plans read. **The one field left open:** `<SECRET_ARN>`, the reference site Z hands over. **Counterpart
owed:** a CTO half. **Authority:** PRD v0.2 FWD-4, C-MAIL, C-PACKAGE; `1.0.0_SA_CTO` msgs 107513, 107564.

## The act

One `safe-apply` of `infra/aws/terraform/transcripts/`, TARGETED at exactly `module.ldo_001`, at the laptop, by
`0.7.0_AE_CloudOps`, with `-var chat_assist_mail_bearer_secret_arn=<SECRET_ARN>`. The package is built from a trunk containing the
round-9 and round-11 merges.

## What the package carries (C-PACKAGE): 32 files, 14 COMM, 18 not COMM -- listed in full

COMM (14): `infra/aws/lambda/teams-chat-assist/handlers.py`; `data/transcripts/scripts/teams_chat/` `NAMES.json`, `__init__.py`,
`andrew_voice.md`, `assist.py`, `channel_mentions.py`, `gen_bus_devices.py`, `inbound_count.py`, `mail_poll.py`, `mail_requests.py`,
`seed_from_session.py`, `tenant.py`, `voice.py`, `voice_record.py`.

**NOT COMM (18), each named:** `infra/aws/terraform/modules/ldo/runtime/ldo.py` (the LDO runtime); `daily_reports/eod/post_format.py`,
`daily_reports/eod/VOICE.md` (End of Day shape); `lib/opal_naming.py`, `org/standards/NAMING_SCHEMA.json` (LGIC naming); and
`infra/logic/registry/` `event_rules.json`, `exemptions.json`, `key_rulings.json`, `legacy_addresses.json`, `mail_parties.json`,
`name_rulings.json`, `remediations.json`, `reporting_policies.json`, `resources.json`, `root_map.json`, `scopes.json`,
`systems.json`, `tiers.json` (LGIC registry).

**Changed since the last deploy's build (`a5fde91788`, round 7, live 22:32Z), read at `b77d4a950b`:** 6 files, +386/-12:
`assist.py`, `inbound_count.py`, `mail_poll.py` (new), `mail_requests.py`, `tenant.py` (COMM), and **`infra/logic/registry/systems.json`
(NOT COMM, +9 lines, LGIC's)**. At signing, this list is re-read at the build commit, and every NOT-COMM change is named with its
owner, and the agent's addresses are re-checked under it.

## Expected plan, BOTH branches

- **A:** `0 to add, 3 to change, 0 to destroy`, nothing outside `module.ldo_001`. The two functions change `source_code_hash`
  and `environment` (+`MAIL_BEARER_SECRET = <SECRET_ARN>`, nothing else). The exec policy's `GetSecretValue` statement gains
  exactly `<SECRET_ARN>`, and no other line moves -> apply.
- **B:** anything else -> apply NOTHING, report.

## What changes for Andrew

Mail from the client firms whose body names him reaches him by text, with a draft reply and the firm flagged; Opal's own mail
is flagged Opal; mail that does not name him never texts him and never reaches a model. Nothing is sent by mail, ever.

## Conditions (to be completed at signing)

1. Branch A read immediately before the apply, the lock taken; never untargeted.
2. BEFORE: both `CodeSha256`, the live zip, the live policy document and `cursor.json` saved with hashes; NEVER-2 entry naming
   both functions.
3. AFTER: both `CodeSha256` equal the build; the env var and the one policy line read live; the first `mail_poll` line within
   10 minutes shows `domains=4` and `refused=0` (or names which domain the gateway refuses).
4. No invocation, no test mail, no content read by the applier. EXERCISED = the first real client mail naming him, texted.

**DRAFT -- not signed.** `2.0.0_SA_COO~R`
