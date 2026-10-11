# TO IRPT_BCKEND.TO-IB-pr-423 -- the vendor performance release applied on lane ~IB2: source map, two session-read policies, then IB-pr-421's adapter zip

<to_id>IRPT_BCKEND.TO-IB-pr-423</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>121</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packets `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~282/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-421.md` (blob e6ac0b9548) and `deliverables/0.9.0_WK_IRPT_BCKEND~283/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-422.md` (blob 853883965b); COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_421_422_VENDOR_PERFORMANCE_PATH_COO_HALF.md` @468df7baa4; CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_421_422_VENDOR_PERFORMANCE_PATH_CTO_HALF.md` @7a01aa805a (SIGNED, conditions 1-5) | **Decomp cell:** `IB-pr-423` (decomposition section 114) | **outcome_ref:** FWD-2

---

## WORKER FACE

ONE release, ONE sitting, ONE ledger entry. Read both packets and both halves in full first. It widens served output and one role: after
it, a signed-in Cottonwood or Inflection user's fresh performance request calls Black Diamond or Orion with the firm's stored session.

| what | the only thing that may land | expect before | rollback |
|---|---|---|---|
| role `irpt-performance-adapter-role` | `irpt-performance-approved-session-policy`: `secretsmanager:GetSecretValue` on `arn:aws:secretsmanager:us-east-1:313476888478:secret:blackdiamond/cot/session-jnzOyC`; `irpt-performance-approved-orion-session-policy`: the same action on `arn:aws:secretsmanager:us-east-1:313476888478:secret:orion/jwt/current-ewrBtp` | 7 inline policies, neither of these | targeted destroy of the two policies, ONLY if step 2 cannot land or is rolled back |
| function `irpt-performance-adapter` | CodeSha256 `OF+8j4ucXsxwJ195NKEQZnma22T8bYVUriw9YP859RU=` | `9kYLdR64P0p2TEbDXcQu1hrpQ9KtqjPNnFDpoE/W31A=` | redeploy S3 version `7IkeCAOa8F8IzqgaW1_WCLczFhmtzaLn`, re-read as present first |

Steps, in this order:
- **Ledger.** Open-deploy read (CLAUDE.md NEVER-2), then open ONE ledger entry naming the function, the role and both policies. COMMIT
  the open and its sentinel before any write.
- **Step 0, source map first.** In `infra/aws/lambda/ci/lambda-source-map.json`, replace the `functions` entry of
  `irpt-performance-adapter` with the same-named entry of
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~282/candidate_source_map.json` (every investor-reporting member at
  `cd833e66cb`). No other entry, no other key. ONE commit touching only that file.
- **Step 1, the two policies.** In `infra/aws/terraform/investor-reporting/performance/`, plan with
  `-target=aws_iam_role_policy.performance_approved_session -target=aws_iam_role_policy.performance_approved_inf_session`: exactly 2
  adds, 0 changes, 0 destroys, or STOP. Apply that targeted plan through `safe-apply`. After-read: `get-role-policy` on each,
  printing its ONE secret ARN and its single action. A stop here is a safe state: with the old zip live the grant is unused, because
  the old code refuses at its plan check before any secret read.
- **Step 2, the zip.** Precheck: live CodeSha256 equals "expect before" and the rollback version is still present and the latest.
  `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-performance-adapter` prints the table's digest,
  or ABORT. Then the same without BUILD_ONLY. Then the full-root plan with a KNOWN hash: exactly 1 change, the function, 0 adds, 0
  destroys, or STOP. Apply through `safe-apply`. Never `aws lambda update-function-code`. After-read: live CodeSha256 equals the built
  digest.
- **Step 3, the live-call arm, within a minute of the promote.** ONE GET of the performance route as a non-49F caller, in the same
  shape as IB-pr-420's arm (a caller the function refuses typed BEFORE the vendor path), so that NO vendor call is made. Expect a
  typed answer: no 500, and 0 `TypeError` and 0 `AccessDenied` lines in `/aws/lambda/irpt-performance-adapter` from the promote on. A
  500, a `TypeError` or an `AccessDenied` is Branch B for step 2 at once. Run the identical event before the promote too, as you did
  for IB-pr-420, and record both.
- **Close the ledger** and write
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB121-1_vendor_path_release_after_reads.json`:
  `{ledger:{state,slug}, source_map_commit, policies:[{name, action, resource}], function:{built_sha256, live_before,
  rollback_version, build_only_digest_matched, rolled_back, live_call:{route, status, typeerror_lines, accessdenied_lines,
  window_start, vendor_reached, use_record_key}}, close_statement}`. `close_statement` says, in these words, that the vendor
  performance path is `APPLIED, UNEXERCISED`: no vendor call was made by the apply. Counts, digests, status and reason codes only.

