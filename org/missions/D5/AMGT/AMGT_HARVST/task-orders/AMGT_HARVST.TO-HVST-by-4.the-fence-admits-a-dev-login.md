# AMGT_HARVST task order -- `HVST-by-4` -- ROUND 81 (`1.0.0_SA_CTO~DELL1` msg 4413, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 2; row `AMGT_HARVST-D1-S9`): THE RESEARCH-PULL-ENQUEUE FENCE ADMITS A CALLER WHOSE TIER IS `internal` OR WHOSE `userType` IS `Dev`, AND STILL REFUSES EVERY OTHER CALLER AND A CALLER WITH NO CONTEXT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-by-4.the-fence-admits-a-dev-login</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-by-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~137</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO deploy, NO `aws lambda` call, NO S3, SQS or CloudWatch call, NO Terraform. A fake boto3 client in the tests.
comp-adversary: RUN at L5 -- the adversary is a clause that admits on a substring or on a case-insensitive match, one that admits a caller with no context, an admit that reads `userType` from the request BODY (forgeable) instead of the authorizer context, or a change that moves a 400, a 202 or the `OK:` line.
</preflight>

## 0. THE CELL

`infra/aws/lambda/research/pull_enqueue/lambda_function.py` (the Lambda `opal-research-pull-enqueue`, behind
`POST /api/private/research/pull`) carries a caller fence. Today `lambda_handler` admits a caller only when the authorizer
context's `tier` is exactly `internal`, and a refusal writes `DENIED: tier=<tier or NONE>` and returns
`403 {"error": "forbidden"}` (HVST-bx-1 and HVST-by-1, both merged).

The portal's authorizer also grants all access to a login whose `userType` is `Dev`, whatever its tier. The laptop CTO measured
3 of 6 Dev logins with a tier other than `internal`, all opal-capital admins; the fence refuses them. The ruling
(`1.0.0_SA_CTO~DELL1` msg 4413 as the cluster lead): **the fence admits `tier == internal` OR `userType == Dev`.** Add that one clause,
and keep the rest exactly: no context is still 403.

## 1. THE BUILD (LOCAL)

Work in your worktree. Change `infra/aws/lambda/research/pull_enqueue/lambda_function.py` and add one test file.
1. **The authorizer context's `userType` is read where `tier` is read, and nowhere else.** Add a helper `_caller_user_type(event)`
   beside `_caller_tier`, with the same shape: `event["requestContext"]["authorizer"]["lambda"]["userType"]` when a `lambda` level
   exists, else `event["requestContext"]["authorizer"]["userType"]`; every non-dict level, a missing key or a non-string value is
   `None`. It never reads the request body, a header, or the event's top level.
2. **The admit test** is `tier == "internal" or user_type == "Dev"`, each an EXACT, case-sensitive string match (`dev`, `DEV`,
   ` Dev` and `Developer` are refused). A caller with no authorizer context has both `None` and is refused. Keep the existing
   refusal branch as it is, including its `DENIED: tier=<...>` line, which still carries the tier string only (do not add `userType`
   to the log line: the ruling did not ask for it, and it is an extra field about the caller).
3. **Nothing else changes:** the 202 body, the 400 for a missing ticker, the status write, the send and the `OK:` line.
4. **Tests**, in `infra/aws/lambda/research/pull_enqueue/test_by4_dev_admitted.py`, with the same fake `boto3` pattern as the existing
   `test_bx1_tier_fence.py` (read it; do not edit it), each arm asserting the response AND the call counts on the fake S3 and SQS:
   - `userType` Dev with tier `advisor` and a ticker: 202, one put, one send;
   - `userType` Dev with NO tier at all and a ticker: 202, one put, one send;
   - `userType` Advisor (not Dev) with tier `advisor`: 403, zero puts, zero sends, stdout `DENIED: tier=advisor`;
   - `userType` `dev` (lower case), and `userType` `Developer`: 403, zero calls;
   - no `requestContext` at all: 403, zero calls, stdout `DENIED: tier=NONE`;
   - `userType` `Dev` carried ONLY in the request body, with an advisor tier in the context: 403, zero calls (the body is not read);
   - an API Gateway v2 shaped event (JSON-string `body`, `requestContext.authorizer.lambda.userType == "Dev"`): 202;
   - a MUTANT: with the `userType` clause removed, the Dev-with-advisor-tier arm fails (assert that it does).
5. Do not deploy, invoke, or run anything against AWS. A surprise is a row; keep working.

