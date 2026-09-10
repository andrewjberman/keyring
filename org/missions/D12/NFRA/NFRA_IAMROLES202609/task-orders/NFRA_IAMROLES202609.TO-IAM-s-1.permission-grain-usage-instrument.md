# NFRA_IAMROLES202609.TO-IAM-s-1 -- EXTEND the working comp-iam-usage from ROLE grain to PERMISSION grain

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-2; acceptance properties 1, 3)

```
IAM-s-1 mirrors manifest row S1. ACT: EXTEND the working `comp-iam-usage` from ROLE grain to
PERMISSION grain -- for a given role, which GRANTED PERMISSIONS has it never used, over a stated
lookback.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-2  For any role, a reviewer can see which of its permissions it has never used
         DONE WHEN  EXERCISED -- real roles have been read and their unused permissions named,
                    over a stated lookback
         ACCEPT     Pick any role. A reviewer can see which of the things it is allowed to do it
                    has never actually done, and over what period that was judged.

WHAT ALREADY EXISTS, AND IT IS THE WHOLE REASON THIS CELL IS AN EXTENSION AND NOT A BUILD:
`.tools/comp-iam-usage` is BUILT, tracked, executable, and its self-test passes rc=0 with 9 of 9
assertions PASS. It forwards to `org/modules/graph/comp_iam_usage.py`. It answers the IDENTITY
plane -- `role-cold` -- and carries an explicit UNKNOWN band plus the assertions
`blind_is_unknown_NOT_unused` and `breakglass_never_used_is_stillborn_NOT_reap`. THE PERMISSION
AXIS IS THE HALF THAT IS ABSENT. That is the whole of this cell.

THE SUBCOMMAND NAME IS CLOSED AT THE CUT so that this order's criteria and your build agree:
add `permission-cold`, taking `--role <name>` and `--lookback <days>`. Its output names the role,
prints the lookback in days, and for each GRANTED permission renders one of: used | never-used |
unobservable. A printed DENOMINATOR (how many granted permissions were examined) travels with it.

THE THREE EXISTING ROLE-GRAIN SURFACES MUST SURVIVE: `role-cold`, `who-can-reach`, `reach-check`.
An extension that removes or renames any of them has broken working code.
```

## DEPENDENCIES

This cell depends on: none -- IAM-s-1 is a ROOT and is ready at issuance.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word.

Downstream, so you know what your output must be usable BY (you do not build these):
IAM-s-3 builds the coverage vocabulary ON your output; IAM-s-2 rolls your output up into the posture
number and NOTHING ELSE; IAM-s-8 uses your output as the input to a pre-flight blast radius.

## BOUNDS -- what this cell may not cross

