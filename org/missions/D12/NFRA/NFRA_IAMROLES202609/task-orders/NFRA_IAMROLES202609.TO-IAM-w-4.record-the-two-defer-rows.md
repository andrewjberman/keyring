# NFRA_IAMROLES202609.TO-IAM-w-4 -- RECORD the two DEFER rows (5 and 16): owner and reason, no adoption

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R6.md</decomp_doc>
<owned_cells>IAM-w-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-4; the round-5 analysis calls this E4)

```
IAM-w-4. ACT: the CTO ruled rows 5 and 16 DEFER: not adopted and not retired, carrying a named owner and a reason
(ROUND_ANALYSIS.round5.md @f77e32d7c3, the home table). Record that on the disposition.

  Row 5   finbert-ec2-backfill-role    reason (the CTO's words): "completed one-shot backfill; retirement is a WORLD act
                                       no one has asked for". Revisited only if a finbert backfill recurs.
  Row 16  workspace-sync-lambda-role   reason: "no consumer since 2025-12-30; no domain module". Adoption opens only if
                                       a module comes to own the function.

THE FILE: org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md
  Today each row reads `N. `role` -- ADOPT owner=0.7.0_AE_CloudOps~Z reason=...` (your round-5 acceptance).

DO:
  (a) Write deliverables/0.7.0_AE_CloudOps~IR/round6/DEFER_ROWS_5_16.md: per row, the CTO's ruling quoted, what would
      reopen it. Commit it under your author line. The owner field stays 0.7.0_AE_CloudOps~Z, which
      accepted ownership of both rows in round 5 (ACCEPTANCE_ROWS_TEN.md @36fae05ea5); this records the CTO's DEFER.
  (b) PREPARE, uncommitted in the shared tree, the two row first-lines changed from `-- ADOPT owner=` to
      `-- DEFER owner=0.7.0_AE_CloudOps~Z reason=`, the reason extended by the CTO's one-line reason. The file sits under
      another serial's folder, so the issuer lands your bytes as carrier (amendment A1, row Z-S19). Take no author override.
```

## DEPENDENCIES

None.

## BOUNDS

```
GOVERNANCE ONLY. Rows 5 and 16 only. Nothing is adopted, retired, deleted or applied.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round6/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-w-4.record-the-two-defer-rows.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k). Flip this order's LAST `<status>` to `complete` with a proof
instance (`to_id` NFRA_IAMROLES202609.TO-IAM-w-4) once the issuer's carrier has landed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-w-4"><invocation>bash -c "grep -E '^(5|16)\. \`' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c -- '-- DEFER owner=0.7.0_AE_CloudOps~Z reason='"</invocation><expect>exactly 2 -- both rows read DEFER with the named owner and a reason</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-w-4"><invocation>bash -c "F=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md; echo rows=\$(git show HEAD:\$F | grep -cE '^[0-9]+\. \`[A-Za-z0-9._-]+\`') unowned=\$(git show HEAD:\$F | grep -E '^[0-9]+\. \`[A-Za-z0-9._-]+\`' | grep -c -v -E 'DECLARED|owner=(0\.7\.0_AE_CloudOps~Z|1\.0\.0_SA_CTO~Z) reason=')"</invocation><expect>exactly `rows=16 unowned=0`, read on the COMMITTED blob (HEAD), never the working tree</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-w-4"><invocation>bash -c "git log --format=%an -- org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round6/DEFER_ROWS_5_16.md | sort -u"</invocation><expect>exactly one line, 0.7.0_AE_CloudOps~IR -- the record of the DEFER is the executing lane's own document</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-w-4" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): does each DEFER say
  what would reopen it, so it is a decision on the record and not a parking lot?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>complete</status>
<round>6</round>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-w-4</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 6) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-5 slug @f022594845 -> `ROUND_ANALYSIS.round5.md` @f77e32d7c3 E4 -> L5 round-6 decomp -> this issuance.
**Risk LOCAL:** two owner-and-reason lines and a deliverable.
<preflight>
comp-schedule: RUN at round 5 -- `python .tools/comp-schedule --budget 220`, BUDGET REACHED, 1 of 6 carriers, C1=23, C2=22 PARTIAL, rc=3; PARTIAL_OR_BLIND, not read as clean; the assignee reads .open_deploys/ for its module before any ledger opens.
comp-iam: RUN -- `bash .tools/comp-iam stats`: 214 IAM roles parsed / 196 services / 1154 operations; none of this order's roles is declared at the cut (ADOPTION_PLAN_TEN section 0).
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 3 of 3 (omission rule, default_tags hazard, row 2 ECS trust; DECOMP_R6 section 2).
</preflight>

**Preflight disposition:** checks dry-run at the base `6e61646e81`: AC1 base: FAIL as expected (0); AC2 base: PASS (`rows=16 unowned=0` has held since round 5; the criterion guards that the edit does not break it); AC3 base: FAIL as expected (file absent).
