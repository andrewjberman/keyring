# TO-AR-y-21 -- the release-1 packet: staged rows carry AR-y-11 and the contract that admits it

<to_id>IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~8</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `AR-y-21` (`decompositions/IRPT_ANLREQ_DECOMP_R2.md`)

---

## WORKER FACE

### THE CELL (AR-y-21) -- COMPLETE: drained @3895b80dae, proof VALID by 0.9.0_WK_IRPT_ANLREQ~2; recorded, not re-run

`AR-y-11` (drained @3ad7526e06) taught the analysis submission to carry `ticket_id` and taught the published request contract to admit it.
Two served functions still package the OLD bytes of those files through `infra/aws/lambda/ci/lambda-source-map.json` `staged_from` rows. **Re-pin
exactly three rows to a pin whose blob equals HEAD's**:

| function | `repo_path` | today's pin |
|---|---|---|
| `irpt-status` | `infra/aws/lambda/investor-reporting/ycharts/generate/submission.py` | `80a79a7462` |
| `irpt-status` | `infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py` | `80a79a7462` |
| `irpt-ycharts-generate` | `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json` | `3f29017cfc` |

- Each new `pin` is the full 40-char sha of a commit whose blob of that path equals HEAD's: the last commit touching it.
  `git log -1 --format=%H -- <path>` gives it.
- Each `sha256` is the hex sha256 of that blob, in the existing format.
- Change nothing else in those rows, and no other row. Edit the JSON byte-preserving: keep its indentation and line endings, and replace
  only the two values per row.
- If AC2 or AC3 then fails because a commit now ships split or a name is missing, STOP and file a row. Do not re-pin further rows to
  chase it.
- Report `python infra/aws/lambda/ci/release-census.py irpt-status --pin HEAD` and the same for `irpt-ycharts-generate`, with every changed
  member listed. This is informational; the release pair grades it.

### AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~07:5xZ): this order now carries cell `AR-y-22`

On CTO round-1 ADDENDUM 1 @64e9e6157d (msg 2813) and row `D2-S6`; decomposition `IRPT_ANLREQ_DECOMP_R2.md` AMENDMENT 2. A re-cut into the
round's one ~Y issuance modifies this order and adds no file (`to-pipeline-gate`, one issuer per round). The criteria below are AR-y-22's.
Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

#### THE CELL NOW (AR-y-22)

The ticket page opens each package file through IRPT under the viewer's own scope. `irpt-status` already serves the report's PDF that
way: operation `analysis-request-pdf`, wired at `infra/aws/lambda/investor-reporting/ops/entry.py:198-204`, with
`OwnedAnalysisReader.pdf` at `ops/owned_report.py:153`. It serves nothing for the advisor's ORIGINAL upload. **Add that reader, on the
same pattern.**

1. **The method.** Add `OwnedAnalysisReader.original(principal, request_id, *, signer, data_firm=None)` in `ops/owned_report.py`.
   - Re-authorize exactly as `pdf` does (through the owned record read, with the final re-reads), then release one Opal-signed link to
     the request's original upload.
   - Resolve the original the way `ops/prospect_dates.py:295-299` resolves it: `ORIGINAL_HOLDINGS` for the template lane, `ORIGINAL_CSV`
     for the CSV lane, under the original owner binding. Do not invent a new lookup.
   - Answer with the link, the artifact's sha256 and byte length (the `pdf` response's shape), and no bytes.
   - Refusals, each by name:
     - a custody-lane request (no prospect upload): `ANALYSIS_ORIGINAL_NOT_APPLICABLE`, NOT_FOUND class (I5', the "No original file"
       case);
     - an absent or unbound original: `ANALYSIS_ORIGINAL_NOT_RETAINED`;
     - a viewer without the record: the existing owned-read refusal.
2. **The route.** In `ops/entry.py`, add operation `analysis-request-original`, mapped from
   `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/original`. Register it in all four places the pdf operation appears:
   `routes`, `operations`, `owner_read_modes` (`OWNED_RECORD`) and `record_id_parameters` (`requestId`). Map its refusal classes in `reasons`
   the way the pdf ones are.
3. **The API.** Add the same route to `docs/contracts/investor-reporting/v1/routes.json`, the carrier that
   `infra/aws/terraform/investor-reporting/api/routes.tf` reads, handler `irpt-status`. Copy the pdf route's entry shape exactly.
