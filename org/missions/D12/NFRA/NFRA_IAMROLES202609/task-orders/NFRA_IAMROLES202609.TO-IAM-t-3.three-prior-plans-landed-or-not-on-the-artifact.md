# NFRA_IAMROLES202609.TO-IAM-t-3 -- THE THREE PRIOR REMEDIATION PLANS: landed or not, ON THE ARTIFACT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R3.md</decomp_doc>
<owned_cells>IAM-t-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~9</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-6; the round-2 analysis calls this R3-C)

```
IAM-t-3. ACT: establish, for each of three prior least-privilege remediation plans, whether the work
LANDED -- on the artifact, never on the plan document's own say-so.

FWD-6's bar, verbatim: "each of the known past plans has been established as done or not done, on
evidence". Its DONE WHEN state is EXERCISED. It has waited two rounds and depends on nothing.

THE THREE PLANS, named by the brief's finding F10 and verified present at HEAD by the issuer:

  1. infra/security/remediation/active/iam-least-privilege-rollback-plan.md          (13331 bytes)
     "Replace 40 overly-permissive IAM policies with least-privilege custom policies."
     Last touched 2026-02-17, in a DIRECTORY REORGANISATION. Still in active/, never moved to
     completed/, no completion record.

  2. infra/security/remediation/active/SOC2-FULL-REMEDIATION-MASTER-PLAN.md          (13127 bytes)
     Same directory, same unknown status.

  3. org/projects/task_orders/PORTAL_AUTHHARD.WS6.least-priv-role-split-secret-dewildcard.md  (5809 bytes)
     Least-privilege role splitting and secret de-wildcarding.
     Carries NO <status> tag at all, and sits inside a project whose PRD marks it "not re-opened".

⛔⛔ THE WHOLE POINT OF THIS CELL IS THAT A DOCUMENT'S LOCATION IS NOT ITS STATUS. There IS an
infra/security/remediation/completed/ directory. A plan sitting in active/ is NOT evidence the work
did not land, and a plan in completed/ would not be evidence that it did. The brief says it in terms:
"a document's location is being asked to carry a completion claim it cannot carry", and "a stale
document is NOT evidence the work did not land. Establishing which is a first-order task for this
project and an assumption for nobody."

⛔ C-CLOSED-RECORD: A CLOSED RECORD IS A SNAPSHOT, NOT AN ORACLE. A plan that says "done", a ledger
entry marked complete, a status tag, a commit message claiming completion -- none of these is
evidence the world changed. THE ARTIFACT IS.

WHAT COUNTS AS EVIDENCE, and each verdict must carry it:
  - the DESIRED plane: does the Terraform / policy source now say what the plan said it would say?
    Cite file:line at a commit-ish. A citation without a vintage is not a citation.
  - the LIVE plane where you can reach it read-only: does AWS actually hold that state today?
  - a NEGATIVE CONTROL for each verdict: what would you have seen if the answer were the other way?
    A verdict whose evidence looks identical under both hypotheses is not a verdict.

WHAT TO PRODUCE, at
    .../deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md

  Per plan: LANDED / NOT-LANDED / PARTIALLY-LANDED / UNDETERMINABLE, the evidence with citations and
  vintages, the negative control, and -- where a plan enumerates items (plan 1 names FORTY policies) --
  the DENOMINATOR: how many of its items you checked and how many you could not.

⚠ UNDETERMINABLE IS A LEGITIMATE VERDICT AND IS BETTER THAN A GUESS, but it must name WHAT WOULD
SETTLE IT. "I could not tell" with the missing instrument named is a finding; "I could not tell" alone
is an unfinished cell.
```

## DEPENDENCIES

**NONE.** No cell of this round precedes it. The round-2 analysis calls it "the independent root that
should not idle" and the PRD says reading FWD-2-first as "nothing else may start" would idle two lanes
for a round.

## BOUNDS -- what this cell may not cross

