# NFRA_OPLGTW task order -- `OG-en-26` -- a filtered typed Parquet read STREAMS by batch and an unfiltered one is refused BEFORE it reads; the peer tables' lineage column is measured, never loaded (round 41; repair of `OG-ap-38` Phase A stop, row Z-S380)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-26</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-26</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~141</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the same objects are read through the same roles.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act repairs the `OG-ap-38` Phase A stop (row `Z-S380`, applier msg 35555): under a hard guard the candidate `etfs_compare_peers` still raised MemoryError inside `pyarrow.parquet.read_table`, peak 724 MB (the live code 927 MB), because `read_parquet` reads the WHOLE object before it filters and the in-memory cap runs after the read.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-26` (decomposition addendum R3-T.118, round 41, workstream ENRICH-R41-W)

THE DEFECT (read `app/typed_scope.py` `read_parquet` and `distinct_values`, and `app/etfs_rivals_flow.py` `_peer_section`, `_read_part`, `_norm`, all in your cone; `OG-en-25` put the filters and the 64 MB cap there). `read_parquet` calls `pq.read_table(io.BytesIO(body), columns=read_cols)` and only THEN filters and checks `table.nbytes`, so the whole object is in memory before any bound applies; when `columns` is None (the peer tables) that is EVERY column. The gold peer tables carry the lineage column `input_manifest` (a JSON list of every input key, up to about 100 KB a row; `_norm` replaces it by its byte count `input_manifest_bytes` and drops it): that column is the bulk of the table and the answer never needs its value, only its length for the few matched rows.

THE FIX (code only):
1. In `app/typed_scope.py` `read_parquet`, open the object once as `pq.ParquetFile(io.BytesIO(body))` and take `num_rows` and the schema from its metadata (the unknown-column `ValueError` stays as is; `total_rows` stays the unfiltered row count, from `metadata.num_rows`).
   - NO FILTERS (the whole table is the answer): BEFORE reading any data, estimate the in-memory size as the sum of `column_chunk.total_uncompressed_size` over the projected columns and all row groups (`metadata.row_group(i).column(j)`); when it exceeds `TYPED_MAX_TABLE_BYTES`, raise the same `TypedOverCap` as today WITHOUT having read a row group (name the byte counts in the message, never a value). Below it, read as today.
   - WITH FILTERS: STREAM. Iterate `pf.iter_batches(batch_size=2048, columns=read_cols, use_threads=False)`; for each batch build the same mask the code builds today (`=`, `<`, `>`, `in`, through `harvest_typed._typed_value`), keep only the matching rows (`batch.filter(mask)`), append the filtered batches to a list, and drop the batch; after the loop build ONE table from the kept batches; if its `nbytes` exceeds `TYPED_MAX_TABLE_BYTES` raise `TypedOverCap`; then the same column select and the same `json.loads(json.dumps(rows, default=str))` conversion as today. The Arrow memory at any moment is one batch plus the matched rows, not the table. Rows keep the file's order.
2. Add an optional keyword `length_columns=()` to `read_parquet`: for each named column, do NOT put its value in the result; instead each returned row carries `<column>_bytes` = `len(str(value or "").encode("utf-8"))` of that row's value (exactly what `_norm` computes for `input_manifest` today, including 0 for a null). Compute it ON THE MATCHED ROWS ONLY: when the column is `string` or `large_string`, in Arrow (`pc.binary_length` of the cast to binary, `fill_null(0)`); for any other type, convert only the matched rows' values of that column to Python and apply the formula. The column is read in the same streamed batches (it may not be in `columns`; add it to the read list internally) and is dropped from each batch right after its lengths are taken for the matched rows.
3. In `app/etfs_rivals_flow.py` `_peer_section` (and `_read_part` / `_read_dates` only as far as they must pass the new keyword through), read the peer tables with `length_columns=("input_manifest",)` in addition to the `OG-en-25` filters; `_norm` then finds `input_manifest_bytes` already set and no `input_manifest` key, and must leave it alone. The section's answer for a valid period and axis, and for absent values, must be IDENTICAL to the answer of the code before this cell (rows, order, `input_manifest_bytes` values, `rows_matched`, `rows_not_shown`, `rows_in_part`, `available_periods`, `available_axes`, `absent_reason`).
4. `distinct_values`: iterate `pf.iter_batches(batch_size=8192, columns=<the named columns>, use_threads=False)` and take `pc.unique` per batch, keeping a running set of strings capped at `DISTINCT_LIMIT` as today (same output); it must not hold the whole column. Its metadata pre-check uses the same uncompressed estimate over the named columns only.
5. Do not touch any other file than `<paths>`; do not change the cap values, the refusal class or any other reader's call.

