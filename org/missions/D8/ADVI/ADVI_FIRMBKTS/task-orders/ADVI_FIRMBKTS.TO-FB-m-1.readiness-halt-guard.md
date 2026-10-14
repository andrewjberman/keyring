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
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM file is edited; the guard reads only objects the function already reads (its dated inputs and its own served snapshots), so no grant changes.
comp-adversary: RUN by the issuer -- at base the test file does not exist (AC1 FAIL) and the file is unchanged (AC2 FAIL, zero inserts); the graders reject a changed or removed existing line, more than 120 inserted lines and a test file with fewer than six passing tests; the issuer reads the signal record against the CTO's three conditions. Blindness: the tests use faked clients and loaders, so they prove the guard's logic and zero-write discipline, not that the frontier reads right against the live bucket; `FB-m-2` reads the arms live.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-m-1` (round 8, workstream READYHALT: the publisher's readiness halt, CTO condition C4)

The Inflection portal publisher is the Lambda `inf-portal-publisher` (source `infra/aws/lambda/inf-portal-publisher/lambda_function.py`). Today an S3 notification starts it when the gold chain writes `gold/meta/pipeline-complete.json` in `opal-data-inf` (the "Door 6 marker", which is being RETIRED). The publisher takes NO input from its event: `lambda_handler` (line 915) first invokes the advisor publisher asynchronously (`ADVISOR_PUBLISHER_FUNCTION`, lines 924-935), then loads whatever gold and silver parquets are in the bucket at that moment (`load_all`, line 173), writes the three firm snapshots under `platinum/firm/snapshots/`, and invalidates CloudFront. It never checks that the day's gold is complete: the marker's existence was the check. The marker is going away and the publisher is about to be started by a clock (an EventBridge Scheduler schedule) instead, so the publisher itself must refuse to publish unless the gold chain has finished for the day. The 49 Financial publisher the Inflection one copies does this with a "conditional self-halt" (`infra/aws/terraform/opal-assets/advi_49f_publisher.tf:15-17`).

### 1a. Your slice

The CTO RULED the readiness signal (msg 5552): it is the DATA FRONTIER, read from CONTENT, not any marker or sidecar. A first attempt of this cell found that no object the gold chain writes can serve (the marker and pull sentinel are excluded; `gold/artifacts/header_metrics.json` is absent live; `gold/eclipse/_meta/dispatch_eclipse_status.json` is classed TRASH-as-gate in `docs/architecture/MDPF_REMEDIATION_REGISTER.md:198,226`; a new chain object would be a successor marker, which Andrew ruled out). Its records are inherited state: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.md` (read it). **A SECOND ATTEMPT built the guard and its five tests (merged as dea0a491ae; they are in your tree). This is a THIRD, SMALL CHANGE to that guard and those tests:** a live read showed that the newest canonical NNA partition lags the holdings by a business day (partitions follow business days: 2026-10-14 holdings, newest NNA 2026-10-13), so a rule requiring all three dated inputs to read the same date would halt every normal day. The CTO amended the rule (msg 5571); items 2, 3 and 5 below are the amended text. Edit your merged guard and tests to it; do not rewrite them.

