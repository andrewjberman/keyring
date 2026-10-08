# TO IRPT_BCKEND.TO-IB-pr-368 -- the IB-pr-367 release applied at pin a0d8d4943f (irpt-export-render: repository.py + retention.py), with a retained-read regression check before and after

<to_id>IRPT_BCKEND.TO-IB-pr-368</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~176</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>81</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** both never-widen halves of IB-pr-367 (COO @764a0abf3c, CTO @275e506034) and
CTO ADDENDUM 5 (msg 1408: release first) | **Decomp cell:** `IB-pr-368` (decomposition section 74) | **outcome_ref:** FWD-8 / CUSTDY hop 5
| **depends_on:** IB-pr-367 (drained @9a594e96a8).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-176` (branch `wk-IRPT_BCKEND-176`). Work, build and commit only there; NEVER build in
`C:/dev/ajb_workspace` (row D2-S3). Paths below are relative to your worktree.

**What this is.** Two signed halves bound one act: release `irpt-export-render` built at pin `a0d8d4943f`. Only two packaged members
change: `repository.py`, which gains the CUSTODY_REPORT kind, and `retention.py`, which takes the policy revision.
- **The halves.** Read all three at your HEAD first; if any is absent, STOP.
  - Packet: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~175/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-367.md`. Its blob
    must be `aa9115a66f459f89ec970a60998cd26be23cc310`.
  - COO half: `.../deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_367_CUSTODY_KIND_COO_HALF.md`.
  - CTO half: `.../deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_367_REPOSITORY_REPIN_CTO_HALF.md`.
- **The custody after-reads are NOT this order's.** They move to a later order, after E8 (`~M2`'s policy family) and IRPT_CUSTDY E2 (CTO
  half).

**Steps.**

0. **Start reads.**
   - Print `git merge-base --is-ancestor a0d8d4943f HEAD` rc (must be 0).
   - Print the live CodeSha256. It must be `03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc=`; otherwise STOP.
   - `git status --porcelain` must be empty.
1. **Census.** `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin a0d8d4943f` must print `changed_members=2`:
   `repository.py` and `retention.py`. Anything else: STOP.
2. **PRE-READ (the regression baseline), before anything is applied.**
   - Find one EXISTING retained ANALYSIS or PERFORMANCE report that `irpt-export-render` reads by reference, through one of its own READ
     operations (one that resolves a retained report through `repository.get`, e.g. the export receipt or download of an existing
     export). Read the code to choose it.
   - Read it back through the DEPLOYED function by direct invoke (`aws lambda invoke`) with an API-shaped event for an Opal
     principal. This is the CTO's path 1 in ADDENDUM 3: the function decrypts, and no new grant is used.
   - Record `report_kind`, `report_id`, `revision`, an `outcome` string, `ok`, and the `body_sha256` of the returned document or payload.
   - **Never call a write operation** (no submit, no create).
   - If no such report exists, or the function refuses every direct-invoke shape you can build from the code, STOP. File a row naming
     what you found. Apply nothing.
3. **Ledger (NEVER-2).** Open an entry with `python .tools/deploy_ledger.py open ...`, and commit its `.open_deploys` sentinel at once. The
   rollback source is S3 version `FHKz88vjxHfi5uqADSw5GlQq8IULm615`.
4. **Build and apply.**
   - Build: `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render` from your clean tree. Print the `key=`
     line and the built sha256. It must equal the packet's `idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8=`; otherwise STOP.
   - Plan `infra/aws/terraform/investor-reporting/export` with `.tools/terraform.exe` to a planfile. Only the function's code and object
     version may change, with `0 to destroy`.
   - Commit the plan text (`terraform show -no-color`) to your deliverables. Then apply with `bash .tools/safe-apply.sh` from that
     planfile.
   - If the tag-authz gate refuses, `TAGAUTHZ_OVERRIDE` is no longer authorized: S334 is fixed at fad269226b. STOP and file a row.
   - Re-read the live CodeSha256: it must equal the built sha. Re-plan: 0 changes. Census: `changed_members=0`.
   - The build stages copies into the source dir. Remove that residue so your tree is clean again.
5. **POST-READ.** Repeat step 2's read with the same reference and event. It must be `ok`, with the same `report_id`, `revision` and
   `body_sha256`.
6. **Close the ledger** and commit it.
7. **Branch B.** If step 4's live sha or re-plan fails, or step 5 fails (a TypeError, any refusal, or a different body):
   - redeploy version `FHKz88vjxHfi5uqADSw5GlQq8IULm615` through the Terraform path the same session;
   - verify CodeSha256 is `03p2eIEK...` again;
   - file a BLOCKING row;
   - write `rolled_back: true`;
   - close the ledger.

