# TO IRPT_BCKEND.TO-IB-pr-374 -- the Performance client statement writer released at pin 9238309eca (irpt-export-render function only; the route waits for the laptop IAM leg) with the replay before the apply

<to_id>IRPT_BCKEND.TO-IB-pr-374</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~182</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- flipped by issuer 2.0.0_SA_COO~P2 after AMENDMENT 1 (cell_refs IB-pr-371 -> IB-pr-374, row D2-W182-S2): worker proof re-validated VALID; IB87-1-AC1 PASS (live rNjtTwcm re-read) and IB87-1-AC2 PASS on the issuer run</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** both never-widen halves of IB-pr-373 (COO @cb29ea67bd, CTO @ece42ad420) and CTO msg
1719 ("release as is") | **Decomp cell:** `IB-pr-374` (decomposition section 80) | **outcome_ref:** FWD-8 / CUSTDY hop 5 |
**depends_on:** IB-pr-373 (drained @6303e36222).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-182` (branch `wk-IRPT_BCKEND-182`, cut from `box/dell2`). Work, build and commit only there.
NEVER build in `C:/dev/ajb_workspace`. Paths below are relative to your worktree. This order follows IB-pr-368's shape (with its
AMENDMENT 1), which ran clean: read `task-orders/IRPT_BCKEND.TO-IB-pr-368.custody-kind-release-applied.md` and its deliverables
(`deliverables/0.9.0_WK_IRPT_BCKEND~176/`) for the replay method.

**What this is.** Release `irpt-export-render` built at pin `9238309eca`: the Performance client statement writer (code kind
CUSTODY_REPORT). Five packaged members change: `entry.py`, `submit_installed.py`, `custody_persist.py` (added), `custody_write.py`
(added) (IB-pr-373), and `infra/logic/registry/reporting_policies.json` (b4d98a4fe3, `irpt-custody-x10-v1` ACTIVE).

**FUNCTION ONLY.** Do NOT apply the route `POST /api/scoped/investor-reporting/custody-report`, and do not plan or apply the `api`
root. The route waits for the laptop IAM leg (row D2-W181-S1, CTO half condition 2) and its own later order. Until both land, the
persist cannot be reached, and it fails closed if reached.

**The halves.** Read all three at your HEAD first; if any is absent, STOP.
- Packet: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~181/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-373.md`. Its blob must
  be `d7264acfc843a87112ce955198c06429a7c45266`.
- COO half: `.../deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_373_PCS_WRITER_COO_HALF.md`.
- CTO half: `.../deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_373_PCS_WRITER_CTO_HALF.md` (its conditions 2-4 bind).

**Steps.**
0. **Start reads.**
   - `git merge-base --is-ancestor 9238309eca HEAD` rc must be 0.
   - Live CodeSha256 must be `PbyqmHBQpr4DC76qt0noBfoqKVleydNaJ7s2qsx5mT0=`; otherwise STOP.
   - `git status --porcelain` must be empty.
1. **Census.** `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin 9238309eca` must show exactly the five members.
   Anything else: STOP.
2. **BUILD_ONLY** (`BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render`). The built sha
   must equal the packet's `rNjtTwcmhpNdHUV7VcO1cRPcC1wHaANm1oIP+Xvf6Ek=`; otherwise STOP.
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
   source is S3 version `LefrKSE11JIR93JOh.1RP5cSIUrqKfI_`.
