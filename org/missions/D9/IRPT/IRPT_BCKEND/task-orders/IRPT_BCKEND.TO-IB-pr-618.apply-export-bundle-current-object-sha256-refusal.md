# TO IRPT_BCKEND.TO-IB-pr-618 -- APPLY the new irpt-export-render bundle that reads the CURRENT filled-report object and refuses on a sha256 or size mismatch (code attributes only), BEFORE the fence row regeneration and the IB-pr-616 Step 6 statement (IB-pr-551 ADDENDUM 3; CTO ruled (B), msg 10126)

<to_id>IRPT_BCKEND.TO-IB-pr-618</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~S2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair IB-pr-551 as amended by ADDENDUM 3 (`deliverables/2.0.0_SA_COO~S2/NEVER_WIDEN_IB_pr_551_ADDENDUM_3_GETOBJECT_ONLY_SHA256_REFUSAL_COO_HALF.md`, git blob `87a46d9cf370c293dae46a413cba213db721b5ef`, CTO half signed @94032d0bb7), which names this bundle as the first of three things that must be live before the statement; the same release plan as IB-pr-616 (`deliverables/2.0.0_SA_COO~S2/IB_pr_551_HOPS_3_4_RELEASE_PLAN_BEFORE_STATE_20261016.md`). The build behind it: IB-pr-617 and IB-pr-619, merged at `1dab1295ef`.

This order is a sibling of IB-pr-616 on the same two ledgers' subject, and it carries NO IAM change. It does not replace Step 6 of IB-pr-616: that step still waits for its own second GO.

---

## WORKER FACE

**Cell `IB-pr-618` (inlined).** `irpt-export-render` today runs the bundle you applied in IB-pr-616 Step 5; its `read_pinned_filled` reads the pinned VersionId (live CodeSha256 `5bIgn/MLNgtNtDnRpmE3OejAMw2IpoJBmzzRfHvFLXI=`). The role will be granted `s3:GetObject` ONLY on the filled object, never `s3:GetObjectVersion`, so that code must not stay live. `infra/aws/lambda/investor-reporting/export/retained_export.py` at HEAD now reads the CURRENT object and raises a worded refusal when its sha256 or size differs from the pin ("the filled report for this client changed after this export was submitted ... open the report again and resubmit"). Apply that code to the function, code attributes only. The filled-report switch, the schedule, the environment and the role are NOT touched.

**Do, in this order. A STOP is reported to the issuer at once and writes nothing further.**

