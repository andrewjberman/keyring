# NFRA_IAMROLES202609.TO-IAM-s-7 -- HISTORICAL REMEDIATION completion evidence: did each past clean-up actually land, ON THE ARTIFACT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md</decomp_doc>
<owned_cells>IAM-s-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~4</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-6; acceptance property 1)

```
IAM-s-7 mirrors manifest row S7. ACT: establish, FOR EACH known past least-privilege remediation
plan, whether it ACTUALLY LANDED -- on the ARTIFACT, never on the plan document's own say-so.

THE OUTCOME THIS SERVES, VERBATIM FROM THE RATIFIED ENDPOINT:
  FWD-6  Anyone can tell whether a past clean-up actually happened
         DONE WHEN  EXERCISED -- each of the known past plans has been established as done or not
                    done, on evidence
         ACCEPT     For work someone planned months ago, a reader learns whether it was finished
                    -- and does not have to guess from which folder the document is filed in.

⛔⛔ READ THE ACCEPT LINE AGAIN, BECAUSE THE TRAP IT NAMES IS SITTING RIGHT THERE IN THE
FILESYSTEM AND IT WILL BE THE FIRST THING YOU SEE. The plans live under
`infra/security/remediation/`, WHICH HAS AN `active/` SUBFOLDER AND A `completed/` SUBFOLDER.
FOLDER LOCATION IS NOT EVIDENCE. A plan filed in `completed/` may not have landed; a plan filed in
`active/` may have landed months ago and never been moved. THE WHOLE POINT OF THIS CELL IS THAT A
READER SHOULD NOT HAVE TO GUESS FROM THE FOLDER -- so you may not guess from it either.

THE THREE PLANS, located and pinned at the cut so you do not have to hunt for them:
  1. infra/security/remediation/active/iam-least-privilege-rollback-plan.md
     last touched @6aad42da0d, 2026-02-17, by Andrew Berman
     ⭐ THIS IS THE ONE BRIEF F10 DESCRIBES AS "UNTOUCHED SINCE FEBRUARY". Nearly seven months.
  2. infra/security/remediation/secrets-allowlist-narrowing-and-least-privilege-PLAN-20260709.md
     last touched @11d00bc906, 2026-07-09, by 0.5.0_AE_OpalETL
  3. infra/security/remediation/secretsmanager-readwrite-least-privilege-20260709.md
     last touched @c0d864ddac, 2026-07-09, by 0.5.0_AE_OpalETL

TWO ARTIFACT-PLANE WITNESSES ALREADY EXIST FOR PLAN 3's FAMILY and are granted to you as read
surfaces. They are LEADS, NOT VERDICTS -- read them, then go to the artifact anyway:
  org/critical_paths/change_management/20260709T1031Z_20260709T1035Z_terraform-p2-B1-least-privilege-secretsmanager-readwrite_deploy_completion.md
  org/tier1_exec/3.0.0_SA_CVO/deliverables/CERT_terraform-p2-B1-least-privilege-write-root-lega_20260709.md

THE SHAPE IS CLOSED AT THE CUT: a deliverable at
    org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/HISTORICAL_COMPLETION.md
with one section per plan, each carrying the plan's path and a verdict token `LANDED`,
`NOT-LANDED` or `PARTIAL`, and each verdict CITING AN ARTIFACT AT A VINTAGE in the form
`<verdict> ... @<7-or-more hex commit>`. A verdict with no citation is an opinion.
```

## DEPENDENCIES

This cell depends on: none -- IAM-s-7 is a ROOT and is ready at issuance. It is the whole of chain D
and it shares no edge with any other cell, so nothing you do here waits on anyone and nothing waits
on you.

## BOUNDS -- what this cell may not cross

