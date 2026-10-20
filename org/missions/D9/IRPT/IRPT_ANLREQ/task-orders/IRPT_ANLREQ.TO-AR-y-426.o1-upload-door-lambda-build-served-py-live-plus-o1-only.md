# TO IRPT_ANLREQ.TO-AR-y-426.o1-upload-door-lambda-build-served-py-live-plus-o1-only -- O1 backend release, BUILD ONLY: the irpt-ycharts-generate package (the upload door) rebuilt twice with the ONE map edit that moves served.py to the live bytes plus the AR-y-415 hunks, compared member by member with the live zip: exactly one mover; nothing is uploaded or applied

<to_id>IRPT_ANLREQ.TO-AR-y-426.o1-upload-door-lambda-build-served-py-live-plus-o1-only</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~314</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ85</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-426` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a staff filing is never refused), C-FIRM | **depends_on:** AR-y-415 (merged b8b8452981c); ~P2 review (msg 10992); the portal half ships in the SAME release (AR-y-416)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~314`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-314` (branch `wk-IRPT_ANLREQ-314`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~314 <0.9.0_WK_IRPT_ANLREQ~314@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W314-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-426`, inlined)

*Context.* The upload door is the Lambda `irpt-ycharts-generate` (handler `generate_installed.lambda_handler`, 107 members, live CodeSha256 `kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE=`, LastModified 2026-10-16T02:39:04Z, read by the issuer 2026-10-20). Its package stages `_authz/served.py` as the flat member `served.py` from the function map `infra/aws/lambda/ci/function-map/irpt-ycharts-generate.json` (`staged_from` entry with `repo_path` `infra/aws/lambda/investor-reporting/_authz/served.py`, `packaged_as` `served.py`, `pin` `564e60483858a3cc5c51ffea6aed0f76ff291abe`, `sha256` `30c0eb88ec38a7ddfc410e4ae1c06ee7a9e77661812ba666a45ffcf5552c2475`, which EQUALS the live member). The issuer's read of the live zip is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/o1_release/LIVE_IRPT_YCDGEN_MEMBERS_20261020.json` (`members`: name, size, sha256; `code_sha256`; `zip_sha256`). AR-y-415 (merged `b8b8452981c`) changed `_create_owner`, `_advisor_owner` and added `AdvisorUnprovisioned` in `served.py`; trunk's `served.py` ALSO carries ~DASHBD's `a3058c274c` (the `FORWARD_FUNCTION_ENV` forward port), which must NOT ride this release. So the issuer made a SCRATCH PIN: branch `scratch/o1-served-pin` = commit `720e125d31469ed60b6e698812c7be731bd6d8e8`, whose `served.py` is the live blob plus ONLY the three O1 hunks: blob sha256 `600a934c4b34da1e14ec8b7d4de4a3f69cc55c331257dd90abb525def9929fcd`, 88553 bytes (`git diff 564e604838 720e125d31469ed60b6e698812c7be731bd6d8e8 -- <served.py>` shows 26 insertions and 13 deletions, all O1). The release moves the map pin of that ONE member to this scratch pin. The same trap bit the r34l build (a producer that read a name the held-back layout lacked): a build can pass its delta and import gates and still be wrong, so this order carries a smoke import of the BUILT package.

