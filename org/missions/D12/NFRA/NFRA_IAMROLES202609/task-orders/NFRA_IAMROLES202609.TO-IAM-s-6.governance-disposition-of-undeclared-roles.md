# NFRA_IAMROLES202609.TO-IAM-s-6 -- The GOVERNANCE DISPOSITION of the undeclared roles: in-code, or a recorded and OWNED exemption

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~3</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; acceptance property 1)

```
IAM-s-6 mirrors manifest row S6. ACT: the GOVERNANCE DISPOSITION of the undeclared roles -- for
EACH one, either it goes in code, or it carries a RECORDED, OWNED exemption.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-4  Every role we run is either written down in our code or is a recorded, owned exception
         DONE WHEN  APPLIED -- each one is either in code or carries a named owner and a reason
         ACCEPT     There is no role running that nobody wrote down and nobody decided to leave
                    out. Something deliberately kept outside the normal way of doing things says
                    who decided that and why.

⛔ THIS IS THE GOVERNANCE HALF AND ONLY THE GOVERNANCE HALF. The question you answer is
"SHOULD THIS ROLE BE IN CODE AT ALL". The question you DO NOT answer is "IS THIS ROLE
OVER-GRANTED". They are two remedies and THEY DO NOT MOVE TOGETHER.

THE SHAPE IS CLOSED AT THE CUT: a deliverable at
    org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md
with one line per member of IAM-s-5's set, each carrying the literal token `IN-CODE` or `EXEMPT`,
and every `EXEMPT` line ALSO carrying `owner=<name> reason=<text>` on that same line.
AN EXEMPTION WITHOUT AN OWNER AND A REASON IS THE ROT WITH A TIDIER LABEL -- FWD-4's ACCEPT says in
terms that something deliberately kept outside the normal way of doing things SAYS WHO DECIDED THAT
AND WHY. A blank owner is not a disposition.

⭐ ONE DISPOSITION WILL NOT FIT ALL SIXTEEN, AND THE L5 LANE MEASURED WHY. The set is NOT a
homogeneous population:
  - `ecsTaskExecutionRole`, `rds-monitoring-role`, `vpc-flow-logs-role` are AWS SERVICE-DEFAULT
    roles that a console or service action mints. Their governance answer is PLAUSIBLY "recorded
    exemption, correctly outside our Terraform" -- but that is a finding for you to make, not one
    to inherit from this sentence.
  - `portal-auth-lambda-role` and `opal-data-refresh-lambda-role` are PRODUCTION SURFACES ON THE
    SERVING PATH. An exemption here is a much heavier claim.
  - `lambda-test-role` READS AS RESIDUE.
ONE CELL ANSWERING BOTH QUESTIONS ACROSS THAT SPREAD WOULD ANSWER ONE OF THEM BADLY FOR EVERY
MEMBER. That is the measured argument for C-TWO-REMEDIES, and it is why S5 and S6 are separate
rows by contract.
```

## DEPENDENCIES

This cell depends on: **IAM-s-5** (the reconciler), keyed to OBSERVED COMPLETION -- its deliverable
exists and its criteria passed -- never to a status word. You hold IAM-s-5 yourself, first in this
queue, so you carry its context and its enumerated set forward.

⛔ DISPOSE OF THE SET IAM-s-5 ESTABLISHED AT ITS OWN VINTAGE, including any member it classed as
ARRIVED. If IAM-s-5 found the count moved off 16, dispose of what it actually found and say so.

## BOUNDS -- what this cell may not cross

