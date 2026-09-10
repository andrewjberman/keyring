# NFRA_IAMROLES202609.TO-IAM-r-2 -- WHAT DO 191, 208 AND 216 EACH COUNT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md</decomp_doc>
<owned_cells>IAM-r-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~6</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-1; acceptance property 1)

```
IAM-r-2. ACT: establish, per figure, WHICH INSTRUMENT produced it, at WHAT VINTAGE, and over WHAT
POPULATION -- for the three irreconcilable role counts this project carries.

THE FOUR ASSERTION SITES, measured in the PRD at v0.2:
    :70        "the coverage is zero of 208"
    :101       "16 of 208 are governable"
    :297-298   "16 of 208, corroborated across two substrates and re-measured at the merged head
                (216 hit(s) / 216 aws node(s))"      <-- 208 AND 216 IN ONE SENTENCE, AS CORROBORATION
    a fresh comp-iam parse                            191

THE OUTCOME THIS SERVES, VERBATIM:
  FWD-1  Someone can state our least-privilege posture with a number, what it is out of, and when
         it was taken
         DONE WHEN  EXERCISED -- a reviewer has actually answered the question with that evidence
                    attached, rather than an opinion

⛔ DO NOT PICK A WINNER BY PREFERENCE, AND DO NOT INVENT A RECONCILED FIGURE. Which of 191 / 208 /
216 is "right" is NOT established. THEY MAY BE THREE DIFFERENT POPULATIONS -- all roles, governable
roles, graph nodes -- or one misclassification, and nobody has reconciled them. Writing a confident
figure today would repeat the exact defect being repaired: a number asserted past what its
instrument measured.

WHAT THE DELIVERABLE MUST DO INSTEAD: for each figure, name the INSTRUMENT that produced it, the
VINTAGE at which it was produced, the POPULATION it ranges over, and WHAT THAT INSTRUMENT CANNOT
SEE. Then state whether the three are reconcilable and, if they are, what the reconciliation is --
with its own evidence. If they are not reconcilable from the available instruments, SAY SO; that is
a finding, not a failure to finish.

THE SHAPE IS CLOSED AT THE CUT: a deliverable at
    org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md
with one section per figure, each carrying the four fields above on its own lines.
```

## DEPENDENCIES

This cell depends on: none -- `IAM-r-2` is a ROOT and is ready at issuance. It is first on the
measurement chain; `IAM-r-3` establishes membership on your findings.

## BOUNDS -- what this cell may not cross

