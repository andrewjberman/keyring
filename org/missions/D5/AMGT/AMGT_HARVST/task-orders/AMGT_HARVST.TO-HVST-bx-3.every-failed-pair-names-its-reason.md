# AMGT_HARVST task order -- `HVST-bx-3` -- ROUND 80 (`1.0.0_SA_CTO~DELL1` msg 4352, `ledger/ROUND_ANALYSIS.round79.md` item 2, row `AMGT_HARVST-D1-S7`): EVERY FAILED PAIR OF A CYCLE CARRIES ITS REASON -- THE EXCEPTION CLASS AND THE VENDOR'S MESSAGE, TRUNCATED, WITH NO CREDENTIAL AND NO FULL RESPONSE BODY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bx-3.every-failed-pair-names-its-reason</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bx-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~135</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the installer is not changed.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO publisher host, NO S3 call, NO collector or runner run against the world, NO change to `config.json` or any scheduled task.
comp-adversary: RUN at L5 -- the adversary is a reason that is a fixed string instead of the failure's own text, a message copied whole (a full response body, a cookie, a token or an authorization header written into a record that is uploaded), a reason added to a SUCCESS row, or a change to which pairs count as failed.
</preflight>

## 0. THE CELL

FWD-18's cycle runner (`lib/opal_data_harvest/cycle_runner.py`) writes a cycle record whose `failures` list names each failed pair
with `{"key", "status", "detail"}` (the runner builds the row at about lines 197 to 215: `"detail": value.get("detail") or status`).
Read on the site Z box, bbg's first completed cycle (`20261010T221526Z`, 242 of 242 attempted, 8 failed) carried, for ALL 8
failures, `detail` equal to the bare word `error`, identical to `status`. A failure that does not say why cannot be retried or fixed.

HVST-bv-1 already stores a job result's `detail` into the checkpoint entry and the record, and the driver's `run_job` returns a
detail such as `no run record (rc=...): <stderr tail>` or `job timeout`. So the reason is being lost one step earlier: for a
pair whose collector job ran and reported `status` `error`, the job result carries no reason text. Find where that status is
produced and where the exception or the vendor's message is dropped (look in `lib/opal_data_harvest/` at `publishers.py`,
`transport.py`, `worker.py`, `emit_job_records.py`, `backfill_driver.py` and `cycle_runner.py`; the 8 failure keys and the
record are in
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/bw2_bbg_20261010T221526Z.cycle.json`, read-only).

## 1. THE BUILD (LOCAL)

Work in your worktree. Change only the files under `lib/opal_data_harvest/` that the trace shows lose the reason.
1. **The reason is kept.** For every failure kind the code can produce, the job result's `detail` becomes
   `<ExceptionClassName>: <message>` where the class name is the Python exception's class (`type(exc).__name__`) or, for a
   vendor HTTP failure, `HTTP <status code>: <vendor message or reason phrase>`; for a subprocess job with no run record it
   stays `no run record (rc=<n>): <stderr tail>`, and `job timeout` stays. The text is cut to **300 characters** and ends with
   `...` when it was cut.
2. **No secret, no body.** Before the cut, replace the value of any `Authorization`, `Cookie`, `Set-Cookie`, `token`,
   `password`, `secret`, `api_key` / `api-key` or `Bearer` occurrence with `[REDACTED]` (case-insensitive; the key name stays).
   Never write a whole HTTP response body: take only the vendor's message or reason phrase, then cut as in 1.
3. **A success row is unchanged:** a pair that succeeded carries no new field and no changed field in the record or the checkpoint.
4. **Which pairs count as failed is unchanged** (bv-1's rules: a pair `error` is failed and the cycle continues; five consecutive
   still stop the publisher). The `failures` row shape stays `{"key", "status", "detail"}`.
5. **Tests**, in `lib/opal_data_harvest/test_bx3_failure_reason_kept.py`, with a fake collector (no network): one planted
   failure of EACH kind the trace found (at least: an exception raised during a fetch, a vendor HTTP error with a body, a
   subprocess with no run record and a stderr tail, a job timeout). For each: the cycle record's `failures[].detail` shows the
   class and message (assert the exact expected text), it is at most 303 characters, and a planted secret in the message
   (`Cookie: session=abc123; token=xyz`) appears as `[REDACTED]`. One more arm: a cycle of successes produces a record and a
   checkpoint byte-identical to the base's for the same inputs (compare the record's keys and the `failures` list). A MUTANT:
   with the reason-keeping line reverted to the bare status, the exception-kind test fails (assert that it does).
6. Do not run anything against a publisher, S3 or the site Z box. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/cycle_runner.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/emit_job_records.py
lib/opal_data_harvest/test_bx3_failure_reason_kept.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~135/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bx-3"><invocation>python -m pytest lib/opal_data_harvest/test_bx3_failure_reason_kept.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bx-3"><invocation>python -m pytest lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py lib/opal_data_harvest/test_ae4_backfill_driver.py lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py lib/opal_data_harvest/test_br2_cycle_runner.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure.
- The full `lib/opal_data_harvest` suite already has 5 failures at the base (`test_ah1_fixture_solve.py::test_fixture_solve[bbg]`,
  three in `test_aw1_origin_load_wait.py`, one in `test_bn1_names_made_whole.py`). Run it before and after, and record both
  counts in your report. Add none.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W135-S1`. If you file
  one, the channel's commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD
  (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~135/AMGT_HARVST.TO-HVST-bx-3.every-failed-pair-names-its-reason.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bx-3.every-failed-pair-names-its-reason`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4352, `ledger/ROUND_ANALYSIS.round79.md` section 2 item 2: "every failure row carries its
  exception class and vendor message, truncated, no secrets. Close: a planted failure of each kind shows its detail, and a
  success row is unchanged." The CVO graded bw-2 AC3 FAIL on exactly this (C-S7, ADJUDICATION_v71 @b284aa2d50).
- This cell's proof is the fixture. The live read (a bbg cycle whose failures name their reasons) is read at site Z after the merge
  and a re-pin of the runner (a WORLD act under its own pair), which is not an order of this round.
- Merge: at the chain end with `safe-merge.sh`, under a never-widen pair (COO half at the drain, and the CTO's producer half),
  into `lib/opal_data_harvest`, as bv-1 was.
- Slot ~135, worktree `C:/Dev/wk-harvst-135`, branch `wk-AMGT_HARVST-135-r80`.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>80</round>
<slot>dell1</slot>
<fabric>dell1</fabric>