<paths>
infra/aws/lambda/research/pull_enqueue/lambda_function.py
infra/aws/lambda/research/pull_enqueue/test_by4_dev_admitted.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~137/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-by-4"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_by4_dev_admitted.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-by-4"><invocation>python -m pytest infra/aws/lambda/research/pull_enqueue/test_bx1_tier_fence.py infra/aws/lambda/research/pull_enqueue/test_by1_refusal_logged.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure. If the handler's `utcnow()` DeprecationWarning makes a bare pytest summary read `passed, N warnings in`, add a filterwarnings mark in YOUR test file only.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W137-S1`.
- **THE CHANNEL FILE `org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md` HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES: read the file in binary, insert before the closing `]` and the code fence in the tail's own line ending, write binary, and check `git diff --numstat HEAD -- <file>` reads N insertions and 1 deletion.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~137/AMGT_HARVST.TO-HVST-by-4.the-fence-admits-a-dev-login.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-by-4.the-fence-admits-a-dev-login`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4413: "the fence admits tier internal OR userType Dev -- add the clause ... keeping no-context = 403.
  Arms: Dev with non-internal tier admitted, advisor non-Dev 403, no context 403. It rides by-2's deploy if by-1 is not merged yet;
  otherwise its own pair." by-1 was merged @31590746f1 and by-2's deploy had begun (plan and apply files written 10:20Z) before the
  ruling, so this is its own build (by-4) and its own deploy (by-5).
- The authorizer's own test was read by `0.7.0_AE_CloudOps~HV1` (`bx2_authorizer.out`): `q.userType === "Dev"` and `q.tier ===
  "internal"` are two independent paths to ALL access, and the context it returns carries both.
- Class WORLD by the L6 gate's path floor; this cell executes no world act. The deploy is by-5.
- Slot ~137, worktree `C:/Dev/wk-harvst-137`, branch `wk-AMGT_HARVST-137`.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>81</round>
<workstream>DEVADMIT</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>

**COMPLETE 2026-10-12 ~14:4xZ (issuer `2.0.0_SA_COO~W1`):**
- **Built:** worker ~137, branch `wk-AMGT_HARVST-137` @a994911d98 (build 2f08f9eb4e, rows and proof a994911d98). Proof VALID rc 0
  (re-run by this seat in the worktree with `--governing-order`). **Merged:** f94560218c on box/dell1 by `safe-merge.sh`
  (4 files, 0 dropped).
- **AC1 PASS** `22 passed in 0.25s` (re-run). **AC2 PASS** `22 passed in 0.26s` (re-run; the 15 bx-1 and 7 by-1 tests, unchanged).
- **The diff, read by the issuer:** `_caller_user_type` has `_caller_tier`'s exact shape (the `lambda` level when present, else the
  authorizer level, `None` for any other shape, never the body, a header or the event's top level); the fence's refusal test is
  `not (tier == "internal" or user_type == "Dev")`. The refusal branch, its tier-only `DENIED` line, the 202, the 400 and the `OK:` line
  are untouched.
- **Rows:** D1-W137-S1 INERT (the module docstring said internal only; reworded, no behaviour change). D1-W137-S2 INERT (the order's
  numstat check read 20 and 0, not 1 deletion, because git aligns the closing brace; the file parses as one JSON array: this
  seat's face was imprecise, the bytes were right).
- **Not done here (by-5):** nothing is deployed; the live function still refuses a Dev login with a non-internal tier.

<status>complete</status>

**CANCELLED 2026-10-12 ~15:3xZ (issuer `2.0.0_SA_COO~W1`), by the ruling of `1.0.0_SA_CTO~DELL1`:** msg 4463 and the record
`ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 3 @b5915fba35 (the laptop CTO's msg 108607: the token's `tier` derives from `firmId`, an
opal-capital login is already `internal`, so the Dev clause is withdrawn and the fence stays tier-only). The status above read
`complete` from 14:50Z (merge f94560218c); it no longer stands.
- **To be reverted in the repo by `HVST-by-6` step 0** (the issuer's lane cannot write `infra/aws`): `lambda_function.py` back to its
  `31590746f1` bytes (the code `HVST-by-2` deployed) and `test_by4_dev_admitted.py` removed. The channel rows and the proof instance
  stay (append-only). Until that commit lands the repo still carries the by-4 code.
- **The live function** carried the Dev-admitting code from 14:40:46Z to its rollback; that is `HVST-by-6`'s act.

<status>cancelled</status>
