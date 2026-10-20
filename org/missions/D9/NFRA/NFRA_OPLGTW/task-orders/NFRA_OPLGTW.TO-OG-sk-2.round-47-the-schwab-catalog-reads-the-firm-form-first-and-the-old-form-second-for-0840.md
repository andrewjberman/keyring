# NFRA_OPLGTW task order -- `OG-sk-2` -- the Schwab catalog DUAL READ for master 08403355: the new firm-folder form first, the old form second, fenced by FILE NAME (round 47; the Schwab 0840 move to `schwab/49financial/`, Andrew-direct ~17:0xZ relayed; the CTO's ruling 2026-10-20 20:18Z; census `OG-sk-1` drained `9bcbf580a33`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sk-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sk-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~178</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, contract text and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this order (the reader IAM text is `OG-sk-3`).
comp-adversary: DECLARED-NOT-APPLICABLE -- the CTO's ruling of 2026-10-20 20:18Z: "the edit is a DUAL READ: new path first (silver in opal-data-assets/schwab/49financial/... by file name 08403355.parquet; state in opal-data-49financial/.../state/*/date=*/08403355.*), then the old schwab/08403355/ path"; and his condition (17:22Z): "the gateway's reads under schwab/49financial/ match the master's file name, never the folder alone ... the proof plants a second master's file in a test tree, and the reader must ignore it".
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-sk-2` (decomposition addendum R3-T.124, amendment A15, round 47, workstream ENRICH-R47-M)

WHY (RELAYED layout, not measured by this seat; cite what the CODE says). Master `08403355` moves in one cutover (window 2026-10-21 12:00Z-20:00Z): silver from `s3://opal-data-assets/schwab/08403355/silver/<table>/date=D/data.parquet` to `s3://opal-data-assets/schwab/49financial/silver/<table>/date=D/08403355.parquet`; the completion marker from `s3://opal-data-assets/schwab/08403355/meta/complete/date=D.json` to `s3://opal-data-49financial/schwab/49financial/state/complete/date=D/08403355.complete.json` (a DIFFERENT bucket). `08242234` and `08335338` DO NOT move. This gateway release must work BEFORE, DURING and AFTER the move, so each read tries the NEW form first and the OLD form second, and a firm folder holding another master's file must never widen anything.