*What to do.*
1. **Pin and base.** Print `git rev-parse scratch/o1-served-pin` (it must read `720e125d31469ed60b6e698812c7be731bd6d8e8`; any other value: STOP and file a BLOCKING row) and `git show 720e125d31469ed60b6e698812c7be731bd6d8e8:infra/aws/lambda/investor-reporting/_authz/served.py | sha256sum` (it must read `600a934c4b34da1e14ec8b7d4de4a3f69cc55c331257dd90abb525def9929fcd`). Print `git rev-parse HEAD`. Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37` first.
2. **The one map edit.** In `infra/aws/lambda/ci/function-map/irpt-ycharts-generate.json`, in the `staged_from` entry whose `packaged_as` is `served.py`, change TWO values and nothing else: `pin` to the full 40-hex `720e125d31469ed60b6e698812c7be731bd6d8e8` and `sha256` to `600a934c4b34da1e14ec8b7d4de4a3f69cc55c331257dd90abb525def9929fcd`. Print `git grep -n 30c0eb88ec38 -- infra/aws/lambda/ci` before and after: any OTHER place naming the old sha256 is reported in a row and not edited. Commit it ALONE (this commit is the PIN for the build). Print its full sha. `git diff --numstat HEAD~1 HEAD` must show exactly `2 2` on that one file.
3. **The build tool.** Copy `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/r36s_build.py` to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/r37_build.py` and change ONLY: the constant `STATUS = "irpt-status"` to `"irpt-ycharts-generate"`, the printed tags to `R37-BUILD-OK` and `R37-BUILD-BAD`, and the docstring's names (release 37, this cell, this function). Everything else stays (two builds with a private TMPDIR, the identical-bytes refusal, the comparison with `census.build_members` at the pin). It passes `bash .tools/commit-gate.sh`.
4. **Run the build** at the step-2 commit (give it up to 590000 ms; the stage folder must NOT exist): `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/r37_build.py --pin <the step-2 full sha> --out C:/dev/irpt-release-r37o1 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/R37_BUILD.json`. The last line must begin `R37-BUILD-OK`; on `R37-BUILD-BAD <why>` or any traceback file ONE row with it and the last 20 lines, change nothing, report. Do not edit other tools or retry with other arguments.
5. **Smoke import of the BUILT package.** Unzip `C:/dev/irpt-release-r37o1/irpt-ycharts-generate.zip` into a private temp folder you create, and from a `python -I` process with that folder as the only extra `sys.path` entry print whether `import served` and `import generate_installed` both succeed (print the exception class and its first line if one does not; the Lambda runtime provides boto3, so an import of boto3 may be satisfied by the local one; say if it is). Record the two lines in the record file's companion text `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/IMPORT_SMOKE.txt`. Remove the temp folder you created.
6. **The checker** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/check_r37.py` (stdlib only, ruff clean), with three modes, each printing ONE final line:
   - `diff <record> <live-members.json>`: compares the BUILT zip's member sha256 map (the record's `functions.irpt-ycharts-generate.member_sha256`, read as `live_diff.py` of the r36 order reads its record) with the live members file and prints `R37-DIFF-OK moved=1 added=0 removed=0 same=106 mover=served.py served_sha256=600a934c4b34` ONLY when the non-SAME set is exactly `{served.py: MOVED}` and the built `served.py` sha256 equals `600a934c4b34da1e14ec8b7d4de4a3f69cc55c331257dd90abb525def9929fcd`; otherwise `R37-DIFF-BAD <why naming every other mover>` and exit 1 (an extra mover is the issuer's decision: do not suppress it).
   - `identity <record> <smoke-file>`: prints `R37-IDENTITY-OK builds_identical=yes import_served=ok import_generate_installed=ok` ONLY when the record shows the two builds byte-identical and the smoke file shows both imports ok.
   - `map <step-2 commit>`: prints `R37-MAP-OK numstat=2/2 pin=720e125d31469ed60b6e698812c7be731bd6d8e8 sha256=600a934c4b34` ONLY when `git diff --numstat <commit>~1 <commit>` is exactly one file, `infra/aws/lambda/ci/function-map/irpt-ycharts-generate.json`, with `2 2` and the `pin` and `sha256` of that entry at the commit equal the values above; otherwise `R37-MAP-BAD <why>` and exit 1.
   Its `--selftest` runs the `diff` mode on a copy of the record with a second member's hash altered and prints `CONTROL-FIRES` only when that copy yields `R37-DIFF-BAD`.
7. **Run, save, commit.** Save the outputs of the three modes and the selftest next to the record (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/DIFF.txt`, `IDENTITY.txt`, `MAP.txt`, `SELFTEST.txt`), commit the record, then the tool and outputs, as separate commits (the map edit is already its own commit). Write the proof instance (`controls.mutant` = the diff mode on the altered record copy: it must print `R37-DIFF-BAD`; `controls.determinism` = the two builds identical) and flip on VALID with all three PASS.
8. **Report** the step-2 commit sha, the build's last line, the zip's sha256, CodeSha256 and size, the three checker lines, the smoke lines, and any extra mover with its commit subject.

---

## ACCEPTANCE

<criterion id="AR426-y-AC1" cell_refs="AR-y-426"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/check_r37.py diff org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/R37_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/o1_release/LIVE_IRPT_YCDGEN_MEMBERS_20261020.json</invocation><expect>R37-DIFF-OK moved=1 added=0 removed=0 same=106 mover=served.py served_sha256=600a934c4b34</expect></criterion>
<criterion id="AR426-y-AC2" cell_refs="AR-y-426"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/check_r37.py identity org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/R37_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/IMPORT_SMOKE.txt</invocation><expect>R37-IDENTITY-OK builds_identical=yes import_served=ok import_generate_installed=ok</expect></criterion>
<criterion id="AR426-y-AC3" cell_refs="AR-y-426"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/check_r37.py map HEAD</invocation><expect>^R37-MAP-OK numstat=2/2 pin=720e125d31469ed60b6e698812c7be731bd6d8e8 sha256=600a934c4b34$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/IRPT_ANLREQ.TO-AR-y-426.o1-upload-door-lambda-build-served-py-live-plus-o1-only.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-426.o1-upload-door-lambda-build-served-py-live-plus-o1-only`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR426-y-AC1,AR426-y-AC2,AR426-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-426</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/ci/function-map/irpt-ycharts-generate.json
infra/aws/lambda/ci/function-map/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-426.o1-upload-door-lambda-build-served-py-live-plus-o1-only.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a build in a stage folder OUTSIDE the repository, one map edit (two values) and the worker's own tools and records; nothing is uploaded, applied, or run on a host; the release (a never-widen pair and IB2's apply with a scoped Terraform plan) is a later act.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the live member record, the function map entry, the scratch pin's diff against the live blob (26 insertions, 13 deletions, all O1) and the r34l lesson against this cell; the lens: DASHBD's a3058c274c riding in served.py (the scratch pin excludes it and AC1 requires served.py to be the ONLY mover at the pinned sha256), a build whose import breaks at cold start (AC2 imports the built package), a wrong member edited (AC3: two values, one entry, numstat 2 2), the stage folder reused (it must not exist). NOT seen (blind): the live Lambda after the apply and the other eight functions that stage served.py (they keep the old pin until their own releases: a drift the packet names); denominator: three criteria.
</preflight>
