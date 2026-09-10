# NFRA_IAMROLES202609.TO-IAM-s-8 -- The PRE-FLIGHT BLAST RADIUS: what a narrowing would break, known BEFORE the change

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~2</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-5; acceptance property 4)

```
IAM-s-8 mirrors manifest row S8. ACT: build the PRE-FLIGHT BLAST RADIUS -- what a narrowing would
break, known BEFORE the change -- and EXERCISE it against a REAL candidate narrowing.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-5  An engineer can narrow a permission and know beforehand what it would break
         DONE WHEN  EXERCISED -- a real narrowing has been checked in advance and the check was
                    believed
         ACCEPT     Before anyone takes a permission away, they can find out what would stop
                    working -- and be right. Nothing breaks because we tidied up.

⛔⛔ READ THIS PARAGRAPH BEFORE ANYTHING ELSE. THE ISSUER HAS ALREADY MADE THIS CALL SO THAT YOU
DO NOT HAVE TO, AND SO THAT YOU NEVER FACE A CHOICE BETWEEN CAUSING AN OUTAGE AND STOPPING.

  THE BAR IS ON THE CHECK, NOT ON AN APPLY. The ratified DONE WHEN reads "a real narrowing has
  been CHECKED in advance and the check was BELIEVED". EXERCISED here means THE PRE-FLIGHT WAS
  ACTUALLY RUN against a real candidate narrowing and its prediction was VALIDATED -- not that the
  narrowing was applied to production.

  THE VALIDATING INSTRUMENT IS `aws iam simulate-principal-policy`, WHICH IS READ-ONLY. It is the
  "simulate battery" the PRD's D3 names as never yet run. Running it is this cell. It changes
  nothing in the world.

  YOU DO NOT APPLY A NARROWING IN THIS CELL. No `terraform apply`, no `safe-apply`, no
  `aws iam put-role-policy`, no `delete-role-policy`. If you conclude that FWD-5 cannot be
  satisfied without a real apply, THAT IS A SURPRISE ROW AND A STOP ON THAT CRITERION -- file it
  with `spec_asserts` and `world_is` and keep working on your other criteria. It is NOT yours to
  decide unilaterally, and it is not something you can ask about: you have no send tool.

  WHY THE ISSUER READ IT THIS WAY, stated so the CVO can grade the reading rather than guess it:
  the L5 decomposition's section 2c says of this cell "a REAL narrowing WILL be applied -- a
  world-changing act". That sentence is the decomposition author's reading of EXERCISED. The
  outcome's own text is about the CHECK being run and believed, and `C-NO-ACCESSDENIED` says in
  terms that THE PROJECT MUST NOT CAUSE THE OUTAGE IT EXISTS TO PREVENT. Where a bound and a
  reading conflict, the bound wins. If the CVO grades this reading wrong, the remedy is a
  round-2 cell that applies under a change-management entry -- not a worker improvising one.

THE SHAPE IS CLOSED AT THE CUT so that this order's criteria and your build agree: an executable at
    org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/preflight-blast-radius.py
taking `--role <name> --remove <action>`, printing what would stop working if that action were
removed from that role, WITH A PRINTED DENOMINATOR of callers/resources examined.
```

## DEPENDENCIES

This cell depends on: **IAM-s-1** (the permission-grain usage instrument, chain A) and **IAM-s-4**
(the condition axis reader, your own queue), both keyed to OBSERVED COMPLETION -- deliverables that
exist and whose criteria passed -- never to a status word.

⛔ IAM-s-1 IS ON ANOTHER WORKER'S CHAIN. You will not be handed this task order until BOTH are
terminal with valid instances. If you are reading this and IAM-s-1's deliverable is not present,
that is a dispatch error: file a BLOCKING surprise row and stop.

## BOUNDS -- what this cell may not cross

