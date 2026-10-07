# TO IRPT_BCKEND.TO-IB-m30-301 -- the FWD-5 replay on the served publication, graded from the delivered laptop read

<to_id>IRPT_BCKEND.TO-IB-m30-301</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~132</issued_to>
<issued_by>2.0.0_SA_COO~M2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop (seat on dell2) | **Workstream:** ~M | **Decomp cell:** `IB-mr-301`
(`decompositions/IRPT_BCKEND_DECOMP_R30_M.md`, AMENDMENT 1) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-301` (E-M1 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md`).
FWD-5 in the PRD: "dated holdings and model snapshots have been replayed for all three registry client firms", with
"UNIQUE UNDERLYING HOLDINGS RECONCILE BEFORE AND AFTER THE OVERLAY" and denominators. The cell reads each firm's newest
served Holdings publication and checks three things:
- **c1:** the Inflection split account `acc_015d15b45d7a8ac71f951a67` (****3282) ties: every parent and basis partition
  in its subtree sums to its parent within 0.01 USD (TARGET excluded).
- **c2:** every Cottonwood account holding SPYI or PSLV ties the same way, with the count printed.
- **c3:** at 49 Financial, Inflection and Cottonwood, three arms each pass:
  - the whole node set's partitions balance;
  - the ACCOUNT nodes sum to the served `custody_totals.total_market_value`;
  - the served `attribution_holdouts.reconcile` reads reconciled.

**The read already ran.** This box's AWS identity is refused on the firm buckets (row IRPT_BCKEND-S352), so laptop
`3.0.0_SA_CVO` ran the reader `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r30m_fwd5_replay_read.py` @d6a3e7b04b
and delivered its result as a file:
- the file is `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R30M_FWD5_REPLAY_READ_2.json` at commit `8b83fd1d6f`;
- its content sha256 is `afa19a65eb338c6adc72be8684e81c51f9f4c2347fea7d5584e78b3cbe884c52`;
- the publications are dated 2026-10-05.

The file is not in your working tree, so the checks read it with `git show 8b83fd1d6f:<path>`, which needs no AWS
access.

**Your work:**
1. Run the three criteria below, and only those.
2. Write your report to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~132/R30_M_FWD5_REPLAY_GRADE.md`.
   Copy each criterion's printed lines verbatim: the file line with both hashes, and the per-firm arms and denominators.
3. Write the proof of spec, then flip this order.

Do not call AWS. Do not re-run the reader.

### ACCEPTANCE

<criterion id="IBM30-301-AC1" cell_refs="IB-mr-301"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R30_CHECKS/r30_delivered_read.py c1</invocation><expect>C1-TIES</expect></criterion>
`IBM30-301-AC1` -- the Inflection split account ties on the served 2026-10-05 publication.

<criterion id="IBM30-301-AC2" cell_refs="IB-mr-301"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R30_CHECKS/r30_delivered_read.py c2</invocation><expect>C2-TIES</expect></criterion>
`IBM30-301-AC2` -- every Cottonwood account holding SPYI or PSLV ties (29 expected; the printed count is the denominator).

<criterion id="IBM30-301-AC3" cell_refs="IB-mr-301"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R30_CHECKS/r30_delivered_read.py c3</invocation><expect>C3-RECONCILES</expect></criterion>
`IBM30-301-AC3` -- before and after the overlay reconcile at 3 of 3 firms, every arm exercised. An ABSENT arm fails.

<expected_criteria>IBM30-301-AC1,IBM30-301-AC2,IBM30-301-AC3</expected_criteria>

Dry-run at the base 2026-10-07 ~10:1xZ (dell2 CLOUD @c61cca7a44):
- AC1, AC2 and AC3 all PASS. That is expected for this cell: it grades a read that already ran, and builds nothing.
- Difference control: the same check with a wrong pinned hash prints `NOT-C3-RECONCILES`.
- The checker also FAILs an ABSENT arm. The first laptop read @e9993e95fa would have failed AC3 for that reason (row S356).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Read-only cell.** Write nothing to AWS, and change no producer, script or check.
- **Refusal clause.** If a criterion prints `NOT-...`, stop and write the printed lines in your report. Then file a
  surprise row (id `IRPT_BCKEND-W132-S<k>`) and do not flip the order to complete. Never edit the check or the pin.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R30_CHECKS/r30_delivered_read.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You may write only the investigation file and your deliverables folder. Every other path named here is read-only.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R30_M.md</decomp_doc> (round 30, workstream ~M, AMENDMENT 1), cell `IB-mr-301`.
<owned_cells>IB-mr-301</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM30-301-AC1, IBM30-301-AC2, IBM30-301-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~132/IRPT_BCKEND.TO-IB-m30-301.fwd5-replay-delivered-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM30-301-AC1,IBM30-301-AC2,IBM30-301-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three criteria's printed lines, the file line with both hashes, the commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read of a delivered file; no schedule, deploy or write.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the AWS read ran on the laptop under its own identity (arn:aws:iam::313476888478:user/Andrew_Berman, recorded in the file).
comp-adversary: RUN -- the first laptop read @e9993e95fa read c2 over the wrong pair and passed c3 on two absent fields (row S356); the checks here FAIL an absent arm, and a wrong-hash negative control prints NOT-.
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msg 156 (analysis), msg 160 (one-issuer condition MET), msg 191 (route (a): grade from the
delivered FILE, naming its path and hash), msg 278 (round 61: ~M2 grades E-M1 on the second laptop FILE); laptop
decision 106087; delivery 106141 relayed as 0.0.0_AB_MSTR~DELL2 msg 303.