1. **The frontier.** Read, in `lambda_function.py`, how the publisher loads its inputs (`load_all`, line 173; `_load_parquet`, line 82; `_load_parquet_prefix_latest`, line 92; `_load_canonical_nna_all`, line 106) and which keys they read. The DATED inputs are exactly three: client performance (`CLIENT_PERF_KEY`, its `date` column), the latest holdings file under `GOLD_HOLDINGS_PREFIX` (its `date` column), and canonical NNA (the latest `canonical_nna_{date}.parquet` partition; its `date` column). Their frontier date is the MAXIMUM of the date column, read from CONTENT (read only the `date` column with the existing `_load_parquet(key, columns=['date'])`; never the whole table; for NNA read the newest partition only). The undated dimensions (`accounts_dim`, `account_team`, `household_dim`) are EXCLUDED and named as excluded in your record.
2. **The rule (the CTO's amended conditions).** Publish only when `holdings` and `client_perf` both read the SAME date D, D is greater than the served snapshots' `data_as_of` (read it from the existing `platinum/firm/snapshots/aua_by_*.json` objects, as your merged guard already does), AND the newest `canonical_nna` partition's date N satisfies D minus 4 calendar days <= N <= D (NNA partitions follow business days, so it may lag D by a weekend and a holiday but not more). Otherwise HALT with zero writes, and the halt line prints all three dates.
3. **Five arms, as unit tests:** (i) holdings and client_perf at D, D greater than the served date, NNA one day behind D: publish; (ii) holdings OR client_perf one day behind the other (split): halt (the part-written-gold case); (iii) holdings and client_perf at D but D equal to the served date (a same-day re-fire): halt; (iv) the served `data_as_of` absent (no snapshot object yet): publish once (the publish itself stamps the date); (v) NNA five calendar days behind D: halt. A read error of any input or of the served object is a halt, never a pass, EXCEPT arm (iv)'s absent served object (a missing snapshot object is the only absence that does not halt).
4. **Implement the guard in `lambda_function.py`, purely additive.** Add helper code (for example `_dated_frontier()` and `_gold_ready()`) and ONE call at the very top of `lambda_handler`, BEFORE the advisor fan-out (the fan-out writes too). On a halt the handler prints exactly one line `READINESS HALT: <input>=<date> <input>=<date> <input>=<date> served=<date or absent> reason=<short reason>` NAMING EACH INPUT'S DATE, returns `{"statusCode": 200, "halted": True}`, and does NOTHING else: no advisor invoke, no S3 put, no CloudFront call. When ready, the handler proceeds exactly as today. No existing line of the file changes or is removed (a grader compares against the pinned base blob), and the file gains at most 120 lines. There is NO event override and no calendar.
5. **Tests.** Edit `infra/aws/lambda/inf-portal-publisher/tests/test_readiness_halt.py` to exactly SIX tests, using `unittest.mock` to fake the module's boto3 clients and loaders (no network, no moto): `test_all_at_d_publishes` (arm i, NNA one day behind D: assert the advisor invoke and the snapshot put are attempted), `test_one_input_behind_halts_zero_writes` (arm ii, holdings or client_perf split: NO s3 put, NO lambda invoke, NO CloudFront call, `halted` true), `test_same_day_refire_halts` (arm iii, same zero-write assertions), `test_served_absent_publishes` (arm iv), `test_nna_five_days_behind_halts` (arm v, same zero-write assertions), `test_halt_log_names_each_input_date` (the one log line contains the three input names and their dates). The sandbox stubs from the earlier attempt stay.

### 1b. The signal record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.json`

```json
{"order": "FB-m-1", "read_at": "<ISO UTC>", "ruling": "CTO msg 5552: the data frontier from content",
 "dated_inputs": [{"name": "client_perf", "key_or_prefix": "<key>", "date_column": "date", "loader": "lambda_function.py:<line>", "claim": "measured|inferred|held|absent"},
                  {"name": "holdings", "key_or_prefix": "<prefix>", "date_column": "date", "loader": "lambda_function.py:<line>", "claim": "measured|inferred|held|absent"},
                  {"name": "canonical_nna", "key_or_prefix": "<prefix>", "date_column": "date", "loader": "lambda_function.py:<line>", "claim": "measured|inferred|held|absent"}],
 "excluded_undated": ["accounts_dim", "account_team", "household_dim"],
 "served_date": {"object": "platinum/firm/snapshots/aua_by_*.json", "field": "data_as_of", "written_at": "lambda_function.py:<line>", "claim": "measured|inferred|held|absent"},
 "not_read": ["<each thing you could not read, and why>"], "claim": "measured"}
```

Also write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.md` (one page: the three dated inputs and the excluded dimensions, how the served date is read, the NNA tolerance and why (cite the live partition names you read), what the guard does on each of the five arms). Overwrite the earlier `READINESS_SIGNAL.json` and `.md` of this folder.

## 2. BOUNDS

1. READ verbs only on AWS (`.tools/aws`, `aws s3 cp <key> -` for one small snapshot JSON, `head-object`, `list`; never a parquet body). No write to AWS, no deploy, no `terraform`, no invoke of any Lambda, no edit of the dispatch script or any file outside
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
  <criterion id="AC1" cell_refs="FB-m-1"><invocation>cd C:/dev/wk-firmbkts-84 &amp;&amp; timeout 120 python -m pytest infra/aws/lambda/inf-portal-publisher/tests/test_readiness_halt.py -q</invocation><expect>^6 passed</expect></criterion>
  <criterion id="AC2" cell_refs="FB-m-1"><invocation>cd C:/dev/wk-firmbkts-84 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py guarddiff --root C:/dev/wk-firmbkts-84 --file C:/dev/wk-firmbkts-84/infra/aws/lambda/inf-portal-publisher/lambda_function.py --base-blob 371eb01b42e5c1e4f6ce1c8ddac20071c0636762</invocation><expect>^GUARDDIFF: OK inserted=[0-9]+ changed=0$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-m-1"><invocation>cd C:/dev/wk-firmbkts-84 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root C:/dev/wk-firmbkts-84 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/ --allow infra/aws/lambda/inf-portal-publisher/lambda_function.py --allow infra/aws/lambda/inf-portal-publisher/tests/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 runs the five arms and the log line against faked clients; AC2 proves the guard is purely additive against the pinned base blob of the file; AC3 is the write-surface bound. Whether the frontier reads right on the live bucket is read at deploy by `FB-m-2`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/ADVI_FIRMBKTS.TO-FB-m-1.proof_of_spec.json`. Commit the code, the tests and the two signal files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W84-S<k>`, `k` from 1,
`surfaced_at` from `date -u +%FT%TZ`. Report once: the three dated inputs and the served-date field, the number of inserted lines, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-14 ~13:3xZ):** worker ~84's first attempt applied the STOP branch (merged 53e2f3bae5; no chain-written object qualifies; BLOCKING row D1-W84-S1). The CTO RULED the signal (msg 5552): (b) the data frontier read from content of the three dated inputs, publish only when all read the same D and D exceeds the served `data_as_of`, four arms; (a) a new chain object is refused under Door 6, (c) the eclipse status under the register. The face is rewritten to that ruling; AC1 is now five tests. D1-W84-S1 is disarmed on this cut (its premise, no signal, is resolved by the ruling). Gate limb: none graded (no criterion changed except AC1's expected count, the issuer's own amendment).

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-14 ~13:4xZ):** worker ~84's second attempt built the guard (merged dea0a491ae; AC1-AC3 re-run by the issuer). A live read (holdings 2026-10-14, newest canonical NNA 2026-10-13, 10-10 to 10-12 absent; row D1-W84-S4) showed the CTO's condition that all three dated inputs read the same D halts every normal day. The CTO amended it (msg 5571): D = holdings = client_perf; NNA at most 4 calendar days behind D; arm (v) NNA five days behind halts. The face is edited to it; AC1 is now six tests. D1-W84-S4 is disarmed on this cut. Gate limb: none graded (no criterion changed except AC1's expected count, the issuer's own amendment).

**ISSUER NOTES:** workstream READYHALT, a separate scope from round 8's frozen decomposition (CLAUDE.md rule 27), cut on the CTO half's condition C4 (`ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_CTO_HALF.md` @1709a6e779, msg 5536): before act 3 of `FB-l-5` the floor gains the 49 Financial shape's readiness halt, a signal that is NOT the Door 6 marker, arms complete / incomplete / logged reason. The form chosen here is the CTO's first option, a guard in the publisher, which needs its own pair at deploy (`FB-m-2`). Class WORLD by the path floor (`infra/aws/**`); the cell deploys nothing.

<status>pending</status>
<round>8</round>
<workstream>READYHALT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-m-1</to_id>
<slot>~84</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
