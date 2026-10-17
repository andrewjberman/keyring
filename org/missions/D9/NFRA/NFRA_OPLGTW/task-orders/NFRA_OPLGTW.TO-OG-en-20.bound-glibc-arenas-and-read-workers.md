# NFRA_OPLGTW task order -- `OG-en-20` -- repair: bound the allocator's per-thread arenas and the page's read workers, so memory stays flat across paged 49F reads (round 40; found by `OG-ev-4`, row Z-S342, answering Z-S338)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-20</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-20</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~132</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act follows the applier's host measurement `OG-ev-4` (`~NFRA1`, release app b124377b41 in fresh processes, three pages each, median RSS growth in MB per page): as released 135.9; plus gc and the pyarrow pool release 146.8; plus `malloc_trim` 110.7; `MALLOC_ARENA_MAX=2` 26.7 (page 3 grew only 3.2); the system pool 104.5; 4 read workers 42.4. Wall time moved under 20 percent in every variant. The supported cause is glibc's per-thread arenas: every page builds a new 16-thread pool and each thread's arena keeps what it freed.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-20` (decomposition addendum R3-T.107, round 40, workstream ENRICH-R40-N)

THE DEFECT. In `app/client_adapter_bd49f.py` (read the whole file first; `OG-en-19` has changed the order of a page's rows, read it merged), `_read_partitions` builds a `ThreadPoolExecutor(max_workers=READ_WORKERS)` of 16 threads for every page. Under glibc each thread takes its own malloc arena and keeps freed memory, so the service's memory climbs about 110 to 165 MB per page and is not returned (host: 1846 MB, no swap; a four-page chain reached 87.1 percent).

THE FIX (code only; the environment, the deploy script and the service unit do NOT change, so no env key is added):
1. **Cap the arenas in code.** A module-level function `_tune_allocator()`, called ONCE at module import, that on Linux asks glibc for at most 2 arenas: `ctypes.CDLL("libc.so.6").mallopt(M_ARENA_MAX, ARENA_LIMIT)` with `M_ARENA_MAX = -8` and `ARENA_LIMIT = 2` (named constants). It returns True when `mallopt` returns 1, False otherwise, and NEVER raises: where libc is absent (Windows, macOS), `ctypes` fails, or `mallopt` is missing, it returns False. A second call does nothing (idempotent). It prints and logs nothing.
2. **Fewer read workers.** `READ_WORKERS = 8` (was 16). The host showed that 4 workers cut the growth by about 70 percent with the wall time within 20 percent; 8 keeps a margin for the page's wall time. Change nothing else in the pool, the page size (30), the gate, the filter, the sort or the cursor.
Change no admission, no fence, no other adapter, no tool signature and nothing in `app/tools.py` or `app/client_core.py`.

TESTS (new file `tests/test_og_en20.py`; read `tests/test_og_en18.py` for the fake-ctx fixtures):
- `test_ogen20_ac01`: `_tune_allocator()` with a fake `ctypes.CDLL` calls `mallopt(-8, 2)` exactly once across two calls and returns True; a fake `mallopt` returning 0 makes it return False; `CDLL` raising `OSError` or the library lacking `mallopt` returns False without raising; the module imported on this device raises nothing.
- `test_ogen20_ac02`: `READ_WORKERS` is 8; a page of 30 partitions over the fake ctx has at most 8 reads in flight at any moment and a 396-partition window paged to its end reads every partition exactly once.
If an existing test pins `READ_WORKERS` 16 or the number of concurrent reads, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no registry change, no change to `app/tools.py` or `app/client_core.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en20.py
infra/aws/ec2/opal-gateway/tests/test_og_en19.py
infra/aws/ec2/opal-gateway/tests/test_og_en18.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_adapter_bd49f.py`, `tests/test_og_en20.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~132/`. Rows: id `NFRA_OPLGTW-Z-W132-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-20"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en20.py test_ogen20_ac01 test_ogen20_ac02; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 2 of 2; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-20"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~132 '^infra/aws/ec2/opal-gateway/(app/client_adapter_bd49f\.py|tests/test_og_(en20|en19|en18|en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~132: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-20"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/en20.AC3.sh; echo "exit=$?"</invocation><expect>(?s)en4, en12, cl2, en13, en15, en17, en18, en19, en20 forward: passed (\d+); failed 0.*reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the two named tests pass. `AC2`: the commits of this serial touch only the listed files. `AC3`: the window test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-20.bound-glibc-arenas-and-read-workers.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-N (decomposition addendum R3-T.107). Risk WORLD by the L6 floor. It is the second code cell on `app/client_adapter_bd49f.py` after `OG-en-19`; it is spawned only after `OG-en-19` is merged.
- The cause is measured on the host (`OG-ev-4`, row Z-S342). The CODE equivalent of the measured `MALLOC_ARENA_MAX=2` (variant D) is `mallopt(M_ARENA_MAX, 2)` at import; `READ_WORKERS=8` is the issuer's choice from variant F (4 workers, 42.4 MB per page, wall within 20 percent). The COMBINATION is not yet measured: the next release's Phase A runs the three-page chain on the candidate code on the host and STOPS if the median growth is above 20 MB per page.
- Honest limit: `mallopt` affects arenas created after the call; threads the service already started keep theirs. The Phase A measurement runs in a fresh process; the Phase B read-back runs against the service, so Phase B samples host memory as before.
- Not here: the per-partition prefix listing (`Z-S328`, `client_core.py`), which also dominates the page's wall time; it is a separate cell.
- Pre-cut: `en20.AC3` base FAIL as expected (the test file is absent); AC1 base FAIL (file absent).

<status>staged</status>
<round>40</round>
<workstream>ENRICH-R40-N</workstream>
<slot>~132</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
