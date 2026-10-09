# TO IRPT_DASHBD.TO-DB-b-60 -- E1: tieout_compound_v2.py becomes the reader of record at org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py; one module computes the daily-mean fee base (writer count 1); the re-grade still reads 8,088

<to_id>IRPT_DASHBD.TO-DB-b-60</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~38</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's rounds 30-31 analysis @fe8e06016b (msg 2007) on ADJUDICATION_v16, enrichment item E1 | **Decomp cell:** `DB-b-60` (decomposition section 34) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-57 and DB-b-58 (merged @605c4cd4ac, @cc72b3f60d).

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

**The cell (`DB-b-60`).** Round 31 produced the daily-mean fee base twice, in ~35's reader and in ~36's classifier. They agree at 8,088
of 9,078 within 0.35 pp. The CTO ruled ~35's `tieout_compound_v2.py` the reader of record. Two homes for one rule is the defect. ISSUER
RULING: the project's tie-out code path is `org/missions/D9/IRPT/IRPT_DASHBD/tieout/`. It is project-owned, never served, and outside every
deploy lane.

1. Create `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py`, the reader of record: v2's grading plus the base it needs. Promote
   the logic rather than importing it from a worker deliverables folder. It may still import round 18's and round 30's readers for what
   v2 did not change. It defines the daily-mean fee base, keeping v2's names `daily_mean_value` and `fee_addback_v2`. Leave its
   `FLOW_CONVENTION` at the served end-of-day behaviour for now; DB-b-61 changes it.
2. **One writer.** Edit `deliverables/0.9.0_WK_IRPT_DASHBD~35/tieout_compound_v2.py` and
   `deliverables/0.9.0_WK_IRPT_DASHBD~36/unexplained_classes.py` so each IMPORTS its fee base from `tieout_reader.py` and no longer
   DEFINES `daily_mean_value`, `mean_daily_value`, `fee_addback_v2`, `fee_base_gross` or `fee_base_daily_mean`. Keep their outputs
   identical: re-run each and show that its record is unchanged (sha256 or the same counts).
3. Re-grade all 9,078 with the reader of record. Write `REGRADE_E1.json` (`segments` [{account, segment, abs_diff_pp, verdict,
   reason}], `within`, `reader_sha256` = sha256 of `tieout_reader.py`'s bytes at your commit, `files_read`) and `REGRADE_E1.md` (COUNTS
   ONLY).

<criterion id="DB32-1-AC1" cell_refs="DB-b-60"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . DB32-1-AC1</invocation><expect>DB32-1-AC1 PASS</expect></criterion>
`DB32-1-AC1` -- the reader of record exists and the writer census over the project tree is exactly that one file. Base: FAIL.

<criterion id="DB32-1-AC2" cell_refs="DB-b-60"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . DB32-1-AC2</invocation><expect>DB32-1-AC2 PASS</expect></criterion>
`DB32-1-AC2` -- the reader of record re-grades the 9,078 to within 8,088, and its sha matches HEAD. Base: FAIL.

<expected_criteria>DB32-1-AC1,DB32-1-AC2</expected_criteria>

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
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/tieout_compound_v2.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~36/unexplained_classes.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-60.reader-of-record.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 34 (round 32), cell `DB-b-60`.
<owned_cells>DB-b-60</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB32-1-AC1, DB32-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~38/IRPT_DASHBD.TO-DB-b-60.reader-of-record.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB32-1-AC1,DB32-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the writer census, the re-grade's within count, the two importers' unchanged outputs, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a project-owned reconciliation reader and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB32-1-AC1/AC2 base FAIL at base 5992357355 (the census reads 2 writers: ~35's v2 and ~36's classifier); positive control on a planted one-writer tree PASS.
lane: the <paths> block IS the grant.
</preflight>
