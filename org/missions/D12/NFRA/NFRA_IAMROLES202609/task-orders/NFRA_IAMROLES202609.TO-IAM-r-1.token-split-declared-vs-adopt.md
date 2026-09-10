# NFRA_IAMROLES202609.TO-IAM-r-1 -- THE TOKEN SPLIT: one token carrying two intents, split into two

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md</decomp_doc>
<owned_cells>IAM-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~5</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; acceptance property 1)

```
IAM-r-1. ACT: split the governance disposition's primary token into its two intents and correct the
coverage line it feeds.

WHY THIS CELL EXISTS. Round 1's governance disposition document defines its primary token in terms --
"the disposition is IN-CODE AS A FACT, NOT A RECOMMENDATION" -- and then applies IN-CODE to EIGHT
MEMBERS THE SAME DOCUMENT MEASURED AS ABSENT. So IN-CODE means "is declared" for one member and
"ought to be declared" for eight others. Its coverage line reads "10 IN-CODE, 6 exempt", which a
governance reader takes as ten of sixteen roles now declared. ROUGHLY TWO ARE.

That is one axis carrying two intents -- rule 24(iii) exactly -- and the token meant to CARRY the
finding is the one that ERASES it. The judgment criterion on that cell was graded FAIL at L9 for
this and only this.

THE VOCABULARY IS CLOSED AT THE CUT so this order's criteria and your edit agree. Replace the single
token with two, and keep the third as it is:
    DECLARED   a FACT: an `aws_iam_role` resource block exists for this member
    ADOPT      a RECOMMENDATION: it is not declared and should be brought into code
    EXEMPT     unchanged: deliberately outside our Terraform, with owner and reason
Then correct the coverage line so it reports the three counts separately and never implies that a
recommendation is an accomplished fact.

⛔ TOUCH NO RESEARCH AND DO NOT RE-OPEN THE SIX EXEMPT LINES. They are individually reasoned,
non-templated, and each names the decision owed AND why no owner could be named, with the cell
correctly refusing to invent one. THE RESEARCH IS SOUND; ONLY THE VOCABULARY REPORTING IT IS NOT.
A cell that re-derives the research will produce a second, differently-wrong document and lose the
part that was right. The remedy is ONE EDIT PER AFFECTED ROW plus the coverage line.

⛔ AND THE VOCABULARY YOU AUTHOR IS A SCHEMA, so rule 24 binds it: it arrives with its FOUR-POSTULATE
RECORD in the same document, or it is not a proposal. State the declared domain, hunt the uncovered
member rather than asserting coverage, keep one grain (a property of ONE MEMBER), keep one intent per
axis, and name which values one remedy does NOT move.
```

## DEPENDENCIES

This cell depends on: none -- `IAM-r-1` is a ROOT and is ready at issuance.

⛔ **YOU ARE FIRST ON A CHAIN OF THREE THAT ALL EDIT THIS ONE DOCUMENT.** `IAM-r-4` records a class
ruling onto your split, and `IAM-r-6` adds a further value onto that. They are chained behind you
precisely so no two workers edit this file at once. **Leave the document in a state the next cell can
extend** -- if your rule-24 record is present and honest, the next two only add rows to it.

## BOUNDS -- what this cell may not cross

