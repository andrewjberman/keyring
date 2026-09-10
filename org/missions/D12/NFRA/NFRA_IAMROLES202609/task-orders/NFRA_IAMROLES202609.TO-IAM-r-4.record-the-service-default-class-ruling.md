# NFRA_IAMROLES202609.TO-IAM-r-4 -- RECORD THE CLASS RULING for the AWS service-default roles

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md</decomp_doc>
<owned_cells>IAM-r-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~5</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; acceptance property 1)

```
IAM-r-4. ACT: record the class ruling against the three AWS service-default roles --
ecsTaskExecutionRole, rds-monitoring-role, vpc-flow-logs-role.

THE RULING, GIVEN AND NOT YOURS TO RE-LITIGATE. 1.0.0_SA_CTO~Z ruled this as ARCHITECTURE:
    AWS-managed service roles stay OUTSIDE our Terraform, with the reason recorded.
    ONE CLASS RULING satisfies the outcome for the whole class.

⛔ DO NOT HUNT THREE OWNERS. Round 1 recorded these three as needing a named exemption owner and
stalled because no owner could be named. That reading was heavier than the outcome demands. The
outcome's words are "something deliberately kept outside the normal way of doing things SAYS WHO
DECIDED THAT AND WHY" -- which asks for A RECORDED DECISION WITH A DECIDER AND A REASON, and a
STANDING RULING satisfies it for a whole class. The decider is 1.0.0_SA_CTO~Z and the reason is
architectural. Record that against each of the three.

⛔ AND DO NOT RE-RULE IT. A cell that reopens whether AWS-managed service roles belong in Terraform
is doing L2 work in an L7 cell. If you believe the ruling is wrong, that is a surprise ROW, not an
edit.

WHAT TO WRITE: in the governance disposition document, each of the three members' rows carries the
EXEMPT value with `owner=1.0.0_SA_CTO~Z` and a reason naming the class -- AWS-managed service role,
minted by a console or service action, correctly outside our Terraform -- plus a pointer to the
ruling's record. The document also gains a short CLASS RULINGS section stating the rule once, so a
later reader sees that three rows share one decision rather than three coincidental ones.
```

## DEPENDENCIES

This cell depends on **IAM-r-1** (the token split -- you write into the vocabulary it establishes)
and **IAM-r-3** (true membership -- you dispose only confirmed members). Both keyed to OBSERVED
COMPLETION.

⛔ **YOU ARE SECOND ON THE DOCUMENT CHAIN.** `IAM-r-1` left this document with a split vocabulary and
a rule-24 record; `IAM-r-6` extends it after you. **Extend, do not restructure** -- and if `IAM-r-3`
found any of your three is not actually in the set, say so and dispose only those that are.

## BOUNDS -- what this cell may not cross

```
⛔ RECORD, DO NOT RE-RULE, AND DO NOT SEEK OWNERS. The ruling is given.
⛔ C-TWO-REMEDIES: this is the GOVERNANCE axis only. You may not narrow a permission, recommend
narrowing one, or read a permissions finding as a governance answer.
⛔ DO NOT TOUCH THE OTHER THIRTEEN MEMBERS' ROWS. Three members, three rows, plus the class section.
⛔ DO NOT MODIFY ANY TERRAFORM AND DO NOT CREATE, DELETE OR EDIT ANY ROLE.
DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED).

⚠ ONE THING TO CHECK RATHER THAN ASSUME, because this round has already found one member misfiled:
confirm from IAM-r-3's verdict list that each of your three is actually NOT-IN-TF. A member the
class ruling exempts while it is in fact declared would be a second instance of exactly the defect
this round is repairing.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-find --corpus aws (round-2 battery): the drift class that named these three still reads 16 and
is known to carry at least one false positive. That is why the bound above asks you to confirm
membership from IAM-r-3 rather than from the class that produced the list.

comp-iam (round-2 battery, RUN): 195 TF roles; its NOTEs on silently mis-linked reused role labels
are a reason not to treat any parse as the oracle for whether a role is declared.

comp-schedule (round-2 battery, RUN to completion): GATES ARMED 25, none this project's; G-21 binds.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/ROUND_ANALYSIS.round1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-4.record-the-service-default-class-ruling.md
</paths>

The document you edit is `deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md`,
inside the granted `deliverables/` prefix.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W5-S<k>`, `"fabric": "site-z"`. An OBSERVATION never interrupts -- file it and keep working.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-r-4"><invocation>grep -c -E '(ecsTaskExecutionRole|rds-monitoring-role|vpc-flow-logs-role).*owner=1\.0\.0_SA_CTO~Z' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 3 -- all three members carry the ruling's decider on their own row; measured 0 at the cut</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-r-4"><invocation>grep -c -i -E 'CLASS RULING' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 1 or greater -- the rule is stated ONCE as a class, so a reader sees three rows sharing one decision rather than three coincidental ones; measured 0 at the cut</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-r-4"><invocation>grep -E 'EXEMPT' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md | grep -c -v -E 'owner=[^ ]+ +reason='</invocation><expect>a count of 0 -- every exemption line, the three you wrote and the ones already there, carries a named owner and a reason; a regression bar that must read 0 before and after</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-r-4"><invocation>grep -c -i -E 'narrow|revoke|over-granted|remove permission' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md</invocation><expect>a count of 0, printed -- C-TWO-REMEDIES honoured: the governance half did not stray into the permissions half</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-r-4" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): all three members carry the ruling's decider -- the outcome asks who decided
- **AC2** (mechanical): the rule is recorded once as a class, which is the whole point of reading the owner requirement down
- **AC3** (mechanical): regression bar -- no exemption line, old or new, loses its owner or reason
- **AC4** (mechanical, NEGATIVE): the governance axis stayed clear of the permissions axis
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): does a governance reader now see a DECISION for these three -- who decided, on what reasoning, applying to what class -- rather than a gap dressed as an exemption? And is the class boundary drawn so a reader can tell which future roles it covers?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6, round 2) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** round-1 slug @fd7a0b3e91 -> `ROUND_ANALYSIS.round1.md` @b647fd4f63 section 4, which carries the class ruling and records that Andrew read the per-role-owner requirement DOWN at the CTO terminal -> L5 round-2 decomp @fde51f6e6a -> this issuance.
**Chain:** the document chain, position 2 of 3 (IAM-r-1 -> IAM-r-4 -> IAM-r-6). Cross-chain join: also depends on IAM-r-3 on the measurement chain.
**Provenance:** the ruling is quoted in substance from the round-1 analysis and is the CTO's, not this issuer's. Round 1's rows Z-W3-S3 recorded the stall this cell resolves.
<preflight>
comp-schedule: RUN to completion, 5 of 5 carriers, 14.5 s, rc=0. GATES ARMED 25, none this project's.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; wafv2:UNMODELED.
comp-find --corpus aws: RUN -- 219 nodes, LIVE-no-DECLARED=16 at vintage 2026-09-10 12:21:58 UTC, a class known to carry a false positive, which is why membership is confirmed from IAM-r-3.
comp-adversary: RUN on the round-2 decomposition; its declaration records that this lane took the class ruling as GIVEN and did not independently derive it.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-2 vintage. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell records a decision in a report and changes no infrastructure.
