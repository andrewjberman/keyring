# TO-IB-yr-761 -- irpt-ycharts-generate installs the custody factory (release 6, part 1)

<to_id>IRPT_BCKEND.TO-IB-yr-761</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~223</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-761` (`decompositions/IRPT_BCKEND_DECOMP_R76_Y.md`)

---

## WORKER FACE

### Read first

- The port contract: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release6_custody/CUSTODY_PORT_CONTRACT.md`.
- ~P2's read set and staging list: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~190/IB94-1_custody_ports_read_set.json`.
- ~M2's port: `infra/aws/lambda/investor-reporting/holdings/holdings_publication_port.py`.
- ~M2's read set: the last paragraph of `org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUND34_M_L8_COMPILE.md`.

The "Performance client statement" is the custody report (code id `CUSTODY_REPORT`).

### THE CELL

Today, `infra/aws/lambda/investor-reporting/reports/generate_installed.py` (`RoutedSubmissionService.submit`, line ~172) raises
`CustodyFactoryRequired("CUSTODY_FACTORY_REQUIRED")` for any body without `input_id`. **Install the custody factory in its place.**

1. **Compose the reader once per request,** from the ports `compose_ports` already builds (clients: `dynamodb`, `table`, `s3`, `sqs`):
   - `store = CustodyBindingStore(clients["dynamodb"], requests_table)` (`_scope/custody_binding.py`).
   - `ports = build_accepted_custody_ports(selection_store=SelectionStore(clients["dynamodb"], requests_table),
     current_authority=<request-bound (principal, owner) -> (scope, directory)>, get_object=<s3 reader>, admitted_firms=<default>)`
     (`_scope/custody_ports.py`).
     - Build `current_authority` per the recipe at `_scope/custody.py:63-88` (`CustodyAccess._current_selection_owner`); it must
       resolve fresh on every call (row D2-W190-S2).
     - Use the module's `s3_object_reader` for `get_object` if one exists; otherwise a minimal `(bucket, key, version_id) -> bytes`
       over `clients["s3"]`.
     - Keep `admitted_firms` at the module default; do not widen it.
   - `reader = AcceptedCustodyReader(store, publication_for=holdings_publication_for(clients["s3"]), **ports.reader_kwargs())`, with
     `from holdings_publication_port import holdings_publication_for`.
2. **Route.** A body with no `input_id` goes to the custody service. Use `build_accepted_custody_entry(reader, **ports)` from
   `ycharts/generate/custody_submission.py`, OR construct `CustodySubmissionFactory` directly and set its `.boundary` to the installed
   Entry. The factory's `submit` requires `self.boundary`. Pass it exactly the transport ports `compose_ports` provides (`send`,
   `queue_url`, `ingestion_revision`, `destination_revision`, `configuration`, `reporting_policy`, `reporting_destination`,
   `schema_directory`, `clock`, `dynamodb`, `table`, `s3`). The `input_id` branch stays byte-identical in behaviour.
3. **Staging (`infra/aws/lambda/ci/lambda-source-map.json`, row `irpt-ycharts-generate`).**
   - Add or re-pin `staged_from` rows so the package carries every module the path imports. Start from ~P2's `release6_staged` list.
   - Add `holdings/holdings_publication_port.py` (packaged as `holdings_publication_port.py`) and `holdings/publication.py` packaged
     as `holdings_publication.py`. Do NOT replace the existing `publication.py` row (that is the YCharts extract module).
   - Re-pin `generate_installed.py` to your cell commit.
   - Let AC2 and AC3 decide completeness: add rows until both pass, and do not re-pin rows they do not flag.
   - Pins are full 40-char shas and sha256 values are the blob at the pin, in the existing formats. Edit byte-preserving.
4. **Layer and grants (`infra/aws/terraform/investor-reporting/ycharts/generate.tf`).**
   - Add the AWS-managed layer `arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python312:16` beside `irpt_common` at line ~326
     (estate precedent: 49f/cot/inf-value-parity). It disarms row D2-W190-S3, per row D2-S19.
   - Add IAM statements for EXACTLY the two read sets above:
     - ~P2's `opal-data-assets` silver parquet reads by version;
     - ~M2's `opal-data-<firm>` `irpt/<firm>/platinum/holdings/` GetObject/GetObjectVersion.
   - Add Put/Get/GetVersion on `opal-data-irpt` `irpt/<firm>/platinum/custody_reports/*` for the CUSTODY_REPORT family (~M2 msg 2163).
   - Build every ARN the way the neighbouring statements do, from the registry/locals (`local.resident_scopes`, `opal_naming`); a
     hand-typed name is refused at commit (rule 30). Print the final statement list in your report.
   - Do NOT plan or apply terraform; release 6's applier does that.
