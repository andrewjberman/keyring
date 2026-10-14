# TO IRPT_BCKEND.TO-IB-pr-521 -- APPLY the signed pair IB-pr-519: re-pin `irpt-export-render`'s packaged `ExportReceipt.schema.json` to v1.2 by the function's Terraform path (CTO round-186 analysis item 1; CTO half signed @a047ade972, COO half @b667f38d96, both at packet sha256 `7d7888984731`)

<to_id>IRPT_BCKEND.TO-IB-pr-521</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>186</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_519_EXPORT_RECEIPT_REPIN_COO_HALF.md`, CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_519_EXPORT_RECEIPT_REPIN_CTO_HALF.md` (both at packet sha256 `7d78889847312b5517d1d85172a93c5f1f993de30760c8f83d60c92079a7b53b`), and the CTO's round-186 analysis (msg 7355) | **Decomp cell:** `IB-pr-521` (decomposition section 178) | **outcome_ref:** FWD-1 (O1 hop)

---

## WORKER FACE

**Cell `IB-pr-521` (inlined).** Andrew's export of an Opal report is created but its status read fails ("The export's status could not be read (UNEXPECTED)"), live on PROD. Cause (row D2-S152, read from the live log and zip): the Lambda `irpt-export-render` writes receipts with `facts.covered_account_ids` but packages a STALE `irpt_contracts/ExportReceipt.schema.json` (v1.1; `facts.additionalProperties` false), so its own receipt read is refused. The signed build changes ONE member of 66, that schema, to v1.2. **This order MOVES the function to the signed built digest, once, by its Terraform path, validates the one stored receipt OFFLINE against the DEPLOYED schema, and runs a health proof. It makes NO Lambda invoke.** The packet `deliverables/0.9.0_WK_IRPT_BCKEND~368/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-519.md` is your procedure: re-hash it first (sha256 must equal `7d78889847312b5517d1d85172a93c5f1f993de30760c8f83d60c92079a7b53b`; any other value: STOP). Its sections "Branch A", "Branch B", "Source-map row diff" and conditions are the steps. **Paths you post are `file:///` absolute URIs or markdown links to them, with the repo-relative form for another box (CLAUDE.md rule 33).**

**Do, in this order:**

