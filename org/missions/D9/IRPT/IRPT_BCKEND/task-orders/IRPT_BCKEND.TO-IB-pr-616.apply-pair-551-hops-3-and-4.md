# TO IRPT_BCKEND.TO-IB-pr-616 -- APPLY hops 3 and 4 of the signed pair IB-pr-551 with its ADDENDUM 1 and 2: the report route on the reporting-read function, the export bundle (server_pinned_body), then the one IAM statement on irpt-export-render-role (after the fence row is read back); STAGED, hop 2 first (CTO msgs 9528, 9546, 9576, 9614)

<to_id>IRPT_BCKEND.TO-IB-pr-616</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~S2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair: COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_551_SERVE_PATH_HOPS_2_4_COO_HALF.md` (git blob `9a036bf61794d7eb3be2fc4def3b3b442dc4c761`; packet `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` sha256 `7daa29f0fe10e0a7bda3eb2c12f1eee3bb4ca43ecc7361fbdf1327ded864abac`: READ IT ALL, sections 1, 4, 5, 9 and 10), the CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_551_SERVE_PATH_HOPS_2_4_CTO_HALF.md` with its ADDENDUM 1 (`deliverables/2.0.0_SA_COO~S2/NEVER_WIDEN_IB_pr_551_ADDENDUM_1_EXPORT_FILLED_READ_GRANT_DRAFT.md`, blob `9462b5ad35af646c96ede013f03d4449e8815033`, and its COO half `..._ADDENDUM_1_COO_HALF.md`, blob `a09b331c4153cba7aea872001ed7998145d0e984`) and ADDENDUM 2 (`..._ADDENDUM_2_FENCE_ROW_COO_HALF.md`, blob `b5c303ea69ffa4195ec441d455d9f1978c327678`); the plan and BEFORE state `deliverables/2.0.0_SA_COO~S2/IB_pr_551_HOPS_3_4_RELEASE_PLAN_BEFORE_STATE_20261016.md` (read it, then re-read every value in it live). Hop 2 is NOT in this order: it is `~D2`'s publish pair (TO-DB-b-312).

**STAGED.** This order is `staged`: you do NOT begin on reading it. The issuer flips it to `pending` and sends a GO that cites this order when ALL of these read true: `~D2`'s TO-DB-b-312 is `complete` and its ledger `irpt-dashbd-49f-publish-hop2-reader-readgrant-20261016` is CLOSED by its issuer (hop 2 first, CTO msg 9614), and no other apply names `irpt-49f-reporting-read-lambda` or `irpt-export-render`. The GO says whether the IAM leg (Step 6) may run: it may only when the second fence row for `irpt-export-render-role` is at HEAD of `infra/logic/registry/exemptions.json` and the laptop's regeneration is read back; until then you run Steps 1 to 5 and report, and the issuer sends a second GO for Step 6.

---

## WORKER FACE

**Cell `IB-pr-616` (inlined).** The filled-report serve path has four hops. Hop 1 (the gold table `filled_report_values`) exists for 49 Financial. Hop 2 (the platinum `filled_report.json` writer, switch OFF) is `~D2`'s and lands first. This cell is hop 3, the route `GET /api/scoped/investor-reporting/reporting/client/{client_id}/report` on `irpt-49f-reporting-read-lambda` (declared at `infra/aws/terraform/investor-reporting/reporting-read/locals.tf:78` and `api.tf:42`; code `reporting/entry.py` and `_scope/filled_named_accounts.py`), and hop 4, the export function `irpt-export-render` (bundle: `server_pinned_body`, `filled_reader_installed.py`, `retained_export.py`, the `filled_report` source kind) plus the one IAM statement that lets the export function read the pinned object by VersionId. Nothing is served until the separate switch-on pair turns hop 2's pass on; this order makes the route and the export able to read what hop 2 will write. Everything is additive: no existing route, key or served value changes.

