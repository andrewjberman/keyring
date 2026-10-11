# NFRA_IAMROLES202609.TO-IAM-y-1 -- DISARM Z-S42: a pre-apply inbox check that cannot read clean from a linked worktree

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R8.md</decomp_doc>
<owned_cells>IAM-y-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (round-7 analysis E1 -- FIRST, before any WORLD act of this project)

```
IAM-y-1. ACT: replace your pre-apply inbox check (row Z-S42: it read 0 from a linked worktree, the same as an empty inbox,
and three apply records cite it) with a form that cannot fail toward CLEAN, and record that form in
.claude/skills/cloud-ops/SKILL.md beside rule 18's HALT-gate caveat. The form, per ROUND_ANALYSIS.round7.md @fef971046b:
  (a) PRIMARY: the broker read get_delivery_state(<your full lane serial>), counting every row not READ;
  (b) FALLBACK only if the broker is unreachable: `test -d` on the REAL inbox path
      (org/mcp/inbox/<base>/~<lane>/ under the MAIN workspace root, never a linked worktree's copy), then `ls -A`, counting
      files other than read/. A missing path is an ERROR (non-zero exit, printed), NEVER a 0.

STEPS:
  1. Write the form into .claude/skills/cloud-ops/SKILL.md (a short subsection under rule 18), naming both limbs and the
     ERROR-on-missing rule.
  2. GRADE IT, from a LINKED WORKTREE (not the main tree), and record the outputs verbatim in
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round8/INBOX_CHECK_GRADE.md:
       - NEGATIVE: run the fallback limb with the worktree-relative path; it must print an ERROR, not 0;
       - POSITIVE CONTROL: have one message planted in your lane inbox (ask nothing; send yourself one with
         send_message(to_agent="0.7.0_AE_CloudOps~IR", subject="Z-S42 control")) and show the primary limb counts it as 1
         unread BEFORE you read it, then ack it;
     with exactly these lines:
       CHECK-NEGATIVE: <ERROR text>
       CHECK-POSITIVE: unread=1
  3. Report to 2.0.0_SA_COO~ZI.
```

## DEPENDENCIES

None. FIRST in round 8: no WORLD act of this project runs before it is complete (DECOMP_R8 section 4).

## BOUNDS

```
LOCAL: no AWS write. Only the skill text and the grade file change. The control message is to yourself only.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
.claude/skills/cloud-ops/SKILL.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round8/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-y-1.disarm-the-inbox-check.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-y-1).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-y-1"><invocation>grep -c -E 'get_delivery_state' .claude/skills/cloud-ops/SKILL.md</invocation><expect>1 or more -- the recorded form names the broker read as the primary limb</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-y-1"><invocation>bash -c "f=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round8/INBOX_CHECK_GRADE.md; test -f \$f || { echo MISSING:\$f; exit 2; }; echo neg=\$(grep -c -E '^CHECK-NEGATIVE: .*ERROR' \$f) pos=\$(grep -c -E '^CHECK-POSITIVE: unread=1\$' \$f)"</invocation><expect>`neg=1 pos=1` -- the missing-path run ERRORs, and the planted control counts as one unread</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-y-1" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): can the recorded
  check still read CLEAN when mail is waiting, from any tree?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>8</round>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-y-1</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 8) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-7 slug (msg 33310, REMEDIATION_v7.Z.md @e65f90921b) -> `ROUND_ANALYSIS.round7.md` @fef971046b E1 -> L5 round-8 decomp -> this issuance.
**Risk LOCAL:** an instrument and its documentation; nothing in AWS moves.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cell opens no deploy ledger and applies nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM resource is read or moved; the cell repairs an inbox check.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 1 of 1 (Z-S42's failure: a linked worktree's inbox path reads 0 like an empty inbox; DECOMP_R8 section 2).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base reads 0 (the form is not recorded yet; FAIL as expected); AC2 base FAIL as expected (`MISSING:` the grade file).