```
DO NOT RE-OPEN ANY MEASUREMENT. You are not re-deciding which roles are declared. You are renaming
what the document already concluded, so that the name matches the conclusion.

⚠ WITH ONE EXCEPTION YOU MUST HANDLE RATHER THAN INHERIT: the round-2 cut measured that a NAME MATCH
IN TERRAFORM IS NOT A DECLARATION. `opal-data-refresh-lambda-role` returns nine Terraform hits and is
NOT declared -- every hit is a reference, and the module carries ZERO `aws_iam_role` blocks and FOUR
`aws_iam_role_policy` blocks attaching to it by name. So DECLARED means an `aws_iam_role` RESOURCE
BLOCK exists, never that the name appears. If round 1's document classed a member on a name match,
that member's row is one you may correct -- and say so explicitly in the row.
⛔ BUT DO NOT LAUNCH A FULL RE-MEASUREMENT: establishing true membership for all sixteen is IAM-r-3's
cell and is not yours. Where you cannot tell from what round 1 recorded, mark the row UNVERIFIED and
say what IAM-r-3 must settle. An honest UNVERIFIED beats a confident guess in either direction.

A VALUE MUST CARRY ITS CLAIM. DECLARED is `measured` and cites the resource block. ADOPT is a
recommendation and is labelled as one.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED).
DO NOT MODIFY ANY TERRAFORM. This cell edits a report.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule (round-2 battery, RUN to completion, 5 of 5 carriers, 14.5s): GATES ARMED 25, NONE
this project's. G-21 binds this cell and is in BOUNDS.

comp-iam (round-2 battery, RUN): 195 TF roles / 188 services / 1084 ops / 304 gaps. ⛔ ITS OWN NOTEs
MATTER HERE: the TF role labels `orchestrator` and `scheduler` are each reused across three modules
and were silently mis-linked before a fix, producing FALSE-MISSING inline policies. A parser that
has demonstrably mis-linked roles is not an oracle for whether a role is declared -- which is
another reason this cell renames rather than re-measures.

THE ROUND-2 CUT'S OWN RE-GROUNDING, inlined because it changes what DECLARED means:
  portal-auth-lambda-role         0 hits in infra/aws/terraform  -- absent outright
  opal-data-refresh-lambda-role   9 hits, NONE of them a declaration
  a role everyone agrees is declared: its hit sits INSIDE `resource "aws_iam_role" ... { name = ... }`
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/ROUND_ANALYSIS.round1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-1.token-split-declared-vs-adopt.md
</paths>

⛔ **THE DOCUMENT YOU EDIT IS `deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md`,
INSIDE THE GRANTED `deliverables/` PREFIX.** You are editing another worker's round-1 artifact ON
PURPOSE: there must remain ONE governance disposition document, not two competing ones. Git preserves
what round 1 said; the analysis and the channel record why it changed.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W5-S<k>`, `"fabric": "site-z"`. An OBSERVATION never interrupts -- file it and keep working.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-r-1"><invocation>grep -c 'IN-CODE' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 0 -- the token that carried two intents is gone from the document; measured 15 at the cut, so this criterion is NOT satisfiable by the current document</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-r-1"><invocation>grep -c -E '\b(DECLARED|ADOPT|EXEMPT)\b' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 16 or greater -- every member of the set carries one of the three replacement values; measured 13 at the cut</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-r-1"><invocation>grep -E 'EXEMPT' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c -v -E 'owner=[^ ]+ +reason='</invocation><expect>a count of 0 -- the six exemption lines still each carry a named owner and a reason, so the part that was right survived the edit; measured 0 at the cut and it must STAY 0</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-r-1"><invocation>grep -c -E 'MECE|SAME GRAIN|INTENT COHERENCE|STATE COHERENCE' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 4 or greater -- the rule 24 four-postulate record for the changed vocabulary is present, one line per postulate; measured 0 at the cut</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-r-1" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the ambiguous token is gone -- measured 15 today, so only a real edit moves it
- **AC2** (mechanical): every member carries one of the three replacement values -- measured 13 today
- **AC3** (mechanical): the six exemption lines survived intact -- this one is a REGRESSION BAR and reads 0 both before and after; a nonzero count means the edit damaged the part that was right
- **AC4** (mechanical): rule 24's record accompanies the changed vocabulary -- measured 0 today
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): does a governance reader now read the TRUE state off the coverage line -- how many roles are actually declared, how many are recommended for adoption, how many are exempt -- with no token implying that a recommendation is an accomplished fact? That is what the round-1 grade failed on, and whether the replacement fixes it is not self-gradeable by the builder.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6, round 2) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** round-1 slug `REMEDIATION_v1.Z.md` @fd7a0b3e91 -> `1.0.0_SA_CTO~Z`'s L10 answer `ledger/ROUND_ANALYSIS.round1.md` @b647fd4f63 (section 6, R2-A) -> L5 round-2 decomp @fde51f6e6a -> this issuance.
**Chain:** the document chain, position 1 of 3 (IAM-r-1 -> IAM-r-4 -> IAM-r-6). A ROOT.
**Provenance:** the cell text mirrors the round-2 decomposition's rectangle row for this cell; the failed-grade account is the round-1 analysis section 2 verbatim in substance; the DECLARED-is-a-resource-block bound is the round-2 cut's own measurement recorded at decomposition section 1a and channel row Z-S8.
<preflight>
comp-schedule: RUN to completion at --budget 500, scanned 5 of 5 carriers, 14.5 s, rc=0. C1=23 C2=6 C3=12 C4=20 C5=335. GATES ARMED 25 (moved 26 -> 25 since round 1, C2 7 -> 6, one deploy-ledger entry closed). NONE owned by this project; G-21 binds this cell.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD; two NOTEs on reused `orchestrator`/`scheduler` labels silently mis-linked pre-fix, inlined because they bear on what DECLARED can mean.
comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16, vintage 2026-09-10 12:21:58 UTC. Still exactly 16 after a member of that set was proven declared.
comp-adversary: RUN on the round-2 decomposition; declaration at its section 6, including that this lane has still never read the L1 brief.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-2 vintage, none declared not-applicable. Non-core lenses DECLARED-NOT-APPLICABLE for this cell -- it edits a report and touches no route, cache key, data prop, gold script or deletable resource. comp-blast is NOT owed here; it is owed at IAM-r-5.