```
⛔⛔ C-TWO-REMEDIES (D6) IS THIS CELL'S GOVERNING BOUND AND IT CUTS BOTH WAYS:
    You may NOT narrow a permission, revoke a grant, or recommend either.
    You may NOT read a PERMISSIONS finding as a GOVERNANCE answer.
A role can be perfectly scoped and still ungoverned; a role can be properly declared in code and
still wildly over-granted. Deciding one tells you NOTHING about the other. If you find yourself
writing "this role is fine because its permissions are narrow", STOP -- that is the conflation the
constraint exists to prevent, and it is a surprise row.

⛔ AN EXEMPTION IS A DECISION SOMEONE MAKES, NOT ONE YOU MINT. You are a worker with no send tool
and you cannot obtain a sign-off. Where a member plainly needs an owner you cannot name, record the
disposition as EXEMPT with `owner=UNASSIGNED` and a reason stating what decision is owed and by
whom, AND FILE A SURPRISE ROW naming it. Do not invent an owner, and do not quietly mark it
IN-CODE to make the line pass.

DO NOT MODIFY ANY TERRAFORM AND DO NOT CREATE, DELETE OR EDIT ANY ROLE. This cell writes an
assessment. Adopting a role into code is a later act under a change-management entry, by a seat
with that lane -- it is not this cell and it is not this round.

EVERY NUMBER CARRIES ITS DENOMINATOR AND ITS VINTAGE (acceptance property 1).

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED; PRD section 4).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam (L5 battery, RUN): 195 TF roles / 188 services / 1084 operations / 304 gaps.
⛔ BLINDNESS STATED AND IT MATTERS HERE SPECIFICALLY: comp-iam parses role resources IT CAN
RESOLVE IN TERRAFORM SOURCE, and its own run emits two NOTEs that role labels `orchestrator` and
`scheduler` were REUSED ACROSS MODULES and silently mis-linked pre-fix. SO comp-iam's silence about
a role is NOT evidence that the role is undeclared -- it may be evidence about the parser. A role
you cannot find in Terraform via comp-iam is a role to look for BY NAME before you class it EXEMPT.
Classing a declared-but-unparsed role as EXEMPT would manufacture a governance finding.

comp-find --corpus aws (L5 battery, RUN): DECLARED=203, LIVE-no-DECLARED=16 of 219 nodes, vintage
2026-09-10 03:31:02 UTC. `LIVE-no-DECLARED` is a DRIFT CLASS over live nodes -- a different plane
from comp-iam's Terraform parse. DO NOT SUBTRACT 195 FROM 203.

brief F9 (via the PRD, one instrument not two): the INSTANCE is discharged and the CLASS RE-ARMS ON
ONBOARDING. Whatever disposition you write, the mechanism that lets a new undeclared role appear
tomorrow is not closed by disposing of today's sixteen. Say so; do not build a monitor for it
(G-21), and do not treat it as this cell's failure.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-6.governance-disposition-of-undeclared-roles.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-6"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md && grep -c -E 'IN-CODE|EXEMPT' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 16 or greater -- every member of the set IAM-s-5 established carries a governance disposition; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-6"><invocation>grep -E 'EXEMPT' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c -v -E 'owner=[^ ]+ +reason='</invocation><expect>a count of 0 -- no EXEMPT line lacks BOTH a named owner and a reason, which is FWD-4's ACCEPT rendered mechanically; an exemption without an owner and a reason is the rot with a tidier label</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-6"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md && grep -c -i -E 'narrow this|revoke|over-granted|remove permission|least-privilege fix' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 0, printed -- C-TWO-REMEDIES honoured mechanically: the governance half did not stray into the permissions half; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-6"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md && grep -c -i -E 're-arms|onboarding' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 1 or greater -- brief F9 carried: the INSTANCE is discharged and the CLASS re-arms on onboarding, stated rather than left implied by a set that looks closed; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-6" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): every member of the set carries a disposition -- coverage over the set, not a sample
- **AC2** (mechanical): FWD-4's ACCEPT rendered as a NEGATIVE census -- no EXEMPT line is missing its owner or its reason
- **AC3** (mechanical): C-TWO-REMEDIES honoured -- the governance half stayed out of the permissions half
- **AC4** (mechanical): the class-vs-instance distinction from brief F9 survives into the deliverable, so a disposed set is not mistaken for a closed mechanism
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): whether each disposition actually FITS ITS MEMBER across a set that spans AWS service-default roles, production serving surfaces and apparent residue -- an `EXEMPT owner=X reason=Y` line passes AC2 whatever the reason says. Whether a reader would accept these as decisions rather than as paperwork is NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** C, position 2 of 2 (IAM-s-5 -> IAM-s-6). Handed to slot ~3 only when IAM-s-5 is terminal with a valid instance.
**Provenance:** the cell text mirrors PRD section 8 row S6 and the endpoint's FWD-4 verbatim. The heterogeneity argument is decomposition section 1a, which the L5 lane derived from the enumerated members rather than from the constraint's say-so -- and which it recorded as arguing for C-TWO-REMEDIES harder than the PRD does.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project; G-21 binds this cell.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD, plus the two NOTEs on reused `orchestrator`/`scheduler` labels. That parser blindness is inlined in BATTERY FINDINGS because at THIS cell it could manufacture a governance finding.
comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16, vintage 2026-09-10 03:31:02 UTC.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable; DECLARED BLINDNESS on the L1 brief, so F9 reaches this order as the PRD's rendering.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell writes a governance assessment and touches no route, cache key, data prop, gold script or deletable resource. comp-blast is NOT owed: this cell deletes nothing and narrows nothing.
