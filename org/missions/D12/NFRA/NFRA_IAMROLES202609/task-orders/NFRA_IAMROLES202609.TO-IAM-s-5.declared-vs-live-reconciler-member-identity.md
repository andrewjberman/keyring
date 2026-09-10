# NFRA_IAMROLES202609.TO-IAM-s-5 -- The DECLARED-vs-LIVE RECONCILER: which live roles exist in code and which do not. RECONCILES ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~3</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; acceptance property 1)

```
IAM-s-5 mirrors manifest row S5. ACT: the DECLARED-vs-LIVE RECONCILER -- which live roles exist in
code and which do not. ⛔ IT RECONCILES ONLY; IT DOES NOT DISPOSE.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-4  Every role we run is either written down in our code or is a recorded, owned exception
         DONE WHEN  APPLIED -- each one is either in code or carries a named owner and a reason
         ACCEPT     There is no role running that nobody wrote down and nobody decided to leave
                    out. Something deliberately kept outside the normal way of doing things says
                    who decided that and why.
         BOUND BY   these are TWO remedies, not one. Whether a role should be in code at all is a
                    different question from whether it is over-granted, and a single cell doing
                    both will do one badly.

YOUR HALF IS THE RECONCILIATION. IAM-s-6 does the governance disposition, on YOUR output.

⭐ THE SINGLE MOST IMPORTANT THING THIS CELL ESTABLISHES, AND THE L5 LANE DELIBERATELY DID NOT:
    MEMBER IDENTITY.
The undeclared COUNT has held at exactly 16 across THREE vintages and TWO instruments while the
population moved 208 -> 216 -> 219. That is strong support for the claim that the 16 are a settled
SET. ⛔ BUT A STABLE COUNT IS NOT PROOF THE MEMBERS MATCH. A stable 16 is equally consistent with
"the same 16" and with "one left and one arrived". THE L5 LANE DID NOT MEASURE MEMBER IDENTITY AND
DOES NOT CLAIM IT. ESTABLISHING IT IS THIS CELL.

THE 16 AT THE L5 LANE'S OWN VINTAGE (2026-09-10 03:31:02 UTC), enumerated so you reconcile a SET
and not a count:
    bd-merge-daily-lambda-role            finbert-ec2-backfill-role
    bd-pipeline-task-role                 lambda-ec2-runtime-monitor-role
    codebuild-semantic-clustering-role    lambda-test-role
    ecsTaskExecutionRole                  opal-data-refresh-lambda-role
    portal-auth-lambda-role               opal-smartx-lambda-role
    portfolio-management-lambda-role      rds-monitoring-role
    seeking-alpha-scraper-role            sentiment_query_api-role
    vpc-flow-logs-role                    workspace-sync-lambda-role

RE-MEASURE AT YOUR OWN VINTAGE and class every member against that list as SAME, ARRIVED or LEFT.
If the count is still 16 but a member changed, THAT IS THE FINDING and it is worth more than the
count ever was.

THE SHAPE IS CLOSED AT THE CUT: a deliverable at
    org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/DECLARED_VS_LIVE.md
carrying a section headed `## THE UNDECLARED SET` with one `- <role-name>` line per member, and a
section headed `## MEMBER IDENTITY` classing each against the list above.
```

## DEPENDENCIES

This cell depends on: none -- IAM-s-5 is a ROOT and is ready at issuance.

Downstream, so you know what your output must be usable BY (you do not build it):
IAM-s-6 takes YOUR set and gives each member a GOVERNANCE disposition.

## BOUNDS -- what this cell may not cross

```
⛔ C-TWO-REMEDIES (D6). THIS ROW RECONCILES; IT DOES NOT DISPOSE. You may not write that a role
should be removed, should be adopted into Terraform, should be granted an exemption, or is
over-granted. Those are IAM-s-6's (governance) and IAM-s-1's (permissions) and they DO NOT MOVE
TOGETHER. Manifest rows S5 and S6 are separate BY CONTRACT for exactly this reason. Reconcile and
STOP.

⛔ A THIRD FIGURE EXISTS AND IT IS A DIFFERENT PLANE -- this is the trap most likely to catch this
specific cell, because it looks exactly like a drift finding:
    comp-iam parses 195 IAM roles from TERRAFORM SOURCE.
    comp-find --corpus aws reports DECLARED=203 as a drift class over LIVE nodes.
THESE ARE DIFFERENT PLANES AND MUST NOT BE SUBTRACTED. comp-iam measures the PARSER's reach as much
as the estate's -- its own run emits two NOTEs that role labels `orchestrator` and `scheduler` were
reused across modules and silently mis-linked pre-fix. NO CELL MAY PRESENT THE 195-vs-203 DELTA AS
AN UNDECLARED-ROLE FINDING. ⛔ STATE WHICH PLANE YOUR NUMBER IS ABOUT, IN THE SENTENCE.

EVERY NUMBER CARRIES ITS DENOMINATOR AND ITS VINTAGE (acceptance property 1). The instrument prints
its own `built:` line; that IS the vintage. Print it.

A VALUE MUST CARRY ITS CLAIM: `measured` for what you read live, `inferred` for what you derived.

DO NOT MODIFY ANY TERRAFORM. This cell reads. DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR
NOTIFICATION (G-21, ARMED; PRD section 4).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-find --corpus aws (L5 battery, RUN) -- the instrument this cell re-runs at its own vintage:
    comp-find '.' --corpus aws IAM_ROLE
    VINTAGE      built from the estate 2026-09-10 03:31:02 UTC; manifest 5361815924ce
    DENOMINATOR  219 hit(s) across 219 aws node(s) scanned [corpus=aws types=IAM_ROLE]
    DRIFT        DECLARED=203  LIVE-no-DECLARED=16     (203 + 16 = 219, reconciles exactly)

