# TO IRPT_BCKEND.TO-IB-pr-424 -- ROLLBACK of the vendor performance release (IB-pr-421, 422, 423) on lane ~IB2: zip back, tree back, two session policies removed

<to_id>IRPT_BCKEND.TO-IB-pr-424</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4624 ("(a) ROLL BACK NOW -- Branch B, both steps"; it authorises the targeted destroy and withdraws msgs 4416 and 4616), on this seat's escalation `deliverables/2.0.0_SA_COO~P2/ESCALATION_IB_pr_423_SERVES_COTTONWOOD_A_VENDOR_FIGURE_AGAINST_FWD_3_20261011.md` @a5f045cabf; the signed Branch B of the pair (COO half @468df7baa4, CTO half @7a01aa805a) | **Decomp cell:** `IB-pr-424` (decomposition section 115) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Why, in one paragraph.** The release you applied under IB-pr-423 was correct to its order and the order was wrong. The ratified
ENDPOINT (FWD-3; PRD ADDENDUM v0.19) serves Inflection and Cottonwood a figure computed by Opal from holdings, and makes a vendor
figure a comparison point only. The refusal the release removed was that design. Since 09:19:10Z a Cottonwood user's fresh
performance request is answered with a Black Diamond-calculated return; three were served at 09:45Z. The CTO ruled the rollback, now.

Run this NOW, ahead of anything else on the lane. ONE ledger entry, opened and COMMITTED before any write, naming the function, the
role and both policies and stating that this is a ROLLBACK of ledger entry `IB-pr-423`'s release.

| what | must read after | reads now |
|---|---|---|
| function `irpt-performance-adapter` | CodeSha256 `9kYLdR64P0p2TEbDXcQu1hrpQ9KtqjPNnFDpoE/W31A=` | `OF+8j4ucXsxwJ195NKEQZnma22T8bYVUriw9YP859RU=` |
| role `irpt-performance-adapter-role` | 7 inline policies; neither `irpt-performance-approved-session-policy` nor `irpt-performance-approved-orion-session-policy` | 9, both present |

Steps, in this order. The zip goes back FIRST, so the new code never runs without its grants and the old refusal is restored before
anything else moves.
1. **Source-map entry back.** In `infra/aws/lambda/ci/lambda-source-map.json`, restore the `functions` entry of
   `irpt-performance-adapter` to its content in the commit before your `f5d33c7aa9` (`git show f5d33c7aa9^:<file>`). No other entry.
   ONE commit touching only that file.
2. **The zip.** Redeploy the pre-release package through the module's Terraform path and `safe-apply`: S3 version
   `7IkeCAOa8F8IzqgaW1_WCLczFhmtzaLn` of `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip`,
   re-read as still present with `content-sha256` equal to `9kYLdR64...` first. If your build path is the way to promote it, a
   `BUILD_ONLY=1` build from the restored entry must print `9kYLdR64...` or ABORT. The full-root plan reads exactly 1 change, the
   function, or STOP. Never `aws lambda update-function-code`. After-read: live CodeSha256 equals `9kYLdR64...`.
3. **One fresh request, refused.** As a non-49F caller that the function ADMITS (not the unauthenticated shape), or, if you cannot
   drive an admitted caller, the same event you used as IB-pr-423's live call PLUS a read of the function's log from the promote on
   showing 0 `served` outcomes and 0 vendor indicators. Record which you did. A request that is SERVED a figure after the rollback is
   a STOP and a row.
4. **The tree back.** Restore `infra/aws/terraform/investor-reporting/performance/retained.tf` and every file under
   `infra/aws/lambda/investor-reporting/performance/` to their content at commit `fb3bae3b99` (`git checkout fb3bae3b99 -- <path>`;
   a file the release ADDED, such as `performance/tests/test_vendor_use_gate.py`, is removed). ONE commit. This is what stops the
   next one-tree build or full-root apply from re-shipping the release. Run `python -m pytest -q tests` in
   `infra/aws/lambda/investor-reporting/performance/` and report its last line.
