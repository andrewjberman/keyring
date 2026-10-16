# NFRA_OPLGTW task order -- `OG-en-17` -- the 49F transactions and fees answer the whole 13-month window: a concurrent full read, or a continuation cursor, never a silent truncation (round 40 W1; CTO ruling @0a15d90223)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-17</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-17</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~129</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the adapter reads the same prefixes through the same dedicated role.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-40 ruling W1 (`ledger/ROUND_ANALYSIS.round38.md` update @0a15d90223) on the CVO's v37 finding that a 13-month request reads about 2 months.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-17` (decomposition addendum R3-T.102, round 40 cell W1, workstream ENRICH-R40-W1)

INPUT YOU READ FIRST. `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/WINDOW_MEASURE.json` (the applier's measurement on the host, order `OG-ev-3`): `body.request_budget.verdict` is `inside` or `outside`. If the file is absent when you start, STOP with a BLOCKING row: the issuer spawns you after it exists. You are the same codebase state as `OG-en-15` (merged `592d79f192`): `get_transactions` and `get_fees` in `app/client_adapter_bd49f.py` read every dated partition in the window up to `MAX_WINDOW_PARTITIONS = 60` (newest 60) and set `window_partial` true only when the cap bites; read the whole file first.

THE FIX (code only). Implement ONLY the branch the measure's verdict names, and record it in a module constant `WINDOW_STRATEGY` (`"concurrent"` or `"cursor"`) whose comment cites `WINDOW_MEASURE.json` and its p95s.
- **`inside` (concurrent full read):** raise `MAX_WINDOW_PARTITIONS` to 400 (the declared maximum window of 13 months is about 395 daily files) and read the partitions CONCURRENTLY with a `ThreadPoolExecutor(max_workers=16)`; keep the order of the answer's rows by partition date (newest first, as today) whatever the completion order; the firm fence runs on every partition; a partition that cannot be read refuses the call (fail closed, as in `OG-en-15`). `window_partial` stays true ONLY when `partitions_in_window` exceeds the cap, with the note naming the cap.
- **`outside` (continuation cursor):** read the newest `PAGE_PARTITIONS = 60` partitions of the window (concurrently, `max_workers=16`) and return `next_cursor`: the ISO date of the day BEFORE the oldest partition read, or `null` when the window start is reached. A caller pages back by passing `next_cursor` as `to_date` of the next call (the existing `to_date` argument; do NOT change any tool signature or `app/tools.py`). `window_partial` is true while `next_cursor` is not null, and the `window_note` says "page back with to_date=<next_cursor>". Never a silent truncation: a window larger than a page ALWAYS returns a cursor.
- Both branches: the existing `exact_duplicates_removed`, `partitions_in_window`, `partitions_read`, `partitions_read_dates` keys stay; figures keep `OG-en-13`'s number format; the single-partition and `snapshot` behaviours are unchanged.

TESTS (new file `tests/test_og_en17.py`; read `tests/test_og_en15.py` for the fake-ctx fixtures; a fake ctx must record each key read and the maximum number of reads in flight):
- `test_ogen17_ac01`: 61 and then 395 planted daily partitions inside a 13-month window. `concurrent`: all 395 are read (the fake ctx records 395 reads), `window_partial` false, rows newest first, never more than 16 reads in flight at once. `cursor`: the first call reads exactly 60, returns `next_cursor` equal to the day before the oldest date read and `window_partial` true; paging with `to_date=<next_cursor>` until it is null reads every partition exactly once and returns every row exactly once across the pages.
- `test_ogen17_ac02`: a window of 450 partitions. `concurrent`: 400 are read, `window_partial` true and the note names the cap. `cursor`: the pages end with `next_cursor` null at the window start, the union equals all 450.
- `test_ogen17_ac03`: `get_fees` behaves as `get_transactions` in the same branch; a partition holding only another account's rows adds nothing and counts in `fence_excluded`; an unreadable partition refuses the call in both branches (no partial answer).
If an existing test pins the old 60-partition cap or the old note, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change, no other adapter, no change to `app/tools.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_adapter_bd49f.py`, `tests/test_og_en17.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~129/`. Rows: id `NFRA_OPLGTW-Z-W129-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-17"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en17.py test_ogen17_ac01 test_ogen17_ac02 test_ogen17_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-17"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~129 '^infra/aws/ec2/opal-gateway/(app/client_adapter_bd49f\.py|tests/test_og_(en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~129: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only the listed files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-17.49f-full-window-or-cursor.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the branch you implemented, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-W1 (decomposition addendum R3-T.102). Risk WORLD by the L6 floor (a gateway infrastructure path); no deploy in this cell; it rides the next batched gateway release with MI's re-emitted catalog. SPAWN waits on `OG-ev-3` (the measure's verdict).
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>staged</status>
<round>40</round>
<workstream>ENRICH-R40-W1</workstream>
<slot>~129</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
