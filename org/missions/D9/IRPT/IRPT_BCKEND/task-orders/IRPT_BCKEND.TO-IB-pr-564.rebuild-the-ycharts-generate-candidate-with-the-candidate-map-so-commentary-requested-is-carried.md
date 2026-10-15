# TO IRPT_BCKEND.TO-IB-pr-564 -- REBUILD the irpt-ycharts-generate candidate WITH THE CANDIDATE MAP so the three ENDPOINT members carry commentary_requested; keep release 29's members at the live bytes; READ ONLY, nothing uploaded (supersedes the candidate of IB-pr-561)

<to_id>IRPT_BCKEND.TO-IB-pr-564</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~408</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PY</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the issuer's correction of its own IB-pr-561 cell, on `2.0.0_SA_COO~Y2`'s live count (msg 8161) and CTO row D2-S187 | **Decomp cell:** `IB-pr-564` (decomposition section 201) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-408`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~408 <0.9.0_WK_IRPT_BCKEND~408@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch408/`).

**Cell `IB-pr-564` (inlined).** The previous order `IB-pr-561` built a candidate (CodeSha256 `MfxpvRhV...`) from the trunk source map WITHOUT the candidate-map override. That map pins the three ENDPOINT members of `irpt-ycharts-generate` (`submission.py`, `acceptance.py`, `AnalysisSubmissionRequest.schema.json`) at commits that predate `commentary_requested`, so the candidate silently DROPPED the feature and equals the live zip except for `composition_admission.py`: it is NOT the IB-pr-456 candidate. The live zip (CodeSha256 `5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=`, release 29 leg L3) holds `commentary_requested` 0 times in those three members. **This order REBUILDS the candidate the way IB-pr-456 did: with a candidate map that re-pins exactly those three members, and keeps release 29's members at the live bytes. It READS the live function and uploads, applies, deploys, signs and writes to AWS NOTHING.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Read** the method: `deliverables/0.9.0_WK_IRPT_BCKEND~312/make_candidate_map.py` (its header says what it re-pins and how), `deliverables/0.9.0_WK_IRPT_BCKEND~312/candidate_repins.json`, the packet `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-456.md` and the record `IB152-1_release_read.json` in that folder (how the build set `BAU_SOURCE_MAP_OVERRIDE` and how the CodeSha256 was computed), and your predecessor's record `deliverables/0.9.0_WK_IRPT_BCKEND~405/IB203-2_ycharts_generate_rebuild.json`. The signed commit is `e7bb7e923a88315e4bc86d94b9d4df045d630b7c`.
3. **Read the live function (read-only):** `lambda get-function-configuration` for `irpt-ycharts-generate`; the live CodeSha256 must read `5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=` (any other value is a STOP: a newer release landed; record it and report). Download the live code zip via `lambda get-function` to scratch outside the repository and count `commentary_requested` in its three ENDPOINT members (expected 0; note the count).
4. **Write the candidate map:** `python deliverables/0.9.0_WK_IRPT_BCKEND~312/make_candidate_map.py e7bb7e923a88315e4bc86d94b9d4df045d630b7c <scratch>/candidate_map.json <scratch>/repins.json` from your worktree root (it re-pins ONLY the three ENDPOINT members; `uploads.py` and `interactive_access.py` keep the trunk map's release 29 pins). Build the candidate LOCALLY with `BUILD_ONLY=1 BAU_SOURCE_MAP_OVERRIDE=<scratch>/candidate_map.json bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` (read `build-and-upload.sh` for the exact use of the override and keep TMPDIR in scratch). Record the candidate's CodeSha256, `total_members` and the members whose bytes differ from the live zip (`moved_members`, with `moved_count` equal to the list length). The ENDPOINT members must be among them; `composition_admission.py` (native, trunk bytes) may be among them.
5. **The silent-revert guard:** `generate_installed.py`, `uploads.py`, `ordinary_viewer.py` and `interactive_access.py` must be byte-identical to the live zip's. If any differs, record `r29c_members_preserved` false and STOP with a BLOCKING row naming the pin that produced the bytes.
6. **The ENDPOINT members:** for each of `submission.py`, `acceptance.py`, `AnalysisSubmissionRequest.schema.json` record `repo_path`, `pin` (the 40-hex commit the candidate map pins it at, read from your `repins.json`), `sha256_at_signing` (the signed build's hash: submission.py `18aba4f0792f1f16c4ba14972b830fe670d4e91edef7f6c804a8fdb967d8b4cb`, acceptance.py `abbdab4935097ea5d595c0e4abcde9cea977b12b15440b0ee70caa9eeb22895d`, the schema `1052343f111b70a9297fdfb14fc9c88894793ade68fd2d23b4076def968b1a7d`), `sha256_now` (the sha256 of `git show <pin>:<repo_path>`, equal to the member in your candidate zip), `commentary_requested_count` (occurrences in those bytes; at least 1) and `changed` (`sha256_now` differs from `sha256_at_signing`). `endpoint_bytes_moved` and `resign_needed` are both true exactly when any `changed` is true.
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~408/IB205-1_ycharts_generate_rebuild_v2.json` as: `{"base_commit":"<40hex>","function":"irpt-ycharts-generate","live_codesha256":"5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=","override_map_used":true,"candidate":{"codesha256":"<base64 sha256, 44 characters>","moved_count":<n>,"total_members":<n>,"moved_members":["<member path>",...]},"r29c_members_preserved":true,"endpoint_members":{"submission.py":{"repo_path":"..","pin":"<40hex>","sha256_at_signing":"..","sha256_now":"..","commentary_requested_count":<n>,"changed":<bool>},"acceptance.py":{..},"AnalysisSubmissionRequest.schema.json":{..}},"endpoint_bytes_moved":<bool>,"resign_needed":<bool>,"composition_admission_moved":<bool, true when composition_admission.py is among the moved members>,"pre_apply_digest_restated":"5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=","notes":["at least three lines of 30+ characters: the build with the override map and its exact invocation; what was not read; where the candidate zip and the live zip sit in scratch (never in the repository); the live zip's commentary_requested count in the three members"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. The candidate CodeSha256 must differ from `MfxpvRhV...` (the wrong build), `AHxuDf7h...` (the stale IB-pr-456 build) and the live digest.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB205-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB205-1-AC1" cell_refs="IB-pr-564"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r205/p205_cells.py" . IB205-1-AC1</invocation><expect>IB205-1-AC1 PASS</expect></criterion>
<criterion id="IB205-1-AC2" cell_refs="IB-pr-564"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r205/p205_cells.py" . IB205-1-AC2</invocation><expect>IB205-1-AC2 PASS</expect></criterion>
<criterion id="IB205-1-AC3" cell_refs="IB-pr-564"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r205/p205_cells.py" . IB205-1-AC3</invocation><expect>IB205-1-AC3 PASS</expect></criterion>

<expected_criteria>IB205-1-AC1, IB205-1-AC2, IB205-1-AC3</expected_criteria>

What the checks grade: AC1 the live digest, a NEW candidate built with the override map (not the wrong, the stale or the live digest) with its ENDPOINT members among the moved members; AC2 release 29's four members not moved, each ENDPOINT member re-read by the check at its pin (sha256 and `commentary_requested` count above zero), the signed hashes, re-sign exactly when one moved; AC3 the restated digest, composition_admission.py consistent with the moved list, notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS (`lambda get-function-configuration`, `lambda get-function` and the download of the live code zip to scratch outside the repository, `list`, `describe`); the candidate package is built LOCALLY in scratch and never uploaded. **Nothing is uploaded, applied, deployed, invoked, signed or sent, and no function code or configuration is changed.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, updates function code or configuration, uploads, invokes or sends; a live CodeSha256 other than the one named; a candidate that moves a release 29 member; a client identifier in a tracked file; a need to type an object address by hand (a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W408-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~408/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 201 (round 2, workstream ~PY), cell `IB-pr-564`.
<owned_cells>IB-pr-564</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB205-1-AC1, IB205-1-AC2, IB205-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~408/IRPT_BCKEND.TO-IB-pr-564.rebuild-the-ycharts-generate-candidate-with-the-candidate-map-so-commentary-requested-is-carried.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads the live function's configuration and code zip, rebuilds a candidate package in scratch with a candidate map and writes one record; nothing is uploaded or applied, so no served byte moves; the apply of IB-pr-456 remains a later act on Andrew's execution ID (call f61b) under a pair re-signed on the corrected candidate.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p205_cells.py IB205-1 dry-run at base on dell2 2026-10-15 ~07:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp git root the run created itself (stub members at the real relative paths in a commit that carries commentary_requested and one that does not, a synthetic record; removed): all three PASS; fifteen negatives, each failing its own arm: the wrong MfxpvRhV candidate, the live digest, no override map, the ENDPOINT members not among the moved members, a count mismatch, release 29's uploads.py moved, the preserved flag false, a pin whose member lacks commentary_requested, a wrong now hash, a wrong signed hash, resign false while changed, the digest not restated, the composition flag wrong, short notes, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~408` (worktree `C:/dev/wk-IRPT_BCKEND-408`). Class SERVED (reads a live function and rebuilds a candidate locally; writes only the worker's records).
</preflight>