1. **Gates, measured now by the artifact (READ ONLY).** (a) Both halves read signed at the packet sha256 above. (b) **The receipt store, re-read:** run `python infra/aws/lambda/investor-reporting/export/tools/backfill_covered_account_ids.py` in its DEFAULT `--dry-run` mode ONLY (never `--apply`), `--census-out` to scratch OUTSIDE the repository; record `receipts_total`, `receipts_with_field`, `receipts_lacking_field`, `unreadable_or_denied` (counts only). **If `receipts_lacking_field` or `unreadable_or_denied` is above 0: STOP**: the backfill must run first under its own signed pair and the re-pin must not go live over a receipt it would refuse (CTO RE 7262: never refuse a receipt that exists today). (c) **One change at a time on this function:** if ANY deploy ledger under `org/critical_paths/change_management/` naming `irpt-export-render` reads OPEN, or any other seat's window is open on it, STOP. (d) Open markers: for EVERY live worktree (`git worktree list --porcelain`; a listed directory that does not exist is named, not counted), read each `org/critical_paths/.open_deploys/` marker's content at HEAD and count `worktrees_read`, `marker_files_read`, and the markers naming `irpt-export-render` split into `naming_the_function_with_open_trunk_ledger` (STOP if above 0) and `stale_views_naming_the_function` (OPEN at a stale worktree HEAD while the trunk ledger reads CLOSED: name them, do NOT close, edit or delete them: NEVER-2). (e) `aws lambda get-function-configuration` CodeSha256 must equal `K74JEIjw0NKmy4YfEo7Sb7LcRxEII+/yaYtaKJ3qnD8=`; anything else: STOP.
2. **Name the Branch B version BEFORE any upload.** `s3api list-object-versions` (paginated to the end, the count printed) for `investor-reporting/irpt-export-render.zip` in `opal-313476888478-lambda-artifacts`; the packet names version `_LGUODZLsTpblhaTy2ODlBjRnwdx6cW1` (ContentLength 419460, content-sha256 metadata equal to the live CodeSha256). Re-read it NOW: download that version to scratch OUTSIDE the repository and hash it; it must equal the live zip's sha256 (`2bbe091088f0d0d2...`). If no version matches: STOP, do not upload. Also download the live zip itself (the pre-apply zip, `get-function` `Code.Location`) for step 5.
3. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`) under `org/critical_paths/change_management/` BEFORE the first write, naming the function `irpt-export-render` only, the Branch B version id, and this order; commit its `.open_deploys` sentinel at once. **Use the ledger's own tooling; do not call a stamp or recorder that writes to the shared source map outside step 4's one row (round 185's apply wrote four stray lines there and reversed them).**
4. **Branch A (the packet's steps 1 to 4):** the release source-map row is the packet's "Source-map row diff" (function `irpt-export-render`, the ONE `staged_from` row `docs/contracts/investor-reporting/v1/ExportReceipt.schema.json`: `pin` `8d08ee54e488e74ef5bc9f4ba715e0a3cad776f5` to `e8005582a1fde9bf21f70b49f8b773e356a394e7`, `sha256` `5a7bda2ecddd81eb91423ee1acf4d86b8bca4b3c515dff97e8028420320d69ba` to `118a3575eaf20ff6ffb37d387b0cb3d4bd5e1a4d42ce68c86c07919bc968b4c7`; the diff file `deliverables/0.9.0_WK_IRPT_BCKEND~368/IB185-1_source_map_row_diff.txt`). Make exactly that edit (verify by content that the blob at the new pin equals the repo's current schema file); `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render` prints the built digest; it must equal `5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=` (hex `e7ff4b6416d311639fae7359b9f73a32acf9a5b0f14f1600c6959c6555111ace`); **ABORT on any difference: never upload a digest other than the one signed.** Then the same build without `BUILD_ONLY`, verified by `head-object`; then the Terraform path `infra/aws/terraform/investor-reporting/export/lambda.tf` (module `irpt_export_render`, `s3_object_version` and `source_code_hash` ONLY): plan to a planfile that must read 1 to change and 0 to add or destroy, then apply it with `bash .tools/safe-apply.sh`. **Never `aws lambda update-function-code`; never a console edit; no other resource moves.** Commit the source-map row with the release (the apply's own commit: the row, and the deploy fields the recorder derives from the applied artifact).
5. **After:** `get-function-configuration` CodeSha256 equals the built digest; the re-plan reads 0 changes; diff the deployed zip's members against the pre-apply zip: exactly `irpt_contracts/ExportReceipt.schema.json` differs and its sha256 equals `118a3575eaf20ff6ffb37d387b0cb3d4bd5e1a4d42ce68c86c07919bc968b4c7`.
6. **The stored receipt on the DEPLOYED schema (OFFLINE, the person-read's seat-side half):** download the ONE stored receipt the dry run counted to scratch OUTSIDE the repository, validate its JSON against the DEPLOYED zip's `irpt_contracts/ExportReceipt.schema.json` member with the `jsonschema` library (the zip's own file, not the repo's), record only `receipts_checked` 1 and `valid` 1 (or 0), and **delete the scratch copy**: no export id, firm key or content in any tracked file. A `valid` of 0 is a Branch B trigger.
7. **The health proof (READ ONLY; NO invoke):** after at least 10 minutes since the apply, over the window from the apply's `LastModified` to now, read the `AWS/Lambda` `Invocations` and `Errors` metrics for the function (`cloudwatch get-metric-statistics`, 60 s periods) and its log group `/aws/lambda/irpt-export-render` for `Traceback`, `TypeError`, `Task timed out`, `ERROR` and `ValidationError` events (a positive control: the START lines in the same window equal the Invocations sum). Record the window, the invocation count and the error count (0 expected).
8. **On any trigger of Branch B** (a 5xx, `TypeError` or `ValidationError` in the window, a digest, re-plan or member disagreement, a stored receipt invalid on the deployed schema): restore by redeploying the step-2 version through the same Terraform path, never a console edit and never `update-function-code`; revert the source-map row; read back that CodeSha256 equals `K74JEIjw0NKmy4YfEo7Sb7LcRxEII+/yaYtaKJ3qnD8=` and the re-plan reads 0 changes; set `rollback_performed` true and report at once.
9. **Do NOT close the ledger entry** after the health proof: the CTO's after-read is a person's (one NEW export reaching a readable status on DEV: Andrew's next export). The issuer closes the ledger (or tells you to) on that read. **Write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB186-1_apply_record.json`:
`{"gates":{"packet_sha256":"<64 hex>","both_halves_signed":true,"receipt_store_reread":{"mode":"dry_run_reads_only","receipts_total":<n>,"receipts_lacking_field":0,"unreadable_or_denied":0},"open_markers":{"worktrees_read":<n>,"marker_files_read":<n>,"naming_the_function_with_open_trunk_ledger":0,"stale_views_naming_the_function":<n>},"open_ledgers":{"ledger_files_read":<n>,"open_naming_the_function":0}},"start_read":{"code_sha256":"<base64 digest>"},"ledger_entry":"org/critical_paths/change_management/<file>","branch_b_version_id":"<S3 version id>","apply":{"built_code_sha256":"<base64 digest>","plan":{"add":0,"change":1,"destroy":0},"safe_apply_rc":0,"path":"terraform-safe-apply"},"after":{"code_sha256":"<base64 digest>","replan_changes":0,"changed_members":["ExportReceipt.schema.json"]},"source_map_row":{"committed":true,"pin":"<40 hex>","sha256":"<64 hex>"},"rollback_performed":false,"health_proof":{"deployed_member_sha256":"<64 hex>","stored_receipt_on_deployed_schema":{"validated_offline":true,"receipts_checked":1,"valid":1,"scratch_removed":true},"window_start_utc":"<ts>","window_end_utc":"<ts>","invocations_in_window":<n>,"errors_in_window":0},"counters":{"function_updates":1,"lambda_invokes":0,"iam_changes":0,"route_changes":0,"env_changes":0,"receipts_written":0,"table_writes":0,"figures_written":0,"files_deleted":0,"sibling_functions_moved":0}}`. The record carries no account, client, export or firm identifier, no ARN, no path beyond the ledger entry. (`files_deleted` counts repository or bucket files, never your own scratch.)

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IB186-1-AC1" cell_refs="IB-pr-521"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r186/p186_cells.py" . IB186-1-AC1</invocation><expect>IB186-1-AC1 PASS</expect></criterion>
<criterion id="IB186-1-AC2" cell_refs="IB-pr-521"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r186/p186_cells.py" . IB186-1-AC2</invocation><expect>IB186-1-AC2 PASS</expect></criterion>
<criterion id="IB186-1-AC3" cell_refs="IB-pr-521"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r186/p186_cells.py" . IB186-1-AC3</invocation><expect>IB186-1-AC3 PASS</expect></criterion>

