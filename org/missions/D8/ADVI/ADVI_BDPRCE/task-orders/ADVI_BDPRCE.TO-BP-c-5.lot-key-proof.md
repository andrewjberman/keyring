# ADVI_BDPRCE task order -- `BP-c-5` -- THE LOT-KEY FIXTURE PROOF RE-RUN WITH `relationship_id` IN THE KEY (STAGED, NOTHING APPLIED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~23</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a patch and an offline fixture; no schedule is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`head-object`, boto3 `get_object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a changed legacy output, any row folded, any colliding group still differing, a key without `relationship_id` (unless the export's own lot id is the basis), an address not from the builder and Units or Cost Basis leaking into the legacy table (35-arm self-test OK). Blindness: the grader proves the fixture's invariants, not the live first export; the live read belongs to the apply cell, under a pair.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-c-5` (round 3; code as a patch and a fixture proof; you apply nothing)

Round 2's `BP-b-6` authored the exact-lot export change and its fixture proof (`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~10/`: `unrealized.patched.json`, `merge_daily_incremental.patched.py`, `unrealized_lots.diff`, `test_lot_split.py`, `LOT_PROOF.json`, `LOT_PROOF.md`; read `LOT_PROOF.md` first).
Its lot key (`account_id`, `asset_id`, `open_date`, `unit_cost`) folded 15,553 export rows, and 14,514 of 14,696 colliding groups differed on Relationship ID (row `ADVI_BDPRCE-D1-W10-S2`). The CTO ruled the key (PRD v1.1,
`org/missions/D8/ADVI/ADVI_BDPRCE/prd/ADVI_BDPRCE_PRD.md` CONTRACTS row "the lot-level unrealized table" and its ADDENDUM v1.1): the lot is (`relationship_id`, `account_id`, `asset_id`, `open_date`, `unit_cost`), or the export's own lot identifier where one exists.
The target of the re-run: **zero rows folded and zero colliding groups still differing on any column.** The template apply stays under its own pair and waits on a clean read of this proof. You re-run the proof. You apply nothing.

The cap check `BP-c-4` is merged into your worktree (`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/CAP.json`, `CAP.md`; read the verdict first). The verdict is read: `CAP` (15 exports at exactly 500,000, from 2026-07-08 on; paging plan: slice on the Relationship ID filter, `unrealized.json:79-83`, since date tiling cannot split a snapshot, `cot_bronze_ingest.py:147`). The 2026-10-09 export therefore held only the first 500,000 rows: run the proof on that export anyway and ALSO state in `LOT_PROOF2.md`
what an incomplete export means for the zero (the proof says the key does not fold the rows it SAW, not that no lot was missed); if the CAP record names a paging plan, say whether the fixture can be paged from S3 data you can read, and use it only if the data exists.

### 1.00 RE-SEAT ON PRD v1.3 (issuer, 2026-10-14 ~05:4xZ); it REPLACES sections 1a items 3-4, 1b, 3 and 4 where they differ

