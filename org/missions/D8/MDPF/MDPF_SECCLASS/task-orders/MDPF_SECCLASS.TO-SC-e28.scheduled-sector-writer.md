# TO MDPF_SECCLASS.TO-SC-e28 -- round 8 SC-e-28: FWD-12 -- the scheduled sector writer: sector and industry group copied from the Bloomberg characteristics file onto each security's row

<to_id>MDPF_SECCLASS.TO-SC-e28</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~24</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-28` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-12 | **depends_on:** MDPF_SECCLASS.TO-SC-e27 (the field names and closed values it writes are declared
there; starts after it drains). Slot ~24's third order. After it: the issuer's sector write act, then `SC-e-29`.

---

## WORKER FACE

### THE CELL

`SC-e-28`: the scheduled sector writer. It copies the sector and the industry group from the Bloomberg characteristics file onto
each security's row in `etf-classifications`. Names and homes from builder output; built, tested, dry run against live inputs;
Terraform declared, NOT applied; its half request written.

- FWD-12 (PRD v0.12): the shared list carries each security's sector and industry group.
- PRD ADDENDUM v0.5: "The Bloomberg characteristics file is an INPUT: a scheduled writer copies `GICS_SECTOR_NAME` onto the
  security's row. A correction is made in the seed source and wins, as for every field (C-WRITER)." ADDENDUM v0.10: the industry
  group (`GICS_INDUSTRY_GROUP_NAME`) moves onto the list with the sector. **C-NOCHAR:** no measurement (ratio, market value,
  yield, duration, beta, price) enters the table; the file keeps its home and its readers. A SCHEDULED PRODUCER, not an alert or
  monitor (CLAUDE.md moratorium; CTO rulings batch 257 Q5): no alarm, SNS, SES or metric filter.

**Inputs:**
- **The two field names and their closed value lists:** `org/standards/MDPF_SECCLASS_CONTRACT.json` at the version `TO-SC-e27`
  landed. A value outside the closed list is NOT written: it is listed in the run's output as `OUT-OF-LIST` with its security.
- **The characteristics file:** `s3://opal-data-etfs/bbg/<date>/characteristics.parquet` (the ETF producer's input:
  `data/etfs/scripts/gold/etf_positioning_gold.py:91` `BBG_ROOT = "bbg"`, `:1690`; the landing signal is
  `bbg/<date>/run_manifest.json`, `:474`). Measured 2026-10-07: newest partition 2026-10-05, 114 rows, key column `security`
  (a Bloomberg security string), `NAME`, `GICS_SECTOR_NAME` (107 non-null), `GICS_INDUSTRY_GROUP_NAME` (107 non-null). It covers
  the ETF books' holdings only (114 securities against 3,507 table rows), which is FWD-12's population (the ETF view); say how
  many table rows the dry run would touch.
- **Key resolution:** how a characteristics `security` maps to an `etf-classifications` key -- read the existing mapping in
  `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` and `rivalfunds_classification.py`
  (`security_bloomberg`, `identifier_namespace` BLOOMBERG rows; US bare tickers). A security that resolves to no row is listed
  `NO-ROW`, never created by this writer.
- **The template:** the FWD-10 producer and its root, `infra/aws/lambda/mdpf-secclass/new-security-classifier/` and
  `infra/aws/terraform/mdpf-secclass/new-security-classifier/` (`main.tf`, `lambda.tf`, `iam.tf`, `schedule.tf`; header of
  `main.tf` for the plan-only and LGIC shape; `schedule.tf` for the EventBridge Scheduler with a timezone).

**Build (code, tests, dry run and declared infra; NO apply and NO table write -- the write is the issuer's act under its own half):**
1. **The writer.** `infra/aws/lambda/mdpf-secclass/sector-writer/lambda_function.py`. For the newest partition with a
   `run_manifest.json` and a characteristics file: per security, resolve the key (consistent get); if the row's two fields
   already equal the file's values, skip (`PRESENT`); else plan a conditional `UpdateItem` that sets ONLY the two new fields
   (never `sector`, `sub_asset_class`, `asset_class` or any other attribute) with a condition that the row exists. A row whose
   value was corrected in the seed source wins (C-WRITER): define and test how that is read (e.g. a `classified_by`/seed marker
   on the field), and state it. `dry_run` is the default without `{"write": true}`. Write the run's list (key, security, planned
   values, state PLANNED/WRITTEN/PRESENT/NO-ROW/OUT-OF-LIST/SEED-WINS) to an S3 address from `lib/opal_naming.py address()`.
   ASCII only.
