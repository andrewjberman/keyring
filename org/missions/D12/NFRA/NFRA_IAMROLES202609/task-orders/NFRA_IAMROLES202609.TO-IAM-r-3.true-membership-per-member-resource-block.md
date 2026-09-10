# NFRA_IAMROLES202609.TO-IAM-r-3 -- TRUE MEMBERSHIP, PER MEMBER, ON A PLANE THAT DID NOT BUILD THE SET

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md</decomp_doc>
<owned_cells>IAM-r-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~6</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; acceptance property 1)

```
IAM-r-3. ACT: establish the TRUE membership of the undeclared set -- per member, one at a time,
against a plane that did not build the set, each with its own citation.

WHY THIS CELL EXISTS, AND IT IS THE ROUND'S CENTRAL FINDING. The live graph's drift class carries at
least one CONFIRMED FALSE POSITIVE: seeking-alpha-scraper-role is classed LIVE-no-DECLARED and IS
declared. The count has held at exactly 16 across three vintages and two substrates -- and it held at
16 again at this round's cut, AFTER a member of that set was proven declared.

⛔ A STABLE COUNT ACROSS VINTAGES IS CONSISTENT WITH A STABLE MISCLASSIFICATION. Membership was
previously established by classing each member against the SAME INSTRUMENT'S OUTPUT AT TWO VINTAGES,
which can only show the classifier was CONSISTENT -- never that it was CORRECT. The "two
corroborating substrates" SHARED THE CLASSIFIER UNDER TEST. That is the entire finding and it is why
this cell exists.

⛔⛔ THE DISCRIMINATOR IS A RESOURCE BLOCK, NEVER A NAME MATCH. Measured at this round's cut:
    seeking-alpha-scraper-role      its hit sits INSIDE
                                    resource "aws_iam_role" "seeking_alpha_role" { name = "..." }
                                    -> DECLARED.                    <-- POSITIVE CONTROL
    opal-data-refresh-lambda-role   NINE hits in infra/aws/terraform and NOT ONE IS A DECLARATION.
                                    The module has ZERO aws_iam_role blocks and FOUR
                                    aws_iam_role_policy blocks attaching to it BY NAME STRING.
                                    -> NOT DECLARED.                <-- NEGATIVE CONTROL
    portal-auth-lambda-role         ZERO hits -> NOT DECLARED.
A CHECK THAT CANNOT SEPARATE THE FIRST TWO IS NOT A DISCRIMINATOR. A name-grep calls both declared.
The question is: does a `resource "aws_iam_role"` block exist whose `name` is this member.

THE SHAPE IS CLOSED AT THE CUT: a deliverable at
    .../deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md
with ONE LINE PER MEMBER carrying the member name, a verdict token DECLARED-IN-TF or NOT-IN-TF, and
a CITATION -- for DECLARED-IN-TF the file:line of the resource block, for NOT-IN-TF the scope
searched and the hit count found (zero hits and nonzero-but-all-references are BOTH NOT-IN-TF and
the line says which).
```

## DEPENDENCIES

This cell depends on: **IAM-r-2**, keyed to OBSERVED COMPLETION. That cell establishes what each
disputed figure counts; you establish who is actually in the set. You hold it yourself, first in this
queue, so you carry its findings forward.

Downstream (you do not build these): three disposition cells wait on YOUR verdicts, because disposing
a member before its membership is re-established risks disposing something that is not in the set.

## BOUNDS -- what this cell may not cross