**Do, in this order. A STOP is reported to the issuer at once and writes nothing further.**

1. **Gates, read only.** (a) `git hash-object` of the pair's COO half equals `9a036bf6...`, of ADDENDUM 1's document equals `9462b5ad35af...`, of its COO half equals `a09b331c4153...`, of ADDENDUM 2's COO half equals `b5c303ea69ff...`; the CTO half reads SIGNED for the pair, ADDENDUM 1 and ADDENDUM 2 at those bytes. (b) The issuer's GO cites this order and names whether Step 6 may run. (c) **One change at a time:** read `.open_deploys/` in EVERY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), union them, print `worktrees_read` and `marker_files_read`; no OPEN ledger or marker names `irpt-49f-reporting-read-lambda`, `irpt-export-render`, their roots (`reporting-read`, `export`) or the role `irpt-export-render-role`, and `~D2`'s hop 2 ledger reads CLOSED (CVO rule, msg 8750). (d) The live BEFORE state equals the plan's: `irpt-49f-reporting-read-lambda` CodeSha256 `WjnDxvu2biEPXcwuF8oXJWRUqFaeUY550xnRxa2daa0=`, `irpt-export-render` CodeSha256 `5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=`, and no `/report` route on the API (`aws apigatewayv2 get-routes` on the reporting API, read only). A different value is a STOP and a re-cut.
2. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`) under `org/critical_paths/change_management/` BEFORE the first write, naming the legs of the packet's section 10 that this order carries (the route and its Lambda deploy; the export source kind; the IAM statement), and this order; commit its `.open_deploys` sentinel at once. Name in it EVERY task family or consumer of `irpt-export-render-role` (one `describe` sweep, printed).
3. **Hop 3 (the route and the read function).** Build the read function's bundle from HEAD through the repo's builder (BUILD_ONLY first; write the three pins the packet's condition names before the build if the builder demands them; the builder only verifies). Upload ONE new version at the source map's `artifact_s3_key`, built == landed. `terraform plan` on `infra/aws/terraform/investor-reporting/reporting-read` to a planfile: it must read ONE `aws_apigatewayv2_route` added for the report route and the read Lambda's code attributes changed, and NO existing route, authorizer or integration changed (read the plan's resource list; record it). Then `bash .tools/safe-apply.sh` on that planfile. Never a bare apply, never a console edit.
4. **After-read, hop 3.** Re-plan reads 0 changes. The function's live CodeSha256 equals the built zip's base64 sha256; the report route is present on the API and the summary route and the series routes are unchanged. Do NOT call the new route with a real client: nothing writes `filled_report.json` yet.
5. **Hop 4a (the export bundle).** Same method for `irpt-export-render` on `infra/aws/terraform/investor-reporting/export` (code attributes only; the filled-report switch is NOT touched here and stays unset/OFF). After-read: live CodeSha256 equals the built zip's.
6. **Hop 4b (the IAM statement), only when the GO says so.** (a) STEP 0 of ADDENDUM 1: read the role's statements live; if a statement already allows `s3:GetObject` on a `filled_report.json` object, or the fence row is not yet the second row read back, STOP (a present, equal or wider grant voids ADDENDUM 1; report instead of adding a duplicate). (b) Read the fence: the second registry row for `irpt-export-render-role` (prefix `irpt/49financial/platinum/reporting/`, `s3:GetObject` and `s3:GetObjectVersion`) is at HEAD of `infra/logic/registry/exemptions.json` AND the laptop's regeneration is read back (the Terraform-generated Deny no longer denies the role on that prefix); not yet: STOP and wait for the second GO. (c) Edit `infra/aws/terraform/investor-reporting/export/b1_submit.tf` ONLY: add one statement to `aws_iam_role_policy.export_render_submit`: `Allow`, `s3:GetObject` and `s3:GetObjectVersion`, resource `arn:aws:s3:::opal-data-49financial/irpt/49financial/platinum/reporting/client=*/filled_report.json`, with the bucket, firm, tier, table and object name DERIVED from `infra/logic/registry/scopes.json` and the `FILLED_REPORT` row of policy `irpt-dashbd-x10-v1` in `infra/logic/registry/reporting_policies.json` (a new local beside `b1_reporting_policy`; nothing typed, CLAUDE.md rule 30); commit that ONE file (`.tools/safe-commit.sh`, your own author, `-F`) and name the pre-edit blob for the rollback. (d) `terraform plan` to a planfile: exactly 0 add / 1 change / 0 destroy, the one being `aws_iam_role_policy.export_render_submit`, one statement added, none removed (an output change is not a resource); anything else: STOP and revert the edit. `bash .tools/safe-apply.sh` on that planfile. (e) After-read: re-plan 0 changes; `aws iam simulate-principal-policy` on the role: `s3:GetObject` and `s3:GetObjectVersion` ALLOWED on `.../client=PLACEHOLDER/filled_report.json` under the bucket; `s3:PutObject` on it, `s3:GetObject` on a key outside `irpt/49financial/platinum/reporting/`, and the same on another firm's bucket DENIED.
7. **Do NOT close any ledger** (the issuer closes it after reading your record). **Write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB247-1_release_record.json` with exactly the keys the checks read: `gates` (`packet_sha256_prefix` `7daa29f0fe10`, `addendum_1_blob` `9462b5ad35af646c96ede013f03d4449e8815033`, `addendum_2_blob` `b5c303ea69ffa4195ec441d455d9f1978c327678`, `all_halves_signed`, `hop2_ledger_closed`, `one_change_at_a_time`, `open_deploys_worktrees_read`, `before` {`read_function_sha256`, `export_function_sha256`, `report_route_absent`}); `h3` (`function`, `built_sha256`, `after_sha256`, `route`, `route_present_after`, `existing_routes_changed`, `plan` {`add`,`change`,`destroy`,`resources`}); `h4a` (`function`, `built_sha256`, `after_sha256`, `sha256_before`, `pass_switch_unchanged`); `h4b` (`fence_row` {`second_row_present`,`regenerated_and_read_back`}, `role_statement_before` `absent`, `plan`, `statements_added`, `statements_removed`, `statement` {`effect`,`actions`,`resource`}, `replan_changes`); `counters` (`rollback_performed`, `console_edits`, `put_role_policy_calls`, `switch_changes`, `other_roles_changed`, `second_firm_prefixes`). Where Step 6 has not run (no second GO), write `h4b` with `fence_row.second_row_present` false and report that AC3 is owed.
8. **Run the three criteria below from the repository root** (record each output and exit code verbatim in `IB247-1_criteria_output.txt`), write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with explicit paths. Report once, under 150 words; report each STOP at once.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB247-1-AC1" cell_refs="IB-pr-616"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r247/p247_cells.py" . IB247-1-AC1</invocation><expect>IB247-1-AC1 PASS</expect></criterion>
<criterion id="IB247-1-AC2" cell_refs="IB-pr-616"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r247/p247_cells.py" . IB247-1-AC2</invocation><expect>IB247-1-AC2 PASS</expect></criterion>
<criterion id="IB247-1-AC3" cell_refs="IB-pr-616"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r247/p247_cells.py" . IB247-1-AC3</invocation><expect>IB247-1-AC3 PASS</expect></criterion>

