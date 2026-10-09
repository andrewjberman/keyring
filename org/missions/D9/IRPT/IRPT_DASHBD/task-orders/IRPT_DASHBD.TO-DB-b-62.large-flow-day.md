# TO IRPT_DASHBD.TO-DB-b-62 -- E3: LARGE_FLOW_DAY (170) traced -- a cause per sub-class with counts; each fixed or carried as a named class

<to_id>IRPT_DASHBD.TO-DB-b-62</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~39</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's rounds 30-31 analysis @fe8e06016b (msg 2007) on ADJUDICATION_v16, enrichment item E3 | **Decomp cell:** `DB-b-62` (decomposition section 34) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-58 (merged @cc72b3f60d).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-39`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/`.

**Sources (read only unless the grant names them):**
- round 18's record `deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json` (the 9,078 graded segments) and reader `tieout_e2_gross.py`;
- round 30's `deliverables/0.9.0_WK_IRPT_DASHBD~34/tieout_compound.py`;
- round 31's reader `deliverables/0.9.0_WK_IRPT_DASHBD~35/tieout_compound_v2.py`, with fee base `daily_mean_value` and `fee_addback_v2` (within 8,088), and its record `TIEOUT_COMPOUND_V2.json`;
- round 31's classifier `deliverables/0.9.0_WK_IRPT_DASHBD~36/unexplained_classes.py`, which has its own `mean_daily_value` and `fee_base_gross`, and its record `UNEXPLAINED_CLASSES_E2.json`;
- round 31's `deliverables/0.9.0_WK_IRPT_DASHBD~37/flow_timing_e3.py` (the flow-start re-link, 337 of 370 tie);
- the BD full-period pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`;
- the served gold `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/`.

A segment is keyed (account, segment.start, segment.end).

**The cell (`DB-b-62`).** Round 31 named 170 of the 1,203 UNEXPLAINED misses LARGE_FLOW_DAY: a flow of at least 25% of the prior day's
value sets the segment's return, and BD's per-flow valuation is not in the landed period point. Trace them further.

**Population:** the rows of `deliverables/0.9.0_WK_IRPT_DASHBD~36/UNEXPLAINED_CLASSES_E2.json` with `cause_class == "LARGE_FLOW_DAY"`
(170). Take it from the record.

1. For each of the 170, find the sub-cause from the landed BD period point (beginning and ending value, net additions, fees) and Opal's
   served daily series around the flow day. Examples: an in-kind transfer valued differently, a flow on the segment's first or last day,
   a flow the other system books a day apart, a flow larger than the account. Give each a `sub_class` with `evidence`. Write `counts`.
2. For each sub_class, write `dispositions[sub_class]` {disposition: "fixed" | "named_cause", cause, note}. A fix lives in a NEW module
   in your folder and states its re-graded effect on the 170. It never edits the reader of record or the served producer.
3. Write `LARGE_FLOW_E3.json` (`rows` [{account, segment, sub_class, evidence}], `counts`, `dispositions`, `files_read`) and
   `LARGE_FLOW_E3.md` (COUNTS ONLY).

<criterion id="DB32-3-AC1" cell_refs="DB-b-62"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . DB32-3-AC1</invocation><expect>DB32-3-AC1 PASS</expect></criterion>
`DB32-3-AC1` -- the 170 each carry a traced sub_class; counts equal the tally. Base: FAIL.

<criterion id="DB32-3-AC2" cell_refs="DB-b-62"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . DB32-3-AC2</invocation><expect>DB32-3-AC2 PASS</expect></criterion>
`DB32-3-AC2` -- every sub_class is dispositioned fixed or named_cause, with its cause. Base: FAIL.

<expected_criteria>DB32-3-AC1,DB32-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`. The tie-out reader is a reconciliation reader; the
  served producer is untouched (the CTO's ruling).
- **AWS:** S3 reads only. NO Black Diamond or vendor call, no secret read, no S3 write, no bun, no download of any package, script or
  program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, an edit outside the grant, a filled figure, or an account number, name or
  balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-62.large-flow-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 34 (round 32), cell `DB-b-62`.
<owned_cells>DB-b-62</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB32-3-AC1, DB32-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/IRPT_DASHBD.TO-DB-b-62.large-flow-day.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB32-3-AC1,DB32-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the sub-classes with counts and dispositions, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a project-owned reconciliation reader and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB32-3-AC1/AC2 base FAIL at base 5992357355 (no record); positive control on planted records PASS (170).
lane: the <paths> block IS the grant.
</preflight>
