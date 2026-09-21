# AMGT_RESAPP task order -- `AMGT-rk-64` -- `pull_consumer.py`'s `stage_pull` call site drops the stray fourth positional argument so it matches `model_block_pull.stage_pull`'s real 3-parameter signature, closing a guaranteed-TypeError EXPOSURE that would have silently destroyed every real pull request through the FAILED-then-delete path, before it ever fires once

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-64</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~64</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one consumer script and adds one offline test file;
  it arms no cron, alarm, monitor or cadence, reads no schedule and writes none; the ONE live act (AC3, a real
  SQS round trip) is a synthetic drain of a pre-existing queue's existing poller shape, not a new schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant changes; AC3 exercises the EXISTING SQS/S3
  permissions this box already holds (the same ones `pull_consumer.py --once` uses today), reads none, changes
  none.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~64`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~64;`. **NEVER RUN AN INSTALL** (no pip install; boto3 is already
the estate's standard dependency).

## 1. THE CELL, inlined in full -- `AMGT-rk-64` (R15-T2; row `AMGT_RESAPP-Z-W39-S2`; EXPOSURE class)

**The analysis row, verbatim (`ROUND_ANALYSIS.round14.md` @93cb6416e4 s.2.3, `:78-86`):** *"`pull_consumer.py`
arity defect (W39-S2, adjudication finding 4). RULED: a round-15 cell, EXPOSURE class. Guaranteed silent
data-loss on first real traffic (`stage_pull` called with 4 positional args against a 3-parameter signature,
inside a `try/except` that marks FAILED and unconditionally deletes the SQS message), measured NEVER FIRED against
the served `packs/` prefix. Per Rule 22's negative mirror: this is an EXPOSURE, not an incident -- the remedy is
building the fix, not re-opening anything the gap admitted, because nothing was admitted. Do not wait for the
box-side consumer's first real run to find it. Cell R15-T2: correct the call site to the current signature; proof
= a live SQS round-trip on a synthetic message proving it is no longer deleted on a mismatched call, plus the AST
check the CVO used, re-run by the cutting worker on its own branch HEAD (not inherited from the adjudication)."*

**The CVO's original finding, verbatim (`ROUND14_L9_ADJUDICATION_20260921.md` s.4 item 4):** *"`pull_consumer.py`
calls `stage_pull` with 4 positional args against a 3-parameter signature (AST-verified) inside a `try/except`
that marks FAILED and then unconditionally deletes the SQS message -- so the first real traffic through this
consumer would silently destroy every enqueued pull request. Measured NEVER FIRED: the served `packs/` prefix
carries exactly one `status.json`, written 19 minutes before the defective call site was committed, and nothing
since. EXPOSURE, not incident."*

**THE MEASURED STATE, at HEAD (cite these lines; do not re-derive from memory -- RE-MEASURE and confirm before you
touch anything):**
- `integrations/bloomberg/research/pull_consumer.py:97-100`:
  ```
  try:
      pull_log: dict = {"securities": [], "requests": []}
      pull_result = mbp.stage_pull(blp, s3, ticker, pull_log)
      derive_result = mbp.stage_derive(s3, ticker, raw_stamp=pull_result["raw_stamp"])
  ```
  Line 99 passes FOUR positional arguments (`blp, s3, ticker, pull_log`).
- `integrations/bloomberg/research/model_block_pull.py:371`: `def stage_pull(blp, s3, security: str) -> dict:` --
  THREE positional parameters. `stage_pull` builds its OWN internal `pull_log` at its own line 386
  (`pull_log = {"securities": [security], "requests": []}`) and accepts no external one; the local `pull_log`
  dict `pull_consumer.py` builds at its line 98 is DEAD -- created, passed as a stray fourth argument, never used
  for anything else in `process_one`.
- Calling a 3-parameter function with 4 positional arguments raises `TypeError: stage_pull() takes 3 positional
  arguments but 4 were given` IMMEDIATELY, before any Bloomberg call, any S3 read, any real work -- on EVERY
  invocation, unconditionally, regardless of ticker or Bloomberg health.
- `pull_consumer.py:97-121`: this call sits inside a `try/except Exception as exc` (`:114`) that marks the status
  FAILED with the exception text (`:115-118`) and then, OUTSIDE and AFTER the try/except, UNCONDITIONALLY deletes
  the SQS message (`:120`, runs on BOTH the success and the except path). So a real message would be marked FAILED
  with reason starting `TypeError: stage_pull() takes 3 positional arguments but 4 were given` and deleted forever
  -- no DLQ is declared (module docstring `:23-24`), so nothing about this failure is ever seen again.
- The health gate (`:88-95`) runs BEFORE this call site and returns early on an unhealthy `blp.health()` --
  meaning the defect is reachable ONLY when Bloomberg reports healthy, which is exactly the branch a real pull
  request needs.
- **MEASURED NOW, confirming the AST claim independently:** `ast.parse` on `pull_consumer.py` finds the
  `mbp.stage_pull(...)` call with `len(call.args) == 4`; `ast.parse` on `model_block_pull.py` finds
  `def stage_pull(...)` with `len(def.args.args) == 3`. Mismatch confirmed at this cut, by this seat, independent
  of the CVO's own read (a different instrument: static AST inspection rather than the CVO's own citation).
