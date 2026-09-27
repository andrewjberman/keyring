# Never-widen sign-off packet -- irpt-export-render: async submit, and rejected prose withheld

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~19:4xZ.
**Rulings:** 1.0.0_SA_CTO 102026 (both items, one change) and 102031 ((a) self-invoke, conditions 1-4).
**Ledger (opened before any write):** `irpt-export-async-submit-20260927` @57be4b1349 (U1 closed; D1, A1 open).

## 1. What window 17 found (ledger ca5ae4f5ea)

The export's ONE POST passed the reopen-rule authorizer and then failed in the narrative packet build after 60.4 s. The
gateway had already answered 503 at 29.3 s. Nothing was written. Two defects:
- The template quotes news headlines verbatim, and two of them carry causal words ("because", "fueled by"). The
  validator REJECTED the prose, but `build_packet` kept the rejected text and `asserts_causation=true` in the packet.
  The schema raised, and only `ValidationUnavailable` was caught.
- The submit ran the whole flow inside the request: 60 s against the gateway's 29 s.

## 2. The change

**Item 1 (backend ac4eb443b3; publish 1b8ead8cbf)**, accepted by CTO 102031:
- On REJECTED, the rejected text leaves the packet. The prose slot carries `prose.REFUSAL_TEXT` ("No narrative is
  released for this report: ..."), with no citations, the REJECTED status kept, and its two flags MEASURED by the same
  validator on the refusal, never typed. The rejected text and its reasons stay in the envelope, off the bound packet.
- A schema violation is answered by name (`contract_validated: false`, `contract_failure`), never raised.
- The live topic store reads each date once: 412 s -> 263 s locally on RPT-b5e0a16e's 46 events and 189 dates.

**Reading of 102026 item 1, stated rather than assumed:** the contract requires `prose.text` (a string) and
`states_contemporaneity` const true. So "the packet drops its text" is met by replacing the rejected text with the fixed
refusal, not by an empty string. An empty string would fail `states_contemporaneity`, or would need that flag typed
true. The page (`PeriodInContextPage.tsx`) renders the slot's text as one note, so the section shows "no narrative
released", not narrative. Withholding is recorded in the envelope's `prose_validation` and `prose_released: false`.

**Item 2 (backend f3995c0d31; publish e8b32494c9)**, conditions 1-4 of 102031:
- **POST** (`submit_async.accept`): resolve the ONE retained report under the current principal, then validate the
  render grant. Write `firms/<firm>/generations/<exr>/pending.json` with stage BUILDING, invoke the function ONCE with
  `InvocationType=Event` and a MARKED event, and answer QUEUED with the `exr_` revision. The portal already treats
  `status.operation.revision` as an opaque export id (`export/submit.ts:369-371`), so there is no portal change.
- **Async leg** (`submit_async.run`): the unchanged `serve_submit` under the carried principal and scope. It
  re-resolves the report and re-checks the grant. The pointer then goes to SUBMITTED with the EXP id. ANY exception
  writes FAILED with the exception class as its reason, then propagates (condition 2).
- **Receipt route:** an `exr_` handle reads the pointer, after the viewer's CURRENT scope is checked against the
  pointer's accounts:
  - BUILDING: NOT_READY.
  - BUILDING older than the build window (the function timeout, 120 s from the new env var, plus 60 s): FAILED /
    TIMED_OUT (condition 3).
  - FAILED: DEPENDENCY_UNAVAILABLE.
  - SUBMITTED: continues exactly as an EXP id did before.
- **One hop** (condition 4): `accept` refuses inside a marked event, and `run` refuses without a BUILDING pointer. So a
  replayed event does nothing. The marked event is reachable only by a direct `lambda:Invoke`: the API Gateway wraps
  every HTTP request in its own event shape, so a browser body cannot set a top-level key.
- **Terraform:** `aws_lambda_function_event_invoke_config` with retries 0 and event age 60 s (condition 1);
  `lambda:InvokeFunction` on the function's OWN ARN only; Get/Put on `generations/exr_*/pending.json`; the timeout is
  one local, passed to the env.

**Tests:**
- narrative 40 passed (3 new); export 117 passed (9 new in `test_submit_async.py`).
- Negative controls: the 3 narrative tests fail on HEAD, the first with W17's exact error; the 6 entry-level async
  tests fail on HEAD's entry.py.

## 3. The artifact and the move

| | live | new |
|---|---|---|
| irpt-export-render CodeSha256 | `3EST/hewG..` (S3 version te7rGPXk.) | `8nkjGpT0..` (S3 version kN5tj1K0.) |

- **Census:** 58 -> 59 members. Changed: entry.py, narrative_build.py, evidence.py and prose.py. Added:
  submit_async.py. Removed: none.
- **Flat extract-and-import:** passed.
- **Dry plan** (export root, backend worktree f3995c0d31): **1 to add, 2 to change, 0 to destroy**:
  - the event-invoke-config (created);
  - the submit policy: +1 resource (pending.json), +1 statement (self-invoke);
  - the function: code (s3_object_version, source_code_hash) and one env var `IRPT_EXPORT_FUNCTION_TIMEOUT_S=120`.
- **Rollback, per key:**
  - Re-apply the export root at backend ac4eb443b3's Terraform, which is f92445392d's. That removes the invoke-config,
    the self-invoke statement, the pending.json grant and the env var, with the code at S3 version te7rGPXk.
    (3EST/hewG), the pattern of every prior export deploy.
  - An `exr_` handle issued before a rollback then reads NOT_FOUND on the old receipt route, and its pointer object
    stays in place, orphaned and holding ids only.

## 4. Blast radius -- both branches of every producer rule

- **submit-export's answer.** Before: the whole submission in the request, which fails at 60 s / 503 for a report
  with RPT-b5e0a16e's event count. After: QUEUED with an `exr_` revision after resolve and grant validation.
  - Refused before any write, exactly as today: out-of-scope callers, a report the caller may not read, and a grant the
    delegator cannot carry. Test: `test_a_caller_out_of_scope_is_refused_before_any_write`.
- **What gets written.** The async leg writes exactly what the synchronous submit wrote (packet, bundle, grant, the EXP
  pending pointer, the render dispatch), plus ONE new object per submit: the `exr_` pointer.
- **Writers of the new pointer:** N = 2, `accept` (BUILDING, or FAILED on an invoke failure) and `run` (SUBMITTED or
  FAILED).
- **Prose.** VALIDATED: released exactly as today. REJECTED: withheld, and the refusal text is bound instead. Nothing
  else in the packet changes.
- **Receipt route.** EXP ids answer exactly as today. `exr_` ids are new and read only under the bound firm's prefix,
  after the scope check.
- **Reachable now:** only a signed-in export POST, which today means the walk windows only. No existing export record
  changes.

## 5. Proof arms -- the NEXT K8 window (ledger A1, and the reopen-rule ledger's open A1)

1. ONE POST answers QUEUED with an `exr_` revision in under 29 s.
2. The pointer goes BUILDING -> SUBMITTED, with the EXP id.
3. The receipt goes NOT_READY -> READY with a %PDF on the served object, or a named FAILED.
4. The render grant and the receipt name THIS window's principal. This is the reopen rule's arm 4, now reachable.
5. The owner row is unchanged (arm 3), and nothing is written outside the export's write set.

**On an arm failing:** roll back per section 3 in the same turn, before any other export.

## What the halves sign against

This file's committed blob; backend ac4eb443b3 + f3995c0d31 (publish 1b8ead8cbf + e8b32494c9); artifact 8nkjGpT0 at
S3 version kN5tj1K0 with its 1/2/0 plan and rollback; the reading of 102026 item 1 in section 2; and the five arms in
the next K8 window.
