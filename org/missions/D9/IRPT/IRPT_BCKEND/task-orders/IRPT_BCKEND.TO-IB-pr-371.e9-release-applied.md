# TO IRPT_BCKEND.TO-IB-pr-371 -- E9 released at pin 0a57f3c0e9 (irpt-export-render: per-family policy revisions, five members) with the offline differential replay before the apply

<to_id>IRPT_BCKEND.TO-IB-pr-371</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~179</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>84</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** both never-widen halves of IB-pr-370 (COO @4e3ead72a3, CTO @c086ec4c2b) and CTO msg
1536 ("release E9 now") | **Decomp cell:** `IB-pr-371` (decomposition section 77) | **outcome_ref:** FWD-8 / CUSTDY hop 5 |
**depends_on:** IB-pr-370 (drained @a1f2d9f43c).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-179` (branch `wk-IRPT_BCKEND-179`, cut from `box/dell2`). Work, build and commit only there.
NEVER build in `C:/dev/ajb_workspace`. Paths below are relative to your worktree. This order follows IB-pr-368's shape (with its
AMENDMENT 1), which ran clean: read `task-orders/IRPT_BCKEND.TO-IB-pr-368.custody-kind-release-applied.md` and its deliverables
(`deliverables/0.9.0_WK_IRPT_BCKEND~176/`) for the replay method.

**What this is.** Release `irpt-export-render` built at pin `0a57f3c0e9`. Five packaged members change:
- `repository.py`, `composition.py`, `submit_installed.py`: IB-pr-369, the per-family revisions;
- `infra/logic/registry/reporting_policies.json`: E8, `irpt-custody-x10-v1` PENDING;
- `lib/opal_naming.py`: b77e2af4d5.

**Custody stays refused after this release** (the row is PENDING). That is expected: the ACTIVE row rides E10.

**The halves.** Read all three at your HEAD first; if any is absent, STOP.
- Packet: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~178/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-370.md`. Its blob must
  be `1d5120c14b2231b33d8adf3dc5f7a5b186519f67`.
- COO half: `.../deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_370_E9_RELEASE_COO_HALF.md`.
- CTO half: `.../deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_370_E9_CTO_HALF.md`.

**Steps.**
0. **Start reads.**
   - `git merge-base --is-ancestor 0a57f3c0e9 HEAD` rc must be 0.
   - Live CodeSha256 must be `idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8=`; otherwise STOP.
   - `git status --porcelain` must be empty.
1. **Census.** `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin 0a57f3c0e9` must show exactly the five members.
   Anything else: STOP.
2. **BUILD_ONLY** (`BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render`). The built sha
   must equal the packet's `PbyqmHBQpr4DC76qt0noBfoqKVleydNaJ7s2qsx5mT0=`; otherwise STOP.
3. **Offline differential replay, BEFORE the ledger.**
   - Unzip the LIVE zip and the BUILT zip into two empty dirs.
   - In separate `python -I` processes, reserve one ANALYSIS and one PERFORMANCE fixture under `irpt-x10-v1` through the LIVE zip's
     code path, with in-memory fakes and the registry packaged in each zip.
   - `repository.get` in each zip must give identical `result_sha256`; neither may raise or refuse.
   - Negative control: an altered `policy_sha256` must be refused by both.
   - Suites: `reports/tests/test_repository.py`, `test_retained_repository.py` and `test_retention.py` pass, each alone.
   - Commit the `replay` record (in the after-reads file) and record `replay_commit`.
   - If the replay fails, STOP before the ledger and file a row.
4. **Ledger (NEVER-2).** `python .tools/deploy_ledger.py open ...`. Commit its sentinel; record `ledger_open_commit`. The rollback
   source is S3 version `fHVzTZi4vdHmRqcy0KK1hmrQ_dcT1QkO`.
