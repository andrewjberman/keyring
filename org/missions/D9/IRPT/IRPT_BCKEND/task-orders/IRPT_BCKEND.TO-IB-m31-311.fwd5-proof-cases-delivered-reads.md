# TO IRPT_BCKEND.TO-IB-m31-311 -- FWD-5's four PROOF cases on the served publication, graded from the delivered reads

<to_id>IRPT_BCKEND.TO-IB-m31-311</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~153</issued_to>
<issued_by>2.0.0_SA_COO~M2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop (seat on dell2) | **Workstream:** ~M | **Decomp cell:** `IB-mr-311`
(`decompositions/IRPT_BCKEND_DECOMP_R31_M.md`, AMENDMENT 1) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-311` (E-M2 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_30_M_20261007.md`).
FWD-5's PROOF clause names four cases: an unassigned account, an unmatched join, a blended model and a
multi-relationship membership. The cell checks three things on the served 2026-10-05 Holdings publication:
- **e1:** for each case, one real instance is found at any of the three firms and named, or its absence at all three
  is stated with the denominator searched.
- **e2:** each found instance reconciles before and after the overlay. Its residual is VISIBLE and not redistributed
  into sleeves.
- **e3:** coverage and join-exception counts are printed per firm, with their denominators.

**The reads already ran.** Each is pinned by commit and content sha256. The checks read them with `git show`, which
needs no AWS access.
- **CASES file:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R31M_FWD5_PROOF_CASES_READ.json` @`471da6f0b0`,
  sha256 `2b61c5a833c761e60b581f4f983f4c2795bc84624494df3a063d45571865f3e5`.
  - Laptop `3.0.0_SA_CVO` ran `r31m_fwd5_proof_cases_read.py` @229b82df18 to produce it.
  - This box was refused on Cottonwood (row S363).
- **RECHECK file:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31M_UNASSIGNED_RECHECK_20261007.json`
  @`6458a5a9d3`, sha256 `9eb9cff78f7721a07653606eb9624ad33ed46b86688ac04641e6c09bde64498e`.
  - The issuer ran it on dell2 on 2026-10-05 data, under AMENDMENT 1 (row S366).
  - It re-checks the UNASSIGNED case over every instance. The rule: the account is served as an ACCOUNT, its subtree
    ties, and no MODEL_LEAF, MODEL_WRAPPER or SLEEVE node sits under it.
  - Why a re-check: the CASES file tested one zero-value account against a rule that cannot hold in the L0 category
    shape.

**Your work:**
1. Run the three criteria below, and only those.
2. Write your report to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~153/R31_M_FWD5_PROOF_CASES_GRADE.md`.
   Copy every printed line verbatim, including both FILE lines with their hashes.
3. Write the proof of spec, then flip this order.

Do not call AWS. Do not re-run any reader.

### ACCEPTANCE

<criterion id="IBM31-311-AC1" cell_refs="IB-mr-311"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31_CHECKS/r31_delivered_reads.py e1</invocation><expect>E1-CASES-NAMED</expect></criterion>
`IBM31-311-AC1` -- each of the four cases is named with its instance, or stated absent with its denominator.

<criterion id="IBM31-311-AC2" cell_refs="IB-mr-311"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31_CHECKS/r31_delivered_reads.py e2</invocation><expect>E2-CASES-RECONCILE</expect></criterion>
`IBM31-311-AC2` -- every found case reconciles. The unassigned case passes over every instance (1,876 expected) on the
same publication date as the cases read.

<criterion id="IBM31-311-AC3" cell_refs="IB-mr-311"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31_CHECKS/r31_delivered_reads.py e3</invocation><expect>E3-COVERAGE-DENOMINATED</expect></criterion>
`IBM31-311-AC3` -- coverage and assigned-without-custody counts are printed with their denominators at 3 of 3 firms.

<expected_criteria>IBM31-311-AC1,IBM31-311-AC2,IBM31-311-AC3</expected_criteria>

Dry-run at the base 2026-10-07 ~11:5xZ (dell2 CLOUD @6458a5a9d3):
- AC1, AC2 and AC3 PASS. That is expected for this cell: it grades reads that already ran.
- Difference control: AC2 with a wrong pinned RECHECK hash prints `NOT-E2-CASES-RECONCILE`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Read-only cell.** Write nothing to AWS, and change no producer, reader, check or pin.
- **Refusal clause.** If a criterion prints `NOT-...`, stop and write the printed lines in your report. Then file a
  surprise row (id `IRPT_BCKEND-W153-S<k>`) and do not flip the order to complete.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R31_CHECKS/r31_delivered_reads.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You may write only the investigation file and your deliverables folder. Every other path named here is read-only.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R31_M.md</decomp_doc> (round 31, workstream ~M, AMENDMENT 1), cell `IB-mr-311`.
<owned_cells>IB-mr-311</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM31-311-AC1, IBM31-311-AC2, IBM31-311-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~153/IRPT_BCKEND.TO-IB-m31-311.fwd5-proof-cases-delivered-reads.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM31-311-AC1,IBM31-311-AC2,IBM31-311-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three criteria's printed lines, both FILE lines with their hashes, the commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read of delivered files; no schedule, deploy or write.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker. The reads ran on the laptop (CASES: arn:aws:iam::313476888478:user/Andrew_Berman) and on dell2 (RECHECK: cloudops-dell2-agent-user, 49F and INF only).
comp-adversary: RUN -- the CASES file's e2 FAIL rested on one zero-value instance under a rule the L0 category shape makes impossible (row S366); the RECHECK covers every instance; a wrong-hash negative control prints NOT-.
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msg 353 (round-30 M analysis, E-M2), msg 191 (grade from delivered FILES, naming path and
hash), msg 217 and msg 361 (fenced reads; probe from dell2 first); delivery 0.0.0_AB_MSTR~DELL2 msg 435 (laptop 106178).
Slot: 1 + max over authors, issued_to and branches = 1 + 152.