```
⛔ C-NO-ACCESSDENIED (D5, docs/doctrine/CONTROLS_OVER_CARE.md:512) -- THE PROJECT MUST NOT CAUSE
THE OUTAGE IT EXISTS TO PREVENT. This is the reason FWD-5's bar is EXERCISED rather than APPLIED
and the reason the apply is out of this cell.

⛔ G-17 + G-23 (standing moratoria, ARMED). IF ANY WORLD-CHANGING ACT NEVERTHELESS BECOMES
NECESSARY AND YOU ARE ABOUT TO TAKE IT, NEVER-2 BINDS AND ITS ORDERING IS NOT NEGOTIABLE:
    open the change-management entry in org/critical_paths/change_management/ BEFORE the act,
    ACT,
    then CLOSE AND COMMIT the entry BEFORE taking the grading reads.
That ordering exists because a worker can die at any instruction boundary and the only residue it
cannot take with it is what is COMMITTED or TRUE IN THE WORLD. Commit the SENTINEL too
(org/critical_paths/.open_deploys/<slug>.json): a merely STAGED sentinel does not survive a forced
worktree teardown, and only a COMMITTED one outlives your worktree.
⚠ BUT RE-READ THE CELL: this order does NOT authorise the apply. These paths are granted so that
NEVER-2 is satisfiable if a deploy is ever opened here, not as permission to open one.

⛔ comp-blast IS OWED AT THIS CELL. The L5 battery declared comp-blast NOT-APPLICABLE for the
decomposition as a whole and said in terms that it "becomes applicable the moment IAM-s-8 exercises
a real narrowing". Run it against the candidate before you predict, and cite it.

C-DESIRED-UNTIL-EXERCISED: anything read from policy TEXT is DESIRED. The simulate battery is what
moves a claim to EXERCISED. Say which plane each claim is on, in the sentence.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED; PRD section 4).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
PRD section 8 DISCLAIMS THIS ROW'S BUILDABILITY AND THE DECOMPOSITION CARRIED THE DISCLAIMER
FORWARD RATHER THAN HIDING IT: "S8 depends on a simulate battery nobody has run (D3)". You are the
first to run it. Expect the instrument to surprise you, and file rows rather than smoothing.

brief F11 (via the PRD, one instrument not two): THE APPLIED-PLANE INSTRUMENT FOR THIS ALREADY
EXISTS. Do not re-buy it. `comp-iam`'s `simulate` mode is named in PRD section 2 under RELIES ON,
DOES NOT OWN -- it belongs to the comp-tool build lane, so USE it and do not modify it.

comp-iam RULE-22a limits, ALL THREE of which bite a blast-radius predictor specifically:
  (a) (action,resource) blindness -- comp-iam models (action) only; a grant on ANY arn falsely
      reads GRANTED for EVERY arn. The existing tool FIXED this by simulating the EXACT
      --resource-arns. YOUR PREDICTOR MUST DO THE SAME OR IT WILL UNDER-PREDICT BREAKAGE.
  (b) 2+-ARN implicitDeny poisoning -- ONE --resource-arns per reach-check call; the positive
      control is a SEPARATE invocation, because BATCHING CORRUPTS THE CONTROL.
  (c) condition-block false-deny -- a conditioned statement with no context is UNKNOWN, never a
      deny. An UNKNOWN you record as "would not break" is a false clean.
⛔ ALL THREE FAIL IN THE SAME DIRECTION FOR THIS CELL: they make a narrowing look SAFER than it is.
That is the exact failure C-NO-ACCESSDENIED forbids.

comp-iam BLINDNESS STATED: `wafv2:UNMODELED` and `UNMAPPED-METHOD` on two services; its 304-gap
figure is a FLOOR on the DESIRED plane. A service comp-iam does not model is a service your
prediction is BLIND on -- say so rather than reporting no breakage.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-8.pre-flight-blast-radius-exercised.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/estate-report/iam.tf
infra/aws/terraform/mdpf-pipeline/iam.tf
infra/aws/terraform/inf-pipeline/iam.tf
</paths>

`change_management/`, `.open_deploys/` and `ledger/` are granted so that NEVER-2 is SATISFIABLE if a
deploy is ever opened at this cell -- they are NOT permission to open one, and this order does not
authorise an apply. The three `iam.tf` files are READ surfaces for choosing a candidate narrowing;
you MUST NOT MODIFY them.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-8"><invocation>python org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/preflight-blast-radius.py --role opal-data-refresh-lambda-role --remove s3:PutObject</invocation><expect>output naming what would stop working if that action were removed from that role, printing a DENOMINATOR of callers or resources examined, and naming any service on which the prediction is BLIND rather than reporting no breakage there</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-8"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/BLAST_RADIUS.md && grep -c 'simulate-principal-policy' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/BLAST_RADIUS.md</invocation><expect>a count of 1 or greater -- the simulate battery D3 records as never run has actually been run and is cited, which is what moves the prediction from DESIRED to EXERCISED; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-8"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/BLAST_RADIUS.md && grep -c -i -E 'terraform apply|safe-apply|put-role-policy|delete-role-policy|APPLIED-TO-PRODUCTION' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/BLAST_RADIUS.md</invocation><expect>a count of 0, printed -- C-NO-ACCESSDENIED honoured mechanically: this cell exercised the CHECK and applied nothing to the world; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-8"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/BLAST_RADIUS.md && grep -c -i -E 'comp-blast' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/BLAST_RADIUS.md</invocation><expect>a count of 1 or greater -- the comp-blast lens the L5 battery declared OWED AT THIS CELL was actually run and cited; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-8" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the predictor runs against a REAL role and a REAL action, with a denominator, and declares its blind services rather than reporting silence as safety
- **AC2** (mechanical): the simulate battery D3 records as never run is actually run -- this is what EXERCISED means here
- **AC3** (mechanical): C-NO-ACCESSDENIED honoured NEGATIVELY -- nothing was applied to the world by this cell
- **AC4** (mechanical): the comp-blast lens the L5 battery deferred to this exact cell was run
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): FWD-5's ACCEPT in plain English, and it is the hard half -- was the check BELIEVED? Before anyone takes a permission away, can they find out what would stop working AND BE RIGHT? A predictor that always answers "nothing breaks" passes every mechanical criterion above. Whether this one would actually have been trusted before a real change, and whether the reading of EXERCISED taken in the cell text is the right one, is NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded, and simulate ONE resource ARN per call (limit (b): batching corrupts the control).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** B, position 2 of 2 (IAM-s-4 -> IAM-s-8). CROSS-CHAIN JOIN: also depends on IAM-s-1 on chain A. Handed to slot ~2 only when BOTH IAM-s-4 and IAM-s-1 are terminal with valid instances.
**ISSUER'S RECORDED SPECIFICATION CALL, flagged for the CVO at L9:** decomposition section 2c reads FWD-5's EXERCISED bar as requiring a REAL narrowing to be APPLIED. This order reads the bar as being on the CHECK -- the ratified DONE WHEN says "checked in advance and the check was believed" -- and resolves the conflict in favour of `C-NO-ACCESSDENIED`, which forbids the project causing the outage it exists to prevent. The apply is therefore OUT of this cell and a worker concluding otherwise files a row rather than choosing. This is a COO specification decision closed at the cut, recorded here rather than left for a worker to improvise, and it is the substance AC5 asks the CVO to grade. If the CVO grades it wrong, the remedy is a round-2 cell that applies under a change-management entry.
**Provenance:** the cell text mirrors PRD section 8 row S8 and the endpoint's FWD-5 verbatim. PRD section 8 itself disclaims this row's buildability (D3: no simulate battery has been run) and the decomposition cut it with that named rather than hidden.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project. G-17, G-21 and G-23 bind this cell; C2's deploy-ledger band (G-8..G-14) includes NFRA_OPSEC202609's G-13/G-14, which this project does NOT inherit notwithstanding the `related` edge.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD on two services. Its three RULE-22a limits all fail in the direction of making a narrowing look SAFER than it is, and are inlined in BATTERY FINDINGS for exactly that reason.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable; DECLARED BLINDNESS on the L1 brief, so F11 reaches this order as the PRD's rendering.
comp-blast: DECLARED-NOT-APPLICABLE at L5 for the decomposition as a whole, and EXPLICITLY DEFERRED TO THIS CELL -- "it becomes applicable the moment IAM-s-8 exercises a real narrowing". It is OWED here and AC4 grades it.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. comp-blast is the one non-core lens that IS owed at this cell and is carried into BOUNDS and AC4. The remaining non-core lenses (comp-routes, comp-cache, comp-transform, comp-pipescript) are DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, data prop or gold script.
