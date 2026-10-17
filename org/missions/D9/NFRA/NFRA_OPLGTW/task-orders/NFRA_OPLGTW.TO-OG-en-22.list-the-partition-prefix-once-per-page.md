# NFRA_OPLGTW task order -- `OG-en-22` -- list the served prefix once per page, not once per partition (round 41; CTO round-40 analysis item 2; row Z-S328)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-22</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-22</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~135</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the same prefixes are read through the same role, with fewer list calls.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-40 analysis item 2 (`ledger/ROUND_ANALYSIS.round40.md` @66aeb73b0c) on the applier's measurement that the per-partition prefix listing is about 0.4 of each partition read's 0.55 s (row Z-S328).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-22` (decomposition addendum R3-T.111, round 41, workstream ENRICH-R41)

THE DEFECT. `Ctx.read_rows(prefix, partition, columns=None, filters=None)` in `app/client_core.py` (about line 303) lists the WHOLE served prefix with `typed_scope.list_keys(scope, real)` to find the one key of the requested date, on EVERY call. The windowed 49F reads (`app/client_adapter_bd49f.py`, `_read_partitions` reads one page of up to 30 partitions with `ctx.read_rows(prefix, part, columns=list(columns))` in a thread pool) therefore list the prefix 30 times per page, each listing about 0.4 s of the 0.55 s a partition read costs. (`Ctx.list_partitions` and `_window_plan` already list once per page for the plan; that stays.)

THE FIX (code only; read `app/client_core.py` `Ctx` and `app/client_adapter_bd49f.py` `_read_partitions`, `_window_plan` first):
1. In `app/client_core.py` add `Ctx.partition_keys(prefix) -> dict` (partition date string -> the key to read): ONE `typed_scope.list_keys` listing of the served prefix, applying exactly the rule `read_rows` applies today (only keys ending `.parquet` whose `_partition_of(_tail(...))` is a date; when several keys carry one date, `max(..., key=harvest_typed._layout_key)`). Give `read_rows` an optional keyword `key=None`: when a key is given it reads that key and does NOT list; when it is None the behaviour is exactly today's. Nothing else in `client_core.py` changes.
2. In the adapter, `_read_partitions` takes the index ONCE per call when `ctx` has `partition_keys` (`getattr`), and passes `key=index.get(part)` to each `ctx.read_rows`; a partition with no key in the index answers an empty row list as `read_rows` does today. When `ctx` has no `partition_keys` (the fake contexts of existing tests) the code runs exactly as today. Keep the filter, fence, sort, cursor, gate, page size and worker count untouched.
3. Do not touch `app/tools.py` (another cell edits it in this round) or any other adapter.

TESTS (new file `tests/test_og_en22.py`; read `tests/test_og_en18.py` for the fixtures and `typed_scope`'s `list_keys`/`read_parquet` call shapes to fake):
- `test_ogen22_ac01`: a fake served store of 396 daily partitions (one key each, some with two keys for one date) behind a REAL `Ctx` whose `typed_scope.list_keys` and `read_parquet` are patched with counters: one page of `get_transactions` (30 partitions) makes exactly 1 listing for the page's reads (plus the one the plan already makes), where the base made 30 more; and `get_fees` likewise.
- `test_ogen22_ac02`: for EVERY one of the 396 partitions, the rows read through the new path (`partition_keys` then `read_rows(key=...)`) are equal to the rows read through the old path (`read_rows` without a key); and a full cursor chain (`to_date=<next_cursor>` until null) returns the same rows as the same chain on a fake `ctx` that lacks `partition_keys`.
- `test_ogen22_ac03`: a `ctx` without `partition_keys` (a plain fake with only `read_rows`, `list_partitions`, `prefix`) still works; a date with no key reads empty; the layout rule (several keys for one date) picks the same key as before.
If an existing test pins the number of listings or the `read_rows` signature, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no registry change, no change to `app/tools.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
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

You WRITE `app/client_core.py`, `app/client_adapter_bd49f.py`, `tests/test_og_en22.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~135/`. Rows: id `NFRA_OPLGTW-Z-W135-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-22"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en22.py test_ogen22_ac01 test_ogen22_ac02 test_ogen22_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-22"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~135 '^infra/aws/ec2/opal-gateway/(app/(client_core|client_adapter_bd49f)\.py|tests/test_og_(en22|en20|en19|en18|en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~135: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-22"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en22set tests/test_og_en4.py tests/test_og_en12.py tests/test_og_cl2.py tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en22.py; echo "exit=$?"</invocation><expect>(?s)en22set forward: passed (\d+); failed 0.*en22set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only the listed files. `AC3`: the ten window test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-22.list-the-partition-prefix-once-per-page.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41 (decomposition addendum R3-T.111), cell 2 of the CTO's round-40 analysis. Risk WORLD by the L6 floor. It rides the next batched release. The CTO's criteria: page wall time before and after on the same 13-month window (MEASURED BY THE APPLIER in the release's Phase A on the host, not by this worker; the offline proof is the listing count and byte-equality); results byte-equal over every partition (`test_ogen22_ac02`).
- Disjoint from `OG-en-21` (which edits only `app/tools.py`) and `OG-db-3` (only `deploy-to-ec2.sh`); the three drain in any order. The existing window tests may be touched by two workers; the drain is the issuer's and resolves a test-file overlap in the issuer's own tree.
- Pre-cut: `AC1` base FAIL as expected (the test file is absent); `AC3` base FAIL (the file is absent).

<status>staged</status>
<round>41</round>
<workstream>ENRICH-R41</workstream>
<slot>~135</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
