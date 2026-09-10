# NFRA_IAMROLES202609.TO-IAM-t-1 -- CLOSE FWD-4: every member row carries an owner, a declaration, or a FINDING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R3.md</decomp_doc>
<owned_cells>IAM-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~7</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; the round-2 analysis calls this R3-A)

```
IAM-t-1. ACT: close FWD-4. Its bar is "each one is either in code or carries a named owner and a
reason". Today 4 of 16 meet it.

THE MEASUREMENT THAT DEFINES YOUR WORK, and it is not yours to re-derive:

    DECLARED (in code)                    1   meets the bar
    EXEMPT owner=1.0.0_SA_CTO~Z           3   meets the bar -- that seat ACCEPTED these three
    EXEMPT owner=UNASSIGNED               2   does not
    RETIRE owner=UNASSIGNED               1   does not  (lambda-test-role)
    ADOPT, WITH NO owner= FIELD AT ALL    9   does not  -- AND NOTHING IS WATCHING THESE
                                         --
                                         16

⛔ THE NINE ADOPT ROWS ARE THE POINT. They carry NO owner field whatsoever, so the metric everyone
has been quoting -- a census of owner=UNASSIGNED -- CANNOT SEE THEM. It counts 3 while 12 rows are
short of the bar. That is a COVERAGE defect in the instrument, not a defect in anyone's arithmetic:
the census spans the rows that HAVE the field while the claim is about all rows.

⭐ THIS IS NOT A REGRESSION AND YOU ARE NOT CLEANING UP A MISTAKE. Round 1's schema was binary and
forced those nine into a value that LOOKED settled. Round 2 split the token into DECLARED (a fact)
and ADOPT (a recommendation), and THAT is what made the gap legible. You are finishing a repair that
worked, not patching one that failed.

WHAT TO WRITE, in the governance disposition document:

  (a) EVERY member row gains an `owner=` field or a `DECLARED` disposition, and every row carrying an
      owner also carries a `reason=`. That is the existing convention -- three rows already follow it
      exactly. NO ROW MAY BE LEFT WITH NO OWNER FIELD AT ALL.

  (b) An ADOPT row's owner is whoever would actually do the adoption, or -- if nobody in this fabric
      would -- an owner value that RECORDS THAT FINDING, with the reason saying what you established
      and how.

  (c) lambda-test-role's RETIRE needs a retirement owner on the same terms.

⛔⛔ A CELL MAY NOT ASSIGN WORK TO A SEAT THAT HAS NOT ACCEPTED IT. Three rows name 1.0.0_SA_CTO~Z
because that seat accepted those three, in writing, at the round-1 terminal. YOU HAVE NO SUCH
ACCEPTANCE FOR ANYONE ELSE AND YOU CANNOT OBTAIN ONE -- you cannot send a message and nobody can
answer you. So writing `owner=<some-seat>` for a seat that has not accepted is FORGING A COMMITMENT
ON ANOTHER AGENT'S BEHALF. Do not do it, however reasonable the guess.

⭐ WHETHER THOSE OWNERS EXIST INSIDE THIS FABRIC AT ALL IS THIS CELL'S FINDING, NOT AN ASSUMPTION IT
MAY MAKE. "No owner exists for these nine, and here is the evidence" is a COMPLETE and CORRECT
outcome for this cell. It is not a failure and it is not a shortfall. The round-2 analysis says that
escalation is the recut's finding and is raised THEN, not pre-emptively -- so raise it in your
deliverable and in a surprise ROW, and stop there.

ONE CHEAP CORRECTION WHILE YOU ARE IN THE DOCUMENT: row 8 says Terraform touches the role through
"three" aws_iam_role_policy attachments. The tree-wide figure of record is FIVE (data-refresh/main.tf
carries 4, qa-scratch-instance.tf carries 1). Substance is unaffected at any count; fix the number.
```

## DEPENDENCIES