5. **Upload and apply.**
   - Run `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render` (the built sha must still equal the
     packet's).
   - Plan `infra/aws/terraform/investor-reporting/export` to a planfile: only this function's code and object version, `0 to destroy`.
   - Commit the plan text, then `bash .tools/safe-apply.sh` from that planfile.
   - Re-read live: it must equal the built sha. Re-plan: 0. Census: `changed_members=0`.
   - Record with `record-terraform-deploy.sh --function irpt-export-render`. Clean any residue.
6. **Close the ledger** and commit it.
7. **Branch B.** If step 5's equality or re-plan fails: redeploy version `LefrKSE1...` through the Terraform path the same session,
   verify `idanP8nX...` is live again, file a BLOCKING row, write `rolled_back: true`, and close the ledger.

**After-reads file:**
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~182/IB87-1_release_after_reads.json`.
- Keys: `pin`, `census_changed_members` (list of the census's member names), `start_live_codesha`, `built_sha`, `build_tree_clean`,
  `post_census_changed_members`, `replan_changes`, `replay`, `ledger_entry`, `ledger_open_commit`, `ledger_closed`, `rolled_back`,
  `rollback_source_version`, `limits`.
- `replay` = `{fixture_family, policy_revision: "irpt-x10-v1", reserved_by: "live", live: {ok, raised, refused, result_sha256},
  built: {...}, negative_control: {live_refused, built_refused}, suites: {path: last line}, replay_commit}`. Name the ANALYSIS
  fixture as `fixture_family`, and keep the PERFORMANCE result alongside it under `extra`.

**AMENDMENT 1 (2026-10-08 ~22:2xZ, issuer `2.0.0_SA_COO~P2`, on row D2-W182-S2).** Both criteria's `cell_refs` read `IB-pr-371`, a
derivation defect of the issuer: the order was derived from IB-pr-371's text. They now read `IB-pr-374`, the owned cell. The criteria,
invocations and expectations are unchanged. Gate limb: none graded this amendment (a modification; GATE viii only).

<criterion id="IB87-1-AC1" cell_refs="IB-pr-374"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r87/p87_cells.py" . IB87-1-AC1</invocation><expect>IB87-1-AC1 PASS</expect></criterion>
`IB87-1-AC1` -- pin 9238309eca, exactly the five members, the start sha equal to the rollback target, built == the packet's sha == live
(re-read live), census 0, re-plan 0, a clean build tree, the ledger closed, and no rollback. Base: FAIL (no file).

<criterion id="IB87-1-AC2" cell_refs="IB-pr-374"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r87/p87_cells.py" . IB87-1-AC2</invocation><expect>IB87-1-AC2 PASS</expect></criterion>
`IB87-1-AC2` -- the replay: an irpt-x10-v1 fixture reserved by the live path reads back with identical bytes through both zips, the
negative control is refused by both, the three suites pass, and the replay was committed before the ledger opened. Base: FAIL (no file).

<expected_criteria>IB87-1-AC1, IB87-1-AC2</expected_criteria>

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
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~182" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~182@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~182 <0.9.0_WK_IRPT_BCKEND~182@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. Keep scratch outside the worktree (the session scratchpad).
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-374.pcs-writer-release-function.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~182/
infra/aws/terraform/investor-reporting/export/
infra/aws/terraform/investor-reporting/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 80 (round 87, workstream ~P), cell `IB-pr-374`.
<owned_cells>IB-pr-374</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB87-1-AC1, IB87-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~182/IRPT_BCKEND.TO-IB-pr-374.pcs-writer-release-function.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit hashes, the built and live CodeSha256, the replay result sha, each criterion's last line,
the ledger entry, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at 9238309eca (IB86-1-AC1, issuer re-run): 5 changed members, built 66 / live 64, one function (irpt-export-render); the replay is the regression arm (CTO half @ece42ad420 condition 3).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added or changed here; the IAM leg (row D2-W181-S1) is a separate laptop sign-off, owed before the route (CTO half condition 2).
comp-routes: DECLARED-NOT-APPLICABLE -- the custody-report-persist route is DECLARED in routes.json but NOT applied by this order (function only; the api root is outside <paths>).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p87_cells.py dry-run at base ece42ad420 on dell2 2026-10-08 ~22:0xZ: IB87-1-AC1 FAIL, IB87-1-AC2 FAIL (no file); 0 control bytes in the check.
lane: the <paths> block IS the grant. Dell apply authority: step C (msgs 1288/1297); irpt-export-render is not among the ten protected functions; the before-rule's four classes are not touched. Worktree cut from box/dell2 (msg 1530; CTO half condition).
</preflight>