5. **The two policies.** With `retained.tf` restored, plan with `-target=aws_iam_role_policy.performance_approved_session
   -target=aws_iam_role_policy.performance_approved_inf_session`: exactly 0 adds, 0 changes, 2 destroys, or STOP. Apply through
   `safe-apply`. The CTO authorises this targeted destroy for this case (msg 4624). After-read: `list-role-policies` shows the 7
   and neither session policy.
6. **A full-root plan, read only:** it must read "No changes", as the baseline did before the release. Anything else is a row.
7. **Close the ledger** and write
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB122-1_vendor_path_rollback_after_reads.json`:
   `{ledger:{state,slug}, source_map_commit, tree_restore_commit, function:{live_after, s3_version}, role_policies_after:[names],
   fresh_request:{how, refused, public_reason_code, vendor_reached, served_outcomes_since_rollback}, full_root_plan,
   served_while_live:{window_start, window_end, served_count, use_record_count}}`. For `served_while_live`, count from the log group
   the `served` outcomes between 09:19:10Z and the rollback's promote, and the `PERFORMANCE_USE#` records written in that window if
   your read reaches them (counts only; say "not read" where it does not). No account id, balance or figure in the file.

<criterion id="IB122-1-AC1" cell_refs="IB-pr-424"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r122/p122_cells.py" . IB122-1-AC1</invocation><expect>IB122-1-AC1 PASS</expect></criterion>
<criterion id="IB122-1-AC2" cell_refs="IB-pr-424"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r122/p122_cells.py" . IB122-1-AC2</invocation><expect>IB122-1-AC2 PASS</expect></criterion>
<criterion id="IB122-1-AC3" cell_refs="IB-pr-424"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r122/p122_cells.py" . IB122-1-AC3</invocation><expect>IB122-1-AC3 PASS</expect></criterion>

<expected_criteria>IB122-1-AC1, IB122-1-AC2, IB122-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. One function's code back to its pre-release package, two inline policies removed
  from one role, two tree restores, one source-map entry. No route, schedule, layer, environment or table change; no other function,
  role or Terraform root; no `lambda.tf` edit. Do NOT delete the retained vendor reports or the use records written while the release
  was live: they are the record of what was served.
- **NO VENDOR CALL** by you or any tool you run, and no `secretsmanager get-secret-value`.
- **Refusal clause:** STOP, file a row and report on any of: a plan count that is not exact; a digest that is not `9kYLdR64...`; a
  refused apply; a request served a figure after the rollback. If step 2 cannot land, do NOT remove the policies: the new code
  without its grants is the broken state; report at once.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. Write the message file with the Write tool, OUTSIDE
  the worktree; do NOT pre-`git add`. ASCII only.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/performance/
infra/aws/terraform/investor-reporting/performance/retained.tf
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-424.vendor-performance-release-rolled-back.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 115 (round 122, workstream ~P), cell `IB-pr-424`.
<owned_cells>IB-pr-424</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB122-1-AC1, IB122-1-AC2, IB122-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-424.vendor-performance-release-rolled-back.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** report twice. After step 2: the live CodeSha256. After the close: the role's policy list, the fresh request's outcome, the
full-root plan's line, the count served while the release was live, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the radius is the signed Branch B of the IB-pr-421 + IB-pr-422 pair (one function's code, two inline policies on one role), plus two tree restores and one source-map entry that put the repository back to its content before the release.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the IAM change is the removal of the two single-secret grants IB-pr-423 added, by a targeted destroy the CTO authorised in msg 4624, with a STOP on any count but 0 add, 0 change, 2 destroy.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p122_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~10:0xZ: AC1 FAIL (live == OF+8j4uc), AC2 FAIL (9 policies), AC3 FAIL (tree carries the release); commit-gate clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2, IRPT_BCKEND only.
</preflight>