**NONE.** This cell depends on no other cell of this round. The membership question it would otherwise
have to ask was settled at round 2: the population is **15 genuinely undeclared of a 16-row set**, one
member (`seeking-alpha-scraper-role`) having been proved DECLARED-IN-TF at
`infra/aws/terraform/seeking-alpha/main.tf:240-241`. Do not re-open membership.

## BOUNDS -- what this cell may not cross

```
⛔ C-TWO-REMEDIES: GOVERNANCE AXIS ONLY. Governance asks "should this role be in code at all"; the
permissions axis asks "is it over-granted". They have two remedies that DO NOT MOVE TOGETHER. You may
not narrow a permission, recommend narrowing one, or read a permissions fact as a governance answer.
If you notice a permissions problem, that is a surprise ROW.

⛔ DO NOT ASSIGN AN OWNER WHO HAS NOT ACCEPTED (above). This is the cell's hardest bound.

⛔ DO NOT MODIFY ANY TERRAFORM. DO NOT CREATE, DELETE OR EDIT ANY ROLE. DO NOT APPLY ANYTHING.
infra/aws/terraform/ is a READ surface for establishing facts and nothing else.

⛔ DO NOT RESTRUCTURE THE DOCUMENT. Three cells across two rounds built it -- a split vocabulary, a
rule-24 record, a class-rulings section, a retirement value. EXTEND it; do not rewrite it.

⛔ DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED, 25 gates).
C-ANALYZER-PRICED-FIRST + G-25: no AWS Access Analyzer.

⚠ THE DOCUMENT CONTAINS NUMBERED LINES THAT ARE NOT MEMBER ROWS. A member row is a numbered line whose
subject is a BACKTICKED ROLE NAME. Five other numbered lines name tools and planes. A census anchored
only on `^[0-9]+\. ` counts 21, not 16 -- this issuer made exactly that error while writing your
criteria and caught it by measuring. Your criteria below carry the tight anchor; use it in your own
reads too.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam (round-3 vintage, RUN as `bash .tools/comp-iam stats` FROM A CLEAN WORKTREE at f20bc65d71):
  191 TF roles / 188 services / 1084 operations / 304 gaps.
  ⛔ THE INVOCATION FORM IS PART OF THE FIGURE. The bare name `comp-iam` resolves through a ~/bin
  forwarder to the MAIN checkout and reports 195, because five untracked .tf files there hold four
  aws_iam_role declarations that are in NO commit. If you run comp-iam, run `bash .tools/comp-iam`
  from your own worktree, and state which form you used beside any number you quote.

comp-find --corpus aws (round-3 vintage 2026-09-10 12:24:50 UTC): 219 IAM_ROLE nodes, DECLARED=203,
  LIVE-no-DECLARED=16 -- STILL EXACTLY 16 after round 2 proved one member of that class is a false
  positive. THE LIVE DRIFT CLASS DOES NOT LEARN FROM THE REPAIR, so it is not the membership oracle.

comp-schedule (round-3 vintage, RUN to completion, 5 of 5 carriers, 13.5 s): GATES ARMED 25, none of
  them this project's. G-21 binds this cell and is in BOUNDS.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R3.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/ROUND_ANALYSIS.round2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-t-1.close-fwd4-every-row-carries-an-owner-or-a-finding.md
infra/aws/terraform/
</paths>

The document you edit is `deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md`,
inside the granted `deliverables/` prefix. Your own deliverable goes in
`deliverables/0.9.0_WK_NFRA_IAMROLES202609~7/`. `infra/aws/terraform/` is granted for READING ONLY and
this order does not authorise any change to it.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W7-S<k>`, `"fabric": "site-z"`. An OBSERVATION never interrupts -- file it and keep working.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-t-1"><invocation>grep -E '^[0-9]+\. `[A-Za-z0-9._-]+`' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c -v -E 'DECLARED|owner='</invocation><expect>a count of 0 -- every one of the 16 member rows now carries either a DECLARED disposition or an owner= field, whatever that owner's value records; measured 9 at the cut, and those nine are the ADOPT rows the owner=UNASSIGNED census cannot see</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-t-1"><invocation>grep -E '^[0-9]+\. `[A-Za-z0-9._-]+`' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep 'owner=' | grep -c -v 'reason='</invocation><expect>a count of 0 -- every owner-bearing member row also carries a reason, which is the convention the three accepted rows already follow; measured 0 at the cut, so this is a REGRESSION BAR that must read 0 before and after and every row you add must satisfy it</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-t-1"><invocation>grep -E 'EXEMPT' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c -v -E 'owner=[^ ]+ +reason='</invocation><expect>a count of 0 -- the regression bar that has now run across four cells and two rounds: no exemption line ever loses its owner or its reason; measured 0 at the cut</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-t-1"><invocation>grep -c -i -E 'narrow|revoke|over-granted|remove permission' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 0, printed -- C-TWO-REMEDIES honoured: the governance half did not stray into the permissions half; measured 0 at the cut and this is a NEGATIVE regression bar</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-t-1"><invocation>grep -c -E 'through three' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 0 -- the stale attachment count is corrected from three to five; measured EXACTLY 1 at the cut, at line 116, so this bar cannot pass without the edit</expect></criterion>
  <criterion id="AC6" cell_refs="IAM-t-1" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, THE MOVER): no member row is left with no owner field at all. Measured 9 at the cut. **A cell that finds no owner exists can still satisfy this** by writing an owner value that records the finding with its reason -- but it CANNOT satisfy it by doing nothing.