2. **Tests.** `infra/aws/lambda/mdpf-secclass/sector-writer/tests/test_sector_writer.py`, S3 and DynamoDB stubbed: only the two
   fields are in the update expression; an out-of-list value is not written; a missing row is `NO-ROW` and nothing is created;
   a present value is skipped; the dry run makes zero write calls (count them); the seed-wins rule.
3. **Rule 30 / LGIC.** Every resource name is `lib/opal_naming.py name(system, scope, function, kind, qualifier=None)` output and
   every S3 address `address(source, scope, tier, table, partition, object=None)` output. A builder REFUSAL is a missing
   registry row: add it to `infra/logic/registry/resources.json` or `systems.json`; never hand-type a name. Homes and tenancy
   per `infra/logic/02_DOCTRINE.md`.
4. **Declared Terraform (NOT applied).** `infra/aws/terraform/mdpf-secclass/sector-writer/` (`main.tf` with backend key
   `mdpf-secclass/sector-writer/tfstate`, `lambda.tf`, `iam.tf`, `schedule.tf`): the Lambda from the S3 artifact pattern; a
   Monday-to-Friday schedule after the characteristics file lands (measure its landing times from `LastModified` of recent
   partitions, pick the time and say why; Friday's file is Monday's answer); a role with `s3:GetObject`/`s3:ListBucket` on
   `opal-data-etfs/bbg/*` only, `dynamodb:GetItem` and conditional `dynamodb:UpdateItem` on `etf-classifications` only, and
   `s3:PutObject` on the run list's address only. Run `comp-iam service <function name>` on the declared root and report it.
5. **The dry run.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sector_writer_dry_run.py --packaged`:
   assembles the files the Lambda would ship (handler plus every `_shared` module it imports) into a temp dir, imports the
   handler from that packaged layout, runs it in dry run against the live inputs and prints
   `SECTOR-WRITER-DRY-RUN partition=<date> securities=<n> planned=<n> present=<n> no_row=<n> out_of_list=<n> seed_wins=<n>`.
6. **The half request.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SECTOR_ROWS_<YYYYMMDD>.md`:
   the act (apply the root, upload the artifact, the first real fire), its BLAST RADIUS (the two fields on the planned rows, the
   table, the run-list address), the dry run's counts and row set, the rollback per key (the prior value of the two fields,
   which is absent today), both branches of the outcome, and `## COO half -- UNSIGNED` / `## CTO half -- UNSIGNED` headings.

### ACCEPTANCE

<criterion id="SC8-e28-AC1" cell_refs="SC-e-28"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/mdpf-secclass/sector-writer/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC8-e28-AC1` -- the writer sets only the two fields, refuses out-of-list values, creates no row and writes nothing in a dry run.

<criterion id="SC8-e28-AC2" cell_refs="SC-e-28"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sector_writer_dry_run.py --packaged</invocation><expect>SECTOR-WRITER-DRY-RUN partition=</expect></criterion>
`SC8-e28-AC2` -- imported from its packaged layout, the writer dry-runs the newest real partition against the live table.

<criterion id="SC8-e28-AC3" cell_refs="SC-e-28"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e28_tf.py</invocation><expect>SC-E28-TF ok=True</expect></criterion>
`SC8-e28-AC3` -- the declared root initialises without a backend (plugin cache under the home directory, no registry egress) and validates.

<expected_criteria>SC8-e28-AC1,SC8-e28-AC2,SC8-e28-AC3</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`PYTEST-BAD rc=4`, no tests folder); AC2 FAIL as expected (no script);
AC3 FAIL as expected (`no root infra/aws/terraform/mdpf-secclass/sector-writer`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`,
  uncommitted. The R10 issuer checks are READ-ONLY to you.
- **No apply, no table write, no S3 write, no deploy.** No `terraform apply`/`plan` against the backend, no artifact upload, no
  `aws lambda` call. The dry run reads live inputs only. This cell opens NO change-management entry because it deploys nothing;
  the issuer opens one at the act. No vendor or model call.
