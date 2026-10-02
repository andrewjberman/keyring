# TO IRPT_BCKEND.TO-IB-pr-297 -- E4's repairs: the export packages the Analysis contract, every grant-staging function packages the owner reader, and the receipt downloads through the live route with a signed answer

<to_id>IRPT_BCKEND.TO-IB-pr-297</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 175 (@6621e009c6, msg 104290) on
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/E4_ANALYSIS_EXPORT_READINESS_20261002.md` gaps G1, G2, G4; rows
IRPT_BCKEND-S271 (ARMED) and S272 | **Decomp cell:** `IB-pr-297` (decomposition section 27 addendum note: round 34, one cell; row
IRPT_BCKEND-S267) | **outcome_ref:** FWD-9 (hop 12) | **depends_on:** IB-pr-296 (merged @2a4a9f823f)

---

## WORKER FACE

**The cell.** Three repairs E4 needs, all source and packaging (no deploy). Read the readiness record first.
- **G1.** The export function `irpt-export-render` does not package `AnalysisReport.schema.json`. Its staged contracts are packaged as
  `irpt_contracts/<name>` from `docs/contracts/investor-reporting/v1/`, pinned at `83e8b9577a`, so `submit_installed.py:72` would
  fail an Analysis submit. Stage `AnalysisReport.schema.json` the same way. Re-pin every `irpt-export-render` staged member whose
  blob differs at HEAD.
- **G2 (binds every function, now or later).** `_authz/served.py:1174` imports `report_owner` whenever `IRPT_EVIDENCE_BUCKET` is
  set. Every function that stages `_render_identity/grant.py` (today: `irpt-export-render`, `irpt-performance-adapter`,
  `irpt-ycharts-generate`) must also stage `_render_identity/report_owner.py` (packaged beside `grant.py`) and
  `reports/repository.py`, all three pinned at HEAD.
  - Add `infra/aws/lambda/ci/test_render_ports_packaging.py`, a pytest file of at least 2 tests over the source map, so a function
    that stages `grant.py` without the other two fails the build's tests from now on.
- **G4.** The receipt's `download_route` is `/api/scoped/exports/{export_id}/download` (`export/receipt.py:23`), and no live route
  matches it. The live route `GET /api/scoped/investor-reporting/export/{exportId}/download` is the contract.
  - Point `receipt.py`'s route at the live route.
  - Make `export_download` (`export/entry.py:248-265`, the live `entry.lambda_handler`) return a signed answer in hop 11's shape:
    a SigV4 presigned GET on the regional endpoint, expiring in 300 s, carrying `sha256` and `byte_length` and no storage key.
  - Move the presigner (`export/download.py`, today wired only through `handler.routes`) into the live entry.
  - Hop 11's shape: `git show 5bc562f689:infra/aws/lambda/investor-reporting/ops/pdf_link.py` and its test `ops/tests/test_pdf_link.py`
    at that commit (2.0.0_SA_COO~Y, the X-Amz-Algorithm test).
  - The ExportReceipt schema's `download_route.route` is a free string, so no contract file changes. 2.0.0_SA_COO~D does the
    portal half.

**What exists (read first).** `infra/aws/lambda/ci/lambda-source-map.json` (entries `irpt-export-render`,
`irpt-performance-adapter`, `irpt-ycharts-generate`; the `staged_from` shape `{repo_path, pin, packaged_as, sha256}`, where `sha256` is
the hex sha256 of `git show <pin>:<repo_path>`); `infra/aws/lambda/ci/build-and-upload.sh` (how `staged_from` is packed);
`export/receipt.py`, `export/entry.py`, `export/download.py`, `export/handler.py`; `bundle.contracts_dir` (how the export finds
`irpt_contracts/`).

<criterion id="IB34-1-AC1" cell_refs="IB-pr-297"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r34/p34_1_ac1_packaging.py" .</invocation><expect>IB34-1-AC1 PASS</expect></criterion>
`IB34-1-AC1` -- G1 + G2. The export stages both contracts at HEAD. Every grant-staging function stages `report_owner.py` and
`repository.py` at HEAD, with `report_owner.py` beside `grant.py`. The packaging test passes at least 2. Base: FAIL (AnalysisReport
not staged).

<criterion id="IB34-1-AC2" cell_refs="IB-pr-297"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r34/p34_1_ac2_download_signed_answer.py" .</invocation><expect>IB34-1-AC2 PASS</expect></criterion>
`IB34-1-AC2` -- G4. `receipt.py` names the live route, and `export/tests/test_download_signed_answer.py` passes at least 4 tests,
naming `X-Amz-Algorithm`, `300`, `sha256`, `byte_length` and `lambda_handler`. Base: FAIL (old route).

<criterion id="IB34-1-AC3" cell_refs="IB-pr-297"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r34/p34_1_ac3_suites_unchanged.py" .</invocation><expect>IB34-1-AC3 PASS</expect></criterion>
`IB34-1-AC3` -- `export`, `_contracts` and `_render_identity` fail 0. `_authz` fails only the six known `test_unguarded_census` ids.
Each suite runs in its own process. Base: PASS (a regression guard).

<expected_criteria>IB34-1-AC1,IB34-1-AC2,IB34-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Source map:** the three named functions' entries only. Other functions' rows are other lanes' packets; touch none. Never edit
  `artifact_sha256` or `artifact_s3_key`; a build writes those.
- **AWS:** none. No build, no upload, no deploy.
- **Refusal clause.** An existing test that moves is a defect: stop and file a row, never edit the test. A download answer that
  would expose a storage key, or a URL that is not SigV4, is a row, never shipped.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/test_render_ports_packaging.py
infra/aws/lambda/investor-reporting/export/receipt.py
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/download.py
infra/aws/lambda/investor-reporting/export/tests/test_download_signed_answer.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r34/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/` (all of it), `infra/aws/terraform/investor-reporting/`,
`docs/contracts/investor-reporting/v1/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 addendum note (round 34, workstream ~P), cell `IB-pr-297`.
<owned_cells>IB-pr-297</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB34-1-AC1, IB34-1-AC2, IB34-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-297.export-packaging-and-download.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB34-1-AC1,IB34-1-AC2,IB34-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the re-pinned entries (function, path, old pin to new pin);
- the signed answer's fields;
- any surprise row ids (`IRPT_BCKEND-W101-S<k>`, k >= 13).

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the source map's rows for three functions (the next build of each packs what they stage) and the export's live entry (the download route); AC3 holds four suites; 0 served bytes move in the cell; E4's packet carries the deploy.
comp-iam: DECLARED-NOT-APPLICABLE in the cell -- no role changes; the presigned GET's s3:GetObject on the export artifacts is read by E4's packet against the export role.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; the receipt now names the existing live route (CTO batch 175 G4).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: request-driven entry code and a build map; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB34-1-AC1 base FAIL (AnalysisReport not staged), IB34-1-AC2 base FAIL (receipt names the old route), IB34-1-AC3 base PASS (regression guard: _authz 201 + 6 baseline, export 158, _contracts 185, _render_identity 45), dry-run at the base 2026-10-02 ~15:0xZ after the census literal fix.
lane: the <paths> block IS the grant.
</preflight>
