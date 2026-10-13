# ADVI_FIRMBKTS task order -- `FB-j-9` -- THE GENERATOR'S MODEL CALL STOPS PASSING `betas`, AND EVERY SLOT DROP LOGS ITS EXCEPTION CLASS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~73</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a Lambda code change, not deployed here; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act and no grant; the test stubs the model call and the metrics.
comp-adversary: RUN by the issuer -- at the base the test file is absent (AC1 FAIL) and the diff is empty (AC2 FAIL); AC3 FAILs with nothing changed; the reproducing arm's premise was reproduced by the issuer offline (`TypeError` on the real SDK). Blindness: the stubbed test proves the call's keywords against the real SDK signature and the helper's output, not that the deployed function reaches the model or the log.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-j-9` (round 7; the CTO's rulings on row `D1-S48`, ROUND_ANALYSIS.round3.md ADDENDA 14 and 15)

`infra/aws/lambda/exec-summary-generator/lambda_function.py`, `_build_slot` (about lines 232-252) calls the model through `_call_llm` and
validates the reply, and its two `except` clauses (`except URLDetectedError ... retry`, and `except (PIIDetectedError, SchemaError, Exception)`)
DROP the slot with NO output at all: `metrics.emit_slot_dropped()` and `return None`. In production every fired slot is dropped (81 of 81 in two
dry runs) and the function's log holds nothing that says why. **The cause, reproduced offline with the installed SDK (0.45.0) and no
network:** `_call_llm` (about line 185) calls `client.messages.create(..., betas=['prompt-caching-2024-07-31'])`; `Messages.create` has NO
`betas` parameter, so every call raises `TypeError: Messages.create() got an unexpected keyword argument 'betas'` before any request, and
`_build_slot`'s `except Exception` swallows it. Prompt caching needs no beta flag: the `cache_control` blocks already in the request do it.
You (1) remove that one argument and (2) make every drop name its exception class. Nothing else changes.

### 1a. The edit (`infra/aws/lambda/exec-summary-generator/lambda_function.py` and one new test file)

0. In `_call_llm`, delete the single line `betas=['prompt-caching-2024-07-31'],` from the `client.messages.create(...)` call. No other
   argument changes (the `system` and `messages` blocks keep their `cache_control`).
1. Add one small helper above `_build_slot`, `_log_slot_drop(slot, exc)`, that `print(..., flush=True)`s exactly ONE line:
   `[SLOT_DROPPED] slot=<slot> exc=<ClassName> msg=<text>`.
   - `<ClassName>` is `type(exc).__name__`.
   - `<text>` is `str(exc)` with every non-printable character (newlines included) replaced by a space, cut to its first 200 characters,
     EXCEPT when `exc` is a `PIIDetectedError`, a `SchemaError` or a `URLDetectedError`: those messages may quote advisor or client
     content, so for them `<text>` is the single word `redacted` (the class only).
   - It logs NO advisor id, NO prompt, NO model reply and NO advisor context.