READ FIRST: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~177/SK_CENSUS.json` (the census; its `dual_read_notes` say where a fallback is simple and where it is not) and `infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py`.

DO, in these files and nothing else:
1. **BOTH contract copies** (`infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json` and `org/standards/NFRA_OPLGTW_CONTRACT.json`, byte-equal before and after): add ONE new top-level key, after the last existing key, and change NOTHING else (every existing key stays byte-for-byte, `data_prefixes` and `completion_prefixes` included: the OLD form is the fallback):
```
"firm_form": {
  "masters": {"08403355": "49financial"},
  "state_bucket": "opal-data-49financial",
  "silver_prefixes": ["schwab/49financial/silver/dim_position/", "schwab/49financial/silver/dim_balance/", "schwab/49financial/silver/dim_asset/", "schwab/49financial/silver/dim_transaction/"],
  "completion_prefix": "schwab/49financial/state/complete/",
  "backfill_status_prefix": "schwab/49financial/state/backfill_status/"
}
```
2. `app/integrations/schwab/catalog.py` (the contract parser `parse_contract` must keep parsing; it ignores unknown keys today, so `firm_form` rides in `contract.raw`; do NOT add a field to `CatalogContract`). Add these module-level functions with EXACTLY these names and meanings:
   - `firm_form_masters(contract) -> dict` master to firm (`{}` when the contract has no `firm_form`);
   - `state_bucket(contract) -> str | None`;
   - `marker_locations(contract, master, date) -> list` of `(bucket, key)`: for a firm-form master FIRST `(state_bucket, completion_prefix + "date=" + date + "/" + master + ".complete.json")`, THEN `(contract.bucket, <the master's old completion prefix> + "date=" + date + ".json")`; for any other master only the old one;
   - `parse_silver_key(key)`: keep the old behaviour for an 8-digit master folder; for any OTHER folder segment (a firm folder) accept only a file name of exactly `<8 digits>.parquet` and return the master FROM THE FILE NAME as the first element, `(master, table, date, filename)`; a firm-folder key with any other file name (for example `data.parquet`) returns `None`;
   - a helper `_key_in_data(key, contract)` (module-private is fine): true when the key starts with one of `contract.data_prefixes` (today's test), OR it starts with one of `firm_form.silver_prefixes` AND `parse_silver_key(key)` names a master that is in `firm_form_masters(contract)`. Use it where `membership_findings` and `head_set` today test `key.startswith(p) for p in contract.data_prefixes`.
   - `Catalog.read_marker(master, date, policy_check)` returning `(marker_dict_or_None, version_id_or_None, (bucket, key) or None)`: iterate `marker_locations`; GET each with the catalog role; on an ABSENT answer (`_absent(exc)`) go to the next; on ANY OTHER `ClientError` raise `_Dependency` (NO fallback on an error: an AccessDenied on the new location must not silently read the old); return the first object found. Make `snapshot()` and the code that reads the marker use it instead of the single `marker_key` path (keep `marker_key` for the old-form callers and tests).
   - `Catalog.list_dates(master, policy_check)`: the UNION of the dates found under the old completion prefix (today's code) and, for a firm-form master, under `firm_form.completion_prefix` counting ONLY keys of the form `<completion_prefix>date=<D>/<master>.complete.json` (a file of another master in that folder is ignored); newest first, de-duplicated.
3. `app/integrations/schwab/integration.py`: the fetch path that today refuses any key outside `data_prefixes` (the census names it, about lines 203 to 220) must use the same `_key_in_data` rule (make it public as `key_in_data` in catalog.py if you need to import it). No other change.
4. NEW `tests/test_og_sk2.py`, at least SIX tests, offline, fakes only (`os.environ.setdefault("MOCK_GRAPH", "1")`; model the fake S3 on `tests/test_schwab_catalog.py`'s `World`/`Spy` helpers or on a small local fake with `get_object`/`list_objects_v2`; never the network): (1) the contract's `firm_form` parses and the two copies are byte-equal; (2) `parse_silver_key` takes the master from the file name for a firm-folder key and refuses `data.parquet` in a firm folder; (3) `membership_findings` and `head_set` admit the new-form and the old-form 08403355 keys and REFUSE a PLANTED `08242234.parquet` in the firm folder; (4) `read_marker`: new absent -> old read; both present -> new wins; AccessDenied on new -> `_Dependency`, old NOT read; (5) `list_dates` unions new and old and ignores another master's file under the new prefix; (6) an old-form master (`08335338`) never touches the state bucket.

## 2. BOUNDS

- Write only: `infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py`, `.../integration.py`, `.../deploy/NFRA_OPLGTW_CONTRACT.json`, `org/standards/NFRA_OPLGTW_CONTRACT.json`, `infra/aws/ec2/opal-gateway/tests/test_og_sk2.py`, `W/` and, if a row is needed, the channel. No Terraform, no other product file, no other test, no release, no deploy, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
org/standards/NFRA_OPLGTW_CONTRACT.json
infra/aws/ec2/opal-gateway/tests/test_og_sk2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~178/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W178-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sk-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)the deploy copy and the standards copy are identical \(parsed\): ok.*parse_silver_key: new form takes the master from the FILE NAME.*: ok.*membership: the new-form 08403355 key and the old-form key pass; a PLANTED 08242234 file in the firm folder is refused \(F_REJECTED_MASTER\): ok.*head_set keeps the new-form and old-form 08403355 keys and DROPS the planted 08242234 file in the firm folder: ok.*read_marker: the new location is ABSENT.*: ok.*read_marker: an ERROR \(AccessDenied\) on the new location raises the dependency error and does NOT fall back to the old: ok.*list_dates: the union of new and old dates.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sk-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_sk2\.py: (?:[6-9]|[1-9]\d+) passed, 0 failed.*neighbours \(4\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-sk-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk2.AC3.sh; echo "exit=$?"</invocation><expect>(?s)catalog\.py against the pin:.*: ok.*integration\.py against the pin:.*: ok.*the two contract copies are byte-equal: ok.*only added top-level key is \['firm_form'\]: ok.*uncommitted files outside the edit set \(0 expected when the worker has committed\): 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the dual-read behaviour with a fake S3 (the issuer's script, independent of your tests). `AC2`: your tests and the four neighbours pass (29 tests at the base; `tests/acceptance/test_local_acceptance.py::test_ogv2_a12` already fails at the base and is not yours). `AC3` (bounds): the edit set, the old-form contract keys byte-equal, the two copies byte-equal, the size of the diffs.

## 5. WHEN YOU ARE DONE

Commit, then write the proof instance at `W/NFRA_OPLGTW.TO-OG-sk-2.round-47-the-schwab-catalog-reads-the-firm-form-first-and-the-old-form-second-for-0840.proof_of_spec.json` and validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-sk-2.round-47-the-schwab-catalog-reads-the-firm-form-first-and-the-old-form-second-for-0840.md` (`python3`, not `python`: ruling msg 35901). `AC3` reads uncommitted files, so run it AFTER your commit. Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-M, amendment A15 of R3-T.124. Second of the cells for the 0840 move: this one is the code and the contract; `OG-sk-3` is the reader IAM text (two `.tf` files), `OG-sk-4` the `family_depth.py` backfill-status dual read. All three go into ONE small release (R3c) under its own signed pair, in the CTO's slot 2026-10-21 07:00Z-11:30Z, live before the cutover window.
- Why `firm_form` lives in the contract and `CatalogContract` is untouched: `parse_contract` already ignores unknown keys, so an OLD gateway reading the NEW contract keeps working, and a NEW gateway reading an OLD contract (no `firm_form`) behaves byte-for-byte as today (rollback is clean in both directions).
- Pre-cut: `AC1` base FAIL as expected; `AC2` base FAIL as expected (new test file absent; the four neighbours read 29 passed); `AC3` base FAIL as expected (0 added lines). Arm: a scratch reference (60 added lines in catalog.py plus the contract key in both copies) read `AC1` PASS (13 of 13 lines), `AC3` PASS and the four neighbours 29 passed, then was restored byte-for-byte. The `AccessDenied` arm of `AC1` first read ok at the base for the wrong reason (an `AttributeError`) and was tightened to require `_Dependency`.
- READINGS DISCLOSED: the layout is RELAYED; the census found no gateway reader of `last_run`, `conversions`, `pulls`, `daily_pull` or `_ops`, and no gateway bronze destination is named, so nothing is dual-read for them; the bronze closure partition check (`catalog.py` near line 456) reads `bronze_keys` from the marker's own closure and is NOT changed here (surprise row `Z-W177-S3` carries it).

<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-M</workstream>
<slot>~178</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
