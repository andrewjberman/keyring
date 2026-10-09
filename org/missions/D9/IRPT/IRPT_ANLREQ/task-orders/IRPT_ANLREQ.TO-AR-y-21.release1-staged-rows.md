# TO-AR-y-21 -- the release-1 packet: staged rows carry AR-y-11 and the contract that admits it

<to_id>IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~3</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
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

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR22-y-AC1" cell_refs="AR-y-22"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ops/tests/test_original_reader.py</invocation><expect>passed</expect></criterion>

<criterion id="AR22-y-AC2" cell_refs="AR-y-22"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ops/tests</invocation><expect>0 failed</expect></criterion>

<criterion id="AR22-y-AC3" cell_refs="AR-y-22"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/ar21_cells.py . AR21-y-AC3</invocation><expect>AR21-y-AC3 PASS</expect></criterion>

<expected_criteria>AR22-y-AC1,AR22-y-AC2,AR22-y-AC3</expected_criteria>

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
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~3" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~3@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~3 <0.9.0_WK_IRPT_ANLREQ~3@opal.agent>" -F <msgfile> -- <paths>`.
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
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md</decomp_doc> round 2, workstream ~Y, cells `AR-y-21` (complete) and `AR-y-22` (AMENDMENT 2).
<owned_cells>AR-y-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR22-y-AC1, AR22-y-AC2, AR22-y-AC3 (AMENDMENT 1; AR-y-21's AR21 ids are recorded VALID in
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~2/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`). New instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~3/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`, `to_id` the FULL id
`IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows`, validated with `python .tools/proof-of-spec-check.py <instance> AR22-y-AC1,AR22-y-AC2,AR22-y-AC3` BEFORE the flip to complete.
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
