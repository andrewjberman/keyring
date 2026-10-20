# TO NFRA_SCHWABBF.TO-BF-p5 -- the converter family writes its completion marker, conversion manifest and backfill status to the state tier in the firm bucket

<to_id>NFRA_SCHWABBF.TO-BF-p5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-p-5` (`decompositions/NFRA_SCHWABBF_DECOMP_R5.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-p-5`, PRD v1.0 C-TIERS. Andrew-direct ~17:0xZ: "a, yes. this needs to go through the same full bronze/silver process that the other masters go through." For a firm-form master the `meta/` objects the converter writes become the builder's `state` tier in the FIRM bucket (CRO msg 109963, ruled by the CTO in v1.0 and msgs 109966 and 109970). Round 4 (merged `cdce7d6d13`) moved the SILVER keys; this cell moves the converter's META writes. Nothing is deployed; WORLD floor only because the Lambda twins sit under `infra/`.

**The contract (fixed in `decompositions/NFRA_SCHWABBF_DECOMP_R5.md`; re-stated here).** Firm-form masters: 08403355 (`49financial`), 08719286, 08134043, 08165601, 08480305 (`cottonwood`). For such a master M with firm F, the state bucket is `opal-data-49financial` (F = `49financial`) or `opal-data-cottonwood` (F = `cottonwood`) (builder output: `address('schwab','49financial','state','complete','date=2026-10-16')` is `s3://opal-data-49financial/schwab/49financial/state/complete/date=2026-10-16`), and:
- completion marker (today `schwab/M/meta/complete/date=D.json`) -> table `complete`, key `schwab/F/state/complete/date=D/M.complete.json` (D = the business date);
- conversion manifest (today `schwab/M/meta/conversions/{run_id}.json`, run id `YYYYMMDDTHHMMSSZ-xxxxxxxx`) -> table `conversions`, `schwab/F/state/conversions/date={UTC date of the run id}/M.{run_id}.json`;
- backfill status (today `schwab/M/meta/backfill-status.json`, ROLLING, overwritten in place) -> table `backfill_status`, `schwab/F/state/backfill_status/date={UTC date of the write}/M.backfill-status.json`. Readers take the NEWEST partition at or before today (CTO msg 109970); no fixed sentinel date.
For 08242234, 08335338 and every other source or family: TODAY's key and today's bucket, byte for byte.

**What exists (read first).** `data/assets/scripts/silver/conversion_manifest.py` (round-4 merge carries `FIRM_SILVER_MASTERS`, `silver_object_key`, `firm_silver_key`): `manifest_key(master, run_id)` (~line 72, `schwab/` + master + `/meta/conversions/` + run id), the completion-marker key (~line 183, `schwab/` + master + `/meta/complete/date=` + date + `.json`), `write_manifest_verified(client, bucket, manifest)` (~143), `write_complete_marker_verified(client, bucket, marker, ...)` (~276) and the closure/verdict code that reads markers back (~900-955). `data/assets/scripts/silver/schwab_runtime.py`: `MONOLITH = os.environ.get("MONOLITH_BUCKET", "opal-data-assets")` (line 36), the run entry that writes the manifest, the marker and then the ONE backfill-status fold via `bs.write_layer_status(...)` of `data/assets/scripts/lib/backfill_status.py` (`status_key(channel, scope)` returns `{channel}/{scope}/meta/backfill-status.json`; `read_status`, `write_layer_status(s3_client, bucket, channel, scope, layer, ...)`, `STATUS_BASENAME`). The vendored twins are flat byte-copies: in `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` (`conversion_manifest.py`, `schwab_runtime.py`, `backfill_status.py`) and `backfill_status.py` also in the etf, eclipse, orion and blackdiamond Lambda directories.
The bd-tree and Lambda code run standalone and cannot import `lib/opal_naming.py`: mirror the bucket and key rule as literals and PROVE them in the test against `lib.opal_naming.address()` and against `infra/logic/registry/scopes.json` (each firm row's `bucket`).

**Build.**
1. ONE pure function pair for the rule in `conversion_manifest.py`: `state_bucket_for(master)` (the firm bucket for firm-form masters; `None` for the others, meaning the caller keeps `MONOLITH`) and `state_key(master, table, date, name)` for the three tables above. Every meta write and read-back in the converter family for a firm-form master goes through them: the manifest write, the completion-marker write and its read-back/verdict code, and the backfill-status write and read in `schwab_runtime.py`. The clients pass the STATE bucket for those calls (the silver and bronze calls keep `opal-data-assets`).
2. `backfill_status.py` (the shared writer): switch the key and the bucket per master the same way, ONLY when `channel == "schwab"` and the scope is a firm-form master; every other channel/scope returns today's key byte-for-byte (a test over etf, eclipse, orion, blackdiamond and schwab 08242234/08335338 proves it). Keep the five Lambda copies of this file byte-equal to the source after your edit. Add the "newest partition at or before today" read (`read_status` for a firm-form master lists `schwab/F/state/backfill_status/` under the state bucket, filtered to names starting `M.`, and returns the newest `date=` partition's object).
3. Keep the two Schwab twins of `conversion_manifest.py` and `schwab_runtime.py` byte-equal to their sources. Leave `BUILD_MANIFEST.json` as is unless the vendored set changes.
4. Tests: new `data/assets/scripts/silver/tests/test_schwab_state_firm_key.py` and the shared writer's `data/assets/scripts/lib/tests/test_backfill_status.py`: (a) KEY/BUCKET parity: 5 firm-form masters x the three tables x 2 dates against `address(...)` and the registry's bucket; (b) OLD: 08242234 and 08335338, and the other channels, give the pre-change key and the `opal-data-assets` bucket (compare against `git show 0429204ae7:<path>` for the key functions); (c) a test whose name contains `firm_state_end_to_end`: the converter's own entry on a firm-form key with a fake S3 writes the marker, the manifest and the status to the STATE bucket and keys above and nothing under the old `meta/` keys; (d) rolling read returns the newest partition; (e) twin byte-equality for the five `backfill_status.py` copies and the two others.