2. Call it in every place `_build_slot` drops a slot (both `except` clauses and the retry's inner `except`), immediately before the existing
   `metrics.emit_slot_dropped()`. The helper must never raise (wrap its body in `try/except Exception: pass`).
3. Everything else is unchanged: the same drop, the same metric, the same return value, the same successful path, and the dry-run branch of
   `lambda_handler` from `FB-j-5` untouched. No new dependency; no other file changes.

### 1b. The test (`infra/aws/lambda/exec-summary-generator/tests/test_slot_drop_log.py`, yours, pytest, stubs only: no network, no AWS call, no model call)

Four named tests. The first three stub `_call_llm` (and the metrics emitter) on the module:
1. `test_drop_logs_class_and_clipped_message`: `_call_llm` raises `TypeError("x" * 400)`: `_build_slot` returns `None`, `emit_slot_dropped`
   is called once, and stdout (capture it) holds exactly one `[SLOT_DROPPED]` line with `exc=TypeError` and a message of at most 200 characters.
2. `test_pii_schema_url_classes_are_redacted`: `_call_llm` returns a reply for which `validate_slot_response` is stubbed to raise
   `PIIDetectedError("secret client text")`: the line has `exc=PIIDetectedError msg=redacted` and the text `secret client text` is NOT in stdout.
3. `test_success_path_unchanged`: with a valid reply the bullet dict is returned, nothing is dropped, and stdout holds no `[SLOT_DROPPED]`.
4. `test_model_call_uses_only_sdk_parameters` (the REPRODUCING test): import the real SDK (`import anthropic`; it is installed in this
   environment and in the layer), take `inspect.signature(anthropic.resources.messages.Messages.create)`, and call `_call_llm` with the module's
   `_get_anthropic` stubbed to return an object whose `messages.create(**kw)` records `kw` and returns a reply object with `usage` and
   `content[0].text`. Assert every recorded keyword is a parameter of that real signature (so `betas` fails it) and that `system` and
   `messages` still carry `cache_control`. At the base this test FAILS with `betas`.
Also run TWO MUTANT controls (temporary local edits, reverted before you commit): (i) remove the helper call from the generic `except`, and show
test 1 FAILS; (ii) put `betas=['prompt-caching-2024-07-31']` back into the call, and show test 4 FAILS; revert and show 4 passed. Never commit a mutant.

## 2. BOUNDS

1. One commit: the handler file and the test file. No deploy, no Terraform, no AWS call, no model call. ASCII only.
2. If `_build_slot` does not look as described, STOP before editing and file a BLOCKING row.

## 3. SURFACES

<paths>
infra/aws/lambda/exec-summary-generator/lambda_function.py
infra/aws/lambda/exec-summary-generator/tests/test_slot_drop_log.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~73/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~73/ADVI_FIRMBKTS.TO-FB-j-9.slot-drop-log.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-9"><invocation>cd /c/dev/wk-firmbkts-73/infra/aws/lambda/exec-summary-generator &amp;&amp; timeout 110 python -m pytest tests/test_slot_drop_log.py -q 2&gt;&amp;1 | sed "s/\x1b\[[0-9;]*m//g" | tail -1</invocation><expect>^4 passed</expect></criterion>
  <criterion id="AC2" cell_refs="FB-j-9"><invocation>cd /c/dev/wk-firmbkts-73 &amp;&amp; git diff --stat $(git merge-base HEAD box/dell1) HEAD -- infra/aws/lambda/exec-summary-generator | tail -1</invocation><expect>^ 2 files changed</expect></criterion>
  <criterion id="AC3" cell_refs="FB-j-9"><invocation>cd /c/dev/wk-firmbkts-73 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-73 --allow infra/aws/lambda/exec-summary-generator/lambda_function.py --allow infra/aws/lambda/exec-summary-generator/tests/test_slot_drop_log.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~73/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the four named arms (the mutant controls are reported, not criteria), AC2 the two-file bound, AC3 the write-surface bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~73/ADVI_FIRMBKTS.TO-FB-j-9.slot-drop-log.proof_of_spec.json`. Commit the handler and the test FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W73-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs, the mutant control's failing test name and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's ADDENDUM 15 (msg 4735): "neither (a) nor (b): fix the betas call HERE (FB-j-9), prove real bullets, read the sample, then FB-j-7 and FB-j-4; remove the betas arg, since cache_control already does caching, and add the drop log; the reproducing test must pass and a betas mutant must fail; deploy under FB-j-6's shape, then dry-run 10 pre-screened advisors; the bullets must be non-empty; read their text against the figures for wording, PII and accuracy." ADDENDUM 14 (msg 4733): "`_build_slot` swallows all exceptions with no output: log the class plus 200 characters of message
(class only for PII), with no advisor content or prompt; deploy under FB-j-6's shape; one dry run on three or more pre-screened advisors; a config
cause (model id, key, quota, SDK) is fixed here under a pair and must prove non-empty bullets; a product cause goes to a CRO brief." The issuer's
offline candidate cause (reproduced with the installed SDK 0.45.0, no network): `client.messages.create(..., betas=[...])` raises `TypeError`
because `messages.create` has no `betas` parameter; it is the candidate this logging will confirm or refute on the deployed layer. Deploy and the
measuring dry run are `FB-j-10` (staged). Class WORLD by the path floor (a Lambda code path), though this cell deploys nothing.

<status>pending</status>
<round>7</round>
<workstream>SLOTDROPLOG</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-9</to_id>
<slot>~73</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