```
C-EXTEND-NOT-BUILD (ruling 20): EXTEND the working tool. A cell written as greenfield RE-BUYS
passing, self-testing code. The L5 lane exercised this rather than inheriting it:
`comp-iam-usage self-test` returns rc=0, 9 of 9 assertions PASS. That self-test IS THE REGRESSION
BAR -- an extension that leaves any of the 9 red has broken working code.

C-ANALYZER-PRICED-FIRST + G-25: AWS Access Analyzer is the FALLBACK and NO PER-ROLE PRICE HAS BEEN
READ BY ANYONE. Taking it off the shelf is a VENDOR call requiring Andrew's explicit per-use word.
YOU MAY NOT REACH FOR IT on the grounds that it is available -- availability is not authorization.
If you conclude the cell cannot be served without it, file a surprise ROW and STOP on that
criterion. Do not call it.

C-DESIRED-UNTIL-EXERCISED: anything you read from a policy DOCUMENT is DESIRED. Only usage
telemetry moves a permission to never-used. Say which plane each claim is about, in the sentence.

FWD-7's DISCIPLINE IS ALREADY LAW AT ROLE GRAIN AND YOU MAY NOT REGRESS IT AT PERMISSION GRAIN:
a permission nobody could observe must NEVER render as a permission shown clean. `unobservable` is
a distinct rendering from `never-used`. IAM-s-3 owns the VOCABULARY; you own not breaking it.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION. The standing moratorium (G-21) is
ARMED and PRD section 4 puts this out of scope.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam (L5 battery, RUN): 195 TF roles / 188 services / 1084 operations / 304 gaps. BLINDNESS
STATED: it emits `wafv2:UNMODELED` and `UNMAPPED-METHOD` for two services -- it does not model
every action namespace, so its 304-gap figure is a FLOOR on the DESIRED plane, not a population
claim. NO CRITERION HERE MAY CITE THE 304 AS A POPULATION.

comp-find --corpus aws (L5 battery, RUN): 219 IAM_ROLE nodes live, DECLARED=203,
LIVE-no-DECLARED=16, vintage 2026-09-10 03:31:02 UTC. A THIRD figure exists -- comp-iam parses 195
roles from Terraform -- and IT IS A DIFFERENT PLANE. DO NOT SUBTRACT 195 FROM 203. comp-iam
measures the PARSER's reach as much as the estate's; its own run emits two NOTEs that role labels
`orchestrator` and `scheduler` were reused across modules and silently mis-linked pre-fix.

comp-iam-usage self-test (L5 battery, EXERCISED at this cut): rc=0, 9 of 9 PASS, including the
RULE-22a fix-or-carry block naming comp-iam's three limits -- (a) (action,resource) blindness,
(b) 2+-ARN implicitDeny poisoning, (c) condition-block false-deny. Those three are FIXED or
CARRIED in the existing tool. AN EXTENSION THAT RE-INTRODUCES ANY OF THEM AT PERMISSION GRAIN IS A
REGRESSION, and (c) is the one most likely to bite you: a conditioned statement with no context is
UNKNOWN, never a deny.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/modules/graph/comp_iam_usage.py
.tools/comp-iam-usage
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-1.permission-grain-usage-instrument.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-1"><invocation>.tools/comp-iam-usage self-test | grep -c '\[PASS\]'</invocation><expect>a count of 9 or greater -- the pre-existing regression bar is still green; measured 9 at the cut, so a count below 9 means the extension broke working code</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-1"><invocation>.tools/comp-iam-usage permission-cold --role opal-data-refresh-lambda-role --lookback 90</invocation><expect>output naming the role, printing the lookback as 90 days, rendering each granted permission as used / never-used / unobservable, and printing a DENOMINATOR of granted permissions examined; measured rc=2 (subcommand absent) at the cut, so only a real build satisfies this</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-1"><invocation>.tools/comp-iam-usage --help | grep -c -E 'role-cold|who-can-reach|reach-check'</invocation><expect>a count of 3 or greater -- all three pre-existing role-grain surfaces survived the extension (C-EXTEND-NOT-BUILD, mechanically); measured 5 at the cut</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-1"><invocation>.tools/comp-iam-usage self-test | grep -c -i 'permission'</invocation><expect>a count of 1 or greater -- at least one self-test assertion now exercises the PERMISSION grain; measured 0 at the cut, so this criterion is NOT satisfiable by the current tool and only a real extension moves it</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-1" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the 9 existing assertions are still green -- the C-EXTEND-NOT-BUILD regression bar
- **AC2** (mechanical): the permission grain actually answers for a REAL role over a STATED lookback, with a denominator -- this is FWD-2's DONE WHEN, exercised
- **AC3** (mechanical): the extension EXTENDED rather than replaced -- the three role-grain surfaces survive
- **AC4** (mechanical): the new grain carries its own regression bar, so the next extension cannot silently break it
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): FWD-2's ACCEPT in plain English -- pick any role, and a reviewer can see which of the things it is allowed to do it has never actually done, and over what period that was judged. Whether the rendering genuinely answers that for a reader who did not build it is NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED on Andrew's "Confirm on IAMROLES202609.") -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** A, position 1 of 4 (IAM-s-1 -> IAM-s-3 -> IAM-s-2 -> IAM-s-9). This is the critical path.
**Provenance:** the cell text mirrors PRD section 8 row S1 and decomposition section 1a RE-GROUNDING 1. Nothing in the manifest was re-measured at L4, so every `measured` claim carries the BRIEF's vintage @cbe45b0db4; the L5 battery re-grounded S1 and it HELD EXACTLY (self-test rc=0, 9 of 9 PASS), which is why C-EXTEND-NOT-BUILD is EXERCISED here rather than inherited.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers; the default 90s budget returns a PREFIX reporting 7 armed gates and says so -- the complete compile reports 26). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project. G-25 (vendor egress) and G-21 (alerting moratorium) bind this cell and are carried into BOUNDS.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD on two services, so 304 is a floor on the DESIRED plane and not a population.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable. DECLARED BLINDNESS: the L5 lane did NOT read the L1 brief, so every F-number in this order is the PRD's rendering of the brief, one instrument and not two.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses (comp-routes, comp-cache, comp-transform, comp-pipescript, comp-blast) DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, data prop, gold script or deletable resource; it extends a read-only assessment tool.
