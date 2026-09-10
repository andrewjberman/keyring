# NFRA_IAMROLES202609.TO-IAM-r-6 -- A THIRD DISPOSITION VALUE, THEN THE RESIDUE CALL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md</decomp_doc>
<owned_cells>IAM-r-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~5</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; acceptance property 1)

```
IAM-r-6. ACT: extend the disposition vocabulary so it can express RETIREMENT, then dispose
lambda-test-role.

WHY THE VALUE COMES FIRST. Round 1's schema was binary -- in-code or exempt -- and lambda-test-role's
honest outcome is neither: it reads as test/scratch residue whose answer is DELETE. The cell stalled
not because the research was hard but because THE SCHEMA HAD NOWHERE TO PUT THE ANSWER.

⛔ FORCING A RETIREMENT INTO THE EXEMPTION VALUE WOULD REPEAT IAM-r-1'S DEFECT ON A DIFFERENT AXIS.
EXEMPT means "deliberately kept outside our Terraform, and it stays". RETIRE means "this should not
exist at all". One axis, two intents, again. Add the value; do not overload an existing one.

⛔ AND THE UNCOVERED-MEMBER HUNT IS NOT OPTIONAL, BECAUSE THIS ROUND ALREADY FOUND A SECOND STATE
THE BINARY COULD NOT EXPRESS. Measured at this round's cut: opal-data-refresh-lambda-role is neither
declared nor cleanly undeclared -- Terraform carries ZERO aws_iam_role blocks for it and FOUR
aws_iam_role_policy blocks attaching to it BY NAME. So the estate MANAGES POLICIES ON A ROLE IT DOES
NOT OWN. Your rule-24 hunt must consider that state explicitly and either give it a value or record
why it does not need one. ⚠ Do not simply add it: a fourth value nobody needs is its own defect.
Decide, and show the reasoning.

RULE 24 BINDS THE CHANGE. It arrives with its FOUR-POSTULATE RECORD and a WORD-BOUNDARY TOKEN CENSUS
against the corpus IAM-r-1's split produced, or it is not a proposal.

THEN DISPOSE THE MEMBER: lambda-test-role gets the new value if the evidence supports retirement, or
another value if it does not. ⛔ RECORDING A RETIREMENT IS NOT PERFORMING ONE. You do not delete the
role, and nothing in this cell touches AWS.
```

## DEPENDENCIES

This cell depends on **IAM-r-4**, keyed to OBSERVED COMPLETION -- and through it on `IAM-r-1`'s split
and `IAM-r-3`'s membership verdicts. You are LAST on the document chain: the vocabulary was split,
the class ruling was recorded, and you extend what they left.

⛔ **CONFIRM FROM `IAM-r-3`'s VERDICT LIST THAT lambda-test-role IS ACTUALLY IN THE SET** before
disposing it. This round has already found one member misfiled; disposing a non-member would be the
same defect a second time.

## BOUNDS -- what this cell may not cross

