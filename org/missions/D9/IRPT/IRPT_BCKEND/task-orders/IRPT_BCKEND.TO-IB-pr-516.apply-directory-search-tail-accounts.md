# TO IRPT_BCKEND.TO-IB-pr-516 -- APPLY the signed pair IB-pr-515: move `irpt-directory-search` to the signed built digest by its Terraform path, then one synthetic tail search (Andrew-direct ~17:0xZ row D2-S140; CTO half signed @01d0a01db9; gates read met, row D2-S141)

<to_id>IRPT_BCKEND.TO-IB-pr-516</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>182</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_515_DIRECTORY_SEARCH_REFRESHED_COO_HALF.md`, CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_515_DIRECTORY_SEARCH_REFRESHED_CTO_HALF.md` (both at packet sha256 `3c369b9086b3453fdb40efcc94655eb17933d2c65c35f248dd6255cb21db6888`), and CTO msg 7098 | **Decomp cell:** `IB-pr-516` (decomposition section 174) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-516` (inlined):** the Lambda `irpt-directory-search` serves the Investor Reporting header search. Today a last-four (tail) query returns the relationship's entry for the head account only. The signed build changes ONE member, `handler.py`, so a tail query returns each PERMITTED account's own ACCOUNT entry with its mask, and a pick resolves to exactly that account. **This order MOVES the function to the signed built digest, once, by its Terraform path, and then runs ONE read-only search by a tail over a SYNTHETIC directory through the deployed function.** The packet `deliverables/0.9.0_WK_IRPT_BCKEND~365/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-515.md` is your procedure: re-hash it first (sha256 must equal `3c369b9086b3453fdb40efcc94655eb17933d2c65c35f248dd6255cb21db6888`; any other value: STOP). Its sections "Branch A", "Branch B" and "Direct-invoke proof" are the steps.

**Do, in this order:**

1. **Gates, measured now by the artifact (READ ONLY).** (a) Both halves read signed at the packet sha256 above (open both files). (b) Step 0: the function's directory homes equal the builder's: read `IRPT_DIRECTORY_BUCKET_MAP` and `IRPT_DIRECTORY_PREFIX` on the live function configuration and the inline policy `irpt-directory-policy`: `opal-data-bd`, `opal-data-cot`, `opal-data-inf` under `investor-reporting/directory`; MATCH is true only if these are the same three buckets and prefix the packet's Step 0 names. (c) No open deploy marker names the function: for EVERY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), read each marker file's content at HEAD and count those naming `irpt-directory-search`; **print the denominator (worktrees read, marker files read)**; a worktree that is not a git repository is listed, not counted. Any marker naming the function: STOP. (d) `aws lambda get-function-configuration` CodeSha256 must equal `tvrsQ+w820jp1pxiUoYrhiKCZGVnViUTbBsDUbJEG3w=`; anything else: STOP.
2. **Name the Branch B version, BEFORE any upload.** List the versions of `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip` (`s3api list-object-versions`, paginated to the end, count printed) and name the version whose content sha256 equals the live hex `b6faec43ec3cdb48e9d69c6252862b8622826465675625136c1b0351b2441b7c` (download that version to scratch OUTSIDE the repository and hash it; the version that `lambda get-function` serves is the same bytes). If no version matches: STOP, do not upload.
3. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`, your usual form) under `org/critical_paths/change_management/` BEFORE the first write, naming the function `irpt-directory-search` only, the Branch B version id from step 2, and this order; commit its `.open_deploys` sentinel at once.
4. **Branch A (the packet's steps 4 to 6, verbatim in intent):** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-directory-search` prints the built digest; it must equal `rXHDDz/ZhY2pZFuLDcrPisAs69IuTd6p8Rwflxhvwyw=` (hex `ad71c30f3fd9858da9645b8b0dcacf8ac02cebd22e4ddea9f11c1f97186fc32c`); **ABORT on any difference: never upload a digest other than the one signed.** Then the same build without `BUILD_ONLY`, verified by `head-object`; then the Terraform path `infra/aws/terraform/investor-reporting/directory/lambda.tf` (module `irpt_directory_search`, `s3_object_version` and `source_code_hash` ONLY): plan to a planfile that must read 1 to change and 0 to add or destroy, then apply it with `bash .tools/safe-apply.sh`. **Never `aws lambda update-function-code`; never a console edit; no other resource moves.** The sibling `irpt-directory-refresh` is NOT moved.
5. **After:** `lambda get-function-configuration` CodeSha256 equals `rXHDDz/ZhY2pZFuLDcrPisAs69IuTd6p8Rwflxhvwyw=`; the re-plan reads 0 changes; diff the deployed zip's members against the pre-apply live zip you downloaded: `handler.py` is the ONLY member that differs.
6. **The direct proof (READ ONLY; persists nothing):** two direct `aws lambda invoke` calls of the DEPLOYED `irpt-directory-search`, each with an API-shaped event carrying a `directory_fixture` (the function then reads no S3 and no live data): build the fixture and the scope with the same shapes as `deliverables/0.9.0_WK_IRPT_BCKEND~365/ib181_replay_reach.py` lines 40-92 (opaque made-up ids and masks). (i) `{"op":"search","q":"3333","resolved_scope":<scope>,"directory_fixture":<fixture>}` must return exactly ONE result of kind ACCOUNT with `permitted_account_count` 1; (ii) `{"op":"resolve","selection":{"entry_id":<that result's entry_id>},...}` must return exactly ONE account. Record the response sha256 of (i) only; do not write the response to the repository.
7. **On any trigger of Branch B** (a 5xx or `TypeError`, a direct-proof arm that disagrees, a digest or re-plan that disagrees): restore by redeploying the step-2 version through the same Terraform path (`s3_object_version` and `source_code_hash`), never a console edit and never `update-function-code`; read back that CodeSha256 equals `tvrsQ+w820jp1pxiUoYrhiKCZGVnViUTbBsDUbJEG3w=` and the re-plan reads 0 changes; set `rollback_performed` true and report at once.
8. **Close the ledger entry; write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB182-1_apply_record.json`:
`{"gates":{"packet_sha256":"<64 hex>","both_halves_signed":true,"step0_match":true,"open_markers":{"worktrees_read":<n>,"marker_files_read":<n>,"naming_the_function":0}},"start_read":{"code_sha256":"<base64 digest>"},"ledger_entry":"org/critical_paths/change_management/<file>","branch_b_version_id":"<S3 version id>","apply":{"built_code_sha256":"<base64 digest>","plan":{"add":0,"change":1,"destroy":0},"safe_apply_rc":0,"path":"terraform-safe-apply"},"after":{"code_sha256":"<base64 digest>","replan_changes":0,"changed_members":["handler.py"]},"rollback_performed":false,"direct_proof":{"operation":"search","directory":"synthetic","persisted":false,"account_entries":1,"kind":"ACCOUNT","permitted_account_count":1,"resolve_account_count":1,"response_sha256":"<64 hex>"},"counters":{"function_updates":1,"lambda_invokes":2,"iam_changes":0,"route_changes":0,"env_changes":0,"table_writes":0,"figures_written":0,"files_deleted":0,"sibling_functions_moved":0}}`. The record carries no account or client number, no ARN, no path beyond the ledger entry.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IB182-1-AC1" cell_refs="IB-pr-516"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r182/p182_cells.py" . IB182-1-AC1</invocation><expect>IB182-1-AC1 PASS</expect></criterion>
<criterion id="IB182-1-AC2" cell_refs="IB-pr-516"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r182/p182_cells.py" . IB182-1-AC2</invocation><expect>IB182-1-AC2 PASS</expect></criterion>
<criterion id="IB182-1-AC3" cell_refs="IB-pr-516"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r182/p182_cells.py" . IB182-1-AC3</invocation><expect>IB182-1-AC3 PASS</expect></criterion>

<expected_criteria>IB182-1-AC1, IB182-1-AC2, IB182-1-AC3</expected_criteria>

What the checks grade: AC1 both halves signed at the packet sha256, step 0 MATCH, the marker count over every worktree with its denominator at 0, the start read equal to the signed live digest, and the ledger entry naming the Branch B version; AC2 the rebuilt digest equal to the signed one, a plan of 1 change and 0 destroy by the safe-apply path, the live function equal to the built digest afterwards, a re-plan of 0 changes, `handler.py` the only changed member, no rollback; AC3 the synthetic tail search (one ACCOUNT entry, one permitted account) and its resolve (one account), the response digest, and the bound counters. Do not edit the checks. If the apply STOPS (a gate, the digest, the plan), the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the S3 object `investor-reporting/irpt-directory-search.zip` in `opal-313476888478-lambda-artifacts` (one build upload, reads of its versions), the function `irpt-directory-search` through the Terraform module only, the ledger entry, and your record folder. Reads: Lambda configuration and `get-function`, IAM inline policy, the open-deploy markers, S3 version lists. **Two `aws lambda invoke` calls of the function, both with `directory_fixture` (read operations over a synthetic fixture).** No IAM, route, schedule, layer, environment or table change; no sibling function; no deletion of any object or file; no live directory read for the proof.
- **Refusal clause:** STOP and report, writing nothing further, on any of: the packet sha256 differs; a half does not read signed; step 0 does not match; a marker names the function; the live CodeSha256 differs from `tvrsQ+w82...`; no S3 version matches the live sha256; the rebuilt digest differs from the signed one; the plan is not 1 change and 0 destroy; the direct proof disagrees (then Branch B). A STOP is reported, not worked around.
- **Row ids** are `IRPT_BCKEND-D2-IB2-S<k>` (the next free `k`); file a row for anything odd and keep working. **Report once at the end, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-516.apply-directory-search-tail-accounts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 174 (round 182, workstream ~P), cell `IB-pr-516`.
<owned_cells>IB-pr-516</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB182-1-AC1, IB182-1-AC2, IB182-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-516.apply-directory-search-tail-accounts.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the function `irpt-directory-search` is the one resource moved, one member (`handler.py`, 1 of 24); its consumers are the portal's header search and the Generate composer (`GenerateComposer.tsx:83`, an empty query, so no tail match changes it); the sibling `irpt-directory-refresh` shares the `source_dir` and is not moved. The pair IB-pr-515 carries the blast radius, Branch B and the rollback per key.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the apply uses the module's existing Terraform path and the function's own role for the direct proof.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p182_cells.py dry-run at base on dell2 2026-10-13 ~17:3xZ: IB182-1 AC1, AC2, AC3 FAIL (no record). Positive control: a synthetic record in a temp root the run created itself (copies of the two signed halves, a synthetic ledger file) passes all three; one defect per arm (a wrong packet sha256, a plan that destroys, two account entries) fails that arm; the temp root removed; nothing in the repository touched.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2, holds no other IRPT_BCKEND order). Class WORLD. Gates measured by me at ~17:2xZ (row D2-S141): both halves signed; portal condition (a) read at 0 null accountId over 9,441 ACCOUNT entries from the built `handler.py`; 0 of 271 open-deploy markers on 15 readable worktrees name the function; live CodeSha256 `tvrsQ+w82...`. The seat re-measures all of them at its own start.
</preflight>