- The producer side, `infra/aws/lambda/research/pull_enqueue/lambda_function.py:100-105`: sends
  `{"ticker": ticker, "security_key": sec_key, "requested_at": now}` as the SQS `MessageBody` -- this is the exact
  body shape `process_one` (`pull_consumer.py:80-84`) reads (`body["ticker"]`, `body.get("security_key")`).
- The queue, `opal-research-pull-requests`, is normally EMPTY (round-14 cell `AMGT-rk-7`'s own measurement: "0
  visible, 0 in flight, no event-source mapping") -- a safe target for one synthetic round trip.

**RULED, what you build:**

1. **`integrations/bloomberg/research/pull_consumer.py`, lines 97-99.** Delete line 98
   (`pull_log: dict = {"securities": [], "requests": []}` -- dead, its only use was the stray argument) and change
   line 99 from `pull_result = mbp.stage_pull(blp, s3, ticker, pull_log)` to
   `pull_result = mbp.stage_pull(blp, s3, ticker)`. Nothing else in `process_one` or the file moves -- `derive_result
   = mbp.stage_derive(s3, ticker, raw_stamp=pull_result["raw_stamp"])` on the next line is already correct (3
   arguments matching `stage_derive`'s own 3-parameter signature at `model_block_pull.py:899`) and is untouched.

2. **`integrations/bloomberg/research/tests/test_pull_consumer_arity.py`** -- a NEW, permanent, fully OFFLINE
   regression file (no real AWS, no real Bloomberg, no network) with exactly two tests:
   - `test_ast_call_arity_matches_signature()`: parses `pull_consumer.py` (find the AST `Call` node whose `func` is
     an `Attribute` named `stage_pull` on a `Name` `mbp`, count `len(call.args)`) and `model_block_pull.py` (find
     the AST `FunctionDef` named `stage_pull`, count `len(node.args.args)`), asserts the two counts are equal. This
     is the STATIC check the CVO used, re-run as a standing regression so this exact class of defect cannot land
     again silently.
   - `test_process_one_reaches_stage_pull_without_arity_typeerror(monkeypatch)`: imports `pull_consumer` and
     `model_block_pull as mbp`; monkeypatches `mbp._load_blp_client` to return a fake object whose `.health()`
     returns `{"ok": True}`, `mbp.stage_pull` to a 3-parameter stub that records its arguments and returns a fixed
     dict with a `raw_stamp`, and `mbp.stage_derive` to a stub that records its arguments and returns a fixed dict
     with a `derived_stamp`; builds a fully in-memory fake `s3` client (a dict-backed store, `get_object`/
     `put_object` only) and a fake `sqs` client (`delete_message` records the receipt handle); calls
     `pull_consumer.process_one(msg, fake_s3, fake_sqs, "https://fixture-queue-url")` with a synthetic message body
     `{"ticker": "ZZZTEST US Equity", "security_key": "ZZZTEST_US_Equity"}`; asserts the returned state is
     `"LANDED"`, the patched `stage_pull` was called with EXACTLY 3 positional arguments, the written
     `packs/ZZZTEST_US_Equity/status.json` reads `state == "LANDED"` with no `"positional argument"` text in its
     `reason`, and the fake SQS `delete_message` was called exactly once with the message's own receipt handle.
     Neither test touches the real `opal-research-pull-requests` queue or the real `opal-data-harvest` bucket --
     write the file's own module docstring saying so, so a future reader does not assume AWS credentials are
     needed to run it in ordinary CI.

**What this cell does NOT change:** `integrations/bloomberg/research/model_block_pull.py` (read only --
`stage_pull`'s signature is the fixed reference; the call site moves to match it, never the reverse); `stage_derive`'s
call (already correct); the health-gate logic (`:88-95`); the delete-unconditionally structure (`:120`) -- that is a
SEPARATE, already-understood design choice (module docstring `:23-24`, "no DLQ is declared... a FAILED status is the
durable record") and not this cell's surface to revisit.

**THE VALIDATION BAR:** the permanent test file (AC1, AC2) is proven offline, no security population, no live call.
The ONE-TIME live proof (AC3, section 5) is a synthetic, non-production round trip on the real
`opal-research-pull-requests` queue and `opal-data-harvest` bucket, self-cleaning (the synthetic S3 key is deleted
in the same act), never a fleet run, never a real ticker.

## 2. WHERE THIS CAME FROM

**ROUND 15**, decomposition s.23 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-14 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round14.md` @93cb6416e4 s.2.3 (`:78-86`) and s.3 (`:105`
row R15-T2); the CVO's `ROUND14_L9_ADJUDICATION_20260921.md` s.4 item 4 (row `AMGT_RESAPP-Z-W39-S2`, no worker ever
filed this row directly -- surfaced by the CVO's own AST read during L9). PRD v0.13 @1699960261: `C-PRODUCTION-HOME`
(the consumer's own module docstring, `SEAM_DESIGN.md` section 2) -- no FWD or new `C-` contract is touched; this is
a defect fix inside an already-ratified design, not a scope change.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/pull_consumer.py
integrations/bloomberg/research/tests/test_pull_consumer_arity.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~64/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-64.pull-consumer-stage-pull-arity.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read
  `integrations/bloomberg/research/model_block_pull.py`, `integrations/bloomberg/READ_HERE.md`,
  `infra/aws/lambda/research/pull_enqueue/lambda_function.py` freely); this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only. AC3 writes and then DELETES exactly one S3 key,
  `packs/ZZZTEST_US_Equity/status.json` -- that key is not a tree path and carries no grant of its own (it is a
  live-store act under section 5's own procedure, the same class as `AC4`'s live pre-act reads in other cells'
  orders), and it MUST NOT survive the invocation (verified by AC3's own trailing read).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~64 <0.9.0_WK_AMGT_RESAPP~64@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every
  `.py` you commit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39) inside safe-commit.

## 4. BOUNDS

**NO DEPLOY, NO VENDOR CALL, NO REAL BLOOMBERG CALL** -- AC3's `blp` is monkeypatched in-process; nothing this
order does reaches the Bloomberg terminal or requires a sign-in. **THE ONE LIVE ACT IS NAMED:** one SQS
SendMessage + ReceiveMessage + (the consumer's own) DeleteMessage on `opal-research-pull-requests`, and one S3
PutObject + GetObject + DeleteObject pair on a single synthetic key under `packs/ZZZTEST_US_Equity/` in
`opal-data-harvest` -- nothing else, no other key, no other queue. PORTAL FROZEN (not your surface). **COLLECTION
STAYS OFF** (this order enqueues nothing new and starts no schedule). **NO alarm, monitor, SNS/SES-send,
notification or freshness checker.** Secrets through `comp-secrets` only (none needed here). No non-ASCII in
anything you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular, never change the
unconditional-delete structure and never add a DLQ or a retry; those are separate, already-ratified design
choices, not this cell's.
**NEVER LEAVE THE SYNTHETIC KEY BEHIND.** AC3's own trailing step deletes `packs/ZZZTEST_US_Equity/status.json`
and re-reads to confirm absence; if the delete fails, that is a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), not
a silent skip.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W64-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-64"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests/test_pull_consumer_arity.py -v 2>&1 | tail -20</invocation><expect>both test_ast_call_arity_matches_signature and test_process_one_reaches_stage_pull_without_arity_typeerror print PASSED, final line "2 passed" (or more if you added helper-only functions pytest does not collect as tests -- name any such addition explicitly), 0 failed</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-64"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import ast
consumer = ast.parse(open('integrations/bloomberg/research/pull_consumer.py', encoding='utf-8').read())
pull = ast.parse(open('integrations/bloomberg/research/model_block_pull.py', encoding='utf-8').read())
call_args = None
for node in ast.walk(consumer):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'stage_pull' and isinstance(node.func.value, ast.Name) and node.func.value.id == 'mbp':
        call_args = len(node.args)
def_params = None
for node in ast.walk(pull):
    if isinstance(node, ast.FunctionDef) and node.name == 'stage_pull':
        def_params = len(node.args.args)
print('call_positional_args', call_args, 'def_positional_params', def_params, 'match', call_args == def_params)
"</invocation><expect>call_positional_args 3, def_positional_params 3, match True -- re-derived independently of AC1's own pytest run, by this worker, on its own branch HEAD, as the analysis's own instruction requires ("re-run by the cutting worker on its own branch HEAD, not inherited from the adjudication")</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-64"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, sys, time
sys.path.insert(0, 'integrations/bloomberg/research')
import pull_consumer
import model_block_pull as mbp

def fake_stage_pull(blp, s3, security):
    return {'raw_stamp': '20260921T000000Z', 'ref_key': 'raw/zzz/ref.json', 'hist_key': 'raw/zzz/hist.json'}

def fake_stage_derive(s3, security, raw_stamp=None):
    return {'derived_stamp': '20260921T000100Z', 'derived_key': 'derived/zzz/model_block.json'}

class FakeBlp:
    def health(self):
        return {'ok': True}

mbp._load_blp_client = lambda: FakeBlp()
mbp.stage_pull = fake_stage_pull
mbp.stage_derive = fake_stage_derive
pull_consumer.mbp = mbp

sqs = boto3.client('sqs')
s3 = boto3.client('s3')
queue_url = pull_consumer._queue_url(sqs)
pre = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['ApproximateNumberOfMessages'])['Attributes']
print('pre_queue_visible', pre.get('ApproximateNumberOfMessages'))

sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps({'ticker': 'ZZZTEST US Equity', 'security_key': 'ZZZTEST_US_Equity', 'requested_at': '2026-09-21T00:00:00Z'}))
resp = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1, WaitTimeSeconds=10)
msgs = resp.get('Messages', [])
print('received', len(msgs), 'of 1 expected')
state = pull_consumer.process_one(msgs[0], s3, sqs, queue_url) if msgs else 'NO_MESSAGE_RECEIVED'
print('state', state)

ho = s3.get_object(Bucket=mbp.BUCKET, Key='packs/ZZZTEST_US_Equity/status.json')
status = json.loads(ho['Body'].read())
print('status_state', status.get('state'), 'reason_has_positional_argument', 'positional argument' in (status.get('reason') or ''))

s3.delete_object(Bucket=mbp.BUCKET, Key='packs/ZZZTEST_US_Equity/status.json')
try:
    s3.head_object(Bucket=mbp.BUCKET, Key='packs/ZZZTEST_US_Equity/status.json')
    cleaned = False
except Exception:
    cleaned = True
print('synthetic_key_cleaned', cleaned)

post = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['ApproximateNumberOfMessages'])['Attributes']
print('post_queue_visible', post.get('ApproximateNumberOfMessages'))
"</invocation><expect>pre_queue_visible "0" (the queue is normally empty, per AMGT-rk-7's own measurement -- re-confirm it here); received 1 of 1 expected; state "LANDED" (not "FAILED" -- the patched stage_pull was reached and returned normally, no positional-argument TypeError); status_state "LANDED" and reason_has_positional_argument False; synthetic_key_cleaned True (the S3 key does not survive this criterion); post_queue_visible "0" (SQS ApproximateNumberOfMessages is eventually-consistent -- if it prints a nonzero transient value, re-read once after a few seconds and record both reads; the message MUST already be deleted by process_one's own DeleteMessage call at :120, which AC3's state="LANDED" already implies ran)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC3 is the ONE live act in this order; run it exactly once, record its full output verbatim, and confirm
the cleanup lines before reporting.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~64/AMGT_RESAPP.TO-AMGT-rk-64.pull-consumer-stage-pull-arity.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming AC3's full output and confirming the synthetic
S3 key and SQS message left no residue.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>15</round>
<slot>~64</slot>
<fabric>site-z</fabric>
