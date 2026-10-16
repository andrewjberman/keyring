# AMGT_HARVST task order -- `HVST-cb-12` -- ROUND 87, workstream EGRESS-WRITE: THE UPLOADER APPENDS SILVER WITHOUT READING THE WHOLE TARGET TABLE FROM S3 (CTO msg 6388, "design B on the write side")

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-12.the-uploader-appends-without-reading-the-target-table</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~148</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and one test only. NO publisher host, NO Secrets Manager call, NO S3 call (tests use fakes that FAIL the test on any `get_object` or table listing), NO browser, NO collector or runner run, NO scheduled task.
comp-adversary: RUN at L5 -- the adversary is a change to `silver_append`'s DEFAULT behaviour (it is shared by the corpus, filings, management and lusha writers: the default path must stay byte for byte as it is), a local known-hash record that is updated BEFORE the put succeeds (a failed put would then suppress the row forever), a record key that does not round-trip through the local table, and a fake S3 that can never be reached so the test passes whatever the code does.
</preflight>

## 0. THE CELL

`lib/research/harvest/store.py` `silver_append(source, table, rows, record_key_fields, run_stamp, client=None)` begins with `latest = silver_latest(source, table, record_key_fields, client=client)`, which (outside a `silver_cache()` context, and an upload is its own process) GETs EVERY `part-*.parquet` of the target table to decide which rows are unchanged. `lib/opal_data_harvest/uploads.py` `HarvestUploader` calls it through the module-level `_silver_append_retrying_object_name` (the `article` path, near the call at about line 343, and the `listing_hit` path, near about line 448). MEASURED and SIZED on dell1 (2026-10-16): `barrons` uploads read 2.57 MiB each; the silver tables are `sa` `listing_hit` 1592 parts / 284.2 MiB, `bbg` `article` 747 parts / 202.2 MiB, `wsj` `article` 419 parts / 125.4 MiB. An upload that writes rows of a table reads that whole table.
The CTO ruled (msg 6388): "silver_append writes new part files and de-duplicates against the local state (dell1 is the single writer), never by reading the target table from S3."
This cell adds an OPT-IN known-hash mode to `silver_append` and makes `HarvestUploader` use it with a local table. NOTHING that calls `silver_append` today without the new argument changes.

## AMENDMENT 1 (issuer, 2026-10-16 ~02:3xZ; GOVERNS wherever the sections below differ; from the worker's first report, rows `D1-W148-S1`, `-S2`, `-S3`)

- **(a) `written_hashes` is added ONLY in known mode.** In the default path (`known is None`) `silver_append` returns EXACTLY its three old keys, so no existing caller (`bright_data_serp`, `social/collect`, `filings`, `lusha`, `bloomberg`, `typed`, whose receipts may be JSON-dumped) sees a new key. This replaces the 'both modes' sentence in 1.a. Test (2) additionally asserts the default result's key set equals `{written_rows, skipped_unchanged, parts}`.
- **(b) The wrapper returns the three old keys.** `_silver_append_retrying_object_name(..., known_db=...)` records the written hashes and then returns the result WITHOUT `written_hashes` (the run receipt is JSON-dumped and a key tuple can hold a date). This is the worker's deviation from 1.c's `return result`, ruled correct.
- **(c) Ten existing tests are updated, and ONLY their instrument.** `test_ai5_batched_silver_append.py` and `test_at1_batched_listing_upload.py` record calls to `store.silver_latest` and assert they equal one-per-source-per-pass (for example `assert calls == [SOURCE]`): that was a PROXY for 'one `silver_append` per source per pass' (each append read the prefix once), and the retired read is exactly what this cell removes. In each of the ten failing tests: (i) change the recorder so it records calls to `store.silver_append` (wrap or replace it, keeping what it returned) and keep the same expected lists, so the batching property is still graded and the test's own mutant (the per-row grouping restored) still fails it; (ii) ADD an assertion that `store.silver_latest` was called ZERO times in the pass (the new contract). Keep every other assertion and every mutant arm in those two files as they are, and change no test that passes today. Report the ten test names, and for each tell whether its mutant still fails after your edit (run it).
- **(d) Paths:** the two test files above are now named in `<paths>`. Nothing else is added.

