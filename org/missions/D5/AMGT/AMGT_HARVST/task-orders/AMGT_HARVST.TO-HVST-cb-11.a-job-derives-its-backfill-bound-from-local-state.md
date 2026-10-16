# AMGT_HARVST task order -- `HVST-cb-11` -- ROUND 87, workstream EGRESS-FIX: A BACKFILL JOB DERIVES ITS BOUND FROM LOCAL STATE AND READS NO SILVER FROM S3 (CTO design B)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-11.a-job-derives-its-backfill-bound-from-local-state</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~147</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and one test only. NO publisher host, NO Secrets Manager call, NO S3 call (tests use fakes that FAIL the test on any S3 read), NO browser, NO collector or runner run, NO scheduled task.
comp-adversary: RUN at L5 -- the adversary is a local watermark that moves FORWARD past articles never stored (a failed job must not advance it), a first job on empty state that pages without a bound, a change to the `plan --with-watermark` command (which keeps its S3 read on purpose), and a test whose fake S3 can never be reached so that it passes whatever the code does.
</preflight>

## 0. THE CELL

Every backfill job (`--retrieval-mode backfill`, which is how `backfill_driver.Collector.run_job` runs every pair) begins with `harvest_grammar.backfill_bound(security_key, publisher, floor_date, client=...)`, called from `lib/opal_data_harvest/worker.py` (search for `backfill_bound`, in `Worker.run_job` near the line `client.bound_date = backfill_bound(`). `backfill_bound` calls `watermark()`, which calls `store.silver_latest(source, "article", ("article_key",))`: with no `silver_cache()` open (a job is its own process) that GETs EVERY parquet part of the source's silver `article` table, then keeps the newest `published_utc` among rows whose `discovered_for` holds the security. MEASURED on dell1 (2026-10-15), one call each: wsj 419 GETs / 125.4 MiB, barrons 64 / 9.9 MiB, sa 1367 / 80.4 MiB, bbg 747 / 202.2 MiB; a 242-pair cycle makes 242 such reads. The CTO ruled DESIGN B (msg 6339): "each job derives its watermark locally, with no silver S3 read. Dell1 is now the single writer per publisher, so the local state is authoritative."
This cell makes the job's bound come from the local progress database instead, and nothing else.

## 1. THE BUILD (LOCAL, about 50 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. `lib/opal_data_harvest/harvest_grammar.py` `backfill_bound(security_key, publisher_code, floor_date, client=None, local_watermark=_NOT_GIVEN)`: add a module-level sentinel `_NOT_GIVEN = object()` and the new keyword. When `local_watermark` is NOT the sentinel (it is a `datetime.datetime` or `None`), use it in place of `watermark(...)` and do NOT call `watermark` or touch `client` at all; the rest of the function (date comparison, `max(floor_date, ...)`) is unchanged. When it IS the sentinel, the function behaves exactly as today (the `plan --with-watermark` path in `__main__.py` keeps its S3 read, deliberately: do not touch `__main__.py`). `watermark()` itself is not changed.
b. `lib/opal_data_harvest/worker.py`:
   - add `Worker._local_watermark(self, publisher, security_key)`: reads the `state` table row with key `"wm|" + publisher + "|" + security_key` (the table `self.db` already holds: `SELECT value FROM state WHERE key=?`, as `Worker.run` does for its cursor) and returns the stored ISO-8601 string parsed to an aware UTC `datetime`, or `None` when there is no row or the value does not parse;
   - add `Worker._note_local_watermark(self, publisher, security_key, published)`: parses `published` (an ISO-8601 string or a datetime; a naive value is read as UTC; anything unparseable or falsy is ignored), compares with the stored value, and writes the LATER of the two back with `INSERT OR REPLACE INTO state VALUES(?,?)` (a watermark never moves backward) and commits;
   - at the existing call site `client.bound_date = backfill_bound(security["key"], publisher, floor_date, client=self.harvest_client)` replace the call by `backfill_bound(security["key"], publisher, floor_date, local_watermark=self._local_watermark(publisher, security["key"]))` (no `client=`);
   - at the point where an article is ACCEPTED and stored, right after `article_path, article_key = self.catalog.store(article, security)` and the `INSERT OR REPLACE INTO articles` commit, call `self._note_local_watermark(publisher, security["key"], article.get("published"))`. Only a STORED article advances the mark: a rejected, duplicate or held article, a failed job and a job that raised do not (the call is nowhere else).
   Change nothing else in `worker.py`.
