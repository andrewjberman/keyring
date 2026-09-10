# NFRA_IAMROLES202609.TO-IAM-s-4 -- The CONDITION AXIS reader: what a policy REQUIRES of a caller, not only what it scopes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~2</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-3; acceptance property 3)

```
IAM-s-4 mirrors manifest row S4. ACT: build the CONDITION AXIS reader -- for a given policy, what
does it REQUIRE OF THE CALLER (MFA, source address, tags, session age), not only what it lets the
caller touch.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-3  For any policy, a reviewer can see what it REQUIRES of the caller, not only what it lets
         them touch
         DONE WHEN  EXERCISED -- at least one real policy has been surfaced as perfectly scoped
                    and yet requiring nothing of whoever calls it
         ACCEPT     A rule that is careful about WHAT someone can touch but asks NOTHING about who
                    they are or how they proved it is visible as such. Being tightly scoped stops
                    being able to hide asking for no second factor.

THE THESIS, from brief F8 via the PRD: LEAST PRIVILEGE HAS TWO AXES AND THE ESTATE MEASURES ONE.
Every existing instrument answers "what resources does this statement scope". None answers "what
does this statement demand of whoever invokes it". A statement can be immaculately scoped to one
ARN and still require no second factor, no source restriction and no tag match -- and today that
reads as CLEAN.

THE SHAPE IS CLOSED AT THE CUT so that this order's criteria and your build agree: an executable at
    org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/condition-axis-reader.py
taking `--policy <path>`, printing PER STATEMENT what that statement REQUIRES of the caller, and
printing the literal token `REQUIRES-NOTHING` for any statement carrying no Condition block.
That token is the cell's whole point: it makes the absence VISIBLE instead of silent.
```

## DEPENDENCIES

This cell depends on: none -- IAM-s-4 is a ROOT and is ready at issuance.

⭐ YOU ARE A ROOT AND THAT IS A CORRECTION THE L5 LANE MADE ON PURPOSE. PRD section 7's sequencing
prose names only TWO independent roots (FWD-4 and FWD-6). But manifest row S4 carries
`depends_on: --`, so IAM-s-4 IS A FOURTH ROOT BY THE MANIFEST'S OWN DATA. The edges are the
carrier and they say four. You do not idle behind IAM-s-1.

Downstream, so you know what your output must be usable BY (you do not build it):
IAM-s-8's pre-flight blast radius consumes your reader alongside IAM-s-1's usage instrument.

## BOUNDS -- what this cell may not cross

