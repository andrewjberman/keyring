# TO IRPT_DASHBD.TO-DB-b-63 -- E1: adopt the two W39-S1 fixes (BD_FEE_FIELD_IS_FLOW, FIRST_DAY_FLOW_AT_START) in the reader of record; the 9,078 re-graded with >= 8,315 held; every IN-to-OUT named

<to_id>IRPT_DASHBD.TO-DB-b-63</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~40</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-32 ADDENDUM 1 @78928255f6 (on ADJUDICATION_v17), enrichment item E1 | **Decomp cell:** `DB-b-63` (decomposition section 35) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-61, DB-b-62 (merged @e72c6c354d, @d077f0f991).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-40`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~40/`.

**The cell (`DB-b-63`).** The reader of record is `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py`. It uses the daily-mean
fee base and flow-START with the 2% near-zero guard. Round 32 re-graded the 9,078 segments of round 18's
`deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json` with it to **8,315** within 0.35 pp, in
`deliverables/0.9.0_WK_IRPT_DASHBD~38/REGRADE_FLOWSTART_E2.json`. Round 32's DB-b-62 (`deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py`,
record `LARGE_FLOW_E3.json`) found two reader defects, and the CTO ruled to ADOPT both:
- **BD_FEE_FIELD_IS_FLOW** (26 segments; 23 tie under the fix): BD's `fees` field equals minus its net additions and the money gain is
  about zero, so the field is a flow, not a fee. Grade on BD's landed gain over the mean daily value instead of adding a fee back.
- **FIRST_DAY_FLOW_AT_START** (4 segments; 4 tie): a flow on the segment's first day is taken at START.

1. Fold both fixes into `tieout_reader.py`, ported from ~39's module (port the rule, cite ~39's lines; do not import from a worker
   deliverables folder). Each fix is gated by a predicate stated in the code. The fee-base writer census must stay at ONE file: the reader
   (names `daily_mean_value`, `mean_daily_value`, `fee_addback_v2`, `fee_base_gross`, `fee_base_daily_mean`).
2. Re-grade all 9,078 with the reader. Write `REGRADE_FIXES_E1.json`: `segments` [{account, segment, abs_diff_pp, verdict, reason}],
   `within`, `reader_sha256` (the reader's bytes at your commit), and `in_to_out`. `in_to_out` lists every segment WITHIN in round 32's
   `REGRADE_FLOWSTART_E2.json` and OUTSIDE here, each with a traced `reason`. Write `REGRADE_FIXES_E1.md` (COUNTS ONLY).
3. The ~35 and ~36 importers must still run unchanged. Re-run each and show their records do not change.

<criterion id="DB33-1-AC1" cell_refs="DB-b-63"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r33/p33_round33.py" . DB33-1-AC1</invocation><expect>DB33-1-AC1 PASS</expect></criterion>
`DB33-1-AC1` -- the 9,078 re-graded with both fixes, within >= 8,315 and equal to the tally; one fee-base writer; sha matches HEAD. Base: FAIL.

<criterion id="DB33-1-AC2" cell_refs="DB-b-63"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r33/p33_round33.py" . DB33-1-AC2</invocation><expect>DB33-1-AC2 PASS</expect></criterion>
`DB33-1-AC2` -- every segment that moves IN to OUT against round 32's flow-start re-grade is named, and nothing else. Base: FAIL.

<expected_criteria>DB33-1-AC1,DB33-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~40/
org/missions/D9/IRPT/IRPT_DASHBD/tieout/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-63.reader-fixes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 35 (round 33), cell `DB-b-63`.
<owned_cells>DB-b-63</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB33-1-AC1, DB33-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~40/IRPT_DASHBD.TO-DB-b-63.reader-fixes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB33-1-AC1,DB33-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the within count, the IN-to-OUT list by reason, the writer census, the importers' unchanged outputs, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a project-owned reconciliation reader and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB33-1-AC1/AC2 base FAIL at base beca8909cd (no record); positive control on a planted record PASS (floor 8,315 and in_to_out exercised).
lane: the <paths> block IS the grant.
</preflight>