**Branch B.** Step 2: redeploy `7IkeCAOa8F8IzqgaW1_WCLczFhmtzaLn` through the same Terraform path, re-pin the source-map entry back in
the same sitting, then the targeted destroy of the two policies (pre-authorised by the CTO for exactly this case). A step-1 failure
with nothing landed needs no rollback.

**The CTO half's conditions, verbatim (section 3):**

1. The COO half's five conditions and its steps 0 to 3, as written. Policies before the zip; each count exact or STOP.
2. **No vendor call is made by the apply or by any agent to test it.** The live-call arm of step 3 is one GET as a non-49F
   caller that answers typed. If that one GET itself reaches a vendor, it is the release's one use and is stated as such in
   the close, with the use record's key.
3. The close reads APPLIED, UNEXERCISED. FWD-1 of DSGN_IRPTV1 is graded on the laptop's re-walk, asked through the managers
   after the ledger closes.
4. Three rows of the COO half stay open after this act and none holds it: a repeat request is refused
   (D2-W282-S2); one unrelated calendar test fails (D2-W282-S3), to be run on the pre-change tree so "pre-existing" is
   measured; the dead plan variables are removed in a later cell.
5. A stale vendor session is a typed refusal and a credential question for its owner, not a rollback.

**The COO half's five conditions:** (1) one sitting, one ledger entry opened and committed before any write, naming the function, the
role and both policies; (2) policies before zip, each step's count exact or STOP; (3) the live-call arm as stated, with `AccessDenied`
in its failure set; (4) the close states the vendor path as APPLIED, UNEXERCISED until the re-walk reads a figure; (5) the apply comes
by this order.

<criterion id="IB121-1-AC1" cell_refs="IB-pr-423"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r121/p121_cells.py" . IB121-1-AC1</invocation><expect>IB121-1-AC1 PASS</expect></criterion>
<criterion id="IB121-1-AC2" cell_refs="IB-pr-423"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r121/p121_cells.py" . IB121-1-AC2</invocation><expect>IB121-1-AC2 PASS</expect></criterion>
<criterion id="IB121-1-AC3" cell_refs="IB-pr-423"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r121/p121_cells.py" . IB121-1-AC3</invocation><expect>IB121-1-AC3 PASS</expect></criterion>

<expected_criteria>IB121-1-AC1, IB121-1-AC2, IB121-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. One function's code, two inline policies on one role, one source-map entry. No
  route, schedule, layer, environment or table change; no other function, role or Terraform root; no `lambda.tf` edit.
- **NO VENDOR CALL** by you or any tool you run, and no `secretsmanager get-secret-value`. No monitor, alarm, SNS or SES.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if step 2 landed) on any of: a plan count that is not exact;
  a moved live version; a digest miss; a refused upload or apply; a failed read-back; a live-call arm reading 500, a `TypeError` or
  an `AccessDenied`. A rolled-back release leaves its criteria FAIL; never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. Write the message file with the Write tool, OUTSIDE
  the worktree; do NOT pre-`git add`. ASCII only.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-423.vendor-performance-release-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 114 (round 121, workstream ~P), cell `IB-pr-423`.
<owned_cells>IB-pr-423</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB121-1-AC1, IB121-1-AC2, IB121-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-423.vendor-performance-release-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** report twice. After step 1: the two policies' after-reads. After the close: the live CodeSha256, the live-call status with
its TypeError and AccessDenied counts, whether the GET reached a vendor, whether anything was rolled back, each criterion's last line
and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the radius is the pair's (one function's code, two inline policies on one role, one source-map entry), read by the issuer in the COO half's "Read by this seat" table.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the IAM change is two single-secret grants whose targeted plan read 2 add, 0 change, 0 destroy in IB-pr-422, re-planned by this order with a STOP on any other count.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the live-call arm reads one existing route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p121_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~09:0xZ: AC1 FAIL (entry differs), AC2 FAIL (7 policies), AC3 FAIL (live == 9kYLdR64); commit-gate clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2, IRPT_BCKEND only.
</preflight>
