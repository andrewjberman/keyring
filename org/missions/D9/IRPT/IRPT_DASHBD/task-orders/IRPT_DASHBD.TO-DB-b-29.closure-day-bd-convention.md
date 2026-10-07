# TO IRPT_DASHBD.TO-DB-b-29 -- E1': test Black Diamond's day count on Opal's side -- the 2,299 UNEXPLAINED segments spanning the 2025-01-09 closure, recomputed with that day held (FWD-8; zero vendor calls; the served figure never moves)

<to_id>IRPT_DASHBD.TO-DB-b-29</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~14</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-18 analysis @62026ca511 item E1 as
replaced by E1' in its ruling msg 308 ("Recompute Opal's own return for each of the 2,299 closure segments under BD's convention:
2025-01-09 counted as a held day, with any daily income accrual Opal's holdings would carry on it. Print the count that then lands within
0.35 pp, with its denominator. Opal's served figure does not change; this tests a hypothesis about BD.") | **Decomp cell:** `DB-b-29`
(decomposition section 19) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-27 (merged @0f304c6405).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-14`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~14/`.

**The cell (`DB-b-29`).** 2025-01-09 was an NYSE closure; Opal's calendar is right and Opal's served figure is not moved toward Black
Diamond's. Black Diamond counts that day as held (its `daysHeld` is exactly one more than Opal's linked days on these segments). Test the
hypothesis that this convention explains the gap: recompute Opal's return for each segment as if 2025-01-09 were a held day -- the
segment's linked daily returns plus one day for 2025-01-09 that carries the daily income accrual Opal's holdings would carry on it
(zero price return; the market was closed) -- and grade that figure against BD's GROSS figure at 0.35 pp.

**The set, defined exactly (the check re-derives it):** rows of
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json` with verdict OUTSIDE,
reason UNEXPLAINED, `bd_days_held - opal_days == 1`, and `start <= 2025-01-09 <= end`. There are 2,299.

**Inputs.** BD's side: that record's `bd_gross_return` (do not re-read BD). Opal's side: the served 49F daily series
`s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=<YYYY-MM-DD>/data.parquet`. The round-17 script
`deliverables/0.9.0_WK_IRPT_DASHBD~12/tieout_e2.py` already reads it (`read_gold`, `segment_days`). Find the income accrual from that
series's columns (the round-17 INCOME_DATE rule reads `income_return`); say in the record which column you used and why.

**THE FENCE (read first).** This box's AWS identity is denied on `opal-data-49financial` by its bucket policy. Never try to widen it.
Two phases:
1. Write `closure_align_e1p.py` (read-only: S3 `list_objects_v2`/`get_object` only, one local output file) and
   `tests/test_closure_align_e1p.py` (at least 4 offline tests on synthetic series, naming `2025-01-09`: a segment that lands within
   once the day is held; one that stays outside; a zero-accrual day; the counts reconciling). Make the tests pass. Commit both. Then file
   ONE row in the investigation file, class BLOCKING, hazard INERT, naming the exact command
   (`python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~14/closure_align_e1p.py" .`) and the output file, and
   STOP. The issuer relays it to the laptop and hands you the record as a FILE.
2. When handed the record: copy it into your folder byte-exact, run the three criteria, write and validate the proof, flip.

**The record `CLOSURE_ALIGN_E1P.json`:** `counts` {`denominator`, `within_bd_convention`, `outside_bd_convention`}, `inputs` (the GROSS
record, the gold prefix and partition count, the accrual column) and `rows`, one per segment:
`{account, segment, bd_gross_return, opal_return, opal_return_bd_convention, abs_diff_pp_bd_convention, verdict_bd_convention,
accrual_on_closure_day}`. `opal_return` is the served figure exactly as the GROSS record holds it. Write the recomputed figure ONLY under
`opal_return_bd_convention`. Write a summary `CLOSURE_ALIGN_E1P.md`, COUNTS ONLY.

<criterion id="DB19-1-AC1" cell_refs="DB-b-29"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_residue.py" . DB19-1-AC1</invocation><expect>DB19-1-AC1 PASS</expect></criterion>
`DB19-1-AC1` -- one row per closure segment with the three `*_bd_convention` fields; the within count is printed against the 2,299
denominator. Base: FAIL.

<criterion id="DB19-1-AC2" cell_refs="DB-b-29"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_residue.py" . DB19-1-AC2</invocation><expect>DB19-1-AC2 PASS</expect></criterion>
`DB19-1-AC2` -- no Opal served figure changes: every `opal_return` equals the GROSS record's, and the recomputation lives only in the
`*_bd_convention` keys. Base: FAIL.

<criterion id="DB19-1-AC3" cell_refs="DB-b-29"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r19/p19_residue.py" . DB19-1-AC3</invocation><expect>DB19-1-AC3 PASS</expect></criterion>
`DB19-1-AC3` -- the tests pass (at least 4, naming 2025-01-09). Base: FAIL.

<expected_criteria>DB19-1-AC1,DB19-1-AC2,DB19-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none from this box against `opal-data-49financial` (fenced). No vendor call, no write anywhere.
- **Refusal clause.** A changed served figure, a vendor call, an attempt to widen the fence, or a client figure in a committed `.md` is a
  defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~14/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-29.closure-day-bd-convention.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 19 (round 19, workstream B), cell `DB-b-29`.
<owned_cells>DB-b-29</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB19-1-AC1, DB19-1-AC2, DB19-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~14/IRPT_DASHBD.TO-DB-b-29.closure-day-bd-convention.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB19-1-AC1,DB19-1-AC2,DB19-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line (or "phase 1 stopped at the fence"), the row ids, and the exact command.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline recomputation; 0 served bytes move; no vendor call.
comp-iam: DECLARED-NOT-APPLICABLE -- the fenced read runs on the laptop under the standing rule; no grant asked.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB19-1-AC1, AC2 and AC3 base FAIL (no record, no tests), dry-run at base 75f9d2c37d 2026-10-07 ~10:2xZ.
lane: the <paths> block IS the grant.
</preflight>
