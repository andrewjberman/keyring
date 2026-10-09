# NFRA_IAMROLES202609.TO-IAM-v-1 -- ACCEPT rows 8 and 10 as owner of record (the INERT adoption stays inert)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R5.md</decomp_doc>
<owned_cells>IAM-v-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-4; the round-4 analysis calls this E1)

```
IAM-v-1. ACT: as the owner of record ruled by 1.0.0_SA_CTO~Z (ledger/CTO_RULING_FWD4_OWNER_OF_RECORD_20261009.md
@fa8ec0e726), write YOUR OWN acceptance onto rows 8 and 10 of the governance disposition. Naming you did not
accept anything for you; this commit is the acceptance. Authorship is not acceptance, and acceptance is not
authorship: the act is yours and nobody else's.

FWD-4, verbatim:
  "Every role is either in code or has a named owner and a reason"
  DONE WHEN  APPLIED -- each one is either in code or carries a named owner and a reason

THE FILE: org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md
  Rows are numbered lines of the form  N. `role-name` -- VALUE owner=<seat> reason=<text>
  Row 8   `opal-data-refresh-lambda-role` -- EXEMPT owner=NO-ACCEPTING-SEAT reason=production serving-path role ...
  Row 10  `portal-auth-lambda-role`       -- EXEMPT owner=NO-ACCEPTING-SEAT reason=production serving-path role ...
  Rows 4, 12, 15 carry owner=1.0.0_SA_CTO~Z (that seat accepted them in writing). Row 13 is DECLARED.

WHAT TO DO:
  (a) Read the adopting Terraform for both roles, INERT by its extension:
      infra/aws/terraform/data-refresh/zz_adoption_candidate.tf.proposed (110 lines, blob b3a1298d6b; two
      `import` blocks, one per role), and its evidence,
      org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md
      (round 2 measured the plan non-destructive; its section 7 names what does not travel with the text,
      and its header says placement of portal-auth-lambda-role is an OPEN CALL).
  (b) On rows 8 and 10 ONLY, replace `owner=NO-ACCEPTING-SEAT` with `owner=0.7.0_AE_CloudOps~Z`, and
      extend `reason=` with one sentence in your words: what you accept (custody of the role and of the
      adoption decision) and what you do NOT accept by this commit (the apply, which is a separate WORLD act
      under its own pair). Keep every other word of both rows. Touch no other row.
  (c) Write deliverables/0.7.0_AE_CloudOps~Z/ACCEPTANCE_ROWS_8_10.md: for each role, what you read,
      what you accepted, and anything in the candidate you would NOT apply as written. If you would not
      accept a row, say so there and leave that row's owner field unchanged. A refusal on the record is a
      valid outcome; a forged acceptance is not.
```

## DEPENDENCIES

None. `IAM-v-2` (the other ten rows) follows this order and edits the same file.

## BOUNDS

```
GOVERNANCE ONLY (C-TWO-REMEDIES): no permission is narrowed, no policy edited, nothing applied.
INERT STAYS INERT: zz_adoption_candidate.tf.proposed is not renamed, edited, copied to a .tf or applied.
ROWS 8 AND 10 ONLY: every other row of the file is unchanged by this commit.
C-ANALYZER-PRICED-FIRST + G-25: no Access Analyzer.  G-21: no alert, alarm, monitor or schedule.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-v-1.accept-rows-8-and-10-as-owner-of-record.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`, `surfaced_at` = `date -u +%FT%TZ` at
filing. Commit through `.tools/safe-commit.sh` under your own author line. Flip this order's LAST `<status>` to
`complete` with a proof instance (below) in your deliverables directory.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-v-1"><invocation>bash -c "grep -E '^(8|10)\. \`' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c 'owner=0.7.0_AE_CloudOps~Z reason='"</invocation><expect>2 -- rows 8 and 10 both name the lane as owner, each with a reason; a 1 or a 0 means a row was not accepted, which is valid only if ACCEPTANCE_ROWS_8_10.md says why</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-v-1"><invocation>bash -c "git log --format=%an -- org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/ACCEPTANCE_ROWS_8_10.md | sort -u"</invocation><expect>exactly one line, 0.7.0_AE_CloudOps~Z -- the acceptance of record is a document only the lane authored; the row edit in GOVERNANCE_DISPOSITION.md is its carrier (amendment A1, row Z-S19)</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-v-1"><invocation>git hash-object infra/aws/terraform/data-refresh/zz_adoption_candidate.tf.proposed</invocation><expect>exactly b3a1298d6b2b8d99284b4211bfc0c18eaa707f19 -- the INERT adopting text is unchanged; acceptance did not slide into an edit</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-v-1" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming
  3.0.0_SA_CVO~Z): does each accepted row's reason say what was accepted and what was not, in the lane's own words,
  so a reader can tell custody from the apply?

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
<to_id>NFRA_IAMROLES202609.TO-IAM-v-1</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 5) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-4 slug @3f69d8a895 -> `ROUND_ANALYSIS.round4.md` @20c2fcabe8 E1 + ruling @fa8ec0e726 -> L5 round-5 decomp -> this issuance.
**Chain:** head of chain v-1 -> v-2 (same assignee, same file). **Risk LOCAL:** an owner field and a deliverable; no AWS write.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 220`, BUDGET REACHED, 1 of 6 carriers, C1=23, C2=22 PARTIAL (0 of 22 scanned), rc=3; PARTIAL_OR_BLIND, not read as clean. G-21 binds as CLAUDE.md law.
comp-iam: RUN -- `bash .tools/comp-iam stats` from the main checkout: 214 IAM roles parsed / 196 services / 1154 operations; neither row-8 nor row-10 role is declared outside the INERT candidate (round-2 ADOPTION_PLAN section 6).
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (rows 8 and 10 read NO-ACCEPTING-SEAT at the base; candidate blob b3a1298d6b, two import blocks).
</preflight>

**Preflight disposition:** checks dry-run at the base `e9bda7b982`: AC1 base: FAIL as expected (0); AC2 base: FAIL as expected (author is not the lane); AC3 base: PASS as expected (pin equals the base blob).