The first seat (~17, closed @f3eaea3038) measured the truth and its record is honest: under the five-column key the 2026-10-09 export folds 192 rows (191 colliding groups, differing on Market Value in 191 and Inherited Date in 1), so the zero-fold criteria could not pass. The CTO then ruled (PRD v1.3, call 67ac): **the lot key gains `units`; Market Value does not join; the zero-fold proof is read on the FIRST REAL export under the apply's pair** (the recorded export carries no Units column, so no fixture can prove a zero). This order therefore proves what a fixture CAN prove. You are the second seat. The first seat's files are in your tree under `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~17/` (`merge_daily_incremental.patched2.py`, `unrealized_lots2.diff`, `test_lot_split2.py`, `LOT_PROOF2.json`, `LOT_PROOF2.md`): copy them into your folder as `...patched3.py`, `unrealized_lots3.diff`, `test_lot_split3.py`; do not edit them in place.
1. **The key.** Change ONLY `LOT_KEY_COLS` of the patched script to the v1.3 key (`relationship_id`, `account_id`, `asset_id`, `open_date`, `unit_cost`, `units`) and whatever the change forces. The lot table builder must tolerate an export WITHOUT a Units column exactly as the first seat's did (the recorded export has none): in that case the builder behaves as the first seat's patch (the synthetic-column arms stay, loudly labelled synthetic). The legacy output stays BYTE-UNCHANGED. Write `unrealized_lots3.diff` (a unified diff against the repo file at your HEAD).
2. **The proof** `test_lot_split3.py` prints one last line `LOT SPLIT3 TEST: OK <n> arms` with n at least 10: the first seat's arms 1 to 8 (legacy bytes equal on both exports; the lot table larger than the legacy table and unique on its key; units and cost basis in the lot table, in neither legacy table; the address equals the builder's; the relationship id survives), PLUS: (9) on a planted frame, two rows equal on the five old key columns and different on `units` BOTH survive in the lot table, and the same two rows with equal `units` fold to one; (10) on the recorded export the number of rows the FIVE-column key would fold is PRINTED and equals an independent recount made another way (`len(df) - len(df.drop_duplicates(subset=[five columns]))` in pandas on the raw rows, written separately from the patched code); this arm passes when the two numbers are equal, whatever the number is (expected 192; never an assertion of zero). State in the test output that the zero-fold proof is deferred to the first real export under the apply's pair.
3. **The record** `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~23/LOT_PROOF3.json` (shape below; grader `r3_checks.py lotproof3`) and `LOT_PROOF3.md` (one page: the key and why, the 192 and what it means, why a fixture cannot prove the zero, what the first real export must show: 0 rows folded and no colliding group differing on any column, read back under the pair, with the S3 template's rollback VersionId from round 2's record).
```json
{"order": "BP-c-5", "read_at": "<ISO UTC>", "claim": "measured", "export_key": "<bronze key>", "export_rows": 0,
 "legacy_bytes_equal": true, "legacy_sha256": "<64 hex>", "lot_rows": 0, "legacy_rows": 0,
 "key_basis": "relationship_id", "keyed_on_lot": true,
 "lot_key": ["relationship_id", "account_id", "asset_id", "open_date", "unit_cost", "units"], "units_in_key": true,
 "folded_without_units": 0, "recount_without_units": 0, "zero_fold": "deferred_to_first_real_export",
 "address": "s3://...", "address_from_builder": true, "new_columns_in_legacy": [], "synthetic_columns": true,
 "template_rollback_version_id": "<VersionId>", "cap_verdict_read": "CAP"}
```
The 2026-10-09 export is at `C:/dev/wk-bdprce-r3-17b-data/` from the first seat (READ it there; verify its sha256 reads `5700843f9e661364910a5bbb9d9d4b60521775922539f47b066a10d80039ef5b`, else re-download it by the key in `LOT_PROOF2.json`); new downloads go to `C:/dev/wk-bdprce-r3-23-data/`. Row ids `ADVI_BDPRCE-D1-W23-S<k>`. Proof (replaces section 4): AC1 runs `test_lot_split3.py` (`^LOT SPLIT3 TEST: OK ([1-9][0-9]) arms$`), AC2 runs `r3_checks.py lotproof3` on `LOT_PROOF3.json`, AC3 is the write-surface bound (`~23/`, the investigation file and this order file). Where the text below names `~17`, `LOT_PROOF2`, `r3-17b` or zero folded, THIS section wins.

### 1a. What to do (the first seat's text; section 1.00 above wins where it differs)

1. **Find the export's own lot identifier first.** Read the column names of the recorded export (the bronze unrealized workbook of 2026-10-09 in `opal-data-bd`; round 2 recorded its key in `LOT_PROOF.json` field `export_key`; download to `C:/dev/wk-bdprce-r3-17b-data/`). If the export carries a column that uniquely identifies a tax lot (a lot id, a tax-lot id, a position-lot id),
   test it: unique on the whole export? If yes, `key_basis` is `export_lot_id` and the lot key is that column. If none exists or it is not unique, `key_basis` is `relationship_id` and the key is (`relationship_id`, `account_id`, `asset_id`, `open_date`, `unit_cost`). State the columns you considered and what you found.
2. **Patch copies, not the repo.** Copy round 2's patched script into your folder as `merge_daily_incremental.patched2.py` and change ONLY the lot key (`LOT_KEY_COLS`) and whatever the change forces (the column must survive the legacy construction's renames; check how `relationship_id` is named after the silver rename step). Write `unrealized_lots2.diff` (a unified diff against the repo file at your HEAD).
   The legacy output stays BYTE-UNCHANGED: the two new columns are dropped from it, and nothing else about it moves.
