# TO NFRA_SCHWABBF.TO-AL-c4 -- the converter learns the four Cottonwood masters: basis labels and declared masters, source and Lambda twin (text and tests only)

<to_id>NFRA_SCHWABBF.TO-AL-c4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~20</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-converter</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-c-4` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** `BF-w-7` merged (`e2fea02fad`); your base carries it.

---

## WORKER FACE

### THE CELL

`AL-c-4`. The Alongside box landed 71 Cottonwood bronze files for master `08719286` (2026-10-21). Each one fires the silver converter Lambda `opal-assets-silver-schwab`, and the converter raised `ManifestError: master '08719286' has no basis label` (`data/assets/scripts/silver/conversion_manifest.py`, `build_manifest`, the check `if master not in BASIS_LABEL`), so no manifest is built and the events retry to the dead-letter queue (`2.0.0_SA_COO~SB`'s report, msg 110152). The converter's per-master constants know only the three 49F masters. This cell adds the four Cottonwood masters (08719286, 08134043, 08165601, 08480305) to those constants, in the source and in the Lambda's vendored twin, with tests. Nothing is deployed or run; WORLD only because `infra/` holds the twin.

**What exists (read first, read-only unless in `<paths>`):** `data/assets/scripts/silver/conversion_manifest.py` lines ~74-80 (`BASIS_LABEL = {"08242234": "SCHWAB-RPS basis", "08335338": "BD-sourced 49F basis", "08403355": "Tax SMA basis"}`, "the ONE constants source ... key-tied to silver_registry.DECLARED_SCHWAB_MASTERS by test") and the two `raise ManifestError(... has no basis label ...)` sites (lines ~158 and ~818); `data/assets/scripts/silver/silver_registry.py` line 56 (`DECLARED_SCHWAB_MASTERS = ("08242234", "08335338", "08403355")`, "the INDEPENDENT side of the declared/observed pair"); the test that ties them: `data/assets/scripts/silver/tests/test_conversion_manifest.py` lines ~53-58 (`assert set(cm.BASIS_LABEL) == set(sr.DECLARED_SCHWAB_MASTERS)`). The Lambda package `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` holds BYTE-IDENTICAL vendored copies of these files and a `BUILD_MANIFEST.json` listing them; the repo files are the source of truth.

**Build.**
1. `conversion_manifest.py`: ADD to `BASIS_LABEL` exactly these four entries after the three existing ones (the existing three stay byte-identical): `"08719286": "Cottonwood firm master basis"`, `"08134043": "Cottonwood advisor master basis (08134043)"`, `"08165601": "Cottonwood advisor master basis (08165601)"`, `"08480305": "Cottonwood advisor master basis (08480305)"`. Add a comment above them: the labels are per-master identities for the never-summed rule; whether the firm master's accounts overlap its advisor masters' accounts is UNMEASURED (open question to the CRO), and no label implies it either way; every master stays its own never-summed lane. No personal names in code.
2. `silver_registry.py`: change `DECLARED_SCHWAB_MASTERS` to the tuple of the three existing masters followed by `"08719286", "08134043", "08165601", "08480305"` (order kept, nothing else in the file changes).
3. Copy the two edited source files over their twins `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py` and `.../silver_registry.py` byte for byte (the twins are vendored copies; no other twin edit). Open `BUILD_MANIFEST.json`: if it records any hash, size or version of the two files, update ONLY those fields; if it records none, leave it unedited and say so in your report.
4. Tests: new file `data/assets/scripts/silver/tests/test_cottonwood_basis_labels.py` (names contain `cottonwood_basis`): the four masters are in `cm.BASIS_LABEL` with the four exact strings above; `set(cm.BASIS_LABEL) == set(sr.DECLARED_SCHWAB_MASTERS)`; the seven masters are the registry's seven (`infra/logic/registry/scopes.json` rows of class MASTER with vendor `schwab`: read them, and require the set to be equal both ways); `cm.build_manifest` for a Cottonwood master does NOT raise `ManifestError` on the basis check (call it with the same minimal arguments the existing tests use for an existing master, copying their fixture, with master 08719286; if its other arguments cannot be built from a fixture, test the label lookup path only and say so); and `twin_identical` (names contain `twin_identical`): each edited source file is byte-equal to its Lambda twin. In `test_conversion_manifest.py` edit ONLY an assertion that pins exactly three masters or the old `DECLARED` tuple; the other five Schwab converter test files (`test_schwab_runtime.py`, `test_schwab_silver_firm_key.py`, `test_schwab_state_firm_key.py`, `test_set_identity_guard.py`, `test_schwab_scope_from_filename.py`) are in your grant only to fix an assertion that the change breaks, and you report each such edit.

### ACCEPTANCE

<criterion id="AL4-c4-AC1" cell_refs="AL-c-4"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cottonwood_basis_labels.py -q -p no:cacheprovider --color=no -k "cottonwood_basis"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL4-c4-AC1` -- the four masters have their basis labels and are declared, tied to the registry both ways, and a Cottonwood manifest no longer raises on the basis check.

