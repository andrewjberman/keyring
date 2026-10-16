# AMGT_HARVST task order -- `HVST-cb-10` -- ROUND 87, workstream EGRESS-COUNT: EVERY COLLECTOR PROCESS REPORTS ITS OWN S3 GETS, AND THE CYCLE RECORD SUMS THEM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-10.every-collector-process-reports-its-own-s3-gets</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~146</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and one test only. NO publisher host, NO Secrets Manager call, NO S3 call (tests use fakes), NO browser, NO collector or runner run, NO scheduled task.
comp-adversary: RUN at L5 -- the adversary is a counter that reads the wrong process (the very defect this cell fixes), a ledger line written for a command that failed before it counted, a sum that includes lines outside the cycle's own time window, and a change to an existing cycle-record key or to the `CYCLE` log line that existing tests read whole.
</preflight>

## 0. THE CELL

`lib/research/harvest/store.py` counts S3 GETs in process-wide counters (`get_stats_snapshot()`, `get_stats_reset()`, `_get_counted`). `lib/opal_data_harvest/cycle_runner.py` `run_cycle` takes `store.get_stats_snapshot()` before and after the driver call and writes the difference to the cycle record as `s3_get_count` and `s3_get_bytes`. But the driver (`backfill_driver.py`) runs every pair as a SUBPROCESS (`Collector._spawn`: `python -m lib.opal_data_harvest run ...`, and `... upload-harvest ...`), and those subprocesses do the S3 reads. The runner process does none, so the cycle record reads 0 and 0 whatever the cycle cost. MEASURED on dell1 (2026-10-15, one `run` job in one process): 747 GETs, 212,043,826 bytes.
This cell makes each `run` and `upload-harvest` process write its OWN counters, and the cycle record sum them. It changes NO read path and NO existing key.

## 1. THE BUILD (LOCAL, about 70 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. New module `lib/opal_data_harvest/s3_ledger.py` (stdlib plus `lib.research.harvest.store` only), two functions:
   - `record_process_gets(runtime_root, command, run_id, started_snapshot)`: reads `store.get_stats_snapshot()` now, subtracts `started_snapshot` (a dict from the same function, taken at process start), appends ONE line of JSON to `<runtime_root>/s3_get_ledger.jsonl` (create the directory if missing): `{"command": <str>, "run_id": <str or null>, "pid": <os.getpid()>, "ended_at": <UTC now, ISO 8601 ending Z>, "get_count": <int>, "get_bytes": <int>}`; returns the line's dict. It never raises: any OSError is swallowed and the function returns None (a counter must never fail a job).
   - `sum_ledger(runtime_root, since_iso, until_iso)`: reads the file if it exists (missing file or an unparseable line counts as zero lines, never an error), and returns `{"lines": n, "get_count": total, "get_bytes": total}` over the lines whose `ended_at` is `>= since_iso` and `<= until_iso` (string comparison is valid: both are UTC ISO ending Z).
