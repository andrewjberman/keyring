# TO IRPT_DASHBD.TO-DB-b-57 -- E1: the 181 segments that tied under the additive basis and miss under the compounded one -- one traced cause per segment, classed; a compounding defect fixed with the 7,459 held or raised

<to_id>IRPT_DASHBD.TO-DB-b-57</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~35</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-30 analysis @4cfe197b0c (msg 1965), enrichment item E1 | **Decomp cell:** `DB-b-57` (decomposition section 33) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-53 re-cut (merged @1698740c8d).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-35`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/`.

**Sources (read only):**
- round 18's additive record `deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json` and its reader `tieout_e2_gross.py`;
- round 30's compounded record `deliverables/0.9.0_WK_IRPT_DASHBD~34/TIEOUT_COMPOUND_E1.json` and its reader `tieout_compound.py`, where gross = (1+net)(1+fees/avg balance)-1. Each segment carries account, segment {start, end}, bd_return (net TWR), opal_return, opal_days, bd_days_held, bd_fees_reported, bd_fee_addback, bd_gross_return, abs_diff_pp, verdict, reason and evidence;
- the BD full-period pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`;
- the served gold `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/` (external_flow, income_received, total_return_daily, market_value_eod, day_quality).

Import the readers; do not restate them. A segment is keyed (account, segment.start, segment.end).

**The cell (`DB-b-57`).** Compounding the fee add-back raised the tie-out from 5,416 to 7,459 of 9,078 within 0.35 pp. But 181 segments
that were WITHIN under round 18's additive basis are OUTSIDE under the compounded one. Either they tied by coincidence before, or compounding
is wrong for a class of segment: for example a partial-period fee, a mid-period flow, or a short or closing holding.

**Population:** segments WITHIN in round 18's record and with `abs_diff_pp > 0.35` in the compounded record (181). Take it from the
records.

1. For each of the 181, trace the cause from the records and the landed files. Look at days held against days requested, fee size against
   balance, flows inside the segment, the additive against the compounded gross, and Opal's daily path. Give one `cause_class` per segment
   and the `evidence` that decided it. Write `counts` per class.
2. Judge each class: is it a COMPOUNDING DEFECT (the compounded formula is wrong for that class) or a coincidental additive tie? List the
   defect classes in `compounding_defect_classes`; the list may be empty.
3. If any class is a defect, fix it:
   - write `tieout_compound_v2.py` in your folder; it imports round 30's `tieout_compound.py` and overrides only what is wrong;
   - re-grade all 9,078 segments with it;
   - write `fix` {file, after_within}, where `after_within` must be >= 7,459.

   If no class is a defect, `fix` is null.
4. Write `CROSSOVER_E1.json` (`rows` [{account, segment, cause_class, evidence}], `counts`, `compounding_defect_classes`, `fix`,
   `files_read`) and `CROSSOVER_E1.md`. The `.md` holds COUNTS ONLY: no account number, name or balance.

<criterion id="DB31-1-AC1" cell_refs="DB-b-57"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py" . DB31-1-AC1</invocation><expect>DB31-1-AC1 PASS</expect></criterion>
`DB31-1-AC1` -- the 181 each carry one traced cause class; counts equal the tally. Base: FAIL.

<criterion id="DB31-1-AC2" cell_refs="DB-b-57"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py" . DB31-1-AC2</invocation><expect>DB31-1-AC2 PASS</expect></criterion>
`DB31-1-AC2` -- defect classes are listed; when any exists, a fix re-grades the full tie-out with within >= 7,459; when none, fix is null. Base: FAIL.

<expected_criteria>DB31-1-AC1,DB31-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Earlier rounds' scripts and records, the plan and the landed pulls are read, never edited. A fix
  lives in a NEW module in your folder that imports the reader it overrides.
- **AWS:** S3 reads only. NO Black Diamond or vendor call, no secret read, no S3 write, no bun, no download of any package, script or
  program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a filled figure, an edit to an earlier round's file, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-57.crossover-181.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 33 (round 31), cell `DB-b-57`.
<owned_cells>DB-b-57</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB31-1-AC1, DB31-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/IRPT_DASHBD.TO-DB-b-57.crossover-181.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB31-1-AC1,DB31-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the classes with counts, the defect judgment, the fix and its within count, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only analysis over landed records, pulls and the served gold; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB31-1-AC1/AC2 base FAIL (no record) at base 491339b7cb; positive control on planted records PASS (181; the defect-class + fix branch exercised).
lane: the <paths> block IS the grant.
</preflight>