4. **IAM, only if the read needs it.** `irpt-status`'s role is declared in `infra/aws/terraform/investor-reporting/ops/iam.tf:85`, and its
   family list already names the original-holdings family. If the CSV lane's `ORIGINAL_CSV` (`state/prospect_inputs`) is also listed there,
   change nothing. If a family the reader needs is missing, STOP and file a row; do not add a grant here.
5. **Test.** Add `infra/aws/lambda/investor-reporting/ops/tests/test_original_reader.py`, offline, in the world/fixture style of
   `ops/tests/test_owned_report.py`. It proves:
   - (a) the owner of a template-lane request gets a signed link whose sha256 equals the retained original's;
   - (b) a viewer at ANOTHER firm is refused (the CTO's named test);
   - (c) a custody-lane request refuses `ANALYSIS_ORIGINAL_NOT_APPLICABLE`;
   - (d) a request whose original is absent refuses `ANALYSIS_ORIGINAL_NOT_RETAINED`.

### AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~08:3xZ, on your rows `D2-W3-S3` and `D2-W3-S1`)

1. **S3:** `<owned_cells>` is now `AR-y-22` only. AR-y-21's completion stands in worker ~2's own proof instance.
2. **S1 (ARMED):** `ops/pdf_link.py` is in `<paths>`. Make `PdfSigner.sign(firm, storage_key, sha256, family="ORIGINAL_VENDOR_PDF")` admit EXACTLY three
   families: `ORIGINAL_VENDOR_PDF` (the default, so the PDF route's behaviour is byte-identical), `ORIGINAL_HOLDINGS` and `ORIGINAL_CSV`.
   - The binding stays the registry's: the key must equal `reporting_destination(firm, family, artifact, sha)`, the existing
     DESTINATION check.
   - Any other family refuses `PDF_LINK_FAMILY`.
   - Derive each family's key shape from the registry's (table, extension) for that family; never hand-type a table name.
   - `OwnedAnalysisReader.original` passes the resolved family.
3. **Test arm (e)** in `test_original_reader.py`: the REAL `PdfSigner` (with `client_factory` returning a stub S3 whose `generate_presigned_url`
   echoes the bucket/key) signs a template-lane original. It refuses a key whose family is not one of the three. The vendor-PDF key still
   signs as before.
4. The criteria stay as written; AC1 now has at least 16 passed. Then re-validate the proof instance, mark rows S1 and S3 disposed (one line
   each), and flip `<status>` to complete.

Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### AMENDMENT 3 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~08:3xZ): AR-y-22's reader must SHIP -- two more staged rows for `irpt-status`

AR-y-22 drained @75650bef27 (worker ~3's proof VALID; that cell is complete). But `irpt-status` stages `ops/entry.py` and `ops/owned_report.py`
at `80a79a7462` (`lambda-source-map.json`), so the built zip does not carry the new route or reader. The issuer's census at HEAD lists only
`acceptance.py`, `submission.py` and `pdf_link.py` as changed. `pdf_link.py` is unpinned, from `source_dir`.

**The cell now (AR-y-21, re-opened):** re-pin EXACTLY these two `irpt-status` rows to the last commit touching each path, with the sha256 of that
blob, exactly as AR-y-21's first three rows were re-pinned (pin and sha256 only, byte-preserving):
`infra/aws/lambda/investor-reporting/ops/entry.py` and `infra/aws/lambda/investor-reporting/ops/owned_report.py`. Touch no other row.
The check `checks/r2/ar21_cells.py` now lists 5 rows (its AMENDMENT 3); base AC1 FAIL, 2 of 5 lag. Report the `irpt-status` census after.
Proof instance: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~4/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`,
criteria AR21-y-AC1..3, `to_id` the FULL id. Rows are `IRPT_ANLREQ-D2-W4-S<k>`. Your paths are the <paths> block (the source map is in it).
Commit as `0.9.0_WK_IRPT_ANLREQ~4`.

Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### AMENDMENT 4 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~10:4xZ, on row `IRPT_BCKEND-D2-S43` and CTO msg 3140): the installed route table must declare `/original`

`_authz/tests/test_unguarded_census.py` FAILS at HEAD: `GET .../analysis/requests/{requestId}/original` is published and declared by `ops/entry.py`, but
irpt-status runs as an INSTALLED entry whose route table is `reports/status_installed.py` `HISTORY_ROUTES` (`:53-58`), and that table does not name it.
This is now a condition of the release-1 CTO half.

**The cell now:**
1. Add ONE line to `HISTORY_ROUTES`: `"GET /api/scoped/investor-reporting/analysis/requests/{requestId}/original": "analysis-request-original"`, beside
   the `/pdf` line, with a one-line comment naming AR-y-22.
2. Re-pin `irpt-status`'s staged row for `infra/aws/lambda/investor-reporting/reports/status_installed.py` (today `80a79a7462`) to your commit, with the
   blob sha256 (pin and sha256 only, byte-preserving). Key the edit on function AND repo_path, and touch no other row.

`checks/r2/ar21_cells.py` lists 6 rows (its AMENDMENT 4). AC2 (co-change) is replaced by AC4, the census test: base FAIL, 1 of 22. Report the
`irpt-status` census and the new built sha (`BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-status`).
Proof instance: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~5/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`,
criteria AR21-y-AC1, AR21-y-AC4, AR21-y-AC3. Rows are `IRPT_ANLREQ-D2-W5-S<k>`. Commit as `0.9.0_WK_IRPT_ANLREQ~5`.

Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### AMENDMENT 5 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~12:1xZ, on CTO msg 3245 and ~G2 msg 3241, row IRPT_YCDGEN-D2-S20): the research registry row in irpt-status

irpt-status refuses the Opal 49financial report (`RetentionRefused 'invalid retention reference'`, 12:02:18Z), because its packaged
`infra/logic/registry/reporting_policies.json` (pin `80a79a7462`) carries `irpt-ycdgen-research-v1` with firms `[cottonwood]` only. HEAD carries
`[cottonwood, 49financial, inflection]` (YCD-a-7, `23e39f11d7`).

**The cell now:** re-pin EXACTLY ONE row, irpt-status's `infra/logic/registry/reporting_policies.json`, to the last commit touching that path
(`git log -1 --format=%H -- infra/logic/registry/reporting_policies.json`), with that blob's sha256 (pin and sha256 only, byte-preserving; key on function
AND repo_path). Do NOT re-pin `ops/entry.py` or `ops/owned_report.py`: ~P2's worker ~268 changed both after this lane's pins, and that change ships in
IB-pr-405, not here. The check now grades both at this lane's own commits (`HELD`). Base: AC1 FAIL, 1 of 7 lag.
Report the irpt-status census and the BUILD_ONLY sha. Proof instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~6/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`. Rows are
`IRPT_ANLREQ-D2-W6-S<k>`. Commit as `0.9.0_WK_IRPT_ANLREQ~6`.

Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### AMENDMENT 6 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~15:0xZ, CTO ruling AMENDMENT 2 @ CTO_RULING_IRPT_YCDGEN_FWD1_RETENTION_REF_SKEW_20261009.md, msg 3514): the READER registers the research revision

`reports/status_installed.py:114` builds irpt-status's repositories WITHOUT `additional_policy_revisions`, while the writer passes
`(OPAL_RESEARCH_REVISION,)` (`reports/resident_installed.py:353`; the constant is defined at `:60`). So irpt-status never registers `YCHARTS_OPAL_REPORT`
under `irpt-ycdgen-research-v1` (`reports/composition.py:43-54`), and the Opal 49financial report is refused. All 13 stored refs fit (laptop walk).

**The cell now:**
1. In `reports/status_installed.py`, import `OPAL_RESEARCH_REVISION` FROM `resident_installed` (the module already imports `make_authorize` from it; NEVER retype
   the string). Pass `additional_policy_revisions=(OPAL_RESEARCH_REVISION,)` to `build_retained_repositories` at `:114`.
2. Add `infra/aws/lambda/investor-reporting/reports/tests/test_status_installed_revisions.py` (offline, fakes):
   - (a) SET EQUALITY: the revisions irpt-status's composition registers (`stores.artifacts.revisions` / the family->revision map) equal the writer's
     composition's, as built by `resident_installed`'s own call;
   - (b) `YCHARTS_OPAL_REPORT` maps to `OPAL_RESEARCH_REVISION`;
   - (c) NEGATIVE ARM: built WITHOUT the argument (the pre-fix call), the family is absent from the map, so the test discriminates.
3. Re-pin irpt-status's staged row for `reports/status_installed.py` to your commit (pin and sha256 only; key on function AND repo_path). `ar21_cells.py` AC1
   grades it against HEAD. Touch no other row.

Criteria: AC1 (rows), AC5 (the new test; base FAIL, no file), AC3 (symbol closure). Report the irpt-status census, which must read exactly
`status_installed.py` against live rev 3, and the BUILD_ONLY sha. Proof at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~7/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`, criteria
AR21-y-AC1, AR21-y-AC5, AR21-y-AC3. Rows are `IRPT_ANLREQ-D2-W7-S<k>`. Commit as `0.9.0_WK_IRPT_ANLREQ~7`.

Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### AMENDMENT 7 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~15:1xZ, CTO ruling AMENDMENT 3, msg 3548, on your rows `D2-W7-S1` and `D2-W7-S2`)

Route (b). Importing `OPAL_RESEARCH_REVISION` from `resident_installed` FAILS symbol closure, because irpt-status stages that module at `80a79a7462`, before the
constant existed. Re-pinning it would ride a +147/-7 backlog. So:
1. **`reports/status_installed.py` DERIVES the revision from the PACKAGED registry.** Use the reporting policy whose `families` hold `YCHARTS_OPAL_REPORT`,
   found through the same `reporting_policy` / registry accessors the module already uses. It FAILS CLOSED: zero or several matching policies mean NO
   extra revision, plus ONE logged error line (ASCII, `ERROR:` prefix). Never a default. Remove the `resident_installed` import of the constant;
   `make_authorize` stays as it was. Never type the revision string.
2. **`reports/tests/test_status_installed_revisions.py`:**
   - (a) keeps SET EQUALITY with the writer: the in-tree test imports `resident_installed.OPAL_RESEARCH_REVISION` at HEAD (the TEST may; the packaged code
     may not);
   - (b) the family maps to it;
   - (c) the negative arm;
   - (d) NEW: a registry with zero matching policies, and another with two, each yield NO extra revision and log the error.
3. **Row S2: `reports/tests/test_status_installed.py` is GRANTED** (added to `<paths>`). Make its fake `active_policy` flip state only for the X10 id
   (`REPORTING_POLICY_ID`) and pass other revisions through unchanged. Its 7 tests must pass.
4. `resident_installed.py` stays at `80a79a7462`. Re-pin ONLY irpt-status's `reports/status_installed.py` row to your final commit.

The criteria are unchanged: AC1, AC5 and AC3 (symbol closure must read missing=0). Also report
`python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/reports/tests/test_status_installed.py` (7 passed). Then re-validate the proof,
run `safe-merge.sh box/dell2` in the worktree, and flip to complete. Mark S1 and S2 disposed.

Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### AMENDMENT 8 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~16:4xZ, rows `IRPT_ANLREQ-D2-S16` and `IRPT_BCKEND-D2-S60`, CTO msg 3677)

Rev 4 shipped split and was rolled back to rev 3 at 16:43Z. `status_installed.py:137` passes `additional_policy_revisions=` to `build_retained_repositories`,
but irpt-status stages `reports/composition.py` at `80a79a7462`, which predates that keyword. The keyword arrived at `f60e6f1d2a`, and `2aa217ec58` also
touched the file. Every call raised TypeError.
1. **Re-pin irpt-status's `reports/composition.py` row** in `infra/aws/lambda/ci/lambda-source-map.json` to HEAD's blob (pin + sha256). Change no source file.
2. **Close what the re-pin needs.** If AC3 then reports a missing name or a NEW signature mismatch in a module composition.py calls, re-pin that module's
   row too (source map only). Name each extra re-pin and why in your report. If closure needs a SOURCE edit, stop and file a row.
3. **AC3 now runs `checks/r2/signature_closure.py`** on each built zip. One pre-existing mismatch is tolerated by name (`served:1006` `profile_reader`,
   row IRPT_BCKEND-D2-S60, owned by 2.0.0_SA_COO~P2). Any other mismatch FAILS. At base, AC3 FAILS on `status_installed:137`.
4. AC1 now also grades the composition.py row. At base, AC1 FAILS with 1 row lagging. AC5 is unchanged.

Rows are `IRPT_ANLREQ-D2-W8-S<k>`. Your deliverables directory is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~8/`. Commit as
`0.9.0_WK_IRPT_ANLREQ~8` (the commit line below, with ~8 in place of ~7). Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### AMENDMENT 9 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~17:1xZ, direct act): the narrower `repository.py` pin

Worker ~8 re-pinned irpt-status `reports/repository.py` to `3fc99be70f`, which rides 6 commits from 4 lanes. Pin `2aa217ec58` closes the same signatures
(issuer read: symbol closure PASS, signature closure 1 mismatch, the tolerated S60 one) and is the pin irpt-export-render already serves. It drops
IB-pr-386 and AR-t-12's two commits (svc-commentary admission), which no served function carries. The row is re-pinned to `2aa217ec58` (sha256 f01fcf549e8e...)
in this commit. The status stays complete. Gate limb that graded this amendment: `to-pipeline-gate.py` GATE (viii) on a modify.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR21-y-AC1" cell_refs="AR-y-21"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/ar21_cells.py . AR21-y-AC1</invocation><expect>AR21-y-AC1 PASS</expect></criterion>

<criterion id="AR21-y-AC5" cell_refs="AR-y-21"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/reports/tests/test_status_installed_revisions.py</invocation><expect>passed</expect></criterion>

<criterion id="AR21-y-AC3" cell_refs="AR-y-21"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/ar21_cells.py . AR21-y-AC3</invocation><expect>AR21-y-AC3 PASS</expect></criterion>

<expected_criteria>AR21-y-AC1,AR21-y-AC5,AR21-y-AC3</expected_criteria>

- AC1: at least 4 passed and 0 failed.
- AC2: base `261 passed, 22 skipped`; no `failed` after the cell.
- AC3: both built zips (irpt-status and irpt-ycharts-generate) still resolve every imported name. If the new code adds a module, it must
  be packaged.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no upload (BUILD_ONLY only, inside AC3), no terraform, no AWS calls.
- Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W3-S<k>`, in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, one `## <id> -- <title>`
  header plus a ```json block per row (the file's existing format). Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Before the issuer drains,** run `bash .tools/safe-merge.sh box/dell2` INSIDE your worktree and resolve any channel conflict there
  (box/dell2's file plus your own row blocks appended whole).
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~7" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~7@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~7 <0.9.0_WK_IRPT_ANLREQ~7@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool (a Windows path); no pre-`git add`; ASCII only; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~2/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/entry.py
infra/aws/lambda/investor-reporting/ops/tests/test_original_reader.py
infra/aws/lambda/investor-reporting/ops/pdf_link.py
docs/contracts/investor-reporting/v1/routes.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~3/
infra/aws/lambda/investor-reporting/reports/status_installed.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~5/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~6/
infra/aws/lambda/investor-reporting/reports/tests/test_status_installed_revisions.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~7/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~8/
infra/aws/lambda/investor-reporting/reports/tests/test_status_installed.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md</decomp_doc> round 2, workstream ~Y, cells `AR-y-21` (complete) and `AR-y-22` (AMENDMENT 2).
<owned_cells>AR-y-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR21-y-AC1, AR21-y-AC5, AR21-y-AC3 (AMENDMENT 6). Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~7/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`, `to_id` the FULL id
`IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows`, validated with `python .tools/proof-of-spec-check.py <instance> AR21-y-AC1,AR21-y-AC5,AR21-y-AC3` BEFORE the flip to complete.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the route entry added;
- the refusal names;
- the IAM family check result;
- the diff summary;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one reader method, one operation in ops/entry.py, one route in the routes.json carrier; the pdf operation is the template; served at the irpt-status release, never here.
comp-iam: RUN (by reading) -- irpt-status's role (ops/iam.tf:85) lists the original-holdings family; the cell adds NO grant and STOPs on a missing family.
comp-routes: RUN -- one new GET route under the existing authorizer, added to routes.json (the API carrier read by api/routes.tf); applied with the irpt-status release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched.
comp-adversary: RUN -- AC1 at base FAILs (no file); arms (b)-(d) are refusals, (b) the CTO's named other-firm test; AC2 base 261 passed/0 failed; AC3 PASS at base.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
