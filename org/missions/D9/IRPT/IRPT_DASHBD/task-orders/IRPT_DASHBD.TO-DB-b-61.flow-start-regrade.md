# TO IRPT_DASHBD.TO-DB-b-61 -- E2: flow-START adopted in the reader of record; the full 9,078 re-graded; every segment that moves IN to OUT named

<to_id>IRPT_DASHBD.TO-DB-b-61</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~38</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's rounds 30-31 analysis @fe8e06016b (msg 2007) on ADJUDICATION_v16, enrichment item E2 | **Decomp cell:** `DB-b-61` (decomposition section 34) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-60 (same worker, previous order).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-38`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~38/`.

**Sources (read only unless the grant names them):**
- round 18's record `deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json` (the 9,078 graded segments) and reader `tieout_e2_gross.py`;
- round 30's `deliverables/0.9.0_WK_IRPT_DASHBD~34/tieout_compound.py`;
- round 31's reader `deliverables/0.9.0_WK_IRPT_DASHBD~35/tieout_compound_v2.py`, with fee base `daily_mean_value` and `fee_addback_v2` (within 8,088), and its record `TIEOUT_COMPOUND_V2.json`;
- round 31's classifier `deliverables/0.9.0_WK_IRPT_DASHBD~36/unexplained_classes.py`, which has its own `mean_daily_value` and `fee_base_gross`, and its record `UNEXPLAINED_CLASSES_E2.json`;
- round 31's `deliverables/0.9.0_WK_IRPT_DASHBD~37/flow_timing_e3.py` (the flow-start re-link, 337 of 370 tie);
- the BD full-period pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`;
- the served gold `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/`.

A segment is keyed (account, segment.start, segment.end).

**The cell (`DB-b-61`).** Do this order AFTER DB-b-60 is complete; it changes the reader of record DB-b-60 created. The CTO ruled that
the tie-out reader adopts flow-START: a flow day's external flow is invested for that day. Round 31 measured 337 of 370 FLOW_TIMING misses
tie at flow-start, against 0 at the end-of-day convention. This is the reconciliation reader's convention only; served values do not
change.

1. In `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py`, set `FLOW_CONVENTION = "start"` and apply it in the daily re-link (reuse
   the method of round 31's `flow_timing_e3.py`; do not restate it if importing works). Keep the daily-mean fee base unchanged. Guard the
   near-zero divisor (round 31 row W37-S1: a flow of about -100% of the prior value) with a stated rule, never a silent fill.
2. Re-grade all 9,078. Write `REGRADE_FLOWSTART_E2.json`: `segments` [{account, segment, abs_diff_pp, verdict, reason}], `within`,
   `reader_sha256`, `files_read`, and `in_to_out`. `in_to_out` lists every segment WITHIN in DB-b-60's `REGRADE_E1.json` and OUTSIDE
   here, each with a traced `reason`. Write `REGRADE_FLOWSTART_E2.md` (COUNTS ONLY: within before/after, the in-to-out count by reason).
3. The within count is printed. The CTO expects at least 8,088 plus most of the 337, but no floor is graded: a lower number is reported
   as found.

<criterion id="DB32-2-AC1" cell_refs="DB-b-61"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . DB32-2-AC1</invocation><expect>DB32-2-AC1 PASS</expect></criterion>
`DB32-2-AC1` -- the reader declares flow-start; the re-grade covers 9,078 with within equal to the tally and the sha matching HEAD. Base: FAIL.

<criterion id="DB32-2-AC2" cell_refs="DB-b-61"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . DB32-2-AC2</invocation><expect>DB32-2-AC2 PASS</expect></criterion>
`DB32-2-AC2` -- every segment that moves IN to OUT against DB-b-60's re-grade is listed with a reason, and nothing else is. Base: FAIL.

<expected_criteria>DB32-2-AC1,DB32-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`. The tie-out reader is a reconciliation reader; the
  served producer is untouched (the CTO's ruling).
- **AWS:** S3 reads only. NO Black Diamond or vendor call, no secret read, no S3 write, no bun, no download of any package, script or
  program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, an edit outside the grant, a filled figure, or an account number, name or
  balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~38/
org/missions/D9/IRPT/IRPT_DASHBD/tieout/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-61.flow-start-regrade.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 34 (round 32), cell `DB-b-61`.
<owned_cells>DB-b-61</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB32-2-AC1, DB32-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~38/IRPT_DASHBD.TO-DB-b-61.flow-start-regrade.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB32-2-AC1,DB32-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, within before and after, the in-to-out list by reason, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a project-owned reconciliation reader and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB32-2-AC1/AC2 base FAIL at base 5992357355 (no reader, no record); positive control on planted records PASS (5 in-to-out named).
lane: the <paths> block IS the grant.
</preflight>