<expected_criteria>IB186-1-AC1, IB186-1-AC2, IB186-1-AC3</expected_criteria>

What the checks grade: AC1 both halves signed at the packet sha256, the receipt store re-read with none lacking the field, no open ledger and no marker with an open trunk ledger naming the function, the start read equal to the signed live digest, and the ledger entry naming the Branch B version; AC2 the rebuilt digest equal to the signed one, plan 1 change 0 destroy by safe-apply, the live function afterwards equal to the built digest, re-plan 0, exactly the schema member changed, the source-map row committed at the new pin, no rollback; AC3 the deployed member equal to the built one, the one stored receipt valid on the DEPLOYED schema (offline), a window with zero errors, no invoke, and the bound counters. Do not edit the checks. If the apply STOPS (a gate, the digest, the plan), the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the S3 object `investor-reporting/irpt-export-render.zip` in `opal-313476888478-lambda-artifacts` (one build upload, reads of its versions), the function `irpt-export-render` through the Terraform module only, the one source-map row, the ledger entry, your record folder, the dry-run reads of the receipt store (the one stored receipt downloaded to scratch and deleted), and reads of Lambda configuration, CloudWatch metrics and logs. **NO Lambda invoke; NO write to the receipt store; the backfill tool is NEVER run with `--apply`.** No IAM, route, schedule, layer, environment or table change; no sibling function; no deletion of any bucket object or repository file; no marker closed or edited.
- **Refusal clause:** STOP and report, writing nothing further, on any of: the packet's sha256 differs; a half does not read signed; a receipt lacking the field or unreadable in the store; an open ledger or another seat's window on the function; a marker naming the function with an open trunk ledger; the live CodeSha256 differs from `K74JEIjw...`; no S3 version matches the live sha256; the rebuilt digest differs from the signed one; the plan is not 1 change and 0 destroy; a member beyond the schema differs after the apply (then Branch B). A STOP is reported, not worked around.
- **Row ids** are `IRPT_BCKEND-D2-IB2-S<k>` (the next free `k`); file a row for anything odd and keep working. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-521.apply-export-receipt-repin-signed-pair.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 178 (round 186, workstream ~P), cell `IB-pr-521`.
<owned_cells>IB-pr-521</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB186-1-AC1, IB186-1-AC2, IB186-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-521.apply-export-receipt-repin-signed-pair.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the function `irpt-export-render` is the one resource moved, one member of 66 (`irpt_contracts/ExportReceipt.schema.json`); its consumers are the receipt read (`GET /api/scoped/investor-reporting/export/{exportId}`, routes cell IB-s-14) and the portal's export status poll (`investor-reporting.ts getExportReceipt`, `submit.ts pollExportReceipt`); the stored receipt count is 1 (the pair's census); the seven other functions that stage a copy of the contracts are not moved. The pair IB-pr-519 carries the blast radius, Branch B and the rollback per key.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the apply uses the module's existing Terraform path; the receipt reads use the seat's existing identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p186_cells.py IB186-1 dry-run at base on dell2 2026-10-13 ~23:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (copies of the two signed halves, a synthetic ledger and record; removed): all three PASS; seven negatives each fail their own arm (a receipt lacking the field, a stale start digest, a second changed member, a plan that destroys, a stored receipt invalid on the deployed schema, scratch kept, an invoke made).
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2; holds the open ledger of round 185's catalogue apply, a different function). Class WORLD. Gates measured by me at ~23:4xZ: both halves signed; the live CodeSha256 `K74JEIjw...` unchanged (re-read at ~23:3xZ); 49 change-management ledger files name the function and all read CLOSED (the worker's census); NOT measured by me: other seats' planned windows on the function (the seat re-measures all of it at its own start).
</preflight>