c. READ AND REPORT (no edit): the value shape of `article["published"]` as the publishers produce it (look in `publishers.py` for where each publisher's article dict gets `published`), and whether the local value compares correctly with the `date` that `backfill_bound` compares (`wm.date()`): say in your report what you found for `wsj`, `barrons`, `sa`, `bbg`. If a publisher's `published` is NOT an ISO-8601 string or datetime (for example epoch seconds or a locale string), do not guess a parser: file a row naming the publisher and the shape, and make `_note_local_watermark` ignore it (the bound then stays the floor for that publisher, which is the safe direction).
d. New test `lib/opal_data_harvest/test_cb11_local_watermark.py` (no network, no S3, no browser; temp directory as the runtime root; reuse the fakes of `test_worker.py` and of the backfill-bound tests you find with `Grep` for `backfill_bound` under `lib/opal_data_harvest/test_*.py`):
   - (1) `backfill_bound` with `local_watermark=None` returns the floor and makes ZERO calls on a client whose every method raises `AssertionError("S3 read")`; with `local_watermark` a datetime later than the floor it returns that datetime's date; earlier than the floor it returns the floor;
   - (2) `backfill_bound` WITHOUT the keyword still calls `watermark` (the S3 path is unchanged): monkeypatch `harvest_grammar.watermark` to a recorder and assert it was called once;
   - (3) a `Worker` job in backfill mode with a fake publisher client that exposes `bound_date` and `max_listing_pages`, on an empty `state` table, with `store.silver_latest` monkeypatched to raise `AssertionError("silver read")`: the job's `client.bound_date` equals the floor and no silver read happened;
   - (4) after a job that STORES an article with `published` D, `_local_watermark` returns D and the next job's `client.bound_date` is `max(floor, D.date())`; after a job that stores NOTHING (every article rejected) the stored mark is unchanged; after a job that raises, unchanged;
   - (5) `_note_local_watermark` never moves backward: a later call with an earlier date leaves the later value;
   - (6) **A MUTANT:** with `worker.backfill_bound` replaced by a wrapper that ignores `local_watermark` and calls the original `watermark` path, arm (3) FAILS (assert that it does). This proves (3) discriminates.
2. Do not run anything against a publisher, S3, Secrets Manager or any box; do not launch a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_cb11_local_watermark.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~147/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-11"><invocation>python -m pytest lib/opal_data_harvest/test_cb11_local_watermark.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-11"><invocation>python -m pytest lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_br2_cycle_runner.py lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py lib/opal_data_harvest/test_eg1_silver_cache.py lib/opal_data_harvest/test_bf1_job_record.py lib/opal_data_harvest/test_o1_run_record_reach.py lib/opal_data_harvest/test_n1_received_bytes_and_run_record.py lib/opal_data_harvest/test_bh8_job_finished_at.py lib/opal_data_harvest/test_ae4_backfill_driver.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^125 passed, 4 subtests passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2 reads exactly `125 passed, 4 subtests passed`: the base's own count (issuer, main tree, 2026-10-15 ~23:5xZ). A test elsewhere in `lib/opal_data_harvest` may assert the OLD `backfill_bound(... client=...)` call: if one now fails, report it with its name and the reason; do not weaken or delete it, and do not widen your paths: the issuer rules on it.
- **Dry-run at the base (issuer, dell1):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`125 passed, 4 subtests passed`).
- Before and after, run the full `lib/opal_data_harvest` suite and record both counts. On a clean main checkout one failure is known (`test_bn1_names_made_whole.py::test_v_building_twice...`, CRLF against LF on disk); a sparse worktree also shows `test_harvest_grammar.py::test_one_writer_for_both_channels` (a missing import outside the cone). Add none.
- **LINE ENDINGS:** `worker.py` and `harvest_grammar.py` may carry mixed line endings. Edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W147-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~147/AMGT_HARVST.TO-HVST-cb-11.a-job-derives-its-backfill-bound-from-local-state.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cb-11.a-job-derives-its-backfill-bound-from-local-state` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cb-11.a-job-derives-its-backfill-bound-from-local-state.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO msg 6339 (design B, the order cb-10, cb-11, cb-9) and 6344 ("Make cb-11 your next cell"). Ledger `ledger/ROUND87_EGRESS_FINDING_JOB_FULL_SILVER_READ_20261016.md`; measurements `deliverables/2.0.0_SA_COO_W1/round87/cb10_watermark_probe.py`.
- **What B changes in behaviour, named:** a first job on dell1 for a security with no local mark pages back to the CYCLE FLOOR (the runner passes the last completed cycle's start date, or yesterday) instead of `max(floor, S3 watermark)`. History that site Z stored is not consulted: re-listed pages are deduplicated by `--new-only` and the held-key check (`article_known`, unchanged). The mark only advances on a STORED article, so a security whose newest article predates the floor behaves as before.
- **NOT in this cell:** the uploader's `silver_append` reads (`uploads.py`, per source per pass in `upload-harvest`): the CTO ruled the uploader separate; cb-10's ledger makes its GETs measurable. `plan --with-watermark` keeps its S3 read.
- **Disjoint from `HVST-cb-10`** (workers ~146 and ~147 run in parallel): cb-10 writes `s3_ledger.py`, `__main__.py`, `cycle_runner.py`; this cell writes `worker.py` and `harvest_grammar.py`.
- The real-job criterion is the issuer's: after BOTH merges, `cb10_job_get_probe.py` for `bbg` on the same pair must read `get_count` near 0 (listing and key-exists calls only), against 747 / 212,043,826 bytes before.
- Direct act: ONE cell, LOCAL, about 50 product lines; no L2, L4-R or L8-L10.
- Slot ~147, worktree `C:/dev/wk-harvst-147`, branch `wk-AMGT_HARVST-147`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts`.

