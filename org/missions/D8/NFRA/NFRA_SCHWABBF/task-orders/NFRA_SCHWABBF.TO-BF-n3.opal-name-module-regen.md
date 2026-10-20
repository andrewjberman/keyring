# TO NFRA_SCHWABBF.TO-BF-n3 -- regenerate modules/opal_name for the new scope rows and add the secret_name output (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-n3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~6</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-n-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R3.md`) |
**outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-n-3`, CTO round-3 item R3-2 (msg 109913, relaying `4.0.0_SA_CRO` msg 109911): regenerate `infra/aws/terraform/modules/opal_name` so Terraform roots accept the new Cottonwood master rows (`infra/logic/registry/scopes.json` at `e5c3c708fc`) and master `08403355`, which has been missing from the module since commit `0be402e218`; and add a module output for the new library function `secret_name(system, scope, purpose)` (`lib/opal_naming.py`, commit `128d358eab`, `NAMING_SCHEMA` `secret.grammar`). The CRO's trial passed `terraform test` 72/72. Every name in the Alongside box's Terraform root (PRD C-ALONGSIDE: "every name goes through `modules/opal_name` with the `alongside` scope") needs this module current. This cell writes Terraform TEXT and tests. It applies nothing.

**What exists (read first).**
- `infra/aws/terraform/modules/opal_name/generated_locals.tf` is GENERATED. Its first lines name the generator: `python lib/opal_naming.py generate --out <dir> --target infra/aws/terraform/modules/opal_name/generated_locals.tf`. DO NOT edit it by hand; run the generator (to a scratch `--out` directory, then copy the one target file into place) so the header's registry hash is the registry's current hash. `python lib/opal_naming.py vectors` prints the vector JSON for `tests/vectors.json`.
- Module files: `main.tf`, `variables.tf`, `tests/opal_name.tftest.hcl`, `tests/fifo.tftest.hcl`, `tests/vectors.json`. Read `main.tf` first: it exposes `name()` as module outputs from input variables. Mirror that shape for `secret_name` with inputs `system`, `scope`, `purpose` and the grammar `lib/opal_naming.secret_name` implements (read that function and `NAMING_SCHEMA.json` `secret.grammar`; do not retype the grammar, test the module against the library's own output).
- `terraform` is on PATH and `terraform -chdir=infra/aws/terraform/modules/opal_name test -no-color` runs offline with no provider: at the base it reads `Success! 48 passed, 0 failed.`.
- `scopes.json` at HEAD already carries the Cottonwood masters `08719286, 08134043, 08165601, 08480305` in the cottonwood firm row and `08242234, 08335338, 08403355` in the 49financial row.

**Build.**
1. Regenerate `generated_locals.tf` with the generator; the new file contains all seven masters in its scope maps and the header carries the current registry hash. Do not change any other generated target.
2. Regenerate `tests/vectors.json` with `python lib/opal_naming.py vectors` (or the module test's own documented path); extend `tests/opal_name.tftest.hcl` with runs for: a Cottonwood master scope; `08403355`; and `secret_name` (at least three vectors taken from the library's own output).
3. Add the `secret_name` module output (and its variables) in `main.tf` / `variables.tf`, leaving every existing output and variable byte-identical in behavior.
4. A drift test `data/canonical/schwab/tests/test_opal_name_generated_current.py` (no network): run the generator for the module target into a temp directory and assert the result equals the committed `generated_locals.tf` byte for byte; assert `08403355`, `08719286`, `08134043`, `08165601` and `08480305` appear in the generated scope map; assert `main.tf` declares a `secret_name` output.

### ACCEPTANCE

<criterion id="BF3-n3-AC1" cell_refs="BF-n-3"><invocation>terraform -chdir=infra/aws/terraform/modules/opal_name test -no-color</invocation><expect>^Success! [0-9]+ passed, 0 failed\.$</expect></criterion>
`BF3-n3-AC1` -- the module's own tests, offline, including the new Cottonwood, `08403355` and `secret_name` runs (48 passed at the base; the count rises).

<criterion id="BF3-n3-AC2" cell_refs="BF-n-3"><invocation>python -m pytest data/canonical/schwab/tests/test_opal_name_generated_current.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-n3-AC2` -- the committed module equals the generator's output and carries the missing masters and the secret output.

<expected_criteria>BF3-n3-AC1,BF3-n3-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 `Success! 48 passed, 0 failed.` (PASS as expected: a control that must stay green); AC2 "file or directory not found" (rc 4) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (`lib/opal_naming.py`, the registry).
- **WORLD floor, nothing applied.** No `terraform init` against a backend, no `plan` or `apply`, no `aws` command, no deploy. `terraform test` is the only terraform command, and only inside the module directory.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass. Row ids are shared across rounds: read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W2-S<k>` and use the next.

<paths>
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/main.tf
infra/aws/terraform/modules/opal_name/variables.tf
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
infra/aws/terraform/modules/opal_name/tests/fifo.tftest.hcl
infra/aws/terraform/modules/opal_name/tests/vectors.json
data/canonical/schwab/tests/test_opal_name_generated_current.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R3.md</decomp_doc> (round 3), cell `BF-n-3`.
<owned_cells>BF-n-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-n3-AC1, BF3-n3-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~6/NFRA_SCHWABBF.TO-BF-n3.opal-name-module-regen.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF3-n3-AC1,BF3-n3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the generator command you ran, the new `terraform test` summary line, the pytest summary line, which module files changed and how, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a name module; no schedule.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; the opal_name module is a pure name function with no IAM resource and this cell touches no IAM; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the generated file must come from the generator, never by hand (stated in the face).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-3 item R3-2 (msg 109913 relaying CRO msg 109911); PRD v0.6 C-ALONGSIDE (names); decomposition round 3 cell BF-n-3.