3. **The proof** `test_lot_split2.py`, on the recorded export with the two synthetic columns (state loudly that they are synthetic), prints one last line `LOT SPLIT2 TEST: OK <n> arms`, with at least: (1) legacy sha256 from the repo function on the ORIGINAL export equals that from the patched function on the same export;
   (2) the patched legacy output on the export WITH the two columns equals (1); (3) the lot table has more rows than the legacy table and its key is unique; (4) **rows folded = 0**: the lot-table row count equals the export's row count after removing only exact duplicate rows (state both counts and the exact-duplicate count);
   (5) **colliding groups still differing = 0**: group the export by the PROPOSED key; every group of more than one row must be identical on EVERY column (if one is not, list the differing columns and the group count: that is a failure and the record says so, never a rounding);
   (6) the lot table carries `units` and `cost_basis`; the legacy table carries neither; (7) the address equals `lib.opal_naming.address('blackdiamond','49financial','silver','unrealized_lots','date=YYYY-MM-DD')`.
4. **Report an honest failure.** If (4) or (5) is not zero under the ruled key, do not widen the key silently: report the counts, the columns that differ, a candidate wider key you tested and its counts, and file a BLOCKING row. The record then carries the real numbers, and the grader will refuse it (that refusal is the correct outcome).

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~17/LOT_PROOF2.json`

```json
{"order": "BP-c-5", "read_at": "<ISO UTC>", "claim": "measured", "export_key": "<bronze key>", "export_rows": 0,
 "legacy_bytes_equal": true, "legacy_sha256": "<64 hex>", "lot_rows": 0, "legacy_rows": 0,
 "rows_folded": 0, "exact_duplicate_rows": 0, "colliding_groups": 0, "colliding_groups_differing": 0,
 "key_basis": "relationship_id | export_lot_id", "keyed_on_lot": true,
 "lot_key": ["relationship_id", "account_id", "asset_id", "open_date", "unit_cost"],
 "columns_considered_for_lot_id": ["<names>"],
 "address": "s3://...", "address_from_builder": true, "new_columns_in_legacy": [], "synthetic_columns": true, "cap_verdict_read": "CAP | NOT_A_CAP | NOT_DETERMINED"}
```
Also write `LOT_PROOF2.md` (one page: the key and why, the counts against round 2's, what the live first export could change that this fixture cannot, the rollback VersionId of the S3 template from round 2's record).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no upload, and NO edit of any file under `data/`, `infra/` or `lib/`. Downloaded files go to `C:/dev/wk-bdprce-r3-17b-data/` (outside the checkout).
2. No client name, account number or advisor name is printed or committed; the recorded export is not committed (hash and key only).
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-c-5 fixture needs the key listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~23/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~23/ADVI_BDPRCE.TO-BP-c-5.lot-key-proof.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-5"><invocation>cd /c/dev/wk-bdprce-r3-23 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~23/test_lot_split3.py</invocation><expect>^LOT SPLIT3 TEST: OK ([1-9][0-9]) arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-5"><invocation>cd /c/dev/wk-bdprce-r3-23 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py lotproof3 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~23/LOT_PROOF3.json</invocation><expect>^LOTPROOF3 record ok legacy_equal=true lots=[0-9]+ units_in_key=true folded_without_units=[0-9]+ recount_equal=true zero_fold=deferred$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-c-5"><invocation>cd /c/dev/wk-bdprce-r3-23 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-23 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~23/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md --allow org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-c-5.lot-key-proof.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (the split, the byte-unchanged legacy, folded and differing at zero); AC2 grades the proof record's invariants; AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit the patch files, the test, `LOT_PROOF2.json` and `LOT_PROOF2.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W23-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: export rows, exact duplicates, legacy rows and lot rows, rows folded, colliding groups and how many still differ, the key and its basis, byte equality (both arms), the address, the CAP verdict read, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 3 (second read); CTO call 239a and PRD v1.1. STAGED at the cut: un-parks when `BP-c-4` is merged and PASS and its verdict is read. Disarms `W10-S2` when it reads clean. The APPLY (WORLD, under its pair) is not cut here: it waits on this proof, on `BP-c-4`, on a dell1 CloudOps lane the CTO names, and on the pair signed at the current bytes.
No `data/`, `infra/` or `lib/` edit, so the L6 floor reads LOCAL.

**CLOSED WITH TWO TARGET CRITERIA FAILING (2.0.0_SA_COO~K1, 2026-10-14 ~03:1xZ):** AC1 and AC2 expect zero rows folded and zero colliding groups still differing under the ruled key; the proof measured 192 folded and 191 differing (191 on Market Value, 1 on Inherited Date) on the recorded 2026-10-09 export, recomputed independently by the issuer with the same numbers. The result IS the deliverable: the ruled key does not clear the gate, the worker did not widen it silently, and the failing instance is kept. The apply stays closed; the key is a call at the CTO (queued). AC3 passes.

<status>pending</status>
<round>3</round>
<workstream>LOTKEY2</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-5</to_id>
<slot>~23</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
