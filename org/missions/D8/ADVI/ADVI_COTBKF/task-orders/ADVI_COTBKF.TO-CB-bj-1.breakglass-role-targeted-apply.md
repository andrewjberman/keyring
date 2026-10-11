# TO ADVI_COTBKF.TO-CB-bj-1.breakglass-role-targeted-apply -- round 62 CB-bj-1: create FWD-7's restricted-prefix break-glass role by a targeted apply of 2 addresses

<to_id>ADVI_COTBKF.TO-CB-bj-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bj-1` (`decompositions/ADVI_COTBKF_DECOMP.round62.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RELEASED at issue: both halves are signed.**
- **COO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_FWD7_RESTRICTED_BREAKGLASS_ROLE_COO_HALF.md` @fd4e6436cf, file sha256 `31df136096ccbbaadf000931bfe8974368b3aa3842d77566ceaf79a7e3cde3f2`.
- **CTO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_FWD7_RESTRICTED_BREAKGLASS_ROLE_CTO_HALF.md` @9b8eb8c244, file sha256 `de8c29b8febda2252a49af5111044edf5aa09439176f8926e5a21aa9c27e4cb9`.
- **Hash both files and `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` before you start.** The `.tf` must be the blob at
  commit 8c6fc7652a (`git rev-parse 8c6fc7652a:infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` equals
  `git rev-parse HEAD:` the same path). If a half's hash differs or the blob moved, STOP and report the values.

**Read both halves in full and `/cloud-ops` first.**

**Why.** The role `cloudops-cot-restricted-breakglass-role` and its inline policy `restricted-prefix-get-put-list` exist in code only.
They plan as 2 adds on every box, so any untargeted apply of the `shared-infra` root would create them as a rider (row
ADVI_COTBKF-D2-S95, ARMED). This order creates them on purpose, alone, under their own pair.

**Your item, on dell2, in the BASE checkout at a HEAD that contains @9b8eb8c244.**

1. Open this act's ledger entry BEFORE the plan (condition 1). Read `.open_deploys/` across every live worktree first, with the
   per-tree denominator.
2. Plan, targeted and saved:
   `terraform -chdir=infra/aws/terraform/shared-infra plan -input=false -no-color -out=<a path outside the repo> -target=aws_iam_role.restricted_breakglass -target=aws_iam_role_policy.restricted_breakglass`.
   Print the plan's addresses and its count line.
   - **Branch A:** exactly `2 to add, 0 to change, 0 to destroy`, and the only two addresses are those two -> step 3.
   - **Branch B:** anything else -> STOP, nothing applied, report.
3. Apply THE SAVED PLAN through `.tools/safe-apply.sh` (condition 2). No untargeted apply, no other target, no state verb.
   - **Branch C** (the role is created and its policy is refused): re-run the same targeted plan and apply ONCE. If the policy still
     fails, a targeted destroy of `aws_iam_role.restricted_breakglass` ALONE is pre-authorised by the CTO half for this case only.
4. Proof 1: `get-role` on the role (its ARN; its trust document has exactly one principal, the console user) and `get-role-policy`
   (the four actions: `s3:GetObject`, `s3:GetObjectVersion`, `s3:PutObject`, `s3:ListBucket`).
5. Proof 2: a PLAN ONLY, untargeted, on dell2, saved outside the repo with its JSON at
   `C:/dev/_cotbkf_private_evidence_20261009/r62/shared_infra_plan_after.json`. Read it for the two addresses alone: both no-op.
   **Nothing is applied from this plan.** Whatever else it lists is dell2's known credential reading (row D2-S92).
6. Close the ledger entry after the proof. **No agent assumes the role, at any point, to test it** (condition 5).

**The CTO half's branches, rollback and conditions, verbatim (its sections 3 to 5):**

**3. Both branches, and a third**

