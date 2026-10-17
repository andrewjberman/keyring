# NFRA_OPLGTW task order -- `OG-en-19` -- a window page is ordered by trade date, newest first (round 40; found by `OG-ap-32` Phase B, row Z-S339)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-19</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-19</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~131</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act repairs the issuer's own ordering rule after the applier's measurement on the host (`~NFRA1`, `OG-ap-32` Phase B, row Z-S339): on page 4 of the transactions chain the rows' `trade_date`s inside one page were not non-increasing (newest row day 2026-07-16, oldest 2026-06-16, 44 rows), because the page orders by PARTITION date and the rows inside a partition stay in the order read, while a partition file can carry rows of several trade dates.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-19` (decomposition addendum R3-T.106, round 40, workstream ENRICH-R40-M)

THE DEFECT. In `app/client_adapter_bd49f.py` (read the whole file first), `_transactions_answer` and `_fees_answer` build their lists from `_window_read`, which runs newest PARTITION first with rows inside a partition in read order. The answer promises rows NEWEST FIRST, but a partition can hold rows of several `trade_date`s, so the list is not ordered by trade date.

THE FIX (code only, at most about 10 product lines): after the duplicate-free list is built in `_transactions_answer` and `_fees_answer` (the lists of items whose `date` is the row's `trade_date` as ISO text), order each list by its `date` DESCENDING with a STABLE sort (`list.sort(key=..., reverse=True)` is stable: equal dates keep the order read). Change nothing else: not the cursor, not the page size, not the counts, not the gate, not the dedupe, not any other adapter. The cursor contract stays by PARTITION date (`next_cursor` is the day before the oldest partition read); only the order of rows inside one page changes.

TESTS (new file `tests/test_og_en19.py`; read `tests/test_og_en18.py` for the fake-ctx fixtures):
- `test_ogen19_ac01`: planted partitions whose rows carry out-of-order trade dates (a partition dated D holding rows of D, D-3 and D-1 in that order, and a later partition holding rows of an earlier trade date); one page of `get_transactions` answers rows whose `date` is non-increasing; the same for `get_fees`; the set of rows (count and the sum of amounts) equals the unsorted build's; rows with an equal `date` keep their read order.
- `test_ogen19_ac02`: a multi-partition window paged with `to_date=<next_cursor>` until null: every row exactly once across the pages (the sort is within a page), and the cursor chain is unchanged (the same `next_cursor` values as without the sort).
If an existing test pins the old oldest-first or read-order of a page, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change, no change to `app/tools.py` or `app/client_core.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en19.py
infra/aws/ec2/opal-gateway/tests/test_og_en18.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_adapter_bd49f.py`, `tests/test_og_en19.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~131/`. Rows: id `NFRA_OPLGTW-Z-W131-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-19"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en19.py test_ogen19_ac01 test_ogen19_ac02; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 2 of 2; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-19"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~131 '^infra/aws/ec2/opal-gateway/(app/client_adapter_bd49f\.py|tests/test_og_(en19|en18|en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~131: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-19"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/en19.AC3.sh; echo "exit=$?"</invocation><expect>(?s)en4, en12, cl2, en13, en15, en17, en18, en19 forward: passed (\d+); failed 0.*reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the two named tests pass. `AC2`: the commits of this serial touch only the listed files. `AC3`: the window test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-19.order-a-window-page-by-trade-date.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-M (decomposition addendum R3-T.106). Risk WORLD by the L6 floor (a gateway infrastructure path); no deploy in this cell. It is the first of two code cells on `app/client_adapter_bd49f.py` (the memory repair `OG-en-20` follows it after `OG-ev-4`); the file is merged in between, never edited by two workers at once.
- The arm `e1_newest_first` of `OG-ap-32` is reworded at the next release's amendment to: within each page the rows' dates are non-increasing; across pages the cursor moves back by PARTITION date.
- Pre-cut: `en19.AC3` base FAIL as expected (the test file is absent); AC1 base FAIL (file absent).

<status>complete</status>
<round>40</round>
<workstream>ENRICH-R40-M</workstream>
<slot>~131</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
