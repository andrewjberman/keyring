# NFRA_IAMROLES202609.TO-IAM-s-2 -- The POSTURE NUMBER: one figure carrying its denominator and its vintage

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-1; acceptance property 1)

```
IAM-s-2 mirrors manifest row S2. ACT: produce THE POSTURE NUMBER -- one figure for the estate's
least-privilege standing, carrying its DENOMINATOR and its VINTAGE, rolled up from IAM-s-1 AND
NOTHING ELSE.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-1  Someone can state our least-privilege posture with a number, what it is out of, and
         when it was taken
         DONE WHEN  EXERCISED -- a reviewer has actually answered the question with that
                    evidence attached, rather than an opinion
         ACCEPT     Asked "are we following least privilege?", someone answers with how many
                    things were checked, out of how many exist, and as of when. "Nobody has
                    measured it" stops being the honest answer.

THE RENDERING SHAPE IS CLOSED AT THE CUT so that this order's criteria and your build agree.
The deliverable carries, on ONE line:
    POSTURE: <n> of <d> ... vintage <YYYY-MM-DD>
where <n> and <d> are integers and <d> is READ AT RENDER TIME. Prose around it is yours.

⛔ IT IS A ROLLUP OF IAM-s-1 AND NOTHING ELSE. Do not fold in comp-iam's 304 gaps, do not fold in
the 16 undeclared roles, do not fold in the condition axis. Each of those is a different plane
with a different denominator, and a composite figure that mixes them answers no question at all.
```

## DEPENDENCIES

This cell depends on: **IAM-s-1** and **IAM-s-3**, both keyed to OBSERVED COMPLETION -- deliverables
that exist and whose criteria passed -- never to a status word. You hold both yourself, earlier in
this queue, so you carry their context forward.

⛔ PRD section 7 is explicit and it is a BOUND, not a preference: "Nothing that quotes a
permission-level number can be graded before it." The posture number's honesty depends on
IAM-s-3's coverage vocabulary. A number rendered before that vocabulary exists cannot say what it
could not see, which is the one thing C-COVERAGE-OVER-COUNT requires of it.

## BOUNDS -- what this cell may not cross

```
⛔ DO NOT HARDCODE 208. This is the single most specific bound the L5 battery added to any cell,
and it was added because the denominator MOVED WHILE THE DECOMPOSITION WAS BEING WRITTEN:

    vintage                       population   DECLARED   LIVE-no-DECLARED
    brief F2  @1a90986047            208          --            16
    brief F2a "merged head"          216         200            16
    L5 lane, 2026-09-10 03:31Z       219         203            16

THE POPULATION MOVED TWICE. THE UNDECLARED COUNT HELD AT 16 ACROSS ALL THREE. The denominator is
a LIVE QUANTITY and must be READ AT RENDER TIME with its vintage printed beside it, NEVER
inherited from the brief or from this order. If you find yourself typing a role-population integer
that you did not just measure, STOP -- that is the failure FWD-1 exists to prevent, and quoting it
inside the cell that commissions FWD-1 would be the project failing at its own thesis.

C-COVERAGE-OVER-COUNT: a SMALLER number that states what it could not see BEATS a larger one that
does not. If IAM-s-3's vocabulary says a slice was unobservable, the posture line says so.

A VALUE MUST CARRY ITS CLAIM: the number is `measured` and says so in a field a consumer can
reject on. A denominator you inferred is `inferred` and is labelled as such.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED; PRD section 4).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-find --corpus aws (L5 battery, RUN): the instrument that carries its own vintage.
    comp-find '.' --corpus aws IAM_ROLE
    VINTAGE      built from the estate 2026-09-10 03:31:02 UTC
    DENOMINATOR  219 hit(s) across 219 aws node(s) scanned [corpus=aws types=IAM_ROLE]
    DRIFT        DECLARED=203  LIVE-no-DECLARED=16   (203 + 16 = 219, reconciles exactly)
⛔ THE `built:` LINE IS THE VINTAGE. Print it. A denominator without a vintage is the defect.

⛔ A THIRD FIGURE EXISTS AND IT IS A DIFFERENT PLANE. comp-iam parses 195 IAM roles from
Terraform, against comp-find's DECLARED=203. DO NOT SUBTRACT THEM and do not present the delta as
drift. comp-iam measures the PARSER's reach as much as the estate's. State which plane your
number is ABOUT, in the sentence.

ARMED ROW YOU SHOULD KNOW ABOUT, owned elsewhere and NOT yours to disarm:
`NFRA_IAMROLES202609-Z-S1` (OBSERVATION, ARMED, disarm_owner `1.0.0_SA_CTO~Z`) records that PRD
section 8's S5 evidence cell states "16 of 208" and "DECLARED=200 LIVE-no-DECLARED=16" in ONE
SENTENCE, and those denominators are 208 and 216 and do not reconcile. That is exactly the failure
this cell exists to prevent, sitting in the PRD that commissions it. It is MITIGATED for you by
this bound. Do not re-file it; do not treat it as blocking.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-2.posture-number-with-denominator-and-vintage.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md && grep -c -E 'POSTURE: [0-9]+ of [0-9]+' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md</invocation><expect>a count of 1 or greater -- the figure and its denominator are on one line in the closed shape; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md && grep -c -E 'vintage [0-9]{4}-[0-9]{2}-[0-9]{2}' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md</invocation><expect>a count of 1 or greater -- the vintage travels with the number in an ISO date; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md && grep -c '208' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md</invocation><expect>a count of 0, printed -- the brief's stale denominator is nowhere in the deliverable, so the figure was READ at render time rather than inherited; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md && grep -c -i -E 'unobservable|could not see|not observed' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/POSTURE_NUMBER.md</invocation><expect>a count of 1 or greater -- the number states what it could NOT see, carrying IAM-s-3's coverage vocabulary forward (C-COVERAGE-OVER-COUNT); NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-2" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): one figure, with its denominator, in the closed rendering shape
- **AC2** (mechanical): the vintage travels with the figure -- acceptance property 1
- **AC3** (mechanical): the NEGATIVE bound the L5 battery added, mechanically -- 208 appears nowhere, so the denominator cannot have been inherited from the brief
- **AC4** (mechanical): coverage travels with the count, so the number can say what it could not see
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): FWD-1's ACCEPT in plain English -- asked "are we following least privilege?", does this deliverable let someone answer with how many things were checked, out of how many exist, and as of when, such that "nobody has measured it" stops being the honest answer? Whether the figure is an ANSWER rather than an artefact is NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** A, position 3 of 4 (IAM-s-1 -> IAM-s-3 -> IAM-s-2 -> IAM-s-9). Handed to slot ~1 only when BOTH IAM-s-1 and IAM-s-3 are terminal with valid instances.
**Provenance:** the cell text mirrors PRD section 8 row S2 and the endpoint's FWD-1 verbatim. The DO-NOT-HARDCODE-208 bound is decomposition section 2c, grounded on the three-vintage table at section 1a which the L5 lane measured on its own instrument rather than inheriting.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project; G-21 binds this cell and is carried into BOUNDS.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED). The 195-vs-203 delta is a PLANE difference and this order forbids presenting it as drift.
comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16, vintage 2026-09-10 03:31:02 UTC; the instrument carries its own `built:` line, which is this cell's vintage carrier.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable; DECLARED BLINDNESS on the L1 brief.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell renders a figure from an upstream cell's output and touches no route, cache key, data prop, gold script or deletable resource.