```
⛔ EVERY NUMBER CARRIES ITS DENOMINATOR AND ITS VINTAGE (acceptance property 1). That binds your own
output as hard as it binds the figures you are auditing.

⛔ A VALUE MUST CARRY ITS CLAIM -- `measured` for what you ran, `inferred` for what you derived,
`held` for what you are repeating from a document you did not verify.

⛔ AND THE INSTRUMENT YOU ARE MOST LIKELY TO OVER-TRUST IS comp-iam's PARSE. It emits its own NOTEs
that the TF role labels `orchestrator` and `scheduler` are each reused across THREE modules and were
silently mis-linked before a fix, producing FALSE-MISSING inline policies. ITS 195 IS A MEASUREMENT
OF THE PARSER'S REACH AS MUCH AS OF THE ESTATE. Treat every figure that way: ask what the instrument
could not see, not only what it counted.

⛔ AND A NAME MATCH IS NOT A DECLARATION. Measured at this round's cut:
`opal-data-refresh-lambda-role` returns NINE hits in `infra/aws/terraform` and is NOT declared --
every hit is a reference, and the module carries ZERO `aws_iam_role` blocks. A count built by
matching names would include it. If any of the three figures was built that way, THAT IS THE
RECONCILIATION and you should say so.

DO NOT MODIFY ANY TERRAFORM AND DO NOT EDIT THE PRD. The PRD correction is the CTO's, already owed
and already recorded in the round-1 analysis. Your deliverable is what that correction will cite.
DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED).
C-ANALYZER-PRICED-FIRST + G-25: no AWS Access Analyzer.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam (round-2 battery, RUN): 195 TF roles / 188 services / 1084 ops / 304 gaps; wafv2:UNMODELED
and UNMAPPED-METHOD on two services, so 304 is a FLOOR on the DESIRED plane. Plus the two reuse
NOTEs above, which are this cell's subject matter.
⚠ NOTE THE ARITHMETIC TRAP: the analysis cites 191 from "the fresh comp-iam parse" and the round-2
battery run of the same tool reports 195. THOSE ARE FOUR APART AND BOTH ARE comp-iam. Establishing
whether that is a vintage difference, a scope difference or a parser change is squarely this cell.

comp-find --corpus aws (round-2 battery, RUN): 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16,
vintage 2026-09-10 12:21:58 UTC, manifest d70b0a16ae79. A FOURTH figure -- 219 -- on a plane none of
the three came from.

comp-schedule (round-2 battery, RUN to completion): GATES ARMED 25, none this project's; G-21 binds.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/ROUND_ANALYSIS.round1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-2.what-do-191-208-216-each-count.md
infra/aws/terraform/
docs/briefs/nfra-iamroles202609-least-privilege-brief-20260909.md
</paths>

`infra/aws/terraform/` and the brief are READ surfaces; you MUST NOT MODIFY either. The brief is
granted because two of the three figures originate there and this is the first cell in the project
authorised to read it directly rather than through the PRD's rendering.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W6-S<k>`, `"fabric": "site-z"`. An OBSERVATION never interrupts -- file it and keep working.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-r-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md && grep -c -E '\b(191|208|216)\b' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md</invocation><expect>a count of 3 or greater -- all three disputed figures are addressed by name, none silently dropped; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-r-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md && grep -c -i -E 'instrument|vintage|population|cannot see' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md</invocation><expect>a count of 12 or greater -- the four required fields carried for each of the three figures; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-r-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md && grep -c -i -E 'the true population is|the correct figure is|the right number is|reconciled to [0-9]+ roles' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md</invocation><expect>a count of 0, printed -- no reconciled figure was invented by preference; a reconciliation that IS established must be stated with its own evidence rather than in one of these bare assertion shapes; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-r-2"><invocation>.tools/comp-find '.' --corpus aws IAM_ROLE --limit 3</invocation><expect>a printed DENOMINATOR line and a VINTAGE line -- the live plane re-measured at this cell's own vintage, giving the fourth figure its own instrument and timestamp rather than inheriting one</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-r-2" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): all three disputed figures are addressed, none dropped
- **AC2** (mechanical): each figure carries instrument, vintage, population and blindness -- four fields x three figures
- **AC3** (mechanical, NEGATIVE): no winner picked by preference; the forbidden sentence shapes are absent
- **AC4** (mechanical): the live plane is re-measured here rather than quoted from the decomposition
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): after reading this, can a reviewer say what each figure counts and whether the three can be reconciled -- and is any claim of irreconcilability itself grounded rather than a shrug? An honest "these are three populations and here is the evidence" and an honest "these cannot be reconciled from these instruments, and here is why" are both passes; an unexamined shrug is not.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded, and scope any Terraform read to one module at a time.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6, round 2) - **Project:** NFRA_IAMROLES202609 - **Directive:** D12 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** round-1 slug @fd7a0b3e91 -> `ledger/ROUND_ANALYSIS.round1.md` @b647fd4f63 (section 6, R2-B, and section 4 which names the three assertion sites) -> L5 round-2 decomp @fde51f6e6a -> this issuance.
**Chain:** the measurement chain, position 1 of 3 (IAM-r-2 -> IAM-r-3 -> IAM-r-5). A ROOT.
**Provenance:** the four assertion sites are the round-1 analysis's own measurement of the PRD at v0.2, and the analysis records that the defect is the CTO's own artifact. The 191-vs-195 discrepancy between the analysis's citation and the round-2 battery is this issuer's observation, added to the face because it is a live arithmetic gap the cell will meet immediately.
<preflight>
comp-schedule: RUN to completion, 5 of 5 carriers, 14.5 s, rc=0. C1=23 C2=6 C3=12 C4=20 C5=335. GATES ARMED 25, none this project's.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; wafv2:UNMODELED; the two reuse NOTEs are this cell's subject matter and are inlined.
comp-find --corpus aws: RUN -- 219 nodes, DECLARED=203, LIVE-no-DECLARED=16, vintage 2026-09-10 12:21:58 UTC.
comp-adversary: RUN on the round-2 decomposition; its declaration records that this lane has never read the L1 brief, which is why this cell is granted the brief directly.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-2 vintage. Non-core lenses DECLARED-NOT-APPLICABLE -- this cell reads instruments and documents and writes an audit; it touches no route, cache key, data prop or gold script and deletes nothing.
