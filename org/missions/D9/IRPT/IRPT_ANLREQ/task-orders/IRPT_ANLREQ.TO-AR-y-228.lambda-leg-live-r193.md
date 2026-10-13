# TO IRPT_ANLREQ.TO-AR-y-228.lambda-leg-live-r193 -- the Lambda release that moves only template_reader.py, built against the package that is live now

<to_id>IRPT_ANLREQ.TO-AR-y-228</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~72</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-228` (`decompositions/IRPT_ANLREQ_DECOMP_R21R_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~72`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-72` (branch `wk-IRPT_ANLREQ-72`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~72 <0.9.0_WK_IRPT_ANLREQ~72@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W72-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only `get-function` of step 1 and the download of its `Code.Location` zip and one `list-object-versions` of its key; no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).
- **THE BUILD GUARD (a past incident: row D2-S69):** every build in this cell is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1. At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`.

### THE CELL (`AR-y-228`, inlined) -- THE LAMBDA LEG OF THE r19.3 RELEASE, REBUILT ON THE LIVE PACKAGE. Nothing is uploaded, deployed or applied.

*Live now (release 20, 2026-10-13): `irpt-ycharts-generate` at CodeSha256 `hpNfkhLtLRl0e9TFL+Vdr5kilZ1W8bN3GKMhlzmVXgg=`, built at base `4067c2dd5b` with its release diff `irpt-ycharts-generate.release.diff` (git hash-object `3b85d26d1f`) -- the diff is in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~64/r20/` or `~61/r20/` (list both; the release-20 pair `deliverables/2.0.0_SA_COO~Y2/release20/NEVER_WIDEN_PAIR_ANLREQ_STATUS_RULE_ALL_EIGHT.md` section 2 names the row). The release must move `intake/template_reader.py` (to the trunk head's r19.3) and nothing else; its map pin for `template_reader.py` moves to the head blob.*

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~56/r19/LAMBDA_LEG_LIVE_REBASE.json` (the method of the release-19 rebase), the release-20 group record that built ycharts-generate (`~64/r20/STATUS_RULE_REBASE_GROUP_B.json` or `~61/r20/STATUS_RULE_REBASE_GROUP_A.json`: find the one naming `irpt-ycharts-generate`; its `build_command` and the worktree procedure), and the map entry `irpt-ycharts-generate` in `infra/aws/lambda/ci/lambda-source-map.json` at HEAD (its `staged_from` rows and the pins for the reader members).

1. **Read the live package.** `.tools/aws lambda get-function --function-name irpt-ycharts-generate --query Configuration.CodeSha256 --output text` (use the `.tools/aws` shim). Expected `hpNfkhLtLRl0e9TFL+Vdr5kilZ1W8bN3GKMhlzmVXgg=`; anything else: STOP, record what it printed, file a BLOCKING row and do nothing more (someone moved it). Then `Code.Location`, download the zip into a NEW EMPTY folder under your `.scratch/r21/` (write the URL to a file and read it from Python run with `-I`), check its sha256 base64 equals the CodeSha256, and take `member_manifest` = member name -> sha256 for every file member. Also `list-object-versions` for `investor-reporting/irpt-ycharts-generate.zip` in `opal-313476888478-lambda-artifacts` (prefix exact; print the latest VersionId and the count as the denominator). Write the latest VersionId in the record: it is the rollback target.
2. **The no-move control.** Rebuild the live package: a throwaway worktree OUTSIDE the product tree DETACHED at `4067c2dd5b` (guard count printed), the release-20 diff applied uncommitted (the same `git apply` the release-20 worker used), `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate`. Copy the zip at once (the script writes one fixed temp path). Its CodeSha256 must equal the live one and `differs_from_live` must be `[]`. If it does not, name the differing members and STOP the cell with a BLOCKING row (the base is then not what runs).
3. **Cut the release map patch.** In a second throwaway worktree at the same base with the same release-20 diff applied, move ONLY the pin of `intake/template_reader.py` in the `irpt-ycharts-generate` entry to a commit whose blob is the trunk head's `template_reader.py` (a full 40-hex commit; confirm its blob sha256 equals HEAD's). Save `git diff` of `infra/aws/lambda/ci/lambda-source-map.json` only as `r21/RELEASE_MAP_PATCH_R3.diff`; print `git hash-object` of it. The trunk map is NOT edited.
4. **Build the release.** In that worktree, `BUILD_ONLY=1` the same command. Copy the zip. Record `package_sha256`, bytes, `code_sha256_base64` (the digest the script prints) and `member_manifest`.
5. **Compare.** `differ_from_live` = members whose sha256 differ between the release build and the live package: EXPECTED EXACTLY `["template_reader.py"]` and its sha256 equals the head blob's. Also members only in one side (expected none), member counts.
6. **Write `r21/LAMBDA_LEG_R193.json`:** `live_read` {`code_sha256`, `read_at`, `member_count`, `member_manifest`, `s3_latest_version_id`, `s3_version_count`}, `guard_counts` {`base_commit`, `build_only_mentions`}, `holds_only_control` {`code_sha256`, `differs_from_live`}, `patch` {`path`, `git_hash_object`, `touches`, `reader_pin_commit`}, `release_build` {`package_sha256`, `package_bytes`, `code_sha256_base64`, `member_manifest`, `build_log`, `zip_copy`}, `differ_from_live`, `only_in_live`, `only_in_release`, `worktrees`, `claim`, `not_read`.
7. **In your report:** the live read in one line, the control (equal or not), the single differing member, the expected CodeSha256 of the release.

### ACCEPTANCE

<criterion id="AR228-y-AC1" cell_refs="AR-y-228"><invocation>python C:/dev/wk-irpt-anlreq-72/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y228-lambda --root C:/dev/wk-irpt-anlreq-72</invocation><expect>Y228-LAMBDA-OK</expect></criterion>
`AR228-y-AC1`: the record carries the live manifest read now, a no-move control that reproduces the live CodeSha256 and differs in no member, and a release build that differs from the live package in exactly `template_reader.py`, with the expected CodeSha256.

<criterion id="AR228-y-AC2J" cell_refs="AR-y-228" judgment="true"/>
`AR228-y-AC2J` (judgment, graded at L9, never by you): the live package was read from AWS in this run and not taken from a record, the guard count was printed before each build, both builds were `BUILD_ONLY` at the base, and nothing was uploaded or applied.

<expected_criteria>AR228-y-AC1 AR228-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~72/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else. The only AWS calls are the `get-function` and `list-object-versions` reads of step 1 and the download of the `Code.Location` zip.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21R_Y.md</decomp_doc>
<owned_cells>AR-y-228</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~72/IRPT_ANLREQ.TO-AR-y-228.lambda-leg-live-r193.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-228`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR228-y-AC1,AR228-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read-only get-function, one list-object-versions and a download of the live zip; local BUILD_ONLY builds in throwaway worktrees outside the product tree; nothing is uploaded, deployed, applied or called with a write.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- the only AWS calls are two read-only calls on one function and one key with the shim identity the seat already holds; no policy changes.
comp-adversary: RUN -- by reading rows D2-S66 and D2-S69 (a package that changed under a census; a build at a commit older than the guard uploaded) against the cell; the lens: a base taken from a record, a build without the guard, a release compared with another build and not with the live package. The order requires the live read in this run, the guard count before each build, and a no-move control that must reproduce the live CodeSha256. NOT seen: the Lambda's configuration and environment.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-21 analysis section 3 item 4 as workstream `YR` round 14. Base: `AR228-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
