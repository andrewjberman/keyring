# AMGT_HARVST task order -- `HVST-bx-1` -- ROUND 80 (`1.0.0_SA_CTO~DELL1` msg 4352, `ledger/ROUND_ANALYSIS.round79.md` item 1; ruling `ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md` section 1): THE RESEARCH-PULL-ENQUEUE HANDLER REFUSES EVERY CALLER THAT IS NOT `internal`, AND FAILS CLOSED WHEN IT HAS NO CALLER CONTEXT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bx-1.the-enqueue-handler-refuses-a-non-internal-caller</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bx-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~134</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO deploy, NO `aws lambda` call, NO S3 or SQS call, NO Terraform. A fake boto3 client in the tests; nothing reaches the world.
comp-adversary: RUN at L5 -- the adversary is a fence that treats a missing context as trusted, a check that matches `internal` as a substring or case-insensitively, a fence placed AFTER the S3 write or the SQS send, or a check on "the event came through API Gateway" (forgeable).
</preflight>

## 0. THE CELL

`infra/aws/lambda/research/pull_enqueue/lambda_function.py` is the Lambda `opal-research-pull-enqueue`, behind
`POST /api/private/research/pull`. Its `lambda_handler(event, context)` reads the ticker from the event and then (1) overwrites
`packs/<security_key>/status.json` in the research bucket and (2) sends one SQS message that a box consumer turns into a
Bloomberg draw. **It examines no caller.** The portal's authorizer lets any verified login through, so a partner-firm login
can reach it. The ruling (laptop CTO section 3 and `1.0.0_SA_CTO~DELL1`, 2026-10-12):

- The handler reads the authorizer context's `tier` and returns **403 unless it is exactly `internal`**.
- **An event with NO authorizer context is refused too (fail closed).** "No context" never reads as "trusted". A direct invoker
  is gated by IAM `lambda:InvokeFunction`, not by this handler.
- Do NOT add a check that the event "came through API Gateway": it is forgeable.
- Nothing else changes: the 202 body, the 400 for a missing ticker, the status write and the send stay as they are.

## 1. THE BUILD (LOCAL)

Work in your worktree. Change `infra/aws/lambda/research/pull_enqueue/lambda_function.py`, add the test file, and amend one
check file.

1. **The fence, FIRST in `lambda_handler`, before the ticker is read and before any S3 or SQS call.** A small helper
   `_caller_tier(event)` returns the authorizer context's `tier` string or `None`. Read the context at
   `event["requestContext"]["authorizer"]`. For an API Gateway HTTP API v2 event with a Lambda authorizer, the authorizer's
   returned context can sit one level down at `event["requestContext"]["authorizer"]["lambda"]`; accept `tier` at either of the two
   places, and nothing else. Before you write it, look in `infra/aws/lambda/` with Grep for an existing helper that reads the
   portal authorizer's `tier` (search `requestContext` and `tier`) and follow its shape if one exists. Every non-dict level, a
   missing key, or a non-string value is `None`.
2. **The refusal:** `if _caller_tier(event) != "internal": return _response(403, {"error": "forbidden"})`. Exact string match,
   case-sensitive. The 403 body carries no detail about why.
3. **Tests**, in `infra/aws/lambda/research/pull_enqueue/test_bx1_tier_fence.py`, with a fake `boto3` (patch `boto3.client`
   before importing the module, and set `QUEUE_URL` in the environment; no network). Four arms, each asserting the response AND the
   call counts on the fake S3 and SQS clients:
   - internal context (`{"requestContext": {"authorizer": {"tier": "internal"}}, "ticker": "NVDA US Equity"}`): 202, one put, one send;
   - non-internal context (`tier` `partner`): 403, zero puts, zero sends;
   - no `requestContext` at all: 403, zero puts, zero sends;
   - a `requestContext` with an authorizer and no `tier`, and another with `tier` `INTERNAL`: 403, zero calls (two assertions).
   - An API Gateway v2 shaped event (JSON-string `body`, `requestContext.authorizer.lambda.tier == "internal"`) is admitted (202).
   - A MUTANT: patch `_caller_tier` to always return `"internal"`; the non-internal arm must then FAIL (assert that it does).
4. **The e2e check is amended.** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/check_e2e.py` invokes the
   deployed function directly with `{"ticker": TICKER}` at line 69. Change its invoke payload to also carry
   `"requestContext": {"authorizer": {"tier": "internal"}}`. Add a `--enqueue-only` command-line flag: with it, the check stops
   right after printing the `ENQUEUE:` line (no consumer launch, no polling) and returns 0 when the response is 202. Without the
   flag, behaviour is unchanged apart from the payload. Add one test in your test file, named
   `test_e2e_check_payload_carries_internal_context`, that imports the check module (path-load it), patches its boto3 client with
   a fake that records the `Payload` bytes, runs `main()` with `--enqueue-only`, and asserts the recorded payload parses to a dict
   whose `requestContext.authorizer.tier` is `internal` and whose `ticker` is the check's `TICKER`.
5. Do not deploy, invoke, or run `check_e2e.py` against anything real. A surprise is a row; keep working.

<paths>
infra/aws/lambda/research/pull_enqueue/lambda_function.py
infra/aws/lambda/research/pull_enqueue/test_bx1_tier_fence.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/check_e2e.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~134/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bx-1"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_bx1_tier_fence.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bx-1"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_bx1_tier_fence.py -k e2e_check_payload -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W134-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~134/AMGT_HARVST.TO-HVST-bx-1.the-enqueue-handler-refuses-a-non-internal-caller.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bx-1.the-enqueue-handler-refuses-a-non-internal-caller`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4215 and the record `ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md` section 1
  (fail closed; the e2e check supplies an internal context; close arms internal / non-internal / no context / amended e2e).
- The laptop CTO's record `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_POST_OFFLINE_FIVE_CROSSBOX_CALLS_AND_TWO_SECURITY_CARRIES_20261012.md`
  section 3 row 2 (@8424b373f2) assigned the fence to AMGT_HARVST, owner `2.0.0_SA_COO~W1`; section 4: the IAM grant is the real control for a direct invoke.
- **The e2e arm is read narrowly, by the issuer, and the reason is stated:** the CTO's fourth arm is "the amended e2e check passes".
  The check as written also launches `pull_consumer.py --once`, which is a real Bloomberg draw for one ticker. This cell does not run
  it. Its arm is the payload (unit test) and, at the deploy cell bx-2, the DEPLOYED function's admission of an internal context read
  as a 400 on an empty body (admitted past the fence, nothing written). A full live e2e remains a separate, Bloomberg-queue act.
- Merge: the issuer merges this branch at the chain end with `safe-merge.sh`; the deploy is bx-2 (a WORLD act under its own pair).
- **Class:** declared WORLD because the L6 gate floors the class by `<paths>` (an `infra/aws/lambda/` path is an infrastructure path,
  spine v3.19 L6). The cell itself executes no world act: local code and a fake client only. The deploy is bx-2.
- Slot ~134, worktree `C:/Dev/wk-harvst-134`, branch `wk-AMGT_HARVST-134-r80`.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>80</round>
<slot>dell1</slot>
<fabric>dell1</fabric>
