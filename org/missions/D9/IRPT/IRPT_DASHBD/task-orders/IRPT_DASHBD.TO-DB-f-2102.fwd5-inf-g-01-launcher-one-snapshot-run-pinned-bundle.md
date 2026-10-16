# TO IRPT_DASHBD.TO-DB-f-2102 -- the FWD-5 INF_G_01 LAUNCHER, ONE CELL: a thin gold script that reads ONE Orion snapshot per run, emits the Inflection account-transaction lines by business date with no source line on two days, reports S6, and ships the producer closure as ONE pinned, deterministic bundle zip

<to_id>IRPT_DASHBD.TO-DB-f-2102</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2102</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>135</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2: msg 9486 (the Inflection producer is a step in the Orion gold dispatch chain) and msg 9625 (the producer "must read ONE snapshot (the newest partition for the run day) and emit lines by their trade date", with "a criterion: no source line appears on more than one emitted day, counted over the full output"); msg 9669 (S6: 96 of 96 events carry an equal-amount line, printed) | **Rows:** IRPT_DASHBD-D2-W2102-S<k> | **Decomp cell:** `DB-f-2102` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R135_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** `DB-f-2101` (the bundle pins the bytes of `transaction_words.json`, which 0.5.1 changes: you are cut your worktree from the trunk AFTER 2101 merged)

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2102` (branch `wk-IRPT_DASHBD-2102`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2102/`. The folders `org/standards`, `lib`, `data/assets/scripts/gold/irpt_reporting`, `data/assets/scripts/lib`, `data/inf`, `infra/logic` and `org/missions/D9/IRPT/IRPT_DASHBD/deliverables` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. Offline tests only (synthetic frames, a fake S3 client; `upload=False` where a dry run is meant). **You have NO AWS in this order: make no AWS call of any kind.** No real client, household or account id, no client figure and no security name anywhere; test accounts, symbols and product names are made up.

**Why.** The Orion gold dispatch chain syncs `code/gold` (and three other prefixes) FLAT by basename into one directory, then runs each catalog script. The Inflection producer (`account_transaction_inflection.py` and its closure) locates the repo by `_ROOT = _HERE.parents[5]`, so it cannot run from a flat directory. And every Orion silver `fact_transactions` partition is a CUMULATIVE SNAPSHOT of the whole history: a run must read ONE snapshot, never loop partitions as days. So the step is a thin launcher plus a pinned zip of the producer closure in the repo layout.

**The inputs (read, never edited).** The producer modules and their tests (`account_transaction.py`, `account_transaction_inflection.py`, `transaction_words.json`, `lib/trading_calendar.py`, `lib/opal_naming.py`); the adapter `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py` (its Orion silver bucket and prefix); the issuer's S6 tool `deliverables/2.0.0_SA_COO~F2/tools/inflection_s6_cash_move.py` (the definition of an S6 event and of the equal-amount line); the contract `org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json` (0.5.1, `inflection_table_shape.gold_run_domain`); the checker `deliverables/2.0.0_SA_COO~F2/checks/r135/p135_step.py` (**read it first; it states every rule and builds the fake S3 you test against; its reason lines tell you what to fix; it has a `--selftest`**).

**The cell (`DB-f-2102`), in this order; commit after each of steps 2 and 4.**