**COMPLETE 2026-10-16 ~00:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~147` (worker-light, haiku, high), branch `wk-AMGT_HARVST-147`, build `40db997c81`, head `0617390fcd`, then this seat's one-character repair: the worker's diff carried an unrelated edit in `worker.py` (`job_id =dt.datetime...`, a deleted space, outside the cell); restored byte for byte, `git diff --stat` for `worker.py` now reads only the cell's lines. Diff read by this seat: `harvest_grammar.py` (+14/-?: `_NOT_GIVEN` sentinel and `local_watermark`; the S3 path unchanged when the keyword is not given), `worker.py` (`_local_watermark`, `_note_local_watermark` (never backward, unparseable ignored), the call site now `local_watermark=` with no client, one `_note_local_watermark` call after a STORED article only).
- **AC1 PASS:** `13 passed` (worker; this seat re-ran). **AC2 PASS:** `125 passed, 4 subtests passed` (worker; this seat re-ran). Proof instance VALID rc 0 (re-run here). Full suite per the worker `872 passed, 1 failed (sparse import), 3 skipped`, base `859 passed, 1 failed`.
- **Report item c:** `published` is an ISO-8601 string with `Z` or an offset for `wsj`, `barrons`, `sa` and `bbg` (code and recorded fixtures); no parser was guessed.
- **Row `D1-W147-S1`** (ARMED, my disarm): a pair with no local mark is bounded at the floor, and a pair whose candidates are ALL already held never writes a mark, so its jobs re-page to the floor each cycle. The floor is the last completed cycle's start date, so the re-paging is bounded to about one cycle of dates and costs listing requests, not silver reads; dispositioned by the issuer's row after the merge; carried, not fixed.
- **What this does NOT prove:** the S3 reads of a REAL job fall to near zero. That is the issuer's real read after both merges (`cb10_job_get_probe.py`, bbg, BA: before 747 GETs / 212,043,826 bytes).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>complete</status>
<round>87</round>
<workstream>EGRESS-FIX</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