```
⛔ LANDED-OR-NOT ON THE ARTIFACT, NEVER ON THE PLAN DOCUMENT'S OWN SAY-SO. A plan that says
"Status: COMPLETE" is making a claim ABOUT THE DAY IT WAS WRITTEN. Go to the thing the plan said it
would change -- the Terraform, the live policy, the role -- and read THAT.

⛔ C-CLOSED-RECORD: A CLOSED RECORD IS A SNAPSHOT, NOT AN ORACLE. This applies to the
change-management entry and the CVO certification granted above as much as to the plans. A deploy
completion entry proves someone recorded a completion; it does not prove the current state. Use
them to know WHERE TO LOOK, then look.

⛔ AND THE INVERSE, WHICH IS THE ONE THAT WILL COST YOU IF YOU MISS IT: A PLAN THAT WAS NEVER
FINISHED IS NOT NECESSARILY A FINDING ABOUT SOMEONE'S DILIGENCE. It may have been superseded, or
the surface may have been retired, or the work may have landed by another route under another
name. `NOT-LANDED` is a claim about the ARTIFACT, not about the plan's author. Where you can tell
WHY, say so; where you cannot, say `NOT-LANDED, cause not established` rather than inventing one.

DO NOT EXECUTE ANY OF THE THREE PLANS. You are grading whether they landed. Finishing an unfinished
remediation is a world-changing act, it is not this cell, and it is not this round. If you conclude
a plan urgently needs finishing, that is a surprise ROW -- file it and keep working.

DO NOT MODIFY THE PLAN DOCUMENTS, and do not move any file between `active/` and `completed/`.
Re-filing a document would destroy the very evidence the next reader needs, and the folder was
never the carrier in the first place.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED; PRD section 4).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-adversary (L5 battery, RUN on the decomposition): 5 of 5 cited commits VERIFIED, 4 of 4 cited
paths stable. ⛔ DECLARED BLINDNESS THAT IS SPECIFICALLY YOURS: "It did not read the three
historical remediation plans IAM-s-7 will grade." NOBODY HAS READ THEM IN THIS PROJECT. Every
statement about them in this order is a location and a git vintage, not a summary of content. You
are the first reader and you should expect the contents to surprise the framing.

brief F10 (via the PRD, one instrument not two): THREE such plans exist WITH UNKNOWN STATUS, one of
them untouched since February. "Unknown status" is the measured starting point, not a hint that the
answer is bad.

comp-iam (L5 battery, RUN): 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on
wafv2 (UNMODELED) and UNMAPPED-METHOD on two services. If a plan's target sits in a service
comp-iam does not model, comp-iam's silence is NOT evidence the plan landed. Read the Terraform
directly for those.

comp-schedule (L5 battery, RUN to completion at --budget 500): GATES ARMED: 26, NONE this
project's. C2's deploy-ledger band includes entries belonging to other projects -- an open ledger
entry you meet while reading is NOT yours to close.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-7.historical-remediation-completion-on-the-artifact.md
infra/security/remediation/
org/critical_paths/change_management/
org/tier1_exec/3.0.0_SA_CVO/deliverables/CERT_terraform-p2-B1-least-privilege-write-root-lega_20260709.md
infra/aws/terraform/
</paths>

Everything outside the project tree in that list is a READ surface: the plans, the change-management
entries, the certification and the Terraform are what you GRADE AGAINST, and you MUST NOT MODIFY any
of them. `infra/aws/terraform/` is granted as a directory prefix because you cannot know in advance
which module a plan's target lives in.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-s-7"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/HISTORICAL_COMPLETION.md && grep -c -E 'iam-least-privilege-rollback-plan|secrets-allowlist-narrowing-and-least-privilege-PLAN-20260709|secretsmanager-readwrite-least-privilege-20260709' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/HISTORICAL_COMPLETION.md</invocation><expect>a count of 3 or greater -- all three known plans are graded, none silently dropped; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-s-7"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/HISTORICAL_COMPLETION.md && grep -c -E '(LANDED|NOT-LANDED|PARTIAL).*@[0-9a-f]{7}' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/HISTORICAL_COMPLETION.md</invocation><expect>a count of 3 or greater -- every verdict cites an ARTIFACT AT A VINTAGE; a verdict without a citation is an opinion and does not count; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-s-7"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/HISTORICAL_COMPLETION.md && grep -c -i -E 'because it is filed in|filed under completed|since it is in active/|the folder says' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~4/HISTORICAL_COMPLETION.md</invocation><expect>a count of 0, printed -- FWD-6's ACCEPT honoured mechanically: no verdict was inferred from which folder the document sits in; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-s-7"><invocation>git log -1 --format=%h -- infra/security/remediation/active/iam-least-privilege-rollback-plan.md</invocation><expect>the short hash 6aad42da0d truncated to its first 7 or more characters -- the February plan is still at the vintage this order pinned, confirming the cell graded the document the order named and that nothing moved it mid-round</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-s-7" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): all three plans graded, coverage over the known set rather than a sample
- **AC2** (mechanical): every verdict is grounded -- an artifact at a vintage, which is what "on evidence" means in FWD-6's DONE WHEN
- **AC3** (mechanical): the folder-location trap FWD-6's ACCEPT names, refused NEGATIVELY
- **AC4** (mechanical): a stability control on the order's own pins -- the graded document is the one the order named, at the vintage it named, so a verdict cannot be about a file that moved underneath it
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): FWD-6's ACCEPT in plain English -- for work someone planned months ago, does a reader LEARN whether it was finished, without having to guess from which folder the document is filed in? Whether each verdict is genuinely established on the artifact rather than reasoned from the plan's own claims is NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded, and read Terraform modules one at a time rather than sweeping `infra/aws/terraform/` whole.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @cbe45b0db4 -> L2/L3/L4 `1.0.0_SA_CTO~Z` (endpoint RATIFIED) -> L5 `2.0.0_SA_COO~ZI` decomp @9e72041da5 -> L6 this issuance.
**Chain:** D, the whole chain -- a singleton with no edges. A ROOT: cuttable and spawnable at issuance, and it blocks nothing.
**Provenance:** the cell text mirrors PRD section 8 row S7 and the endpoint's FWD-6 verbatim. The three plan paths and their git vintages were LOCATED AND MEASURED BY THE ISSUER AT THE CUT (comp-find over the repo, then `git log -1` per file) because the L5 lane declared in terms that it had NOT read them -- so this order pins locations and vintages and claims nothing about their contents.
<preflight>
comp-schedule: RUN to completion at --budget 500 (5 of 5 carriers). Denominators C1=23 C2=7 C3=12 C4=20 C5=335. GATES ARMED: 26, NONE owned by this project; G-21 binds this cell. C2's deploy-ledger band carries other projects' open entries, which this cell reads and never closes.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD on two services, so its silence is never evidence a plan landed.
comp-adversary: RUN on the decomposition -- 5 of 5 cited commits VERIFIED, 4 of 4 cited paths stable. DECLARED BLINDNESS NAMING THIS CELL EXPLICITLY: the L5 lane did not read the three historical remediation plans this cell grades.
</preflight>

**Preflight disposition:** mandatory core RUN at L5, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell reads archival documents and live Terraform and writes an assessment; it touches no route, cache key, data prop or gold script. comp-blast is NOT owed: this cell deletes nothing and narrows nothing.
