# NFRA_OPLGTW task order -- `OG-en-15` -- the 49F transactions and fees answers read the partitions the measurement says the window needs (round 39 E1; CVO v35 AC3 finding 5; PRD v3.6 item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-15</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-15</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~126</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the adapter reads the same prefixes through the same dedicated role, now more than one dated file per call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-38 analysis (`ledger/ROUND_ANALYSIS.round38.md` @faa77bd49e, E1) on the CVO's v35 finding 5: a 13-month window answered from ONE daily partition.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-15` (decomposition addendum R3-T.99, round 39 item E1, workstream ENRICH-R39-B)

INPUT YOU READ FIRST. `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/E1_PARTITION_MEASURE.json` (the applier's measurement of the live data, order `OG-ev-2`): `body.tables.transactions.classification` and `body.tables.fees.classification` are each `increment`, `snapshot` or `mixed`. If the file is absent when you start, STOP with a BLOCKING row: the issuer spawns you after it exists. You are the same worker as `OG-en-13`: its commits are your inherited state in `app/client_adapter_bd49f.py`; do not undo them.

THE GAP. `get_transactions` and `get_fees` in `app/client_adapter_bd49f.py` select ONE partition (`_select`) and answer the window from it (`window_partial: true`, `window_note: "one partition read; ..."`). A 13-month request gets one day's rows when the daily files are increments.

THE FIX (code only; read the whole file first):
- Add a module table `PARTITION_SEMANTICS = {"transactions": "<measured classification>", "fees": "<measured classification>"}` with a comment citing `E1_PARTITION_MEASURE.json`.
- `increment` or `mixed`: read EVERY dated partition inside the window `[start, end]` (use `_partitions(ctx, prefix)` and the window helper), at most `MAX_WINDOW_PARTITIONS = 60` of them (the newest 60 when more are in the window), answer from the union. DEDUPLICATION IS UNCHANGED (A1): keep the adapter's existing within-answer `seen`-set on `transaction_id` exactly as `get_transactions` has it today, shared across the partitions you read (the measurement found the daily partitions disjoint, overlap 0.0, so it removes nothing across partitions); do NOT add a new key or a new dedupe rule. The measurement also found `transaction_id` repeating within a partition (more rows than distinct ids, row Z-S314), so the existing rule may drop real legs: that is a carried question for the next round, not this cell; do not change it. Add `partitions_in_window` and `partitions_read` (integers), `partitions_read_dates` (the list of ISO dates), and set `window_partial` to `true` ONLY if `partitions_read < partitions_in_window` (the cap bit) or a dated partition inside the window could not be read, with a `window_note` that says which; otherwise `window_partial: false` and `window_note` states "all <n> partitions in the window read".
- `snapshot`: read the newest partition at or before `as_of` (as today), `window_partial: false`, `partitions_in_window: 1`, `partitions_read: 1` and `window_note: "cumulative snapshot: the newest partition holds the history to its date; the window is answered from it"`.
- The envelope fields (`partition_date`, `freshness_td`, `source_keys`) name the NEWEST partition read; `_source_keys` lists every key read. `denominator.partition_rows` is the sum of rows read; `fence_excluded` is summed.
- Every other behaviour is unchanged: the firm fence runs on EVERY partition read, a partition of another account is never merged, and the figures keep `OG-en-13`'s number format.

TESTS (new file `tests/test_og_en15.py`; read `tests/test_og_en12.py` and `tests/test_og_en13.py` for the fake-ctx fixtures; a fake ctx must record each key read):
- `test_ogen15_ac01`: with `PARTITION_SEMANTICS` patched to `increment`, TWO planted partitions inside a window both answer: the union's rows are returned, two rows with the same `transaction_id` (one in each partition) are returned once, by the existing `seen` rule, `partitions_read` is 2, `window_partial` is false, and the source keys name both.
- `test_ogen15_ac02`: with `snapshot` patched, two planted partitions: only the newest is read (the fake ctx records ONE read), `window_partial` is false, and the note says cumulative snapshot.
- `test_ogen15_ac03`: 61 planted daily partitions inside one window with `increment`: exactly 60 are read (the newest 60), `partitions_in_window` is 61, `partitions_read` is 60, `window_partial` is true and the note names the cap; and a partition holding ONLY another account's rows adds nothing to the answer and counts in `fence_excluded`.
Apply the same change to `get_fees` with the same tests parametrised over both tools (one test may loop over the tool). If an existing test pins the old one-partition window note, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change, no other adapter.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_en4.py
infra/aws/ec2/opal-gateway/tests/test_og_en12.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
infra/aws/ec2/opal-gateway/tests/test_og_ch1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/client_adapter_bd49f.py`, `tests/test_og_en15.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~126/`. Rows: id `NFRA_OPLGTW-Z-W126-S<k>` (continue your numbering), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-15"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en15.py test_ogen15_ac01 test_ogen15_ac02 test_ogen15_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-15"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~126 '^infra/aws/ec2/opal-gateway/(app/client_adapter_bd49f\.py|tests/test_og_(en15|en13|en4|en12|cl2|ch1)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~126: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial (this order and `OG-en-13`) touch only the listed files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-15.49f-window-spans-partitions.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 39 E1, workstream ENRICH-R39-B (decomposition addendum R3-T.99). Risk WORLD by the L6 floor (a gateway infrastructure path); no deploy in this cell. Second order of worker `~126`'s queue (same file as `OG-en-13`); SPAWN waits on `OG-ev-2`. The cap of 60 partitions per call is the issuer's bound on S3 reads per tool call; a window over the cap is answered from the newest 60 and says so.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

- A1 (issuer, 2026-10-16 ~19:4xZ, `OG-ev-2` result and rows Z-S313, Z-S314): the measurement reads transactions = increment, fees = increment (1930 and 2008 dated partitions, overlap 0.0 on all five pairs, key column `transaction_id`), so `PARTITION_SEMANTICS` is `increment` for both. The dedupe sentence is corrected to leave the existing rule alone, because `transaction_id` is not a unique row key in a partition (14359 rows, 2954 distinct ids). Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>staged</status>
<round>39</round>
<workstream>ENRICH-R39-B</workstream>
<slot>~126</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