5. **Test.** Add `infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed_custody.py`. It is offline, with fake
   clients and the module's own seams. It proves:
   - (a) a no-`input_id` body reaches the custody service, not `CUSTODY_FACTORY_REQUIRED`;
   - (b) an `input_id` body still reaches the prospect factory;
   - (c) a reader whose `authorize_snapshot` refuses yields the existing custody refusal, not an admit.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="Y76-1-AC1" cell_refs="IB-yr-761"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed_custody.py</invocation><expect>passed</expect></criterion>

<criterion id="Y76-1-AC2" cell_refs="IB-yr-761"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r73/cochange_closure.py irpt-ycharts-generate</invocation><expect>cochange_closure PASS</expect></criterion>

<criterion id="Y76-1-AC3" cell_refs="IB-yr-761"><invocation>bash org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/y71_ac2.sh</invocation><expect>symbol_closure PASS</expect></criterion>

<expected_criteria>Y76-1-AC1,Y76-1-AC2,Y76-1-AC3</expected_criteria>

- AC1: at least 3 passed and 0 failed.
- AC2: `split=0`.
- AC3: `missing=0`, and its build line still reads `OK: import-closure`.
- Also report the census: `python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD`, with every changed member
  listed. It is informational here; the release pair grades it.

**Issuer's base run at box/dell2 HEAD 7edd214b96:**
- AC1: no file;
- AC2: `split=0`, PASS;
- AC3: `missing=0`, PASS.

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~03:1xZ, on rows D2-W223-S1..S3).**
- **S1 (AC3):** `checks/r71/symbol_closure.py` now treats an ImportFrom inside an `except ImportError` / `ModuleNotFoundError`
  handler as an OPTIONAL fallback, when every ImportFrom in that try's body resolves in the package. ~M2's
  `holdings_publication_port.py:8-11` is that shape: the primary `holdings_publication` resolves. The negative control is a synthetic
  zip in which an unguarded missing import and a guarded one with a failing primary are still MISSING. AC3 is unchanged as written.
- **S2:** `opal-data-assets` is SSE-S3 (AES256, `get-bucket-encryption`), so NO KMS statement is owed. Keep the silver grant at
  the two cottonwood tables, the module's default `admitted_firms`.
- **S3:** `<paths>` now admits `reports/tests/test_generate_installed.py`. Update ONLY
  `test_both_branches_refuse_by_name_with_the_public_code_not_ready`: its custody arm asserted `CustodyFactoryRequired`, which this
  cell deliberately removes. Assert instead that a no-`input_id` body reaches the custody factory (or refuses through the custody
  reader), and keep the prospect arm as it is. Both test files must pass.
- Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

## BOUNDS

- **Grant.** The `<paths>` block. No deploy, no upload (BUILD_ONLY only), no terraform plan or apply, no AWS writes, no downloads or
  installs.
- Do not edit ~P2's or ~M2's modules. If a port cannot be called as its contract says, stop and file a row.
- Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_BCKEND-D2-W223-S<k>`. Re-read the channel, then append only your own block. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~223" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~223@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~223 <0.9.0_WK_IRPT_BCKEND~223@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool; no pre-`git add`; edit byte-preserving; ASCII only; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/reports/generate_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed_custody.py
infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed.py
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/ycharts/generate.tf
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~223/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-761.install-custody-factory.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R76_Y.md</decomp_doc> round 76, workstream ~Y, cell `IB-yr-761`.
<owned_cells>IB-yr-761</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y76-1-AC1, Y76-1-AC2, Y76-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~223/IRPT_BCKEND.TO-IB-yr-761.install-custody-factory.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y76-1-AC1,Y76-1-AC2,Y76-1-AC3` BEFORE the flip to complete. Shape:
`deliverables/0.9.0_WK_IRPT_BCKEND~222/IRPT_BCKEND.TO-IB-yr-731.repin-cochange-closure.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the census lines;
- the staged rows added or re-pinned, with their pins;
- the final IAM statement list and the layer line;
- the diff summary;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one route branch in generate_installed.py, the custody modules it imports (staged rows; ~P2's release6_staged list + ~M2's 2 modules), one layer, the grants from two measured read sets; nothing deploys in this cell.
comp-iam: RUN (by reading) -- the role's live inline policy (16 statements) holds requests GetItem/PutItem and the system-key decrypt; this cell DECLARES new reads (opal-data-assets silver, opal-data-<firm> platinum holdings) and custody_reports Put/Get in TF only; BLIND to the role's 2 other inline policies; applied by release 6, not here.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or authorizer changes; the custody branch is inside the existing submission route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched.
comp-adversary: RUN -- AC1 at base FAILs (no file); its arm (c) is the negative control (a refusing reader never admits); AC2/AC3 PASS at base and guard against a split commit or a missing name introduced by the new rows.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