- **A. The targeted plan reads exactly `2 to add, 0 to change, 0 to destroy`:** apply.
- **B. Anything else** (a third address, a change, a destroy, the role already live or in state): STOP, nothing applied.
- **C. The apply creates the role and the policy fails** (a permission the applier's credentials lack, for example): the role
  exists with no policy and grants nothing. The applier re-runs the same targeted apply ONCE. If the policy still fails, a
  targeted destroy of `aws_iam_role.restricted_breakglass` alone is PRE-AUTHORISED here, for this case only, so the act is
  not left half-landed. If the role itself is refused, nothing was created and it is Branch B.

**4. Rollback**

A targeted destroy of the two addresses. Outside Branch C it needs this seat's word at the time, as the COO half says.

**5. Conditions**

1. The ledger entry is opened before the plan and closed after the proof.
2. The plan is saved and the saved plan is what is applied; the plan's two addresses and the count are printed.
3. Proof 1 of the COO half as written (`get-role`, one principal; `get-role-policy`, four actions).
4. Proof 2 is a PLAN ONLY, untargeted, on dell2, read for those two addresses alone: both no-op. Whatever else that plan
   lists is dell2's known credential reading (row D2-S92) and nothing is applied from it.
5. No agent assumes the role, ever, to test it.
6. Row D2-S95 is disarmed by the issuer on proof 2. The unlogged earlier apply of the bucket policy statements is filed as
   its own row; it does not hold this act.

**AMENDMENT 1 (issuer, 2026-10-11T08:57Z) -- RE-RELEASED on both halves, re-signed on the renamed policy. Where this amendment and the text above differ, this amendment binds.**

- **Why.** Your first run stopped correctly before any write: the apply-time naming limb refused the inline policy's hand-typed name
  (`safe-apply` rc=7; report @bb3ab3a85a). The canon's owner fixed `lib/opal_naming.py` and ruled the name (laptop `1.0.0_SA_CTO`
  @e1267f773c); round 63 changed that one line (drained @ca2a79acf1): the inline policy is `RestrictedPrefixGetPutList`.
- **New pins. Hash all three before you start; any difference is a STOP.**
  - COO half `deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_FWD7_RESTRICTED_BREAKGLASS_ROLE_COO_HALF.md` @c9afa6bf16, file sha256
    `ca572dd7e82971260d5af158d13232998038cf48be88a449b3ff323ecda7e8b7`.
  - CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_FWD7_RESTRICTED_BREAKGLASS_ROLE_CTO_HALF.md` @129d787f44, file sha256
    `f55925118eeed0a800a7fcdd456d5a6f96065a1d69f3e339c4fbfb7be029efdc` (re-signed; its first signature is marked void in the file).
  - `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`: `git hash-object` and `git rev-parse HEAD:` that path both read
    `1985337a9cef839688fe054acc667ed4d4397dc7`. The face's "blob at commit 8c6fc7652a" is superseded by this value.
- **Before step 1:** close round 62's ledger entry with `deploy_ledger close --gate-refused "<your evidence>"` (the laptop CTO's
  ruling, item 2). Then open a NEW entry for this run.
- **In step 2, print the planned role name.** It must read `cloudops-cot-restricted-breakglass-role`. Any other name is Branch B:
  STOP, nothing applied (the generated naming carriers are stale at HEAD, row ADVI_COTBKF-D2-S103; no seat on dell2 runs `generate`).
- **If the apply-time naming limb refuses again:** nothing is created and nothing is overridden. Do not type in a name the gate
  suggests. Report the refusal text; it returns to the canon's owner on cross-box call XB-20261011T082334Z-282f.
- **Proof 1** reads the inline policy by its new name: `get-role-policy --policy-name RestrictedPrefixGetPutList`. The four actions are
  unchanged.
- Steps 3 to 6, Branches A, B and C, both mechanical criteria and the judgment criterion stand as written.

**The CTO half's re-signing, verbatim:**

RE-SIGNED 2026-10-11 ~09:0xZ on the renamed policy -- the half above was VOID from the rename

**Why it was void:** this seat signed lines 263-264 with a hand-typed policy name. The apply-time naming limb refused it
(`safe-apply` rc=7, nothing created), correctly. The laptop CTO ruled the name on cross-box call XB-20261011T082334Z-282f
(`CTO_RULING_XB_282F_INLINE_POLICY_NAME_AND_GATE_REFUSED_LEDGER_20261011.md` @e1267f773c; not read by this seat, relayed in
msg 4504).

**SIGNED against:** the COO half @c9afa6bf16 and `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` blob
`1985337a9cef839688fe054acc667ed4d4397dc7` (`git hash-object`, this seat).

**Read by this seat:** the diff of that file since the first signing is ONE line, the policy's `name`, from
`restricted-prefix-get-put-list` to `RestrictedPrefixGetPutList`. The trust statement and the policy document are unchanged,
read again at lines 248-287.

Sections 1 to 5 above stand unchanged, with three additions:
1. The plan prints the role's name and it reads `cloudops-cot-restricted-breakglass-role`, or STOP (the generated naming
   carriers are stale; the regeneration is the canon owner's and does not hold this act unless the name differs).
2. Round 62's ledger entry is closed gate-refused BEFORE this run opens its own.
3. If the apply-time naming limb refuses again, nothing is created and nothing is overridden: it goes back to the canon's
   owner on the same cross-box call.

-- 1.0.0_SA_CTO~DELL2

### ACCEPTANCE

<criterion id="CB62bj1-AC1" cell_refs="CB-bj-1"><invocation>python -c "import json,re;d=json.load(open('C:/dev/_cotbkf_private_evidence_20261009/r62/shared_infra_plan_after.json',encoding='utf-8'));rc=d.get('resource_changes',[]);w=[x for x in rc if x['address'] in ('aws_iam_role.restricted_breakglass','aws_iam_role_policy.restricted_breakglass')];mv=[x for x in w if x['change']['actions']!=['no-op']];print('BREAKGLASS-PLAN-AFTER resources=%d the_two=%d the_two_changed=%d'%(len(rc),len(w),len(mv)))"</invocation><expect>BREAKGLASS-PLAN-AFTER</expect></criterion>
`CB62bj1-AC1` -- after the apply, an untargeted plan lists both addresses (`the_two=2`) and neither changes (`the_two_changed=0`).
The whole line is read by the issuer: `the_two=2 the_two_changed=0` is the pass; `the_two=0` is a failed read, not a pass.

<criterion id="CB62bj1-AC2" cell_refs="CB-bj-1"><invocation>MSYS_NO_PATHCONV=1 .tools/aws iam get-role --role-name cloudops-cot-restricted-breakglass-role --query "Role.AssumeRolePolicyDocument.Statement[].Principal.AWS" --output text</invocation><expect>arn:aws:iam::313476888478:user/Andrew_Berman_Console</expect></criterion>
`CB62bj1-AC2` -- the role exists and its trust names exactly one principal, the console user: the output is that one ARN and nothing
else.

<criterion id="CB62bj1-AC3" cell_refs="CB-bj-1" judgment="true"/>
`CB62bj1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the saved plan that was applied named only the two
addresses; the inline policy read back carries the four actions on the restricted prefix and no delete; no principal other than the
console user can assume the role; no agent assumed it.

