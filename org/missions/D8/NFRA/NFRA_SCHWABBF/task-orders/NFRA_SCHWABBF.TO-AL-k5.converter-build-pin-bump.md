# TO NFRA_SCHWABBF.TO-AL-k5 -- bump the schwab converter build pin in silver.tf to the commit that carries the Cottonwood basis labels, and move its pin test (Terraform text and a test only)

<to_id>NFRA_SCHWABBF.TO-AL-k5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~21</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-pin</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-k-5` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** `AL-c-4` merged (`be55cb3071f`; your base carries it).

---

## WORKER FACE

### THE CELL

`AL-k-5`. The schwab converter Lambda is built from a pinned commit: `local.silver_build_commit["schwab"]` in `infra/aws/terraform/opal-assets/silver.tf` (line ~125, now `"27acf60210"`) names the commit whose `data/assets/scripts/silver/` tree the package directory `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` is byte-equal to, module by module, for every file in that directory's `BUILD_MANIFEST.json` `vendored_modules`. Cell `AL-c-4` (merged `be55cb3071f`) added the four Cottonwood masters to `conversion_manifest.py` and `silver_registry.py` in the source and in the package twin, so the old pin no longer matches the package. This cell moves the pin to `be55cb3071` (the ten-character form the file uses; `git rev-parse be55cb3071f` gives the full commit) and moves the pin test with it. You run no `terraform` command and no `aws` command. Nothing is deployed; WORLD only because the files sit under `infra/`.

**Read first (read-only unless in `<paths>`):** `infra/aws/terraform/opal-assets/silver.tf` lines ~85-126 (the pin comments and the map; the comment names the rollback pin and says what the pin carries) and `data/canonical/schwab/tests/test_schwab_build_pin.py` (the whole file: its constants `_PIN = "27acf60210"` and `_ROLLBACK = "12ecbe2b8f"`, the tests that read the pin from the Terraform text and prove it against git: value and rollback named, the other four entries unchanged at `dee04e1b01`, the commit resolves and is an ancestor of HEAD, and the package dir equals that commit's blobs for each vendored module).

**Build.**
1. `silver.tf`: change ONLY the `schwab` entry of `silver_build_commit` from `"27acf60210"` to `"be55cb3071"`, and extend the pin comment above the map with one new paragraph in the file's own style: `NFRA_SCHWABBF AL-k-5 moves it to be55cb3071: the merge that carries the four Cottonwood masters in conversion_manifest.py BASIS_LABEL and silver_registry.py DECLARED_SCHWAB_MASTERS (source and package twin byte-equal; tested by data/canonical/schwab/tests/test_schwab_build_pin.py). Rollback pin: 27acf60210.` Keep every earlier comment line (the earlier `Rollback pin:` lines stay; the NEW last `Rollback pin:` line names `27acf60210`). The other four entries (`etf`, `blackdiamond`, `eclipse`, `orion`) stay byte-identical.
2. `test_schwab_build_pin.py`: set `_PIN = "be55cb3071"` and `_ROLLBACK = "27acf60210"`; keep every other test and constant; if a test asserts the comment names `Rollback pin: {_ROLLBACK}` it now finds the new line. If any test reads the pin's commit message or an expected file list, update only what the new pin changes and say what.
3. Do NOT edit any package file, any source file, or any other root.

### ACCEPTANCE

<criterion id="AL5-k5-AC1" cell_refs="AL-k-5"><invocation>python -m pytest data/canonical/schwab/tests/test_schwab_build_pin.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL5-k5-AC1` -- the pin names `be55cb3071`, the rollback is named, the other entries are unchanged, the commit resolves and is an ancestor of HEAD, and the package equals that commit's blobs module by module.

<expected_criteria>AL5-k5-AC1</expected_criteria>

Dry-run at the base 2026-10-21 (issuer, after `AL-c-4` merged): `1 failed, 4 passed`. The failing arm is `test_build_pin_package_dir_byte_equal_module_by_module`: the package dir no longer equals the OLD pin's blobs, because `AL-c-4` changed `conversion_manifest.py` and `silver_registry.py` in it. That failure is the defect this cell removes -- FAIL as expected. Change the TEST constants first and watch the value-and-rollback arms fail on the unedited `silver.tf`, then edit `silver.tf` and see all five pass.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **Nothing applied or deployed.** The module reads its code from S3, so changing the pin alone stamps new text on old code: building and uploading the package and applying the Lambda are a later CloudOps order under a never-widen pair. Say that in your report; do not claim the Lambda is updated.
- **Refusal clause.** If a criterion cannot be met as written (the package does not equal that commit's blobs for some module), stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W21-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken the test.

<paths>
infra/aws/terraform/opal-assets/silver.tf
data/canonical/schwab/tests/test_schwab_build_pin.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-k-5`.
<owned_cells>AL-k-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL5-k5-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~21/NFRA_SCHWABBF.TO-AL-k5.converter-build-pin-bump.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL5-k5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the changed lines with file and line, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- finding: the module reads its code from S3, so a pin bump without the artifact build is a false statement of what runs; the later CloudOps order builds, uploads and applies in that order, and its after-read prints the deployed OPAL_BUILD_COMMIT.
lane: the <paths> block IS the grant.
</preflight>

Source: `2.0.0_SA_COO~SB` msg 110155 (bump the schwab pin in the same cell as the check, the `test_schwab_build_pin.py` pattern); decomposition cell AL-k-5.