### ACCEPTANCE

<criterion id="BF5-p5-AC1" cell_refs="BF-p-5"><invocation>python -m pytest data/assets/scripts/silver/tests/test_schwab_state_firm_key.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-p5-AC1` -- state key and bucket parity for the five masters against the builder and the registry, old-form parity, the rolling read, and twin equality.

<criterion id="BF5-p5-AC2" cell_refs="BF-p-5"><invocation>python -m pytest data/assets/scripts/silver/tests/test_schwab_state_firm_key.py -q -p no:cacheprovider --color=no -k firm_state_end_to_end</invocation><expect>^1 passed[ ,]</expect></criterion>
`BF5-p5-AC2` -- the seam probe against the REAL neighbor: the converter's own entry writes a firm-form master's marker, manifest and status to the state tier in the firm bucket and nowhere else.

<criterion id="BF5-p5-AC3" cell_refs="BF-p-5"><invocation>python -m pytest data/assets/scripts/lib/tests/test_backfill_status.py data/assets/scripts/silver/tests/test_schwab_runtime.py data/assets/scripts/silver/tests/test_conversion_manifest.py data/assets/scripts/silver/tests/test_mirror_conversion.py data/assets/scripts/silver/tests/test_etf_conversion.py data/assets/scripts/silver/tests/test_rebalancer_conversion.py -q -p no:cacheprovider --color=no --deselect data/assets/scripts/silver/tests/test_mirror_conversion.py::test_float64_declared_str_dtype_column_RAISES_VendorDriftError_naming_the_column</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-p5-AC3` -- the control: the shared writer's own tests and every family's tests that use it still pass (run it at the base first and record the count). ONE test is deselected because it already FAILS at the base for a reason outside this project (`test_mirror_conversion.py::test_float64_declared_str_dtype_column_RAISES_VendorDriftError_naming_the_column`: "this belt needs a NON-object string dtype ... pandas gave object", a pandas-version fact, measured 2026-10-20); do not touch it.

<expected_criteria>BF5-p5-AC1,BF5-p5-AC2,BF5-p5-AC3</expected_criteria>

Dry-run at the base: AC1 and AC2 "no tests ran" (rc 4) -- FAIL as expected; AC3 passes (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (notably `schwab_conversion.py`, `schwab_projections.py` and `set_identity_guard.py`, which round 4 closed).
- **WORLD floor, nothing deployed.** You do not build or upload any package, you touch no Lambda, S3 or other AWS service, and no network.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W1-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]` and keep the file's own line endings; verify `git diff --numstat` shows only added lines). Do not weaken the test to pass.

<paths>
data/assets/scripts/silver/conversion_manifest.py
data/assets/scripts/silver/schwab_runtime.py
data/assets/scripts/lib/backfill_status.py
data/assets/scripts/lib/tests/test_backfill_status.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_runtime.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/backfill_status.py
infra/aws/lambda/opal-assets/opal-assets-silver-etf/backfill_status.py
infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/backfill_status.py
infra/aws/lambda/opal-assets/opal-assets-silver-orion/backfill_status.py
infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/backfill_status.py
data/assets/scripts/silver/tests/test_schwab_state_firm_key.py
data/assets/scripts/silver/tests/test_schwab_runtime.py
data/assets/scripts/silver/tests/test_conversion_manifest.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R5.md</decomp_doc> (round 5), cell `BF-p-5`.
<owned_cells>BF-p-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF5-p5-AC1, BF5-p5-AC2, BF5-p5-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-p5.converter-state-tier.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF5-p5-AC1,BF5-p5-AC2,BF5-p5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the functions you added and where, every call site moved (file and line), the shared writer's switch, the AC3 count at the base and after, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- converter code and tests; no schedule.
comp-iam: RUN -- decomposition battery scanned silver.tf and monolith-iam.tf (2 Terraform files) and the firm buckets' own policies NOT read (blind); neither the converter role nor the box role can write the firm bucket today (cell BF-g-5 adds it); this cell touches no IAM; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 1 (state moves to a different bucket), 2 (the backfill-status writer is shared with other families) and 3 (rolling objects take the write date) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-TIERS; CTO msgs 109966 and 109970; decomposition round 5 cell BF-p-5; round-4 merge `cdce7d6d13`.
