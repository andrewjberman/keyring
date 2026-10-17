# TO IRPT_DASHBD.TO-DB-f-2602 -- the INFLECTION LAUNCHER'S BOUNDED DEFAULT, ONE cell: without `--since`, `INF_G_01.account_transaction_gold.py` writes only the business days after the newest day already written at the target prefix, the 25 newest of them at most; an empty target takes the cap, an up-to-date target writes nothing; an explicit `--since` keeps its meaning (the CTO's RULING B, msg 10145)

<to_id>IRPT_DASHBD.TO-DB-f-2602</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2602</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>F2BOUND</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2BOUND (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 10145 (item 4 RULED B: "The nightly block's default writes only the trading days after the newest written partition, capped at 25. It never writes the whole history, and it writes nothing when it is up to date. A test covers an empty prefix, which takes the cap and not 2020 onward. The first range stays the 25-day --since run under SSM (XA-a222). Earlier history is a later act on my word, in runs of 25.") | **Decomp cell:** `DB-f-2602` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md`, "Cell 2") | **outcome_ref:** FWD-5 | **depends_on:** none (the launcher is on the trunk).

**Risk class LOCAL:** repo text and offline tests in a branch. No AWS call, no Terraform, no upload, no push. The bundle manifest and its pin are NOT yours and not touched (the launcher is not a bundle member).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2602` (branch `wk-IRPT_DASHBD-2602`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2602/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS: make no AWS call.** No client data is read or recorded (the tests use made-up accounts and symbols). Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** Today `run()` in the launcher writes EVERY business day of the one snapshot when `--since` is absent (for the real snapshot, the whole history), and the dispatch script's best-effort block calls the launcher without `--since` each night. The CTO ruled the default bounded.

**The cell (`DB-f-2602`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_bounded.py` (your three criteria; the scenarios are the exact spec; it has a `--selftest`); the launcher `data/inf/scripts/gold/INF_G_01.account_transaction_gold.py` (whole); its test file `data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py` (the `FakeS3`, `line`, `put_partition`, `emitted` helpers); and `data/assets/scripts/gold/irpt_reporting/account_transaction_inflection.py` lines 316 to 351 (`emit_transaction_day`: the target address is `opal_naming.address("irpt", firm, "gold", TABLE_TRANSACTION, "date=<day>")`; it puts `<key>/data.parquet` and THEN `<key>/manifest.json`).
2. **The edit: the launcher only** (one file), ASCII, no new dependency:
   - `DEFAULT_CAP = 25` (a module constant).
   - `newest_written_day(s3)`: the newest `date=YYYY-MM-DD` partition at the target table prefix that holds a `manifest.json` object (the writer puts it LAST, so a partition with only `data.parquet` is not counted), or `None` when the prefix holds none. The bucket and prefix come from the producer's builder address (`opal_naming.address` through the producer module, exactly as the producer builds it); **never type a bucket or a prefix**. List with the client's `get_paginator("list_objects_v2")` (as `newest_partition` does).
   - In `run(s3, run_day, upload=True, since=None)`: when `since` is None, emit only the business days of the plan that are AFTER `newest_written_day(s3)` (all of them when it is None), and of those only the `DEFAULT_CAP` newest. When `since` is given, behave exactly as today (every business day from it, no cap). `check_no_repeat` stays over the FULL plan, before the window is applied. The summary keeps `rows_in` and `rows_planned` over the full plan, `days` and `rows_out` the days actually written (or that a dry run would write), and gains `window` {`newest_written` (the day or null), `cap`, `days_pending` (the count of plan days after the newest written, before the cap)}. A dry run (`upload=False`) reads the same window and makes no `put_object` call.
   - `main()`: the `--since` help text says what it now is (an explicit range start that lifts the cap); the printed `summary:` line gains `window=<json>`. Nothing else in `main` changes.
3. **The tests: the launcher test file gains tests** (offline, `FakeS3`), at least: an empty target with more than 25 plan days writes exactly the 25 newest; a target written through W writes only the days after W; more than 25 pending writes the 25 newest only; an up-to-date target writes nothing and makes no `put_object` call; a partition holding only `data.parquet` (no manifest) is not counted as written; an explicit `--since` writes every day from it with no cap; a dry run writes nothing and reports the same window; `check_no_repeat` still refuses a repeat that sits in a day the window dropped.
4. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_bounded.py" . DBF138-2-AC1`, then `AC2`, then `AC3`; and `python -m pytest data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py -q -p no:cacheprovider`. **The baseline on the trunk before your edit is 2 failed and 7 errors, 49 passed**: they are the bundle tests (two bundle members, `infra/logic/registry/exemptions.json` and `lib/opal_naming.py`, drifted from the manifest, so `build_bundle` refuses); they are NOT yours, you neither fix nor worsen them. Your tests must all pass, and the set of failing or erroring test ids after your edit must equal the baseline's. Record the baseline ids and the after ids in `RD_BOUNDED_DEFAULT_FACTS_R138.json` with `claim` ("measured"), `tests_added` (the count), `failing_before`, `failing_after`, `files_touched` (2).
5. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2602 <0.9.0_WK_IRPT_DASHBD~2602@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool), the launcher and the test file in one commit, the record and proof in a second.

<criterion id="DBF138-2-AC1" cell_refs="DB-f-2602" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_bounded.py" . DBF138-2-AC1</invocation><expect>DBF138-2-AC1 PASS</expect></criterion>
`DBF138-2-AC1` -- an EMPTY target, no `--since`: `run()` and `main()` write exactly the 25 newest business days and nothing earlier. Base: FAIL (it writes every day).
<criterion id="DBF138-2-AC2" cell_refs="DB-f-2602" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_bounded.py" . DBF138-2-AC2</invocation><expect>DBF138-2-AC2 PASS</expect></criterion>
`DBF138-2-AC2` -- a target with a newest written day W: only the days after W are written, the 25 newest when more are pending, nothing when W is the newest day. Base: FAIL (an up-to-date target is written again).
<criterion id="DBF138-2-AC3" cell_refs="DB-f-2602" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_bounded.py" . DBF138-2-AC3</invocation><expect>DBF138-2-AC3 PASS</expect></criterion>
`DBF138-2-AC3` -- an explicit `--since` still writes every business day from it with no cap, and a dry run with no `--since` makes no `put_object` call yet reports the same bounded days. Base: FAIL (a dry run reports every day).

<expected_criteria>DBF138-2-AC1, DBF138-2-AC2, DBF138-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer modules, the bundle manifest and zip, the dispatch script, the registry, the contract, the checker.
- **AWS: none; no Terraform; no push.** No change to the manifest `INF_G_01.bundle.json`, to `EXPECTED_BUNDLE_SHA256` or to any bundle member.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker or an order sentence is wrong, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2602-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES (the file may hold non-ASCII from other rows). **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2602/
data/inf/scripts/gold/INF_G_01.account_transaction_gold.py
data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2602.inflection-launcher-bounded-default-window.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md</decomp_doc> round 138, workstream F2BOUND (F-SHIP), cell `DB-f-2602`.
<owned_cells>DB-f-2602</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF138-2-AC1, DBF138-2-AC2, DBF138-2-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2602/IRPT_DASHBD.TO-DB-f-2602.inflection-launcher-bounded-default-window.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2501/IRPT_DASHBD.TO-DB-f-2501.inf-pipeline-runner-account-transaction-scoped-policy.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF138-2-AC1,DBF138-2-AC2,DBF138-2-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the pytest line and the before/after failing ids; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the edit is one launcher function path and its tests; the launcher's readers are the dispatch script's best-effort block (read by the issuer in round 135) and the by-hand release runs, and no deploy is made in this order.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM object is changed here. The issuer found that the default needs s3:ListBucket on the gold prefix, which the runner policy of DB-f-2501 does not grant; that is put to the CTO as a separate ask and a later cell, not this one.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed; nothing is deployed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF138-2-AC1 to AC3 FAIL at base, a reference implementation put into the launcher by the issuer made all three PASS and was reverted, and the checker's pure helpers are exercised by its selftest (7 arms).
lane: the <paths> block IS the grant.
</preflight>