- **The contract file is READ-ONLY here** (SC-e-27 is its one writer). A value set you find wrong is a surprise row.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W24-S<k>`), and do not weaken the test.

<paths>
infra/aws/lambda/mdpf-secclass/sector-writer/lambda_function.py
infra/aws/lambda/mdpf-secclass/sector-writer/tests/test_sector_writer.py
infra/aws/terraform/mdpf-secclass/sector-writer/main.tf
infra/aws/terraform/mdpf-secclass/sector-writer/lambda.tf
infra/aws/terraform/mdpf-secclass/sector-writer/iam.tf
infra/aws/terraform/mdpf-secclass/sector-writer/schedule.tf
infra/logic/registry/resources.json
infra/logic/registry/systems.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sector_writer_dry_run.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SECTOR_ROWS_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. The two registry files are for a builder refusal only. Everything else named here you READ and
never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-28`.
<owned_cells>SC-e-28</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e28-AC1, SC8-e28-AC2, SC8-e28-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~24/MDPF_SECCLASS.TO-SC-e28.scheduled-sector-writer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e28-AC1,SC8-e28-AC2,SC8-e28-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the dry-run line, the builder names and addresses used (or registry rows added), the key-resolution rule, the
seed-wins rule, the schedule and why, the `comp-iam service` output, the half request path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): no armed gate names a sector writer. The cell DECLARES one new schedule after the characteristics landing; applied only under the issuer's half.
comp-iam: RUN -- R8 battery (comp-iam gaps): 0 gap lines name etf-classifications or secclass; the role this cell needs does not exist yet, so a zero says nothing about it. The worker runs comp-iam service on its declared root (step 4).
comp-adversary: RUN -- R8 battery; issuer reads 2026-10-07: the characteristics home (etf_positioning_gold.py:91, :474, :1690), the newest file (bbg/2026-10-05/, 114 rows, 107 non-null per field), the FWD-10 root as template, opal_naming name()/address() signatures. BLIND: the key-resolution rate from `security` to table keys (the dry run measures it); the landing times (step 4 measures them).
risk floor: WORLD -- declares a new role, schedule and S3 address and plans a live-table write (R8 table).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 @87ad6d2e4c (FWD-12, ADDENDUM v0.5 C-SECTOR/C-WRITER/C-NOCHAR, v0.10); DECOMP_R8 @495efa3c32.

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-07 ~08:4xZ) -- Andrew-direct ~08:1xZ: LGIC naming and registration for every new resource

Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_081xZ_LGIC_NAMING_DILIGENCE_AND_REGISTRATION_FOR_EVERY_NEW_RESOURCE.md`
(origin 4cea56993a), relayed by 1.0.0_SA_CTO~DELL1 msg 49. Verbatim: "everyone is being very diligence with LGIC_NAMING for any new
resource creation, everything should be registered as well".

1. Every resource the root declares takes its name from `lib/opal_naming.py name()` and every S3 address from `address()`.
2. Every declared resource name gets a row in `infra/logic/registry/resources.json` (already in your `<paths>`). It lands IN THE SAME COMMIT
   as the Terraform that declares it, not only on a builder refusal; the row's `evidence` names the `.tf` file and line.
3. Nothing is created by a CLI or SDK call. No gate sees such a create, so you make none. The issuer's apply runs through `safe-apply` only.
4. `SC8-e28-AC3` now also grades point 2. `issuer_check_sc_e28_tf.py` reads every literal `function_name` / `name` / `role_name` on an
   `aws_*` resource (log groups excluded), and prints `ok=True` only when each one has a registry row and at least one name is found.
   The expectation `SC-E28-TF ok=True` is unchanged. Exercised by the issuer: positive control (a registered name) ok=True, negative
   control (one unregistered name) ok=False `missing=['not-a-registered-name']`, base FAIL as expected (no root).
Gate limb: none graded this modification (LIMB 6 fires on new orders only; no `<placeholders>`).

## AMENDMENT 2 (2.0.0_SA_COO~M1, 2026-10-07 ~09:4xZ) -- rulings on BLOCKING rows W24-S5 (no provider cache) and W24-S8 (redundant rows)

- **W24-S8, ruled.** Amendment 1 point 2 asked for a `resources.json` row per name; the registry's own validator refuses a row for a
  name that already resolves its system from its own tokens (the same conflict as NFRA_CTLPLN row W10-S1). "Registered" is now the
  registry's rule: a declared name grades `CONFORMANT` through `lib/opal_naming.py grade()` under its `NAMING_SCHEMA.json tf_type_map`
  node type, OR carries a `resources.json` row where `grade()` cannot resolve it. Add no redundant row.
- **W24-S5, ruled.** dell1 holds no provider cache and no seat may download one (row S49). `terraform validate` leaves AC3; it runs in
  the issuer's `safe-apply` plan when the root is applied. AC3 now checks `terraform fmt -check -recursive` plus the registered rule.
- `SC8-e28-AC3`'s invocation and expectation are unchanged (`issuer_check_sc_e28_tf.py` -> `SC-E28-TF ok=True`); the script changed.
  Its output no longer prints "The configuration is valid". Issuer controls: base FAIL (no root); worker root @4da617c979 `ok=True
  fmt=clean names=5 registered=5`; a fixture with one unresolvable name `ok=False unregistered=['not-a-registered-name=UNRESOLVED...']`.
- Then re-run AC3, update the proof instance, and flip. Gate limb: none graded this modification (no new order; no `<placeholders>`).