THE THREE-VINTAGE TABLE, which is the evidence for "settled SET" and against any hardcoded number:
    brief F2  @1a90986047        208 population,  --  DECLARED,  16 LIVE-no-DECLARED
    brief F2a "merged head"      216 population, 200 DECLARED,  16 LIVE-no-DECLARED
    L5 lane, 2026-09-10 03:31Z   219 population, 203 DECLARED,  16 LIVE-no-DECLARED

ARMED ROW, OWNED ELSEWHERE, AND IT IS ABOUT YOUR ROW SPECIFICALLY -- do NOT re-file it and do NOT
treat it as blocking: `NFRA_IAMROLES202609-Z-S1` (OBSERVATION, ARMED, disarm_owner
`1.0.0_SA_CTO~Z`) records that PRD section 8's S5 evidence cell states "16 of 208" and
"DECLARED=200 LIVE-no-DECLARED=16" in ONE SENTENCE, and those denominators are 208 and 216 and do
not reconcile. It is a stale denominator carried beside a fresher one. Your re-measurement at your
own vintage is what makes it harmless.

comp-iam (L5 battery, RUN): 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on
wafv2 (UNMODELED) and UNMAPPED-METHOD on two services.

⭐ THE SET IS NOT HOMOGENEOUS AND THE L5 LANE FLAGGED IT FOR YOUR SUCCESSOR: `ecsTaskExecutionRole`,
`rds-monitoring-role` and `vpc-flow-logs-role` are AWS SERVICE-DEFAULT roles a console or service
action mints; `portal-auth-lambda-role` and `opal-data-refresh-lambda-role` are PRODUCTION SURFACES
ON THE SERVING PATH; `lambda-test-role` reads as RESIDUE. Note the character of each member as you
reconcile -- IAM-s-6 needs it -- but do NOT dispose of any of them.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-5.declared-vs-live-reconciler-member-identity.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-5"><invocation>comp-find '.' --corpus aws IAM_ROLE --limit 5</invocation><expect>a printed DENOMINATOR line giving the IAM_ROLE node count and a vintage line naming when the graph was built -- the live plane re-measured at this cell's own vintage rather than inherited from the decomposition</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-5"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/DECLARED_VS_LIVE.md && grep -c -E 'DECLARED=[0-9]+' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/DECLARED_VS_LIVE.md</invocation><expect>a count of 1 or greater -- the reconciliation prints the declared figure with its drift class; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-5"><invocation>sed -n '/## THE UNDECLARED SET/,/^## /p' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/DECLARED_VS_LIVE.md | grep -c '^- '</invocation><expect>a count of 16 -- the settled set ENUMERATED BY NAME, one member per line, so IAM-s-6 disposes of a set and not a count; a count other than 16 is itself the finding and belongs in a surprise row before this criterion is recorded</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-5"><invocation>sed -n '/## MEMBER IDENTITY/,$p' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/DECLARED_VS_LIVE.md | grep -c -E 'SAME|ARRIVED|LEFT'</invocation><expect>a count of 16 or greater -- every member classed against the L5 lane's enumerated list, establishing MEMBER IDENTITY rather than resting on a stable count</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-5"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/DECLARED_VS_LIVE.md && grep -c -i -E 'should be removed|should be adopted|exemption granted|is over-granted|narrow this role' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/DECLARED_VS_LIVE.md</invocation><expect>a count of 0, printed -- C-TWO-REMEDIES honoured mechanically: this cell RECONCILED and disposed of nothing; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="IAM-s-5" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the live plane is RE-MEASURED at this cell's own vintage, with a denominator, not inherited
- **AC2** (mechanical): the reconciliation states the declared figure and its drift class
- **AC3** (mechanical): the undeclared set is ENUMERATED BY NAME -- a count cannot be disposed of, and this is what IAM-s-6 consumes
- **AC4** (mechanical): MEMBER IDENTITY established -- the thing the L5 lane explicitly did not claim and handed to this cell
- **AC5** (mechanical): C-TWO-REMEDIES honoured NEGATIVELY -- no disposition language leaked into the reconciliation
- **AC6** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): whether the reconciliation genuinely separates the two planes it is warned about (the Terraform-parse plane and the live-graph drift plane) without presenting either as evidence about the other, and whether the member-identity finding is grounded rather than asserted. NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** C, position 1 of 2 (IAM-s-5 -> IAM-s-6). A ROOT: cuttable and spawnable at issuance.
**Provenance:** the cell text mirrors PRD section 8 row S5 and the endpoint's FWD-4 verbatim. The enumerated 16 and the three-vintage table are decomposition section 1a, measured by the L5 lane on its own instrument at 2026-09-10 03:31:02 UTC. The MEMBER IDENTITY assignment is decomposition section 1a's own explicit hand-off: "This lane did not measure member identity against the brief's list and does not claim it; IAM-s-5 establishes it."
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project; G-21 binds this cell.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED). The 195-vs-203 plane separation is inlined in BOUNDS because this is the cell where mistaking it for drift would produce a false finding.
comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16, vintage 2026-09-10 03:31:02 UTC, manifest 5361815924ce.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable; DECLARED BLINDNESS on the L1 brief, so F2/F2a/F3 reach this order as the PRD's rendering, one instrument and not two.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell reconciles two read-only planes and touches no route, cache key, data prop, gold script or deletable resource.