## 1. THE BUILD (LOCAL, about 90 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. `lib/research/harvest/store.py` `silver_append(..., client=None, known=None)`: add the keyword `known`. When `known is None` (the default) the function is EXACTLY what it is today. When `known` is a mapping `{record_key_tuple: record_hash_string}` (anything with `.get`): do NOT call `silver_latest` and do not read S3; for each row compute `new_hash = record_hash(row)` and the `record_key` as today, set `prior = {"record_hash": known[record_key]}` when `record_key` is in `known` else `None`, and use the existing `_unchanged(prior, new_hash)` for the skip decision (do not change `_unchanged`). Add ONE new key to the returned dict, `"written_hashes"`: a list of `(record_key_tuple, new_hash)` for the rows actually written, in both modes (the default path fills it too, so callers see one shape); the three existing keys keep their meaning.
b. New module `lib/opal_data_harvest/silver_known.py` (stdlib only): the local record of what this runtime has appended, in the progress database the uploader already holds (`self.db`, a sqlite3 connection):
   - `ensure(db)`: `CREATE TABLE IF NOT EXISTS silver_known(source TEXT, tbl TEXT, record_key TEXT, record_hash TEXT, PRIMARY KEY(source, tbl, record_key))`;
   - `encode_key(record_key_tuple)`: `json.dumps(list(record_key_tuple), default=str, sort_keys=True)`; and `decode_key(text)`: `tuple(json.loads(text))`;
   - `load(db, source, table)`: ensures the table, returns `{decode_key(k): hash}` for the pair; an unparseable stored key is skipped;
   - `note(db, source, table, written_hashes)`: ensures the table, upserts each `(record_key, hash)` with `INSERT OR REPLACE`, commits.
   Round trip: a key tuple of strings, ints and `None` must satisfy `decode_key(encode_key(k)) == k`; a key that holds a non-JSON value (a datetime) is stored through `default=str` and will NOT equal on reload: the test pins this as a documented limit, and `load` simply never matches such a key (the row is then appended again, which is the safe direction).
c. `lib/opal_data_harvest/uploads.py`: the module-level `_silver_append_retrying_object_name(client, source, table, rows, record_key_fields, run_stamp, max_attempts=20)` gains a keyword `known_db=None`. When it is None, nothing changes. When it is a connection: `known = silver_known.load(known_db, source, table)` ONCE before the attempts loop; every attempt calls `harvest_grammar.store.silver_append(..., known=known)`; ONLY AFTER a call returns (not before, and not on a `ClientError`) call `silver_known.note(known_db, source, table, result["written_hashes"])` and return `result`. On the `PreconditionFailed` retry the same `known` mapping is reused (it was not updated). In `HarvestUploader`, the two call sites of the module-level function (the `article` path and the `listing_hit` path: find them with `Grep` for `_silver_append_retrying_object_name(` in the class's methods; do NOT touch the `Uploader` class's own method near the end of the file, which belongs to the legacy channel) pass `known_db=self.db`. Change nothing else in `uploads.py`.
d. New test `lib/opal_data_harvest/test_cb12_uploader_known_hashes.py` (no network, no S3: a fake client whose `get_object` and `get_paginator` raise `AssertionError("S3 read")` and whose `put_object` records its calls; `sqlite3.connect(":memory:")`; reuse the fakes of `test_ai5_batched_silver_append.py`, `test_at1_batched_listing_upload.py` and `lib/research/harvest/tests/test_store.py`):
   - (1) `silver_append(..., known={})` with two rows writes both (two `put_object` calls at most, one per fetch date), makes NO S3 read, and returns `written_hashes` of length 2; the same call with `known` holding the first row's hash writes only the second and returns `skipped_unchanged` 1;
   - (2) `silver_append` WITHOUT `known` still calls `silver_latest` (monkeypatch it to a recorder returning `{}`) exactly once: the default path is unchanged;
   - (3) `silver_known`: `note` then `load` round-trips string, int and `None` keys; a datetime-valued key does NOT round-trip (pin it); `load` on a fresh database returns `{}`;
   - (4) `_silver_append_retrying_object_name(..., known_db=db)` with the fake client: a first call writes the rows and records them in `silver_known`; a second call with the SAME rows writes NOTHING (zero `put_object`) and reads no S3; a changed row (different content, same key) IS written;
   - (5) a `put_object` that raises a non-`PreconditionFailed` error leaves `silver_known` EMPTY (nothing recorded before the put succeeded), and a `PreconditionFailed` on the first attempt then success records the rows once;
   - (6) **A MUTANT:** with `silver_known.note` monkeypatched to do nothing, arm (4)'s second call writes the rows again (assert that it does). This proves (4) discriminates.
