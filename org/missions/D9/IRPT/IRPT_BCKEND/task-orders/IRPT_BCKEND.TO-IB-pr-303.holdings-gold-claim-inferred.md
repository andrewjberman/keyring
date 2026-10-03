# TO IRPT_BCKEND.TO-IB-pr-303 -- the adapter's gap claim reads "inferred", inside the claim vocabulary (CTO batch 207; nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-303</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~106</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 207 (CTO half @d9f15bc006, msg 104550). The round-36
packet's D2 is SIGNED and served. D1 (the adapter) is re-cut, because claim `"partial"` grows the measured/inferred/held/absent
vocabulary. GATE (x) puts this in ROUND 38 (row S267). | **Decomp cell:** `IB-pr-303` (decomposition section 30) | **outcome_ref:**
the Performance FWD (a value carries its claim) | **depends_on:** IB-pr-299 (merged @b1fccfb3f5)

---

## WORKER FACE

**The ruling.** CLAUDE.md, "A VALUE MUST CARRY ITS CLAIM": the claim vocabulary is `measured`, `inferred`, `held` and `absent`.
IB-pr-299 added a fifth, `"partial"`. Re-cut it to `"inferred"`:
- the figure linked across a missing day is inferred, not measured;
- KEEP the PARTIAL `missing_trading_days` ABSENCE that names the days (that is the absence class, not a claim);
- KEEP `value_facts["missing_trading_days"]`.

**What you build.**
1. In `infra/aws/lambda/investor-reporting/performance/holdings_gold.py`, replace `CLAIM_PARTIAL = "partial"` with
   `CLAIM_INFERRED = "inferred"`, and use it wherever the gap claim is set: `value_facts["claim"]` and the result's `"claim"`.
   No other behaviour changes. The module docstring and comments say `inferred`.
2. In `performance/tests/test_holdings_gold_calendar_gap.py`, the three assertions of `"partial"` as a claim become `"inferred"`.
   Nothing else in the file moves.

<criterion id="IB38-1-AC1" cell_refs="IB-pr-303"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r38/p38_claim_inferred.py" . IB38-1-AC1</invocation><expect>IB38-1-AC1 PASS</expect></criterion>
`IB38-1-AC1` -- the claim constants are inside the vocabulary, with `inferred` among them, and no `'partial'` literal remains in the
module. The gap tests name `inferred` and pass (at least 7). Base: FAIL (CLAIM_PARTIAL = "partial").

<criterion id="IB38-1-AC2" cell_refs="IB-pr-303"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r38/p38_claim_inferred.py" . IB38-1-AC2</invocation><expect>IB38-1-AC2 PASS</expect></criterion>
`IB38-1-AC2` -- the performance suite passes, at least 246, 0 failed. Base: PASS (a guard).

<expected_criteria>IB38-1-AC1,IB38-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none.
- **Refusal clause.** Any change beyond the claim value, its constant's name, comments and the three test assertions is out of
  bounds: stop and file a row. No client name in any record.

<paths>
infra/aws/lambda/investor-reporting/performance/holdings_gold.py
infra/aws/lambda/investor-reporting/performance/tests/test_holdings_gold_calendar_gap.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~106/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/performance/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 30 (round 38, workstream ~P), cell `IB-pr-303`.
<owned_cells>IB-pr-303</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB38-1-AC1, IB38-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~106/IRPT_BCKEND.TO-IB-pr-303.holdings-gold-claim-inferred.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB38-1-AC1,IB38-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the diff of the claim lines.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served irpt-performance-adapter's holdings_gold.py claim value; 0 served bytes move in the cell; D1 of ledger irpt-round36-gap-catchup-20261003 builds and applies it after its new blob is signed (before Mon 2026-10-05 14:00Z).
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB38-1-AC1 base FAIL (CLAIM_PARTIAL = "partial"), IB38-1-AC2 base PASS (246, a guard), dry-run at the base 2026-10-03 ~05:3xZ.
lane: the <paths> block IS the grant.
</preflight>
