# TO IRPT_BCKEND.TO-IB-pr-520 -- APPLY the signed pair IB-pr-518: move `irpt-ycharts-generate` to the signed built digest by its Terraform path (CTO round-185 analysis msg 7305; CTO half signed @f7bd0b5b7e, COO half @d06ee1f0fc, both at packet sha256 `7439728602c6`)

<to_id>IRPT_BCKEND.TO-IB-pr-520</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>185</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_518_CATALOGUE_FUNCTION_COO_HALF.md`, CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_518_CATALOGUE_FUNCTION_CTO_HALF.md` (both at packet sha256 `7439728602c6b63b19e727ffacced7c57cb513c0abbd676febd1c778e4f7cd99`), and the CTO's msgs 7305 and 7310 | **Decomp cell:** `IB-pr-520` (decomposition section 177) | **outcome_ref:** FWD-1 (O1 hop)

---

## WORKER FACE

**Cell `IB-pr-520` (inlined).** The Lambda `irpt-ycharts-generate` serves, among other routes, the comparison catalogue the Analysis Request form lists. The signed build changes TWO members of its 104: `templates.json` (adds Opal Ultra Short-Term, keyed by Opal's own identity, and puts the five models in canonical order: Long-Term moves from first to fourth, so the form's model checkboxes reorder for every firm, which Andrew asked for) and `maintained_sources.py` (its one pin line for the new key); `recipe.py` and every other member do not move. **This order MOVES the function to the signed built digest, once, by its Terraform path, and runs a health proof. It makes NO Lambda invoke** (the deployed entry takes no synthetic event; order IB-pr-516's first proof was refused for that reason). The packet `deliverables/0.9.0_WK_IRPT_BCKEND~367/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-518.md` is your procedure: re-hash it first (sha256 must equal `7439728602c6b63b19e727ffacced7c57cb513c0abbd676febd1c778e4f7cd99`; any other value: STOP). Its sections "Branch A", "Branch B", "Source-map row diff" and "Three conditions" are the steps. **Paths you post are `file:///` absolute URIs or markdown links to them, with the repo-relative form for another box (CLAUDE.md rule 33).**

**Do, in this order:**

1. **Gates, measured now by the artifact (READ ONLY).** (a) Both halves read signed at the packet sha256 above (open both files). (b) **One change at a time on this function** (CTO half condition 1): IB-pr-456 (`commentary_requested`) and IRPT_ANLREQ's consolidated FWD-1 release target the same function; if ANY deploy ledger under `org/critical_paths/change_management/` naming `irpt-ycharts-generate` reads OPEN, or any other seat's window is open on it, STOP: do not apply, report to the issuer. (c) Open markers: for EVERY live worktree (`git worktree list --porcelain`; a listed directory that does not exist is named, not counted), read each `org/critical_paths/.open_deploys/` marker's content at HEAD (`git -C <wt> ls-tree -r --name-only HEAD ...`, then `git show`), and count: `worktrees_read`, `marker_files_read`, and the markers naming `irpt-ycharts-generate` split into `naming_the_function_with_open_trunk_ledger` (its ledger under `org/critical_paths/change_management/` on the trunk reads OPEN: STOP if above 0) and `stale_views_naming_the_function` (OPEN at a stale worktree HEAD while the trunk ledger reads CLOSED: three are known, `irpt-ycg-release1-20261007` on two mstr merge worktrees and `tckt-vnext-r2-tr1-fwd1-thread-rerun-run3-20261011` on one rel-resident worktree; NEVER-2: such a marker proves only that THAT device saw no completion; name them, do NOT close, edit or delete them). (d) `aws lambda get-function-configuration` CodeSha256 must equal `hpNfkhLtLRl0e9TFL+Vdr5kilZ1W8bN3GKMhlzmVXgg=`; anything else (another release landed first): STOP.
2. **Name the Branch B version BEFORE any upload.** `s3api list-object-versions` (paginated to the end, the count printed) for `investor-reporting/irpt-ycharts-generate.zip` in `opal-313476888478-lambda-artifacts`; the packet names version `ennO07toFOYlPWM64JC4MS9g.bVRr7fW` (IsLatest at 2026-10-13T12:57:53Z, content-sha256 metadata equal to the live CodeSha256). Re-read it NOW: download that version to scratch OUTSIDE the repository and hash it; it must equal the live zip's sha256 (`86935f9212ed2d19...`). If no version matches: STOP, do not upload.
3. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`, your usual form) under `org/critical_paths/change_management/` BEFORE the first write, naming the function `irpt-ycharts-generate` only, the Branch B version id, and this order; commit its `.open_deploys` sentinel at once.
4. **Branch A (the packet's steps 1 to 5):** the release source map row is the packet's "Source-map row diff" (one `staged_from` row of `irpt-ycharts-generate`: `_scope/maintained_sources.py`, `pin` `0642c9d00454a852068acdee3b1b9ccd8e6ddba2` to `0d0e9e1229c099817988758bce973b06a6a969a2`, `sha256` `29c35dbfba72ca031a7d172d74f401b5976ef383d5fc4ef5deaa3a21ab2d1587` to `74c262b6db6d9d6c8c76b3668cad8d900f2977abe68325430836f26843ea2116`; the diff file `deliverables/0.9.0_WK_IRPT_BCKEND~367/IB184-1_source_map_row_diff.txt`). Make exactly that edit in the source map at your HEAD (verify by content that the blob at the new pin equals the repo's `maintained_sources.py`); `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` prints the built digest; it must equal `xP47NQDnZNZ8Lui1XQKUxUtTMTasR8Cj/A1sQnRDZYY=` (hex `c4fe3b3500e764d67c2ee8b55d0294c54b533136ac47c0a3fc0d6c4274436586`); **ABORT on any difference: never upload a digest other than the one signed.** Then the same build without `BUILD_ONLY`, verified by `head-object`; then the Terraform path `infra/aws/terraform/investor-reporting/ycharts/generate.tf` (module `irpt_ycharts_generate`, `s3_object_version` and `source_code_hash` ONLY): plan to a planfile that must read 1 to change and 0 to add or destroy, then apply it with `bash .tools/safe-apply.sh`. **Never `aws lambda update-function-code`; never a console edit; no other resource moves; the sibling functions that also stage `maintained_sources.py` are NOT moved.** Commit the source-map row with the release (the apply's own commit: the row, and the deploy fields the recorder derives from the applied artifact).
5. **After:** `get-function-configuration` CodeSha256 equals the built digest; the re-plan reads 0 changes; diff the deployed zip's members against the pre-apply live zip (download it before the apply): exactly `templates.json` and `maintained_sources.py` differ and their sha256 equal `87be046cf2bd0390a703d37be9e82a9037a3d867423e52e64a3db6415fe4728b` and `74c262b6db6d9d6c8c76b3668cad8d900f2977abe68325430836f26843ea2116`.
6. **The health proof (READ ONLY; NO invoke):** over the window from the apply's `LastModified` to now, read the `AWS/Lambda` `Invocations` and `Errors` metrics for the function (`cloudwatch get-metric-statistics`, 60 s periods) and its log group `/aws/lambda/irpt-ycharts-generate` for `Traceback`, `TypeError`, `Task timed out` and `ERROR` events (a positive control: the START lines in the same window equal the Invocations sum). Wait until at least 10 minutes have passed since the apply before you read. Record the window, the invocation count and the error count (0 expected).
7. **On any trigger of Branch B** (a 5xx or `TypeError` in the window, a digest, re-plan or member disagreement): restore by redeploying the step-2 version through the same Terraform path (`s3_object_version` and `source_code_hash`), never a console edit and never `update-function-code`; revert the source-map row; read back that CodeSha256 equals `hpNfkhLtLRl0e9TFL+Vdr5kilZ1W8bN3GKMhlzmVXgg=` and the re-plan reads 0 changes; set `rollback_performed` true and report at once.
8. **Do NOT close the ledger entry** after the health proof: the CTO's after-read is a PERSON's (the served catalogue returns the five labels in canonical order for one permitted firm and the Analysis Request form on DEV lists Ultra Short-Term; no seat can sign in). The issuer closes the ledger (or tells you to) on that read. **Write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB185-2_apply_record.json`:
`{"gates":{"packet_sha256":"<64 hex>","both_halves_signed":true,"open_markers":{"worktrees_read":<n>,"marker_files_read":<n>,"naming_the_function_with_open_trunk_ledger":0,"stale_views_naming_the_function":<n>},"open_ledgers":{"ledger_files_read":<n>,"open_naming_the_function":0}},"start_read":{"code_sha256":"<base64 digest>"},"ledger_entry":"org/critical_paths/change_management/<file>","branch_b_version_id":"<S3 version id>","apply":{"built_code_sha256":"<base64 digest>","plan":{"add":0,"change":1,"destroy":0},"safe_apply_rc":0,"path":"terraform-safe-apply"},"after":{"code_sha256":"<base64 digest>","replan_changes":0,"changed_members":["maintained_sources.py","templates.json"]},"source_map_row":{"committed":true,"pin":"<40 hex>","sha256":"<64 hex>"},"rollback_performed":false,"health_proof":{"deployed_member_sha256":{"maintained_sources.py":"<64 hex>","templates.json":"<64 hex>"},"window_start_utc":"<ts>","window_end_utc":"<ts>","invocations_in_window":<n>,"errors_in_window":0},"counters":{"function_updates":1,"lambda_invokes":0,"iam_changes":0,"route_changes":0,"env_changes":0,"table_writes":0,"figures_written":0,"files_deleted":0,"sibling_functions_moved":0}}`. The record carries no account or client number, no ARN, no path beyond the ledger entry.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IB185-2-AC1" cell_refs="IB-pr-520"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r185/p185_cells.py" . IB185-2-AC1</invocation><expect>IB185-2-AC1 PASS</expect></criterion>
<criterion id="IB185-2-AC2" cell_refs="IB-pr-520"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r185/p185_cells.py" . IB185-2-AC2</invocation><expect>IB185-2-AC2 PASS</expect></criterion>
<criterion id="IB185-2-AC3" cell_refs="IB-pr-520"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r185/p185_cells.py" . IB185-2-AC3</invocation><expect>IB185-2-AC3 PASS</expect></criterion>

<expected_criteria>IB185-2-AC1, IB185-2-AC2, IB185-2-AC3</expected_criteria>

What the checks grade: AC1 both halves signed at the packet sha256, no open ledger and no marker with an open trunk ledger naming the function (the stale views counted), the start read equal to the signed live digest, and the ledger entry naming the Branch B version; AC2 the rebuilt digest equal to the signed one, plan 1 change 0 destroy by safe-apply, the live function afterwards equal to the built digest, re-plan 0, exactly the two members changed, the source-map row committed at the new pin, no rollback; AC3 the deployed members equal the built ones, a window with zero errors, no invoke, and the bound counters. Do not edit the checks. If the apply STOPS (a gate, the digest, the plan), the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the S3 object `investor-reporting/irpt-ycharts-generate.zip` in `opal-313476888478-lambda-artifacts` (one build upload, reads of its versions), the function `irpt-ycharts-generate` through the Terraform module only, the one source-map row, the ledger entry, and your record folder. Reads: Lambda configuration and `get-function`, CloudWatch metrics and logs, S3 version lists, the open-deploy markers. **NO Lambda invoke.** No IAM, route, schedule, layer, environment or table change; no sibling function; no deletion of any object or file; no marker closed or edited.
- **Refusal clause:** STOP and report, writing nothing further, on any of: the packet's sha256 differs; a half does not read signed; an open ledger or another seat's window on the function; a marker naming the function with an open trunk ledger; the live CodeSha256 differs from `hpNfkhLtLRl0...`; no S3 version matches the live sha256; the rebuilt digest differs from the signed one; the plan is not 1 change and 0 destroy; a member beyond the two differs after the apply (then Branch B). A STOP is reported, not worked around.
- **Row ids** are `IRPT_BCKEND-D2-IB2-S<k>` (the next free `k`); file a row for anything odd and keep working. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-520.apply-catalogue-function-signed-pair.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 177 (round 185, workstream ~P), cell `IB-pr-520`.
<owned_cells>IB-pr-520</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB185-2-AC1, IB185-2-AC2, IB185-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-520.apply-catalogue-function-signed-pair.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the function `irpt-ycharts-generate` is the one resource moved, two members of 104 (`templates.json`, `maintained_sources.py`); its consumers are the catalogue route (`entry.py:150-166`), the portal's Analysis Request form (`TicketCenter.tsx:287`, `AnalysisRequestParts.tsx:112-121`) and the request composition (`reports/request_composition.py:190-215`); the model checkboxes reorder for every firm (signed on Andrew's word); the seven other functions that stage `maintained_sources.py` are not moved. The pair IB-pr-518 carries the blast radius, Branch B and the rollback per key.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the new entry adds no firm and no principal class; the apply uses the module's existing Terraform path.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p185_cells.py IB185-2 dry-run at base on dell2 2026-10-13 ~23:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (copies of the two signed halves, a synthetic ledger and record; removed): all three PASS; nine negatives each fail their own arm (a wrong packet sha256, an open ledger, a stale start digest, a plan that destroys, a third changed member, an uncommitted source-map row, errors in the window, an invoke made, a wrong deployed member).
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2, holds no other IRPT_BCKEND order). Class WORLD. Gates measured by me at ~22:5xZ: both halves signed; the live CodeSha256 `hpNfkhLtLRl0...` unchanged (re-read at ~22:3xZ); 56 of 1,860 change-management ledger files name the function and all 56 read CLOSED; no marker naming it in the open-deploy folder of this tree; NOT measured by me: other seats' planned windows on the function (the CTO half names IB-pr-456 and IRPT_ANLREQ's FWD-1 release; I asked `2.0.0_SA_COO~Y2` for theirs), and the other worktrees' markers (the seat reads every one at its own start).
</preflight>
