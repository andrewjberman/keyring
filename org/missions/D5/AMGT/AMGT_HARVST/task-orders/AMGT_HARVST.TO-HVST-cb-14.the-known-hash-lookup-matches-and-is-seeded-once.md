# AMGT_HARVST task order -- `HVST-cb-14` -- ROUND 87, workstream EGRESS-SEED: THE KNOWN-HASH LOOKUP MATCHES DATE KEYS, AND THE LOCAL RECORD IS SEEDED ONCE FROM S3 (CTO condition C-d3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-14.the-known-hash-lookup-matches-and-is-seeded-once</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~149</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO publisher host, NO Secrets Manager call, NO S3 call in any test (fakes; a fake whose reads you do not expect raises), NO browser, NO collector or runner run, NO scheduled task. The new seed command READS S3 when a person runs it later; your tests never run it against S3.
comp-adversary: RUN at L5 -- the adversary is a lookup that still misses a `date` key (so every re-uploaded `listing_hit` row is appended again), a seed that writes a hash different from the one the uploader computes (so a seeded row is still appended again), a seed that overwrites newer local rows, and a check that passes whatever the data is.
</preflight>

## 0. THE CELL

`HVST-cb-12` (merged `c1df06b1ef`) made the uploader decide "unchanged" from a local table, `silver_known` (`lib/opal_data_harvest/silver_known.py`, keys stored by `encode_key` = `json.dumps(list(key), default=str, sort_keys=True)`, loaded by `load` into `{decode_key(text): hash}`), instead of reading the target silver table from S3. Two defects remain, both found by the issuer reading the merged code, one named by the CTO (C-d3):
1. **A `date` key never matches.** The `listing_hit` table's record key is `("query_sha256", "fetch_date_utc", "search_page", "search_rank", "source")` and `silver_from_bronze.py` (about line 655) sets `row["fetch_date_utc"] = fetched_at.date()`, a `datetime.date`. `encode_key` turns the date into the string `"2026-10-15"`, `decode_key` gives back the STRING, but `store.silver_append` looks up `known.get(record_key)` with a tuple holding the `date` object: no match, so a `listing_hit` row is appended again every time it is uploaded. (The cb-12 test pinned this as a "documented limit"; the limit is wrong for the table that matters most.)
2. **The record starts empty.** A row already in S3 (from the site Z era or from this runtime before the re-pin) is unknown to `silver_known`, so an identical row it uploads is appended again. The CTO's condition C-d3: before the first upload to a table under the new pin, `silver_known` must hold that table's existing keys, seeded once; the first uploads' record must state the seed source and 0 duplicate keys written.
This cell fixes (1), adds a one-off seed command and a no-duplicates check for (2), and changes nothing else.

## 1. THE BUILD (LOCAL, about 120 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. `lib/opal_data_harvest/silver_known.py`: make the lookup normalise its key. `load(db, source, table)` returns an object of a small class `KnownMap` (define it in the module) that holds `{encode_key(k_tuple_as_decoded): hash}` keyed by the ENCODED TEXT, and implements `get(key_tuple, default=None)`, `__contains__`, `__len__` and `__iter__` over the encoded texts; `get` encodes the lookup tuple with `encode_key` before looking it up, so a tuple holding a `datetime.date`, `datetime.datetime`, string, int or `None` matches the stored text of the same value. `encode_key`, `decode_key`, `ensure` and `note` keep their behaviour and signatures. `store.silver_append` already uses only `known.get(record_key)` (do not edit `store.py`).
b. New module `lib/opal_data_harvest/seed_silver_known.py`, a command `python -m lib.opal_data_harvest.seed_silver_known seed --runtime-root <dir> --publishers wsj barrons [--dry-run]` and `... check --runtime-root <dir> --publishers wsj barrons --since <UTC ISO ending Z>`:
   - the tables are exactly those the `HarvestUploader` appends: `article` with key fields `("article_key",)` and `listing_hit` with key fields `("query_sha256", "fetch_date_utc", "search_page", "search_rank", "source")`; keep them in ONE module constant `UPLOADER_TABLES` and name the file `uploads.py` lines in its comment (do NOT import from `uploads.py` and do not edit it); the source of a publisher is `harvest_grammar.SOURCE_FOR_PUBLISHER[publisher]`;
   - `seed`: for each (publisher, table) it calls `store.silver_latest(source, table, key_fields)` ONCE (the one place this command reads S3), and `silver_known.note(db, source, table, [(key_tuple, row["record_hash"]) ...])` where `db` is `sqlite3.connect(<runtime-root>/progress.sqlite3)` and `key_tuple = tuple(row.get(f) for f in key_fields)`; rows without a `record_hash` are skipped and counted; an existing local `silver_known` entry for a key is NOT overwritten (a newer local hash wins: skip keys already present); it prints one line per table: `SEED source=.. table=.. keys_seeded=.. keys_already_local=.. rows_without_hash=.. s3_gets=.. s3_bytes=..` (from `store.get_stats_snapshot()` deltas), and it also writes `<runtime-root>/silver_known_seed.json` with `{"seeded_at": <UTC ISO>, "tables": {"<source>/<table>": {"keys": <n>, "hashes": {"<encode_key text>": "<hash>"}}}}` (the snapshot the `check` reads; merge into an existing file by table). `--dry-run` reads and prints but writes neither the database nor the snapshot. It does NOT probe any lock: the caller stops the runner first, and the module docstring says so;
   - `check`: for each (publisher, table) it LISTS the table prefix (`list_objects_v2`, paginated) and GETs only the parts whose `LastModified` is `>= --since`, reads their rows, and for each row takes `(encode_key(key_tuple), row["record_hash"])` (rows without the column are skipped and counted); counts rows whose `(key text, hash)` is present in the snapshot file's `hashes` for that table (a DUPLICATE: the same row already existed at seed time and was written again). It prints one line per table: `CHECK source=.. table=.. parts_read=.. rows=.. duplicates=.. new_keys=..`, then a final line `DUPLICATES=<total>`; exit 0 when total is 0, exit 1 otherwise;
   - `main(argv=None)` returns the exit code; `__main__` guard calls it.
