# TO IRPT_BCKEND.TO-IB-pr-561 -- REBUILD the IB-pr-456 irpt-ycharts-generate candidate from current trunk on the live R29c bytes: restate the pre-apply digest, prove no silent revert of release 29, compare the ENDPOINT members by hash; READ ONLY, nothing uploaded

<to_id>IRPT_BCKEND.TO-IB-pr-561</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~405</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PY</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8116 (row D2-S185; the live bytes are R29c) and the Y2 correction (msg 8130) | **Decomp cell:** `IB-pr-561` (decomposition section 199) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-405`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~405 <0.9.0_WK_IRPT_BCKEND~405@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch405/`).

**Cell `IB-pr-561` (inlined).** The live `irpt-ycharts-generate` bytes are IRPT_ANLREQ release 29 leg L3 (`TO-APPLY-R29c`, authored by `0.7.0_AE_CloudOps~AQ2`, ledger `org/critical_paths/change_management/20261014T1246Z_irpt-ycg-r29-20261014_deploy_completion.md`, CLOSED 13:08:47Z, expected CodeSha256 `5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=`), not the pre-apply digest of the IB-pr-456 pair (`tdpterTMfJl...`). The IB-pr-456 minimal candidate (`AHxuDf7h...`, packet `deliverables/0.9.0_WK_IRPT_BCKEND~312/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-456.md` and record `IB152-1_release_read.json`, the COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_456_COMMENTARY_REQUESTED_ENDPOINT_READ_AND_COO_HALF.md`) was built BEFORE R29c: applied as it is, it would SILENTLY REVERT release 29's L3 code. The CTO ruled (msg 8116): rebuild the candidate from CURRENT trunk source, restate its pre-apply digest as `5TRFZf6G...`, and re-sign the pair only if ENDPOINT bytes move. Facts from `2.0.0_SA_COO~Y2` (msg 8130): the live zip's `uploads.py` is `f85e8c9b...` and `interactive_access.py` is `c28d9a74...` (hashed from the zip); trunk's source-map entry already pins exactly those (pins `15a387dd36`, `f09b802cdc`); the stale IB-pr-456 build input pinned `uploads.py` at `83eb798a` (sha256 `48f39329...`) and `interactive_access.py` at `5be427ba` (sha256 `d416e375...`), bytes that are NOT live. **This order REBUILDS the candidate PACKAGE LOCALLY and READS the live function. It uploads, applies, deploys, signs and writes to AWS NOTHING.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Read** the IB-pr-456 packet `~312` and its record (the BUILD METHOD: how the candidate package was assembled from `infra/aws/lambda/ci/lambda-source-map.json` and the function's source directory, and how its CodeSha256 was computed; reuse the same tool or script, find it from the record), the ledger above (what R29c moved: `generate_installed.py` and `uploads.py` moved, `ordinary_viewer.py` added) and CTO msgs 8116 and 8133.
3. **Read the live function (read-only):** `lambda get-function-configuration` for `irpt-ycharts-generate` (CodeSha256, LastModified, size) and the live code zip via `lambda get-function` (the `Location` is a presigned download; download to scratch outside the repository; hash it). The live CodeSha256 must read `5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=`; any other value is a STOP (a newer release landed): record it and report.
4. **Rebuild the candidate** from the CURRENT trunk source with the method above (local only; nothing uploaded). Record its CodeSha256, the member count (`total_members`) and the members whose bytes differ from the live zip's (`moved_members`, with their count `moved_count` equal to the list length).
5. **The silent-revert guard:** the candidate must NOT move release 29's members: `generate_installed.py`, `uploads.py`, `ordinary_viewer.py` and `interactive_access.py` must be byte-identical to the live zip's. If any of them differs, record `r29c_members_preserved` false and STOP with a BLOCKING row naming which source pin produced the old bytes.
6. **The ENDPOINT members (CTO: re-sign only if ENDPOINT bytes move):** for `submission.py`, `acceptance.py` and `AnalysisSubmissionRequest.schema.json` record `sha256_at_signing` (the hash of the member as the signed pair's packet `~312` or its record names it; if the packet gives only a build, hash the member from the IB-pr-456 build input) and `sha256_now` (the member in the new candidate), and `changed`. `endpoint_bytes_moved` and `resign_needed` are both true exactly when any of the three changed.
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~405/IB203-2_ycharts_generate_rebuild.json`: `{"base_commit":"<40hex>","function":"irpt-ycharts-generate","live_codesha256":"5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=","candidate":{"codesha256":"<base64 sha256, 44 characters>","moved_count":<n>,"total_members":<n>,"moved_members":["<member path>",...]},"r29c_members_preserved":true,"endpoint_members":{"submission.py":{"sha256_at_signing":"<64 hex>","sha256_now":"<64 hex>","changed":false},"acceptance.py":{..},"AnalysisSubmissionRequest.schema.json":{..}},"endpoint_bytes_moved":<bool>,"resign_needed":<bool>,"pre_apply_digest_restated":"5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=","notes":["what each fact rests on and what was not read; the build method used; where the candidate zip sits in scratch (never in the repository)"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB203-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record or packet (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB203-2-AC1" cell_refs="IB-pr-561"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r203/p203_cells.py" . IB203-2-AC1</invocation><expect>IB203-2-AC1 PASS</expect></criterion>
<criterion id="IB203-2-AC2" cell_refs="IB-pr-561"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r203/p203_cells.py" . IB203-2-AC2</invocation><expect>IB203-2-AC2 PASS</expect></criterion>
<criterion id="IB203-2-AC3" cell_refs="IB-pr-561"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r203/p203_cells.py" . IB203-2-AC3</invocation><expect>IB203-2-AC3 PASS</expect></criterion>

<expected_criteria>IB203-2-AC1, IB203-2-AC2, IB203-2-AC3</expected_criteria>

What the checks grade: AC1 the live function and digest, the rebuilt candidate (not the stale `AHxuDf7h` build) with its moved members listed against their count and the member total; AC2 release 29's members `generate_installed.py`, `uploads.py`, `ordinary_viewer.py` and `interactive_access.py` are NOT moved, the three ENDPOINT members compared by hash with `changed` consistent, and `resign_needed` true exactly when one moved; AC3 the pre-apply digest restated as the live one, notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS (`lambda get-function-configuration`, `lambda get-function` and the download of the live code zip to scratch outside the repository, `list`, `describe`); the candidate package is built LOCALLY in scratch and never uploaded. **Nothing is uploaded, applied, deployed, invoked, signed or sent, and no function code or configuration is changed.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, updates function code or configuration, uploads, invokes or sends; a live CodeSha256 other than the one named (a newer release landed); a candidate that moves a release-29 member (record the source pin and stop); a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W405-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~405/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 199 (round 1, workstream ~PY), cell `IB-pr-561`.
<owned_cells>IB-pr-561</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB203-2-AC1, IB203-2-AC2, IB203-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~405/IRPT_BCKEND.TO-IB-pr-561.rebuild-the-ib-pr-456-ycharts-generate-candidate-on-the-live-r29c-bytes.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads the live function's configuration and code zip, rebuilds a candidate package in scratch and writes one record; nothing is uploaded or applied, so no served byte moves; the apply of IB-pr-456 remains a later act on Andrew's execution ID (call f61b) under a pair whose pre-apply digest this record restates.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB203-2 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; eight negatives on IB203-2, each failing its own arm: the wrong live digest, the stale IB-pr-456 build, moved members not matching their count, release 29's uploads.py moved, an ENDPOINT member moved with no re-sign, a changed flag disagreeing with the hashes, the pre-apply digest not restated, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~405` (worktree `C:/dev/wk-IRPT_BCKEND-405`). Class SERVED (reads a live function and rebuilds a candidate locally; writes only the worker's records).
</preflight>
