# NFRA_OPLGTW task order -- `OG-en-18` -- repair: a window page keeps only the account's rows per partition, pages of 30, and one windowed read in flight per process (round 40; found by the applier's Phase A measurement of `OG-ap-32`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-18</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-18</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~130</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the adapter reads the same prefixes through the same dedicated role.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act repairs the issuer's own `OG-en-17` after the applier's measurement on the host (`~NFRA1`, Phase A of `OG-ap-32`): a 60-partition page holds all its rows at once, +470 to +550 MB on a host where one such page is 55 to 59 percent used and two overlapping pages 85 to 100 percent (no swap, no code limit); transactions rate predicts a first page of about 43 s against the 60 s ALB idle timeout.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-18` (decomposition addendum R3-T.104, round 40, workstream ENRICH-R40-R)

THE DEFECT. In `app/client_adapter_bd49f.py` (read the whole file first), `_read_partitions` reads every partition of a page with `ThreadPoolExecutor(16)` and RETURNS a list of every partition's FULL row list; `_window_read` then fences and `get_transactions`/`get_fees` filter to the account afterwards. So a 60-partition page keeps about 60 partitions of other accounts' rows in memory until the end (measured on the host: +470 to +550 MB per page; a transactions partition is about 1 MB on disk and about 14,000 rows in memory). Two overlapping pages nearly exhaust the 2 vCPU host. Also, at the measured throughput (about 0.72 s per file), a 60-file page takes about 43 s for transactions, over the 30 s budget the issuer set (the ALB idle timeout is 60 s).

THE FIX (code only):
1. **Filter inside the worker.** Each pool task reads ONE partition, then immediately fences it (`_fence`) and keeps ONLY the rows of the requested account (`str(row.get("account_id") or "") == bd_id`, the filter the callers apply today), and returns `(part, kept_rows, partition_row_count, fence_excluded)` so the full row list of that partition is dropped when the task returns. Change `_read_partitions`/`_window_read` (and their callers `get_transactions` and `get_fees`) to pass the account id in and to build the answer from the kept rows; the answer's `denominator.partition_rows` still sums the partition row counts and `fence_excluded` still sums the exclusions, so every figure of today's answer stays equal for the same data. The retained memory per page is then the account's rows plus at most `READ_WORKERS` (16) partitions in flight, never the whole page.
2. **Pages of 30.** `PAGE_PARTITIONS = 30` (was 60). The cursor semantics are unchanged (`next_cursor` the day before the oldest partition read; `to_date` pages back).
3. **One windowed read in flight per process.** A module-level `threading.BoundedSemaphore(1)` (`WINDOW_READ_GATE`) wraps the whole windowed read of `get_transactions` and `get_fees`. A call that cannot take the gate within `WINDOW_GATE_WAIT_SECONDS = 15` returns, with NO partition read, the answer `_absent(..., "window_read_busy", ...)` shape of the file (empty rows, `absent_reason: "window_read_busy"`, `retry_after_seconds: 15`), never an exception and never a long wait past the ALB budget. The single-partition and `snapshot` paths do not take the gate.
Change no admission, no fence, no other adapter, no tool signature and nothing in `app/tools.py` or `app/client_core.py`.

TESTS (new file `tests/test_og_en18.py`; read `tests/test_og_en17.py` for the fake-ctx fixtures; the fake ctx records each key read and counts partition row lists that are alive at once through a list subclass with a finalizer):
- `test_ogen18_ac01`: 396 planted daily partitions of 5,000 rows each, 5 of them the requested account's. One page answers with the account's rows only, `partition_rows` equal to the sum of the rows the page read, and the number of full partition row lists alive at the same moment never exceeds 16 (`READ_WORKERS`) at any point of the call.
- `test_ogen18_ac02`: `PAGE_PARTITIONS` is 30: the first page of a 396-partition window reads exactly 30 and returns a cursor; paging with `to_date=<next_cursor>` until it is null reads every partition exactly once and returns every account row exactly once; `get_fees` behaves the same.
- `test_ogen18_ac03`: with one windowed read blocked mid-flight (a fake read waiting on an event), a second call (patch `WINDOW_GATE_WAIT_SECONDS` to 0.2) returns `window_read_busy` with ZERO partition reads; after the first finishes a third call succeeds; a call that fails inside the gate releases it (the next call is not blocked).
If an existing test pins `PAGE_PARTITIONS` 60, the 60-file first page, or `_read_partitions`/`_window_read` shapes, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change, no change to `app/tools.py` or `app/client_core.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en18.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_adapter_bd49f.py`, `tests/test_og_en18.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~130/`. Rows: id `NFRA_OPLGTW-Z-W130-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-18"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en18.py test_ogen18_ac01 test_ogen18_ac02 test_ogen18_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-18"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~130 '^infra/aws/ec2/opal-gateway/(app/client_adapter_bd49f\.py|tests/test_og_(en18|en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~130: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-18"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/en18.AC3.sh; echo "exit=$?"</invocation><expect>(?s)en4, en12, cl2, en13, en15, en17, en18 forward: passed (\d+); failed 0.*reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only the listed files. `AC3`: the window test files pass together in both orders with the same count (a test must not depend on what ran before it).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-18.49f-window-memory-and-page-size.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40 repair, workstream ENRICH-R40-R (decomposition addendum R3-T.104). Risk WORLD by the L6 floor (a gateway infrastructure path); no deploy in this cell; it replaces `OG-en-17`'s page of 60 before `OG-ap-32` goes to its halves (release `11031f278d` is superseded; a new Phase A GO follows the merge).
- The 30-file page and the 15 s gate wait are the issuer's numbers from the measured rates (0.72 s per file: about 22 s for 30 transactions files; +235 to +275 MB if all rows were kept, far less once filtered in the worker). The CTO reads them at the round analysis.
- Pre-cut: `en18.AC3` is a generic both-order check (`_named`-style); AC1/AC2 base FAIL as expected (the test file is absent; no commit of this serial yet).

<status>staged</status>
<round>40</round>
<workstream>ENRICH-R40-R</workstream>
<slot>~130</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
