# NFRA_OPLGTW task order -- `OG-en-29` -- the window page size becomes the size the host sweep chose (round 42; CTO round-41 analysis item 1; the sweep is `OG-ev-6`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-29</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-29</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~144</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-41 analysis item 1 ("a page now reads in about 2 s against a 55 s limit, so 30 partitions per page no longer binds; the cell picks the new size from a measured sweep").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-29` (decomposition addendum R3-T.119, round 42, workstream ENRICH-R42-A)

YOU ARE SPAWNED ONLY AFTER the host sweep `OG-ev-6` has drained, so `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/PAGE_SWEEP.json` exists on your branch. If it does not, STOP and file a BLOCKING row. Its field `body.chosen_partitions` is 30, 60 or 120, chosen by a rule fixed before any run (the size measured, never assumed). If it reads 30 there is nothing to build: file a row saying so and make NO change (the issuer cancels this order).

THE CHANGE (one constant and what pins it). The window page size is the module constant `PAGE_PARTITIONS = 30` in `infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py` (line 82: the newest partitions of a window read per call; `next_cursor` is the day before the oldest partition read). Set it to `chosen_partitions` and update, in the same file, only the text that states the old size (the trailing comment on that line, and any docstring or note that says "30"; the note built at line 393 formats the constant, so it follows). Nothing else in the adapter changes.

THE TESTS. Some existing tests pin the old page size (read `tests/test_og_en17.py`, `tests/test_og_en18.py`, `tests/test_og_en19.py`, `tests/test_og_en20.py`, `tests/test_og_en22.py`, `tests/test_og_en23.py`, `tests/test_og_en24.py`: search them for `PAGE_PARTITIONS`, `30`, `next_cursor`). Update an existing test to the new truth with the SMALLEST edit (read the constant instead of hard-coding the old number where you can) and name each one in your report; never weaken a test or delete an assertion. NEW FILE `tests/test_og_en29.py`:
- `test_ogen29_ac01`: a window holding more than `PAGE_PARTITIONS` partitions answers the NEWEST `PAGE_PARTITIONS` partitions on the first call, with a `next_cursor` equal to the day before the oldest partition read, and a note naming the partial window (use the fixture style of `tests/test_og_en18.py`).
- `test_ogen29_ac02` (the size changes WHERE a page ends, never WHAT a row is): paging the same window at the new size and at the old size 30 (patch `PAGE_PARTITIONS` in the adapter module for the second run) and concatenating the pages returns the same rows in the same order, row for row, over the same newest partitions.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no change to `client_core.py`, `app/tools.py` or any other app file; no change to the answer's shape.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en29.py
infra/aws/ec2/opal-gateway/tests/test_og_en24.py
infra/aws/ec2/opal-gateway/tests/test_og_en23.py
infra/aws/ec2/opal-gateway/tests/test_og_en22.py
infra/aws/ec2/opal-gateway/tests/test_og_en20.py
infra/aws/ec2/opal-gateway/tests/test_og_en19.py
infra/aws/ec2/opal-gateway/tests/test_og_en18.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE the adapter, the new test file and, only to follow the new truth, the existing tests listed; the rest you only READ (including `PAGE_SWEEP.json`). `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~144/`. Rows: id `NFRA_OPLGTW-Z-W144-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-29"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/en29.AC1.sh; echo "exit=$?"</invocation><expect>(?s)PAGE_PARTITIONS assigned 1 time\(s\) as a literal; value (\d+); the sweep chose \1.*pytest rc=0; named tests passed 2 of 2; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-29"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~144 '^infra/aws/ec2/opal-gateway/(app/client_adapter_bd49f\.py|tests/test_og_(en29|en24|en23|en22|en20|en19|en18|en17|en15|en13)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~144: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-29"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en29set tests/test_og_en4.py tests/test_og_en12.py tests/test_og_cl2.py tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_en29.py; echo "exit=$?"</invocation><expect>(?s)en29set forward: passed (\d+); failed 0.*en29set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the constant is assigned once, as a literal, and equals the size the sweep chose; the two new tests pass. `AC2`: your commits touch only the listed files. `AC3`: the thirteen window test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-29.round-42-window-page-size-from-the-sweep.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines, the chosen size, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-A (decomposition addendum R3-T.119). Chain: `OG-ev-6` (host sweep, applier) -> this cell -> `OG-ap-39` (the batched release). The CTO's criterion for the size (page time under 15 s, median growth under 20 MB at the chosen size) is graded by `ev6.AC1`, which recomputes the rule from the runs; this cell only sets the constant. Spawn only after `OG-ev-6` has drained and `ev6.AC1` PASSes on my run. If the sweep chooses 30, this order is CANCELLED and `OG-ap-39` ships without it.
- Pre-cut: `AC1` base FAIL as expected (the sweep file is absent); `AC3` base: the twelve existing files pass, the thirteenth is absent.

- SUPERSEDED (2.0.0_SA_COO~O, round 42, ~03:0xZ): the sweep `OG-ev-6` chose 30 (`W/PAGE_SWEEP.json`; `ev6.AC1` PASS on my run): 60 partitions per page fails the growth clause (run medians 38.8, 39.3 and 29.6 MB against 20, none above 30), 120 fails it too (193.6, 249.9, 225.0) and returns 127 rows over the newest 120 partitions against 222 (the byte cap in `client_core._project` drops tail rows, read in code and seen in the row hash). There is nothing to build: the constant stays 30 and this order is not spawned. A later round revisits the size only with new evidence (a smaller row footprint or a raised cap).

<status>superseded</status>
<round>42</round>
<workstream>ENRICH-R42-A</workstream>
<slot>~144</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
