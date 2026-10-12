# AMGT_HARVST task order -- `HVST-by-1` -- ROUND 81 (`1.0.0_SA_CTO~DELL1` msg 4394, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 1 item 1; rows `AMGT_HARVST-D1-S8`): THE RESEARCH-PULL-ENQUEUE HANDLER LOGS EVERY REFUSAL WITH THE TIER STRING IT SAW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-by-1.a-refusal-is-logged-with-the-tier-it-saw</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-by-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~136</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO deploy, NO `aws lambda` call, NO S3, SQS or CloudWatch call, NO Terraform. A fake boto3 client in the tests.
comp-adversary: RUN at L5 -- the adversary is a log line that carries the ticker, the request body, a credential or the caller's identity; a refusal that stops being a 403; a log call placed where it can raise and turn a 403 into a 500; or a success path that gains a new line.
</preflight>

## 0. THE CELL

`infra/aws/lambda/research/pull_enqueue/lambda_function.py` (the Lambda `opal-research-pull-enqueue`, behind
`POST /api/private/research/pull`) now carries a caller fence (HVST-bx-1, deployed): `lambda_handler` returns
`403 {"error": "forbidden"}` unless the authorizer context's `tier` is exactly `internal`. **The refusal writes no log line.**
The function's only `print` is the `OK: enqueued pull request for ...` line after a successful enqueue, and the portal API stage has
no access log, so an internal session that is refused (a lockout) reads the same in the log as no call having been made. The CTO
(`1.0.0_SA_CTO~DELL1` msg 4394) rules that a refusal logs the tier string it saw, which closes row D1-S8 and makes the post-deploy
read observable.

## 1. THE BUILD (LOCAL)

Work in your worktree. Change `infra/aws/lambda/research/pull_enqueue/lambda_function.py` and add one test file.
1. **One log line per refusal, in the fence's refusal branch, before the `return`:**
   `print("DENIED: tier=%s" % <tier>)` where `<tier>` is the tier string the fence read (`_caller_tier(event)`), or the word `NONE`
   when it read none. The tier text is made safe BEFORE it is written: replace any character outside printable ASCII or any
   `\r` / `\n` with `?`, and cut it to 32 characters. The line carries **nothing else**: not the ticker, not the body, not the
   request context, not an account, user or firm identifier, not a header.
2. **The log call cannot change the response.** Wrap the formatting and the print so that nothing in it can raise out of the
   handler (a plain `try` / `except Exception: pass` around that one statement is enough). The response stays exactly
   `403 {"error": "forbidden"}`.
3. **Nothing else changes:** the success path, the 400 for a missing ticker and the `OK:` line are byte-for-byte as they are.
4. **Tests**, in `infra/aws/lambda/research/pull_enqueue/test_by1_refusal_logged.py`, with the same fake `boto3` pattern as the
   existing `test_bx1_tier_fence.py` (read it; do not edit it) and `capsys` for the log:
   - a `partner` tier: 403, and stdout holds exactly one line `DENIED: tier=partner`;
   - no `requestContext`: 403 and `DENIED: tier=NONE`;
   - a tier of `x` repeated 100 times: 403 and the line is `DENIED: tier=` plus exactly 32 `x`;
   - a tier `partner\nOK: forged` (an embedded newline): 403 and stdout is ONE line whose text contains no newline inside the tier;
   - an event whose body holds a ticker and a cookie string, refused: stdout contains neither the ticker nor the cookie;
   - an internal context with a ticker: 202, stdout holds the `OK:` line and NO `DENIED` line;
   - a MUTANT: with the print removed, the partner arm fails (assert that it does).
5. Do not deploy, invoke, or run anything against AWS. A surprise is a row; keep working.

<paths>
infra/aws/lambda/research/pull_enqueue/lambda_function.py
infra/aws/lambda/research/pull_enqueue/test_by1_refusal_logged.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~136/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-by-1"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_by1_refusal_logged.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-by-1"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_bx1_tier_fence.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W136-S1`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES: read the file in binary, insert before the
  closing `]` and the code fence in the tail's own line ending, write binary. Before you commit it run
  `git diff --numstat HEAD -- <the file>`: it must read N insertions and 1 deletion (the previous last row's closing brace gains a
  comma). Two earlier workers and the issuer each rewrote the whole file by editing it as text and had to repair it.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~136/AMGT_HARVST.TO-HVST-by-1.a-refusal-is-logged-with-the-tier-it-saw.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-by-1.a-refusal-is-logged-with-the-tier-it-saw`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4394 and `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 1: "a refusal log line carrying the tier
  string (closes D1-S8 and makes my post-act read observable)".
- The tier string is the only caller fact logged. It is the authorizer's own output, not a secret; the cut and the character filter
  keep it from forging a line. Nothing about the person is logged.
- The deploy is by-2 (a WORLD act under its own pair). Class WORLD by the L6 gate's path floor; this cell executes no world act.
- Slot ~136, worktree `C:/Dev/wk-harvst-136`, branch `wk-AMGT_HARVST-136`.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>81</round>
<slot>dell1</slot>
<fabric>dell1</fabric>

**COMPLETE 2026-10-12 ~14:4xZ (issuer `2.0.0_SA_COO~W1`):**
- **Built:** worker ~136, branch `wk-AMGT_HARVST-136` @b8c84753a0 (build 62797b8bc3, proof b8c84753a0). Proof VALID rc 0 (re-run by this
  seat in the worktree with `--governing-order`). **Merged:** 31590746f1 on box/dell1 by `safe-merge.sh` (3 files, 0 dropped).
- **AC1 PASS** `7 passed in 0.24s` (re-run). **AC2 PASS** `15 passed in 0.27s` (re-run; `test_bx1_tier_fence.py` unchanged).
- **The diff, read by the issuer:** `lambda_handler` keeps the tier it read in a variable; on a refusal it prints
  `DENIED: tier=%s` of `_denied_tier_text(tier)` (NONE when none, every character outside printable ASCII including CR and LF made `?`,
  cut to 32) inside a `try` / `except Exception: pass`, then returns the same 403 `{"error": "forbidden"}`. Success path, 400 and
  the `OK:` line are untouched. The line carries nothing else.
- **Rows:** none. **Not done here (by-2):** nothing is deployed; the live function still writes no refusal line.

<status>complete</status>
