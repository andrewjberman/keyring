# TO IRPT_DASHBD.TO-DB-b-58 -- E2: the 1,203 UNEXPLAINED misses on the compounded basis -- every one classed by cause; the largest classes covering >= 80% named, each fixed or carried as a named cause

<to_id>IRPT_DASHBD.TO-DB-b-58</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~36</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-30 analysis @4cfe197b0c (msg 1965), enrichment item E2 | **Decomp cell:** `DB-b-58` (decomposition section 33) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-53 re-cut (merged @1698740c8d).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-36`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~36/`.

**Sources (read only):**
- round 18's additive record `deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json` and its reader `tieout_e2_gross.py`;
- round 30's compounded record `deliverables/0.9.0_WK_IRPT_DASHBD~34/TIEOUT_COMPOUND_E1.json` and its reader `tieout_compound.py`, where gross = (1+net)(1+fees/avg balance)-1. Each segment carries account, segment {start, end}, bd_return (net TWR), opal_return, opal_days, bd_days_held, bd_fees_reported, bd_fee_addback, bd_gross_return, abs_diff_pp, verdict, reason and evidence;
- the BD full-period pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`;
- the served gold `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/` (external_flow, income_received, total_return_daily, market_value_eod, day_quality).

Import the readers; do not restate them. A segment is keyed (account, segment.start, segment.end).

**The cell (`DB-b-58`).** After compounding, 1,619 of 9,078 segments miss 0.35 pp, and 1,203 of those carry round 18's catch-all reason
`UNEXPLAINED`. FWD-8 accepts a disagreement that carries a stated reason; this cell turns the catch-all into causes.

**Population:** compounded rows with `abs_diff_pp > 0.35` and `reason == "UNEXPLAINED"` (1,203). Take it from the record.

1. For each of the 1,203, find the cause from the records, the landed BD files and Opal's served daily series. Candidates include a flow BD
   and Opal date differently, income timing, a price gap, a fee basis residue, a segment-length artefact, and an account opened or closed
   inside the segment. Give one `cause_class` per segment with its `evidence`. Write `counts`.
2. Write `top_classes`: sort the classes by descending count and cut at the smallest prefix whose cumulative count reaches 80% of 1,203.
   The check recomputes this cut. Give each top class a `disposition`:
   - `fixed`: a correction in a NEW module in your folder, with its re-graded effect stated;
   - `named_cause`: the reason stated, so FWD-8 can accept it.
3. Write `UNEXPLAINED_CLASSES_E2.json` (`rows` [{account, segment, cause_class, evidence}], `counts`, `top_classes` [{class, disposition,
   count, note}], `files_read`) and `UNEXPLAINED_CLASSES_E2.md`. The `.md` holds COUNTS ONLY: no account number, name or balance.

<criterion id="DB31-2-AC1" cell_refs="DB-b-58"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py" . DB31-2-AC1</invocation><expect>DB31-2-AC1 PASS</expect></criterion>
`DB31-2-AC1` -- the 1,203 each carry one cause class; counts equal the tally. Base: FAIL.

<criterion id="DB31-2-AC2" cell_refs="DB-b-58"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py" . DB31-2-AC2</invocation><expect>DB31-2-AC2 PASS</expect></criterion>
`DB31-2-AC2` -- the top classes are the smallest prefix reaching 80% of 1,203, each fixed or a named cause. Base: FAIL.

<expected_criteria>DB31-2-AC1,DB31-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Earlier rounds' scripts and records, the plan and the landed pulls are read, never edited. A fix
  lives in a NEW module in your folder that imports the reader it overrides.
- **AWS:** S3 reads only. NO Black Diamond or vendor call, no secret read, no S3 write, no bun, no download of any package, script or
  program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a filled figure, an edit to an earlier round's file, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~36/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-58.unexplained-classes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 33 (round 31), cell `DB-b-58`.
<owned_cells>DB-b-58</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB31-2-AC1, DB31-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~36/IRPT_DASHBD.TO-DB-b-58.unexplained-classes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB31-2-AC1,DB31-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the classes with counts, the top classes and their dispositions, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only analysis over landed records, pulls and the served gold; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB31-2-AC1/AC2 base FAIL (no record) at base 491339b7cb; positive control on planted records PASS (1,203; the 80% prefix recomputed).
lane: the <paths> block IS the grant.
</preflight>