```
⛔ THIS CELL ESTABLISHES STATUS. IT DOES NOT REMEDIATE. You do not finish an unfinished plan, you do
not narrow a permission, you do not move a document between active/ and completed/, and you do not
edit any of the three plans. Recording that work did not land is NOT a licence to do it.

⛔ C-TWO-REMEDIES: if a plan's unfinished work is a permissions narrowing, saying so is a STATUS
finding. Recommending or performing the narrowing is the other axis and is out of this cell.

⛔ C-NO-ACCESSDENIED: AWS is READ-ONLY here. get-role, get-policy, list-*, describe-*. Nothing that
changes anything.

⛔ DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED, 25 gates).
C-ANALYZER-PRICED-FIRST + G-25: no AWS Access Analyzer.

⚠ PLAN 3 SITS INSIDE ANOTHER PROJECT (NFRA_OPSEC202609) WHOSE PRD MARKS IT "not re-opened". You may
READ it and establish its status. You may NOT act on it, re-open it, or write into that project. If
establishing its status would require acting there, that is a FINDING and a surprise ROW.

⚠ BOUND EVERY READ. Each invocation runs under `timeout 120` and a timeout is recorded AS the output.
Plan 1 names forty policies -- do not attempt an unbounded estate sweep; state a cap and a denominator.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule (round-3 vintage, RUN to completion, 5 of 5 carriers, 13.5 s): GATES ARMED 25.
  ⭐ C2, THE DEPLOY-LEDGER CARRIER, READS 6 OPEN ENTRIES -- none of them this project's and NONE OF
  THEM YOURS TO CLOSE. They are named here because an OPEN ledger entry is exactly the kind of
  "closed record" trap this cell exists to see through, in the opposite direction: an entry a device
  left OPEN proves only that THAT DEVICE saw no completion. If one of your three plans has a ledger
  entry, read the ARTIFACT before believing either the open or the closed state.
  C5 PROJECT-BLOCKING is NOT-DECIDABLE with denominator 335 and carries a DRIFT CANDIDATE class whose
  own reason text contains satisfaction language while the sentinel is still armed -- the same shape
  as your subject.

comp-iam (round-3 vintage, RUN as `bash .tools/comp-iam stats` FROM A CLEAN WORKTREE at f20bc65d71):
  191 TF roles / 188 services / 1084 operations / 304 permission gaps.
  ⛔ THE INVOCATION FORM IS PART OF THE FIGURE -- the bare name reports 195 against the MAIN checkout,
  because five untracked .tf files there hold four aws_iam_role declarations that are in no commit.
  This bears directly on you: IF YOU MEASURE THE TERRAFORM PLANE FROM A DIRTY TREE YOU MAY SEE A
  POLICY THAT IS NOT IN ANY COMMIT and read it as landed. Measure the DESIRED plane from committed
  state and say which tree and which commit you read.

comp-find --corpus aws (vintage 2026-09-10 12:24:50 UTC): 219 IAM_ROLE nodes, DECLARED=203,
  LIVE-no-DECLARED=16. This is your LIVE-plane lens; its vintage is its own and is not "now".
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R3.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/ROUND_ANALYSIS.round2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-t-3.three-prior-plans-landed-or-not-on-the-artifact.md
infra/security/remediation/
infra/aws/terraform/
org/projects/task_orders/PORTAL_AUTHHARD.WS6.least-priv-role-split-secret-dewildcard.md
</paths>

Your deliverable goes in `deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/`, inside the granted prefix.
⛔ `infra/security/remediation/`, `infra/aws/terraform/` and the named plan-3 file are granted for
READING ONLY. This order authorises NO edit to any of them -- not a status tag, not a move between
active/ and completed/, not a correction. They are listed because the grant is read-or-write and you
cannot read a path that is not listed.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W9-S<k>`, `"fabric": "site-z"`. A BLOCKING row is read by the COO in your final report; an OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-t-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md && grep -c -E 'iam-least-privilege-rollback-plan|SOC2-FULL-REMEDIATION-MASTER-PLAN|PORTAL_AUTHHARD.WS6' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md</invocation><expect>a count of 3 or greater -- all three plans are addressed BY NAME and none was silently dropped; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-t-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md && grep -c -E 'LANDED|NOT-LANDED|PARTIALLY-LANDED|UNDETERMINABLE' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md</invocation><expect>a count of 3 or greater -- each plan carries an explicit verdict from the closed set, rather than prose a reader has to interpret</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-t-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md && grep -c -i -E 'negative control' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md</invocation><expect>a count of 3 or greater -- one negative control per verdict, because a verdict whose evidence would look identical under both hypotheses is not a verdict</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-t-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md && grep -c -i -E 'denominator' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~9/PRIOR_REMEDIATION_STATUS.md</invocation><expect>a count of 1 or greater -- where a plan enumerates items, the deliverable prints how many were checked against how many exist; plan 1 names forty policies and a verdict over an unstated subset of forty is not a verdict about the plan</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-t-3"><invocation>git status --porcelain -- infra/security/remediation/ org/projects/task_orders/PORTAL_AUTHHARD.WS6.least-priv-role-split-secret-dewildcard.md infra/aws/terraform/ | wc -l</invocation><expect>a count of 0 -- NEGATIVE: the three plans and the Terraform tree are untouched in the worktree. This cell establishes status and remediates nothing, moves nothing between active/ and completed/, and edits no plan. Note this reads the WORKING TREE, so it is checked BEFORE any commit as well as after</expect></criterion>
  <criterion id="AC6" cell_refs="IAM-t-3" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): all three plans addressed by name, none dropped.