<criterion id="AL4-c4-AC2" cell_refs="AL-c-4"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cottonwood_basis_labels.py -q -p no:cacheprovider --color=no -k "twin_identical"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL4-c4-AC2` -- the Lambda twins are byte-equal to the edited sources.

<criterion id="AL4-c4-AC3" cell_refs="AL-c-4"><invocation>python -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py data/assets/scripts/silver/tests/test_schwab_runtime.py data/assets/scripts/silver/tests/test_schwab_silver_firm_key.py data/assets/scripts/silver/tests/test_schwab_state_firm_key.py data/assets/scripts/silver/tests/test_set_identity_guard.py data/assets/scripts/silver/tests/test_schwab_scope_from_filename.py data/assets/scripts/silver/tests/test_cottonwood_basis_labels.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL4-c4-AC3` -- the converter's whole Schwab test set stays green (121 passed at the base, plus the new tests).

<expected_criteria>AL4-c4-AC1,AL4-c4-AC2,AL4-c4-AC3</expected_criteria>

Dry-run at the base 2026-10-21: AC1 and AC2 name a test file that does not exist (rc 4) -- FAIL as expected; AC3 names that file too, so pytest exits 4 -- FAIL as expected (the six existing files alone: 121 passed, a control). Write the new test file FIRST and watch its `cottonwood_basis` arms fail on the unedited constants.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit (including `schwab_conversion.py`, `set_identity_guard.py`, `lambda_function.py`, every other twin, Terraform).
- **WORLD floor, nothing deployed or run.** No `terraform`, no `aws`, no Lambda build, no upload. The deploy of the converter is a later CloudOps act under a never-widen pair.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W20-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a test.

<paths>
data/assets/scripts/silver/conversion_manifest.py
data/assets/scripts/silver/silver_registry.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/silver_registry.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json
data/assets/scripts/silver/tests/test_cottonwood_basis_labels.py
data/assets/scripts/silver/tests/test_conversion_manifest.py
data/assets/scripts/silver/tests/test_schwab_runtime.py
data/assets/scripts/silver/tests/test_schwab_silver_firm_key.py
data/assets/scripts/silver/tests/test_schwab_state_firm_key.py
data/assets/scripts/silver/tests/test_set_identity_guard.py
data/assets/scripts/silver/tests/test_schwab_scope_from_filename.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-c-4`.
<owned_cells>AL-c-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL4-c4-AC1, AL4-c4-AC2, AL4-c4-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~20/NFRA_SCHWABBF.TO-AL-c4.cottonwood-basis-labels.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL4-c4-AC1,AL4-c4-AC2,AL4-c4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the changed lines with file and line, whether `BUILD_MANIFEST.json` needed an edit, any assertion you edited in the other test files, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- findings: (1) the converter's own rule "an unknown master never gets a defaulted basis" is why this is a cell, not a default; (2) the firm-versus-advisor overlap is unmeasured and is stated in the code comment, not guessed; (3) the Lambda is shared with the 49F masters, so the change adds keys and edits nothing existing.
lane: the <paths> block IS the grant.
</preflight>

Source: `2.0.0_SA_COO~SB` msg 110152 (the ManifestError), CloudOps `TO-AL-r2` evidence (71 landed files); decomposition cell AL-c-4.