**After-reads file:**
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~176/IB81-1_release_after_reads.json`.
- Keys: `pin`, `census_changed_members` (list), `start_live_codesha`, `built_sha`, `build_tree_clean`, `post_census_changed_members`,
  `replan_changes`, `pre_read`, `post_read`, `type_error`, `ledger_entry`, `ledger_closed`, `rolled_back`, `rollback_source_version`,
  `limits`.
- `pre_read` and `post_read` each hold `{report_kind, report_id, revision, outcome, ok, body_sha256, operation}`.
- Use opaque ids only: no names, emails or raw account numbers.

**AMENDMENT 1 (2026-10-08 ~19:5xZ, issuer `2.0.0_SA_COO~P2`, on row D2-W176-S1 and the CTO half's AMENDMENT 1 @49efddd80c, msg 1423).**
Steps 2 and 5 (the live pre-read and post-read) are REPLACED: `irpt-export-render` has no read route for a retained ANALYSIS or
PERFORMANCE report. In their place, BEFORE step 3 (the ledger):
- **Offline differential replay.**
  - Unzip the LIVE zip (from `get-function` Code.Location) and the BUILT zip (`BUILD_ONLY=1` at the pin, from your clean tree; it
    must equal the packet's `idanP8nX...`) into two empty directories.
  - In one offline process per zip (python `-I`), reserve ONE ANALYSIS or PERFORMANCE fixture under `irpt-x10-v1` through the LIVE
    zip's code path, with in-memory index and blob fakes and the HEAD registry policy row.
  - Read that same fixture back through `repository.get` in each zip.
  - Pass: both ok; neither raises nor refuses; identical result bytes (`result_sha256`).
- **Negative control.** Alter the fixture's `policy_sha256`. Both zips must refuse it.
- **Suites.** `reports/tests/test_repository.py`, `test_retained_repository.py` and `test_retention.py` pass, each in its own process.
- **Commit the record before the apply.** The record is the after-reads file's `replay` object:
  `{fixture_family, policy_revision, reserved_by: "live", live: {ok, raised, refused, result_sha256}, built: {...}, negative_control:
  {live_refused, built_refused}, suites: {path: last line}, replay_commit}`. Commit it, then open the ledger and record
  `ledger_open_commit` in the file.
- AC1 keeps its meaning. AC2 now grades the replay (check amended in the same commit). Drop `pre_read`, `post_read` and `type_error`.
- If the replay fails: STOP before the apply and file a row.
- Gate limb: none graded this amendment (a modification; GATE viii only).

<criterion id="IB81-1-AC1" cell_refs="IB-pr-368"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r81/p81_cells.py" . IB81-1-AC1</invocation><expect>IB81-1-AC1 PASS</expect></criterion>
`IB81-1-AC1` -- pin a0d8d4943f, exactly the two members, the start sha equal to the rollback target, built == the packet's sha == live
(re-read live), census 0, re-plan 0, a clean build tree, the ledger closed, and no rollback. Base: FAIL (no file).

<criterion id="IB81-1-AC2" cell_refs="IB-pr-368"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r81/p81_cells.py" . IB81-1-AC2</invocation><expect>IB81-1-AC2 PASS</expect></criterion>
`IB81-1-AC2` -- one existing retained ANALYSIS or PERFORMANCE report is read back by reference before and after, ok both times, with
the same id, revision and body, and no TypeError. Base: FAIL (no file).

<expected_criteria>IB81-1-AC1, IB81-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and nothing else.
- **The only served change** is `irpt-export-render`'s code. No route, IAM, table, bucket, policy registry or other function. No write to
  any data plane: reads only, through the function's own read operations.
- **The source map** moves only on the `irpt-export-render` entry, through the build and `record-terraform-deploy.sh` (artifact and
  deploy fields). Never edit a `staged_from` row. If the recorder also writes `infra/aws/terraform/investor-reporting/CHANGELOG.json`,
  that path is granted.
- **No vendor call.** No call off Opal infrastructure. No monitor, alarm, SNS or SES send.
- **Refusal clause.** A moved start sha, a census other than the two members, a built sha other than the packet's, a plan that destroys
  or touches anything else, a refused or changed read-back, or a name, email or raw account number in any file: STOP, file a row, apply
  nothing more (Branch B if already applied).
- **Row ids** are `IRPT_BCKEND-D2-W176-S<k>`. Re-read the channel right before you append. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~176" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~176@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~176 <0.9.0_WK_IRPT_BCKEND~176@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-368.custody-kind-release-applied.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~176/
infra/aws/terraform/investor-reporting/export/
infra/aws/terraform/investor-reporting/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 74 (round 81, workstream ~P), cell `IB-pr-368`.
<owned_cells>IB-pr-368</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB81-1-AC1, IB81-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~176/IRPT_BCKEND.TO-IB-pr-368.custody-kind-release-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit hashes, the built and live CodeSha256, the read-back operation and report kind used, each
criterion's last line, the ledger entry, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at a0d8d4943f (issuer re-run, IB80-1-AC1): 2 changed members of 64, one function (irpt-export-render); retention.py changes every retained read, hence the CTO half's pre/post read-back.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added or changed; the read-back uses the function's own role by direct invoke (ADDENDUM 3 path 1).
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p81_cells.py dry-run at base ea6b96a66a on dell2 2026-10-08 ~19:0xZ: IB81-1-AC1 FAIL, IB81-1-AC2 FAIL (no file).
lane: the <paths> block IS the grant. Dell apply authority: step C (msgs 1288/1297); irpt-export-render is not among the ten protected functions; the before-rule's four classes are not touched.
</preflight>
