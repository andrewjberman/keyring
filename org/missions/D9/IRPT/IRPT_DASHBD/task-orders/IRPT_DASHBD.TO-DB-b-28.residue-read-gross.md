# TO IRPT_DASHBD.TO-DB-b-28 -- E2: read the residue of the gross re-grade -- the segments still UNEXPLAINED and the +1-day segments over the 2025-01-09 market closure (FWD-8; zero vendor calls)

<to_id>IRPT_DASHBD.TO-DB-b-28</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~13</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-15..17 analysis item E2
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUNDS_15_17_20261007.md` @e363a194ed, section 5 row E2) |
**Decomp cell:** `DB-b-28` (decomposition section 18) | **outcome_ref:** FWD-8 | **depends_on:** `DB-b-27` (its GROSS record; same
worker, same queue, handed on after DB-b-27 drains).

THIS CELL MAKES NO VENDOR CALL AND NO S3 READ. Its one input is the GROSS record DB-b-27 committed.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-13`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/`.

**The cell (`DB-b-28`), verbatim from the analysis:** "Read the residue. The segments still UNEXPLAINED after E1 (about 1,345 expected)
and the 3,395 +1-day segments over 2025-01-09: count each against the closed reason set with named evidence, plus the overlap of the
two sets." And: "a reason outside the closed set is filed as a surprise row, not added." The closed set is FLOW_TIMING,
MISSING_PRICE, INCOME_DATE, COVERAGE_DAYS, UNEXPLAINED. PRD ruling 23 (like day sets) stands: a +1-day segment is residue, never
agreement.

**The two sets, defined exactly (the check re-derives both from the GROSS record):**
- UNEXPLAINED = graded rows of `TIEOUT_49F_BD_POPULATION_E2_GROSS.json` with verdict OUTSIDE and reason UNEXPLAINED.
- PLUS_ONE_DAY = graded rows (verdict WITHIN or OUTSIDE) where `bd_days_held - opal_days == 1` and the segment's `start <=
  2025-01-09 <= end`.
- The denominator is the GROSS record's graded rows.

**What you build:**
1. `residue_e2_gross.py` in your folder. It reads the GROSS record and writes `RESIDUE_E2_GROSS.json` with:
   - `counts`: `denominator`, `unexplained`, `plus_one_day`, `overlap` (the intersection), and the residue count per reason;
   - `rows`: one row per segment in the union of the two sets, `{account, segment, sets: [...], reason, evidence}`. `reason` is from
     the closed set; `evidence` names what in the row or the BD response supports it (for a PLUS_ONE_DAY row at minimum the two day
     counts and the closure date). A segment you cannot explain stays UNEXPLAINED with evidence saying what was checked.
   - A pattern you believe needs a reason the set lacks: file ONE surprise row in the investigation file, keep the segments
     UNEXPLAINED, and name the row id in the summary.
2. `tests/test_residue_e2_gross.py`: at least 4 offline tests on synthetic records, naming `overlap`: a segment in both sets; a
   +1-day segment not spanning 2025-01-09 left out; an UNEXPLAINED segment kept with its evidence; the counts reconciling.
3. A summary `RESIDUE_E2_GROSS.md`, COUNTS ONLY (no client figure).
4. Run the script once; commit the script, tests, record and summary.

<criterion id="DB18-2-AC1" cell_refs="DB-b-28"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_gross.py" . DB18-2-AC1</invocation><expect>DB18-2-AC1 PASS</expect></criterion>
`DB18-2-AC1` -- the counts (denominator, unexplained, plus_one_day, overlap) equal those re-derived from the GROSS record. Base: FAIL.

<criterion id="DB18-2-AC2" cell_refs="DB-b-28"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_gross.py" . DB18-2-AC2</invocation><expect>DB18-2-AC2 PASS</expect></criterion>
`DB18-2-AC2` -- one row per segment of the union, each with a closed-set reason and non-empty evidence. Base: FAIL.

<criterion id="DB18-2-AC3" cell_refs="DB-b-28"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_gross.py" . DB18-2-AC3</invocation><expect>DB18-2-AC3 PASS</expect></criterion>
`DB18-2-AC3` -- the residue tests pass (at least 4, naming overlap). Base: FAIL.

<expected_criteria>DB18-2-AC1,DB18-2-AC2,DB18-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No vendor call.
- **Refusal clause.** A reason added to the closed set, or a client figure in a committed `.md`, is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-28.residue-read-gross.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 18 (round 18, workstream B), cell `DB-b-28`.
<owned_cells>DB-b-28</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB18-2-AC1, DB18-2-AC2, DB18-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/IRPT_DASHBD.TO-DB-b-28.residue-read-gross.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB18-2-AC1,DB18-2-AC2,DB18-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the four counts and the residue per reason, and any
row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline read of a committed record; 0 served bytes move.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB18-2-AC1, AC2 and AC3 base FAIL (no record, no tests), dry-run at base 3dd25927f2 2026-10-07 ~08:5xZ.
lane: the <paths> block IS the grant; it binds when the issuer flips this order from staged to issued at DB-b-27's drain.
</preflight>
