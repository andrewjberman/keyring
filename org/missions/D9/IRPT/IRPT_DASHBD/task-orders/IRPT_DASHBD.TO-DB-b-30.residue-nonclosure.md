# TO IRPT_DASHBD.TO-DB-b-30 -- E2: read the 980 UNEXPLAINED segments that do not span the 2025-01-09 closure, each against the closed reason set with named evidence (FWD-8; zero vendor calls)

<to_id>IRPT_DASHBD.TO-DB-b-30</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~15</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-18 analysis @62026ca511 item E2, cut now
over the non-closure segments by its ruling msg 308 ("(b) taken: cut E2 now over the ~980 non-closure segments") | **Decomp cell:**
`DB-b-30` (decomposition section 19) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-27 (merged @0f304c6405).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-15`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~15/`.

**The cell (`DB-b-30`), from the analysis:** "the segments still unexplained ... are counted against the closed reason set, each with
named evidence; a reason outside the set is filed as a surprise row, not added; the final UNEXPLAINED count and its share of 9,078 are
printed." The closed set is FLOW_TIMING, MISSING_PRICE, INCOME_DATE, COVERAGE_DAYS, UNEXPLAINED. A basis difference (the fee, the
closure day) is never a reason.

**The set, defined exactly (the check re-derives it):** rows of
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json` with verdict OUTSIDE and
reason UNEXPLAINED, EXCEPT those where `bd_days_held - opal_days == 1` and `start <= 2025-01-09 <= end`. There are 980. The denominator
for the share is the record's 9,078 graded rows.

**Inputs you may read from this box:** the GROSS record; the plan
`deliverables/0.9.0_WK_IRPT_DASHBD~6/BD_POPULATION_PLAN_E3.json`; the landed BD responses
`s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=<bd_account>.json` (readable here; they
hold each segment's Account-level point and Asset-level points with fees, market values, daysHeld and returns). Look for evidence the
round-17 rules did not use: BD's own market values, a BD asset-level point that alone carries the gap, a segment whose average value is
near zero (a small denominator magnifies any difference), and so on. Assign a closed-set reason only on evidence named in the row.

**THE FENCE.** This box is denied on `s3://opal-data-49financial` (the served Opal series). If your evidence needs it, write that part
read-only, test it offline, commit, file ONE BLOCKING row naming the exact command and output file, and STOP; the issuer relays it to the
laptop and hands you the result as a FILE. Never try to widen the fence.

**What you build:**
1. `residue_nonclosure_e2.py` in your folder, writing `RESIDUE_NONCLOSURE_E2.json`: `counts` {`denominator` (9,078), `nonclosure`
   (980), `per_reason` (summing to `nonclosure`), `final_unexplained`, `share_of_graded` (= final_unexplained / 9,078)}, and `rows`, one
   per segment, `{account, segment, reason, evidence}`. A pattern that needs a reason the set lacks: ONE surprise row, the segments stay
   UNEXPLAINED, the row id named in the summary.
2. `tests/test_residue_nonclosure_e2.py`: at least 4 offline tests on synthetic inputs, naming `nonclosure`.
3. A summary `RESIDUE_NONCLOSURE_E2.md`, COUNTS ONLY (no client figure).
4. Run once; commit script, tests, record and summary.

<criterion id="DB19-2-AC1" cell_refs="DB-b-30"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_residue.py" . DB19-2-AC1</invocation><expect>DB19-2-AC1 PASS</expect></criterion>
`DB19-2-AC1` -- the counts are re-derived from the GROSS record: denominator 9,078, nonclosure 980, per-reason summing to it, the final
UNEXPLAINED count and its share printed. Base: FAIL.

<criterion id="DB19-2-AC2" cell_refs="DB-b-30"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_residue.py" . DB19-2-AC2</invocation><expect>DB19-2-AC2 PASS</expect></criterion>
`DB19-2-AC2` -- one row per non-closure segment, each with a closed-set reason and non-empty evidence. Base: FAIL.

<criterion id="DB19-2-AC3" cell_refs="DB-b-30"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_residue.py" . DB19-2-AC3</invocation><expect>DB19-2-AC3 PASS</expect></criterion>
`DB19-2-AC3` -- the tests pass (at least 4, naming nonclosure). Base: FAIL.

<expected_criteria>DB19-2-AC1,DB19-2-AC2,DB19-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads of the bronze prefix only. No vendor call, no write.
- **Refusal clause.** A reason added to the closed set, a vendor call, an attempt to widen the fence, or a client figure in a committed
  `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~15/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-30.residue-nonclosure.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 19 (round 19, workstream B), cell `DB-b-30`.
<owned_cells>DB-b-30</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB19-2-AC1, DB19-2-AC2, DB19-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~15/IRPT_DASHBD.TO-DB-b-30.residue-nonclosure.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB19-2-AC1,DB19-2-AC2,DB19-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the counts and per-reason residue, the evidence kinds used, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline read of landed data; 0 served bytes move; no vendor call.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads of opal-data-assets only; a fenced read, if needed, runs on the laptop.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB19-2-AC1, AC2 and AC3 base FAIL (no record, no tests), dry-run at base 75f9d2c37d 2026-10-07 ~10:2xZ.
lane: the <paths> block IS the grant.
</preflight>
