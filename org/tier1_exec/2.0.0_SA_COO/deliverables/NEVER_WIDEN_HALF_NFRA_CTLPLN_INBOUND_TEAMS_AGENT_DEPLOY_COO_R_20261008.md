# COO never-widen half -- NFRA_CTLPLN workstream INBOUND: deploy the Teams agent's function with the inbound work, and let its role send to the two Dell bus queues (one targeted apply of one module)

**Author:** `2.0.0_SA_COO~R`, 2026-10-08 ~05:3xZ. **Read at:** trunk `ebc8931b3c` (the merge of cell CT-i-6). Root
`infra/aws/terraform/transcripts/`. **Counterpart owed:** a CTO half for this same act. **Authority:** `1.0.0_SA_CTO` msg 106725
("that deploy needs its never-widen pair like any other; send me the half request"); the outcome is FWD-20 of PRD v0.20, on
Andrew's words of 2026-10-07 ~16:3xZ and ~21:4xZ as recorded
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_163xZ_FABRIC_ROLES_MSTR_CTO_COO_CVO_CRO_AND_THE_INBOUND_WORK_PIPELINE_INTO_NFRA_CTLPLN.md`,
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_214xZ_COO_R_INBOUND_FOR_BOTH_TEAMS_AND_OUTLOOK_AND_AN_ANDREW_VOICE_MD.md`).

## The act

One `safe-apply` of the root TARGETED at exactly `module.ldo_001`, at the laptop, by `0.7.0_AE_CloudOps~E`, after both function
packages are built from the trunk commit the order names.

## The plan, MEASURED -- and why it must be targeted

By cell CT-i-6 (worker `0.9.0_WK_NFRA_CTLPLN~34`, 2026-10-08 ~04:5xZ, read-only, scratch data directory, no lock); the plan
texts are `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~34/PLAN_TARGETED_module_ldo_001.txt` and
`PLAN_UNTARGETED.txt`. The issuer re-ran the cell's reader on the saved targeted plan: `CHAT-ASSIST-PLAN ok=True add=0 change=3
destroy=0 outside_module=0`.

Targeted: `Plan: 0 to add, 3 to change, 0 to destroy.`

| address | change, as read |
|---|---|
| `module.ldo_001.aws_iam_policy.exec` | in place: TWO statements added, `TellDell1OnTheBus` and `TellDell2OnTheBus`, each Allow, actions exactly `sqs:GetQueueUrl` and `sqs:SendMessage`, Resource the one queue `agentbus-global-dell1-queue.fifo` / `agentbus-global-dell2-queue.fifo`; no line removed |
| `module.ldo_001.aws_lambda_function.handler` | in place: `source_code_hash` only |
| `module.ldo_001.aws_lambda_function.ingress[0]` | in place: `source_code_hash` only |

The new package: SHA-256 `c1af3fe33556e895ec97cbf0ad6bd1915596f4daee5c259d1fca55a697d1da32`, 28 files, built by
`infra/aws/lambda/teams-chat-assist/build.sh`; the plan's new hash decodes to it.

**UNTARGETED, the same root reads `9 to add, 4 to change, 0 to destroy`:** another project's unapplied pull function (rule,
target, log group, policy, role, attachment, key grant, function, permission: nine creates) and `aws_lambda_function.mail_pull`
(a code hash). None of that is this workstream's, none is covered here, and an untargeted apply would land all of it.

**A fact about planning this root, measured (row NFRA_CTLPLN-W34-S1):** the configuration does not load until BOTH packages
exist on disk, because `pull.tf` and `mail_pull.tf` hash `transcripts-pull/dist/transcripts-pull.zip`. The applier builds both
before any plan; building the second uploads nothing and the target excludes its resources. `init` with a scratch data
directory configured the declared S3 backend with no migration prompt.

**Writers of the two properties, read. N is printed.**
- What the agent's role may do: N = 1 managed policy (`module.ldo_001.aws_iam_policy.exec`, this act changes it) plus the KMS
  grant the root declares for that role (unchanged). LIVE inline policies on the role were not listed.
- What code the two functions run: N = 1 package feeding 2 functions. No other writer of the package is declared in the root;
  a hand upload to either function was not looked for.

## Blast radius

**The access change (the widening).** One role, `teams-global-chat-assist-role`, gains send on two named queues, the inbound
bus queues of dell1 and dell2. It could already send to the laptop's and site Z's. What the agent sends there is what it
sends today: a job's offer, award, lost and close lines with the job's brief. So after this act a remote job's brief (drawn
from a Teams conversation, or from a mail that passed clause 9) can reach a Dell box's manager seat. It gains no receive, no
delete, no queue administration, and no other queue.

**The function change.** Both functions of LDO-001 run a new package. What becomes live, by cell:
- the one text Andrew already gets for an unanswered chat message gains, WHEN the model reads the message as a request for
  work, `WORK REQUESTED by`, a recommendation and the `#dev` line; otherwise it is byte-identical (CT-i-1, tested);
- ONE more model call per waiting chat message, to the same vendor, of the same content the reply draft already sends; no
  new kind of content leaves, and a failed call falls back to today's text;
