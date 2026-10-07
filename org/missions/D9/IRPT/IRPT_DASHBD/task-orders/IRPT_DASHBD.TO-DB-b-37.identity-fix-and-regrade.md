# TO IRPT_DASHBD.TO-DB-b-37 -- E2: fix the cause DB-b-36 names and re-grade the activity identity over the same 91 accounts; one window with realized gain and a flow ties to the cent (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-37</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~21</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-23 analysis @9f285400cf item E2 ("The named cause
fixed and the identity re-graded (after E1): (1) the identity re-run over the same 91 windows prints passed / failed, with every remaining
failure listed by class; (2) one named window with a non-zero realized gain AND a non-zero contribution or withdrawal ties within one
cent, printed term by term (FWD-4's first real exercise)") | **Decomp cell:** `DB-b-37` (decomposition section 24) | **outcome_ref:**
FWD-4 | **depends_on:** `DB-b-36` (its diagnosis; same worker, same queue, handed on after DB-b-36 drains).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-21`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/`.

**The cell (`DB-b-37`).** Your slot's DB-b-36 diagnosed the round-23 identity gaps in `GAP_DIAGNOSIS_E1.json` (the largest gap's cause,
the transaction types that move value and map to no term, and the 39 gaps classed ROUNDING or MISSING-TERM). Now:
1. **Fix the named cause** in `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`: map each value-moving type to its term,
   and correct whatever else the diagnosis named. A gap is never plugged: a day that still fails stays `GAP_ABOVE_ALLOWANCE` with its gap
   carried. `account_return_daily.py` and every served producer are not edited.
2. **Tests** in `data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py`: one test per fix (the previously unmapped
   type now moves its term), on synthetic rows. Keep the existing 23 passing.
3. **Re-grade** the identity over the SAME 91 accounts and window as round 23 (2026-09-01..2026-10-05; the accounts in
   `deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json`). Write `IDENTITY_REGRADE_E2.json` with `regrade` `{graded,
   passed, failed, failures: [{account_id, gap, class}]}` (class ROUNDING within the 0.05 tolerance, or MISSING-TERM with its cause, or
   OTHER with a cause) and `exercise` `{account_id, window, beginning_value, contributions, withdrawals, realized, unrealized_change,
   income, ending_value}`: ONE window whose realized gain is non-zero AND whose contributions or withdrawals are non-zero, with the
   identity holding within one cent. Choose it from the 91 accounts or, if none qualifies, from the producer's population over the same
   window, and say which. Write `IDENTITY_REGRADE_E2.md`, COUNTS ONLY.

<criterion id="DB24-2-AC1" cell_refs="DB-b-37"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r24/p24_identity.py" . DB24-2-AC1</invocation><expect>DB24-2-AC1 PASS</expect></criterion>
`DB24-2-AC1` -- the re-grade over the same 91 accounts prints passed and failed, every failure listed with its class. Base: FAIL.

<criterion id="DB24-2-AC2" cell_refs="DB-b-37"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r24/p24_identity.py" . DB24-2-AC2</invocation><expect>DB24-2-AC2 PASS</expect></criterion>
`DB24-2-AC2` -- one window with a non-zero realized gain and a non-zero flow ties within one cent, every term printed. Base: FAIL.

<criterion id="DB24-2-AC3" cell_refs="DB-b-37"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r24/p24_identity.py" . DB24-2-AC3</invocation><expect>DB24-2-AC3 PASS</expect></criterion>
`DB24-2-AC3` -- the producer's tests pass (at least 23, naming identity). A bound: PASS at the cut, and it must stay so after the fix.

<expected_criteria>DB24-2-AC1,DB24-2-AC2,DB24-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only. No write, no vendor call, no bun, no download.
- **Refusal clause.** A plugged gap, an edit to a served producer, an S3 write, or a client figure in a committed `.md` is a defect:
  stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-37.identity-fix-and-regrade.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 24 (round 24, workstream B), cell `DB-b-37`.
<owned_cells>DB-b-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB24-2-AC1, DB24-2-AC2, DB24-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IRPT_DASHBD.TO-DB-b-37.identity-fix-and-regrade.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB24-2-AC1,DB24-2-AC2,DB24-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the fixes made, passed and failed with failures by class, the exercise window's
seven terms, and any row ids.


## AMENDMENT 1 (2026-10-07 ~16:0xZ, issuer 2.0.0_SA_COO~D2, on DB-b-36's diagnosis and rows W21-S1, W21-S2, W21-S3) -- staged -> issued

DB-b-36 named three causes (GAP_DIAGNOSIS_E1.json). The issuer rules each, inside this decomposition:

1. **Dropped conditional rows (W21-S1).** `classify_and_sum` in the SERVED producer resolves the CONDITIONAL-BY-COUNTERPARTY class with
   `_final is None`; under pandas 3 the None becomes NaN and the rows drop. MEASURED by the issuer: the served function's layer
   `irpt-performance-native-layer` v1 carries pandas 2.2.3 (numpy 1.26.4, pyarrow 14.0.2), so the SERVED gold is unaffected; this box runs
   pandas 3.0.6, so every LOCAL run here is. Do NOT edit `account_return_daily.py`. In `account_activity_lots.py`, make the call reproduce
   the served runtime's behaviour on any pandas: run it under `pd.option_context("future.infer_string", False)` where that option exists,
   and assert after the call that the CONDITIONAL rows resolved (a count of rows left unresolved, which must be 0 or each named). Print
   the local pandas version in the record.
2. **In-kind transfers.** An in-kind arrival (`TOA/IC`, `JNL/IC` LONG) is a CONTRIBUTION at its market value on the transfer date; an
   in-kind departure is a WITHDRAWAL at its market value. For the identity, a lot that arrived in kind measures its unrealized change and
   any realized gain FROM its transfer-date market value, not from the custodian's original cost basis. Carry the custodian cost basis
   beside it, labelled, in the lot tables; never use it in the identity.
3. **Unmapped value-moving types (10).** Map each cash type to its term: cash journals `$JNL` and `TOA/FC` are contributions or
   withdrawals by side; `FTP/FC/WD/DEBIT` is a withdrawal; `FEE/FC/FE/DEBIT` (fee-admin) and the withheld-tax debit are NEGATIVE components
   of `income`, each shown in an `income_breakdown` beside the term (so income is net of fees and withholding, labelled); `ADJ/IC` and
   `JNL/IC/JR/SHORT` follow rule 2 by side. A type you cannot place is a surprise row, not a guess.

The ROUNDING tolerance stays 0.05. The re-grade runs over the same 91 accounts. Add one test per rule. Criteria unchanged.
No gate limb graded this modification (LIMB 6 does not fire on a modification; GATE (viii) grades the unchanged `<placeholders>NONE</placeholders>`).

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a fix to the round-23 producer, which serves nothing yet; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB24-2-AC1 and AC2 base FAIL (no record); DB24-2-AC3 base PASS (23 tests, a bound); dry-run at base c2b4cbb412 2026-10-07 ~15:1xZ.
lane: the <paths> block IS the grant; it binds when the issuer flips this order from staged to issued at DB-b-36's drain.
</preflight>
