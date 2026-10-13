# TO COMM_ASSIST.TO-CA-i-3 -- round 17 CA-i-3: the dell2 forwarder that moves a muse answer file onto the assistant's mailbox, once (FWD-7, FWD-8)

<to_id>COMM_ASSIST.TO-CA-i-3</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~11</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-3` (`decompositions/COMM_ASSIST_DECOMP.round17.md`) | **outcome_ref:** FWD-7, FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew will answer a waiting draft from muse, an agent on his tailnet that has no AWS access, by writing a signed ANSWER FILE into a folder on dell2
(`<reader folder>/answers/`; the folder `data/transcripts/scripts/muse_reader/refresh.py` already fills with four JSON files). A small job on dell2
forwards each answer file onto the assistant's mailbox (an SQS FIFO queue) as an event. You build that job: `forwarder.py`. It does NOT check
signatures: the assistant (the receiver) does that, because anything that can write to the queue can skip an upstream check. Your job is shape,
tag, once-only, and a clean local record of what it did.

### THE CONTRACT (fixed by the issuer; the receiver cell and the checks pin their halves)

- An ANSWER FILE is one JSON object `{"payload": "<json text>", "signature": "<armored SSH signature text>"}`. `payload` parses as JSON with at least
  `tag`, `action`, `version`. The file's bytes are never modified, moved or deleted by you.
- `<reader folder>/drafts.json` (written by the refresh) has `items`, a list of rows; each row has `tag` and `object_id` (the refresh cell adds `object_id`
  this round; read `drafts.json` defensively, a row without `object_id` is "tag not waiting" for you).
- The EVENT: object id = the row's `object_id`; kind `muse.reply`; payload `{"answer": {"payload": <file payload>, "signature": <file signature>}}`;
  event id = `"muse-" + sha256 hex of the answer file's bytes`.

### BUILD, IN THIS ORDER

1. `data/transcripts/scripts/muse_reader/forwarder.py`, standard library only. It exposes `forward(root, send, now)`: `root` the reader folder; `send(object_id,
   kind, payload, event_id)` a callable that raises on failure; `now` a UTC time string like `2026-10-13T22:30:00Z`. For every `*.json` directly under
   `root/answers/` (sorted by name):
   - compute the sha256 of the bytes. If `answers/done/<sha>.json` or `answers/rejected/<sha>.json` exists, skip it (so the same bytes under any file name act once).
   - not JSON, or no string `payload`, or no string `signature`, or `payload` not JSON with a string `tag`: write `answers/rejected/<sha>.json`
     `{"at", "file", "reason": "malformed"}`; send nothing.
   - the tag has no row in `root/drafts.json` with a non-empty `object_id`: write `answers/rejected/<sha>.json` with `reason` `tag-not-waiting` and the tag; send nothing.
   - otherwise call `send(...)`. On success write `answers/done/<sha>.json` `{"at", "file", "tag", "event_id"}`. If `send` raises, write NO marker (the next run retries it)
     and carry on with the other files: one bad send never stops the rest.
   - create `answers/done/` and `answers/rejected/` when missing. Write every marker by temp-file-then-rename.
2. The command line: `python data/transcripts/scripts/muse_reader/forwarder.py --root <folder>` builds the real sender and calls `forward`, prints one line
   `MUSE-FORWARD sent=<n> rejected=<n> failed=<n>` and exits 0 whatever the per-file outcomes (a crash exits non-zero).
   - Queue address ONLY from the environment: `MUSE_MAILBOX_URL`. If it is unset, print `ERROR: MUSE_MAILBOX_URL is not set` and exit 2 before touching any file. Type no
     URL, ARN, account number or queue name anywhere in the file. The assistant's id comes from `MUSE_LDO_ID`.
   - AWS only through the AWS CLI by subprocess, executable name from `MUSE_AWS_BIN` (default `aws`; CA-h-1's report found `shutil.which("aws")` is the form that works from Python on
     Windows): `aws sqs send-message --queue-url <url> --message-body <json> --message-group-id <id> --message-deduplication-id <id>`. Pass the JSON body as
     `file://<temp file>` (not inline: the Windows shell mangles quotes). The body is the SAME envelope `ldo.send` builds: read
     `infra/aws/terraform/modules/ldo/runtime/ldo.py` lines 122-136 (`envelope`, `group_id`, `dedup_id`) and IMPORT those helpers or call the same functions; do not copy their logic.
     The only AWS call is `sqs send-message`.