```
⛔ THE VOCABULARY CHANGE COMES FIRST AND CARRIES ITS RECORD. Disposing first and naming the value
afterwards is how the round-1 defect happened.
⛔ RECORDING A RETIREMENT IS NOT PERFORMING ONE. No role is deleted, no AWS call changes anything, no
Terraform is modified. The deliverable is a document.
⛔ C-TWO-REMEDIES: governance only. Retirement is a governance disposition -- whether the role should
exist. It is not a permissions narrowing and you may not recommend one.
⛔ DO NOT RESTRUCTURE WHAT THE TWO EARLIER CELLS LEFT. Extend the record; do not rewrite it.
DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED).

⚠ AND IF THE EVIDENCE DOES NOT SUPPORT RETIREMENT, SAY SO AND DISPOSE IT OTHERWISE. "lambda-test-role
reads as residue" is a reading from a name and a shape, not a measurement. If it turns out to be in
use, the honest disposition is a different value and the finding is that the residue reading was
wrong. That is a good outcome, not a failed cell.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
THE ROUND-2 CUT'S OWN MEASUREMENT, which is your uncovered-member candidate:
  opal-data-refresh-lambda-role   9 Terraform hits, NONE a declaration; the module has 0
                                  aws_iam_role blocks and 4 aws_iam_role_policy blocks attaching
                                  to it by name, plus hardcoded role ARNs. Its own comment reads
                                  "inline policy attached to the PRE-EXISTING ... role".
  seeking-alpha-scraper-role      the contrast: its hit sits INSIDE a resource "aws_iam_role" block.

comp-iam (round-2 battery, RUN): 195 TF roles; its NOTEs on reused role labels silently mis-linked
pre-fix are a reason to read source rather than parses when deciding what a role's state is.

comp-schedule (round-2 battery, RUN to completion): GATES ARMED 25, none this project's. G-21 binds
this cell and is in BOUNDS.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/ROUND_ANALYSIS.round1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-6.a-third-disposition-value-then-the-residue-call.md
infra/aws/terraform/
</paths>

The document you edit is `deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md`,
inside the granted `deliverables/` prefix. `infra/aws/terraform/` is a READ surface for checking
whether the member is genuinely unused; you MUST NOT MODIFY it.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W5-S<k>`, `"fabric": "site-z"`. An OBSERVATION never interrupts -- file it and keep working.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-r-6"><invocation>grep -c -i -E 'RETIRE' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 1 or greater -- the vocabulary can now express retirement; measured 0 at the cut, so only a real extension moves it</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-r-6"><invocation>grep -c -i -E 'uncovered member|policy-attached|manages policies on a role' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 1 or greater -- the uncovered-member hunt addressed the policy-attached-but-undeclared state explicitly, either by covering it or by recording why it needs no value; measured 0 at the cut</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-r-6"><invocation>grep -c -E 'lambda-test-role' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 1 or greater -- the member that had nowhere to go now carries a disposition</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-r-6"><invocation>grep -E 'EXEMPT' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c -v -E 'owner=[^ ]+ +reason='</invocation><expect>a count of 0 -- the regression bar across all three document cells: no exemption line ever loses its owner or its reason, including after a third value is added beside it</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-r-6" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the retirement value exists -- measured 0 today
- **AC2** (mechanical): the uncovered-member hunt engaged the second state this round found, rather than adding one value and stopping
- **AC3** (mechanical): the stalled member now carries a disposition
- **AC4** (mechanical): the regression bar that has run across all three document cells still reads 0
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): does the extended vocabulary keep ONE INTENT PER AXIS -- is retirement genuinely a different question from exemption rather than a relabelling -- and is the decision on the uncovered state (cover it or not) reasoned rather than asserted? A fourth value nobody needs is as much a defect as a missing third one.

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6, round 2) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** round-1 slug @fd7a0b3e91 -> `ROUND_ANALYSIS.round1.md` @b647fd4f63 section 6 R2-C, which states the schema needs a third value BEFORE a cell can record that outcome -> L5 round-2 decomp @fde51f6e6a -> this issuance.
**Chain:** the document chain, position 3 of 3 and last (IAM-r-1 -> IAM-r-4 -> IAM-r-6).
**Provenance:** the stall is round-1 row Z-W3-S5. The second uncovered state -- policy-attached-but-undeclared -- is this round's own pre-cut measurement at decomposition section 1a and channel row Z-S8, and is handed to this cell as a CANDIDATE rather than as a required fourth value.
<preflight>
comp-schedule: RUN to completion, 5 of 5 carriers, 14.5 s, rc=0. GATES ARMED 25, none this project's; G-21 binds.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; reuse NOTEs inlined.
comp-find --corpus aws: RUN -- 219 nodes, LIVE-no-DECLARED=16 at vintage 2026-09-10 12:21:58 UTC.
comp-adversary: RUN on the round-2 decomposition; declaration at its section 6.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-2 vintage. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell authors a vocabulary and records a disposition; it deletes nothing and changes no infrastructure. comp-blast is NOT owed: recording a retirement is not performing one.
