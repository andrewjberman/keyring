# TO IRPT_ANLREQ.TO-AR-y-339.irpt-status-release-31-build -- BUILD the irpt-status Lambda package that serves the new commentary-pdf route, from the merged tree (BUILD ONLY: nothing uploaded or released)

<to_id>IRPT_ANLREQ.TO-AR-y-339</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~145</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZY</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-339` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-331` (merged `a1015b40f9`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~145`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-145` (branch `wk-IRPT_ANLREQ-145`), provisioned by the issuer. Commit WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~145 <0.9.0_WK_IRPT_ANLREQ~145@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W145-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke, no AWS call. Scratch outside the product tree.

### THE CELL (`AR-y-339`, inlined)

*The new served route `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/commentary-pdf` (`AR-y-331`, merged `a1015b40f9`) is declared in `ops/` (`entry.py`, `owned_report.py`, `pdf_link.py`) and `reports/status_installed.py`. The route is served by the `irpt-status` Lambda (the source map entry `functions.irpt-status` in `infra/aws/lambda/ci/lambda-source-map.json`, `source_dir` `infra/aws/lambda/investor-reporting/ops`), so the ticket page can open the commentary PDF only after that package is rebuilt and released. This cell is the BUILD of that package from the merged tree, the way `AR-y-320` built the ticket service package (read its record first: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~130/r40/OPAL_TICKET_API_BUILD.json`, its `artifact.build_command`, `guard_counts`, `no_move_control`, `delta_vs_live`, `rollback`, `terraform_note`). Nothing is uploaded, applied, invoked or deployed.*

**Release input (fixed):** the commit `c4c2afe896` on `box/dell2` (print its full 40-hex with `git rev-parse c4c2afe896` and use that). The live package is read READ-ONLY (`.tools/aws lambda get-function` on `irpt-status`: `Configuration.CodeSha256`, `LastModified`, `CodeSize`, `Code.Location`; download the live zip with the presigned URL and take its sha256 and member manifest), exactly as `AR-y-320` read the ticket service.

1. **Read first:** the `AR-y-320` record above; the `irpt-status` entry of `infra/aws/lambda/ci/lambda-source-map.json` (its `files`, its `staged_from` rows with their pins and sha256, and the pipeline name the CI script takes); `infra/aws/lambda/ci/build-and-upload.sh` (its `BUILD_ONLY` guard); and the Terraform that declares `irpt-status` (`infra/aws/terraform/` -- find it by the function name; read only).
2. **Build (BUILD ONLY):** create a clean release worktree OUTSIDE the repository at the pin (`git -c core.longpaths=true worktree add --detach C:/dev/irpt-release-r31/wt-status-c4c2afe896 <full sha>`; `git status` clean; remove it when done), print `git show <pin>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY` before the build (it must equal the count at the base the live package was built from, as `AR-y-320` printed), and run the CI script with `TMPDIR=C:/dev/irpt-release-r31/tmp-status BUILD_ONLY=1 MSYS_NO_PATHCONV=1 bash infra/aws/lambda/ci/build-and-upload.sh <pipeline> irpt-status` (the pipeline name from the map). Build TWICE and compare: the two zips must be identical by member name and sha256, and the `CodeSha256` (base64) must be equal. Stage the zip as `C:/dev/irpt-release-r31/irpt-status-r31.zip` with its sha256 and `CodeSha256`. No `aws s3 cp`, no upload (BUILD_ONLY is the guard; say it).
3. **The delta against the live package (member by member):** list `unchanged`, `differing`, `only_in_release`, `only_in_live` with names. EXPECT, and state whether it holds: the differing members are within `entry.py`, `owned_report.py`, `pdf_link.py`, `status_installed.py` and any `staged_from` or listed member the merged cells changed (the commentary id helper stays local to `owned_report.py`; no new member). ANY other differing, added or removed member is a surprise row naming it, with the commit that explains it. Include the NO-MOVE CONTROL of `AR-y-320`: build the live package's own source commit (read it from the live package's last record) and show it reproduces the live `CodeSha256`; if you cannot find that commit, say so and print what you could not reproduce.
4. **Tests:** from the release worktree run, ONE PROCESS PER FILE where the neighbours need it, `ops/tests/test_commentary_pdf_route.py`, `ops/tests/test_pdf_link.py`, `reports/tests/test_status_installed.py`, `_authz/tests/test_svc_custody_statement.py`, `_authz/tests/test_unguarded_census.py` and `_contracts/tests/test_seam_paired.py`; the `_contracts` suite has failures at the base (the baseline set of `AR-y-331`'s record `r41/baseline_failures.json`): explain any failure by that baseline, and a failing name NOT in the baseline is a surprise row.
5. **Terraform note (READ ONLY):** say which Terraform resource releases this package (the module and the artifact key), whether the S3 object version is pinned in HCL (as `s3_object_version` for the ticket service), and what a scoped plan would change; run NO plan.
6. **Write `r41/IRPT_STATUS_R31_BUILD.json`:** `artifact` {path, bytes, sha256, code_sha256_base64, member_count}, `release_input`, `guard_counts`, `two_builds`, `live_read` {read_at, CodeSha256, LastModified, CodeSize, sha256 of the downloaded zip}, `no_move_control`, `delta_vs_live`, `expected_delta_holds`, `tests`, `terraform_note`, `rollback` {s3_bucket, s3_key, s3_version_id of the live object, read-only}, `claim`, `not_read`.
7. **Write the three checker scripts** named in ACCEPTANCE. In your report: the artifact `CodeSha256`, the delta, the test counts, the surprise rows.


### ACCEPTANCE

<criterion id="AR339-y-AC1" cell_refs="AR-y-339"><invocation>python C:/dev/wk-irpt-anlreq-145/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~145/build_check.py</invocation><expect>^BUILD-OK </expect></criterion>
`AR339-y-AC1`: you write `build_check.py`: it prints `BUILD-OK <members> members, builds identical, CodeSha256 <8 chars>, delta <d> differing` only when the staged zip's sha256 and base64 `CodeSha256` equal the record's, the two builds agree member by member, re-extracting the zip and the downloaded live zip reproduces the record's delta lists exactly, and the differing set is a subset of the expected names of step 3 plus any member explained by a surprise row; otherwise `BUILD-BAD <why>` and exit 1.

<criterion id="AR339-y-AC2" cell_refs="AR-y-339"><invocation>python C:/dev/wk-irpt-anlreq-145/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~145/route_check.py</invocation><expect>^ROUTE-OK </expect></criterion>
`AR339-y-AC2`: you write `route_check.py`: it extracts the staged zip and prints `ROUTE-OK commentary-pdf declared in <n> tables, signer family present` only when the extracted `entry.py` declares the route `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/commentary-pdf` mapped to `analysis-request-commentary-pdf`, the extracted `status_installed.py` carries the same route key, the extracted `pdf_link.py` `FAMILIES` contains `YCHARTS_OPAL_REPORT` and the extracted live zip's does NOT, and the extracted `analysis-request-pdf` route is unchanged against the live zip; otherwise `ROUTE-BAD <why>` and exit 1.

<criterion id="AR339-y-AC3" cell_refs="AR-y-339"><invocation>python C:/dev/wk-irpt-anlreq-145/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~145/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR339-y-AC3` (a third check, with a reason: the cell is BUILD ONLY and a build that touched the repository or the cloud is a release nobody signed): you write `scope_check.py`: it prints `SCOPE-OK` only when `git diff --name-only <base> HEAD` (`<base>` = the parent of your first commit, printed) lists only paths under `org/missions/D9/IRPT/IRPT_ANLREQ/`, `git status --porcelain` of the product tree shows nothing untracked or modified under `infra/`, no `aws` write call appears in your shell history for this order (state how you checked), and the staged artifacts live under `C:/dev/irpt-release-r31/`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR339-y-AC4J" cell_refs="AR-y-339" judgment="true"/>
`AR339-y-AC4J` (judgment, graded at L9, never by you): the irpt-status package carries exactly the merged route, signer and table changes on top of the live package, the existing report PDF route is unchanged, and nothing was uploaded or released.

<expected_criteria>AR339-y-AC1 AR339-y-AC2 AR339-y-AC3 AR339-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~145/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>

org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-339</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~145/IRPT_ANLREQ.TO-AR-y-339.irpt-status-release-31-build.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-339`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR339-y-AC1,AR339-y-AC2,AR339-y-AC3,AR339-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a BUILD ONLY order: a local zip outside the repository and read-only describe/get calls on the live function; nothing is uploaded or released.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; any route this cell adds is source only and is served only after a later signed release. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the build record of AR-y-320 and the merged route cell against the build; the lens: a member that no merged cell changed, an upload reachable from the build command, the report PDF route altered, a live read that mutates, the source map edited. The cell requires BUILD_ONLY, a delta equal to the expectation, two identical builds and the route and signer present only in the release. NOT seen (blind): the live system and the deployed bytes; denominator: 1 live package, 4 expected differing members, 3 checkers.
</preflight>


---

## RECORD FACE

- Cut on the merge of `AR-y-331` (`a1015b40f9`) and the single-release plan (CTO msgs 7767, 7777). Workstream `ZY` of round 40. Base: `AR339-y-AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- Whether the Lambda leg is released with the resident is the issuer's decision at the pair; this cell only builds it. The portal reader (`AR-y-332`) works live only after both the route and the resident are released.