3. Nothing else: no signature check, no read of any key, no DynamoDB, no S3, no alert or notification. No non-ASCII. Bake no absolute path.

### RULES FOR THIS CELL

- Edit nothing but the files in `<paths>`. You do not install, schedule or deploy anything: that is a later cell, run on dell2 by its own seat.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi3-AC1" cell_refs="CA-i-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i3_forward.py"</invocation><expect>I3-FORWARD ok=True arms=6 of 6</expect></criterion>
`CAi3-AC1` -- the issuer's check (read it; do not edit it): a valid file is sent once with the right object id, kind and `muse-` event id and leaves a done marker; the same file twice, and the same bytes under a new name, act once; a malformed file and an unknown-tag file are rejected locally and send nothing; a failed send leaves no marker, does not stop the next file, and retries on the next run. It prints ok=False at the base.

<criterion id="CAi3-AC2" cell_refs="CA-i-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i3_cli.py"</invocation><expect>I3-CLI ok=True calls=1</expect></criterion>
`CAi3-AC2` -- the seam against the AWS CLI (replaced by a stub that records its argv): the command makes exactly one `sqs send-message` with the queue URL from `MUSE_MAILBOX_URL`, a message group id, a deduplication id and a `muse.reply` envelope for the draft's object id; with the variable unset it exits non-zero, names the variable and makes no call. It prints ok=False at the base.
</proof_of_spec>

<expected_criteria>CAi3-AC1,CAi3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~11/COMM_ASSIST.TO-CA-i-3.dell2-forwarder-for-muse-answers.proof_of_spec.json`,
validate it by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree:
`python .tools/proof-of-spec-check.py <instance> CAi3-AC1,CAi3-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID. Your final
report names: the AWS launch form, which `ldo.py` helpers you imported, the environment variables the job reads, and anything the install on dell2 will need
(the install is a later cell). Your surprise rows are `COMM_ASSIST-W11-S<k>`; append only to the investigation file and keep its existing line endings;
`surfaced_at` = `date -u +%FT%TZ` at filing.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-3</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/muse_reader/forwarder.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-3.dell2-forwarder-for-muse-answers.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~11/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the dell2 task is cell CA-i-5.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made here (the CLI is a stub in AC2). The forwarder will need sqs:SendMessage on the mailbox; the Dell users hold the admin group (CTO ruling @53acd6fe5f), and the install cell reads it back.
comp-adversary: RUN -- a forwarder that verifies signatures upstream (refused: THE CELL; the receiver is the authority); a typed queue address (refused: AC2 uses an unset variable and a made-up URL); a send that marks done before it succeeds (refused: AC1 failed-send arm); the same bytes acting twice under a renamed file (refused: AC1 arm 3); a rejected file moved or deleted (refused: THE CONTRACT, bytes untouched). BLIND: a real send to the real queue is not made here; the live read-back is cell CA-i-5.
naming: no S3 address, AWS resource or registry name is created (CLAUDE.md rule 30 non-application); the queue address is read from the environment.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAi3-AC1 base: FAIL as expected (no forwarder module); CAi3-AC2 base: FAIL as expected (no forwarder.py). Both green arms: PASS as expected against a scratch reference forwarder (6 of 6, 1 call), then removed.
Source: CTO round-16 analysis `ledger/ROUND_ANALYSIS.round16.md` @6e9e2fc1ff section 3 item 3; rows COMM_ASSIST-W8-S8, W8-S9; PRD v0.7 FWD-7, FWD-8.
