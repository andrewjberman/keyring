# TO IRPT_BCKEND.TO-IB-pr-349 -- EMERGENCY release of irpt-export-render at pin b921635dad: export reads fail closed and every admitted read is logged (IB-pr-343), by hash, laptop applier

<to_id>IRPT_BCKEND.TO-IB-pr-349</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~I</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete -- flipped by issuer 2.0.0_SA_COO~P2 on IB68-1-AC1 PASS (amended criterion, AMENDMENT 1 @b883510cd9) and proof VALID, both re-run by the issuer at dell2 HEAD 581ccf5454; legs 4-5 OPEN-BY-DESIGN, discharged by the first real Opal export (row S382)</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (the applier is a laptop seat; the issuer is on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 525
(a non-zero reach is a security exception) and msg 590 ruling, option (a); MSTR ruling 106243 (msg 589) names this applier | **Decomp
cell:** `IB-pr-349` (decomposition section 61) | **outcome_ref:** FWD-2 (rows W142-S4 / W146-S1 / W148-S1) | **depends_on:** IB-pr-343 and
IB-pr-347 (both drained).

---

## WORKER FACE

**Why this is an emergency.** The live `irpt-export-render` admits an export read whose receipt names no account (row W142-S4).
IB-pr-347 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~148/IB67-1_export_reach.json`) measured **7 non-Opal
principals** who can call that read directly through the API. The fix is IB-pr-343. It is in the code but not deployed, because dell2
has no terraform. You release it from the laptop, BY HASH.

**The two halves. Step 0 reads both at the published HEAD; nothing applies on one half.**
- CTO: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_343_EXPORT_FAIL_CLOSED_EMERGENCY_CTO_HALF.md`
  @adaf13fec6, plus AMENDMENT 1 @4493cf1800.
- COO: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_343_EXPORT_FAIL_CLOSED_EMERGENCY_COO_HALF.md`.
- They bound the act: one function, `irpt-export-render`, at pin `b921635dad`, and exactly nine changed members.

**What you do** (from a checkout of the published branch carrying `b921635dad`; the commit must be an ancestor of your HEAD -- print
`git merge-base --is-ancestor b921635dad HEAD` rc):

0. **Read both halves.** Print each path and its commit. If either is absent, STOP.
1. **Census at the pin.** Run `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin b921635dad`.
   - It must print `changed_members=9`, naming exactly: entry.py, receipt.py, bundle.py, finalize_on_read.py, handler.py,
     retained_export.py, narrative_submit.py, submit_service.py, submit_installed.py.
   - Print the live CodeSha256. The COO half read `exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg=`; if it moved, STOP and file a row.
   - Any other member set: STOP and file a row.
2. **Ledger.** Open a change-management entry: `python .tools/deploy_ledger.py open ...` under
   `org/critical_paths/change_management/`. COMMIT its sentinel `org/critical_paths/.open_deploys/<slug>.json` immediately. Name the
   pre-release S3 object version of the function's artifact: that is the rollback source.
3. **Build and apply.**
   - Build: `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render` from a tree at `b921635dad` or a descendant whose census
     is unchanged. Print the `key=` line and the built sha256.
   - Plan the root `infra/aws/terraform/investor-reporting/export` with `.tools/terraform.exe`. The plan changes ONLY the function's
     code and object version; `0 to destroy`.
   - Apply with `.tools/safe-apply.sh` from the saved planfile. Never `aws lambda update-function-code`.
4. **After-reads. Write every result to `IB68-1_release_after_reads.json` in your deliverables folder.**
   1. Deployed CodeSha256 equals the built sha. A re-plan reads 0 changes.
   2. The live `entry.py` member's sha256 starts `fc241d806ecc` (download the live zip from `get-function` Code.Location).
   3. **Negative:** read an existing, un-back-filled export as an admin principal. It answers the refusal (NOT_AUTHORIZED, "names no
      covered account"), not the PDF.
   4. **Positive:** submit a NEW export and read it back as an Opal principal whose scope covers its accounts. It reaches READY, and one
      `irpt_export_read_admitted` log line appears with its covered account ids.
   5. **Positive:** a performance export and an analysis export each reach READY.
   6. **The outside path is refused:** reconstruct one of the 7 principals' path offline, the way IB-pr-347 did, and run it through
      the DEPLOYED bytes against an export whose receipt names no account. It is refused. Use an opaque id only; mint no token for an
      outside principal.
   7. An admitted Opal caller is still served (item 4 counts).
   8. Close the ledger entry and commit it before the grading read.
5. **Branch B.** If after-read 1 or 4 fails, roll back the same turn: a targeted apply to the pre-release S3 version, verified by
   CodeSha256. File a BLOCKING row. Set `rolled_back: true`.

The JSON keys: `pin`, `census_changed_members` (list), `built_sha`, `replan_changes`, `live_entry_sha256`, `existing_export_refused`,
`new_export_ready`, `admitted_read_log_lines`, `performance_ready`, `analysis_ready`, `outside_principal_refused`, `opal_caller_served`,
`ledger_closed`, `rolled_back`, `rollback_source_version`, `limits`. Opaque ids only: no names, emails or raw account numbers.

**AMENDMENT 1 (2026-10-07 ~15:2xZ, issuer `2.0.0_SA_COO~P2`, on row S382 and CTO REC msg 757).**
- **The exposure is graded on the controls already proven against the deployed bytes:** an existing receipt is refused for an admin
  and for a non-Opal principal, an Opal read is admitted, and there is no blanket deny.
- **After-reads 4 and 5 (new, performance and analysis exports READY; the admitted-read log line) are OPEN-BY-DESIGN.** No
  authenticated Opal principal exists to submit a new export without writing `opal-users-v2`, which this order forbids. Do NOT
  mint a principal.
- **In `IB68-1_release_after_reads.json`:** write `"OPEN-BY-DESIGN"` for `new_export_ready`, `performance_ready` and
  `analysis_ready`. Write `open_leg_discharge`: "the first real Opal export (Andrew's or an Opal user's) read with its
  irpt_export_read_admitted line; the issuer records it on row S382". `admitted_read_log_lines` may be 0.
- **Then close the ledger.** The open legs are named in the ledger entry. The check file carries the same amendment.

<criterion id="IB68-1-AC1" cell_refs="IB-pr-349"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r68/p68_cells.py" . IB68-1-AC1</invocation><expect>IB68-1-AC1 PASS</expect></criterion>
`IB68-1-AC1` -- the after-reads file holds: pin b921635dad; exactly the nine members; built == live CodeSha256 (re-read live by the
check); replan 0; the live entry.py is fc241d806ecc; the existing export refused; the new, performance and analysis exports READY with an
admitted-read line; the outside path refused and the Opal caller served; ledger closed; not rolled back. Base: FAIL (no file).

<expected_criteria>IB68-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder, and nothing else.
- **No apply on one half, and none at any pin but `b921635dad`** (or a descendant whose census is unchanged). `34f71024a1` is REFUSED:
  its build omits the fix.
- **The source map** may move only on the irpt-export-render entry, and only by the build and `record-terraform-deploy.sh` (artifact
  and deploy fields). Never edit a `staged_from` row.
- **The only served change** is `irpt-export-render`'s code. No IAM, route, authorizer, table, bucket or other function changes. No
  write to the auth plane. No token minted for a non-Opal principal.
- **No vendor call.** No call off Opal infrastructure. No monitor, alarm, SNS or SES send.
- **NEVER-2.** The ledger is opened before the act and closed after it; the sentinel is committed.
- **Refusal clause.** A census that differs from the nine members, a moved live CodeSha256, a plan that destroys or touches any other
  resource, or a name/email/raw account number in any file: STOP, file a row, apply nothing.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-349.emergency-release-export-reads-fail-closed.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~I/
infra/aws/terraform/investor-reporting/export/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 61 (round 68, workstream ~P), cell `IB-pr-349`.
<owned_cells>IB-pr-349</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: IB68-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~I/IRPT_BCKEND.TO-IB-pr-349.emergency-release-export-reads-fail-closed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P2`: the commit hashes, the built sha and live CodeSha256, IB68-1-AC1's last line, the ledger
entry, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at b921635dad: 9 changed members of 63, one function (irpt-export-render), the only function the source map packages from export/; both halves sign this set.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route, authorizer or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB68-1-AC1 dry-run at base b921635dad 2026-10-07 ~13:2xZ: FAIL as expected (no after-reads file).
lane: the <paths> block IS the grant.
</preflight>