1. **The launcher** `data/inf/scripts/gold/INF_G_01.account_transaction_gold.py`, ASCII, stdlib plus what the chain's runner has (pandas, pyarrow, boto3). Module constants `ORION_BUCKET = "opal-data-assets"` and `ORION_PREFIX = "orion/inflection/silver/fact_transactions/"`. Functions (the checker calls each by name):
   - `newest_partition(s3, bucket, prefix, run_day)`: the newest `date=YYYY-MM-DD/` partition NOT AFTER `run_day`; a `SystemExit` whose message contains `partition` when none exists.
   - `read_snapshot(s3, bucket, prefix, day)`: that partition's parquet as ONE pandas frame.
   - `plan(frame)` returns `(by_day, excluded, reasons)`: the Reversed keys are derived from THIS frame (`reversed_keys_of`), the producer's `split_complete(frame, reversed_keys=...)` and mapping run on it, and `by_day` maps each BUSINESS date to its rows (a Saturday line under the Monday). `excluded` counts by status (`Rejected`, `Reversed`, ...) and `OFFSET_OF_REVERSED`.
   - `check_no_repeat(by_day)`: `SystemExit` whose message contains `repeated` if any `source_txn_id` appears on two days.
   - `emit(...)` writes each day through the producer's writer (its partition refusal and address from `opal_naming` stand), honouring `upload=False` (no `put_object`) and `since` (drop business dates before it).
   - `run(s3, run_day, upload=True, since=None)` returns `{snapshot, rows_in, rows_out, excluded, ...}`; it reads exactly ONE partition.
   - `s6_report(frame)` returns `{events, with_equal_amount_line, missing, printed}` where `printed` contains "N of M" (e.g. "1 of 2"), with the event and equal-amount-line definitions of the issuer's S6 tool.
   - `main(argv, s3=None)`: `--date`, `--upload`, `--dry-run`, `--since`; prints the S6 report and the summary; returns 0.
