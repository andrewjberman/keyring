# TO NFRA_SCHWABBF.TO-BF-s4 -- the converter family writes, reads back, lists and checks silver on the firm form for firm-form masters

<to_id>NFRA_SCHWABBF.TO-BF-s4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-s-4` (`decompositions/NFRA_SCHWABBF_DECOMP_R4.md`) |
**outcome_ref:** FWD-1, FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-s-4`, PRD v0.9 C-TIERS. Andrew-direct ~17:0xZ: "a, yes. this needs to go through the same full bronze/silver process that the other masters go through." The silver of a firm-form master moves to the firm folder, and **the silver key carries the master in its file name** (v0.9, on the CVO's refusal: one fixed `date=D/data.parquet` per table would let several masters overwrite one another): for a firm-form master M with firm F, table T and date D the silver object is `schwab/{F}/silver/{T}/date={D}/{M}.parquet` = `address('schwab', F, 'silver', T, 'date=D')` without `s3://opal-data-assets/`, plus `/{M}.parquet`. Firm-form masters: 08403355 (`49financial`) and 08719286, 08134043, 08165601, 08480305 (`cottonwood`). For 08242234, 08335338 and any other master the key is TODAY's `schwab/{M}/silver/{T}/date={D}/data.parquet`, byte for byte. "The same converters, the same silver tables and completion markers, triggered the same way. Nothing is converted by a one-off path." Every other byte of the converter's output is unchanged.
WORLD floor only because the Lambda twins sit under `infra/`; nothing is deployed, uploaded or run in AWS.

**What exists (read first).** The converter family under `data/assets/scripts/silver/` and its five vendored twins (flat copies, byte-equal to the sources) in `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`: `schwab_conversion.py`, `conversion_manifest.py`, `schwab_projections.py`, `set_identity_guard.py`, `schwab_runtime.py`. Round 2 (merged `3d7a1d172f`) made them read the firm-form BRONZE key and scope the master from the file name; the silver side is still master-folder.
Silver-key sites measured 2026-10-20 (census them again; this list is a start, not an inventory):
- `silver_registry.py:201-202` `silver_key(obj, observed_scope, section)` returns `{source}/{scope}/silver/{table}/date={D}/data.parquet`. **This module is SHARED with the other source families (each family Lambda vendors a copy); DO NOT EDIT IT.** Apply the Schwab override in the Schwab-only modules, after `silver_key` returns.
- `schwab_projections.py:93-96` `dim_key(scope, dim_name, date)` returns `schwab/{scope}/silver/{dim}/date={D}/data.parquet`.
- `conversion_manifest.py:402-405` `canonical_object_key(master, table, date)` returns the same shape (the object a partition may hold, used for read-back).
- `set_identity_guard.py:~183` `walk("schwab/" + scope + "/silver/")` lists a master's silver, and `parse_silver_key(key, scope)` (~line 73) parses `schwab/{scope}/silver/{table}/date={date}/{file}`; both read the master from path position `parts[1]`.
- `schwab_conversion.py:397,538` read `skey.split("/silver/")[1].split("/")[0]` (the fact name); check they hold for the firm key. The closure verdict's partition check in `conversion_manifest.py` (it uses `bronze_key_in_partition` for bronze; find its silver twin) and `schwab_runtime.py`'s `day_inventory` must count only THIS master's objects in a shared firm folder.
- The completion markers (`meta/complete/...`) and manifests (`meta/conversions/...`, `backfill-status.json`) are META, which is round 5: leave their keys exactly as they are, and say in your report which functions you saw that build a meta key.

**Build.**
1. ONE pure function in the Schwab-only code for the rule above (put it where the import direction allows with no cycle: a leaf such as `schwab_projections.py`, imported by the others), with `FIRM_SILVER_MASTERS = {"08403355": "49financial", "08719286": "cottonwood", "08134043": "cottonwood", "08165601": "cottonwood", "08480305": "cottonwood"}`. Every silver key the family writes, reads back, lists or parses for a master goes through it: `dim_key`, `canonical_object_key`, the fact key produced by `silver_key` (map its result), the set-identity guard's walk and parser, the closure verdict, the runtime inventory.
2. For firm-form masters the guard and the census FILTER by the file name `{M}.parquet` inside the shared firm folder (two masters' objects in one folder are never counted as each other's).
3. Old-form masters: no behavior change at all. A test proves it by running the pre-round function and the new one on the same inputs (the pre-round source is `git show 5f1ad506a4:data/assets/scripts/silver/<file>`).
4. Update the twins so each is byte-equal to its source again; `BUILD_MANIFEST.json` changes only if the vendored set changes (a new module would need an entry; prefer none).
5. Tests: new `data/assets/scripts/silver/tests/test_schwab_silver_firm_key.py` (load modules by path with `data/assets/scripts/lib` first on `sys.path`; it imports `stream_parquet`): (a) KEY: for the five firm-form masters x 18 table names (take them from `workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_schwab_08403355_*.yaml`) x 2 dates, the function equals `address(...)` plus `/{M}.parquet`; (b) OLD: for 08242234 and 08335338 the result equals the pre-round key; (c) GUARD: a stubbed shared firm folder holding 08403355's and 08719286's objects; `walk` and the census count each master's own objects only; (d) a test whose name contains `firm_silver_end_to_end`: run the converter's own conversion entry (use the synthetic bronze fixtures the existing converter tests use) on a firm-form 08403355 key with a fake S3 client and assert the silver written lands at `schwab/49financial/silver/<table>/date=<D>/08403355.parquet`, the old path is NOT written, and the set-identity guard finds the object; (e) twin byte-equality. Extend the existing test files only where a changed function's own test needs it.

### ACCEPTANCE

<criterion id="BF4-s4-AC1" cell_refs="BF-s-4"><invocation>python -m pytest data/assets/scripts/silver/tests/test_schwab_silver_firm_key.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF4-s4-AC1` -- the firm silver key for the five masters x 18 tables x 2 dates against the builder, the old-form parity, the master-filtered guard, and twin equality.

<criterion id="BF4-s4-AC2" cell_refs="BF-s-4"><invocation>python -m pytest data/assets/scripts/silver/tests/test_schwab_silver_firm_key.py -q -p no:cacheprovider --color=no -k firm_silver_end_to_end</invocation><expect>^1 passed[ ,]</expect></criterion>
`BF4-s4-AC2` -- the seam probe against the REAL neighbor: the converter's own conversion entry writes a firm-form key's silver at the firm silver address and nowhere else.

<criterion id="BF4-s4-AC3" cell_refs="BF-s-4"><invocation>python -m pytest data/assets/scripts/silver/tests/test_schwab_scope_from_filename.py data/assets/scripts/silver/tests/test_schwab_runtime.py data/assets/scripts/silver/tests/test_set_identity_guard.py data/assets/scripts/silver/tests/test_conversion_manifest.py data/assets/scripts/silver/tests/test_schwab_conversion.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF4-s4-AC3` -- the control: the family's existing tests still pass (122 passed at the base) with the tests you extend.

<expected_criteria>BF4-s4-AC1,BF4-s4-AC2,BF4-s4-AC3</expected_criteria>

Dry-run at the base 2026-10-20: AC1 and AC2 "no tests ran" (rc 4) -- FAIL as expected; AC3 `122 passed` -- PASS as expected (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (notably `silver_registry.py`, which is shared, and every `meta` key).
- **WORLD floor, nothing deployed.** You do not build or upload the package, you do not touch Lambda, S3 or any other AWS service, and no network.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W1-S<k>` and use the next), and do not weaken the test to pass.

<paths>
data/assets/scripts/silver/schwab_conversion.py
data/assets/scripts/silver/conversion_manifest.py
data/assets/scripts/silver/schwab_projections.py
data/assets/scripts/silver/set_identity_guard.py
data/assets/scripts/silver/schwab_runtime.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_conversion.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_projections.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/set_identity_guard.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_runtime.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json
data/assets/scripts/silver/tests/test_schwab_silver_firm_key.py
data/assets/scripts/silver/tests/test_conversion_manifest.py
data/assets/scripts/silver/tests/test_set_identity_guard.py
data/assets/scripts/silver/tests/test_schwab_conversion.py
data/assets/scripts/silver/tests/test_schwab_runtime.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R4.md</decomp_doc> (round 4), cell `BF-s-4`.
<owned_cells>BF-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF4-s4-AC1, BF4-s4-AC2, BF4-s4-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-s4.converter-silver-firm-key.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF4-s4-AC1,BF4-s4-AC2,BF4-s4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the function you added and where, every call site you moved to it (file and line), the meta-key functions you saw and left alone, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- converter code and tests; no schedule.
comp-iam: RUN -- decomposition battery scanned silver.tf and monolith-iam.tf (2 Terraform files); the converter's silver write grant covers `schwab/<master>/silver/*` over silver_source_scopes and not the firm prefix (cell BF-i-4 adds it); this cell touches no IAM; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 1 (three key builders, two walkers), 2 (shared folder, filter by file name) and 3 (silver_registry is vendored by other families) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.9 C-TIERS; Andrew-direct ~17:0xZ; decomposition round 4 cell BF-s-4; round-2 merge `3d7a1d172f`.