- a job is offered to four boxes; a completion with no passing reviewer grade is refused and he is texted one line;
- a handler for mail events, a reply path for a mail item's tag, and the voice file's lines in two draft prompts. NO mail
  event is produced by anything in this deploy: nothing polls mail and the gateway's route does not serve the read (row
  W31-S6). The voice file's examples object does not exist yet, so drafts get the file's plain lines only.
- **Also in the package and NOT this workstream's:** `lib/opal_naming.py`, `org/standards/NAMING_SCHEMA.json` and every
  `infra/logic/registry/*.json` as they are on the trunk today, all changed since the last deploy (2026-10-04 23:04Z). Read by
  the issuer: the addresses the agent builds (its bucket, a state key, a silver key, a bronze key) and its resource names
  are IDENTICAL under the tree of the last deployed commit `55cb79f93c` and under today's. That is four addresses and the
  names table, not every code path of the naming library.

**What nothing in this act does:** it sends nothing to Teams without his 1, opens no job without his `#dev`, sends no mail,
adds no schedule, alarm or notification, and touches no resource outside `module.ldo_001`.

**Served output:** the texts to Andrew and, on his 1, messages to Teams. No file a portal or a client reads.

## Evidence, the issuer's own runs on the trunk

`INBOUND-CLOUD-TEST ok=True cases=9/9`; `INBOUND-MAIL-TEST ok=True cases=15/15 model_calls_on_failed=0`;
`INBOUND-VOICE-TEST ok=True cases=14/14`; `INBOUND-MAIL-REPLY-TEST ok=True cases=9/9`; `INBOUND-SEAM-TEST ok=True cases=8/8`
(the real box tool's envelopes through the real handlers); the seven existing Teams and End of Day files, `127 passed`;
`CHAT-ASSIST-BUS ok=True boxes=4 statements=4 matched=4 extra=0`. **What that evidence is not:** every model call and every
send in those tests is faked. No deployed function was invoked.

## Expected outcome, BOTH branches

- **A:** the applier's targeted plan reads exactly `0 to add, 3 to change, 0 to destroy`, the three addresses above; the
  policy diff is exactly the two statements, no line removed; each function's only changed argument is `source_code_hash`
  (with `last_modified` known after apply) and the new hash decodes to the SHA-256 of the package the applier built; that
  SHA-256 is recorded, and where it differs from `c1af3fe3...` the applier names the trunk files that changed since
  `ebc8931b3c` under the packaged paths -> apply.
- **B:** any address outside `module.ldo_001`; any add, destroy or replacement; any other argument of a function changing
  (role, handler, timeout, environment, layers); any removed policy line or any action, queue or Sid other than the two; an
  `init` that asks to migrate or reconfigure; a job in state `bidding` on the live agent at apply time that the applier can
  see; or the End of Day window (20:00Z to 21:45Z, the hour the day's post is drafted and sent) -> apply NOTHING and report.

## Rollback

Per property. The policy: revert the two statements (the edit of commit `9734652dbe` to `chat_assist.tf`) and the same
targeted apply; the saved prior policy document is the reference. The code: check out the packaged paths at the last deployed
commit `55cb79f93c`, rebuild, and the same targeted apply; the prior hash `IBrveNQC+Zbry9pHjbJ7C1Ww6EZb95XRXaFrziNSn6E=` is the
reference a rebuilt package must reproduce before it is applied. A text already sent to Andrew is not recalled.

## Conditions

1. The targeted plan shape of branch A, read immediately before the apply, with the state lock taken. NEVER an untargeted
   apply of this root under this half.
2. BEFORE: the live policy document of `module.ldo_001.aws_iam_policy.exec` and each function's `CodeSha256` and
   `LastModified` saved with hashes (the rollback references); a NEVER-2 ledger entry opened before the act and closed after,
   naming both functions as the families that take the package.
3. `python infra/aws/terraform/transcripts/tests/check_chat_assist_bus.py` reads `ok=True boxes=4 statements=4 matched=4
   extra=0`, and `python data/transcripts/scripts/teams_chat/gen_bus_devices.py --check` reads `BUS-DEVICES ok=True`,
   immediately before the build.
4. The box half is on the laptop's trunk already (2660df145d). Site Z and the Dells take it at their next pull; until a box
   has it, that box's completion is refused by the cloud and he is texted the refusing line. The applier states, from the
   fabric manager's record or by asking `0.0.0_AB_MSTR` once, which boxes have pulled past `2660df145d`; a box that has not is
   named in the report, and the apply does not wait on it.
5. Read-back LIVE: both functions' `CodeSha256` equal the built package's; the live policy equals the saved one plus exactly
   the two statements (parsed, with a planted-mutant control); a targeted re-plan reads no changes; an untargeted plan
   (read-only) still reads `9 to add` and now `1 to change`: its counts are reported and none of it applied.
6. The applier invokes neither function, sends no test event, no text and no bus line, and reads no chat or mail content.
   The exercised read is FWD-20's own: one real request from a person in Teams. Until it runs the deploy is APPLIED, not
   EXERCISED, and the report says so in those words.

**SIGNED** -- `2.0.0_SA_COO~R`