- **AC2** (mechanical, REGRESSION): every owner-bearing row carries a reason. 0 before, 0 after.
- **AC3** (mechanical, REGRESSION): no exemption line loses its owner or reason. 0 before, 0 after.
- **AC4** (mechanical, NEGATIVE): the governance axis stayed clear of the permissions axis.
- **AC5** (mechanical, THE SECOND MOVER): the three-to-five correction. Measured exactly 1 at the cut.
- **AC6** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): does FWD-4 now read as CLOSED to a governance reader -- and where an owner could not be named, is the FINDING evidenced well enough that a reader learns something true about this estate rather than reading a placeholder dressed as a decision? An owner field filled with a non-answer would satisfy AC1 and defeat the outcome, and only a reader can tell those apart.

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>3</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 3) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2, amended at six sites @3cadaf52ca
**Authority chain:** round-2 slug @d076801ecf -> `ROUND_ANALYSIS.round2.md` @3cadaf52ca section 8 (R3-A) -> L5 round-3 decomp -> this issuance.
**Chain:** an independent chain of one. No cell of this round precedes or follows it.
**Provenance:** the 4-of-16 measurement is the CTO's, re-derived independently by this issuer against the document at HEAD before the cut (1 DECLARED + 3 owner=CTO = 4; 9 ADOPT with zero owner fields; 3 owner=UNASSIGNED; partition closes at 16). The nine-row blind spot was first written into the artifact by the round-2 worker itself, whose row 9 says an inventory entry is not a decision to except.
<preflight>
comp-iam: RUN at round-3 vintage from a CLEAN worktree via the explicit .tools/ path -- 191 TF roles / 188 services / 1084 operations / 304 gaps. The bare-name form reports 195 and measures the main checkout; both figures and the discriminator are recorded in the decomposition section 2.
comp-schedule: RUN to completion, 5 of 5 carriers, 13.5 s, WITHIN BUDGET. GATES ARMED 25, none this project's; C2 deploy-ledger 6 open, none this project's.
comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16 at vintage 2026-09-10 12:24:50 UTC, unchanged after round 2 proved a false positive in that class.
comp-adversary: RUN on the round-3 rectangle; its declaration is that this lane took the analysis's recut as GIVEN and re-derived only the comp-iam-usage premise recorded at decomposition section 2a.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-3 vintage. comp-blast DECLARED-NOT-APPLICABLE and discharged at round 2 -- this cell changes no Terraform custody. Non-core lenses DECLARED-NOT-APPLICABLE: this cell records decisions in a report and changes no infrastructure.
