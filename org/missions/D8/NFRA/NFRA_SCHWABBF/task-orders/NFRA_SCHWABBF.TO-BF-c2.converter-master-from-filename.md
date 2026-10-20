# TO NFRA_SCHWABBF.TO-BF-c2 -- the silver converter takes the master from the vendor file name (code, deployed twin, manifest)

<to_id>NFRA_SCHWABBF.TO-BF-c2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~5</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-c-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-c-2`, the consequence of PRD v0.5 C-KEYFORM for the thing every stored object wakes up. Andrew-direct 2026-10-20 ~14:3xZ: the bronze key is "schwab vendor and 49 firm ... cottonwood firm"; masters share a firm folder and are told apart by the vendor file name's master prefix.
The converter reads the master from path segment 1. Under the firm form segment 1 is the FIRM (`49financial`), so its folder claim for every file would be wrong.

**What exists (read, then change).**
- `data/assets/scripts/silver/schwab_conversion.py` lines 133-143: `scope_from_key(key)` returns `parts[1]` when `parts[0] == "schwab"` and `len(parts) > 1`, else `parts[0]` (the staging key shape `{master}/bronze/...`). Its docstring says identity binds from the BYTES and this only picks which path segment carries the folder's claim. `feed_from_key` (lines 146-160) and `date_from_key` (lines 179-197) already read the FILE NAME (`{master}.CRS{YYYYMMDD}.{TYPE}.zip`) and need no change.
- The deployed twin `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_conversion.py` is byte-equal to the source today (measured 2026-10-20). Its directory carries `BUILD_MANIFEST.json` listing `vendored_modules` (the source paths copied FLAT into the zip) and the build rules; read it and the generator it names (find it from the manifest's text, or `comp-which "how is the opal-assets-silver-schwab lambda package built"`), and keep the twin and the manifest exactly as that generator would produce them. Do not hand-type a hash.
- Other vendored modules in that directory (`schwab_runtime.py`, `conversion_manifest.py`, `set_identity_guard.py`, `silver_registry.py`) may also derive a master from a key by position; census them for `parts[`, `split("/")` and `scope_from_key` and say what you found (read-only unless it is the same bug; if it is, change it only if its file is in your `<paths>`, else file a row).

**Build.**
1. `scope_from_key(key)`: three shapes, each explicit:
   - monolith OLD master form `schwab/{8 digits}/bronze/...` -> that master (unchanged behavior; stored keys still use it until the cutover);
   - monolith FIRM form `schwab/{firm}/bronze/...` where `{firm}` is `49financial` or `cottonwood` -> the master is the 8 digits before the first `.` of the FILE NAME (`^(\d{8})\.`); a file name with no such prefix RAISES `ValueError` ("refusing to guess"), never a default;
   - staging `{master}/bronze/...` -> `parts[0]` (unchanged).
   Any other first or second segment RAISES as it would have failed before. Update the docstring: the claim still stays a claim and identity still binds from the bytes.
2. Apply the identical change to the twin and regenerate/adjust `BUILD_MANIFEST.json` the way its generator does. After your change the twin's `schwab_conversion.py` must again be byte-equal to the source.
3. Test `data/assets/scripts/silver/tests/test_schwab_scope_from_filename.py` (load the converter by path with `data/assets/scripts/lib` first on `sys.path`: it imports `stream_parquet`): old form, firm form for each of the seven masters (08242234, 08335338, 08403355 under `49financial`; 08719286, 08134043, 08165601, 08480305 under `cottonwood`), the staging form; a firm-form key whose file name has no master prefix RAISES; a firm-form key whose file-name master is not 8 digits RAISES; `feed_from_key` and `date_from_key` agree on a firm-form key; the twin is byte-equal to the source (compare file bytes); and `BUILD_MANIFEST.json` still parses and lists `schwab_conversion.py`.

4. **Issuer ruling 2026-10-20 after rows `NFRA_SCHWABBF-W5-S2` and `-S3` (amendment; the cell's intent is "the consumer tolerates the firm form", and these two modules are consumers that read the key by position).** Extend the same change to:
   - `data/assets/scripts/silver/conversion_manifest.py`: `_key_scope(key)` (line ~398) and `_bronze_type_and_date(key)` (line ~403, which accepts only an 8-digit folder after the type; the firm form's folder is `date=YYYY-MM-DD` and must yield the same `(type, YYYY-MM-DD)`). Old master form behavior stays.
   - `data/assets/scripts/silver/set_identity_guard.py`: `parse_bronze_key(key, scope)` (line ~63; today it requires `parts[1] == scope` and an 8-digit `parts[4]`, so a firm-form key returns `None` and the guard would count ZERO bronze for the master and say nothing). For the firm form it must return `(type, YYYY-MM-DD)` ONLY when the file name starts with `{scope}.`, so two masters sharing a folder never count each other's files; old form unchanged.
   - Both files' deployed twins in `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`, byte-equal to the source after your change, and their existing test files `data/assets/scripts/silver/tests/test_conversion_manifest.py` and `test_set_identity_guard.py` (add tests whose names contain `firm_form`).
   - Census where the `bronze_keys` census that feeds the guard and the manifest is LISTED (the S3 prefix it lists, in `schwab_runtime.py` or elsewhere in the vendored set). If it lists by `schwab/{scope}/bronze/` it misses firm-form keys: change it in `schwab_runtime.py` (source and twin) so it lists the firm folder filtered by the file-name master as well as the old prefix, and add a `firm_form` test; if it already lists correctly, say so in the report.
   Keep all existing behavior for old-form keys (stored keys stay old-form until the cutover).

### ACCEPTANCE

<criterion id="BF2-c2-AC1" cell_refs="BF-c-2"><invocation>python -m pytest data/assets/scripts/silver/tests/test_schwab_scope_from_filename.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-c2-AC1` -- the three key shapes, the refusals, and the twin byte-equality.

<criterion id="BF2-c2-AC2" cell_refs="BF-c-2"><invocation>python -m pytest data/assets/scripts/silver/tests/test_schwab_runtime.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-c2-AC2` -- the control against the REAL neighbor: the converter's own runtime tests still pass (11 passed at the base).

<criterion id="BF2-c2-AC3" cell_refs="BF-c-2"><invocation>python -m pytest data/assets/scripts/silver/tests/test_set_identity_guard.py data/assets/scripts/silver/tests/test_conversion_manifest.py -q -p no:cacheprovider --color=no -k firm_form</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-c2-AC3` -- the two by-position consumers (set-identity guard and conversion manifest) read a firm-form key, master-filtered by the file name (added by the issuer ruling above).

<expected_criteria>BF2-c2-AC1,BF2-c2-AC2,BF2-c2-AC3</expected_criteria>

Dry-run at the base 2026-10-20: AC1 "no tests ran" (rc 4) -- FAIL as expected; AC2 `11 passed` -- PASS as expected (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing deployed.** You do not build or upload the package, you do not touch Lambda or AWS, and no network. The Terraform deploy of the new package is the issuer's release act.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/assets/scripts/silver/schwab_conversion.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_conversion.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json
data/assets/scripts/silver/tests/test_schwab_scope_from_filename.py
data/assets/scripts/silver/conversion_manifest.py
data/assets/scripts/silver/set_identity_guard.py
data/assets/scripts/silver/schwab_runtime.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/set_identity_guard.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_runtime.py
data/assets/scripts/silver/tests/test_conversion_manifest.py
data/assets/scripts/silver/tests/test_set_identity_guard.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-c-2`.
<owned_cells>BF-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-c2-AC1, BF2-c2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~5/NFRA_SCHWABBF.TO-BF-c2.converter-master-from-filename.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-c2-AC1,BF2-c2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the diff of `scope_from_key` in one sentence, what the census of the other vendored modules found, how the manifest was regenerated (command), the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- converter code and tests.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell touches no IAM; BLIND: the live IAM plane and the converter's execution role (0 roles read; cell BF-i-2 reads the role from silver.tf).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 3 (the converter reads segment 1; the twin carries a build manifest) is inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-KEYFORM consequence; CTO round-1 analysis ruling 1 (converter takes the master from the vendor file name); decomposition round 2 cell BF-c-2.