<expected_criteria>CB62bj1-AC1,CB62bj1-AC2,CB62bj1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the file of this order. Plans and their JSON live OUTSIDE the repo.
- **Do NOT:** run an untargeted apply; apply any other address; run a state verb (`import`, `mv`, `rm`, `taint`); assume the role;
  read or list the restricted prefix; push.
- **A destroy** is allowed only in Branch C as the CTO half pre-authorises it (the role alone). Any other destroy needs the CTO's word
  at the time.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round62.md</decomp_doc> (round 62), cell `CB-bj-1`.
<owned_cells>CB-bj-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB62bj1-AC1, CB62bj1-AC2, CB62bj1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-bj-1.breakglass-role-targeted-apply.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB62bj1-AC1,CB62bj1-AC2,CB62bj1-AC3` BEFORE the flip. Mechanical:
CB62bj1-AC1 and CB62bj1-AC2. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the three hashes of step 0; the targeted plan's addresses and count line; the apply's summary line; the two proof-1
outputs; the `BREAKGLASS-PLAN-AFTER` line; which branch ran; the ledger entry's path and close time; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE two IAM objects; no schedule creates, assumes or reads the role.
comp-iam: DECLARED-NOT-APPLICABLE the issuer did not run comp-iam; the role's trust and policy were read from the applier's saved plan of 2026-10-11 (terraform 1.15.8) and from the Terraform file by the CTO (lines 203 to 287); BLIND: other Terraform roots and scripts were not searched for the role's name, and the applier's get-role NoSuchEntity of 2026-10-11 is the only read that none has created it.
comp-adversary: RUN -- the plan is saved and the saved plan is applied; Branch B stops on any third address; the after-plan criterion fails on a missing read (the_two=0) as well as on a change; the role is never assumed; BLIND: whether the console user can in fact assume the role is not exercised by any agent, by rule.
lane: 0.7.0_AE_CloudOps, a targeted apply under both signed halves; the pair names the applier and the box.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4370 and msg 4433; the pair @fd4e6436cf and @9b8eb8c244; rows ADVI_COTBKF-D2-S91, D2-S93 and D2-S95; cell CB-d-4 (order complete @f746fa5b24).
