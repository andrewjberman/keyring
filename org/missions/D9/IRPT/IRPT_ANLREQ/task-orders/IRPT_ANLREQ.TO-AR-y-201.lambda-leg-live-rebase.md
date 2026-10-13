# TO IRPT_ANLREQ.TO-AR-y-201.lambda-leg-live-rebase -- the Lambda release rebased on the package that is live now, with the four holds re-pinned to the live bytes

<to_id>IRPT_ANLREQ.TO-AR-y-201</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~56</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-201` (`decompositions/IRPT_ANLREQ_DECOMP_R19R5_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~56`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-56` (branch `wk-IRPT_ANLREQ-56`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~56 <0.9.0_WK_IRPT_ANLREQ~56@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W56-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only `get-function` of step 1 and the download of its `Code.Location` zip; no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-201`, inlined) -- REBASE THE LAMBDA RELEASE ON THE PACKAGE THAT IS LIVE NOW. Nothing is uploaded, deployed or applied.

*The release must move the two reader members and nothing else. Its holds must equal what runs today.* ADVI_FIRMBKTS act 4 replaced the live package on 2026-10-12 (ledger `org/critical_paths/change_management/20261012T1340Z_advi-firmbkts-fb-f-11-act4-irpt-leg-20261012_deploy_completion.md`, section "Builds": built from branch `scratch/r4-act4-ycharts-pin` c4ca0c9a99, CodeSha256 `NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM=`).

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r19/RELEASE_BUILD_RECORD.json` (the release build record of AR-y-193: `member_manifest`, `base_commit` 5d8b0390ed, `build_command`, the worktree procedure) and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r19/RELEASE_MAP_PATCH.diff` (the map patch: two reader pin moves plus four added `staged_from` rows for the holds).

1. **Read the live package.** `.tools/aws lambda get-function --function-name irpt-ycharts-generate --query Configuration.CodeSha256 --output text` (a single-resource read; use the `.tools/aws` shim). It MUST print `NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM=`; if it prints anything else, STOP, record what it printed, file a BLOCKING row and do nothing more. Then get `Code.Location`, download the zip into a NEW EMPTY folder under your `.scratch/r19/` (write the URL to a file and read it from Python; Python run with `-I`), check its sha256 base64 equals the CodeSha256, and take `member_manifest` = member name -> sha256 for every file member (expected 104).
2. **Re-find the four holds.** For `acceptance.py`, `submission.py`, `submission_service.py`, `durable_job.py` (paths `infra/aws/lambda/investor-reporting/ycharts/generate/<name>`): find a full 40-hex commit whose blob at that path has sha256 equal to the LIVE member's. Start from `git log -- <path>` and check each blob's sha256 (`git show <commit>:<path>`; with `MSYS_NO_PATHCONV=1` only for a slashed ref). Candidates measured by the issuer, to confirm and not trust: `acceptance.py` 2f7cc7be4210e42220e4f97b91bfc98b5c22c014, `submission_service.py` 2f7cc7be4210e42220e4f97b91bfc98b5c22c014, `durable_job.py` 3acafb3f453033d584e25fcc639c371185f61116, `submission.py` 1eed34a8c065f81f1a84a1638bc88dccafd0e51d. A hold with no equal blob is a BLOCKING row.
3. **Cut the release map patch again.** In a throwaway worktree OUTSIDE the product tree at base `5d8b0390ed` (for example `C:/dev/wk56-release/patch`; detached, as AR-y-193 did): apply the AR-y-193 patch's two reader pin moves (`uploads.py`, `template_reader.py`, the same pins as `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r19/RELEASE_MAP_PATCH.diff`) and add the four `staged_from` rows with YOUR pins from step 2 (each row with its `sha256`). Save the result as `r19/RELEASE_MAP_PATCH_R2.diff` (git diff of `infra/aws/lambda/ci/lambda-source-map.json` only) and print `git hash-object` of it. The trunk map is NOT edited.
4. **Build.** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` in that worktree (AR-y-193's `build_command`; read the BUILD_ONLY branch again: it exits before any aws call). Copy the zip at once (the script writes one fixed temp path). Record `package_sha256`, bytes, and `member_manifest`.
5. **Holds-only control.** A second throwaway worktree at `5d8b0390ed` with ONLY the four hold rows (no reader moves), built the same way. Record `live_equivalent_differs_from_live` = the members whose sha256 differ from the live manifest: expected `[]`. If it is not empty, those members are a finding: name each with the commit that would hold it, do NOT widen.
6. **Compare.** `differ_from_live` = members whose sha256 differ between the release build and the live package: expected EXACTLY `template_reader.py` and `uploads.py` (their sha256 should equal AR-y-193's `83ab9b45...` and `176682cb...`). Also record members only in one side (expected none).
7. **Write `r19/LAMBDA_LEG_LIVE_REBASE.json`:** `live_read` (`code_sha256`, `read_at`, `member_count`, `member_manifest`), `hold_pins` (a list of objects: `member`, `pin`, `blob_sha256`, `equals_live` true), `patch` (`path`, `git_hash_object`, `touches`), `release_build` (`package_sha256`, `package_sha256_build_only_base64`, `package_bytes`, `member_manifest`, `build_log`, `zip_copy`), `live_equivalent_differs_from_live`, `differ_from_live`, `only_in_live`, `only_in_release`, `worktrees`, `claim`, `not_read`.
8. **In your report:** the live read in one line, the four pins, the two differing members, whether the holds-only control was empty.

### ACCEPTANCE

<criterion id="AR201-y-AC1" cell_refs="AR-y-201"><invocation>python C:/dev/wk-irpt-anlreq-56/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y201-live --root C:/dev/wk-irpt-anlreq-56</invocation><expect>Y201-LIVE-OK</expect></criterion>
`AR201-y-AC1`: the record carries the live manifest read now, four hold pins each equal to the live member, the release build, a holds-only control that differs from the live package in no member, and the release differs from the live package in exactly the two reader members.

<criterion id="AR201-y-AC2J" cell_refs="AR-y-201" judgment="true"/>
`AR201-y-AC2J` (judgment, graded at L9, never by you): the live package was read from AWS in this run and not taken from a record, each hold pin was confirmed by the blob's bytes, both builds were BUILD_ONLY from the base commit, and nothing was uploaded or applied.

<expected_criteria>AR201-y-AC1 AR201-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~56/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R5_Y.md</decomp_doc>
<owned_cells>AR-y-201</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~56/IRPT_ANLREQ.TO-AR-y-201.lambda-leg-live-rebase.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-201`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read-only get-function and a download of the live zip, local BUILD_ONLY builds in throwaway worktrees outside the product tree; nothing is uploaded, deployed, applied or called with a write.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- the only AWS call is one read-only lambda get-function on one function (CodeSha256 and Code.Location) with the shim identity the seat already holds; no policy changes.
comp-adversary: RUN -- by reading the finding (the live package changed under act 4 after the census) against the cell; the lens: a hold pin taken from a record and not from the live bytes, or a build compared with another build and not with the live package. The order requires the live read in this run, the blob bytes for each pin, and a holds-only control that must differ from live in no member. NOT seen: the Lambda's configuration and environment (not read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on this seat's own measurement (row `IRPT_ANLREQ-D2-S66`) as workstream `YR` round 5. Base: `AR201-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
