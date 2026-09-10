# NFRA_IAMROLES202609.TO-IAM-s-9 -- The RE-RUN HARNESS: repeatable on demand by someone who did not build it, and NEVER scheduled

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-8; acceptance property 5)

```
IAM-s-9 mirrors manifest row S9. ACT: build the RE-RUN HARNESS -- the whole assessment repeatable
by someone who did not build it, producing a COMPARABLE answer.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-8  The assessment can be re-run without doing it by hand again
         DONE WHEN  EXERCISED -- it has actually been re-run and produced a comparable answer
         ACCEPT     Someone can ask the same question next quarter and get an answer they can put
                    beside this one. It does not quietly stop happening because only one person
                    knew how to do it.

THE SHAPE IS CLOSED AT THE CUT so that this order's criteria and your build agree: a single
executable at
    org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh
taking `--dry-run` (prints every step it would run, in order, and exits 0 without touching AWS)
and a default mode that runs them. COMPARABILITY is the point: the denominator and vintage of
IAM-s-2's posture number travel with every run, so two runs can be put side by side.

⛔ BUILD-LADDER RUNG 2 -- COMPOSE, DO NOT MINT. The estate already has the instruments: this
harness ORCHESTRATES `comp-iam-usage` (role and permission grain), `comp-iam`, and
`comp-find --corpus aws`. A harness that reimplements what those already do has re-bought working
code, which is the same error C-EXTEND-NOT-BUILD names one cell upstream.
```

## DEPENDENCIES

This cell depends on: **IAM-s-2** and **IAM-s-3**, both keyed to OBSERVED COMPLETION. You hold both
yourself, earlier in this queue, so you carry their context forward. This is the LAST cell of
chain A and the last of the whole decomposition's depth.

## BOUNDS -- what this cell may not cross

```
⛔⛔ G-21 IS ARMED AND IT IS THE BOUND MOST LIKELY TO CATCH YOU BY ACCIDENT. The standing
alerting/monitor moratorium forbids minting any alert, alarm, monitor, SNS topic, freshness
checker, notification or SCHEDULE without Andrew's explicit ask. A RE-RUN HARNESS THAT ACQUIRES A
SCHEDULE BECOMES THE THING THE MORATORIUM FORBIDS.

    RE-RUNNABLE BY A PERSON ON DEMAND IS THE BAR. SCHEDULED IS NOT.

This is not a technicality: PRD section 4 already puts minting any alert, alarm, monitor or
notification OUT OF SCOPE, and the L5 battery made the carrier explicit at decomposition section
2c because a harness is exactly the artefact that tempts a cron. No EventBridge rule, no
EventBridge Scheduler entry, no cron line, no CloudWatch alarm, no SNS publish, no Lambda
schedule. If you believe the outcome cannot be met without one, FILE A SURPRISE ROW AND STOP ON
THAT CRITERION -- do not build it and do not ask for permission through a channel you do not have.

C-ANALYZER-PRICED-FIRST + G-25: the harness may not call AWS Access Analyzer. Availability is not
authorization; a per-role price has been read by nobody and taking it off the shelf is a VENDOR
call requiring Andrew's explicit per-use word.

⛔ AND THE HARNESS IS NOT A LICENCE TO WIDEN. It re-runs the assessment. It does not narrow a
permission, delete a role, or apply anything. A read-only harness is the whole deliverable.

COMPARABILITY REQUIRES THE DENOMINATOR AND THE VINTAGE TO TRAVEL. A re-run that prints a bare
number is not comparable to anything -- that is acceptance property 1 and it binds here too.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule (L5 battery, RUN to completion at --budget 500): GATES ARMED: 26. G-15..G-26 are the
twelve standing MORATORIA and THESE BIND EVERY PROJECT INCLUDING THIS ONE. G-21 is the alerting
moratorium named in BOUNDS above.
⚠ AN INSTRUMENT NOTE THAT IS ITSELF WORTH CARRYING: the DEFAULT 90-second budget returns a PREFIX
and says so -- it reported `GATES ARMED: 7`, and the complete compile at --budget 500 reports 26.
Quoting the prefix would have understated the armed set by 19. If your harness composes
comp-schedule, IT MUST PASS A BUDGET THAT COMPLETES, or it will quietly report a prefix as an
answer -- which is precisely the class of defect this project exists to eliminate.

brief F4 (via the PRD, one instrument not two): the closest existing thing to a re-run harness is
EXPLICITLY MARKED AS NOT SCHEDULABLE. That is the ancestor of this cell and of G-21's bite here.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-9.re-run-harness-composed-not-scheduled.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-9"><invocation>bash org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh --dry-run</invocation><expect>the harness prints every assessment step it would run, in order, and exits 0 without touching AWS -- this is FWD-8's EXERCISED bar met on the dry-run arm</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-9"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh && grep -c -i -E 'cloudwatch|sns|put-rule|schedule|alarm|crontab|cron ' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh</invocation><expect>a count of 0, printed -- G-21 honoured mechanically, the harness acquired no schedule, alarm or notification; NO OUTPUT AT ALL means the harness is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-9"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh && grep -c -E 'comp-iam-usage|comp-iam|comp-find' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh</invocation><expect>a count of 2 or greater -- the harness COMPOSES the estate's existing instruments rather than reimplementing them (build-ladder rung 2); NO OUTPUT AT ALL means the harness is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-9"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh && grep -c -i -E 'denominator|vintage' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh</invocation><expect>a count of 1 or greater -- the denominator and vintage travel with the run, which is what makes two runs COMPARABLE; NO OUTPUT AT ALL means the harness is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-9" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the harness actually runs and enumerates the assessment -- FWD-8's EXERCISED bar on the safe arm
- **AC2** (mechanical): G-21 honoured, mechanically and negatively -- the harness acquired no schedule, alarm or notification
- **AC3** (mechanical): it composes existing comp-tools instead of minting a runner -- build-ladder rung 2
- **AC4** (mechanical): comparability is built in, because a bare number is comparable to nothing
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): FWD-8's ACCEPT in plain English -- could someone who did not build this ask the same question next quarter and get an answer they can put beside this one, without it quietly stopping because only one person knew how? Whether the harness is genuinely re-runnable BY A STRANGER is NOT self-gradeable by its builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded, and give the harness's default (non-dry-run) mode its own internal budgets.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** A, position 4 of 4 and the deepest cell of the decomposition. Handed to slot ~1 only when BOTH IAM-s-2 and IAM-s-3 are terminal with valid instances.
**Provenance:** the cell text mirrors PRD section 8 row S9 and the endpoint's FWD-8 verbatim. The G-21 bound is decomposition section 2c, which named the carrier explicitly because a harness is the artefact most likely to acquire a schedule by accident.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers, 173.8 s, rc=0). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project. G-15..G-26 are the twelve standing moratoria and BIND EVERY PROJECT INCLUDING THIS ONE; G-21 is this cell's principal bound. The default 90 s budget returns a PREFIX reporting 7 and says so.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED).
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable; DECLARED BLINDNESS on the L1 brief (not read by the L5 lane), so brief F4 reaches this order as the PRD's rendering.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell composes read-only assessment tools and touches no route, cache key, data prop, gold script or deletable resource. comp-blast is NOT owed here: this cell deletes and narrows nothing.
