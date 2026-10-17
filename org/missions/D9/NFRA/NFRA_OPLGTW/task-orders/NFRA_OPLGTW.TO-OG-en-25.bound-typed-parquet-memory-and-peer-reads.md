# NFRA_OPLGTW task order -- `OG-en-25` -- a typed Parquet read can no longer turn a small object into gigabytes of Python, and `etfs_compare_peers` reads only what it answers (round 41; repair of the ARMED hazard row Z-S375, CTO decision 35541)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-25</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-25</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~139</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the same objects are read through the same roles.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's decision 35541 on row Z-S375: "bound etfs_compare_peers's memory, or refuse above a size, proven in a fresh process".
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-25` (decomposition addendum R3-T.116, round 41, workstream ENRICH-R41-T)

THE DEFECT (read `app/typed_scope.py` `read_parquet` and `app/etfs_rivals_flow.py` `_peer_section`, `_read_dates`, `_read_part`, all in your cone). `typed_scope.read_parquet(scope, key, columns, filters)` caps the COMPRESSED object at `scope.max_bytes` (the S3 read), reads the whole table with `pq.read_table`, applies any filters in Arrow, and then converts ALL remaining rows to Python with `json.loads(json.dumps(table.to_pylist(), default=str))`: three GIL-holding passes in which a table of modest compressed size becomes gigabytes of dicts. `etfs_rivals_flow._peer_section` (the `etfs_compare_peers` tool) calls `_read_dates(scope, tool, parts, [newest])` with NO filter and NO column list on the gold `buying_trend` and `holding_contribution` tables, filters to the home fund's group, period and axis in Python afterwards, and derives `available_periods` and `available_axes` from the whole part. On 2026-10-17 at 17:21Z one such call took the 1.8 GB gateway host out of memory (the kernel killed the gateway and eight system daemons; row `Z-S375`). The same class of read (a whole table to Python) is the root cause that `OG-en-23` already fixed for the 49F window.

THE FIX (code only, two layers):
1. In `app/typed_scope.py` `read_parquet`: after the Arrow table is read and the filters and the column select are applied, and BEFORE `to_pylist`, compare the table's in-memory size (`table.nbytes`) with a new module constant `TYPED_MAX_TABLE_BYTES = 64 * 1024 * 1024` (the Python copy of a table is many times its Arrow size, so 64 MB of Arrow is the bound for one answer); above it raise the SAME refusal the compressed cap raises (`TypedOverCap`, with a message that says the filtered table is over the in-memory cap and names the byte counts, never a row value), so every typed reader refuses and none builds the Python copy. Add `distinct_values(scope, key, columns) -> dict` (additive; column name to a sorted list of the DISTINCT non-null values as strings), computed in Arrow with `pc.unique` on a column-projected read of only those columns and never converted row by row (its own bound: a column whose distinct count exceeds 5 000 returns the first 5 000 sorted and a `truncated` marker in a second dict `{"truncated": [names]}` returned as the second element of a tuple; keep the signature `(values, truncated)`).
2. In `app/etfs_rivals_flow.py` `_peer_section`: read the newest part with the filters in Arrow (`fund_id` in the group's funds, `period` equal, `axis` equal, as `("fund_id", "in", funds)`, `("period", "=", period)`, `("axis", "=", axis)`, through `_read_dates(..., flt=...)`), take `rows_in_part` from the unfiltered total that `read_parquet` already returns, and take `available_periods` and `available_axes` from `ts.distinct_values` over the `period` and `axis` columns of the same key. A section's answer for a VALID period and axis must be IDENTICAL to today's (same rows, same order, same `rows_matched`, `rows_not_shown`, `rows_in_part`, `available_periods`, `available_axes`, `absent_reason`). When the table is over the in-memory cap the tool answers its existing refusal shape for `TypedOverCap` (read how the module already handles `ts.TypedOverCap` at the end of `etfs_compare_peers`), not a crash and not a MemoryError.
3. Do not touch the other readers of `typed_scope.read_parquet` except through the new bound (it protects them all); do not change `app/tools.py`, the catalog or any deploy file.

TESTS (new file `tests/test_og_en25.py`; read `tests/test_og_rv2.py` for the fixtures of the peer tools and `tests/test_og_en23.py` for building Parquet bytes in memory with pyarrow and patching `typed_scope._load_capped`):
- `test_ogen25_ac01` (the cap): a table whose Arrow `nbytes` is above `TYPED_MAX_TABLE_BYTES` (patch the constant down to a few KB and use a small table) makes `read_parquet` raise `TypedOverCap` BEFORE `to_pylist` is called (a spy on `json.dumps` in `typed_scope` records zero calls), with and without filters; a table under the cap returns exactly the rows it returned before; a filter that leaves few rows from a big table passes the cap (the cap is on the FILTERED table).
- `test_ogen25_ac02` (the peer read answers the same): for synthetic `buying_trend` and `holding_contribution` partitions (several funds, several periods and axes, rows for funds outside the group), `etfs_compare_peers` through the REAL module path answers a body EQUAL to the one the base code answered (build the expected body with the old logic inline in the test: the full-table Python filter) for a valid period and axis, for a period the part does not hold (empty section with `available_periods` and `available_axes` listed) and for an axis it does not hold.
- `test_ogen25_ac03` (only what it answers is converted, and a fresh process holds the line): a spy on `json.dumps` in `typed_scope` shows that for a 200 000-row synthetic `buying_trend` part the rows converted are the matched rows only (a few hundred at most), never 200 000; and a test that launches a FRESH Python subprocess (`subprocess.run([sys.executable, "-I", "-c", ...])`) which builds a synthetic part of at least 1 000 000 rows in a temp file, calls the `etfs_compare_peers` read path with an unrecognised period and axis (the call that ran away on the host) with `_load_capped` patched to the file's bytes, and reports (as one JSON line on stdout) the answer's refusal or empty-section shape and the process's PEAK Python heap from `tracemalloc` with Arrow memory from `pyarrow.total_allocated_bytes()` sampled at the end: the test asserts exit 0, the shape is the refusal or an empty section with the available values, and the peak Python heap is under 300 MB. If the host's `psutil` or `resource` is available you may also record peak RSS, but the assertion is the tracemalloc number.
If an existing test pins the old unfiltered read of the peer tables (for example by counting rows passed to a fake `read_parquet`), update it to the new truth with the smallest edit and name it in your report; never weaken any other test.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no registry change, no change to `app/tools.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/etfs_rivals_flow.py
infra/aws/ec2/opal-gateway/tests/test_og_en25.py
infra/aws/ec2/opal-gateway/tests/test_og_rv2.py
infra/aws/ec2/opal-gateway/tests/test_og_gt6.py
infra/aws/ec2/opal-gateway/tests/test_og_en23.py
infra/aws/ec2/opal-gateway/tests/test_og_en22.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/typed_scope.py`, `app/etfs_rivals_flow.py`, `tests/test_og_en25.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~139/`. Rows: id `NFRA_OPLGTW-Z-W139-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-25"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en25.py test_ogen25_ac01 test_ogen25_ac02 test_ogen25_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-25"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~139 '^infra/aws/ec2/opal-gateway/(app/(typed_scope|etfs_rivals_flow)\.py|tests/test_og_(en25|rv2|gt6|en23|en22|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~139: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-25"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en25set tests/test_og_rv2.py tests/test_og_gt6.py tests/test_og_cl2.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_en25.py; echo "exit=$?"</invocation><expect>(?s)en25set forward: passed (\d+); failed 0.*en25set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass (the in-memory cap before any conversion; the peer answer identical for valid and absent values; only the answered rows converted, and a fresh process stays under the heap bound on the call that ran away). `AC2`: the commits of this serial touch only the listed files. `AC3`: the window, peer and client test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-25.bound-typed-parquet-memory-and-peer-reads.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, the list of other readers of `read_parquet` that the new cap now protects (names and counts only), each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41-T (decomposition addendum R3-T.116): the CTO's decision 35541 on row `Z-S375` (ARMED, disarm owner this seat): cut the fix cell now; "bound `etfs_compare_peers`'s memory, or refuse above a size, proven in a fresh process", plus a `MemoryMax` on the gateway unit (`OG-un-1`). Each ships under its own never-widen (a later release).
- The CAUSE is a code reading, INFERRED, not measured on the host: the unfiltered whole-table `to_pylist` of the newest part of the gold peer tables (`_peer_section`), the same class as `OG-en-23`; what changed since the 05:19Z 27-of-27 read is not measured (the data behind the gold tables is the first suspect, unmeasured). The measurement that grades the fix is the applier's in the release's Phase A, on the host, with a HARD GUARD (never an unguarded call: the host is a 1.8 GB single-worker box); this worker proves the bound offline.
- Pre-cut: `AC1` and `AC3` base FAIL as expected (the test file is absent).

<status>complete</status>
<round>41</round>
<workstream>ENRICH-R41-T</workstream>
<slot>~139</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
