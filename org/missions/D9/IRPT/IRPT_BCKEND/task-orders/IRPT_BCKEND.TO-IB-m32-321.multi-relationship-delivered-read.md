# TO IRPT_BCKEND.TO-IB-m32-321 -- one true multi-relationship membership, graded from the delivered laptop read

<to_id>IRPT_BCKEND.TO-IB-m32-321</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~154</issued_to>
<issued_by>2.0.0_SA_COO~M2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop (seat on dell2) | **Workstream:** ~M | **Decomp cell:** `IB-mr-321`
(`decompositions/IRPT_BCKEND_DECOMP_R32_M.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-321` (E-M3 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_31_M_20261007.md`).
FWD-5's PROOF names "a multi-relationship membership". Round 31 read a proxy, "more than one MODEL", and the CTO ruled
that the proxy is not the case. The cell checks three things:
- **m1:** one account that belongs to more than one relationship (more than one Relationship ID in Cottonwood's custody
  rows) is named, from the producer's own collapse evidence.
- **m2:** that account's unique underlying holdings reconcile before and after the overlay:
  - equal relationship duplicates are collapsed, so there is no double count;
  - its rebuilt subtree ties;
  - its value equals the served 2026-10-05 value.
- **m3:** the overlap between "more than one model" and "more than one relationship" is printed as a 2x2 with its
  denominator.

**The read already ran.** The evidence lives only inside a producer build: `_manifest.actual_custody_controls` is never
served. Cottonwood is refused to this box (row S368), so laptop `3.0.0_SA_CVO` ran `r32m_multi_relationship_read.py`
@a533959eae, which calls the producer's `build_snapshot("cottonwood", s3, "2026-10-05")`.
- It ran under a guard that refused every non-read AWS call: 0 were refused.
- The file is `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R32M_MULTI_RELATIONSHIP_READ.json` at commit
  `09e0d7c89c`, sha256 `e2606081349ee91aef56ede3fac5c368f57cbcff057bae23922e92de1595f56a`.
- The checks read it with `git show`, which needs no AWS access.

**Your work:**
1. Run the three criteria below, and only those.
2. Write your report to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~154/R32_M_MULTI_RELATIONSHIP_GRADE.md`.
   Copy every printed line verbatim, including the FILE line with both hashes.
3. Write the proof of spec, then flip this order.

Do not call AWS. Do not re-run any reader. Do not run bun.

### ACCEPTANCE

<criterion id="IBM32-321-AC1" cell_refs="IB-mr-321"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R32_CHECKS/r32_delivered_read.py m1</invocation><expect>M1-MULTI-RELATIONSHIP-NAMED</expect></criterion>
`IBM32-321-AC1` -- one account in more than one relationship is named, with its relationship count and the instance total.

<criterion id="IBM32-321-AC2" cell_refs="IB-mr-321"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R32_CHECKS/r32_delivered_read.py m2</invocation><expect>M2-RECONCILES</expect></criterion>
`IBM32-321-AC2` -- that account's positions are collapsed with no double count, its subtree ties, and the rebuilt value
equals the served 2026-10-05 value. The build date and the served date match.

<criterion id="IBM32-321-AC3" cell_refs="IB-mr-321"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R32_CHECKS/r32_delivered_read.py m3</invocation><expect>M3-OVERLAP-MEASURED</expect></criterion>
`IBM32-321-AC3` -- the multi-model by multi-relationship 2x2 is printed, and its four cells sum to the account denominator.

<expected_criteria>IBM32-321-AC1,IBM32-321-AC2,IBM32-321-AC3</expected_criteria>

Dry-run at the base 2026-10-07 ~13:0xZ (dell2 CLOUD):
- AC1, AC2 and AC3 PASS. That is expected for this cell: it grades a read that already ran.
- Difference control: AC2 with a wrong pinned hash prints `NOT-M2-RECONCILES`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Read-only cell.** Write nothing to AWS, and change no producer, reader, check or pin.
- **Refusal clause.** If a criterion prints `NOT-...`, stop and write the printed lines in your report. Then file a
  surprise row (id `IRPT_BCKEND-W154-S<k>`) and do not flip the order to complete.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R32_CHECKS/r32_delivered_read.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You may write only the investigation file and your deliverables folder. Every other path named here is read-only.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R32_M.md</decomp_doc> (round 32, workstream ~M), cell `IB-mr-321`.
<owned_cells>IB-mr-321</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM32-321-AC1, IBM32-321-AC2, IBM32-321-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~154/IRPT_BCKEND.TO-IB-m32-321.multi-relationship-delivered-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM32-321-AC1,IBM32-321-AC2,IBM32-321-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three criteria's printed lines, the FILE line with its hashes, the commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read of a delivered file; no schedule, deploy or write.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the read ran on the laptop under a non-read-refusing guard (dynamodb GetItem 2,026 / Scan 3, s3 GetObject 16 / ListObjectsV2 6, sts 1; 0 refused).
comp-adversary: RUN -- the round-31 proxy (more than one model) finds 181 accounts while the case holds 3 (overlap 1), which is why the CTO refused it; m2 was tied on 1 of the 3 multi-relationship accounts (the criterion asks for one); a wrong-hash control prints NOT-.
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msg 454 (round-31 M analysis, E-M3), msg 191 (grade from the delivered FILE by path and hash);
delivery laptop 3.0.0_SA_CVO @09e0d7c89c. Slot: 1 + max over authors, issued_to and branches = 1 + 153. bun: none
(rule 106215 / 106221).