2. Do not run anything against a publisher, S3, Secrets Manager or any box; do not launch a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/research/harvest/store.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/silver_known.py
lib/opal_data_harvest/test_cb12_uploader_known_hashes.py
lib/opal_data_harvest/test_ai5_batched_silver_append.py
lib/opal_data_harvest/test_at1_batched_listing_upload.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~148/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-12"><invocation>python -m pytest lib/opal_data_harvest/test_cb12_uploader_known_hashes.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-12"><invocation>python -m pytest lib/research/harvest/tests/test_store.py lib/research/harvest/tests/test_o3_silver_tie_break.py lib/research/harvest/test_at4_silver_union_keys.py lib/opal_data_harvest/test_ai5_batched_silver_append.py lib/opal_data_harvest/test_at1_batched_listing_upload.py lib/opal_data_harvest/test_eg1_silver_cache.py lib/opal_data_harvest/test_retrieval_provenance.py lib/opal_data_harvest/test_silver_from_bronze.py lib/opal_data_harvest/test_legacy_upload.py lib/opal_data_harvest/test_au1_upload_timeout.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^110 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2 reads exactly `110 passed`: the base's own count (issuer, main tree, 2026-10-16 ~01:5xZ). A sparse worktree may differ: if your worktree's base count differs, say so with both counts and do not weaken the pattern. `silver_append` is shared: if ANY test in `lib/research` or `lib/opal_data_harvest` that is not in AC2 fails after your change, report its name and the reason.
- **Dry-run at the base (issuer, dell1):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`110 passed`).
- Before and after, run the full `lib/opal_data_harvest` suite AND `lib/research/harvest` and record both counts of each. On a clean main checkout one failure is known in `lib/opal_data_harvest` (`test_bn1_names_made_whole.py::test_v_building_twice...`, CRLF against LF on disk); a sparse worktree also shows `test_harvest_grammar.py::test_one_writer_for_both_channels` (a missing import outside the cone). Add none.
- **LINE ENDINGS:** `store.py` and `uploads.py` may carry mixed line endings. Edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit, and make no whitespace edits outside your lines.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W148-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~148/AMGT_HARVST.TO-HVST-cb-12.the-uploader-appends-without-reading-the-target-table.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cb-12.the-uploader-appends-without-reading-the-target-table` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cb-12.the-uploader-appends-without-reading-the-target-table.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO msg 6388 (cut cb-12: the uploader appends without reading the whole table; keep a small manifest if a key set is needed; measure uploads per job; `sa` and `bbg` join only after cb-12 shows their projected per-cycle total under 5 GiB). Ledger `ledger/ROUND87_FIRST_CYCLES_ON_Q_AND_UPLOADER_SIZES_20261016.md`.
- **Design chosen inside the CTO's ruling (named):** a local `silver_known` table in the progress database (key to hash), not an S3 manifest object: dell1 is the single writer for each publisher, and a manifest object would add an S3 read per upload anyway. **Its behaviour change, named:** rows this runtime never appended are unknown to it, so an identical row already in S3 from the site Z era is appended AGAIN if this runtime re-uploads it; consumers read the newest row per key, so a duplicate is not a wrong value, but it is extra storage. Also after a `PreconditionFailed` retry, rows that an earlier incomplete run left in a stale part are written again. Neither is a correctness fault; both are the price of not reading S3.
- **Not in this cell:** the `Uploader` (legacy) class; `silver_from_bronze`; a manifest object; deleting duplicates.
- **Real-job criterion is the issuer's:** after the merge and a re-pin, the ledger's `upload-harvest` lines for `wsj` and `barrons` must read near 0 GETs per upload (against the measured 2.57 MiB and 922 GETs for 5 uploads). The projection for `sa` and `bbg` (the CTO's join gate) is read from the same ledger after they join one at a time under the 5 GiB bar.
- Direct act: ONE cell, LOCAL, about 90 product lines; no L2, L4-R or L8-L10.
- Slot ~148, worktree `C:/dev/wk-harvst-148`, branch `wk-AMGT_HARVST-148`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts`; `lib/research/harvest` and `lib/research/corpus` tests are in the `lib` cone.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>pending</status>
<round>87</round>
<workstream>EGRESS-WRITE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