c. New test `lib/opal_data_harvest/test_cb14_known_lookup_and_seed.py` (no network; temp directories and `sqlite3`; a fake S3 client with `get_paginator`/`get_object`/`put_object` serving in-memory parquet parts built with `pyarrow` the way `lib/research/harvest/tests/test_store.py` builds them; reuse its helpers):
   - (1) `KnownMap.get` matches a key tuple holding a `datetime.date` after a `note` of the same key: `note(db, "s", "listing_hit", [(("q", date(2026,10,15), 1, 2, "barrons"), "h1")])`, `load(...)` then `.get(("q", date(2026,10,15), 1, 2, "barrons")) == "h1"`; the same with a `datetime`; a key that differs by one element returns None; `load` of a fresh database is empty and falsy;
   - (2) END TO END: `_silver_append_retrying_object_name` (from `uploads.py`) with `known_db=db`, a fake client that raises on any `get_object`/`get_paginator`, and `listing_hit` rows whose `fetch_date_utc` is a `date`: the first call writes them, a second call with the SAME rows writes NOTHING (zero `put_object`). This is the arm that fails on the cb-12 code;
   - (3) `seed`: with a fake client holding two `article` parts and one `listing_hit` part (rows carry `record_hash`, as `silver_append` writes them), `main(["seed", ...])` seeds exactly the distinct keys, prints the `SEED` lines with `s3_gets` equal to the parts read, writes the snapshot file, and a following `_silver_append_retrying_object_name(..., known_db=db)` of the SAME rows writes NOTHING; a row with the same key and a DIFFERENT hash IS written; `--dry-run` writes neither the database nor the snapshot; a local entry already present is not overwritten;
   - (4) `check`: after (3), append one genuinely new row and one row identical to a seeded one through the known path (the second is skipped, so only the new one is written), run `check --since` the test's start time: `DUPLICATES=0`; then write an identical seeded row into a new part DIRECTLY (bypassing the known path) and run `check` again: `DUPLICATES=1` and exit 1;
   - (5) **A MUTANT:** with `KnownMap.get` monkeypatched to look up the RAW tuple (no `encode_key`), arm (2) FAILS (assert that it does). This proves (2) discriminates.
   - Update the cb-12 test that pinned the old limit: in `lib/opal_data_harvest/test_cb12_uploader_known_hashes.py` the test that asserts a datetime-valued key does NOT round-trip must now assert it DOES match through `load(...).get(...)`, and any assertion that compares `load(...)` to a plain dict must compare through `.get` or `dict(...)` of the encoded texts; change nothing else in that file.
