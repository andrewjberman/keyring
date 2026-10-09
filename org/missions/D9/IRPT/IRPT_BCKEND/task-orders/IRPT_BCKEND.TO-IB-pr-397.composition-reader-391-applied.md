# TO IRPT_BCKEND.TO-IB-pr-397 -- the NEW irpt-commentary-composition-read-lambda (IB-pr-391) applied on lane ~IB2, after IB-pr-395

<to_id>IRPT_BCKEND.TO-IB-pr-397</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>102</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~202/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-391.md` (blob 531de9a9e7); COO half @feeee0be4d; CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_391_COMPOSITION_READER_CTO_HALF.md` @a946f8b829 (msg 2765: standalone after IB-pr-395); precondition met: ~V2 amended svc-commentary's pair (AMENDMENT 3 @c7bc0e611f, msg 2766) | **Decomp cell:** `IB-pr-397` (decomposition section 95) | **outcome_ref:** NFRA_TRNSPT FWD-10 H2 (gates IRPT_ANLREQ's commentary apply)

---

## WORKER FACE

Start AFTER IB-pr-395 closes. The packet is your procedure; the CTO half's conditions 1-4 win.
1. **Register the source-map entry** EXACTLY as `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~202/IB97-4_source_map_entry.json`
   (16 `files[]`, 12 `staged_from` rows). A different entry changes the sha256, which is a STOP.
2. **Re-run the packet's 8 replay arms BEFORE the ledger.** All 8 must match.
3. **Open the ledger.** It states the pin `9c995243f7`, the built sha256 `ZZmWOFSA/GjO0d/cKHSm9G5+xDc5sNfEHOpbmfIabQ0=` and the
   uploaded version id (law @ccbe8b8be1).
4. **Apply** `infra/aws/terraform/investor-reporting/export/commentary_composition.tf` through safe-apply.
   - The plan reads ONLY the listed adds (function, its role and read-only policy, invoke policy).
   - Names are `name()` output.
   - Anything else is a STOP.
5. **Read back** the live CodeSha256 equal to built, and a 0-diff re-plan.
6. **Leave the invoke policy's attachment to `outlook-global-commentary-draft-role` to ~T2's transcripts-root pair** (step 4
   there). That pair REQUIRES the commentary role's standing `kms:Decrypt` on the irpt key to be DROPPED. Tell ~T2 when the
   function is live.
7. **After-read** (CTO condition 3): ONE invoke as ~T2's role, holding only `lambda:InvokeFunction`, for one READY item. Record
   counts and stage only, NEVER composition content. If the attachment is not yet live, record `after_read_invoke` as
   `{status: WAITING_ON_T2_ATTACH}` and say so.
8. **Close the ledger.** Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB102-1_reader_release_after_reads.json`:
   `{ledger:{state,pin,sha256,version_id}, rolled_back, replay_rerun_before_ledger:[{name,verdict,negative_control}],
   after_read_invoke:{status,counts}}`.

<criterion id="IB102-1-AC1" cell_refs="IB-pr-397"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r102/p102_cells.py" . IB102-1-AC1</invocation><expect>IB102-1-AC1 PASS</expect></criterion>

<expected_criteria>IB102-1-AC1</expected_criteria>

## AMENDMENT 1 (2026-10-09 ~07:4xZ, issuer 2.0.0_SA_COO~P2, on CTO round analysis ADDENDUM 14 (msg 2804, @02f8c49182; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_75_76_P_64_Y_20261008.md`))

Rows W202-S1 and W202-S2. Register the reader in `lambda-source-map.json`, then BUILD FROM THE REAL MAP: no override, no `BAU_PARITY_SKIP`,
no parity skip of any kind. The built sha256 must equal `ZZmWOFSA...`; a different sha is a STOP and a row. Record in the after-reads file
`existing_functions_unchanged: true`, with the census line showing no existing function's members or behaviour change.

The issuer amends its own order on the CTO analysis (CLAUDE.md 27 L5-L6). Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE). If you work in a worktree, merge box/dell2 before flipping `<status>`.

## BOUNDS

- **Grant:** the `<paths>` block below and nothing else.
- **No vendor call**, no monitor, alarm, SNS or SES. Touch no other function.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if already applied) on any of these:
  - a moved start sha;
  - a built sha other than the packet's;
  - a failed replay arm;
  - a plan touching anything else;
  - a failed read-back.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
infra/aws/terraform/investor-reporting/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/investor-reporting/export/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-397.composition-reader-391-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 95 (round 102, workstream ~P), cell `IB-pr-397`.
<owned_cells>IB-pr-397</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB102-1-AC1. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-397.composition-reader-391-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give live sha before and after, the ledger entry, the replay verdicts, the invoke status, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- ONE new function plus its role, read-only policy and invoke policy; live_before ABSENT; no existing function moves (packet).
comp-iam: RUN -- NEW: the function's read-only role/policy and the InvokeFunction-only policy, both DESIRED in commentary_composition.tf; the commentary role's attachment and its kms:Decrypt drop ride ~T2's transcripts-root pair.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p102_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~07:2xZ: AC1 FAIL (reader absent); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2 (MSTR msg 2725), IRPT_BCKEND only.
</preflight>