2. **The producers are imported lazily** (inside `plan`/`emit`, never at module import): from the repo layout when the launcher sits in the repo (`parents[3]` holds `data/assets/scripts/gold/irpt_reporting/`), otherwise from the bundle (step 3).
3. **The bundle.** `data/inf/scripts/gold/INF_G_01.bundle.json` is the manifest: `files` = `[{path, sha256}]` sorted by path, repo-relative, the closure of the producer (the checker requires `account_transaction.py`, `account_transaction_inflection.py`, `transaction_words.json`, `lib/opal_naming.py`, `lib/trading_calendar.py`; add what the imports need; NO test files), and `basename_collisions_with_synced_dirs` (the checker states the exact list: the zip is not synced flat, so a collision is recorded and harmless). The launcher carries `build_bundle(root, out_path)` (a DETERMINISTIC zip: sorted members, fixed timestamps, fixed compression and attributes; returns the zip's sha256), `EXPECTED_BUNDLE_SHA256` (the pin), and `bootstrap()`: when not in the repo layout it finds the zip at the path in env `INF_IRPT_BUNDLE_LOCAL`, else `INF_G_01.bundle.zip` BESIDE the launcher (the chain syncs code/gold flat, so the release uploads the zip with the launcher), refuses with a `SystemExit` naming `sha256` when the zip's hash differs from the pin, and only then EXTRACTS the verified zip into a fresh temporary directory in the repo layout and imports the producers from there (AMENDMENT 2: the producer's registry reads are `open()` calls, which a zip on `sys.path` cannot serve; the repo root of the launcher in the repo is `parents[4]`, not `parents[3]`; the manifest may list the registry files the naming reader opens at run time). Build the zip with `build_bundle` to a scratch path to compute the pin; do NOT commit the zip. Your repo-layout run in step 4 is on the merged trunk files, so the pin names the FINAL bytes.
4. **Tests** `data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py`: at least 30 tests with names containing `snapshot`, `repeat`, `business`, `bundle`, `reversed`, `dry`, `since` and `s6`: the newest-partition choice and its refusal, one partition read per run, the Complete lines only, a Rejected and a Reversed line and the offset of a Reversed original excluded and counted, a Saturday line under Monday, no source line twice, `since`, dry run with no put, the S6 report counts, the manifest closure and sha256, the deterministic zip (two builds equal), the pin, a tampered zip refused naming sha256, and a flat-directory run with only the launcher and the zip.
6. **The neighbouring test (AMENDMENT 1).** After 2101 merged, `data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction_inflection.py::test_row_filter_in_the_contract_is_the_issuer_census_per_status` fails: it pins the all-partition counts (218,054,352 rows) that 0.5.1 restated on the latest snapshot. It is in your grant now. Change that one test to compare the contract's `row_filter.inflection` (`rows`, `kept_rows`, `excluded_rows_per_status` and their sum) with the latest-snapshot figures of `deliverables/2.0.0_SA_COO~F2/R135_INFLECTION_SNAPSHOT_CENSUS.json` (`latest_snapshot` block: `rows`, `rows_per_status`), read from the record, never typed; change no other test and no producer. Check: the whole file passes (the checker's AC1 runs it).
5a. **Mutants** (temporary, reverted): (a) make `read_snapshot` read every partition: at least one test fails; (b) make `plan` skip `check_no_repeat`'s input (emit the same line on two days): at least one test fails. Say which test failed each.

<criterion id="DBF135-2-AC1" cell_refs="DB-f-2102" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r135/p135_step.py" . DBF135-2-AC1</invocation><expect>DBF135-2-AC1 PASS</expect></criterion>
`DBF135-2-AC1` -- the one-snapshot run, run by the checker against a fake S3 holding two cumulative snapshots: only the newest partition is read; lines are emitted under their business dates; the emitted ids are the Complete lines of that one snapshot minus the offset of the Reversed original; no source line on two days; the summary and excluded counts; the run-day choice; `since`; the dry run makes no put; `check_no_repeat`; the S6 report "1 of 2"; `main --dry-run`; at least 30 launcher tests with the named words, which pass; and (AMENDMENT 1) the whole Inflection producer test file passes on the 0.5.1 contract. Base: FAIL (no launcher).
<criterion id="DBF135-2-AC2" cell_refs="DB-f-2102" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r135/p135_step.py" . DBF135-2-AC2</invocation><expect>DBF135-2-AC2 PASS</expect></criterion>
`DBF135-2-AC2` -- the bundle, run by the checker: the manifest closes (every file present, sha256 equal to the repo file, sorted, no tests, the required modules, the collision list); `build_bundle` is deterministic and returns the zip's sha256; `EXPECTED_BUNDLE_SHA256` equals it; the zip's members are exactly the manifest's; the launcher alone in a flat directory with the zip named by `INF_IRPT_BUNDLE_LOCAL`, under `python -I` from another working directory, plans the Saturday line under Monday; a zip with a different hash is refused naming sha256. Base: FAIL (no launcher).

<expected_criteria>DBF135-2-AC1,DBF135-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every producer, the words file, `lib/`, the adapter, the contract, the issuer's tools and checkers, the dispatch script (a sibling order edits it), every Terraform file.
- **AWS: none.** **NOT WIRED.** Nothing is deployed; the catalog row, the chain and the release are other orders.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker rule and this order disagree, follow this order and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2102-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2102/
data/inf/scripts/gold/INF_G_01.account_transaction_gold.py
data/inf/scripts/gold/INF_G_01.bundle.json
data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction_inflection.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2102.fwd5-inf-g-01-launcher-one-snapshot-run-pinned-bundle.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R135_F.md</decomp_doc> round 135, workstream ~F2 (F-SHIP), cell `DB-f-2102`.
<owned_cells>DB-f-2102</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF135-2-AC1, DBF135-2-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2102/IRPT_DASHBD.TO-DB-f-2102.fwd5-inf-g-01-launcher-one-snapshot-run-pinned-bundle.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF135-2-AC1,DBF135-2-AC2 --governing-order <this order>` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the launcher test count; the bundle's sha256 and its member count; the two mutants and which test failed each; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a script, a manifest and offline tests in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access in this order.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the launcher is not scheduled until the release pair.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF135-2-AC1 and AC2 FAIL at base and the checker's helpers are exercised by its self-test (9 arms).
lane: the <paths> block IS the grant.
</preflight>