```
⛔ C-DESIRED-UNTIL-EXERCISED (G-15 + acceptance property 3). THE CONDITION AXIS IS READ FROM POLICY
TEXT, so EVERY CLAIM THIS CELL MAKES IS `DESIRED` UNTIL A SIMULATE BATTERY EXERCISES IT. Label them
so, in the field a consumer can reject on. A document read is not an applied state and is never an
exercised one. `aws iam simulate-principal-policy` is the instrument that would move it, and
running that battery is NOT this cell -- it is named at IAM-s-8.

⛔ AND THE BOUND THAT MATTERS MOST, because it is the one an enthusiastic reader will cross without
noticing. PRD section 8 row S4 and brief Part VII item 5:

    THAT THE ESTATE IS BROADLY SILENT ON THIS AXIS IS AN INFERENCE FROM ONE POLICY.
    IT IS NEVER A MEASURED POPULATION CLAIM.

You may surface as many policies as you like. You MAY NOT write "the estate does not use condition
keys", "no policy requires MFA", "all policies are silent on this axis" or any sentence of that
shape, UNLESS you have measured the whole population and can print its denominator -- and this cell
is not commissioned to do that. Report what you read, with its denominator, and stop there. The
exhibit FWD-3 asks for is ONE real policy, not a census.

DO NOT MODIFY ANY POLICY. This cell READS. Narrowing is IAM-s-8's question and applying is nobody's
in this round.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED; PRD section 4).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam (L5 battery, RUN): 195 TF roles / 188 services / 1084 operations / 304 gaps.
⛔ COMP-IAM'S OWN RULE-22a LIMIT (c) IS THIS CELL'S SUBJECT MATTER, AND YOU SHOULD READ IT BEFORE
BUILDING: "Condition-block false-deny -> FIXED/CARRIED: --context-entries when given; A CONDITIONED
STATEMENT WITH NO CONTEXT IS UNKNOWN, NEVER A (FALSE) DENY." The estate's existing instrument
already knows that a Condition block it cannot evaluate must render UNKNOWN. Your reader inherits
that discipline: a Condition block you cannot PARSE is UNKNOWN, never REQUIRES-NOTHING. THE TWO ARE
OPPOSITE CLAIMS AND CONFLATING THEM WOULD MANUFACTURE THE FINDING THIS CELL EXISTS TO FIND.

comp-iam BLINDNESS STATED: `wafv2:UNMODELED` and `UNMAPPED-METHOD` on two services -- it does not
model every action namespace. comp-iam's silence about a service is never evidence about that
service's condition keys.

comp-schedule (L5 battery, RUN to completion at --budget 500): GATES ARMED: 26, none this
project's. G-15 (in the standing-moratoria band G-15..G-26) is carried into BOUNDS above.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-4.condition-axis-reader-what-a-policy-requires.md
infra/aws/terraform/estate-report/iam.tf
infra/aws/terraform/mdpf-pipeline/iam.tf
infra/aws/terraform/inf-pipeline/iam.tf
infra/aws/terraform/cot-pipeline/iam.tf
infra/aws/terraform/news-pipeline/iam.tf
infra/aws/terraform/etfs-reports/iam.tf
infra/aws/terraform/bd-pipeline/iam.tf
infra/aws/terraform/fred-pipeline/iam.tf
</paths>

The eight `iam.tf` files are READ surfaces -- real policy text for the reader to run against and for
the FWD-3 exhibit. You may READ them and you MUST NOT MODIFY them; this cell narrows nothing.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-4"><invocation>python org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/condition-axis-reader.py --policy infra/aws/terraform/estate-report/iam.tf</invocation><expect>per-statement output naming what each statement REQUIRES of the caller, printing the literal token REQUIRES-NOTHING for any statement with no Condition block, and printing a denominator of statements examined</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-4"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/CONDITION_AXIS.md && grep -c 'REQUIRES-NOTHING' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/CONDITION_AXIS.md</invocation><expect>a count of 1 or greater -- FWD-3's DONE WHEN met: at least one REAL policy statement surfaced as scoped yet requiring nothing of its caller; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-4"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/CONDITION_AXIS.md && grep -c -E 'DESIRED' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/CONDITION_AXIS.md</invocation><expect>a count of 1 or greater -- every claim read from policy TEXT is labelled DESIRED, per C-DESIRED-UNTIL-EXERCISED; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-4"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/CONDITION_AXIS.md && grep -c -i -E 'the estate is (broadly )?silent|no policy requires|all policies|every policy in the estate' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/CONDITION_AXIS.md</invocation><expect>a count of 0, printed -- brief Part VII item 5 honoured mechanically: no population claim was made from an inference over sampled policies; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-4" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the reader runs against REAL policy text and renders the second axis per statement
- **AC2** (mechanical): FWD-3's DONE WHEN, exercised -- the exhibit exists and the absence is VISIBLE as a token rather than as silence
- **AC3** (mechanical): C-DESIRED-UNTIL-EXERCISED honoured -- a document read never masquerades as an applied state
- **AC4** (mechanical): the population bound honoured NEGATIVELY -- the one sentence shape this cell is forbidden to write is absent
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): FWD-3's ACCEPT in plain English -- is a rule that is careful about WHAT someone can touch but asks NOTHING about who they are or how they proved it visible AS SUCH to a reviewer? Whether being tightly scoped has genuinely stopped being able to hide asking for no second factor is NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded, and scope the reader to ONE policy file per run rather than sweeping the estate.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** B, position 1 of 2 (IAM-s-4 -> IAM-s-8). A ROOT: cuttable and spawnable at issuance.
**Provenance:** the cell text mirrors PRD section 8 row S4 and the endpoint's FWD-3 verbatim. The fourth-root finding is decomposition section 4, which read the manifest's own `depends_on` column against PRD section 7's prose and recorded that the edges say four where the prose said two.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project; G-15 and G-21 bind this cell.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD on two services. Its RULE-22a limit (c), the condition-block false-deny, is this cell's own subject matter and is inlined in BATTERY FINDINGS.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable; DECLARED BLINDNESS on the L1 brief, so F8 and Part VII item 5 reach this order as the PRD's rendering, one instrument and not two.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell reads policy text and writes an assessment; it touches no route, cache key, data prop or gold script. comp-blast is NOT owed: this cell deletes and narrows nothing.
