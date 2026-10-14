# ADVI_FIRMBKTS task order -- `FB-m-1` -- THE READINESS HALT IN THE INFLECTION PORTAL PUBLISHER (A GUARD THAT PUBLISHES ONLY WHEN THE DAY'S GOLD IS COMPLETE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_READYHALT.md</decomp_doc>
<owned_cells>FB-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~84</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cell edits publisher code and tests only; no rule, schedule or cadence is added or changed (the floor schedule is a separate order).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM file is edited; whether the function's role can read the chosen signal key is read at deploy time by the deploying seat (`FB-m-2`), which stops if it cannot.
comp-adversary: RUN by the issuer -- at base the test file does not exist (AC1 FAIL) and the file is unchanged (AC2 FAIL, zero inserts); the graders reject a changed or removed existing line, more than 120 inserted lines, a test file with fewer than three passing tests, and (for the signal record, read by the issuer) a signal that is the Door 6 marker. Blindness: the tests use faked clients, so they prove the guard's logic and zero-write discipline, not that the signal reads right against the live bucket; `FB-m-2` reads the arms live.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-m-1` (round 8, workstream READYHALT: the publisher's readiness halt, CTO condition C4)

The Inflection portal publisher is the Lambda `inf-portal-publisher` (source `infra/aws/lambda/inf-portal-publisher/lambda_function.py`). Today an S3 notification starts it when the gold chain writes `gold/meta/pipeline-complete.json` in `opal-data-inf` (the "Door 6 marker", which is being RETIRED). The publisher takes NO input from its event: `lambda_handler` (line 915) first invokes the advisor publisher asynchronously (`ADVISOR_PUBLISHER_FUNCTION`, lines 924-935), then loads whatever gold and silver parquets are in the bucket at that moment (`load_all`, line 173), writes the three firm snapshots under `platinum/firm/snapshots/`, and invalidates CloudFront. It never checks that the day's gold is complete: the marker's existence was the check. The marker is going away and the publisher is about to be started by a clock (an EventBridge Scheduler schedule) instead, so the publisher itself must refuse to publish unless the gold chain has finished for the day. The 49 Financial publisher the Inflection one copies does this with a "conditional self-halt" (`infra/aws/terraform/opal-assets/advi_49f_publisher.tf:15-17`).

### 1a. Your slice

1. **Find the readiness signal (read-only).** Read `data/inf/scripts/gold/orion-gold-dispatch.sh` (it writes the marker at about line 1889; it derives `RUN_DATE`; `check_freshness` at about line 500 reads
   `gold/artifacts/header_metrics.json` field `data_as_of`; the pull-stage sentinel `gold/meta/pull-complete.json` is written at about line 1860; `gold/meta/pipeline-failed.json` on failure; the eclipse status is
   `gold/eclipse/_meta/dispatch_eclipse_status.json`) and the step scripts it runs. Choose ONE object in `opal-data-inf` that the FULL gold chain writes, that carries the date of the gold it describes, that is
   written by ONE script only (the "single writer"), that survives the marker's retirement, and that is NOT `gold/meta/pipeline-complete.json` and NOT `gold/meta/pull-complete.json` (written before compute). Read ONE live copy
   of it (`aws s3 cp s3://opal-data-inf/<key> -` for a small JSON; never a parquet body) to see its real fields. Write `READINESS_SIGNAL.json` and `READINESS_SIGNAL.md` (below). If no object qualifies, file a
   BLOCKING row saying which candidates you read and why each fails, write the two files with `chosen` null, and STOP: you do NOT edit the dispatch script (it is not in your paths).
2. **The date the guard checks.** The gold chain's `RUN_DATE` derivation is the truth for "that day's gold". Read how `orion-gold-dispatch.sh` derives `RUN_DATE` and mirror it in the guard (cite the line). Do not import
   `lib/trading_calendar.py` (the Lambda does not carry `lib/`). An optional event field `readiness_date` (YYYY-MM-DD) replaces the derived date, ONLY to choose which date is checked (it is how the live arm test supplies a date
   whose gold is incomplete); with no event field the derived date is used.
3. **Implement the guard in `lambda_function.py`, purely additive.** Add a helper `_gold_ready(expected_date)` and ONE call at the very top of `lambda_handler`, BEFORE the advisor fan-out (the fan-out writes too). When the signal's date
   is not the expected date, or the signal object is absent or unreadable, the handler: prints exactly one line `READINESS HALT: date=<expected_date> signal=<key> reason=<short reason>`, returns
   `{"statusCode": 200, "halted": True, "date": "<expected_date>"}`, and does NOTHING else: no advisor invoke, no S3 put, no CloudFront call. When the signal is ready the handler proceeds exactly as today. No existing line of
   the file changes or is removed (a grader compares against the pinned base blob), and the file gains at most 120 lines. A read error of the signal is a halt, never a pass (fail closed).