b. In `lib/opal_data_harvest/__main__.py` `main()`: take `started = store.get_stats_snapshot()` (import `lib.research.harvest.store as store` at the top as `cycle_runner.py` does) right after the arguments are parsed. For the commands `run` and `upload-harvest` ONLY, in a `finally` that runs whether the command returned or raised, call `s3_ledger.record_process_gets(root, args.command, run_id, started)`, where `root` is the runtime root `main()` already resolves and `run_id` is the run id of the run record the worker wrote (from `worker.last_run_record`'s file stem when the attribute exists and is a path; else None). For `run` ONLY, when the line was written and a run record file exists, ALSO add the two keys `"s3_get_count"` and `"s3_get_bytes"` (the same two numbers) to that run record JSON, rewriting it atomically with `lib/opal_data_harvest/storage.py` `atomic_json` (read the file, add the two keys, write back; swallow any error). Touch no other behaviour of `main()`: its return codes, its printed output and its `worker.close()` stay as they are.
c. In `lib/opal_data_harvest/cycle_runner.py` `run_cycle`: after the existing `record` dict is built and BEFORE it is written, add three NEW keys: `"s3_jobs_lines"`, `"s3_get_count_jobs"`, `"s3_get_bytes_jobs"` from `s3_ledger.sum_ledger(runtime_root, record["started_at"], record["ended_at"])`. Add the three names to the tuple of cycle-record field names near line 45 (read what it is used for first; if a reader compares the tuple against the record's keys, keep the two consistent). The existing keys `s3_get_count` and `s3_get_bytes` (the runner process's own) stay exactly as they are, and so does the `CYCLE ...` log line.
d. New test `lib/opal_data_harvest/test_cb10_job_get_counters.py` (no network, no S3: fake store counters by monkeypatching `store.get_stats_snapshot`; temp directories):
   - (1) `record_process_gets` appends one line with the delta (not the absolute) of the two snapshots, with the right keys, and a second call appends a second line;
   - (2) it returns None and raises nothing when the runtime root is unwritable (monkeypatch `open`/`Path.open` to raise `OSError`);
   - (3) `sum_ledger` sums only lines inside `[since, until]`, ignores a line outside and a corrupt line, and returns zeros for a missing file;
   - (4) a cycle driven through `cycle_runner.run_cycle` with the fake driver and fixtures that `test_br2_cycle_runner.py` uses, where the test first writes two ledger lines inside the cycle window and one outside: the record carries `s3_jobs_lines` 2 and the two sums, and its old keys `s3_get_count` and `s3_get_bytes` are unchanged from what the runner process measured;
   - (5) `__main__.main` for a `run` writes the two keys into the run record and one ledger line: drive it the way `test_ad2_no_sign_in.py` or `test_worker.py` drive a run with a fake publisher factory; if no existing test drives `main()` end to end, instead test the small block you added by moving it into a function in `s3_ledger.py` (`finish_command(root, command, worker, started)`) and call that with a fake worker whose `last_run_record` is a temp file;
   - (6) **A MUTANT:** with `s3_ledger.sum_ledger` monkeypatched to return zeros, arm (4) FAILS (assert that it does). This proves (4) discriminates.
2. Do not run anything against a publisher, S3, Secrets Manager or any box; do not launch a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/s3_ledger.py
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/cycle_runner.py
lib/opal_data_harvest/test_cb10_job_get_counters.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~146/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-10"><invocation>python -m pytest lib/opal_data_harvest/test_cb10_job_get_counters.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-10"><invocation>python -m pytest lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_br2_cycle_runner.py lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py lib/opal_data_harvest/test_eg1_silver_cache.py lib/opal_data_harvest/test_bf1_job_record.py lib/opal_data_harvest/test_o1_run_record_reach.py lib/opal_data_harvest/test_n1_received_bytes_and_run_record.py lib/opal_data_harvest/test_bh8_job_finished_at.py lib/opal_data_harvest/test_ae4_backfill_driver.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^125 passed, 4 subtests passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2 reads exactly `125 passed, 4 subtests passed`: the base's own count (read by the issuer on the main tree at 2026-10-15 ~23:5xZ). A sparse worktree may differ: if your worktree's base count differs, say so with both counts and do not weaken the pattern.
- **Dry-run at the base (issuer, dell1):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`125 passed, 4 subtests passed`).
- Before and after, run the full `lib/opal_data_harvest` suite and record both counts. On a clean main checkout one failure is known (`test_bn1_names_made_whole.py::test_v_building_twice...`, CRLF against LF on disk); a sparse worktree also shows `test_harvest_grammar.py::test_one_writer_for_both_channels` (a missing import outside the cone). Add none.
- **LINE ENDINGS:** `__main__.py` and `cycle_runner.py` may carry mixed line endings. Edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W146-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~146/AMGT_HARVST.TO-HVST-cb-10.every-collector-process-reports-its-own-s3-gets.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cb-10.every-collector-process-reports-its-own-s3-gets` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cb-10.every-collector-process-reports-its-own-s3-gets.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO msg 6335 item 2 ("per-job GET count and bytes in each run record, summed in the cycle record") and msg 6339 item 2 (order: cb-10 counters, then cb-11, then cb-9). Ledger `ledger/ROUND87_EGRESS_FINDING_JOB_FULL_SILVER_READ_20261016.md`.
- **Why a ledger file and not the run record alone:** `upload-harvest` writes no run record, and it reads the same silver prefixes through `silver_append` (the CTO's "the uploader is separate": this cell makes it MEASURABLE, the fix is not here). The ledger carries both commands; the run record carries the `run` job's own two keys, as the CTO asked.
- **Disjoint from `HVST-cb-11`** (workers ~146 and ~147 run in parallel): cb-10 writes `s3_ledger.py`, `__main__.py`, `cycle_runner.py`; cb-11 writes `worker.py` and `harvest_grammar.py`. Neither order names the other's files.
- The real-job criterion is the issuer's (the 120 s cap): after the merge, `cb10_job_get_probe.py` (run in one process) and a plain `run` of the same pair are compared: the run record's `s3_get_count` and `s3_get_bytes` must equal the probe's in-process figures within the listing's own variation (same pair, same silver).
- Direct act: ONE cell, LOCAL, about 70 product lines; no L2, L4-R or L8-L10.
- Slot ~146, worktree `C:/dev/wk-harvst-146`, branch `wk-AMGT_HARVST-146`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts`.

**COMPLETE 2026-10-16 ~00:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~146` (worker-light, haiku, high), branch `wk-AMGT_HARVST-146`, build `d6a4353d58`, head `044fa2d45d`. Diff read by this seat: `s3_ledger.py` (new, 68 lines: `record_process_gets` appends one delta line and returns None on OSError; `sum_ledger` windows by `ended_at`, a missing file or corrupt line counts as nothing), `__main__.py` (+27/-?: `_record_process_gets` in a `finally` for `run` and `upload-harvest` only, two keys onto the run record; the worker also removed a local `import ... as store` that would have shadowed the module import, row `D1-W146-S1`), `cycle_runner.py` (+9: three NEW keys and their names in the field tuple; the old two keys and the `CYCLE` log line untouched).
- **AC1 PASS:** `6 passed` (worker; this seat re-ran). **AC2 PASS:** `125 passed, 4 subtests passed` (worker; base the same). Proof instance VALID rc 0. Full suite per the worker `865 passed, 1 failed (sparse import), 3 skipped`, base `859 passed, 1 failed`.
- **Rows** `D1-W146-S1` (the `import` shadow, resolved by the worker) and `-S2` (the two keys land on the runtime-root copy of the run record, not the bronze copy persisted earlier inside `worker.run`): OBSERVATION / INERT, no action; the ledger is the cycle's authority.
- **What this does NOT prove:** a real job's counters equal the in-process probe's. That is the issuer's real read after the merge.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>complete</status>
<round>87</round>
<workstream>EGRESS-COUNT</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
