# NFRA_OPLGTW task order -- `OG-en-23` -- a windowed partition read converts only the account's rows to Python (round 41; repair of `OG-ap-36` Phase A stop, row Z-S370)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-23</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-23</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~137</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the same objects are read through the same role.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act repairs the two host measurements that failed in `OG-ap-36` Phase A (row Z-S370): the event loop is starved 1 to 3.9 s at a time during a page, and the chain's RSS grows 27.7 MB per page against the live code's 18.3.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-23` (decomposition addendum R3-T.113, round 41, workstream ENRICH-R41-Q)

THE DEFECT (read `app/client_adapter_bd49f.py` `_read_partitions` and `app/typed_scope.py` `read_parquet`, both already in your cone). A windowed 49F read takes each partition of the page with `ctx.read_rows(prefix, part, columns=...)`, which reads the WHOLE partition (every account, about 1 200 rows a day on average and far more on busy days), then `typed_scope.read_parquet` turns the whole table into Python with `json.loads(json.dumps(table.to_pylist(), default=str))`, and only then the adapter's `_fence` keeps the 49F-prefixed ids and a list comprehension keeps the one account's rows. Those three conversions run in C holding the GIL for the whole partition, so each worker thread starves the event loop for seconds even after `OG-en-21` moved the page off the loop, and the transient Python copies of every other account's rows are what the heap retains. The answer needs only (1) the account's rows, (2) the partition's TOTAL row count and (3) the count of rows the fence excludes (the 49F-prefix test), because the answer body reports those two counts as denominators.

THE FIX (code only):
1. In `app/client_core.py` add `Ctx.read_account_rows(prefix, partition, columns, key, id_column, fence_prefix, account_id) -> (kept_rows, total_rows, excluded_rows)`. It loads the object exactly as `typed_scope.read_parquet` does (`typed_scope._load_capped(scope, key)`, then `pq.read_table(io.BytesIO(body), columns=...)`; the over-cap and unknown-column refusals stay as they are) and does the fence and the account test IN ARROW BEFORE any conversion: when the id column's type is string or large_string, `fence_ok` = the id is not null and starts with `fence_prefix` (`pc.starts_with`), `excluded_rows = total_rows - count(fence_ok)`, `match` = `fence_ok` AND the id equals `account_id`; only `table.filter(match).select(columns)` is converted, with the SAME conversion `json.loads(json.dumps(rows, default=str))` so each kept row is identical to the one the old path kept. Row order is the file's order. When the id column is NOT string-typed (an integer, a float, a dictionary), do not guess: take the old path (read every row as `read_rows` does, apply the adapter's own fence rule `str(row.get(id_column) or "").startswith(fence_prefix)` and `str(row.get(id_column) or "") == account_id`) and return the same triple. Free the table before returning (`del`).
2. In the adapter, `_read_partitions.read_one` calls `ctx.read_account_rows(prefix, part, list(columns), key, "account_id", ACCOUNT_PREFIX, account_id)` when `ctx` has it (`getattr`; the key is the `OG-en-22` index key, or None when there is no index; a partition with no key in the index answers `([], 0, 0)`), and otherwise runs the existing code unchanged (the fake contexts of existing tests have no such method). The tuple `read_one` returns stays `(part, kept rows, row count, excluded)` with `row count` = `total_rows`. Keep the sort, cursor, gate, page size, worker count and the `OG-en-22` index untouched.
3. Do not touch `app/tools.py`, `app/typed_scope.py` or any other adapter.

TESTS (new file `tests/test_og_en23.py`; read `tests/test_og_en22.py` and `tests/test_og_en18.py` for the fixtures; build real parquet bytes with pyarrow in memory and patch `typed_scope._load_capped` to return them):
- `test_ogen23_ac01` (the oracle): for a set of synthetic partitions holding ids with the 49F prefix, ids of other prefixes, null ids and empty-string ids, and for each of several target accounts (a present one, an absent one, one in the other-prefix set), `read_account_rows` returns a `(kept, total, excluded)` EQUAL to the old path's (`read_rows` then the adapter's `_fence` then the `str(...) ==` test, `len(read)`); the kept rows are equal dict for dict and in the same order. Include a partition with a date column and a decimal-like column so the `default=str` conversion is exercised.
- `test_ogen23_ac02` (only the account's rows are converted): a spy around the conversion (for example a wrapper on `json.dumps` inside `client_core`) records the number of rows in the list it is asked to dump for a partition of 5 000 rows holding 3 rows of the account: it is 3, never 5 000; and a non-string id column (integer ids) takes the old path and still returns the old path's triple.
- `test_ogen23_ac03` (the adapter): one `get_transactions` page and one `get_fees` page and a full cursor chain over a fake served store return answers EQUAL (rows, counts, `partitions_read`, `fence_excluded`, `next_cursor`) with a ctx that has `read_account_rows` and with a fake ctx that lacks it; a partition with no key answers empty; `READ_WORKERS` and `PAGE_PARTITIONS` are unchanged.
If an existing test pins `read_one`'s calls or the `read_rows` signature, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no registry change, no change to `app/tools.py` or `app/typed_scope.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en23.py
infra/aws/ec2/opal-gateway/tests/test_og_en22.py
infra/aws/ec2/opal-gateway/tests/test_og_en20.py
infra/aws/ec2/opal-gateway/tests/test_og_en19.py
infra/aws/ec2/opal-gateway/tests/test_og_en18.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_core.py`, `app/client_adapter_bd49f.py`, `tests/test_og_en23.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~137/`. Rows: id `NFRA_OPLGTW-Z-W137-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-23"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en23.py test_ogen23_ac01 test_ogen23_ac02 test_ogen23_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-23"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~137 '^infra/aws/ec2/opal-gateway/(app/(client_core|client_adapter_bd49f)\.py|tests/test_og_(en23|en22|en20|en19|en18|en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~137: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-23"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en23set tests/test_og_en4.py tests/test_og_en12.py tests/test_og_cl2.py tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en22.py tests/test_og_en23.py; echo "exit=$?"</invocation><expect>(?s)en23set forward: passed (\d+); failed 0.*en23set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass (the oracle equality, only the account's rows converted, the adapter's answers equal with and without the new method). `AC2`: the commits of this serial touch only the listed files. `AC3`: the eleven window test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-23.convert-only-the-accounts-rows-to-python.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41-Q (decomposition addendum R3-T.113): the repair of the `OG-ap-36` Phase A stop (row Z-S370). The CAUSE is a code reading, INFERRED, not measured: `typed_scope.py:155` converts the whole partition and the adapter filters afterwards (`client_adapter_bd49f.py:341-348`). The measurement that grades it is the applier's, on the host, in the re-run of `OG-ap-36` Phase A (the event-loop probe and the chain's RSS); this worker proves only equality and that only the account's rows are converted. Risk WORLD by the L6 floor. It rides `OG-ap-36`.
- The answer's two denominators (the partition's total row count and the fence-excluded count) are kept exactly, computed in arrow; a non-string id column takes the old path rather than a guessed cast.
- Pre-cut: `AC1` base FAIL as expected (the test file is absent); `AC3` base FAIL (the file is absent).

<status>staged</status>
<round>41</round>
<workstream>ENRICH-R41-Q</workstream>
<slot>~137</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