1. **Gates, read only.** (a) `git hash-object` of ADDENDUM 3's COO half equals `87a46d9cf370...`; the CTO half (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_551_SERVE_PATH_HOPS_2_4_CTO_HALF.md`) reads SIGNED for the pair and ADDENDUM 1, 2 and 3 at those bytes. (b) **One change at a time:** read `.open_deploys/` in EVERY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), union them, print `worktrees_read` and `marker_files_read`. The ONLY open ledger naming `irpt-export-render` or `irpt-export-render-role` is `irpt-bckend-serve-path-hops-3-4a-report-route-export-bundle-20261017` (IB-pr-616's, L1 to L6 closed, L7 open, the IAM leg owed); any other open ledger or marker naming the function, its root `export`, or the role is a STOP. (c) The live BEFORE equals `5bIgn/MLNgtNtDnRpmE3OejAMw2IpoJBmzzRfHvFLXI=` (`aws lambda get-function-configuration --function-name irpt-export-render`, read only); count the environment variables and print the count. A different value is a STOP and a re-cut.
2. **Ledger.** Do NOT open a second ledger for the function: record this order's leg in the existing entry `irpt-bckend-serve-path-hops-3-4a-report-route-export-bundle-20261017` (an addition under `python .tools/deploy_ledger.py`, its own note line naming IB-pr-618 and the build commit), and commit nothing that closes it. If the tool refuses a note on an entry another order opened, STOP and report.
3. **Build.** From HEAD, through the repo's builder for the export function (BUILD_ONLY first; write the pins the builder demands before the build, the builder only verifies). Record the build commit (`git rev-parse HEAD` at build time), the git blob of `retained_export.py` that went into the zip (`git rev-parse HEAD:infra/aws/lambda/investor-reporting/export/retained_export.py`), the built zip's base64 sha256, and an import smoke in a fresh directory (rc 0). The build commit must be at or after `1dab1295ef`. Upload ONE new version at the source map's `artifact_s3_key`, built == landed.
4. **Plan and apply.** `terraform plan` on `infra/aws/terraform/investor-reporting/export` to a planfile: exactly 0 add / 1 change / 0 destroy, the one being the function's code attributes (`source_code_hash` and its S3 version); nothing on the role, the policy, the schedule or the environment. Anything else: STOP, change nothing. `bash .tools/safe-apply.sh` on that planfile. Never a bare apply, never a console edit.
5. **After-read.** Re-plan reads 0 changes. The live CodeSha256 equals the built zip's base64 sha256 and differs from the BEFORE. The environment variable count equals the BEFORE count and the filled-report switch is unchanged (print the variable's value before and after, or its absence). Do NOT invoke the function and do NOT call any route: nothing writes `filled_report.json` yet.
6. **Stamp.** `infra/aws/lambda/ci/lambda-source-map.json` is retired; on this box the stamps are `infra/aws/lambda/ci/function-map/<function>.json`. Its two entries for this release still hold the PRE-release shas (read function `WjnDxvu2...`, export `5/9LZBbT...`, the drain deleted the stamps your Steps 3 and 5 wrote). Through the repo's stamp tool, record (a) `irpt-export-render` at the new built sha, and (b) `irpt-49f-reporting-read-lambda` at its live CodeSha256 `z634S2QsrfCpY4c3cD2UGwicdmLDo6/Rmng8SrEskCQ=` (read it live first; it is IB-pr-616 Step 3's, still the live value). Write `apply.stamp_file` `function-map` and `apply.read_stamp_sha256` (the value now in the read function's entry). If the tool refuses, STOP and report instead of editing a file by hand.
7. **Do NOT close any ledger** (the issuer closes it after reading your record). **Write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB250-1_bundle_record.json` with exactly the keys the checks read: `gates` (`addendum_3_blob` `87a46d9cf370c293dae46a413cba213db721b5ef`, `all_halves_signed`, `ledger_616` {`l1_to_l6_closed`, `l7_open_by_design`}, `one_change_at_a_time`, `open_deploys_worktrees_read` (an integer), `before` {`export_function_sha256`}); `build` (`commit`, `retained_export_blob`, `built_sha256`, `import_smoke_rc`); `apply` (`plan` {`add`,`change`,`destroy`,`resources` (a list of one)}, `after_sha256`, `replan_changes`, `env_vars_before`, `env_vars_after`, `switch_changes`, `stamp_file`, `read_stamp_sha256`); `counters` (`rollback_performed`, `console_edits`, `invokes`, `iam_changes`). Never write a run of nine or more digits in the record (the check refuses it): write account numbers and ids truncated.
8. **Run the three criteria below from the repository root** (record each output and exit code verbatim in `IB250-1_criteria_output.txt`), write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with explicit paths. Report once, under 150 words; report each STOP at once.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB250-1-AC1" cell_refs="IB-pr-618"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r250/p250_cells.py" . IB250-1-AC1</invocation><expect>IB250-1-AC1 PASS</expect></criterion>
<criterion id="IB250-1-AC2" cell_refs="IB-pr-618"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r250/p250_cells.py" . IB250-1-AC2</invocation><expect>IB250-1-AC2 PASS</expect></criterion>
<criterion id="IB250-1-AC3" cell_refs="IB-pr-618"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r250/p250_cells.py" . IB250-1-AC3</invocation><expect>IB250-1-AC3 PASS</expect></criterion>

<expected_criteria>IB250-1-AC1, IB250-1-AC2, IB250-1-AC3</expected_criteria>

What the checks grade: AC1 the signed bytes of ADDENDUM 3, the ledger of IB-pr-616 in its by-design state, one change at a time, the BEFORE equal to this order's; AC2 the build commit is an ancestor of HEAD, the zip holds that commit's `retained_export.py`, and its `read_pinned_filled` passes no `version_id` and keeps the sha256 refusal; AC3 the plan 0/1/0 on the one function, the live CodeSha256 equal to the built zip, a clean re-plan, the environment untouched, no invoke, no IAM change, no rollback.

## BOUNDS

- **Grant:** the export root (`infra/aws/terraform/investor-reporting/export/`) for the plan and apply only, with NO edit of any `.tf` file; `.tools/safe-apply.sh` on a saved plan; the deploy stamps through the repo's tool; the S3 upload of the one function bundle at the source map's key; reads of the function, the repo and the ledgers; your record folder; the change-management directory and its sentinel. **NO** edit of any source file (the code is already merged); **NO** IAM change, no `put-role-policy`; **NO** touch of the filled-report switch, the schedule, any other function, role or route; **NO** invoke of the function; **NO** call of any route; **NO** write to any `filled_report.json`; **NO** console edit.
- **Refusal clause:** STOP and report, writing nothing further, on any of: a byte of ADDENDUM 3 that differs; a CTO half not SIGNED; another open ledger or marker naming the function, its root or its role; a BEFORE value that differs; a plan that is not 0 add / 1 change / 0 destroy on the function's code attributes; a build commit before `1dab1295ef`; a stamp tool refusal. A bound in a CTO half is raised only by a CTO half.
- **Rollback:** the export bundle back to the one at `5bIgn/MLNgtN...` (the previous S3 version at the source map's key, re-applied through `safe-apply`); read the live CodeSha256 back equal. No other key moves.
- **Row ids** `IRPT_BCKEND-D2-IB2-S<k>` or the next free `D2-S<k>` the gate accepts; file a row for anything odd and keep working. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/investor-reporting/export/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/function-map/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-618.apply-export-bundle-current-object-sha256-refusal.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 245 (round 10, workstream ~PS), cell `IB-pr-618`.
<owned_cells>IB-pr-618</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB250-1-AC1, IB250-1-AC2, IB250-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-618.apply-export-bundle-current-object-sha256-refusal.proof_of_spec.json` (the file stem of this order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- `comp-blast irpt-export-render` on dell2 2026-10-16 (graph vintage 2026-10-16T21:03:04Z), carried from IB-pr-616: the function reaches `irpt-requests`, `opal-users-v2`, `opal-news-trending-daily` and its event rules. This apply changes its code only; the new code is stricter (a changed filled object is refused) and reads one object family the role cannot yet read, so no filled-report export can succeed until Step 6 of IB-pr-616 lands; the switch is OFF, so no export takes that path today.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed in this order; the one statement is IB-pr-616 Step 6, held.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p250_cells.py IB250-1 dry-run at the base on dell2 2026-10-17: AC1, AC2 and AC3 each FAIL (no record). A synthetic record with the real signed documents and the real build commit passes the three; each of the negatives named in the issuance commit fails its own arm.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class WORLD (an `infra/` path and a deploy).
</preflight>