- **AC2** (mechanical): each carries an explicit verdict from a closed set.
- **AC3** (mechanical): a negative control per verdict -- the discipline that separates a verdict from an impression.
- **AC4** (mechanical): the denominator is printed where a plan enumerates items.
- **AC5** (mechanical, NEGATIVE): nothing was remediated, moved or edited. Reads the working tree so a pre-commit run is meaningful.
- **AC6** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): can a reader now tell, for each of the three, whether the work landed -- **without having to trust the plan document, its directory, or its status tag**? And where the verdict is UNDETERMINABLE, does the deliverable name what would settle it, so the next round has something to cut rather than a shrug?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- bound every read.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>3</round>
<slot>~9</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 3) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2, amended at six sites @3cadaf52ca
**Authority chain:** round-2 slug @d076801ecf -> `ROUND_ANALYSIS.round2.md` @3cadaf52ca section 8 (R3-C) -> L5 round-3 decomp -> this issuance.
**Chain:** an independent chain of one. The analysis calls it the independent root that should not idle.
**Provenance:** the three plans are the brief's F10, quoted from the brief at HEAD, and all three paths were VERIFIED PRESENT at HEAD by the issuer before the cut with a negative control (a bogus sibling path returns rc=128). The existence of `infra/security/remediation/completed/` was also verified, because it is the trap the cell is built around.
<preflight>
comp-schedule: RUN to completion, 5 of 5 carriers, 13.5 s, WITHIN BUDGET. GATES ARMED 25, none this project's. C2 deploy-ledger 6 OPEN entries, none this project's and none this cell's to close; inlined in the worker face because an open ledger entry is the same closed-record trap seen from the other side.
comp-iam: RUN at round-3 vintage from a CLEAN worktree via the explicit .tools/ path -- 191 TF roles / 188 services / 1084 operations / 304 gaps; the bare-name form reports 195 against the main checkout and that hazard is inlined, because a DESIRED-plane read from a dirty tree could show this cell a policy that is in no commit.
comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16 at vintage 2026-09-10 12:24:50 UTC.
comp-adversary: RUN on the round-3 rectangle.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-3 vintage. comp-blast DECLARED-NOT-APPLICABLE -- this cell changes no Terraform custody and applies nothing. comp-iam-usage NOT-APPLICABLE here: it is the permissions axis and this cell is historical status, which C-TWO-REMEDIES keeps apart.