5. **Upload and apply.**
   - Run `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render` (the built sha must still equal the
     packet's).
   - Plan `infra/aws/terraform/investor-reporting/export` to a planfile: only this function's code and object version, `0 to destroy`.
   - Commit the plan text, then `bash .tools/safe-apply.sh` from that planfile.
   - Re-read live: it must equal the built sha. Re-plan: 0. Census: `changed_members=0`.
   - Record with `record-terraform-deploy.sh --function irpt-export-render`. Clean any residue.
6. **Close the ledger** and commit it.
7. **Branch B.** If step 5's equality or re-plan fails: redeploy version `fHVzTZi4...` through the Terraform path the same session,
   verify `idanP8nX...` is live again, file a BLOCKING row, write `rolled_back: true`, and close the ledger.

**After-reads file:**
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~179/IB84-1_release_after_reads.json`.
- Keys: `pin`, `census_changed_members` (list of the census's member names), `start_live_codesha`, `built_sha`, `build_tree_clean`,
  `post_census_changed_members`, `replan_changes`, `replay`, `ledger_entry`, `ledger_open_commit`, `ledger_closed`, `rolled_back`,
  `rollback_source_version`, `limits`.
- `replay` = `{fixture_family, policy_revision: "irpt-x10-v1", reserved_by: "live", live: {ok, raised, refused, result_sha256},
  built: {...}, negative_control: {live_refused, built_refused}, suites: {path: last line}, replay_commit}`. Name the ANALYSIS
  fixture as `fixture_family`, and keep the PERFORMANCE result alongside it under `extra`.

<criterion id="IB84-1-AC1" cell_refs="IB-pr-371"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r84/p84_cells.py" . IB84-1-AC1</invocation><expect>IB84-1-AC1 PASS</expect></criterion>
`IB84-1-AC1` -- pin 0a57f3c0e9, exactly the five members, the start sha equal to the rollback target, built == the packet's sha == live
(re-read live), census 0, re-plan 0, a clean build tree, the ledger closed, and no rollback. Base: FAIL (no file).

<criterion id="IB84-1-AC2" cell_refs="IB-pr-371"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r84/p84_cells.py" . IB84-1-AC2</invocation><expect>IB84-1-AC2 PASS</expect></criterion>
`IB84-1-AC2` -- the replay: an irpt-x10-v1 fixture reserved by the live path reads back with identical bytes through both zips, the
negative control is refused by both, the three suites pass, and the replay was committed before the ledger opened. Base: FAIL (no file).

<expected_criteria>IB84-1-AC1, IB84-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and nothing else.
- **The only served change** is `irpt-export-render`'s code. No route, IAM, table, bucket, policy registry content or other function.
  Reads only, apart from the release itself.
- **The source map** moves only on the `irpt-export-render` entry, through the build and `record-terraform-deploy.sh` (artifact and
  deploy fields). Never edit a `staged_from` row.
- **No vendor call.** No call off Opal infrastructure. No monitor, alarm, SNS or SES send.
- **Refusal clause.** A moved start sha, a census other than the five, a built sha other than the packet's, a failed replay, a plan
  that destroys or touches anything else, or a name, email or raw account number in any file: STOP, file a row, apply nothing more
  (Branch B if already applied).
- **Row ids** are `IRPT_BCKEND-D2-W179-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~179" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~179@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~179 <0.9.0_WK_IRPT_BCKEND~179@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. Keep scratch outside the worktree (the session scratchpad).
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-371.e9-release-applied.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~179/
infra/aws/terraform/investor-reporting/export/
infra/aws/terraform/investor-reporting/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 77 (round 84, workstream ~P), cell `IB-pr-371`.
<owned_cells>IB-pr-371</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB84-1-AC1, IB84-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~179/IRPT_BCKEND.TO-IB-pr-371.e9-release-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit hashes, the built and live CodeSha256, the replay result sha, each criterion's last line,
the ledger entry, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at 0a57f3c0e9 (issuer, IB83-1-AC1): 5 changed members of 64, one function (irpt-export-render); the replay is the regression arm for retention (CTO half @c086ec4c2b).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p84_cells.py dry-run at base c086ec4c2b on dell2 2026-10-08 ~20:1xZ: IB84-1-AC1 FAIL, IB84-1-AC2 FAIL (no file).
lane: the <paths> block IS the grant. Dell apply authority: step C (msgs 1288/1297); irpt-export-render is not among the ten protected functions; the before-rule's four classes are not touched. Worktree cut from box/dell2 (msg 1530; CTO half condition).
</preflight>