2. Do not run anything against a publisher, S3, Secrets Manager or any box; do not launch a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/silver_known.py
lib/opal_data_harvest/seed_silver_known.py
lib/opal_data_harvest/test_cb14_known_lookup_and_seed.py
lib/opal_data_harvest/test_cb12_uploader_known_hashes.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~149/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-14"><invocation>python -m pytest lib/opal_data_harvest/test_cb14_known_lookup_and_seed.py lib/opal_data_harvest/test_cb12_uploader_known_hashes.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-14"><invocation>python -m pytest lib/research/harvest/tests/test_store.py lib/research/harvest/tests/test_o3_silver_tie_break.py lib/research/harvest/test_at4_silver_union_keys.py lib/opal_data_harvest/test_ai5_batched_silver_append.py lib/opal_data_harvest/test_at1_batched_listing_upload.py lib/opal_data_harvest/test_eg1_silver_cache.py lib/opal_data_harvest/test_retrieval_provenance.py lib/opal_data_harvest/test_silver_from_bronze.py lib/opal_data_harvest/test_legacy_upload.py lib/opal_data_harvest/test_au1_upload_timeout.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^110 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2 reads exactly `110 passed`: the base's own count after `HVST-cb-12` (issuer, main tree, 2026-10-16 ~02:4xZ). A sparse worktree may differ: if your worktree's base count differs, say so with both counts and do not weaken the pattern.
- **Dry-run at the base (issuer, dell1):** AC1 base FAIL as expected (`no tests ran` for the new file: it does not exist, and the cb-12 file's updated test is not yet updated); AC2 base PASS as expected (`110 passed`).
- Before and after, run the full `lib/opal_data_harvest` suite and record both counts. On a clean main checkout one failure is known (`test_bn1_names_made_whole.py::test_v_building_twice...`, CRLF against LF on disk); a sparse worktree also shows `test_harvest_grammar.py::test_one_writer_for_both_channels` (a missing import outside the cone). Add none.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W149-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~149/AMGT_HARVST.TO-HVST-cb-14.the-known-hash-lookup-matches-and-is-seeded-once.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cb-14.the-known-hash-lookup-matches-and-is-seeded-once` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cb-14.the-known-hash-lookup-matches-and-is-seeded-once.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO addendum 3 and condition C-d3 (msg 6396): before the first upload to a table under the new pin, `silver_known` holds that table's existing keys, seeded once; the first uploads' record states the seed source and 0 duplicate keys written; a duplicate is Branch F. The date-key defect is this issuer's reading of `store.silver_append`'s `known.get(record_key)` against `encode_key`'s `default=str` and `silver_from_bronze.py:655`; it is MY miss in the cb-12 cut (I named the datetime limit as acceptable without reading what the `listing_hit` key holds).
- **Where the seed runs (not in this cell):** the executor `0.7.0_AE_CloudOps~SC1`, at the re-pin act, with the runner STOPPED, as `python -m lib.opal_data_harvest.seed_silver_known seed --runtime-root C:\dev\ajb_workspace\.runtime\harvest-cycle\runtime --publishers wsj barrons`, once, before the first start under the new pin; then `check --since <T0>` after the first uploads. The seed reads each table once (wsj `article` 125.4 MiB, barrons `article` 9.9 MiB and `listing_hit` 3.2 MiB, wsj `listing_hit` 0.1 MiB: about 139 MiB in all, one time).
- **Direct act:** ONE cell, LOCAL, about 120 product lines; no L2, L4-R or L8-L10. The real-job criterion is the issuer's dry run: `seed --dry-run` against the real bucket for `barrons` (read-only, about 13 MiB) after the merge, printing the SEED lines.
- Slot ~149, worktree `C:/dev/wk-harvst-149`, branch `wk-AMGT_HARVST-149`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts`.

**COMPLETE 2026-10-16 ~03:0xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~149` (worker-light, haiku, high), branch `wk-AMGT_HARVST-149`, build `28309f6547`, head `48ed1e7591`. Diff read by this seat: `silver_known.py` (+41/-?: `KnownMap` keyed by the encoded text, `get` and `__contains__` encode the lookup tuple, so a `date` or `datetime` key matches; `load` returns it; `encode_key`, `decode_key`, `ensure`, `note` unchanged), `seed_silver_known.py` (new, 217 lines: `seed` does ONE `store.silver_latest` per (publisher, table) of `UPLOADER_TABLES`, notes only keys the local record lacks, writes the snapshot; `--dry-run` writes neither; `check` lists, GETs only parts with `LastModified >= --since`, counts a row whose (key text, hash) is in the snapshot as a DUPLICATE, prints `DUPLICATES=<n>`, exit 1 when not 0, exit 2 with no snapshot), the cb-12 test that pinned the old limit now asserts the match (15 insertions, 12 deletions in that file only).
- **AC1 PASS:** `18 passed` (worker; this seat re-ran). **AC2 PASS:** `110 passed` (worker; this seat re-ran). Proof instance VALID rc 0 (re-run here); ruff clean. Suite per the worker: `lib/opal_data_harvest` before 887 passed / 1 failed (sparse import) / 3 skipped, after 896 / 1 / 3.
- **Rows** `D1-W149-S1` (ARMED, my disarm: `check --since` must open AFTER the seed, carried into the re-pin order), `-S2`, `-S3`, `-S4` (INERT notes); dispositioned by the issuer's row after the merge.
- **What this does NOT prove:** a seed or a check against the real bucket. The issuer's dry run (`seed --dry-run`, `barrons`) and the executor's seed at the re-pin are the real reads.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>complete</status>
<round>87</round>
<workstream>EGRESS-SEED</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
