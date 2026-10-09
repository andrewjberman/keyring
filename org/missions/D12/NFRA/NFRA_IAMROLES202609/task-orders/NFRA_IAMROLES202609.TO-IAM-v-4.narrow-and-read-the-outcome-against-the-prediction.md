# NFRA_IAMROLES202609.TO-IAM-v-4 -- NARROW the one permission under a signed pair, and read the outcome against the prediction

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R5.md</decomp_doc>
<owned_cells>IAM-v-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-5; the round-4 analysis calls this E3, and this is its second half)

```
IAM-v-4. ACT: make the ONE narrowing IAM-v-3 predicted, through Terraform, and read what happened against
what was predicted. This is a WORLD act on a live role.

FWD-5, verbatim:
  "An engineer can narrow a permission and know beforehand what it would break"
  DONE WHEN  EXERCISED -- a real narrowing has been checked in advance and the check was believed
  C-NO-ACCESSDENIED: the project must not cause the outage it exists to prevent.

INPUTS (committed by IAM-v-3 before you start):
  deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/PREDICTION.json  (role, action, terraform_file,
      predicted_breaks, observation_window, rollback)
  deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/narrowing.patch   (one file, one action removed)
  ledger/NEVER_WIDEN_ROUND5_FWD5_NARROWING_CTO_HALF.md and ..._COO_HALF.md, both SIGNED, naming this
      role, this action, the blast radius and the rollback. NO GO WITHOUT BOTH.

STEPS:
  1. Open a deploy-ledger entry in org/critical_paths/change_management/ (and its .open_deploys/ marker)
     named with `iamroles-fwd5-narrowing`, before anything else.
  2. Apply the patch to the terraform file, then `safe-apply` PLAN in that module. STOP if the plan shows
     anything other than the one in-place update of the one policy that drops the one action. A wider plan
     is a surprise row and a halt, not a judgment call.
  3. `safe-apply` the plan; commit the .tf change through safe-commit under your author line.
  4. Read the change: simulate-principal-policy on the role for the removed action (expect implicitDeny)
     and for one retained action on the same statement (expect allowed, the control). Quote both raw JSON
     results in deliverables/0.7.0_AE_CloudOps~Z/fwd5/OUTCOME.md.
  5. Wait out the observation window PREDICTION.json names (the consumer run it waits for), then read what
     broke: the consumers' own run results and any AccessDenied for the role in that window. Write
     OUTCOME.md: observed breaks, and one line `MATCHES-PREDICTION: yes` or `MATCHES-PREDICTION: no`.
  6. If anything broke that matters, ROLL BACK at once with the named rollback (revert + safe-apply), then
     record it. A mismatch is a finding; hiding it is the failure.
  7. Close the ledger entry.
```

## DEPENDENCIES

`IAM-v-3` complete AND both never-widen halves SIGNED. This order is `staged` until the issuer's GO, which it sends
once both hold and has amended `<paths>` to add the one terraform file.

## BOUNDS

```
ONE ACTION, ONE ROLE, ONE FILE. Nothing else on the role moves.
safe-apply only (CLAUDE.md NEVER-9); the deploy ledger opens first and closes last (NEVER-2).
C-ANALYZER-PRICED-FIRST + G-25: no Access Analyzer.  G-21: no alert, alarm, monitor or schedule.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/fwd5/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-v-4.narrow-and-read-the-outcome-against-the-prediction.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-AEC-S<k>`, `"fabric": "site-z"`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-v-4"><invocation>grep -c '"EvalDecision": "implicitDeny"' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/fwd5/OUTCOME.md</invocation><expect>1 or greater -- the removed action now reads implicitDeny on the live role, so the narrowing landed; a "No such file" error means it was not done</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-v-4"><invocation>grep -c -E '^MATCHES-PREDICTION: (yes|no)$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/fwd5/OUTCOME.md</invocation><expect>exactly 1 -- the outcome is read against the prediction and stated either way; a `no` passes this criterion and is graded at AC4</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-v-4"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-fwd5-narrowing') closed=\$(ls org/critical_paths/change_management/ | grep -c 'iamroles-fwd5-narrowing')"</invocation><expect>`open=0` and `closed=` 1 or greater -- the deploy ledger was opened and closed for this act</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-v-4" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming
  3.0.0_SA_CVO~Z): was the check believed -- the prediction on record before the change, the outcome read in the
  window it named, and the two agreeing (or the disagreement found, said and rolled back)?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>staged</status>
<round>5</round>
<slot>0.7.0_AE_CloudOps~Z</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-v-4</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 5) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-4 slug @3f69d8a895 -> `ROUND_ANALYSIS.round4.md` @20c2fcabe8 E3 ("a WORLD act ... carries its own never-widen pair") -> L5 round-5 decomp (issuer rulings 1 and 2) -> this issuance.
**Chain:** v-3 -> v-4. **Risk WORLD:** an IAM change on a live role; one permission, a named rollback, a signed pair.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 220`, BUDGET REACHED, 1 of 6 carriers, C1=23, C2=22 PARTIAL (0 of 22 scanned), rc=3; PARTIAL_OR_BLIND, not read as clean. The assignee reads .open_deploys/ for its module before step 1.
comp-iam: RUN -- `bash .tools/comp-iam stats` from the main checkout: 214 IAM roles parsed / 196 services / 1154 operations; the role is chosen by v-3 and must be declared.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 1 of 1 (the analysis names E3 WORLD with its own pair; the module is unknown until v-3, so comp-blast is v-3's and is quoted in PREDICTION.md).
</preflight>

**Preflight disposition:** checks dry-run at the base `e9bda7b982`: AC1 base: FAIL as expected (file absent); AC2 base: FAIL as expected (file absent); AC3 base: FAIL as expected (`open=0 closed=0`).