```
⛔ SAME-INSTRUMENT AGREEMENT IS NOT EVIDENCE. Do not cite the live graph agreeing with itself at two
vintages. Every verdict rests on a read of Terraform SOURCE, which is a different plane from the one
that built the set.

⛔ CARRY BOTH CONTROLS AND SAY SO IN THE DELIVERABLE. The positive control is a member that IS
declared and must read DECLARED-IN-TF; the negative control is a member with many name hits and no
resource block and must read NOT-IN-TF. A probe that cannot demonstrate both is not shown to
discriminate, and a verdict set from an undemonstrated probe is worth nothing.

⛔ REPORT WHAT YOU FIND, INCLUDING IF IT IS BORING. If all sixteen minus the known false positive are
genuinely undeclared, that is the finding and it is a good one -- it converts "at most 15" into a
measured number. Do NOT hunt for extra false positives to make the cell feel productive.

⛔ RECONCILE, DO NOT DISPOSE. You establish who is in the set. You do not say what should happen to
any member -- not adopt, not exempt, not retire. That is C-TWO-REMEDIES and it is three other cells.

EVERY NUMBER CARRIES ITS DENOMINATOR AND ITS VINTAGE. A VALUE MUST CARRY ITS CLAIM.
DO NOT MODIFY ANY TERRAFORM. DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-find --corpus aws (round-2 battery, RUN): 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16,
vintage 2026-09-10 12:21:58 UTC, manifest d70b0a16ae79. ⭐ STILL EXACTLY 16 AFTER A MEMBER OF THAT SET
WAS PROVEN DECLARED -- the classifier has not moved and the false positive is still inside the count.
That is your strongest single piece of evidence that the count is not the thing to trust.

comp-iam (round-2 battery, RUN): 195 TF roles parsed. ⛔ NOT AN ORACLE FOR THIS QUESTION: it emits its
own NOTEs that `orchestrator` and `scheduler` were reused across three modules each and silently
mis-linked pre-fix. A parser that has demonstrably mis-linked roles cannot adjudicate declaration.
READ THE SOURCE, not the parse.

INSTRUMENT NOTE: `.tools/comp-find` invoked by its explicit path scans YOUR worktree; the bare name
resolves through a ~/bin forwarder. Use the explicit path and read the printed denominator.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-3.true-membership-per-member-resource-block.md
infra/aws/terraform/
</paths>

`infra/aws/terraform/` is a READ surface granted as a directory prefix because you cannot know in
advance which module declares a given member. You MUST NOT MODIFY anything under it.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W6-S<k>`, `"fabric": "site-z"`. An OBSERVATION never interrupts -- file it and keep working.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-r-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md && grep -c -E '(DECLARED-IN-TF|NOT-IN-TF)' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md</invocation><expect>a count of 16 or greater -- every member of the set carries a verdict token, none silently dropped; measured 0 at the cut, so no existing document satisfies this</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-r-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md && grep -c -E 'seeking-alpha-scraper-role.*DECLARED-IN-TF' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md</invocation><expect>a count of 1 or greater -- the POSITIVE control fires: the known false positive is caught by the probe and reads DECLARED-IN-TF; a probe that misses it is not shown to work</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-r-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md && grep -c -E 'opal-data-refresh-lambda-role.*NOT-IN-TF' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md</invocation><expect>a count of 1 or greater -- the NEGATIVE control fires: the member with nine name hits and no resource block reads NOT-IN-TF, so the probe separates a reference from a declaration</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-r-3"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md && grep -c -i -E 'agrees with the live graph|consistent across vintages|corroborated by the drift class' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/MEMBERSHIP_PER_MEMBER.md</invocation><expect>a count of 0, printed -- no verdict rests on the set's own classifier agreeing with itself, which is the failure this cell exists to correct; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-r-3" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): coverage over the set -- every member judged, not a sample
- **AC2** (mechanical): the POSITIVE control fires on the known false positive
- **AC3** (mechanical): the NEGATIVE control fires -- a reference-heavy undeclared role is not misread as declared
- **AC4** (mechanical, NEGATIVE): no verdict leans on same-instrument agreement
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): is each verdict genuinely established on the source plane, with a citation a reader can follow, such that the set's membership is now known rather than inherited? And where a member could not be settled, is the uncertainty stated rather than resolved by preference?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- read one module at a time rather than sweeping `infra/aws/terraform/` whole.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6, round 2) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** round-1 slug @fd7a0b3e91 -> `ledger/ROUND_ANALYSIS.round1.md` @b647fd4f63 (section 6, R2-B) -> L5 round-2 decomp @fde51f6e6a (sections 1a and 2c) -> this issuance.
**Chain:** the measurement chain, position 2 of 3 (IAM-r-2 -> IAM-r-3 -> IAM-r-5). Handed to slot ~6 when IAM-r-2 is terminal with a valid instance.
**Provenance:** the false positive is channel rows Z-W3-S2 and Z-S6, confirmed by this lane on a second instrument. The resource-block discriminator and both named controls are this round's own pre-cut measurement, recorded at decomposition section 1a and channel row Z-S8.
<preflight>
comp-schedule: RUN to completion, 5 of 5 carriers, 14.5 s, rc=0. GATES ARMED 25, none this project's; G-21 binds.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; its two reuse NOTEs are inlined as a reason NOT to treat its parse as the oracle for this cell's question.
comp-find --corpus aws: RUN -- 219 nodes, DECLARED=203, LIVE-no-DECLARED=16 at vintage 2026-09-10 12:21:58 UTC; still 16 after a member was proven declared.
comp-adversary: RUN on the round-2 decomposition; its declaration records that this lane never read the L1 brief and did not itself re-measure the other fourteen members.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-2 vintage. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell reads Terraform source and writes a verdict list; it deletes nothing and changes no infrastructure. comp-blast is owed at IAM-r-5, not here.