4. **Tests.** Write `infra/aws/lambda/inf-portal-publisher/tests/test_readiness_halt.py`, exactly three tests, using `unittest.mock` to fake the module's boto3 clients (no network, no moto): `test_complete_publishes`
   (signal ready: the existing path runs; assert the advisor invoke and the snapshot put are attempted), `test_incomplete_halts_zero_writes` (signal one day old: assert NO s3 put, NO lambda invoke, NO CloudFront call and the
   return value has `halted` true), `test_halt_log_names_date_and_signal` (the one log line contains the expected date and the signal key). If importing the module needs `pandas` or `boto3` that the sandbox lacks, stub them in
   `sys.modules` before the import inside the test file.

### 1b. The signal record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.json`

```json
{"order": "FB-m-1", "read_at": "<ISO UTC>", "chosen": {"key": "<object key in opal-data-inf>", "date_field": "<the field that carries the gold date>", "writer": "<script>:<line>", "single_writer": true,
  "means": "<why this object existing for date D means gold is complete for D>", "part_written_reads": "<what it reads while the chain is part-written>", "claim": "measured|inferred|held|absent"},
 "candidates_read": [{"key": "<key>", "verdict": "chosen|rejected", "reason": "<one line>"}],
 "run_date_derivation": "<script>:<line>: <how RUN_DATE is derived>", "not_read": ["<each thing you could not read, and why>"], "claim": "measured"}
```

Also write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.md` (one page: the chosen object and why, the candidates rejected, the date derivation, what the guard does on each arm).

## 2. BOUNDS

1. READ verbs only on AWS (`.tools/aws`, `aws s3 cp <key> -` for one small JSON, `head-object`, `list`). No write to AWS, no deploy, no `terraform`, no invoke of any Lambda, no edit of the dispatch script or any file outside
   section 3. Print no client name, secret or relationship id (write `<id>`).
2. The guard changes `lambda_handler` only by an added call at its top and adds helper code; the `build_*`, `load_*` and `_save_json` functions and every existing line stay byte-identical.
3. Tests fake every AWS client; no test touches the network. Each command is bounded (`timeout 120`).

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/
infra/aws/lambda/inf-portal-publisher/lambda_function.py
infra/aws/lambda/inf-portal-publisher/tests/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/ADVI_FIRMBKTS.TO-FB-m-1.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-m-1"><invocation>cd C:/dev/wk-firmbkts-84 &amp;&amp; timeout 120 python -m pytest infra/aws/lambda/inf-portal-publisher/tests/test_readiness_halt.py -q</invocation><expect>^3 passed</expect></criterion>
  <criterion id="AC2" cell_refs="FB-m-1"><invocation>cd C:/dev/wk-firmbkts-84 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py guarddiff --root C:/dev/wk-firmbkts-84 --file C:/dev/wk-firmbkts-84/infra/aws/lambda/inf-portal-publisher/lambda_function.py --base-blob 371eb01b42e5c1e4f6ce1c8ddac20071c0636762</invocation><expect>^GUARDDIFF: OK inserted=[0-9]+ changed=0$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-m-1"><invocation>cd C:/dev/wk-firmbkts-84 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root C:/dev/wk-firmbkts-84 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/ --allow infra/aws/lambda/inf-portal-publisher/lambda_function.py --allow infra/aws/lambda/inf-portal-publisher/tests/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 runs the three arms against faked clients; AC2 proves the guard is purely additive against the pinned base blob of the file; AC3 is the write-surface bound. Whether the signal reads right on the live bucket is read at deploy by `FB-m-2`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/ADVI_FIRMBKTS.TO-FB-m-1.proof_of_spec.json`. Commit the code, the tests and the two signal files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W84-S<k>`, `k` from 1,
`surfaced_at` from `date -u +%FT%TZ`. Report once: the chosen signal key and its single writer, the date derivation, the number of inserted lines, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** workstream READYHALT, a separate scope from round 8's frozen decomposition (CLAUDE.md rule 27), cut on the CTO half's condition C4 (`ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_CTO_HALF.md` @1709a6e779, msg 5536): before act 3 of `FB-l-5` the floor gains the 49 Financial shape's readiness halt, a signal that is NOT the Door 6 marker, arms complete / incomplete / logged reason. The form chosen here is the CTO's first option, a guard in the publisher, which needs its own pair at deploy (`FB-m-2`). Class WORLD by the path floor (`infra/aws/**`); the cell deploys nothing.

<status>pending</status>
<round>8</round>
<workstream>READYHALT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-m-1</to_id>
<slot>~84</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