<expected_criteria>IB247-1-AC1, IB247-1-AC2, IB247-1-AC3</expected_criteria>

What the checks grade: AC1 the signed bytes of the pair and both addenda, hop 2's ledger closed, the BEFORE state equal to this order's, the worktree union of `.open_deploys` printed; AC2 hop 3 and hop 4a: each plan as named, each function at its built zip, the report route present, no existing route changed, the switch untouched; AC3 hop 4b: the fence row read back first, exactly one statement added with the two read actions on the one resource, a clean re-plan, the counters at zero, no rollback.

## BOUNDS

- **Grant:** the reporting-read root (`infra/aws/terraform/investor-reporting/reporting-read`) and the export root (`infra/aws/terraform/investor-reporting/export/b1_submit.tf` for the one edit), `.tools/safe-apply.sh` on saved plans, `lambda-source-map.json` through the repo's deploy-stamp tool, the S3 uploads of the two function bundles at the source map's keys, `iam simulate-principal-policy`, reads of the API, the functions and the fence, your record folder, the change-management directory and its sentinel. **NO** edit of `handler.py`, `publisher.py`, the `reporting-publish` root or `sources.json` (they are `~D2`'s); **NO** touch of the filled-report switch, the schedule, any other role or route; **NO** call of the new route with a real client; **NO** write to any `filled_report.json`; **NO** second firm's prefix; **NO** console edit and no `put-role-policy`.
- **Refusal clause:** STOP and report, writing nothing further, on any of: a byte of the pair or addenda that differs; a CTO half not SIGNED; hop 2's ledger OPEN; an open ledger or marker on a named function, root or role; a BEFORE value that differs; a plan that is not the one named for its step (any destroy, any existing route, authorizer or integration changed); an existing grant on the filled object; the fence row not at HEAD or not regenerated and read back (Step 6 only); an AFTER simulate arm that differs. A bound in a CTO half is raised only by a CTO half.
- **Rollback, per key:** the route resource and its local; the read bundle back to `WjnDxvu2...`; the export bundle back to `5/9LZBbT...`; the one IAM statement (revert the single edit, `safe-apply`, read the simulate arms back equal to BEFORE). The fence row is the CRO lane's and the laptop's; do not touch it.
- **Row ids** `IRPT_BCKEND-D2-IB2-S<k>` or the next free `D2-S<k>` the gate accepts; file a row for anything odd and keep working. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/investor-reporting/reporting-read/
infra/aws/terraform/investor-reporting/export/b1_submit.tf
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-616.apply-pair-551-hops-3-and-4.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 242 (round 7, workstream ~PS), cell `IB-pr-616`.
<owned_cells>IB-pr-616</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB247-1-AC1, IB247-1-AC2, IB247-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-616.apply-pair-551-hops-3-and-4.proof_of_spec.json` (the file stem of this order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- `comp-blast irpt-49f-reporting-read-lambda` and `comp-blast irpt-export-render` on dell2 2026-10-16 ~21:3xZ (graph vintage 2026-10-16T21:03:04Z): the read function reaches `opal-users-v2` and the served-guard event rules; the export function reaches `irpt-requests`, `opal-users-v2`, `opal-news-trending-daily` and its event rules. Both are additive here: one new route and new code, no existing consumer's contract changes. The only new property reached is one platinum object name family in 49 Financial's bucket (Step 6).
comp-iam: RUN -- `comp-iam service irpt-export-render` 2026-10-16: role `irpt-export-render-role`, 29 statements declared in `export/iam.tf`; the new statement is the one named in Step 6, read-only on one object-name family, sitting behind the second fence row (ADDENDUM 2).
comp-routes: RUN -- `comp-routes api-routes` 2026-10-16: 34 lines, none naming `reporting/client`; the reporting API's routes are the API Gateway resources of `reporting-read/api.tf`, and the AWS graph (vintage 2026-10-16T18:42:02Z, API `7k3ed8px20`) holds the `/summary` route and no `/report` route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched; the new route is on the existing scoped API behind the existing edge pattern.
comp-adversary: RUN -- p247_cells.py IB247-1 dry-run at the base on dell2 2026-10-16 ~21:3xZ: AC1, AC2, AC3 each FAIL (no record). The control (control247.py, in temp roots the run built itself from the real signed documents and a synthetic record) passes the three positives and each of 13 negatives (the no-record case included) fails its own arm: 0 unexpected.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class WORLD. STAGED: not issued for work until the GO.
</preflight>
