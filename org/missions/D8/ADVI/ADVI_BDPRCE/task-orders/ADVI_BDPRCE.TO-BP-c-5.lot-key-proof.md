# ADVI_BDPRCE task order -- `BP-c-5` -- THE LOT-KEY FIXTURE PROOF RE-RUN WITH `relationship_id` IN THE KEY (STAGED, NOTHING APPLIED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~17</issued_to>
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

### 1a. What to do

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
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~17/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~17/ADVI_BDPRCE.TO-BP-c-5.lot-key-proof.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-5"><invocation>cd /c/dev/wk-bdprce-r3-17b &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~17/test_lot_split2.py</invocation><expect>^LOT SPLIT2 TEST: OK [0-9]+ arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-5"><invocation>cd /c/dev/wk-bdprce-r3-17b &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py lotproof2 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~17/LOT_PROOF2.json</invocation><expect>^LOTPROOF2 record ok legacy_equal=true lots=[0-9]+ folded=0 differing=0 key=(relationship_id|export_lot_id)$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-c-5"><invocation>cd /c/dev/wk-bdprce-r3-17b &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-17b --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~17/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (the split, the byte-unchanged legacy, folded and differing at zero); AC2 grades the proof record's invariants; AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit the patch files, the test, `LOT_PROOF2.json` and `LOT_PROOF2.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W17-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: export rows, exact duplicates, legacy rows and lot rows, rows folded, colliding groups and how many still differ, the key and its basis, byte equality (both arms), the address, the CAP verdict read, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 3 (second read); CTO call 239a and PRD v1.1. STAGED at the cut: un-parks when `BP-c-4` is merged and PASS and its verdict is read. Disarms `W10-S2` when it reads clean. The APPLY (WORLD, under its pair) is not cut here: it waits on this proof, on `BP-c-4`, on a dell1 CloudOps lane the CTO names, and on the pair signed at the current bytes.
No `data/`, `infra/` or `lib/` edit, so the L6 floor reads LOCAL.

<status>pending</status>
<round>3</round>
<workstream>LOTKEY2</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-5</to_id>
<slot>~17</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
