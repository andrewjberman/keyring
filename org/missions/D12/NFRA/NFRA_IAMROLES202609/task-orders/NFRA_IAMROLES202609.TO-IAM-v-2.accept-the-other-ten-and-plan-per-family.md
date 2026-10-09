# NFRA_IAMROLES202609.TO-IAM-v-2 -- ACCEPT the other ten unowned rows, plus one adoption plan per family

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R5.md</decomp_doc>
<owned_cells>IAM-v-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-4; the round-4 analysis calls this E2)

```
IAM-v-2. ACT: as the owner of record ruled by 1.0.0_SA_CTO~Z (ledger/CTO_RULING_FWD4_OWNER_OF_RECORD_20261009.md
@fa8ec0e726), accept the ten rows IAM-v-1 did not cover and write how each family reaches code. No apply.

FWD-4, verbatim:
  "Every role is either in code or has a named owner and a reason"
  DONE WHEN  APPLIED -- each one is either in code or carries a named owner and a reason

THE FILE: org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md
  Your ten rows, each reading owner=NO-ACCEPTING-SEAT at the cut:
    1 bd-merge-daily-lambda-role          ADOPT     9 opal-smartx-lambda-role              ADOPT
    2 bd-pipeline-task-role               ADOPT    11 portfolio-management-lambda-role     ADOPT
    3 codebuild-semantic-clustering-role  ADOPT    14 sentiment_query_api-role             ADOPT
    5 finbert-ec2-backfill-role           ADOPT    16 workspace-sync-lambda-role           ADOPT
    6 lambda-ec2-runtime-monitor-role     ADOPT     7 lambda-test-role                     RETIRE
  Rows 8 and 10 are IAM-v-1's (yours already); rows 4, 12, 15 are owned by 1.0.0_SA_CTO~Z; row 13 is DECLARED.

WHAT TO DO:
  (a) Write deliverables/0.7.0_AE_CloudOps~Z/ACCEPTANCE_ROWS_TEN.md: your acceptance of record, one
      section per row, in your words. Then PREPARE the row edits in GOVERNANCE_DISPOSITION.md in the
      shared tree (owner=NO-ACCEPTING-SEAT -> owner=0.7.0_AE_CloudOps~Z, reason extended) and leave them
      UNCOMMITTED: that file sits under another serial's deliverables folder and the owned-paths lane
      refuses your commit there, so the issuer lands your prepared bytes as the carrier, citing your
      acceptance commit (amendment A1, row Z-S19). Do not take an author override.
  (b) Write deliverables/0.7.0_AE_CloudOps~Z/ADOPTION_PLAN_TEN.md: group the ten into families (by the
      Terraform module that should own each, or by the producing pipeline), and per family state the custody
      home, the adopting act (an `import` block per role, as round 2's candidate does), the module-scoped
      things that do not travel (state key, provider default_tags), and the order you would apply them in.
      Row 7 (RETIRE) gets a retirement plan instead: what proves nothing assumes the role, and the delete.
      Name every role by its exact name.
  (c) A row you will NOT accept: leave its owner field as it is, say why in ADOPTION_PLAN_TEN.md, and file
      one surprise row. A refusal on the record is valid; a forged acceptance is not.
```

## DEPENDENCIES

`IAM-v-1` complete (same file; never edit it concurrently with v-1).

## BOUNDS

```
GOVERNANCE ONLY (C-TWO-REMEDIES): no permission narrowed, no policy edited.
NO APPLY THIS ROUND: no .tf file is written, no import is applied, no role is deleted. The plan is text.
YOUR TEN ROWS ONLY: rows 4, 8, 10, 12, 13, 15 are unchanged by this commit.
C-ANALYZER-PRICED-FIRST + G-25: no Access Analyzer.  G-21: no alert, alarm, monitor or schedule.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-v-2.accept-the-other-ten-and-plan-per-family.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh`
under your own author line. Flip this order's LAST `<status>` to `complete` with a proof instance in your
deliverables directory.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-v-2"><invocation>bash -c "F=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md; echo rows=\$(grep -cE '^[0-9]+\. \`[A-Za-z0-9._-]+\`' \$F) unowned=\$(grep -E '^[0-9]+\. \`[A-Za-z0-9._-]+\`' \$F | grep -c -v -E 'DECLARED|owner=(0\.7\.0_AE_CloudOps~Z|1\.0\.0_SA_CTO~Z) reason=')"</invocation><expect>exactly `rows=16 unowned=0` -- 16 of 16 rows are in code or carry a named owner and a reason, read on the committed blob with the denominator printed; unowned above 0 is valid only for a row ADOPTION_PLAN_TEN.md refuses by name</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-v-2"><invocation>bash -c "grep -o -E 'bd-merge-daily-lambda-role|bd-pipeline-task-role|codebuild-semantic-clustering-role|finbert-ec2-backfill-role|lambda-ec2-runtime-monitor-role|lambda-test-role|opal-smartx-lambda-role|portfolio-management-lambda-role|sentiment_query_api-role|workspace-sync-lambda-role' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/ADOPTION_PLAN_TEN.md | sort -u | wc -l"</invocation><expect>10 -- the plan names every one of the ten roles; a "No such file" error means the plan is missing</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-v-2"><invocation>bash -c "git log --format=%an -- org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/ACCEPTANCE_ROWS_TEN.md | sort -u"</invocation><expect>exactly one line, 0.7.0_AE_CloudOps~Z -- the acceptance of record is a document only the lane authored (amendment A1, row Z-S19)</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-v-2" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming
  3.0.0_SA_CVO~Z): could a later round cut one adoption cell per family straight from ADOPTION_PLAN_TEN.md, without
  re-deriving custody homes?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>5</round>
<slot>0.7.0_AE_CloudOps~Z</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-v-2</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 5) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-4 slug @3f69d8a895 -> `ROUND_ANALYSIS.round4.md` @20c2fcabe8 E2 + ruling @fa8ec0e726 -> L5 round-5 decomp -> this issuance.
**Chain:** v-1 -> v-2 (same assignee, same file). **Risk LOCAL:** owner fields and a plan; no AWS write.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 220`, BUDGET REACHED, 1 of 6 carriers, C1=23, C2=22 PARTIAL (0 of 22 scanned), rc=3; PARTIAL_OR_BLIND, not read as clean. G-21 binds as CLAUDE.md law.
comp-iam: RUN -- `bash .tools/comp-iam stats` from the main checkout: 214 IAM roles parsed / 196 services / 1154 operations; a source count, used here only to say the ten are outside it per round 2.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (16 rows by the strict regex; 12 NO-ACCEPTING-SEAT at the base, 10 of them this cell's).
</preflight>

**Preflight disposition:** checks dry-run at the base `e9bda7b982`: AC1 base: FAIL as expected (`rows=16 unowned=12`); AC2 base: FAIL as expected (file absent); AC3 base: FAIL as expected (author is not the lane).
