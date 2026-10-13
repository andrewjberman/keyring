# ADVI_BDPRCE task order -- `BP-b-6` -- THE EXACT-LOT EXPORT CHANGE AS A PATCH AND A BYTE-UNCHANGED FIXTURE PROOF (NOTHING APPLIED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~10</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a patch and an offline fixture; no schedule is added or changed (the apply cell, not this one, touches the export's schedule-driven input).
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`head-object`, boto3 `get_object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the patch, test and proof do not exist (AC1, AC2 FAIL); AC2's grader rejects a changed legacy output, a lot key that is not the lot, an address not from the builder and Units or Cost Basis leaking into the legacy table (33-arm self-test OK). Blindness: AC2 proves the fixture's invariants, not the live first export; the live read belongs to the apply cell, under a pair.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-6` (round 2; code as a patch and a fixture proof; you apply nothing)

Black Diamond's unrealized-gains export (query type 4, template `data/black_diamond/scripts/bronze/templates/unrealized.json`) offers `Units` (measure 15) and `Cost Basis` (measure 16), switched OFF in 49 Financial's
template (`"isSelected": false`; Cottonwood's `data/cot/scripts/bronze/templates/unrealized.json` has both `true`). Our silver step `process_unrealized_xlsx_to_parquet`
(`data/black_diamond/scripts/silver/merge-daily-incremental.py`, about :1138-1215) de-duplicates on `(account_id, asset_name)` keeping the first row, so every later tax lot of a position is dropped.
The plan, ruled by the CTO under "its own never-widen pair": turn the two measures on AND route the lot-level rows to a NEW table, with the legacy `silver/unrealized` BYTE-UNCHANGED. The act that applies this
(the S3 template, the repo files, the runner sync, the first export) is WORLD and waits on its pair. **This cell produces the change and its proof, offline, and applies none of it.**

### 1a. The change you author (as files in your deliverables folder; do not edit anything under `data/`)

1. **The template:** a copy of the 49F template with measures 15 and 16 `isSelected: true` and nothing else changed. Write it to `.../deliverables/0.9.0_WK_ADVI_BDPRCE~10/unrealized.patched.json`. Prove "nothing else
   changed" by a diff of the parsed JSON (only those two `isSelected` values differ) and print the byte counts of the original and the copy. The S3 copy is read for comparison:
   `s3://opal-data-bd/code/bronze/templates/unrealized.json` (the round-1 measurement: equals the repo copy, 14,419 bytes, VersionId `VgzqQbd.3F3sAlllb6SWsjKZ2XvXgAfE`); read its current VersionId and state whether it still equals the repo copy.
2. **The silver step:** a patched copy of `merge-daily-incremental.py` as `merge_daily_incremental.patched.py` plus `unrealized_lots.diff` (a unified diff against the repo file at your HEAD). The patch:
   (a) leaves the legacy output construction exactly as today and DROPS the two new columns from it, so `silver/unrealized/<date>.parquet` keeps its rows, columns and values;
   (b) builds a lot-level table from the same export's rows, de-duplicated on the LOT (`account_id`, `asset_id`, `open_date`, `unit_cost`), never on the position, carrying `units` and `cost_basis`;
   (c) names the table's address from the builder, never typed: `python -c "from lib.opal_naming import address; print(address('blackdiamond','49financial','silver','unrealized_lots','date=YYYY-MM-DD'))"`
   run from the repo root returns `s3://opal-data-assets/blackdiamond/49financial/silver/unrealized_lots/date=YYYY-MM-DD` (the PRD's CONTRACTS row; if the builder refuses or differs, file a row and stop on this item).
   The export's column names for Units and Cost Basis are not known until the template is on: read the column names of a REAL bronze unrealized export for one recent day to learn the existing names, and for the two
   new columns follow the naming rule the Cottonwood silver step uses for the same export (`data/cot/scripts/silver/cot_silver_merge.py`; read how it names Units and Cost Basis). State the mapping you assumed.
3. **No `data/` edit.** The three files above live only under your deliverables folder.

### 1b. The proof (offline, on a recorded export)

- `test_lot_split.py`: loads a REAL bronze unrealized export of one recent day from `opal-data-bd` (find its key from the current silver step; download to `C:/dev/wk-bdprce-r2-10-data/`), ADDS two synthetic columns
  (`Units`, `Cost Basis`) so the export looks as it will after the switch (state loudly in the output that they are synthetic), runs BOTH the repo function (legacy, from your HEAD) and your patched function on it, and prints one last line
  `LOT SPLIT TEST: OK <n> arms` (exit 0) with at least these arms: (1) the legacy parquet bytes from the repo function on the ORIGINAL export equal the legacy parquet bytes from the patched function on the
  SAME original export (sha256 equal); (2) on the export WITH the two columns, the patched legacy output is byte-equal to (1); (3) the lot table has more rows than the legacy table (state both counts) and its
  key is unique; (4) the lot table carries `units` and `cost_basis`; the legacy table carries neither; (5) the address equals the builder's output.
- `LOT_PROOF.json` (below), and `LOT_PROOF.md` (one page: the diff in words, the mapping assumed, what the live first export could change that this fixture cannot).

```json
{"order": "BP-b-6", "read_at": "<ISO UTC>", "claim": "measured", "export_key": "<bronze key used>",
 "legacy_bytes_equal": true, "legacy_sha256": "<64 hex>", "lot_rows": 0, "legacy_rows": 0,
 "keyed_on_lot": true, "lot_key": ["account_id", "asset_id", "open_date", "unit_cost"],
 "address": "s3://...", "address_from_builder": true, "new_columns_in_legacy": [],
 "template": {"changed_keys": ["measure 15 isSelected", "measure 16 isSelected"], "s3_equals_repo": true, "s3_version_id": "<id>"},
 "synthetic_columns": true}
```

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no upload, and NO edit of any file under `data/`, `infra/` or `lib/`. Downloaded files go to `C:/dev/wk-bdprce-r2-10-data/` (outside the checkout).
2. No client name, account number or advisor name is printed or committed; the recorded export is not committed (hash and key only).
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-6 fixture needs the key listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~10/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~10/ADVI_BDPRCE.TO-BP-b-6.lot-export-patch.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-6"><invocation>cd /c/dev/wk-bdprce-r2-10 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~10/test_lot_split.py</invocation><expect>^LOT SPLIT TEST: OK [0-9]+ arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-6"><invocation>cd /c/dev/wk-bdprce-r2-10 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py lotproof --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~10/LOT_PROOF.json</invocation><expect>^LOTPROOF record ok legacy_equal=true lots=[0-9]+ keyed_on_lot=true$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-b-6"><invocation>cd /c/dev/wk-bdprce-r2-10 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-10 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~10/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (the split and the byte-unchanged legacy, five arms); AC2 grades the proof record's invariants; AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit the three change files, the test, `LOT_PROOF.json` and `LOT_PROOF.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W10-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: legacy rows and lot rows on the fixture, byte equality (both arms), the address, the template diff, the S3 VersionId and whether S3 equals the repo, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 6, first half (the PRD's C1 as code). The apply is WORLD and is not cut here: it is the next amendment, after this merges and the pair (CTO + COO halves) is signed at the current bytes; the COO half is authored from this proof.
No `data/`, `infra/` or `lib/` edit, so the L6 floor reads LOCAL. Rollback at apply: the template's prior VersionId, named in `LOT_PROOF.json`.

<status>pending</status>
<round>2</round>
<workstream>LOTEXPORT</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-6</to_id>
<slot>~10</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