TESTS (new file `tests/test_og_en26.py`; read `tests/test_og_en25.py` for the patching of `typed_scope._load_capped` and the fresh-subprocess pattern, and `tests/test_og_en23.py` for building Parquet bytes with pyarrow; write synthetic files with MANY row groups (`row_group_size` of a few thousand rows) and a long-string `input_manifest` column):
- `test_ogen26_ac01` (refused BEFORE it reads): an unfiltered `read_parquet` of a table whose projected uncompressed metadata size is above `TYPED_MAX_TABLE_BYTES` (patch the constant down) raises `TypedOverCap` and a spy on `pq.ParquetFile.read_row_group`, `.read` and `.iter_batches` records ZERO calls; with a projection of only small columns that fit the cap the same file reads normally.
- `test_ogen26_ac02` (streams, and equals the whole-table answer): for a filtered read over the synthetic file, the rows returned EQUAL (dict for dict, same order) the rows a reference whole-table computation returns (read the whole file with `pq.read_table`, filter in Python); the `input_manifest_bytes` values equal `len(str(v or "").encode("utf-8"))` of the reference's `input_manifest` for each matched row, with a null value giving 0 and a non-string (list-typed) lineage column handled by the fallback; and in a FRESH subprocess (`sys.executable -I`) over a synthetic file of at least 400 000 rows with a 2 KB `input_manifest`, the Arrow pool's PEAK (`pyarrow.default_memory_pool().max_memory()`) after the streamed filtered read is under 25 percent of the file's total uncompressed bytes (read from the metadata) and the process exits 0.
- `test_ogen26_ac03` (the peer tool through the real path): `etfs_compare_peers` with the module's own fixtures (`tests/test_og_rv2.py`) answers a body EQUAL to the pre-cell answer for a valid period and axis, for a period the part does not hold and for an axis it does not hold, with `input_manifest_bytes` present and no `input_manifest` key; and `distinct_values` on the synthetic multi-row-group file returns the same sorted values as the whole-column reference without holding the whole column (the Arrow pool peak in a fresh subprocess is under 5 percent of the column's uncompressed bytes).
If an existing test pins the whole-table read (the `OG-en-25` tests do), update it to the new truth with the smallest edit and name it in your report; never weaken any other test.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no registry change, no change to `app/tools.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/etfs_rivals_flow.py
infra/aws/ec2/opal-gateway/tests/test_og_en26.py
infra/aws/ec2/opal-gateway/tests/test_og_en25.py
infra/aws/ec2/opal-gateway/tests/test_og_rv2.py
infra/aws/ec2/opal-gateway/tests/test_og_gt6.py
infra/aws/ec2/opal-gateway/tests/test_og_en23.py
infra/aws/ec2/opal-gateway/tests/test_og_en22.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/typed_scope.py`, `app/etfs_rivals_flow.py`, `tests/test_og_en26.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~141/`. Rows: id `NFRA_OPLGTW-Z-W141-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-26"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en26.py test_ogen26_ac01 test_ogen26_ac02 test_ogen26_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-26"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~141 '^infra/aws/ec2/opal-gateway/(app/(typed_scope|etfs_rivals_flow)\.py|tests/test_og_(en26|en25|rv2|gt6|en23|en22|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~141: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-26"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en26set tests/test_og_rv2.py tests/test_og_gt6.py tests/test_og_cl2.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_en25.py tests/test_og_en26.py; echo "exit=$?"</invocation><expect>(?s)en26set forward: passed (\d+); failed 0.*en26set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass (refused before reading; streamed and equal to the whole-table answer with a bounded Arrow peak; the peer tool's answer identical with the lineage measured, not loaded). `AC2`: the commits of this serial touch only the listed files. `AC3`: the peer, window and client test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-26.stream-typed-parquet-reads-by-batch.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, the Arrow pool peaks measured in the fresh subprocesses (bytes), each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41-W (decomposition addendum R3-T.118): the repair of the `OG-ap-38` Phase A stop (row `Z-S380`, msg 35555). The measured facts: under the hard guard the candidate raised MemoryError in `pyarrow.parquet.read_table` at a 724 MB peak, the live code at 927 MB; `OG-en-25`'s cap ran after the read. The cause the issuer reads in the code (INFERRED): the unprojected whole-table Arrow read dominated by the lineage column `input_manifest` (the module itself says up to about 100 KB a row). The measurement that grades the fix is the applier's re-run of Phase A (a) on the host under the guard.
- `OG-ap-38` is amended (A1) in the same issuance: its guard may be a cgroup limit (`systemd-run --scope -p MemoryMax=1400M`) as well as the address-space limit, because the applier measured that pyarrow cannot start its thread pools under `RLIMIT_AS` (virtual address space); the guard's PURPOSE (the process is the first victim and cannot take the service or a daemon) is unchanged.
- Pre-cut: `AC1` and `AC3` base FAIL as expected (the test file is absent).

<status>staged</status>
<round>41</round>
<workstream>ENRICH-R41-W</workstream>
<slot>~141</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
