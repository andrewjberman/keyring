# TO IRPT_BCKEND.TO-IB-m27-272 -- re-stage the irpt-holdings Lambda's contract copy (row W84-S4)

<to_id>IRPT_BCKEND.TO-IB-m27-272</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~84</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-272`
(`decompositions/IRPT_BCKEND_DECOMP_R27_M.md`) | **outcome_ref:** FWD-5 | **depends_on:** IB-mr-261

---

## WORKER FACE

### THE CELL

`IB-mr-272` -- row IRPT_BCKEND-W84-S4. The irpt-holdings Lambda resolves
`infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json` FIRST (`holdings/snapshot.py`
`_contract_candidates`, :72-89). That copy is a STAGED artifact of
`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`, pinned in `holdings/STAGE_MANIFEST.json` at
68a732b792, and it is three commits stale: it lacks the CATEGORY node kind, assigned_strategy and source_vendor_keys.
IB-mr-261 added `security_aggregates` and `class_totals` to all three copies, but the staged copy still differs from
docs.

The issuer measured that `validate_slice` has no caller in the handler path (only `tests/test_snapshot.py:315`), so
this is drift, not a serve-time refusal. It is still re-staged, so that the copy the Lambda resolves first equals
docs.

**Build (LOCAL -- no deploy, no Terraform):**
1. Re-stage the Lambda's contract copy from docs with the sanctioned stage tool: the `stage.py` that wrote
   `STAGE_MANIFEST.json`. Find it by the manifest's own header or by reading the holdings directory. Run it the way
   it is written to run, not by hand-copying, so that `STAGE_MANIFEST.json` carries the current pin and sha256.
2. Stage nothing beyond the contract unless the stage tool's own member list requires it. If it restages other
   members, report each one with its old and new sha256.
3. The Lambda's own suite stays whole. `test_snapshot.py:315` (`validate_slice` on a fixture) must still pass
   against the new copy.

### ACCEPTANCE

<criterion id="IBM27-272-AC1" cell_refs="IB-mr-272"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_CHECKS/r27_restage_check.py</invocation><expect>STAGED-CURRENT</expect></criterion>
`IBM27-272-AC1` -- the staged copy equals docs, carries the current pin, and admits every field the producer emits.

<criterion id="IBM27-272-AC2" cell_refs="IB-mr-272"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_CHECKS/r27_suite_whole.py infra/aws/lambda/investor-reporting/holdings/tests</invocation><expect>SUITE-WHOLE</expect></criterion>
`IBM27-272-AC2` -- the Lambda's suite passes whole on the re-staged copy (control: it passes before too).

<expected_criteria>IBM27-272-AC1,IBM27-272-AC2</expected_criteria>

Dry-run 2026-09-30 00:5xZ:
- AC1 at CLOUD @6c0317e55c and at wk-IRPT_BCKEND-84 @bb9e765c4d: NOT-STAGED (the copy differs from docs) -- FAIL as
  expected.
- AC2 at both: SUITE-WHOLE 147 passed -- PASS as expected (control).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** No deploy, no Terraform, no Lambda publish.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W84-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/investor-reporting/holdings/contracts/
infra/aws/lambda/investor-reporting/holdings/STAGE_MANIFEST.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R27_M.md</decomp_doc> (round 27, workstream ~M), cell `IB-mr-272`.
<owned_cells>IB-mr-272</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM27-272-AC1, IBM27-272-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~84/IRPT_BCKEND.TO-IB-m27-272.holdings-lambda-contract-restage.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM27-272-AC1,IBM27-272-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the stage tool and its invocation, the members restaged (old and new sha256), the check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; the Lambda redeploys only on its own later act.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant change.
comp-adversary: RUN -- 1 code read (snapshot.py validate_slice has no handler caller; tests/test_snapshot.py:315 only), 1 manifest read (STAGE_MANIFEST pins 68a732b792; three later contract commits unstaged); BLIND: whether stage.py restages members beyond the contract is unread at the cut (step 2 reports it).
lane: the <paths> block IS the grant.
</preflight>

Source: row IRPT_BCKEND-W84-S4 (0.9.0_WK_IRPT_BCKEND~84).
